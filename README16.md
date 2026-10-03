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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25e36fb9-ac86-3d0c-a448-33b02b0a06de | -1.53194 | -47.5149 | 2026-10-03 03:53:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01851dd4-6962-37f6-a2cc-1225b1c4ee99 | -4.36075 | -47.77425 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b509dcd9-23fa-385b-b541-b436ef01bd9b | -4.45231 | -47.93182 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 336dffdf-9e77-3347-b34f-7c301a53bdb6 | -7.24028 | -45.25885 | 2026-10-03 03:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25c0a98d-56ed-3186-8acc-b853ee6dcc12 | -10.3679 | -39.87159 | 2026-10-03 03:55:00 | NOAA-20 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c2b68a97-8cd6-3403-a3ab-bcc138861bd0 | -5.74228 | -45.05514 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8e7f617-ebf5-3bab-af8c-f151505d9b49 | -5.75809 | -45.29552 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 018d7845-431c-3360-b9e4-5f6699e77c05 | -6.90086 | -43.68738 | 2026-10-03 03:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b62c9a63-aac7-3d64-b987-32179d55d284 | -13.38349 | -41.34799 | 2026-10-03 03:55:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 55f2254a-c05e-39b2-9ffc-43f25c76b608 | -5.61306 | -44.38438 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ab740dca-5235-3efc-9d72-ec66f1ebf39c | -11.47654 | -43.40322 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d462998-2b8a-3464-9f69-a9af0c064f14 | -5.55848 | -43.9632 | 2026-10-03 03:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8829a60c-dd5d-3a99-932d-214a030aad4f | -4.80498 | -49.87917 | 2026-10-03 03:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 644e8dc6-df10-3650-a0c2-455e6026eeaf | -5.73679 | -45.05702 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6164c72c-1d41-3257-8dec-c7671f469998 | -13.38418 | -41.34385 | 2026-10-03 03:55:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8670e9b6-93f1-313e-a868-d9dd12fca916 | -6.92603 | -49.63184 | 2026-10-03 03:55:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d1d9fb7e-3eb1-39da-b84a-de4c5ca935c2 | -11.48061 | -43.40396 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72d25c47-96ff-3377-8d8a-8d1412e62a18 | -11.8145 | -43.55103 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4e6326b3-aba6-3e78-a63a-b53adedb5318 | -6.88799 | -43.73616 | 2026-10-03 03:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e5b379f-b276-3e4e-98ba-52741e44c8b7 | -6.42128 | -45.86128 | 2026-10-03 03:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17230bbc-83f3-3ef9-a994-7042645917b9 | -5.73204 | -45.14375 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 048d2e40-fb09-3f38-869a-142e2bb2907d | -5.94475 | -43.6622 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| f95b764d-1e42-32f7-a32c-98fed523fa6f | -6.58925 | -43.49994 | 2026-10-03 03:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd3687a0-e0cd-34c1-aa4e-749a983b96f4 | -4.812 | -49.87971 | 2026-10-03 03:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 130ce48b-dfdb-3ef7-afb4-85e21322c4e3 | -5.7637 | -43.98548 | 2026-10-03 03:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afd16de6-18aa-3e31-b2d5-115470244423 | -12.97311 | -41.17831 | 2026-10-03 03:55:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b9ab52d7-f276-3d1d-b1f6-083ac384b5ba | -11.70659 | -43.63461 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 865c9eb4-8c6f-338a-82df-7d5203a876e9 | -9.45554 | -40.3737 | 2026-10-03 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 24.6 |
| b5416e4c-ada4-32f4-b934-498e6069b2e2 | -5.94148 | -43.65969 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| b140af02-fe6b-3478-b3ae-d73b659a17cd | -6.50045 | -41.75181 | 2026-10-03 03:55:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a834adf9-0928-35a1-a211-d3336f0f2de6 | -6.91876 | -44.56733 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b390770c-f339-3a5a-b96d-930009254a15 | -6.41604 | -45.8604 | 2026-10-03 03:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45480b18-3415-32bf-9f7f-a13d2d134c03 | -11.44125 | -43.38916 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| acfe03c8-6e73-39e1-92b4-cd7b58337dd9 | -5.8267 | -45.0133 | 2026-10-03 03:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddf93a41-09e8-3027-9f35-d4d1e66656dc | -9.72134 | -36.11001 | 2026-10-03 03:55:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0e1e5f6b-6614-3552-984c-d7912c31a030 | -4.40522 | -49.97524 | 2026-10-03 03:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 081e2bb4-357d-3d2d-a970-98ce6ebdd98a | -6.92397 | -49.63216 | 2026-10-03 03:55:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c7998cc5-7224-38f2-8285-92df04dcdc9a | -5.61732 | -44.38605 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5263d390-b22e-3def-ab85-c7b0e2a18fd3 | -6.92438 | -44.56314 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 367c7273-e28d-3e12-bd6a-af37a0737a30 | -9.72473 | -36.11054 | 2026-10-03 03:55:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.6 |
| e7ea4c2a-01d9-38f4-b7ea-96ea1baffa9d | -6.73719 | -44.14705 | 2026-10-03 03:55:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9673a35d-eb61-3c08-8437-0a5aae430d75 | -5.95217 | -43.65195 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b17e708-9e93-3d9a-a8a2-822ffb0af2b2 | -5.95007 | -43.65828 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d74ecfca-01e4-3c89-a160-979f70b6185d | -6.50133 | -41.74665 | 2026-10-03 03:55:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 83a017fd-3284-3c0a-b4b0-b48090ed4829 | -5.95752 | -43.64799 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7332a357-ac80-3c09-b8de-674498e9bff3 | -5.74515 | -45.15803 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9eaaad10-1cec-3ce7-aa8e-c6842ef182bd | -9.45268 | -40.36909 | 2026-10-03 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b521893a-1c19-3160-87bf-bb6815441946 | -5.95135 | -43.6566 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0311ee3-5dc6-3de8-a706-889f25900bba | -5.75169 | -45.15024 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe81e52f-978c-3dce-acc6-c65790542528 | -5.43475 | -43.44872 | 2026-10-03 03:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 726f9d94-3991-3b8e-a0b1-5b3fdc847f91 | -5.13202 | -45.58425 | 2026-10-03 03:55:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6708727e-8d36-39e7-9803-c28ce680e71d | -12.53634 | -43.07933 | 2026-10-03 03:55:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6ce4eb4f-de49-3f0e-9ece-1bf0cd26ac30 | -5.94631 | -43.65282 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c4a819b8-4651-3d3c-9459-8f1cfc16f1f7 | -5.19521 | -46.16737 | 2026-10-03 03:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51b6ec87-1661-3600-9947-0388eb2b5f95 | -9.72812 | -36.11106 | 2026-10-03 03:55:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.6 |
| 078e8997-f826-3faa-8378-2771dac81ecc | -12.95983 | -41.19262 | 2026-10-03 03:55:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e9af58e8-eb6a-3c7e-9cef-2ebc52bab4b4 | -5.61251 | -44.38531 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f2fea961-c2c0-38ce-9efe-212d510d13df | -5.94682 | -43.65584 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 84a6c440-566f-391c-b121-3f906c8c623a | -13.44889 | -41.32495 | 2026-10-03 03:55:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| be2cdab7-1e84-357c-bcf6-b14b58ead671 | -5.71579 | -46.20411 | 2026-10-03 03:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3acc2232-cb7f-38b7-8595-366b740113da | -12.86744 | -44.71852 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 46f905fc-ca22-3461-838d-89dc3c2b9f21 | -5.63534 | -44.36758 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c6f9412-2ddd-3a02-a3e5-52a1872481a1 | -9.45688 | -40.36569 | 2026-10-03 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| cf6b23e8-4649-318c-b3df-a665444a3a8e | -5.73709 | -45.1446 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c3505211-c202-3d08-950c-7505fc82588a | -5.74566 | -45.15509 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fe525d2-5975-3f9f-9384-bbdcbe13f76b | -5.73961 | -45.16 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0490cd7-ebc1-3ac5-8a8b-3a7bfbf53fd7 | -5.95671 | -43.65268 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 105344ac-873d-3da4-99ee-8687752b83f5 | -6.92505 | -49.62651 | 2026-10-03 03:55:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 61cb6861-616a-3aa4-8fc4-fb5fb5b43bf7 | -10.56777 | -36.86953 | 2026-10-03 03:55:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c2afcbab-6524-3b75-932a-8522556417e3 | -5.94851 | -43.6677 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| e46cdfcb-52cd-3e21-8f4c-4fd2770cfb67 | -5.74616 | -45.1522 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0a99f08-9104-3549-8b5e-da1aa7a442fe | -7.12656 | -41.33328 | 2026-10-03 03:55:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94e40c74-181a-3a3e-9aac-f3383e2b7cb1 | -5.95084 | -43.65361 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8469c9d9-6bba-3764-807a-997f3bebd337 | -5.73609 | -45.15033 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7043bbaa-044c-3dcf-83e6-633287833adb | -5.94397 | -43.6669 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| b4c367ed-cd27-3034-bc40-e2967cc3c3d1 | -11.79535 | -43.54005 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 40791733-6419-3ab0-b3d3-8a3378ca6c3b | -11.84641 | -41.27785 | 2026-10-03 03:55:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ca035314-20d0-3085-a6fd-0782a1005ccc | -5.93937 | -43.64502 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5a5ccffd-77af-3cc4-8003-ebe0850df937 | -11.70728 | -43.63081 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a024fa17-a23e-3acf-a37c-eb9c8146a7a1 | -5.74162 | -45.14841 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b5113b2-b7af-39e8-ac1f-17616f5e3781 | -9.13576 | -37.23511 | 2026-10-03 03:55:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4ccbddd2-bab9-3fee-98a1-304860cdc20b | -9.72868 | -36.1074 | 2026-10-03 03:55:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 51.5 |
| cc859b36-527f-38c6-b9f5-9dfabf285552 | -9.46394 | -40.36688 | 2026-10-03 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 52d5fdfe-9f67-3480-b413-60d07244804f | -12.85404 | -44.69392 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0828ae02-fcc1-359f-be51-b0372ea28baa | -12.85835 | -44.69479 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c43ceed8-b29c-38bb-b97c-da2e2c1ec229 | -11.79062 | -43.54299 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c24d2c1d-efa1-3743-9d09-4b718f960cad | -9.46327 | -40.37088 | 2026-10-03 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 070f1c48-7892-38dc-af86-262d30ca8ce7 | -6.88723 | -43.74068 | 2026-10-03 03:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac8d0911-7383-3e5d-a904-8286d34c97cb | -5.43025 | -43.44788 | 2026-10-03 03:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aeab9a93-04e9-3cc4-b9e4-7d6a41b87cec | -10.36576 | -39.49962 | 2026-10-03 03:55:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 359549e5-8efa-37f6-aa7b-61bca4b11ff4 | -12.86266 | -44.69565 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 74928e96-db31-3ff0-90e2-c883403e970c | -7.01265 | -43.42573 | 2026-10-03 03:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e640a10-cee9-3f49-8c6b-0c6557d01a95 | -5.94709 | -43.64815 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 349f8808-03f1-334a-aafb-fc34740e98e3 | -5.73759 | -45.14169 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e032383-12ca-3ac0-a442-54cb4e4ea0eb | -5.73659 | -45.14748 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 535df6c7-17d7-360f-aa3e-12d8f8e6ea17 | -11.84282 | -41.27723 | 2026-10-03 03:55:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 184f1526-5dd9-3670-a69c-7ebd445af1dd | -5.93857 | -43.6496 | 2026-10-03 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ecb03585-c029-387c-a77c-47334b64d198 | -12.85957 | -44.71258 | 2026-10-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b400655-6da8-384e-a2ba-29a84f849238 | -5.74212 | -45.14555 | 2026-10-03 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5638751d-d5a3-3e05-8c4b-10367be18702 | -11.48746 | -43.41278 | 2026-10-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README17.md)
