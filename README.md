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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58027cb6-bca5-3744-8e7a-1b6b7244c91a | -12.6579 | -58.2079 | 2025-06-05 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 0aa4fa27-4e32-33ce-8a77-b1e54e6b0822 | -11.6305 | -55.3875 | 2025-06-05 00:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 758a894a-c835-3b3a-a656-5fcbe76b8fd6 | -12.6577 | -58.2277 | 2025-06-05 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| e5ed690f-2ade-3fc7-bb54-d8295707a4b5 | -7.8929 | -50.368 | 2025-06-05 00:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 05e4de75-00ae-33bb-ad45-77a42dada3dd | -18.8484 | -53.6035 | 2025-06-05 00:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 4384d08c-5c23-3ed0-a63e-62adf8068724 | -18.8279 | -53.6283 | 2025-06-05 00:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 75caf911-ed4e-38c7-8256-201ef5693683 | -7.9116 | -50.3666 | 2025-06-05 00:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 0bcbf6f7-e7b5-3f27-b975-49bd983b991e | -18.8479 | -53.6251 | 2025-06-05 00:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 2a27824a-16de-3215-8beb-072b8db63669 | -11.5426 | -56.4438 | 2025-06-05 00:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4d450d98-3309-338e-bdc4-5d46b317b90c | -10.8767 | -46.8713 | 2025-06-05 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c361a7d4-b3b0-30f2-9ea4-f0eb411bd56f | -10.5004 | -53.651 | 2025-06-05 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 3196b618-6dc1-3743-8ca3-b5269118f323 | -12.6767 | -58.2262 | 2025-06-05 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 5c2c5e94-c096-3603-b4ff-6ff29bfe62c8 | -11.5428 | -56.4237 | 2025-06-05 00:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1aa4a46b-7f3c-37f2-9310-5a8b45ccc4e9 | -12.6769 | -58.2063 | 2025-06-05 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ff0a089f-2536-3a17-b52d-de65714735b5 | -11.5428 | -56.4237 | 2025-06-05 00:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 8160ba11-9245-313b-a808-d5105f56f3a2 | -12.6767 | -58.2262 | 2025-06-05 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 99205ba2-859d-3671-9c5f-705fee874a63 | -7.9118 | -50.3454 | 2025-06-05 00:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 990bd846-7f80-358c-880a-c9d46a404b64 | -18.8279 | -53.6283 | 2025-06-05 00:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6672eec1-49c4-339f-8073-163f0d21628e | -18.8479 | -53.6251 | 2025-06-05 00:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 60a38780-fd81-3ae9-b821-94730e4f7ef8 | -11.5426 | -56.4438 | 2025-06-05 00:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 0a4fbcc5-94f5-337a-b0d3-3a062ebf64bf | -18.8484 | -53.6035 | 2025-06-05 00:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d21aac3d-5bc4-3eb8-accb-5f7c9c54c52f | -10.858 | -46.8513 | 2025-06-05 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 753a5df7-1f4f-39b0-8b4c-0dd8d1c9ba67 | -7.9116 | -50.3666 | 2025-06-05 00:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 2e3d84e1-83c4-3624-995d-74463388695b | -10.8583 | -46.8288 | 2025-06-05 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 74f18f04-e52c-3f77-b1ff-efbc85bf86b8 | -11.5426 | -56.4438 | 2025-06-05 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 355fd9ba-0f32-399c-a28d-2ecfd707f113 | -11.6305 | -55.3875 | 2025-06-05 00:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| f929edbe-4092-32e9-9679-87de465fbb24 | -7.9118 | -50.3454 | 2025-06-05 00:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9e7c256a-0229-3a3f-aa22-da2cbc8a2503 | -11.5617 | -56.4221 | 2025-06-05 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| a4a24ca5-d91d-3516-ada4-de24aa21c4d5 | -10.858 | -46.8513 | 2025-06-05 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 6c3b4333-f30f-3d2c-9cac-7ee957ac9bf6 | -10.5004 | -53.651 | 2025-06-05 00:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 15655859-71d1-3ea2-9acb-bc6848d704f4 | -18.8479 | -53.6251 | 2025-06-05 00:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 104.1 |
| ba3b5e98-0259-30e5-addc-a8ae29be8455 | -11.5615 | -56.4422 | 2025-06-05 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 78aef000-dd57-3d6b-be11-1179ef4f02c0 | -18.8279 | -53.6283 | 2025-06-05 00:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 51.2 |
| ad19912d-727d-3cab-9937-b3683ca2392b | -18.8484 | -53.6035 | 2025-06-05 00:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 18ffc8a1-819d-3d44-a5b9-3e3b8971258d | -7.9116 | -50.3666 | 2025-06-05 00:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 6f7fe1c5-76bd-37f0-8db6-ddf31bfd3dff | -11.5428 | -56.4237 | 2025-06-05 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 3e94a092-f128-34f1-b6f2-3041288a2f0f | -11.6305 | -55.3875 | 2025-06-05 00:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| c764f780-f3a0-3224-a03e-53138a97e57a | -6.204 | -43.3241 | 2025-06-05 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 8e65650e-7b68-321a-9888-e2ce07e4ef7c | -7.9116 | -50.3666 | 2025-06-05 00:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| fee2e45b-7f4d-32e5-99cc-61fe0f9403b0 | -18.8279 | -53.6283 | 2025-06-05 00:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 4f016185-57da-3d99-9ea3-edabd2fda566 | -18.8479 | -53.6251 | 2025-06-05 00:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 185178a7-08c9-332c-bfdd-b73e41846d11 | -11.5428 | -56.4237 | 2025-06-05 00:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| af0cdd2e-7943-347b-a491-83464b86693f | -6.2038 | -43.3475 | 2025-06-05 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 8f17f25f-1d20-3ade-ae6d-31fd73a7f265 | -7.8929 | -50.368 | 2025-06-05 00:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c5c4cc69-6cce-3d5f-aa36-4317a9c7519c | -7.9118 | -50.3454 | 2025-06-05 00:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4b75cc80-07ea-3637-8163-09c03a223930 | -11.5426 | -56.4438 | 2025-06-05 00:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b3d5e853-ec48-3df2-899e-5bee7382dc8d | -12.15377 | -46.59766 | 2025-06-05 00:37:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f7fe1322-31ce-3ab0-b463-e441404b505b | -12.03177 | -43.723 | 2025-06-05 00:37:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d84f3a13-6246-343b-b786-88164f320c65 | -13.22049 | -49.02889 | 2025-06-05 00:37:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 29f43f8d-0aa6-3311-b3ce-a86abdff4702 | -13.8644 | -44.12873 | 2025-06-05 00:37:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 78f689e2-0e8d-31ef-9179-14380394869a | -14.23529 | -45.47949 | 2025-06-05 00:37:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c8415d1d-f584-3a0c-a7d5-289f4ae83297 | -14.22768 | -45.49024 | 2025-06-05 00:37:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cce299e4-1f69-328a-acd5-af26dd127b70 | -14.72429 | -45.09541 | 2025-06-05 00:37:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b569ec4c-e95b-344e-9150-e0e519a11552 | -12.0534 | -47.32995 | 2025-06-05 00:37:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7c3e5ea2-2f8d-3a8e-a7b3-3b3bf47e000c | -12.29323 | -43.55196 | 2025-06-05 00:37:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 40df3510-1eb6-38dd-af6b-8f25740922b3 | -18.08878 | -47.09776 | 2025-06-05 00:37:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d4a691e7-a7d6-3f9a-8985-2af1f9dedd29 | -13.51565 | -56.54427 | 2025-06-05 00:37:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 84ba7d2d-f146-3195-b7bc-fdae4c4d3485 | -13.08447 | -49.24838 | 2025-06-05 00:37:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 796fe0b6-525a-378b-97bc-4a5908469282 | -16.07135 | -43.65817 | 2025-06-05 00:37:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a1076bb6-407b-360e-bd75-a2918084aff8 | -16.58711 | -45.87817 | 2025-06-05 00:37:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 355d8052-8153-3602-8229-810e60e06065 | -13.51952 | -56.58021 | 2025-06-05 00:37:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 713.5 |
| f1960e70-065e-3048-99b2-4c6c73635d49 | -14.16227 | -45.48121 | 2025-06-05 00:37:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e26525f6-03b8-34d8-9262-be2bd8bc8741 | -13.56952 | -44.2697 | 2025-06-05 00:37:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2e3517cd-ad49-3aac-a627-6afb628943fb | -11.90442 | -47.45544 | 2025-06-05 00:37:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5d1e5c23-e6fa-39c9-8ace-7d5e4cd2445f | -11.62632 | -41.83355 | 2025-06-05 00:37:00 | TERRA_M-M | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 7a148bc4-dede-3d11-948a-7bbd4f118014 | -13.50892 | -56.57462 | 2025-06-05 00:37:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 239.8 |
| 47df1993-54e5-3256-8018-ad18da7e88ec | -13.52544 | -56.57268 | 2025-06-05 00:37:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 570.2 |
| c0d079be-aad3-3c0e-b1fc-d0434f844716 | -11.44146 | -45.11087 | 2025-06-05 00:37:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2ae00b28-8538-32c5-890a-c9c3aff3c310 | -14.15356 | -45.4889 | 2025-06-05 00:37:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d0bb1a04-e99e-39a9-af52-2dc28aa2cbdc | -18.62854 | -47.64501 | 2025-06-05 00:37:00 | TERRA_M-M | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f6f3fc1a-d378-3758-bfe9-1df762dcf30a | -14.73333 | -45.09395 | 2025-06-05 00:37:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 595eb308-77f0-3d9f-9e98-d66d0c62703e | -14.22634 | -45.48088 | 2025-06-05 00:37:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6d5683f8-f09f-3abb-8b64-f527217aaaf3 | -13.5292 | -56.60983 | 2025-06-05 00:37:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 57dec22e-d090-32b7-9b65-4fb3bfcfb4f3 | -14.58013 | -46.75006 | 2025-06-05 00:37:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82af3969-1a02-3d1b-b610-9f9d31d827ef | -14.7347 | -45.10348 | 2025-06-05 00:37:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f88e3b50-bfa7-3876-8d7d-69ea3ef443a3 | -12.06223 | -47.32866 | 2025-06-05 00:37:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5135a681-ffe1-30f6-8be6-0549a9b23d64 | -8.95868 | -47.28705 | 2025-06-05 00:39:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 47319e22-4253-331b-a189-9082ef11c6db | -8.6857 | -48.30155 | 2025-06-05 00:39:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6fb55c38-9a94-342d-b1ba-c6e555dfd103 | -10.66404 | -44.38069 | 2025-06-05 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f8891969-89f3-3ac5-a024-a5d6012a083a | -7.19671 | -43.12698 | 2025-06-05 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| d6e1ad1e-5dfb-3e3c-a89c-268711a5eae0 | -10.87598 | -46.8817 | 2025-06-05 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bcbb4284-ae31-335b-9a78-ed19da06e505 | -6.20663 | -48.56514 | 2025-06-05 00:39:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 230a3d2a-626c-3aae-afe2-07a76ec1a3bc | -10.1292 | -48.6887 | 2025-06-05 00:39:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1c923199-3fe9-3c03-8e89-1cc97bda85bf | -6.63486 | -47.3464 | 2025-06-05 00:39:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4a338190-da73-3705-82ef-8476c5e5d6c1 | -8.68447 | -48.29263 | 2025-06-05 00:39:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd0c9423-6288-319c-99ae-19a0d7413acf | -6.96862 | -42.91774 | 2025-06-05 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| adf59db3-bc3b-3fec-abfc-47336cc057ba | -10.64507 | -49.43927 | 2025-06-05 00:39:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| ddf6a169-2fd3-3a9c-a6cd-095be950279b | -7.07337 | -44.35391 | 2025-06-05 00:39:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3cd2a929-7b8b-3684-9ae9-e04fb453e5c6 | -11.13743 | -53.94267 | 2025-06-05 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 20cb6125-13d8-35d1-8f60-8d8f2ab044e5 | -10.87472 | -46.87274 | 2025-06-05 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 441c0033-3749-3e6b-84a2-dcc967e24945 | -6.29302 | -47.01343 | 2025-06-05 00:39:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4fd954af-7778-3192-b9ad-956b1553bdce | -6.59966 | -43.90662 | 2025-06-05 00:39:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 66f44d90-5ab6-3f42-bc96-50807cc0cd99 | -10.50191 | -53.65363 | 2025-06-05 00:39:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7f326f27-35bd-306c-b100-9e2a02b1bbbb | -4.8129 | -45.27166 | 2025-06-05 00:39:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1862928a-e1c0-3109-bb3c-05cc06f148e4 | -9.10775 | -47.63143 | 2025-06-05 00:39:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1f8f9b98-0a3e-360a-bddd-551a9fb5bb6d | -6.30202 | -47.01213 | 2025-06-05 00:39:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2235f8c4-a628-30d3-b4dd-f484407dc020 | -7.90708 | -50.36336 | 2025-06-05 00:39:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 220.8 |
| 3f660f36-8dec-3c31-b007-436348561e9b | -10.87346 | -46.86375 | 2025-06-05 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4d74570b-3b63-3978-9847-098a5ce92005 | -7.54563 | -45.8342 | 2025-06-05 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4d74cb4e-cbaf-39a5-b406-b1820b3a9fc1 | -9.2311 | -48.85722 | 2025-06-05 00:39:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README2.md)
