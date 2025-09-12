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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57b36423-c8bf-3810-bdf1-e13acb4cc45d | -10.48456 | -49.37046 | 2025-09-12 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d01d87d-64f5-39aa-877f-7a09f2f96a53 | -10.40087 | -50.03057 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8791912e-78bc-30e8-b08b-dc6a2cb19747 | -6.65389 | -44.13266 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c165d721-90da-325c-b402-8cf8770997b4 | -8.17863 | -46.08943 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8f64ad9-d624-3e1c-abde-fa006df25d95 | -6.479 | -45.14695 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec1a456b-d800-34d0-b38c-8b08ea7e3d99 | -9.03679 | -47.06776 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20ae8ca9-b214-3ca5-aa59-fe7d45a6dec2 | -8.18198 | -46.11147 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e897bb33-2937-3df7-9fa5-8ca73be90125 | -4.92951 | -55.78165 | 2025-09-12 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe4bc24f-86a2-3433-b4a8-37fa36d79488 | -10.4212 | -49.99654 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8bca629-1bde-304c-8f94-d25c1bcdcfca | -8.02433 | -44.80361 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75550c39-268d-30fa-9c63-0fd4d6e7f934 | -9.832 | -54.53441 | 2025-09-12 04:25:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3ef26ca6-2c39-3aaf-91a6-4c2c85c87a47 | -9.98779 | -51.72544 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe0c73b4-f5eb-365a-90d9-9c84a9c26e76 | -10.18889 | -46.23559 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7f3866e-9e8b-337b-b654-30efe7cf9b43 | -6.82396 | -45.65507 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 963d90fe-43ea-3807-84b3-641a74a642f9 | -11.03158 | -51.51575 | 2025-09-12 04:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ab09a07-0986-3632-97d0-190988b62821 | -9.06797 | -50.50283 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0270a922-9b17-323b-94b4-4a28674d69dd | -11.51532 | -50.60437 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45465e42-bc2c-3c53-b546-f91c75d4061f | -10.67635 | -48.60296 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9fc6ab4-d9f4-304c-aae1-4a70a93a0875 | -11.6754 | -46.56357 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a584e345-7c1f-3924-964f-3a72b89305a0 | -7.3216 | -49.62455 | 2025-09-12 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf50afeb-4405-3bad-ad5f-de58418db39a | -9.6874 | -47.54865 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c13a2c71-14c9-3cf8-9e04-5196df348b19 | -12.13194 | -44.83659 | 2025-09-12 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ec5db39-4f92-3594-83a8-d38739dbc4ec | -11.37001 | -43.50904 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d388dd7-5c75-3a32-bb4f-1473d1c4456c | -7.90859 | -44.8742 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a02236c-a84a-3672-be1b-477c4ddc9c20 | -11.68979 | -46.51472 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b59aa5a-4e33-3cff-9c27-77577f236697 | -11.17982 | -48.43471 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25701885-5b40-3589-80b2-88fe80f4cfba | -10.40268 | -50.02451 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41f1cc40-dba4-3aaa-858d-02582e2f9909 | -8.88012 | -49.5413 | 2025-09-12 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58eaf66d-3c9e-3abf-870b-695d1fa57060 | -9.95999 | -51.6995 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41de2956-4d42-3356-83e1-67e361aee64f | -10.003 | -51.73061 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ea52087-f3f0-3953-b7ef-7ff72fa0b326 | -8.95777 | -46.07828 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 968ab001-d34f-305c-9864-a3bbbee9e821 | -7.84541 | -43.88768 | 2025-09-12 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cb4c7a7-81cf-3f60-9701-ce7c3025519c | -6.30771 | -42.2262 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f3152351-932b-32e4-ac07-c234007e30c8 | -12.1384 | -44.86629 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcf7dc3d-517c-3350-806e-fd19999d5ddc | -7.54187 | -44.38816 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2814ec48-0b44-387b-af18-c2bc06a65678 | -11.67317 | -46.55592 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25fc76f6-9c57-33b2-a076-40ea4c084506 | -10.74142 | -48.17918 | 2025-09-12 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abccb5dc-7a31-35e5-bf6d-504db88585d4 | -10.43847 | -50.60359 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9a1e4d0-ed3d-3e5f-b618-442b89bf5825 | -7.24928 | -44.47126 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27fb0a4d-3003-3024-a4ef-1bf7ca839aa0 | -11.97738 | -46.65163 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 64cc8104-17df-3bfc-9470-b2acb4f9ffb8 | -8.18278 | -42.42947 | 2025-09-12 04:25:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 5d7324f1-f28c-3445-954a-0ea359ac256b | -11.67157 | -46.61043 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3748042-f563-33f1-8687-83568312ba6e | -10.21889 | -46.24033 | 2025-09-12 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9536620f-0f37-3a91-b30e-b682f643f2fd | -9.25295 | -57.06923 | 2025-09-12 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb3bf4b7-290a-3eb9-bbbf-a88605e7e7c6 | -5.27651 | -49.29478 | 2025-09-12 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6bce1694-09dd-3cb5-a900-a3893a152b8c | -8.3113 | -44.89659 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a4b33f4-f049-359b-9c90-aea002347349 | -6.10078 | -45.93642 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d7a8d72-3373-3fa7-88e2-1d3816e9a66a | -6.95955 | -44.78294 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cb55b5c-16ab-3d5e-be0b-1676c041dd0f | -7.46924 | -45.29932 | 2025-09-12 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43f31751-0dd5-3274-8d9b-519029c77a97 | -9.68684 | -47.55215 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95f98d6b-e5cd-33fe-a077-3a469c72052c | -11.49007 | -49.2701 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf500864-93ca-3221-b5cc-5060b37d4c04 | -9.48888 | -55.97139 | 2025-09-12 04:25:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6ec6063-4c25-372a-b378-2f9d43b82056 | -6.30838 | -42.2216 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eed8ac0a-22d9-3fdb-a93f-942b2451b243 | -11.3176 | -50.34301 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0c1288c-2d89-31fb-b6f7-e30132b2dd6d | -7.22018 | -43.97984 | 2025-09-12 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1230d8b1-4bdd-391a-99c4-05e1be3a9bad | -11.46802 | -43.60474 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7583cc7c-d36e-31d4-8e39-5217ee4807d7 | -6.82228 | -45.64405 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a7d947e-dc71-3f3b-8e99-0ee0784e11d4 | -3.79464 | -51.15712 | 2025-09-12 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf2943d2-edce-39b6-8655-81fbddf506e0 | -9.07479 | -46.95613 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdf530ce-394f-351a-bff6-11b37bb745c4 | -7.46014 | -44.92223 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c35bf0c-25ab-3809-bb71-0ebaa4818a1e | -8.04307 | -44.81814 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3fdf197-bcf0-3f94-b604-696401a6ecfb | -11.09692 | -48.4027 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 088397c5-acd6-31e9-8141-73b63e08cb17 | -11.86446 | -47.52763 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3f29bff-0c45-362e-9367-585e9df3e248 | -9.80147 | -48.89042 | 2025-09-12 04:25:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69ba6a70-1f69-3ec0-9ae3-c546056a648d | -11.69819 | -46.5709 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d093e68a-53df-3c8c-9683-b9d06046772a | -10.1654 | -46.16644 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30adea4a-063c-3aa4-818b-f32f31e48909 | -11.4438 | -45.14158 | 2025-09-12 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35ecbb71-c255-3fe1-b2b9-3fe27a900c33 | -10.70588 | -48.63404 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68f9677d-eb01-3b18-a134-6cb7067ee245 | -7.45568 | -51.81108 | 2025-09-12 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7caef810-39c1-343e-ac82-1ca2e1db589e | -8.17702 | -46.12143 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1e0f4d3-30f7-3890-b17b-66f9ddd82a5c | -9.06438 | -47.04357 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e82c7baa-925f-3096-9871-3272f761e316 | -7.84894 | -43.88822 | 2025-09-12 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35a67db9-4f6c-3b14-9884-54705e028719 | -12.02228 | -43.78517 | 2025-09-12 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b5c58c73-2622-3bf5-9244-1cd2a228322f | -8.97108 | -46.08038 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83819b22-7b6d-3b43-bc8c-e4516b3b879e | -8.17757 | -46.11793 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bdebd48-97db-31e2-b193-1f1fbf6d4625 | -8.1737 | -46.12091 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27f9edf5-6e66-3cac-94e2-f7e930243f1e | -11.1147 | -51.98521 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18497e9f-9f32-3c82-a3c9-52f9bb09920d | -10.6703 | -48.66153 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fec0a8a-e4d5-33fa-9549-0ded1ecb31c2 | -11.47738 | -49.28347 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab1a7039-915a-3aaa-8746-0b7b8bd27b5c | -12.10542 | -44.86967 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e30dc73-7740-3f0f-a581-fc9515aed0d8 | -7.13349 | -45.51991 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 606b27e5-966a-3eea-82c0-7c16a974b2f4 | -10.37172 | -50.50964 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c59bf8b-3790-383b-b705-2aa38182b5a3 | -9.03348 | -47.11007 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| edd8299c-8da1-365e-9817-8fd88408e864 | -5.28748 | -48.13233 | 2025-09-12 04:25:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2095a2f6-6ecf-3e21-85be-c28d7844a9d4 | -6.40387 | -43.50362 | 2025-09-12 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2b7902e-10f1-3712-b149-05a5d45cb778 | -7.83874 | -44.89361 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae4c4b8d-279d-3e05-9e66-74bdd475cb80 | -9.01684 | -45.74307 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 840eae95-e0e5-30dc-8b79-5addc826a5ea | -6.4045 | -43.49955 | 2025-09-12 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| be9d9239-1fc0-388b-a13d-b8059242f558 | -7.73097 | -50.74465 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 596a4de6-0dfe-3545-8ee1-5b5af557eb3d | -9.32319 | -48.9406 | 2025-09-12 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2eddbcc-8e7d-3b67-92fe-d952a0c8428c | -8.96775 | -46.07986 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0b1ccc8-dd83-3e1b-a531-7d3ad66fa2df | -10.7021 | -48.6146 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a09be1d0-096e-3605-b451-d3afd175de24 | -11.65935 | -46.60115 | 2025-09-12 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 314bf017-6b06-3b11-8d8a-824f8aae1ce3 | -9.88128 | -46.46934 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fa4bb10-3e2c-3893-9e1e-6bc83dd92a15 | -11.53675 | -50.39924 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9538fe70-1a0f-3495-a7d8-9a48bf200e3e | -9.89403 | -51.87042 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d9d37fa-e9e7-381c-bc01-5a721fdf51f6 | -11.75015 | -48.26858 | 2025-09-12 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb4a5331-6b9e-3649-994e-c758f078e92c | -10.8459 | -48.16367 | 2025-09-12 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 67a1c166-d3fe-3d52-8cd7-bb1475dec699 | -10.33049 | -48.80939 | 2025-09-12 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5c6aa61-2cdb-3642-afaf-b640ece1c9cd | -4.63682 | -47.05122 | 2025-09-12 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README70.md)
