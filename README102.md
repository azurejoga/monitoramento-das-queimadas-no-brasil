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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb68ed7f-3b31-3d16-aea0-dfb95ec2cad5 | -9.7643 | -47.7786 | 2025-09-28 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| a6bda433-8a4d-317d-ab1d-f0822fa0071a | -5.9004 | -43.6976 | 2025-09-28 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| f9546b46-9ded-38f2-875a-1dcf95ab73b8 | -6.3 | -45.0205 | 2025-09-28 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d5665aa5-323a-38b0-a503-e5469d3a76af | -11.4604 | -44.997 | 2025-09-28 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 3ef6345a-8a86-3bef-9b03-0002e0d0416d | -15.8682 | -46.2214 | 2025-09-28 13:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 73.4 |
| eb0d5205-59fd-3615-86e7-9618695d3f08 | -10.8242 | -45.3841 | 2025-09-28 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 120470b6-d180-3bc0-9524-2462e104fbb3 | -11.3846 | -44.9618 | 2025-09-28 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d4c9847f-95d4-3c40-adab-ce455b2d4d36 | -7.2216 | -44.7601 | 2025-09-28 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 90eb7b84-31a5-33ae-aa59-10ccdab9d862 | -11.4217 | -45.0257 | 2025-09-28 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 9e7b5b8f-8cc0-3935-a562-6a4a62f00ffa | -6.2759 | -43.6442 | 2025-09-28 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 062a7df4-dcd9-3238-9e20-806593db8827 | -7.3847 | -47.0378 | 2025-09-28 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 299.8 |
| 875782f2-e69c-3ead-aba0-6cb956b8972a | -15.6092 | -53.1669 | 2025-09-28 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ef1e1eec-c98e-3c19-9d71-b47c064f2d2f | -8.2665 | -45.4791 | 2025-09-28 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7b4b9051-c9b1-3e72-90dc-354adf861cd8 | -5.1885 | -43.7495 | 2025-09-28 13:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 607e03e1-b56b-3c29-98dc-8d8349620cdf | -17.7138 | -46.7098 | 2025-09-28 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 95.6 |
| a858ef3a-343c-39c0-9701-73ee0135746d | -9.3013 | -45.7082 | 2025-09-28 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 88e18a60-e5f1-3bb5-9d15-f632c9bece57 | -12.7637 | -50.4921 | 2025-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 0bef68df-eedb-3868-b448-fa4975ebed0c | -9.4194 | -54.697 | 2025-09-28 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| c3d1ab1c-10ed-3b25-b00d-a876a55a41fb | -13.2966 | -50.7036 | 2025-09-28 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d78a7b85-4cd2-3897-b0c6-8fce00c9601f | -9.106 | -47.6275 | 2025-09-28 13:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 439a9a08-df69-387b-a51c-283ac0796c19 | -13.77 | -47.8987 | 2025-09-28 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| bb3a0197-d2b1-3146-88c6-4ea62ee19aff | -5.7396 | -42.8461 | 2025-09-28 13:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| f86ddccd-aabb-34fd-9b90-d193e04781bc | -9.4009 | -54.6781 | 2025-09-28 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| bb66d8d3-d7d6-369b-9f23-4aa1f2ef747f | -6.6002 | -44.9736 | 2025-09-28 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 9d8a9ee7-29e6-34ab-8534-5aac2c107e0e | -6.3154 | -43.4548 | 2025-09-28 13:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 9849709d-e263-333b-b842-aed0fd292a7c | -8.2856 | -45.4545 | 2025-09-28 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 374a9569-6882-376d-8788-13a958446664 | -7.8823 | -44.5594 | 2025-09-28 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 167.1 |
| ca0044ab-9e36-36a8-b0ec-56aa92996b18 | -6.3107 | -45.8775 | 2025-09-28 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 1eaaa896-10c0-3db9-bfc8-57a4a6076f91 | -12.0214 | -47.9703 | 2025-09-28 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 0abf8778-29b9-37fc-874a-ba499a54f31f | -5.6461 | -44.933 | 2025-09-28 13:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8b681c3a-4ba1-3b14-ac4c-9509284ecc73 | -15.9076 | -46.2139 | 2025-09-28 13:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 8fb13b8e-cd50-3408-9fa3-bc2692066f70 | -11.6805 | -44.4545 | 2025-09-28 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d4c0cb9d-2508-3efd-b496-391dc9bbdf1f | -8.2668 | -45.4564 | 2025-09-28 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 1a0cc205-c763-3a93-8e9f-593e780adaca | -11.979 | -47.0847 | 2025-09-28 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 3227c31b-2552-3b32-a3f4-03d811d7065b | -9.4007 | -54.6984 | 2025-09-28 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 0a2c5189-717a-32f2-b0b0-32b5f46fdda0 | -12.9547 | -45.1618 | 2025-09-28 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 01bcde35-46d1-31c1-b136-178b129ccb87 | -6.3105 | -45.8999 | 2025-09-28 13:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 176dcc7e-7962-3a64-9039-e48c18f43dc8 | -14.885 | -45.5708 | 2025-09-28 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 217.5 |
| 4d55079f-c5b3-36a2-bfa9-c9da69a52e2c | -7.3849 | -47.0157 | 2025-09-28 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 708cd984-9daf-314f-8fda-bc510ad8ac01 | -14.7846 | -45.7051 | 2025-09-28 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 435.6 |
| ecbde718-812b-3d45-8f41-3b497b52e2e0 | -15.8879 | -46.2177 | 2025-09-28 13:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 134.5 |
| dc46da4a-47dc-3a4b-9cbc-0a5a12937488 | -7.1761 | -45.4915 | 2025-09-28 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 263e4564-76d2-3acf-9edd-5ae63c6bcf91 | -11.7002 | -44.4283 | 2025-09-28 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| b9cfbe68-f6de-3069-aad1-3272eb6061ba | -11.4409 | -45.0229 | 2025-09-28 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 36939351-86fb-37be-912e-690b86a040f7 | -18.1778 | -53.3239 | 2025-09-28 13:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 53884fb4-bdb1-3476-bee6-225f8fe53d8a | -17.7338 | -46.7056 | 2025-09-28 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 96.5 |
| bedc1717-cfe3-3a53-9e7d-8679b869ca9e | -5.9006 | -43.6744 | 2025-09-28 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 8f2d41c0-b1e0-37c7-851c-f84cdb340bb4 | -15.8873 | -46.2409 | 2025-09-28 13:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 48718bca-abbf-3a20-8b85-874d023be963 | -6.6005 | -44.9509 | 2025-09-28 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 73999a0f-d91b-3dc9-a82a-9da785f753ff | -11.681 | -44.4312 | 2025-09-28 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 1349e4af-fc71-3a9e-b40b-10207caa0ddb | -7.882 | -44.5824 | 2025-09-28 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| ed81eb7e-c61d-3f24-8595-f9dd46a84089 | -11.9794 | -47.0622 | 2025-09-28 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 3fed9e3e-4f3f-365f-a3dc-07b73ccda92d | -9.9578 | -43.6222 | 2025-09-28 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 60ff929b-da1d-3a9b-8f8e-df8f32ece756 | -5.2869 | -43.1613 | 2025-09-28 13:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3686b5c4-9f9d-3cff-b18c-4cc173ccd006 | -11.904 | -44.8161 | 2025-09-28 13:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 022029e9-99c5-32ee-9f57-567344322db5 | -7.8634 | -44.5612 | 2025-09-28 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 532380c0-cc96-31b6-bada-bbe230f1e820 | -12.0218 | -47.9481 | 2025-09-28 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 130694e2-b609-30fb-8046-8b4a10fc37b7 | -9.9585 | -43.5752 | 2025-09-28 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c76bac22-9f87-3fbd-94f0-f5ca085898fc | -12.0222 | -47.9259 | 2025-09-28 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 1f1f8d44-a8f3-3be2-8d9a-f75a1ca73fc1 | -12.935 | -45.1881 | 2025-09-28 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e8c6fc4d-3975-3e66-9d9c-4c7836ff9d0d | -14.3813 | -54.9472 | 2025-09-28 13:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| b5974cb9-a17c-388e-bcd5-f7adccdc8d04 | -11.3654 | -44.9645 | 2025-09-28 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 95f53694-16b4-356f-80e1-b3ee6fb412c0 | -10.9137 | -45.7375 | 2025-09-28 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.2 |
| b7b93f4d-0d86-36d4-9429-3c05a9cec9aa | -8.1611 | -46.4122 | 2025-09-28 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 1a1844f3-3f09-3d1a-ad3e-a3e13655a780 | -7.3659 | -47.0394 | 2025-09-28 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 06ce1066-15a6-3103-a3cb-5b37fde8f2ad | -8.2859 | -45.4317 | 2025-09-28 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| ca224666-4b3e-3a50-a92b-48f94f0d8163 | -12.9363 | -45.1184 | 2025-09-28 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 453e6434-21e1-3a22-9006-20cff7f795c0 | -12.9156 | -45.1912 | 2025-09-28 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 51a68695-411c-3693-81ea-4a70c633dadb | -6.6192 | -44.9493 | 2025-09-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 62796203-2d0d-30b8-9791-72b11634c2be | -11.9637 | -48.0001 | 2025-09-28 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| f57dcfc5-c451-37ec-b98e-e00ecc76abfc | -9.4009 | -54.6781 | 2025-09-28 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c8852c47-ae46-3490-928e-cf3c04311ac5 | -11.0306 | -47.9857 | 2025-09-28 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 844e1eaf-36e0-343a-9c6e-bbcc26fdae7f | -11.9644 | -47.9557 | 2025-09-28 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 229.8 |
| fad3825c-1d07-3c0c-9913-b037d03a9279 | -9.8198 | -47.8606 | 2025-09-28 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 5193a33f-b49f-37b1-98ee-11331ba05d44 | -8.5206 | -44.7685 | 2025-09-28 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| d8e8c28f-41bd-3289-80e4-687b3aa91c99 | -12.791 | -47.7533 | 2025-09-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 5097ed20-8ba2-3f36-9bd5-843d5fbfe5d2 | -11.9794 | -47.0622 | 2025-09-28 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 5ea98218-faad-3608-ac1e-6b9e40a4851c | -12.2829 | -44.0568 | 2025-09-28 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 05734d94-aceb-33d1-816c-abf686f4e204 | -11.964 | -47.9779 | 2025-09-28 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 4e60dd5b-dfda-3da4-85de-377d5446ea20 | -7.2216 | -44.7601 | 2025-09-28 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 50c59d61-9c39-3e18-b661-346d566c75bc | -11.9456 | -47.936 | 2025-09-28 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 1c83474f-2928-3de9-b910-2c44ecf6474d | -7.3661 | -47.0173 | 2025-09-28 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 673a79b7-7532-36ca-988d-ad9149ffc8cb | -5.6461 | -44.933 | 2025-09-28 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c503f638-241f-3777-b5eb-441848b8aaec | -5.3057 | -43.1599 | 2025-09-28 14:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| f8eb7402-2271-3efb-8661-419cfeb0e935 | -13.7889 | -47.9181 | 2025-09-28 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| a1ab2c06-4b0a-3b06-9c1b-9ae5306e7449 | -4.4013 | -44.0755 | 2025-09-28 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 307.0 |
| 3e5063df-3d54-3697-920f-9e653dd6ce22 | -9.3013 | -45.7082 | 2025-09-28 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| fcff577b-6559-3f02-a182-b952e37cb7a8 | -15.9076 | -46.2139 | 2025-09-28 14:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 55009a4a-9b08-3688-bded-58517aa8148c | -6.6178 | -45.0859 | 2025-09-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| f2e35ee6-522c-375d-b73a-07b528c2878c | -7.1571 | -45.5158 | 2025-09-28 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 0821128a-1a88-3396-a25f-1743bc77d9e2 | -9.7457 | -47.7586 | 2025-09-28 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 993dcca4-42df-3364-be7a-536624ebd850 | -12.7637 | -50.4921 | 2025-09-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2597f247-aef6-3d83-bb39-ee7e011fb417 | -5.17 | -43.7276 | 2025-09-28 14:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 93176481-3d23-33e7-b200-6c545a996b76 | -5.1885 | -43.7495 | 2025-09-28 14:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| f3f40d5d-a407-3369-a1f1-80dcf15ed845 | -11.3846 | -44.9618 | 2025-09-28 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| fbeb8216-c1f5-3745-89ea-cdd1ef96d63c | -11.3642 | -45.0339 | 2025-09-28 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 5b1de4ed-c884-3487-8fd9-6e06501ed736 | -11.9986 | -47.0596 | 2025-09-28 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 7ab076a6-1df6-3bbf-adeb-9947990222a6 | -5.7396 | -42.8461 | 2025-09-28 14:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| daae8425-9a2f-3ebe-bbf9-60af8469decf | -6.2762 | -43.621 | 2025-09-28 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 4d317c05-1c26-39b4-a57a-f667a46a9a3b | -9.2824 | -45.7104 | 2025-09-28 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |


[Clique aqui para ver as próximas entradas](README103.md)
