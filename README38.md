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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19af837d-b93d-3621-ac6d-749e7254c992 | -2.54996 | -47.71104 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fa7398d-8251-3c9f-89f0-d85858b6d282 | -8.02822 | -47.01378 | 2025-08-21 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33b4dbaa-7634-32e1-b5b5-08976c5dc2e1 | -8.69052 | -48.51593 | 2025-08-21 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f7e1db8-e365-3caa-a04b-ce791a836c78 | -5.37418 | -50.89805 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2a5c684-37c3-39ba-9197-9f04ce3f32cf | -6.07073 | -44.11454 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48ea59fb-1f25-394c-af30-dc962d719bd1 | -7.70461 | -44.02397 | 2025-08-21 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9d73560f-bd2b-381e-a3d4-146d707cff10 | -2.69853 | -48.21383 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 425429d3-4295-3d21-a306-842ddc8e9e6b | -6.66119 | -51.57352 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c02cd9a-9d7d-31a7-9987-ff8a1ae112f9 | -8.2842 | -47.27914 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67a9f955-7b92-38e0-905c-1e978ae96874 | -7.85554 | -45.19083 | 2025-08-21 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9da8c27f-1ca6-3b8c-abe4-afa0406b7d2f | -5.9663 | -44.13977 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9ded01a-57fb-30b1-bdc7-a82536df45b3 | -2.34966 | -47.47132 | 2025-08-21 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d535052-be91-393c-a576-891f83b0142d | -6.82931 | -44.43326 | 2025-08-21 04:38:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d9cbc87-1e84-3392-88db-7df88fc2325c | -5.10368 | -43.15996 | 2025-08-21 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68b8576d-da9d-3445-804a-5802badd86a1 | -6.31517 | -43.7537 | 2025-08-21 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1c2ddf0-9d36-31be-8c95-5a7478ad6af1 | -6.94805 | -42.86179 | 2025-08-21 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7aeb22ce-e6e6-3718-956a-8171dbe09147 | -7.63888 | -45.24633 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 794042e9-4138-3b33-9647-64c54c7b27dd | -5.87536 | -50.14782 | 2025-08-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6cccd00-486f-385d-a567-6ceb4d3fa196 | -6.29146 | -43.88483 | 2025-08-21 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95e4692a-a930-350f-955e-e333be2c836b | -2.91193 | -48.30398 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35ce5238-43da-36f4-b1cd-5880c05caa17 | -5.10738 | -43.16481 | 2025-08-21 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1489cbc5-6655-335d-905e-0e15e911066f | -6.10191 | -45.41054 | 2025-08-21 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 201f1551-68d6-3475-93ae-6b7adc069c0d | -5.96831 | -44.13317 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8506bfe-4ed9-3897-99b9-e42d890458ec | -7.64669 | -45.24755 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bb25fa7-458f-3f06-bf51-30ec100c388a | -7.14715 | -44.64616 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ada18ce6-536f-3cf4-90f2-e2690060b1dd | -6.22266 | -44.12171 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6d6faac-cc9d-35f4-95b8-358c61a32c0f | -3.74917 | -49.04868 | 2025-08-21 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7a4d2ad-bd73-3efe-9e7c-d9b344a51305 | -8.79638 | -45.43535 | 2025-08-21 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b94c5ce7-95bd-3184-b303-e664dd497943 | -7.61958 | -45.26859 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d283724-93e5-3e86-84dc-0820deadc54d | -2.44643 | -47.32673 | 2025-08-21 04:38:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78872068-72eb-30e4-b536-81b19608f933 | -6.96327 | -44.16782 | 2025-08-21 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e243890-68e0-33d9-9786-7b9c39361b2b | -7.64353 | -45.24445 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8376cacd-74e1-39bb-b42c-cbd4d1c8c73f | -6.07431 | -44.11864 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7da4ab3-be71-3853-a0b3-a5e88628428b | -6.34855 | -55.56019 | 2025-08-21 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3d5b5b22-c7b9-3662-b4f1-12b974a9faa5 | -7.58818 | -44.38345 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d658188b-a0d5-30b3-a514-706653aae37c | -6.0135 | -44.35645 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc55d97a-e05b-3f0e-921b-59549be42d36 | -6.56125 | -44.47811 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92dba26a-ecf7-318f-bae5-8738926a6f15 | -2.29527 | -47.99167 | 2025-08-21 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62ddf21b-03d5-3618-acfb-654e82683ebc | -6.41004 | -53.36172 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dafd7c53-d9b0-384d-b012-fdfde0d5bbe9 | -3.83013 | -47.73199 | 2025-08-21 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 261d7f0d-8bf1-3daa-b53b-59e0f6ecb5fd | -8.15107 | -45.5544 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e7ccc7a-92fe-315e-b0bf-980b4388beec | -4.30828 | -48.10514 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa7b3c30-c346-33ba-949c-e2d493b58798 | -8.3825 | -44.60068 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a6df9d8-e2c0-39fa-af03-fb2682e90b42 | -7.63433 | -45.25295 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2d92664-23eb-3344-bffa-d7889d0a370e | -6.77742 | -44.33619 | 2025-08-21 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fefa05bb-2969-331e-8ede-2ad92c8903b3 | -5.85414 | -48.79615 | 2025-08-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f84e43fd-99c4-3954-89db-fab74c51137d | -6.28928 | -43.69423 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6dc1643-01b9-368b-aac8-53993983e544 | -6.17776 | -44.7301 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb5df588-498f-3081-994a-ac068b4b8ad5 | -6.02101 | -44.36145 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30944a91-4436-3223-9917-77c04b9f6468 | -5.79954 | -45.00683 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51c3c246-0874-3bfa-b69b-b22829947a22 | -6.22155 | -44.12931 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e48bea4-dc72-3243-83d7-178c9b3fc885 | -4.83639 | -42.69202 | 2025-08-21 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48cf280f-ecc5-3b24-bd88-5b369fb4fb02 | -5.68054 | -44.97242 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddd163ed-731b-376b-b24c-864044e57bd6 | -6.41752 | -53.38626 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 852e72e0-e481-3f27-bdaa-c2dc6f77602b | -6.02131 | -44.38692 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aeedb869-6d0e-3ec6-8fe0-3185cfec874a | -4.77981 | -44.91634 | 2025-08-21 04:38:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76e23f87-3057-3614-b73b-eea4f7d7b197 | -5.4055 | -46.22115 | 2025-08-21 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7db9d803-72fc-35df-a5ce-4aabec763da4 | -6.0788 | -43.4465 | 2025-08-21 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84e9ba35-7ae6-3ddf-b927-fb819d9bc6c9 | -7.02961 | -44.62577 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0c28733-994c-333e-87ef-5c7e85a17c9d | -5.79247 | -45.07977 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4354560-2f43-36b4-984d-6330ef10063a | -6.26929 | -42.81971 | 2025-08-21 04:38:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bc2cfa5a-c6a1-3b36-a444-8d31dade002a | -5.13552 | -56.97356 | 2025-08-21 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a464ce83-42dd-3ec3-958b-d7668274bb14 | -6.01663 | -42.82198 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 82dd40ea-764b-3ffa-8501-aad965e6069f | -4.47815 | -47.66747 | 2025-08-21 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f5ba7b3f-deea-3c9b-a800-53dfd09849f9 | -6.20411 | -55.63202 | 2025-08-21 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0e12b6d-acd5-3461-8853-ba8b4971acb5 | -8.30371 | -47.6054 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f325bb6-5c02-36fd-9306-4a5d6b551e67 | -7.38363 | -47.04457 | 2025-08-21 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 567df7b4-1c7c-360c-8a53-761a446b3b3b | -2.92887 | -48.23944 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1040d44a-49ff-3a3a-a9fc-3eb6917cbfce | -6.58366 | -44.46603 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2e29c70-56b1-31c2-84fa-4cec2b88f196 | -7.38381 | -44.27448 | 2025-08-21 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64708eb3-2e86-325a-8f5e-e1fb31511f85 | -6.50452 | -43.44265 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d1278cf9-d2d7-3796-be15-c2a3ee5f81f1 | -5.96682 | -44.13617 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6f43ddf-13af-3fd3-9241-b0feb61eedf8 | -6.26878 | -53.65215 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 123d2866-5105-392a-8528-d8f56db6a8eb | -7.70376 | -44.02684 | 2025-08-21 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41131def-964d-392f-90ba-4e46ab5e20fa | -6.42375 | -44.66827 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64659832-077f-3012-939a-f2a2766c7c08 | -7.2751 | -43.68119 | 2025-08-21 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c39c0235-b989-30e2-9f04-aa4461553902 | -6.02854 | -44.36633 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e29df0d6-7ffa-3be7-9e32-4aaf81bf75f8 | -7.61568 | -45.26799 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 534151a8-d986-3056-b09f-eb02577a8306 | -8.34048 | -47.50384 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e4f52f7-c13e-34ad-8e79-379b2c5395a0 | -5.87066 | -42.41244 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4e8120db-7297-3d43-a0db-13589dab6ce1 | -5.87181 | -48.11803 | 2025-08-21 04:38:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cc4dd4a-db4b-32f6-b51b-07b01291f52f | -8.16419 | -47.35436 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1d0c263-ea63-3c3f-bda7-fabfe3fc8d3f | -7.03068 | -44.61845 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 036f1648-b54b-359d-9913-325df4c192b1 | -3.93537 | -50.44291 | 2025-08-21 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cbd24cf-b009-3389-a355-095887eade87 | -5.08616 | -47.71599 | 2025-08-21 04:38:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 951ddd27-a475-3385-a0f9-1ade0a3abe07 | -4.31216 | -48.10215 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9421488a-e8d5-35d0-b605-59c0d4b7fc2d | -5.66877 | -43.50978 | 2025-08-21 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e350c698-981b-33b9-910d-f353e50cf9c4 | -7.64829 | -46.26781 | 2025-08-21 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baaa0c24-6631-3cd3-8bef-9358c38526c7 | -6.76972 | -44.33166 | 2025-08-21 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1035520f-51fb-36fe-a570-0bd5a8e299b8 | -8.82279 | -47.47267 | 2025-08-21 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c4d75b5-6572-33ae-9862-f207bfb951bd | -5.78934 | -45.0744 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 096765d0-9a08-39c7-a80e-6de734d4c894 | -6.36177 | -43.25602 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a040d37-138d-3883-8b32-a7d76d1b7b1e | -6.61959 | -43.8861 | 2025-08-21 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 356c59ab-fe7c-31be-8584-4a7d6fd040f6 | -6.07104 | -44.14027 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff1adf5e-09c0-3de9-a91d-a4ae60af94ee | -6.06693 | -44.13971 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab34b186-19a1-3f04-b7c9-ced24568a553 | -4.64355 | -41.40757 | 2025-08-21 04:38:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eb0476ae-56ff-3379-902d-51633df4b5e9 | -7.018 | -44.62062 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ccd9a4e8-48c9-3153-8e5f-0a33c172a133 | -8.34746 | -47.50494 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ec41120-af17-3cb6-8419-9c29a36ed6ef | -6.03393 | -44.38532 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 909fd0e5-fad1-3438-b28a-341b78ecd11a | -6.09858 | -44.63457 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README39.md)
