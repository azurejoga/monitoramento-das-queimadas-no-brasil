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

## Dados Diários - Página 410

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6129aca6-30ba-37d2-bc56-374c179795a9 | -9.9205 | -44.8124 | 2026-10-08 19:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 59b92474-131d-3d4f-aa3f-6679850a2c0e | -6.2348 | -52.7866 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| a3d69f11-636c-3a4d-bf3c-894ffd360a82 | -2.7428 | -54.1146 | 2026-10-08 19:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 252.2 |
| 14599f85-4402-3bde-ab16-08e7e05cd5b4 | -2.8346 | -54.1326 | 2026-10-08 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 2e74eb05-c231-372b-b741-af0de6f51d15 | -9.8817 | -44.8632 | 2026-10-08 19:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9be41a1c-1d5d-3dd8-85b6-74a9ecc9352d | -3.0256 | -57.7768 | 2026-10-08 19:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f11ff0fe-07c4-3c75-b103-08846fc12bc8 | 1.6937 | -55.6263 | 2026-10-08 19:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 35c155d4-b96c-357a-aaf6-de219f6d7e0d | -5.0946 | -46.206 | 2026-10-08 19:40:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 9133f642-a922-35fb-9a7a-df127dd3c0d7 | -2.0834 | -46.5765 | 2026-10-08 19:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| f3a3ef9c-9e3c-36da-9ac1-a4792eec6f97 | -2.8228 | -58.361 | 2026-10-08 19:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 85753fcb-4312-3cac-9088-5080812b94f0 | -6.5129 | -55.3784 | 2026-10-08 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| cfc0aace-0dc4-3224-abc6-9750551e00b6 | -7.3284 | -45.2969 | 2026-10-08 19:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 51e3d7aa-6f28-374a-8171-bd0fe87b79a3 | -2.8896 | -54.1715 | 2026-10-08 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| f63487af-3a01-3d48-90db-f8095b2e1b31 | -2.1361 | -54.4671 | 2026-10-08 19:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| b5380ae0-d58b-34a7-9f81-880397bcda7c | -11.0754 | -44.0534 | 2026-10-08 19:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| c980b2cb-8897-3c4b-b0e0-6278edef506c | -6.3283 | -55.3276 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 60292947-adcb-3eaf-8ee6-e531b5dbab25 | -2.8434 | -57.4696 | 2026-10-08 19:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 896c8307-7b83-3f9d-9a81-be3baad3f543 | -2.5903 | -56.1839 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| cf826996-f63b-31f6-a1e6-f7667bf679f0 | -2.8712 | -54.192 | 2026-10-08 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| b08ab958-bc71-338b-ac0c-dfa6031f4f7a | -2.4942 | -58.0768 | 2026-10-08 19:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 81c7d89b-3151-36d6-98f7-64cddb2c2750 | -4.1644 | -43.2092 | 2026-10-08 19:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| b8569efb-a6b6-360a-bfd2-6e0ad55c2750 | -9.5124 | -46.8534 | 2026-10-08 19:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 972695a9-76b3-3ab0-9b4c-a77bfdcac7c7 | -6.4596 | -55.0415 | 2026-10-08 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 5ad6b5ef-fdb8-3f3b-b487-c15fd26ae9d5 | -6.2164 | -52.7671 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| bd47212b-e5f6-3042-bb12-3cac6b02c00d | -2.499 | -56.0675 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 924801ee-6bdf-3bfb-984e-d990c57cb197 | -13.3671 | -43.8742 | 2026-10-08 19:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 1005bf69-20cd-3ad9-adc0-8f9d41af02b9 | -3.2085 | -57.87 | 2026-10-08 19:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 9ea48f4c-6c5d-372c-bea4-49983f5a31ab | -1.7307 | -55.4479 | 2026-10-08 19:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a9902b84-2130-32c8-93d7-ad9609027c2f | -3.354 | -58.1961 | 2026-10-08 19:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9f1ea3c6-518a-3798-9f6b-70c6f1239f65 | -6.234 | -52.8889 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 353.8 |
| f4bab7fd-71e2-3619-a968-1ce161b22532 | -3.3139 | -53.718 | 2026-10-08 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 6d47443d-a3f1-3dc9-a0fc-7173c642ab12 | -7.089 | -52.6958 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 235.8 |
| 7ba39b02-0ada-3efd-b3f2-272d8643c35a | -12.1549 | -44.7314 | 2026-10-08 19:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 6e03ab41-9ec9-3d29-afd9-29edce4b24e8 | -3.3637 | -50.4701 | 2026-10-08 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e3545760-31c0-3d5b-acb4-e63611df74a7 | -9.422 | -46.5506 | 2026-10-08 19:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| b3f6a5f4-9e3e-3021-a5dc-340524bf64f1 | -2.8347 | -54.1125 | 2026-10-08 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 1b69b7fe-3ac5-3c12-a362-490be00dd108 | -14.4535 | -43.9359 | 2026-10-08 19:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 93.3 |
| b743d948-4508-3592-872d-bc321a4ddf4e | -4.6362 | -50.9646 | 2026-10-08 19:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 628.6 |
| 4edb4d61-89ce-347d-ad01-449bba896c74 | -2.5168 | -56.2639 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 116669e7-4c84-345f-8637-9e0526eeed97 | -4.0838 | -44.1159 | 2026-10-08 19:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 27c0a8c1-359d-3879-8e93-a07bb752e5fd | -5.2352 | -56.109 | 2026-10-08 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| cee1b437-e9ba-3bc5-aee6-7da097a685af | -14.4339 | -43.9396 | 2026-10-08 19:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 153.7 |
| d15eb82b-df9f-3cbb-b73f-46e15a3750ab | -4.7404 | -55.6522 | 2026-10-08 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 9928ef65-7c1e-3cba-85e0-f0b46ccb36a5 | -5.9835 | -40.9367 | 2026-10-08 19:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 1c4620eb-274a-3f0a-9aba-cc5137616951 | -4.7009 | -56.2268 | 2026-10-08 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0036575b-033d-35b6-a2a5-414e9fe0483a | -1.2911 | -55.4133 | 2026-10-08 19:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 839f081e-ff67-3949-80be-97c166b2dd51 | 1.7672 | -55.5463 | 2026-10-08 19:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 0a632d71-ef0f-3597-ad92-756a3d6b599e | -2.853 | -54.1322 | 2026-10-08 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 515e3d1b-cd1e-395f-a594-5929d7252ff5 | -11.2259 | -45.3064 | 2026-10-08 19:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b75314b2-695f-3cfc-9d05-9b9590e88244 | -6.1615 | -47.9419 | 2026-10-08 19:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 4403d65b-ebbc-3477-9d0e-5a61fc3dacbc | -2.572 | -56.1646 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| b92f7483-a278-3c09-a953-ed0a4c836829 | -6.0386 | -51.7261 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| df3a9cb3-2dc0-314b-81c6-2251eda6b01f | -6.1041 | -55.7162 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 4703bf94-c283-30e7-b5d0-3acb4a122378 | -3.2137 | -42.953 | 2026-10-08 19:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 208.5 |
| fd7e684b-c254-3251-ba1d-965a335b0529 | -2.4988 | -56.1266 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 67b0dc6e-02c2-3b82-9c4a-6552e94081fe | -6.4031 | -55.2042 | 2026-10-08 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| b4e9209f-aa62-361b-a124-fe3902f85421 | -5.3718 | -44.1981 | 2026-10-08 19:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 742afa54-db4c-3958-8c4d-b4662f928446 | -2.4623 | -56.0879 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 1bd08059-2c13-3ea8-9b4c-a354f71ce1bd | -8.537 | -66.9764 | 2026-10-08 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 9b8e58d3-187b-3f19-8a0a-2d44e86eb998 | -2.7613 | -54.0941 | 2026-10-08 19:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| c65f2bb9-c4dd-3248-8981-f6c06b7c659c | -11.7742 | -43.5245 | 2026-10-08 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| fa314a36-83b3-32e1-9e0b-cf0a2a8aa7a2 | -3.2532 | -50.4108 | 2026-10-08 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 394f9f57-a729-3c16-af7e-b48bfc871f9d | -6.5127 | -55.3984 | 2026-10-08 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 0ce71c9a-f98a-3cad-9099-c138022d6565 | -4.1645 | -43.1859 | 2026-10-08 19:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 5a2f4d86-037e-346f-9cf4-bc47b4474d4c | -3.9483 | -56.0335 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 58ff1787-c698-36ef-8ef7-3abd2e69311d | -14.4345 | -43.9157 | 2026-10-08 19:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 4d2f6262-5ae4-32bf-aead-80981c563278 | -6.2342 | -52.8685 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 301.3 |
| 5420d876-e2e4-30d6-b0b5-2cc74f0b5a81 | -8.3011 | -45.7245 | 2026-10-08 19:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4568b194-e850-3130-9025-4d8fd9011288 | -3.2031 | -53.8621 | 2026-10-08 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d68efa53-7850-35c3-9a56-f12279d38b21 | -2.5675 | -58.037 | 2026-10-08 19:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 86783402-8ac2-3ba9-b062-7b53996d8207 | -2.572 | -56.1842 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 210.6 |
| a4d6ff96-c14c-3586-ad4a-7c1170a3a4c8 | -5.3716 | -44.2211 | 2026-10-08 19:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 138.6 |
| a81f473c-23e2-34b0-8248-ca54b2562db5 | -9.3205 | -65.5392 | 2026-10-08 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 4211ce79-4d5c-3b42-82bc-962dc156989e | -2.8712 | -54.1719 | 2026-10-08 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 40decd44-7a94-393d-82a2-89be1e64ca9e | -2.9451 | -54.0497 | 2026-10-08 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 135ecb6e-659b-362a-8a25-d6961770d4e1 | -7.4694 | -42.8551 | 2026-10-08 19:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 96c3cded-3b4c-33eb-8b44-7920b608b534 | -13.3666 | -43.8979 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 16466157-2e1b-3b78-9f93-b389d09930d3 | -6.4752 | -55.48 | 2026-10-08 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| b24a5667-be95-339e-bffd-9d4a788ee07c | -2.517 | -56.1656 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6e8c5ec1-b6fa-3b91-9854-5974a2b54fbd | -7.4097 | -44.7427 | 2026-10-08 19:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 960e7b11-5349-384e-8394-4d7460d55f10 | -5.9266 | -51.8358 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 181.8 |
| 45064be0-d133-3036-82c0-9dffb33d3b8b | -3.188 | -58.6241 | 2026-10-08 19:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 0f761b52-8d26-3279-b61e-ec2d8dbbb0dc | -6.0076 | -53.4919 | 2026-10-08 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 190.0 |
| d8d1b439-06e0-38e0-bb61-0b2ac1cd079e | -3.2533 | -50.3899 | 2026-10-08 19:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 664b6660-682e-3942-8b9a-2f13b546883a | -3.1951 | -42.9538 | 2026-10-08 19:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d73e9e28-ad64-35af-92cd-54bcb4117f6c | -2.4623 | -56.0682 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| b9170e1a-65fe-3884-afe3-ca552b0038c9 | -3.1697 | -58.6437 | 2026-10-08 19:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| d8eddad2-39fc-3175-98a5-d476b0e76361 | -6.8907 | -45.8988 | 2026-10-08 19:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| d3bb6895-74bf-34a4-9f02-8c9c4ecb3e17 | -3.1874 | -58.8358 | 2026-10-08 19:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b6bc7927-e835-36c7-a149-8c8ad02ca8f7 | -5.9587 | -55.3448 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 152.2 |
| c058bb8e-1b33-3269-ae41-4fabe5f45ef4 | -3.1697 | -58.6244 | 2026-10-08 19:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 7ef48884-ecb4-38e9-893d-28b85e0a7dc1 | -5.9891 | -53.4928 | 2026-10-08 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| b77233c9-bb72-3133-bb5d-6ed89ca06c1d | -3.1114 | -53.7839 | 2026-10-08 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| b99f8653-74d1-3232-bec4-1e5d16d19481 | -5.9772 | -55.344 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 24129799-e314-39e9-be91-c71d6a3256e7 | -6.4567 | -55.4809 | 2026-10-08 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| d382b766-c024-3a6d-83f0-dbda7b8a4dfc | -9.9208 | -44.7893 | 2026-10-08 19:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 0675de58-e5f0-3d09-b663-84caade6a758 | -3.1879 | -58.6626 | 2026-10-08 19:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ed8fae7a-024d-3e97-8523-c16dd6006cc8 | -3.4312 | -56.9307 | 2026-10-08 19:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 89ff8db3-030c-330b-923c-fd04335a0cbe | -1.146 | -54.2199 | 2026-10-08 19:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 716f4b23-6999-3d6a-a6b0-52281a5bf2d2 | -11.755 | -43.5275 | 2026-10-08 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |


[Clique aqui para ver as próximas entradas](README411.md)
