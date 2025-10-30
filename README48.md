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
| d6c139f0-8dde-3a61-a8b3-126b4457ee8d | -11.0039 | -41.68083 | 2025-10-30 04:25:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c289474a-d300-3bc1-a71e-e90eef2cb16f | -10.85705 | -47.61731 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a296fc04-1bc8-39e0-adb5-5c3d033b123e | -8.25871 | -43.92881 | 2025-10-30 04:25:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e9dab64-679d-39f7-9221-ec17f70466e5 | -6.17638 | -41.61213 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a6df5ed-d7ec-3b6a-9b50-ebcfac1d1b6b | -10.918 | -47.81125 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 375144a1-eb48-31ac-ac59-2a03efedfcae | -11.11856 | -47.74693 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34d8924f-953b-32cb-a99d-8e5892017186 | -11.24 | -49.78136 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d22c6d3b-4d84-308d-9540-23068352eeda | -12.65836 | -41.26937 | 2025-10-30 04:25:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86f089ca-7c09-39a8-be35-a71bcec8f32f | -9.84301 | -44.88025 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 528ee2dc-840e-358d-8c2a-f214b8e58b54 | -5.57842 | -47.6174 | 2025-10-30 04:25:00 | NOAA-20 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ebb3f2e-7eb8-369a-a6f9-c65cd24b4409 | -9.31936 | -45.85738 | 2025-10-30 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 339ab659-c90a-39c2-8b03-a49e0be7e6f6 | -5.03735 | -43.61166 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 35334304-4a5a-36ee-a92a-eb711e35a0da | -11.06251 | -50.32585 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2b0ab735-36d2-362c-aed1-a7a68ff82b21 | -11.17022 | -45.22052 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ade9408c-acd2-3f54-91b1-48304a304876 | -7.59712 | -43.56847 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 749521b2-fea4-378e-b877-c8406ee47e1d | -6.10254 | -42.44292 | 2025-10-30 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 134f5881-c961-33fd-a64d-7a13d3fb7a2b | -6.18463 | -46.74015 | 2025-10-30 04:25:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb5ef9da-2a18-3dcd-b4de-11aff3f99530 | -5.58292 | -46.54875 | 2025-10-30 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3decc38f-55c5-38d6-bdb5-6ad4b244f965 | -6.14821 | -41.6687 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aeec9fdc-228c-3f26-9f77-c91956bf2f32 | -10.45165 | -44.31887 | 2025-10-30 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 26115d59-1823-35a0-9857-e3fd8e1f2578 | -5.77229 | -44.38744 | 2025-10-30 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18409408-8350-32e8-934f-bc8e36fdce0a | -3.52972 | -51.5759 | 2025-10-30 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42bd1a5e-4cc5-329b-9dd4-75b0958c5498 | -4.29884 | -48.06707 | 2025-10-30 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90a1f707-44ea-37da-8dfb-323e204f4b02 | -10.48712 | -45.0418 | 2025-10-30 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 29014fe4-7724-396a-86ce-d217b5638924 | -7.34665 | -47.63649 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7becd3f-e6dd-326f-ae21-f48c71cdb102 | -6.10546 | -51.21286 | 2025-10-30 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3ca7fbd-d0c5-37cb-9bf9-306640401576 | -10.39411 | -48.27983 | 2025-10-30 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4699f7f3-f686-384d-bd39-3843c2ecb6eb | -10.63112 | -44.68919 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ab09e17-12ea-3da4-916c-0f8c52228c89 | -7.64872 | -42.24557 | 2025-10-30 04:25:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 805a4b59-c80a-3727-8d5c-aba8fcd16478 | -5.7043 | -43.15683 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7ba29f35-541d-3116-9e47-355d3d91ce4d | -9.86955 | -47.69488 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63ddda06-84b0-33c7-ae35-fdc04ee3dbd5 | -5.29515 | -45.27134 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7eea6af0-08c4-3fa8-b22d-c44d9073a06f | -7.66091 | -43.91525 | 2025-10-30 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ce00fa6-5112-3ac6-8ccb-6fd7cb0a7aa3 | -9.85903 | -47.69675 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b4abd7e-227e-307b-8c93-53e21bd18c33 | -10.35695 | -48.70223 | 2025-10-30 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd35c7ea-266a-32a9-b6b5-a3f2816d16a3 | -11.69999 | -46.70724 | 2025-10-30 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9a947558-76ab-3f68-8e88-165b18a80970 | -8.04989 | -45.17871 | 2025-10-30 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97ce32a6-4435-3900-816a-67518902d2a4 | -5.8974 | -44.95997 | 2025-10-30 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66c2ea11-4750-3b2a-a09b-c98fb1097a5d | -11.38939 | -46.03698 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae35a7a9-8b8a-346f-af94-663f8a7b6c73 | -9.88545 | -47.44549 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0c289f8-33df-3329-a339-ade0a6d6bb25 | -6.12139 | -41.70689 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6ea50bff-9df1-334b-b505-ecc3ad6c1af3 | -5.72279 | -44.79559 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f952ac7f-6224-3c90-9f6b-abfabcbac198 | -7.95413 | -46.74543 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1b9a4c1-185d-37ef-bb03-c2921b5e4f50 | -9.90894 | -44.90532 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab1470cc-7d6d-3060-abe2-b26b3c2e946e | -9.23603 | -45.56719 | 2025-10-30 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03f2967b-49bf-3947-99f3-fb3945a5abf9 | -9.08874 | -47.90255 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4169d949-892d-36cf-9a87-30287bd41d05 | -8.17603 | -45.70074 | 2025-10-30 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb8238ff-9883-3fcf-81b3-f5852237e2ae | -6.10903 | -41.71006 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| be7bea73-fed2-3aa1-be07-068b0d112dc4 | -7.50022 | -46.73694 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1bae39f-2f75-3c65-b332-c997d5510476 | -10.98565 | -47.87634 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d969d60-cb75-3c36-9f05-29193c2b8a6c | -10.91413 | -47.81419 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bba0bf5-9ba7-3232-bac0-90d569af9a36 | -4.88466 | -44.35185 | 2025-10-30 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a807170-0cb1-318e-bf50-f042fab2cceb | -5.3773 | -47.20274 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61282950-2c88-3b89-a370-3da8b25fa9de | -5.75865 | -49.5018 | 2025-10-30 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f351ea4-16b8-3da4-8105-fdbd98ea604d | -5.81348 | -44.41257 | 2025-10-30 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bdddcc7-2ff9-3763-95fe-3f208f037669 | -6.13548 | -41.70164 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bd3f215f-cb67-3d34-a2a2-dba9ff3a9aaa | -7.7771 | -46.48971 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4d50f6d3-2f2c-30af-b3eb-70aed87f0c9f | -5.40061 | -49.42216 | 2025-10-30 04:25:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 940fe880-9e9f-3d17-829a-26aa762379d5 | -5.05993 | -45.32021 | 2025-10-30 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 608537b7-2aac-3fd6-9949-88772dbab82b | -7.34329 | -47.63601 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7423ed2a-72c9-3dd6-9a98-b870476c6564 | -7.54357 | -44.04619 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd5717eb-956a-36d9-b768-1ee2abd588f1 | -5.94377 | -42.62539 | 2025-10-30 04:25:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 43f63301-ee57-325a-a3e8-687115432029 | -11.1395 | -44.9386 | 2025-10-30 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be00f338-f34e-3b75-b33d-eb792d86ed5d | -5.1369 | -46.19049 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf90b480-7ee1-3f9b-b815-ba5fcc6a3f99 | -7.28222 | -45.6616 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e25030b-bf43-3cee-b762-9a2185cf9a2d | -7.00042 | -42.28828 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f697288e-4059-3bf1-b862-7bfe282b0900 | -6.29487 | -42.87638 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e223d6f7-0599-31b1-8879-3799746dc205 | -11.89122 | -44.35601 | 2025-10-30 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5a556cc-e15c-3644-9d65-970f793c94be | -4.95605 | -45.48452 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 001ba533-e523-34b0-bc2f-c93de12fee6b | -4.63079 | -45.06824 | 2025-10-30 04:25:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 494c7665-dbdf-307a-9e2e-f7b7fd12edb9 | -8.16573 | -45.48528 | 2025-10-30 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c625768e-48de-3510-88c4-793510e2ad52 | -10.88232 | -45.13534 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0fe586cb-97f5-3aac-bd41-21dd92ebc086 | -6.37125 | -44.57158 | 2025-10-30 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be0bfacd-9084-3d5c-a9b1-fd8c56610b64 | -7.79188 | -46.4175 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 4897579c-bf14-3292-abf4-71a2aa6b1f99 | -11.17823 | -45.21399 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 057851ac-82ef-34d4-b1a1-b6828e9a79a2 | -6.46388 | -41.64567 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9cad5bfc-5e8d-3206-84ad-1c5f72b74291 | -10.85528 | -50.13152 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c4fc802-74ed-3b38-964a-bcddff86fb7b | -7.01851 | -45.95846 | 2025-10-30 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41ed9c0c-d41d-3b40-be02-009496be367a | -10.61458 | -47.88116 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6765403-37b5-3eb4-b6fd-078ea9e96343 | -7.79849 | -46.41855 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1359be69-bf64-31c6-8b4f-15fec56e32a0 | -6.13478 | -41.70644 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fcc3e501-69f1-313d-9905-70ce70ac5ced | -7.22698 | -46.91716 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af4b7dc6-7a93-30b5-910b-261764ed9444 | -7.50473 | -47.05156 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa0b5580-d031-3a33-aa79-9e3ba6fe4a68 | -7.12474 | -47.00498 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53e1d825-a93c-3cb8-ba31-9c637ee29c45 | -10.48999 | -45.0461 | 2025-10-30 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e1d7f845-0290-3b25-a831-9f6f12d4f36e | -6.99209 | -46.23421 | 2025-10-30 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86f43384-e395-37fd-ba02-af51d921a7cf | -10.76592 | -47.61398 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 088be63a-0dbf-3dba-8d7c-c33bee316e57 | -11.86285 | -44.74045 | 2025-10-30 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8871617-97f8-30d1-807d-6d8b4ed97900 | -5.80363 | -40.83655 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7a451ac4-f72b-3f6d-bcda-d8448cb2fffc | -7.07641 | -44.47126 | 2025-10-30 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea5af99f-5f37-3e9c-8888-5ef104d95594 | -9.88886 | -44.87957 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0ce1d5a-9a67-3d2a-8da4-4357a57f5d3a | -4.58783 | -47.0775 | 2025-10-30 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94671835-657c-3389-9034-f46411309b16 | -4.25411 | -50.67127 | 2025-10-30 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 165f3b43-88d3-3078-a30a-4374adb1a4e2 | -6.70846 | -43.44687 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 995434e6-22fa-324c-ac8b-eb73aec084b0 | -7.37731 | -46.22408 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 146cd64e-517a-3928-95a0-2aff9e21f8e2 | -11.0388 | -47.8418 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6ff6e0c-853d-372b-944f-d8e39563b74c | -5.72622 | -44.50662 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59ca5470-a37c-3b89-a320-e9d3b7f95fa3 | -5.52256 | -41.2397 | 2025-10-30 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 09f4e227-1407-33af-90d5-888e92a74106 | -5.70632 | -43.13974 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5196a893-e4ec-3723-a9f5-92446c0b4596 | -7.01824 | -46.43311 | 2025-10-30 04:25:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README49.md)
