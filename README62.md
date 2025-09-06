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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef348246-3506-3c3b-b60a-3daf534e9d6e | -7.42938 | -49.46764 | 2025-09-06 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4710c00e-1d96-3e7e-8607-d000f581c641 | -4.32742 | -48.39425 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ffb8d06-974f-3187-9518-4eb147b342e8 | -7.60173 | -43.86889 | 2025-09-06 04:38:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7ebe851-bc80-39dd-8c64-7478b531c3bb | -3.24551 | -50.80919 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d8d9162-0111-3e2b-bca4-7d7acab311dd | -3.74946 | -44.37333 | 2025-09-06 04:38:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66869802-8708-350c-95a7-c2f3748e0939 | -6.22812 | -45.12913 | 2025-09-06 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5224787f-b759-3381-8dd1-866c6c797209 | -6.06892 | -43.30068 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d6f6fe55-2972-34b5-ac3d-bca93bd94e34 | -6.59105 | -44.55015 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fab7fed4-6cf3-36ab-94b6-e726bad58933 | -5.72634 | -43.90736 | 2025-09-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b44071e-8086-31aa-99f6-3ccd0f9aa239 | -5.38255 | -45.96683 | 2025-09-06 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71c72e8b-e084-37a8-adb0-5b640f6a11e8 | -3.67865 | -49.02007 | 2025-09-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e6ce16b-077a-3266-829e-88f6347c1bad | -8.54652 | -55.24269 | 2025-09-06 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 424335c6-7165-388a-82ca-f0fa927c44e4 | -6.84064 | -52.84314 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f5f586a-8df7-3e45-8429-b53349937e88 | -6.06165 | -43.33894 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ad60b54b-8060-359b-9a13-5f9a094922c2 | -6.50674 | -43.0656 | 2025-09-06 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2e4ffad-6c8f-3118-a086-dea679c563cc | -5.94684 | -42.96062 | 2025-09-06 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1af53dfc-0c4c-3b42-8867-c3e7f18f2839 | -6.49529 | -44.21115 | 2025-09-06 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7c50391-da6d-30c5-b7e8-1452601d1f24 | -7.05831 | -50.86553 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b76d4b43-e5f5-3403-8fe3-aa1ef6efb9a0 | -6.183 | -53.26231 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22d931a2-d8e6-3552-b5d7-4abc450f3829 | -6.73371 | -51.96484 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bf6c453-4b76-3055-927f-1d666cab686a | -6.82373 | -52.80991 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 709e9ff5-acf6-3058-be12-0c3fea1bcbd1 | -6.2775 | -53.44011 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b210f931-78dc-33e9-acc3-e9afb1d3dc58 | -8.33825 | -52.52518 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02a8f269-290b-37d9-aef3-88d2ef27f1f6 | -6.26564 | -43.49499 | 2025-09-06 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85ff1758-9fe4-3285-b4bb-f0d0719da415 | -6.06782 | -43.29769 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 62aaec50-40c2-3a7f-a82c-21239a3ecadf | -7.30097 | -43.73249 | 2025-09-06 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0219b0ab-5f0d-3037-9877-d0fea0a72208 | -5.8714 | -46.04371 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19670165-57d1-3476-a581-4b78a0c933ac | -8.36289 | -48.27766 | 2025-09-06 04:38:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 26fcce4e-87a6-3323-abd9-537928b28f96 | -4.86618 | -50.82618 | 2025-09-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba9d1702-d213-3927-a1e9-ca48a1d1e8af | -7.04846 | -44.34912 | 2025-09-06 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5bdc8a2e-ec59-31f9-bb60-433603365c33 | -5.90121 | -57.72469 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65251c3a-08b7-3ce4-9210-129f1052a736 | -2.65433 | -48.79541 | 2025-09-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 831e7d9f-706f-3db9-a533-e9e01fa1475d | -5.98437 | -53.59928 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfbae08a-a0b2-3249-bd10-f3da08f7024c | -5.98023 | -44.72672 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 404b8309-b872-3bb2-9e77-93de0d3f7cf2 | -5.87998 | -46.03637 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adce0573-d403-3fa6-aa47-6dfa78cf3db8 | -6.63167 | -53.15547 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5158176-71b7-3754-b3f1-41429f09ecf4 | -8.4315 | -47.31415 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5ea0797-cbe0-3ac0-9ea5-157d48e2fc37 | -6.22425 | -45.12865 | 2025-09-06 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67de02b7-4880-3aa2-a068-81785c41f598 | -6.27674 | -53.44471 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 931a066d-7ab5-3509-9b1a-802933b69813 | -6.24469 | -43.2911 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 247f6292-1ad2-341d-94ef-0261a9ac30e6 | -5.86181 | -57.77176 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45d34d1f-c5b5-3190-9c0b-37751dfffd29 | -7.69086 | -50.28408 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7283a286-a8ab-3a4b-97ef-496e51dc103f | -5.69515 | -53.75008 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8fec68b-cf24-3712-b75b-fcb82e23bfd7 | -5.77964 | -49.93338 | 2025-09-06 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54f0c50d-4207-3d26-b18e-7e61dfd8a3b2 | -9.17743 | -46.02851 | 2025-09-06 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ff2f533-7c1e-3eaf-9117-cb04000e6889 | -5.85574 | -57.77663 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bf07259-d92e-3e0e-b15a-11001295690f | -5.65646 | -43.62096 | 2025-09-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9b4f3f2-1db9-3675-a932-c008541f4659 | -6.60648 | -43.97118 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06216976-1155-3b92-865e-8b4a7923c21c | -5.742 | -42.76084 | 2025-09-06 04:38:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a89489d-3c84-37ac-96c6-a4b8d230c8a4 | -6.00077 | -44.1567 | 2025-09-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 635a0089-0fa2-36ea-9a97-93aeb7db07d1 | -6.21694 | -43.36001 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83c67d24-ada7-3dce-8c93-2eccf0f6c7b8 | -7.34723 | -43.95551 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a0dc81a-f06e-3858-93d2-9b404285aa44 | -8.49213 | -45.09982 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39ed6ac3-0a63-3685-852f-6e873a827b53 | -9.08509 | -47.00605 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2d75ff9-79e4-3e94-808d-0fb24d0ee882 | -6.15943 | -53.68795 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 451c8535-4219-3456-9b9c-73838ee347d3 | -6.39152 | -43.82005 | 2025-09-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74882234-13ff-3de8-a293-c32c2f9f10ba | -5.98054 | -53.59867 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b846ad6-ebdb-312c-ae76-360ea596f983 | -6.63094 | -53.15987 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b91b2a6f-0ba6-3774-9912-0b16e97da0ea | -3.42977 | -49.0477 | 2025-09-06 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10bf9bbc-d4ba-3c64-89f3-ad1dfedab600 | -2.73945 | -48.68542 | 2025-09-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a11022bd-5ad9-3a60-8e99-e0ec9a0c044f | -4.50515 | -42.8922 | 2025-09-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61ae6854-683a-349e-bc64-ed2ee0db541f | -4.89834 | -41.75813 | 2025-09-06 04:38:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 666bae88-2ae2-3139-aaa5-dac4be389655 | -6.81148 | -52.81651 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5619bf14-ba58-3a12-8349-5756c8bf6e99 | -3.68089 | -52.18596 | 2025-09-06 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f85d051-787f-3871-8c7d-926c4c5c8d91 | -9.30679 | -45.41221 | 2025-09-06 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2fd23e1f-90de-3c6d-83fe-3450ba1d75cc | -7.42745 | -44.93474 | 2025-09-06 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 079f232e-de18-3eb6-a373-b6b6a2a89ba5 | -8.77835 | -49.63452 | 2025-09-06 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2773fb9d-69a7-382f-abd3-dd176ba02254 | -7.34297 | -43.95511 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bedd325d-d265-3b66-89d6-d92e325d64d1 | -6.16601 | -43.1825 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1320c483-9599-3a28-acd9-353a799edcdc | -7.67871 | -50.29634 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e91b5e6d-8424-34d1-9fcb-b5d77fc5ff8e | -8.43655 | -45.03377 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff023764-2f12-376e-b9d3-009022c2694d | -6.24153 | -43.2823 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52913696-e9e4-30ee-a859-dde64fa436ab | -6.5119 | -42.41991 | 2025-09-06 04:38:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 460884f1-373e-3800-967e-987e42610dfc | -5.97671 | -53.59802 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1644ae7c-4a1f-3e74-b49a-7112468cef4a | -5.87374 | -46.05269 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8f10927-e57e-3810-bcd5-fa5471f8463d | -6.17926 | -53.26165 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f9e9229-39de-3d03-9772-61f32c1ae772 | -5.63028 | -43.65277 | 2025-09-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4c1e795-8b59-3c2e-944e-3071d93a1822 | -3.16105 | -49.48054 | 2025-09-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87072098-98e1-3044-a5ed-8a966a49dc38 | -7.73221 | -50.32323 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc48c9a7-cdf8-346b-bb80-1b9cbedd43b4 | -6.08568 | -43.30719 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7bcee587-e1c7-3f8b-8389-ba1bb8127e25 | -5.86543 | -46.03411 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7e3ec18-e42f-36fc-b329-a8696af50f5b | -8.88336 | -47.91352 | 2025-09-06 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd89fc17-b903-379b-a9d7-376e2e74093d | -6.39767 | -46.09761 | 2025-09-06 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9443f76-6b92-3fab-bfb0-6a00de771a5e | -5.86961 | -46.10355 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4307dff-1dd6-3dc8-90ce-56c550622a3e | -6.86543 | -52.7822 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c121ff0d-2035-3779-9dac-b868bc91831b | -7.2075 | -46.2025 | 2025-09-06 04:38:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 486fe09d-7856-3338-b587-ed38526a2f21 | -8.08684 | -45.32454 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6e48ec11-b75c-32c3-aaab-3282a80b6632 | -2.91463 | -48.67392 | 2025-09-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9818722-1f1c-3a50-8041-ff7d1d180db4 | -6.53433 | -49.4996 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f1eb3e8-81b3-3eb1-9c0f-7b648afdf71d | -7.0337 | -49.30568 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 376667a6-5ba9-3863-9354-e48222dbb9bb | -5.9574 | -44.74674 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ccc3df3-b83a-3b57-ab64-6a49b210b9be | -3.24207 | -50.80863 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41229bc7-cda7-39c5-9727-97a19ede1190 | -6.51114 | -43.06647 | 2025-09-06 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19914142-fa67-3b4f-bfbd-5e61d73d4b20 | -6.28128 | -53.44076 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12c43896-1e3b-3500-bad8-4981c68fe5ec | -7.30301 | -43.7298 | 2025-09-06 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c53702cb-9623-3941-bd27-a5c5467bb346 | -3.24954 | -50.80599 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94260bb6-9556-39b6-b737-a21ae60032d7 | -6.53932 | -49.51102 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12c19c7a-92ae-3167-a224-4042c7b54b69 | -5.87175 | -52.16309 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfc22926-f1bf-30dd-ba33-38ff4784268e | -5.97211 | -53.6021 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e76e08f-2728-339b-9cc5-f6a406bdf9f5 | -9.29354 | -50.26653 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README63.md)
