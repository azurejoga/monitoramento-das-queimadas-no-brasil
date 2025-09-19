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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49cbc1df-f96a-3564-9507-62b297af4b2d | -6.99986 | -44.63599 | 2025-09-19 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af83c585-3a11-3aa9-8e84-6842ac4ac726 | -5.98671 | -45.73277 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2405890d-bb28-3803-8a5c-41b348174a53 | -7.60941 | -45.26975 | 2025-09-19 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 698acb9b-6c9f-3da3-9e40-b457dda99c36 | -5.12586 | -47.83384 | 2025-09-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d6154180-2d6a-3f4d-919d-89ab09ad7138 | -7.57958 | -45.47185 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d88f574c-d290-314a-9b68-fb74b309af66 | -5.98264 | -44.14991 | 2025-09-19 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a19ba9e5-6d32-3185-84a8-57751d13682f | -9.14584 | -44.85255 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69176885-7b15-3a89-af0e-b23ba93f43f3 | -9.0297 | -44.97083 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d5c6d8d-0c67-3066-a523-0270a9240d84 | -9.17587 | -45.32355 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e078bf1-240a-31c3-8b1f-1148dc1c3563 | -5.20584 | -45.17993 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af5623a7-43c3-3eb2-893b-df7cfc68d881 | -8.30751 | -44.65488 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 900293a2-7bc1-310f-a187-46bdf77d6808 | -4.69951 | -41.96027 | 2025-09-19 03:53:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 761565d7-2809-30d4-bc3c-4ea47c942722 | -3.27534 | -49.14693 | 2025-09-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97848c14-8eb2-3891-afb2-68a687e50cf9 | -5.77639 | -43.90142 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56c9295d-d395-3698-9a2e-cb6ff5ce5543 | -7.57421 | -45.47584 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71ac2ab8-aa63-31e5-89f6-919280c1cc79 | -9.16861 | -45.31345 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67ba08c3-c947-3822-a969-10d428ff83b2 | -7.24065 | -39.23437 | 2025-09-19 03:53:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 74f21e78-2173-36d7-a98b-73e503cb8b31 | -7.57627 | -45.49129 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e85c9c48-6961-3d87-8c72-cfacbba01491 | -5.79763 | -45.71758 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d572767d-4248-3ad7-8b2a-053df2859e7f | -7.38372 | -44.2981 | 2025-09-19 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56dabece-4e8e-3b5a-8dba-34fabc802a29 | -5.89061 | -45.86045 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 849904f2-0ec2-36fc-86fd-3440709ad092 | -7.23732 | -39.23384 | 2025-09-19 03:53:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 638cf893-d4e9-3291-a4bf-88e08511506d | -7.99319 | -43.93734 | 2025-09-19 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a885bbf-67fd-326e-b7c6-d5bef7f89c17 | -9.02468 | -44.97418 | 2025-09-19 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85de9a00-1202-3109-8f76-4b022a40b28e | -9.18327 | -45.30724 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b8d463e-1bd5-358b-aa8c-87d5afd919ab | -7.32267 | -46.61168 | 2025-09-19 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1264da73-9079-3118-93a7-bbb719876f2e | -3.2807 | -49.15294 | 2025-09-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a64b7966-f2ae-335b-8f8a-69cc787dcff0 | -8.68995 | -46.44885 | 2025-09-19 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8be1dc46-f4f9-3cf5-a954-9fad6e70a0c9 | -5.45741 | -46.68346 | 2025-09-19 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3a7994f-38f5-3f0a-bc15-522ada0111f6 | -7.87303 | -45.62693 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2928a350-bda9-3e7f-b19d-d7f5d7d59a4c | -6.32654 | -42.39554 | 2025-09-19 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8a2528ec-2619-3940-a0ca-2cd791cfcd8c | -8.1532 | -46.77904 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe716dff-34d2-3907-a82b-bcc69f0eb304 | -6.83113 | -41.04302 | 2025-09-19 03:53:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 876aff49-933c-362f-aafb-8d24c56205c1 | -9.02609 | -44.89061 | 2025-09-19 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 518f8ade-6956-332a-a053-21625e615614 | -5.13143 | -47.83481 | 2025-09-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 53df7a26-0637-3e5d-8784-7adace29f7b2 | -8.13942 | -44.47286 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 784d7021-7da0-3fff-b896-6db070f60ae8 | -6.08 | -37.46432 | 2025-09-19 03:53:00 | NOAA-20 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2c0267c-1857-38dd-87b5-6d8fb928b1c1 | -7.36086 | -44.58364 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75ffd992-2d5c-3965-b3ac-baac8a88046d | -8.06628 | -44.09352 | 2025-09-19 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 549efb68-5362-3c86-8506-95c3e0318b38 | -7.28957 | -43.92932 | 2025-09-19 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da222cf1-4d24-3eae-8145-32b7b4dd5432 | -6.95921 | -44.7654 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0d95a974-84c1-3667-9a16-67009c151ce2 | -5.7975 | -43.90482 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a74cd1bd-6adf-350e-8b58-71eb22fca662 | -6.85912 | -44.16891 | 2025-09-19 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35069948-c213-3b89-907e-eefec1c3249a | -7.00856 | -44.63739 | 2025-09-19 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a37efe2a-fabd-3275-82e9-7494a032953a | -3.69924 | -49.57822 | 2025-09-19 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66769330-8366-3771-971e-e2123a24e29c | -9.18101 | -45.32007 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f03edf59-b558-300e-9654-c42023e380f9 | -8.55442 | -47.54959 | 2025-09-19 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ba81f13-6123-340e-abf7-9d9e8ac4cf79 | -6.19006 | -41.19583 | 2025-09-19 03:53:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4284dfae-62f6-3219-a779-7e5640b1dca4 | -7.28553 | -44.13894 | 2025-09-19 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5e20a62-1d8e-3e3b-bb32-ac6c5f58e08e | -6.8512 | -45.21609 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de23d8bb-267f-3b7a-a6aa-b6dbb64691de | -9.33594 | -44.53299 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ab44d249-1591-36b3-a3b8-e3131011e934 | -5.77331 | -45.97991 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af782306-d875-3642-81a8-32aaeb11e013 | -8.4888 | -44.73415 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4553baac-85ea-3900-a0b3-dc8b982a827e | -7.24674 | -39.23893 | 2025-09-19 03:53:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f158e4df-19b3-31af-aab8-71f7fe79d69b | -5.76118 | -43.38853 | 2025-09-19 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ab51a3c-75ec-3293-9e77-344fa95023a0 | -7.30916 | -44.05195 | 2025-09-19 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| daf5b3d2-6d96-3201-8edc-dc1c55f24fa7 | -9.20884 | -40.24905 | 2025-09-19 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dcf1db1a-a1ad-3f56-89c1-7f639e5fa2ed | -7.57222 | -44.48835 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4eff5660-9ec1-3003-a5cc-d01fd229203f | -5.45465 | -36.51268 | 2025-09-19 03:53:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e3a5f17-26d0-3875-8c4a-eaffe6111889 | -5.6887 | -45.32392 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f80223c-32c7-3eae-a974-9095f7020d22 | -9.16861 | -44.89816 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd520c7c-9ef5-39c3-a029-7f740c79662e | -4.77663 | -42.7522 | 2025-09-19 03:53:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3460eda-f941-36bd-9d61-4b81a49f3bac | -7.01294 | -44.63795 | 2025-09-19 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 644ea571-8cd3-3437-8e0b-94470aeb82ac | -7.55481 | -44.74307 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eba4342-de4a-3317-9509-886bad07c3d3 | -7.2264 | -46.60156 | 2025-09-19 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1815541d-5e9d-3bfa-892b-a2947546c098 | -6.99264 | -44.62611 | 2025-09-19 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e863336b-42ee-3817-8adb-d6b19c4e6b97 | -7.38437 | -44.29435 | 2025-09-19 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 224062e7-688c-3dba-95bf-d37f6360d817 | -5.3406 | -46.143 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b7e49a08-ba5c-38a1-8057-d60d44bf57d7 | -5.8032 | -45.37159 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fe5c01d-e576-3089-b133-0dc1851b1a8a | -3.69381 | -49.57183 | 2025-09-19 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37245672-535d-3a4a-8bbd-7cabd8588ba7 | -9.16362 | -44.90157 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a6c685c-7e11-3d26-a9d1-77a491c0cf8d | -9.15369 | -44.6595 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05617ff2-5dda-3f7f-a619-eac98d0ff1fd | -4.69572 | -41.95968 | 2025-09-19 03:53:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 25a802fc-140e-30cd-80a3-5e2e286e2eff | -4.78143 | -42.74773 | 2025-09-19 03:53:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50bd6480-4b48-3d8c-8829-d0eb7532a1a2 | -7.35506 | -44.59161 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ef8e974-5cbe-33b5-b2a5-3773cc4e8b15 | -5.92321 | -45.08271 | 2025-09-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 00b07fe2-23f9-3e5d-befc-a53477f97644 | -9.17185 | -44.65467 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e33b08b-2494-339b-b26f-2e9a83ef2920 | -7.83774 | -45.63993 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ee050070-d9ce-32ed-a134-abb1714b48ce | -9.16832 | -44.65012 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21aaaec0-813e-39da-821f-a17ffa775385 | -5.63447 | -43.89494 | 2025-09-19 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1033151d-ffb7-333e-99cc-e12ac4cf2afb | -6.89948 | -44.77146 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 02b7a88f-beec-31b9-9864-7500da7698dd | -7.58327 | -45.47969 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de033391-3ee9-3a50-9968-dd56426a12b1 | -8.34067 | -44.64044 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a948d419-7bea-3d2c-ab86-e706f732cd16 | -8.13359 | -46.77499 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e607a189-0993-37d7-b176-f3fa135921e8 | -9.05669 | -44.86648 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f82f170-949f-3796-8395-d6e81687e064 | -5.83129 | -46.28235 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acd5b28e-62a8-3d8e-b792-eb8ecd3a4716 | -9.03032 | -44.89163 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ee33e64-049a-3b0d-8281-4e2aef500fce | -7.57447 | -44.78487 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e7fd05d-1931-326d-a7b6-a935e2b7fca3 | -7.84629 | -45.61792 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3375205a-2d88-3e3b-b646-8038aec727f9 | -7.25495 | -39.3157 | 2025-09-19 03:53:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dcaaf5b1-7e1b-32a5-aac1-d801fa9eceb1 | -7.31332 | -44.05267 | 2025-09-19 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b64f933-f9c2-317a-b8fe-7f5784c1f5b7 | -8.04966 | -44.07673 | 2025-09-19 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c57a69f-8b50-3a31-9f12-1e33a1baaa69 | -7.18078 | -44.34297 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e14474e8-48f7-3255-9f2a-f3160d5eb20b | -3.70015 | -49.57301 | 2025-09-19 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6a90f75-4284-3a70-908e-0993b8d01685 | -7.70549 | -44.3963 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 216c9fc8-eaee-3f35-b2bb-803efddd45dc | -8.14345 | -46.77674 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6fc3f38f-26c0-397d-a446-1e69d179b5f9 | -7.55049 | -44.74223 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4284ba0e-e1a8-3b24-b9a2-88c4f7d5b2a1 | -8.6313 | -45.71096 | 2025-09-19 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97b03b56-4ecb-37eb-b7ac-bbfd38565ff0 | -6.39196 | -42.84924 | 2025-09-19 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e7e82e49-43f4-3279-80d9-8dc89942dc10 | -4.70026 | -41.9556 | 2025-09-19 03:53:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README12.md)
