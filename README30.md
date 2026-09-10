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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d03c886-2a53-3252-844d-99555d9fbe63 | -3.37099 | -59.43238 | 2026-09-10 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e91e963-ca6b-3443-a406-316fd4ef20f6 | -5.11687 | -46.00952 | 2026-09-10 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a1caab9-81e8-30cd-bac5-bb01e8bad2c4 | -5.7602 | -45.08242 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 69b5090e-7dc7-3702-983b-b1611fcc4980 | 0.24919 | -51.46156 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34c5ada0-ab9e-3d47-a91a-82c11133203f | -5.48196 | -45.12753 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41efc934-1a4a-36ba-9912-682d858aaba1 | -7.51439 | -45.27036 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4463d8c-6021-315a-8030-2f8521940255 | -3.3681 | -59.42792 | 2026-09-10 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9eed826a-b205-3b20-a927-21085e6baa66 | -3.37477 | -50.40238 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9109074d-b523-3eac-8acf-750c0bce04f5 | -5.7725 | -45.08456 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| d9559e44-3689-350a-880d-3fde79a69543 | -3.962 | -59.36003 | 2026-09-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4170b89e-148f-3589-a98a-a4e2e1993bab | -2.73265 | -57.63017 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26048c15-1cdc-3df2-87ac-ba8292dcbac8 | 0.25626 | -51.45301 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8a8b31ef-7163-31cf-932a-e54fbb35fa9c | -3.54845 | -48.18568 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef10911c-06ea-35e5-99ca-2309f3527dcd | -5.28348 | -55.96666 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f62142d0-0ca0-3236-a88b-21fb8b7be4a8 | -2.94027 | -50.47806 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9905fdae-d518-3c1f-b2f1-3e4cf326309d | -6.24927 | -51.68157 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94bcb10d-9c4d-36e7-96ad-971a545e0279 | -3.25045 | -47.24854 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab2a3c73-33a1-3c31-ac4f-9db97dc7aa6a | -4.19124 | -59.95538 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c8a5257-ca07-3da1-8ca5-3d11de8a87c9 | -2.7343 | -57.61969 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2eaa8ab0-d45d-3c4b-8558-da56c75d86b7 | -4.82855 | -55.76971 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d2eb2b1-3fdb-38eb-8b51-6871ad73720b | -3.98614 | -56.09275 | 2026-09-10 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 960a8873-e716-3eeb-b452-fa1a6aded46e | -5.77324 | -45.07896 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 730aa85c-0af0-326c-a322-c10e0bbe1c5c | -3.43457 | -59.25564 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a27d6dee-fa76-3713-944e-811c2555157f | -3.0856 | -51.39537 | 2026-09-10 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 251ac43d-0ff2-3bea-8b7b-77dce998ff2b | -3.05951 | -59.26968 | 2026-09-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a54c6c9-65d1-3a11-accb-c8e5ab2aa768 | -3.36872 | -59.42402 | 2026-09-10 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c99ce196-6fcd-323f-86bd-ec18c97aef66 | -2.94089 | -50.47383 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3b51377-f70e-395e-9760-84885e03dca7 | -4.179 | -55.36816 | 2026-09-10 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e5d8eed-1ed7-3a61-a76e-ae019de8c9ed | -6.24983 | -51.67761 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0df06a5f-bd02-3a08-b77b-9eb778989587 | -2.39742 | -57.88031 | 2026-09-10 05:10:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7865ce06-d3c5-3414-bb30-60261fc2ffdc | -2.93933 | -50.4804 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a20c222-c9b8-3736-bcd5-0f6f7356b1d7 | -4.82573 | -55.76564 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f31b8dbe-f739-3c6b-b406-4fbc12b5239e | -4.83583 | -55.76718 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05d00d23-071d-3039-b30a-25a8b3011557 | -2.72319 | -57.60367 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12d0fd0b-10d7-3a3d-9f51-731be58fb93a | -1.47714 | -47.27357 | 2026-09-10 05:10:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90c58d7c-e7fc-394b-ab1b-bbbea642f530 | -2.94808 | -50.48181 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13ede0ec-a86d-3837-a5cc-57d75e2a1390 | -3.49724 | -59.57298 | 2026-09-10 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 143a050f-95f7-3c55-a3bd-4787afb72337 | -1.03249 | -53.73795 | 2026-09-10 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 700655e1-08a4-36c8-87c4-fdbe498bf4fb | -2.94465 | -50.47874 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d473f6b-0dca-337d-a993-a5ae85d472d7 | -3.49662 | -59.57693 | 2026-09-10 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7587202-caf4-3ce2-9f10-52903d7164c7 | -6.10773 | -51.73474 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdcdeb20-2bd0-3c52-a801-8b649d341cb8 | -3.43866 | -59.25233 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ecfdb1a-5901-30a8-9138-f43266de5cd7 | -5.76674 | -45.07769 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1fb57676-c435-30fd-9e6b-bc6fb2c46c70 | -2.945 | -50.47267 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 171389ad-e5fb-3d42-be62-fb5979dc265a | -2.92083 | -54.11115 | 2026-09-10 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f20d3c1e-d096-38a9-a258-0d7c274dfbdb | -2.94061 | -50.47202 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2455cbfb-471e-3d3b-ba61-34caeb0ce3be | -2.82724 | -49.22815 | 2026-09-10 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 983b15cd-90e5-3f82-87fa-f7858829a456 | -3.53832 | -58.94985 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ac0daa9-d359-31e4-bc87-50a86229e37a | -3.59172 | -59.07693 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9524441b-4c26-368a-baa7-20d7618e8458 | -5.76456 | -45.09412 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| cd9c9555-20f1-314b-aef4-dda311883b8a | -2.94565 | -50.46843 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4aa484c2-f904-30f5-a726-4509329aea71 | -5.766 | -45.08328 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| d31dfc58-02f9-3700-8f5e-21239eb6977e | -5.76527 | -45.0888 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 72dd0e9a-1e0c-39ea-b306-da361167dfaa | -6.09422 | -44.13815 | 2026-09-10 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1c5f94e-84fa-3a3b-84af-3b7f273c4ff1 | -3.37161 | -59.42847 | 2026-09-10 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca984e67-4905-3050-8f33-6f142e703a6d | -4.82628 | -55.76207 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 84e667b7-7d3b-3ba5-bf2c-e1d08e837eac | -3.35633 | -59.43411 | 2026-09-10 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6103230-593b-34cc-b156-6e366c5c9735 | -6.10113 | -44.13943 | 2026-09-10 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54d875c2-3593-3108-8091-fc7c43928bfb | -4.49561 | -55.49832 | 2026-09-10 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3aef195f-62e1-3187-b43e-9dba7c817cd1 | -1.09875 | -48.0564 | 2026-09-10 05:10:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69fc6166-55c7-30cb-96c6-132aeccef2a9 | -5.77167 | -45.09572 | 2026-09-10 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 174db524-a0c1-3a82-86a1-244af143c6cb | -4.20899 | -59.99867 | 2026-09-10 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea3ded4c-e033-3d71-a7bd-6c7e0bd26824 | -6.76114 | -45.47478 | 2026-09-10 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8eb43ffa-1dd1-3a29-b1e5-15b9e548e99c | -3.65872 | -58.89942 | 2026-09-10 05:10:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbb18abb-553a-3fe3-ade4-f5d719a26b84 | -3.5489 | -48.18262 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fb9abae-5a97-3b05-9aeb-e8ce643e2e86 | -3.24993 | -47.25211 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 861a2237-7334-387b-861f-f26c6336a4c9 | -2.11036 | -54.38131 | 2026-09-10 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e88560c-c154-32d4-909a-12e0fafd01e2 | -2.94336 | -50.45689 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b47f98e-eac7-3cce-b374-d0c15a71e8cf | -1.03725 | -53.73058 | 2026-09-10 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f1c49ca-fbea-3d08-b9ad-64f6c62c5b92 | -6.10196 | -44.13811 | 2026-09-10 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c93eda36-82c4-3642-a2f9-c5a2d70baca3 | -3.19835 | -51.01956 | 2026-09-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ead58965-6f26-3dae-ad17-cbe8a9c34979 | -2.73042 | -57.62267 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3b6759ae-8dcd-3e71-a797-abf9c7ce2949 | -2.94743 | -50.48598 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9574066-9893-3c6f-a137-67efad1efef4 | -3.96488 | -59.36441 | 2026-09-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6013768d-365f-3524-a03a-d26e6b72b8c8 | -3.24496 | -47.24769 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1b6c16d6-2671-39c0-98ab-b035a0f056ce | -3.96008 | -49.01424 | 2026-09-10 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6df3c0a7-16dc-30e2-9137-f2520332d2fa | -1.70429 | -55.02553 | 2026-09-10 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03215113-5db1-3c31-9ace-020e72253490 | -4.38021 | -59.4906 | 2026-09-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d21675c-34a4-3ad5-b4ec-95dd97e49d90 | -3.47959 | -60.00411 | 2026-09-10 05:10:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb6ad2cc-71ce-391d-b1b9-f13305c88e1a | -3.25003 | -47.91201 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff602802-e710-37ef-94e6-377482086556 | -3.06589 | -59.27465 | 2026-09-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5ae171a-860a-39cf-8170-a800cd706a87 | -6.10297 | -51.73789 | 2026-09-10 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc716927-6779-35dc-a433-56a18f82788a | -4.83246 | -55.76666 | 2026-09-10 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14be850d-fbab-3243-8892-eca80fbac146 | -7.48899 | -45.27205 | 2026-09-10 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cd0df360-fab9-3f98-b189-2c05fc788350 | -2.94343 | -50.48712 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f14e4e46-293f-35ba-9a41-66fcdeaa6325 | -2.93773 | -50.46471 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cef823cc-54ed-3a53-b7d6-a0d39e8504de | -2.93752 | -50.46291 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2178eb32-c47e-35a5-b965-0857a65460fc | -5.37894 | -54.44943 | 2026-09-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8668c2f-2969-3945-a6ae-9dd225080c03 | 0.24922 | -51.45918 | 2026-09-10 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8a2dcc68-c346-3b9f-8cc9-b641c1022f61 | -2.73503 | -60.06262 | 2026-09-10 05:10:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8764337d-f761-3fbc-a76b-0bd1e1b65ea6 | -3.24924 | -50.82247 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afe9e159-096a-3ac3-883b-4fdc5974e9fa | -4.03646 | -50.885 | 2026-09-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92b84bd0-8052-3c0b-8625-74a95e8c08ec | -2.94781 | -50.48782 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 533259ae-5204-3167-8ac0-f42b4c2a0613 | -3.24444 | -47.25124 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 00343ca9-a0d8-3a3e-ab17-f86d87b3fd3d | -2.72932 | -57.62965 | 2026-09-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 908ecf20-61c1-3dd7-8bd8-96796a53ea28 | -3.55499 | -48.17724 | 2026-09-10 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76bcdb2f-306f-3eea-967c-de6d98582e8a | -2.9415 | -50.46961 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c5eefb4-9e61-317e-8be4-72a5ee35bfb3 | -3.49717 | -59.57617 | 2026-09-10 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f1626e5c-677d-35df-a4e1-421949943634 | -2.94527 | -50.4745 | 2026-09-10 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c49fd79-fcf1-3bd7-a8f5-1edc7ba2c074 | -3.66835 | -53.74333 | 2026-09-10 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README31.md)
