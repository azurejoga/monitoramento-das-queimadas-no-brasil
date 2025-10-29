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
| e1817075-3f47-35d0-8e60-669a66af6feb | -7.36507 | -47.63672 | 2025-10-29 03:53:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f773009f-bbef-35b0-bc0e-ea68e82c6efb | -6.09952 | -39.66204 | 2025-10-29 03:53:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c191314-13db-317a-9ed2-897eb531600f | -5.19034 | -44.35605 | 2025-10-29 03:53:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32ad8a4c-f35d-32fd-bf1b-b543fbda75aa | -7.93106 | -45.51235 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1083c6ea-f35d-3349-b2c5-50245790440d | -7.98787 | -45.53655 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 32e95a1c-c58e-38d0-bec3-d29fb9f68077 | -6.85982 | -43.44507 | 2025-10-29 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eafbf8af-1890-3810-b9e5-60d8c98935b3 | -6.28641 | -47.87867 | 2025-10-29 03:53:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c3baff9-91ef-3a45-a3ea-7d7c40e6e125 | -6.2275 | -37.42278 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5e05e7a7-20a3-3c80-b313-117d47ec4052 | -6.56389 | -38.73273 | 2025-10-29 03:53:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 203a477f-2223-3bb5-938c-ac633dbf462d | -6.1526 | -41.81454 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eda5a68c-8c6c-39cf-8345-4a1029911722 | -7.78827 | -46.48156 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 15bd5536-53ea-37f8-befa-c0f510b54ded | -5.54469 | -41.2788 | 2025-10-29 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 772dba98-7989-304f-9ea6-64556bd443c1 | -6.09347 | -41.78199 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| dbd531b0-85d2-32f2-8305-a8242b963022 | -4.08624 | -46.93574 | 2025-10-29 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d1e2af83-9194-3754-adfd-33110097a119 | -3.81211 | -48.65702 | 2025-10-29 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ef923ee-ab8a-3334-9d30-a3374325c8a7 | -7.60757 | -43.57609 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cceb9c54-e461-3e47-833c-7f83cf76c5c0 | -7.30393 | -44.98866 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8aa2b25f-1e85-3558-ad6e-a25d38a4fba6 | -7.67041 | -45.94832 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b43b106e-5688-3d00-ab07-2ea2b98e033c | -6.08783 | -42.1459 | 2025-10-29 03:53:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cf63f530-fe20-3ff4-ad31-c7f1503cf9c0 | -4.92887 | -44.56057 | 2025-10-29 03:53:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 00ac04e6-5fad-3b00-b294-bb851a2ef207 | -6.65163 | -43.6109 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 05c80d34-db09-341b-aec0-06022aca348b | -7.44493 | -46.61285 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fe7b8358-bc94-30e1-a32a-8e833d50d9c8 | -4.48527 | -43.43867 | 2025-10-29 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 999552d3-fd60-37c8-83c0-3ad03c7682d2 | -7.70182 | -46.90861 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff19c7be-72df-3867-8bbd-efe68f4ee780 | -7.37294 | -42.44022 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 19e5059c-5487-3005-9d5d-9e4d4947bf55 | -6.28086 | -47.87805 | 2025-10-29 03:53:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7465555d-36b0-3b7f-81f5-b06a05fc13a6 | -5.57353 | -46.52977 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8220b39-d104-317a-9cc0-a5bad711b752 | -5.05504 | -44.53833 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 056c10b3-e6e8-3fac-9931-7c3175f1dd4a | -6.56397 | -41.5913 | 2025-10-29 03:53:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5aad7c1-da05-37cd-8b53-e2a66a9f1948 | -8.0333 | -47.41361 | 2025-10-29 03:53:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ebdd5ae4-3586-3b16-bca5-f86b6e596149 | -3.81595 | -48.6575 | 2025-10-29 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d01610c4-bc55-3368-8bb8-53fd3c431baf | -5.17085 | -45.64542 | 2025-10-29 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95259948-4a14-3698-aeec-04effa474772 | -6.18995 | -41.58312 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 07bd5bec-7b60-37ff-86a9-58fd6bf2a77e | -7.61439 | -43.58458 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0a808401-8b00-3761-a4c1-7a9113aab315 | -4.48108 | -43.43804 | 2025-10-29 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a743b4a0-ca90-3824-a4e4-dcf37c54bb50 | -6.46868 | -42.24185 | 2025-10-29 03:53:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bd1f4eef-2a5a-38a3-a629-379f019277b9 | -5.57714 | -46.52872 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1899f3c9-7d99-399d-b500-e78f66e04280 | -4.21564 | -44.24049 | 2025-10-29 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8cc12c2-4520-3b4a-9b67-85ae0565dd22 | -8.55876 | -45.7015 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 380b90f5-d724-3060-babd-163fda11825c | -5.63808 | -41.53684 | 2025-10-29 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 05de5156-37d9-3bc4-a527-e1d9ca99c120 | -6.15011 | -41.57329 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 54694520-359e-3ff7-824d-51279c2a2dc0 | -8.03275 | -47.41666 | 2025-10-29 03:53:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2d364f3-7df2-38e5-adca-d7f19e7a5a69 | -4.76259 | -43.57084 | 2025-10-29 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9273c9e-afd0-37c5-af13-c5c18253705e | -7.50358 | -46.74758 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1d7f220-55d5-3616-a83c-0cbc8151bc8e | -5.85771 | -47.70085 | 2025-10-29 03:53:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59d1ed79-2c28-3e0f-948b-8920078e7518 | -5.85834 | -47.69722 | 2025-10-29 03:53:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6706f377-a5e9-3286-bc9c-7d4f63ac6561 | -6.13576 | -41.70804 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 39a391c3-b36f-38b1-9e6d-0f58beb0c6bb | -4.72612 | -46.81767 | 2025-10-29 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b850d09-5b8a-37cd-a2c8-26004fe9ef4c | -5.65283 | -46.45326 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96fbec47-8ecc-3c08-998a-b915ee87c055 | -6.27238 | -42.08836 | 2025-10-29 03:53:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dffcb726-4419-3a3f-9498-c107652d5f7a | -6.14296 | -41.68681 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| cb750db9-b47e-3699-ad71-43ea354ec825 | -6.27872 | -42.88099 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1663314e-977d-3c9a-a47b-c5739927fbc5 | -7.06994 | -44.95273 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58cd9484-b477-3c51-95cd-0878cce9a5de | -2.42039 | -49.29821 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a810c01d-faca-3748-953f-fbda1b32fcfb | -6.23126 | -42.53066 | 2025-10-29 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3fec8a65-386b-3280-9bea-1a7e1482aeb8 | -3.24166 | -48.77621 | 2025-10-29 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b845130-6dad-38d1-8371-8d669106cd8e | -2.42588 | -49.30449 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2b455fb6-3dfe-3ae0-9acd-5425da6bc6af | -5.41051 | -45.21922 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed1d4324-8a4a-3fd6-9bb9-5e90dff8f623 | -6.67054 | -42.67437 | 2025-10-29 03:53:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 09f430f7-510e-3fe5-ad05-40fa3f6f3f01 | -4.85761 | -45.7746 | 2025-10-29 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 449e5509-162b-3cf5-a004-d49b3701aad6 | -5.62319 | -44.01257 | 2025-10-29 03:53:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 467819e5-9a4a-3915-8d28-61570a7974d3 | -8.64066 | -44.77209 | 2025-10-29 03:53:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e70c2a05-aeb8-3442-a4fc-6a2d0b2b51f1 | -6.11266 | -42.44547 | 2025-10-29 03:53:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a231d4be-c4ec-3f24-ad57-34316f590930 | -7.79895 | -46.47803 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a633856-7345-30ac-ae4c-63800b397490 | -8.5452 | -45.69654 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e8ab9a4-c038-3cdf-8291-7f692c0554df | -6.36288 | -44.18769 | 2025-10-29 03:53:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c323a850-b1fb-3283-a934-168b69aba182 | -7.70738 | -46.90652 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b9a5ef2-082a-3663-8fcb-f3b95fa51be2 | -4.91897 | -47.32339 | 2025-10-29 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 00f5caee-d076-3f67-a458-068dbd191602 | -4.6591 | -46.57656 | 2025-10-29 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 571844c6-f63c-3e30-a571-ee17314b1493 | -7.34997 | -43.90684 | 2025-10-29 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f90bcc89-e301-3d95-85e8-a340a7920c6b | -7.49337 | -47.03823 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40e48939-de3f-3dec-9a1e-4a22ff935d86 | -7.08046 | -44.94488 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c092db33-98ef-33ad-9ed4-ede237690915 | -4.52821 | -46.04218 | 2025-10-29 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 678a88ee-fb7a-383e-b1ad-5f19978a5a94 | -4.47092 | -43.70716 | 2025-10-29 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c266f2d-351b-3c08-b12e-ab2015a3be55 | -6.1351 | -41.85263 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e1cc6cbe-7b5b-3b1c-9567-947ef70e7d32 | -3.60226 | -48.99069 | 2025-10-29 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cde010aa-59e2-3e53-bf69-0005a8b9429b | -7.07385 | -44.93014 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 09433041-2301-3cf9-b22b-457849e5d549 | -6.13505 | -41.71243 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a3d01018-655a-3044-bd96-9ed0b9b69bec | -4.35172 | -43.63929 | 2025-10-29 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0efc1817-9629-3dd2-8343-60ec39652a22 | -7.10049 | -44.09278 | 2025-10-29 03:53:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbe2de4f-b48a-3798-88e4-0f7d00911ea4 | -5.8026 | -42.57261 | 2025-10-29 03:53:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 956fc38f-c2e7-3dd1-b6b9-4bfad75de242 | -8.45733 | -40.75447 | 2025-10-29 03:53:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0d73fa39-217b-318e-a7ca-bd14ba3b0056 | -2.83166 | -49.39698 | 2025-10-29 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bfefcd4-9c49-3768-a328-f1e2648335fb | -8.50706 | -40.53281 | 2025-10-29 03:53:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 743cfe0e-870b-3a9a-9922-74f35fc27fc9 | -8.03386 | -47.41055 | 2025-10-29 03:53:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 045e0f24-8401-3190-9244-2c5a8b6267ef | -7.34507 | -42.46615 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 528eb2cb-cc83-33c5-8f38-f49c24e9076e | -4.20853 | -50.09252 | 2025-10-29 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| f5d45e72-ce8e-3382-9b9f-98f10635e2b6 | -6.30171 | -41.88619 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 3982cff2-00fe-38ab-b9dc-07f8e0832366 | -7.92802 | -45.49932 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0077f668-9bb2-3ae6-8b8c-691e8fffe067 | -4.70246 | -46.10723 | 2025-10-29 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 593d0e4e-572c-352e-a3a9-3b355d7d2f24 | -8.54589 | -45.69448 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44266601-2c0f-39db-8640-e53fedd9adc0 | -4.01401 | -43.23753 | 2025-10-29 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7277d345-5259-324e-8ed9-f52dc44d7bdd | -6.65582 | -41.5364 | 2025-10-29 03:53:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ddd17ba7-7c97-320e-8220-dc258c30ae37 | -6.9958 | -42.78748 | 2025-10-29 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a969894a-f426-3f1c-afdc-878b4d582fd5 | -5.97467 | -46.32058 | 2025-10-29 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d459117-f4bc-3fea-85c0-36fbdb417ee3 | -2.43228 | -49.30554 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9b309b9e-14d4-327d-ab01-37380c04aa6e | -2.42387 | -49.30553 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2d8ff9af-8e84-3106-9edc-99ad7da8d6bc | -7.336 | -42.47422 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8779ba3b-e6f8-3692-af97-d241cab3c256 | -5.41132 | -45.21441 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a17ea34a-e7c6-36b1-ac73-5b261784c7cf | -4.75778 | -46.97789 | 2025-10-29 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README7.md)
