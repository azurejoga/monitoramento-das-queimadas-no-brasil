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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63100b39-2b9d-39c2-aa62-c56540ce00a1 | -4.66768 | -45.79238 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c8b9ca82-61d4-38c9-a4ae-4cfbeeda9ea5 | -4.65811 | -45.80123 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 39c484af-3e89-3111-aa5b-6428fe6c03a3 | -7.77319 | -47.37389 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc9eb001-cabf-30b1-a654-bb22b2663e10 | -7.73998 | -42.59824 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1bcc51a7-6ed0-350d-9745-57e9272cdf8a | -6.72857 | -44.14125 | 2025-10-03 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25b3b736-7dfc-3336-a873-bd2129d25be1 | -7.05454 | -43.28574 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 26b13355-e8a4-3a8d-983f-2985924b9c6d | -6.66677 | -42.78686 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3e45205e-95df-33e5-b1b0-d72d0986a93c | -7.75599 | -42.55455 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 81a39f99-6d12-3b6a-96b2-9087f610a5e4 | -6.85325 | -44.7804 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 385da28a-132a-3ef5-b6dc-cbbd35675fa9 | -4.67478 | -45.79851 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 752f72c5-f6f5-37d3-b660-d08f5cee34a8 | -6.41281 | -43.92783 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc847cb5-4644-39a0-9c0c-12b0a5693a8c | -7.42126 | -40.07467 | 2025-10-03 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4f0f6b9b-9f35-3bb1-bf7e-b7bbdb129c4b | -8.44908 | -41.8981 | 2025-10-03 04:10:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c291bdf5-d874-3a58-ad90-9635ece80867 | -5.61762 | -45.95283 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22665d41-584e-3017-aee2-5fcb5f104660 | -8.17285 | -44.15995 | 2025-10-03 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| affc238f-c2e1-337f-9443-0edfdb895dda | -7.29203 | -45.26701 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc7a741b-8331-36ee-b38b-d2c7ab80f82d | -6.28843 | -43.63295 | 2025-10-03 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d5baae4-a342-3c9f-ad61-d8c88e783b68 | -7.77387 | -42.50701 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6f4d8e5b-03c9-31bd-b612-4c61e6afe97c | -7.77673 | -47.3783 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34a350c0-df47-3e5c-88a6-222e9fd4ac87 | -8.4524 | -41.89863 | 2025-10-03 04:10:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 54fafce0-9dd7-3e17-a49d-1f2966ff8ee8 | -5.17838 | -42.83278 | 2025-10-03 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a192db61-cd3d-30e4-922e-55a5853c531b | -3.4529 | -40.23233 | 2025-10-03 04:10:00 | NPP-375D | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0cd4f6fa-90c6-3d09-8449-71b3129fa35a | -7.75767 | -46.25838 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 8c249085-dd74-3476-bfa2-c9219c6e4455 | -7.75543 | -42.55805 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 12f4e050-f37b-3b59-b06b-42134cbb2807 | -7.79747 | -46.0198 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27ad76e8-78ca-3258-ac2e-2ad6c8302130 | -6.51381 | -42.4972 | 2025-10-03 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 46586fd5-b2d1-30b0-b660-90d611d8b2a2 | -5.48018 | -44.86866 | 2025-10-03 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30062856-c16c-36f4-9b53-9193c8a537db | -7.29481 | -44.18825 | 2025-10-03 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c028121a-b207-3f9a-9bbc-017356ddbc33 | -6.6835 | -42.83338 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9bda2ce2-8579-3b39-8359-5a224ebb3851 | -6.66004 | -42.78579 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d6f8201d-fc01-347c-b18e-aa7e6291d019 | -6.68242 | -42.81855 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6505abd3-f127-3f43-b671-2fef931e28ce | -4.31709 | -38.12775 | 2025-10-03 04:10:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0c6a6a64-a4aa-35fb-962b-21a844b88e35 | -4.0138 | -41.79543 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 488eae22-53e6-3fe4-906a-744b7bef05e3 | -7.05715 | -43.22617 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6b25e2a5-6bb4-34d1-b49a-a5e10f043d8a | -2.92726 | -48.30449 | 2025-10-03 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2760257e-35ea-3ddf-a79d-336b43817d79 | -7.5619 | -42.39355 | 2025-10-03 04:10:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2427c04d-5c08-3de9-b834-fd117b77e9c4 | -7.31553 | -42.87961 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| baaa091e-ce61-3288-b9f9-8affdeba8df9 | -4.6247 | -49.37517 | 2025-10-03 04:10:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6f4e8be-3e68-3fba-bb81-c5618b0567ff | -4.48031 | -47.67317 | 2025-10-03 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f951a918-b15f-3bb8-befe-8be8fc44dc2d | -7.79405 | -47.37726 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 081c7bdd-dcec-3f8e-98f6-4644c6dfbf6c | -7.74166 | -42.58766 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d568fcd7-09c5-3c10-8ccd-05fac74cde43 | -8.04308 | -44.11616 | 2025-10-03 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3c0a616-96d5-3f0e-9646-af94336a44db | -7.78047 | -42.57287 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 42702784-344b-3bae-afb9-615122e17fd4 | -6.34448 | -44.30462 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be1f15fa-8bda-31f3-b88e-8d812c82f8fe | -4.85502 | -44.51598 | 2025-10-03 04:10:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0e2f4d00-eac5-3a89-86e8-12690a54b3e6 | -4.6534 | -47.54599 | 2025-10-03 04:10:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37fc22bc-1647-3e6c-84bb-df0c04c409db | -2.24916 | -47.88125 | 2025-10-03 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 6f81e31a-f6e0-3de5-b4c5-59ab3b8b017b | -7.19973 | -45.38737 | 2025-10-03 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa75b884-b8d1-3ba9-8387-c641a0b62dab | -6.21798 | -42.50767 | 2025-10-03 04:10:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2a2abded-7824-3cd3-8eed-9f074c034103 | -6.05537 | -44.61341 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0da8ddb1-c23e-3641-a368-8fdf4e91ee7b | -5.96846 | -44.22347 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6d61623-714d-3b8e-9ec6-7431cfb599d7 | -4.55713 | -50.4665 | 2025-10-03 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9dd3e35c-a727-3efe-a02d-6c5c1496e820 | -7.79341 | -47.38106 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 623fcee4-4709-3542-8c36-924cf66a93e0 | -8.17347 | -44.15613 | 2025-10-03 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb330871-6391-3017-89e9-a8308f897ab1 | -4.65331 | -45.80568 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| effde6e9-d9fc-3303-91e4-d3205bd08bcc | -5.35239 | -43.74794 | 2025-10-03 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3f124ba9-2a9b-398a-95d8-25bcd726c38f | -4.64025 | -42.52928 | 2025-10-03 04:10:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a043e61f-2861-300f-bb4f-c08bfef60b67 | -7.75694 | -46.23891 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1592cfbb-80cf-320e-b1ab-cbc6dc73c025 | -6.24332 | -45.35094 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 080747b4-ebc8-39fa-a210-015159f4fad4 | -6.23028 | -44.27516 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dba7d44c-bdc8-3bd4-801a-fb5761578c07 | -6.70262 | -42.8219 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4458a005-74b4-34b7-ad10-11bb45a0b011 | -7.84895 | -42.86252 | 2025-10-03 04:10:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 24a72e19-4868-303f-b0cc-45df005609be | -5.44528 | -44.82729 | 2025-10-03 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91ea6962-feed-3d18-b3a0-eadab3bc2957 | -6.72411 | -45.97173 | 2025-10-03 04:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb990b6e-7c08-3326-877f-0e3d75cf82c2 | -6.24063 | -44.2564 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ebe00386-221b-3926-b1a6-6447865f2d9f | -7.74389 | -42.59525 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 706798fe-faaf-333f-b173-60fd024afe08 | -5.38455 | -48.95654 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5457ba6f-788a-3982-a3cb-edc405ff69a2 | -6.28472 | -44.05175 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65683f88-9ff3-34c8-9de7-4e619c6ce956 | -7.78159 | -42.56584 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2909223c-6e58-30cf-81c1-5816a4136ec0 | -4.57513 | -46.50437 | 2025-10-03 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e54873b2-8be4-3230-ae5e-cdd1774f3c5d | -6.85286 | -44.78146 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f96249d-b0f2-3bad-9658-8b2e1c6e1562 | -7.7577 | -46.23436 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c21ee09-96b0-33b0-9120-22cf5ca1e2b8 | -7.32004 | -42.87303 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 42e5b768-7a6e-3c02-b554-ac523385a3f7 | -8.30434 | -44.85265 | 2025-10-03 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd5d5dd6-0732-3386-8ef6-72955a1aa641 | -8.59344 | -44.78065 | 2025-10-03 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb1ce47a-3252-378f-b269-f4ab27edff9b | -7.77487 | -42.58641 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 1dc34a2a-58c5-38c2-80a8-60d13c8df4f0 | -7.7504 | -42.56805 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 20ba8384-2832-3b03-a2fb-637338595fdc | -7.78381 | -42.57341 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a2e429d6-d5a5-316f-a051-03ab8307c84a | -5.61768 | -51.93768 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3d7b96d-5bdb-3424-9a56-45ef830dc431 | -5.62722 | -43.92263 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3f81c4e-257d-32a8-8656-d5861ceffa7e | -6.23461 | -44.22625 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c508f745-c6cb-3862-8e7e-af000a422fcd | -8.24873 | -47.02292 | 2025-10-03 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fcaa41e-e46d-3d17-a2d8-87b6e5a5bddb | -6.67905 | -42.81799 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f4d22a9-b352-3ed2-9545-8b6b43fc9ef8 | -6.94241 | -38.56698 | 2025-10-03 04:10:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7ccd5fb0-e98f-329c-8fa5-431e2bf71cb9 | -7.90621 | -43.52625 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f6d12afa-6da9-38fc-9a48-1a712814e465 | -6.2403 | -45.34586 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 081a566c-a66b-359f-93c2-fad5d5529003 | -7.48574 | -43.03857 | 2025-10-03 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4469a315-c696-3e1b-9ff3-549c50edd3c0 | -4.67164 | -45.79299 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 4c67c50e-9c89-3600-9363-a4b2fadec3cd | -8.33366 | -46.22221 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c66cef9c-2e38-3971-9179-e74e0cd86d38 | -4.6652 | -45.80737 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| bb37e3b7-55a1-390d-9eed-75e7b80dbac7 | -7.94477 | -47.30227 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a9a37a8-e976-3316-8827-c1fc0ab976f5 | -5.48879 | -52.13197 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1eb48eb-7e4d-3d3a-8039-23f5929dab24 | -8.5892 | -44.78414 | 2025-10-03 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b5d6d291-1328-3bd3-92cc-839fdad222f7 | -4.44028 | -43.38647 | 2025-10-03 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f82d0b00-5ae3-3014-a497-e09d7fb5b3a3 | -5.78614 | -47.06615 | 2025-10-03 04:10:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95f1c192-2a07-3b5b-bd29-979fade3ceff | -7.73142 | -46.22469 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2637f6a8-9cd9-3076-a601-d99113d26f4e | -7.7665 | -42.59591 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1ac8ba17-ec4e-3395-8a22-08e215831357 | -5.34637 | -43.76297 | 2025-10-03 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b051a8f6-bba5-37ee-9ef4-c64b2c4c022a | -4.64621 | -45.79957 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a2fce38-c119-3116-9813-f446be1edce2 | -6.32225 | -43.88614 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README50.md)
