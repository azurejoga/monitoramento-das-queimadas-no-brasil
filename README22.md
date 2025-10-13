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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7cdfd90-0ba7-328d-a968-d8cc9e685a8e | -6.73923 | -42.20679 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6c0b50e6-4988-3641-9df0-996f8210572d | -10.14231 | -44.55538 | 2025-10-13 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bdd7251-ab8c-3e82-b531-34401b14059e | -7.49373 | -42.15102 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| f3c2d3f0-31e3-3a0c-9f1f-d1f357b23dba | -7.83742 | -44.52771 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c22a622-0df6-375c-98a0-ae21700967ee | -10.80404 | -43.97259 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c93daaf-08c5-305d-aff0-ddacac3c679f | -10.82004 | -43.98265 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c80b93ce-a929-3b3f-8653-9a2a493eaef2 | -6.74573 | -42.16352 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 83a8983e-8a48-344c-8c03-2b134ff9762f | -7.26823 | -44.14688 | 2025-10-13 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e8b83bb-cf78-3e13-91fb-9f424b67dc49 | -6.64349 | -46.71463 | 2025-10-13 04:23:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59bd371b-b3ca-3fe3-8821-6213fa539d36 | -7.91607 | -47.2175 | 2025-10-13 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 843a0377-00f9-31a0-974c-f3a27a3b8179 | -7.05208 | -40.32366 | 2025-10-13 04:23:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 48f926cf-eac4-3395-8fdb-60fd6d8d8dac | -7.75544 | -44.20532 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74a99b66-f224-342b-9553-d8523f43f9de | -7.02664 | -46.97992 | 2025-10-13 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| adacac76-b5a3-3408-9b24-fd30729e03c2 | -7.64877 | -42.57155 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3b037bf9-ba73-34cc-9ede-c14ed6e05327 | -7.4873 | -42.757 | 2025-10-13 04:23:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6ed5399c-a81f-3ad9-b773-53b8aa9fb807 | -7.69658 | -42.37614 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 64a030ae-0b6f-3676-a394-869c602154fe | -7.54366 | -46.09636 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ce321dc9-1a89-3f02-aa39-5555c1ded51a | -7.35168 | -43.85526 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06a6a2d9-7868-329d-ba6f-2c8983057eeb | -7.80552 | -42.44025 | 2025-10-13 04:23:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 134cde6c-ea09-371c-be44-2b9ce897d138 | -6.2927 | -46.72091 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 961878fe-d253-3244-94fc-991da699e035 | -7.37456 | -44.06995 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9c868b2-b009-3027-b1c9-8326630e09ae | -10.8206 | -43.97892 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cc7ae06-987b-3c8a-8476-733c9cc8ea15 | -7.49451 | -43.06791 | 2025-10-13 04:23:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b1ea4106-aeda-3257-b2e6-903a3e21b611 | -7.28866 | -41.95999 | 2025-10-13 04:23:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2a37911c-734b-3d2a-a1f0-b0fb3a30f4c6 | -8.40284 | -45.06076 | 2025-10-13 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79587c45-aa07-3810-a760-30d05dce6c3a | -8.3232 | -46.2392 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33a2b129-bfa9-3d2a-b20e-845a899fe5c4 | -6.28104 | -43.90287 | 2025-10-13 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e59f8af4-8f62-38e9-87bb-6175cb8e08fd | -7.49636 | -44.6526 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d91fa244-4e02-3cc8-8ee3-58097e5762e0 | -7.77684 | -44.04538 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b099311-edfb-3a08-8c7b-efc7cce110e2 | -7.04999 | -41.52501 | 2025-10-13 04:23:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4728529d-85a5-36d7-aba8-ce6076e74a71 | -7.68806 | -42.57672 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 26a3e9e1-8f77-3e02-8ae9-87f3baeed0e7 | -8.23733 | -43.36603 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f3ecbe1b-5e8f-38f2-bb84-2d7d278252b7 | -7.05782 | -44.2617 | 2025-10-13 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d168c9c-e6fc-3628-8857-2180035fed44 | -7.46047 | -43.88328 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a821e710-c853-3a6d-9416-251925dbb3da | -9.33185 | -40.87549 | 2025-10-13 04:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 72ef39b2-7648-3d8f-b46b-42744f34f43c | -7.75319 | -44.19772 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a0f78eb1-aa77-3443-b8d1-3e77d874c72f | -8.23276 | -43.35008 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5a94816d-7c58-3349-9c4d-900189814263 | -7.68164 | -42.57168 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 434a638e-a371-311d-b221-f95505590cd2 | -6.73694 | -42.08553 | 2025-10-13 04:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e0ca81c8-69b9-3326-a603-c333895de275 | -8.22991 | -43.34582 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 63d7b7dd-95e8-3f86-873f-b8e96f98c1f4 | -6.77168 | -42.82609 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 25150de6-3614-3250-9585-59d02da6e1de | -7.79785 | -42.44313 | 2025-10-13 04:23:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 6befa09c-7677-3589-8e38-4e7a62f2efde | -7.5015 | -42.14806 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 984ed34c-9149-320b-afa9-e8761639a83f | -8.45342 | -46.12546 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 199bd547-bf0e-3d28-b3d6-61da4e2a9810 | -7.55738 | -43.83623 | 2025-10-13 04:23:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7ee3114-af18-331e-a1e6-1c5794f7206e | -7.64466 | -42.57488 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7110bb94-eb81-309a-823f-a3ab3c25047f | -10.78867 | -43.9635 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0bf8299-d12d-3e6b-8c81-59ab6ed5da71 | -7.53877 | -46.09571 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8a80e5ad-5acf-3b64-be0e-0105ec07b534 | -7.37736 | -44.07399 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8321bf7d-ce73-357c-9603-181dc9bd48a6 | -7.35908 | -45.19801 | 2025-10-13 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f156219e-d886-3e3f-b429-79682ffa5e19 | -6.64289 | -46.71835 | 2025-10-13 04:23:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec68d30d-f584-36b0-92ed-961f80dca7d3 | -10.80691 | -43.97682 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 609ff1f5-e07e-3593-9d19-61d09e4efc41 | -6.6334 | -44.65534 | 2025-10-13 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f283b235-2b00-35fc-81b8-45d76ef29c8e | -7.88787 | -44.8076 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67c86490-1d16-378a-a2d2-5da23a74987d | -7.48797 | -44.61916 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 668495c1-a58d-3047-991e-e35539b663bb | -6.70399 | -45.97285 | 2025-10-13 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dc7a775-7ac6-3136-a4c5-f3f98b08c174 | -6.75003 | -42.16531 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eec8554a-126f-3749-9f79-9996f8be60af | -8.45121 | -46.11779 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 16b26080-8ad8-3b3e-87c7-64cf91f7bdb9 | -7.5403 | -46.09582 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7a8a8578-4d05-396e-8228-27f6c0d958e7 | -7.02602 | -46.98372 | 2025-10-13 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 858fbf7e-4077-310b-8f34-cbe196ef3889 | -7.64406 | -42.57875 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 47859112-67c1-3585-84b2-5a943702b6a2 | -6.88838 | -44.69237 | 2025-10-13 04:23:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 626461ba-6272-3f7a-8364-fc66bce6f638 | -7.48671 | -42.76081 | 2025-10-13 04:23:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5f2c6742-2c49-374f-997e-ece3ae1c3868 | -8.32542 | -46.24688 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08951ad4-86e2-30d5-9e88-8e9187f79659 | -7.05448 | -44.26117 | 2025-10-13 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8955b1d4-5c97-3756-b43b-7501b0c242b5 | -7.10373 | -44.26498 | 2025-10-13 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4257dd0-a89b-3aa8-93b6-06258e22a8f2 | -10.79152 | -43.96775 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4992d702-ac7f-3b5f-87ae-ee07f2107597 | -6.51151 | -44.4405 | 2025-10-13 04:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34450bc2-2494-3413-ad96-fba3e6aa6986 | -10.81376 | -43.97787 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53aabb50-181e-3d13-a0e9-7ab25b910770 | -8.54012 | -44.59113 | 2025-10-13 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d36c7b5-106b-352d-b1fe-a66ade918bea | -6.29209 | -46.72467 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 385b7a8c-bfca-368a-bfdf-9e50b7e1a08a | -7.49964 | -44.63173 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f30d941-2a2a-35f5-94ff-b95bf4b8cc96 | -8.21504 | -43.32833 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a17a1fe7-f06e-37cb-9210-06b954c13372 | -11.59879 | -47.52005 | 2025-10-13 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e681407-0f70-36d6-b4a2-137b19e3164e | -8.4961 | -44.72824 | 2025-10-13 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfa2bee4-ab86-36bd-8ac5-b8fab44a410a | -6.76998 | -42.83725 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c25d16ce-20d2-364f-b2b3-920a401045a9 | -7.44217 | -45.147 | 2025-10-13 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 422fa165-d013-3c98-9969-3aed99e7cbd0 | -8.54493 | -45.42348 | 2025-10-13 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e79ee7c8-ed8e-36b5-a532-1860fc67bb04 | -10.7995 | -43.97948 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4640b678-6d7d-3926-a008-830e5f09e736 | -7.43552 | -45.14595 | 2025-10-13 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9e7d9a2-e617-3fae-8f3f-f3d8a404f878 | -7.91669 | -47.21369 | 2025-10-13 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 511e573b-7e83-3e37-81ce-4e0530d6f155 | -6.27769 | -43.90237 | 2025-10-13 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 871dbd51-fe30-32dc-bc77-ab673c721fe6 | -7.49408 | -44.6237 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fdb638aa-20cc-3c53-b7c3-e6c0b0d83711 | -8.53678 | -44.5906 | 2025-10-13 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9757d5a-88fe-3d5d-ab77-56b2949c3318 | -7.52225 | -44.29111 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fc8373b-908b-30d2-81ca-645857e24360 | -7.49792 | -44.59926 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77b22f92-5ae5-3332-87d2-92ab2db38937 | -7.35338 | -43.8521 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eff88a04-af34-34de-876a-83ce3a2b5a50 | -7.1465 | -42.51398 | 2025-10-13 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 77e57555-3d27-37f3-b10f-94f831e46744 | -8.48999 | -44.72367 | 2025-10-13 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 748b0bab-e10d-3a6c-bdec-eeb646a3ff87 | -7.49019 | -42.76134 | 2025-10-13 04:23:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c588132-af9d-3ea3-8691-7f7800468ed2 | -8.45399 | -46.1219 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ca432d5e-a123-30c9-8ac2-faab65c9fdac | -6.63617 | -44.65934 | 2025-10-13 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5d33bcf-294d-3af9-9ada-beecd58e3a0c | -7.1389 | -42.51685 | 2025-10-13 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4a28ec07-9e76-36fc-8305-46e54e311948 | -6.69869 | -44.30554 | 2025-10-13 04:23:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 354bbc69-56be-371b-9760-ac77a4e8782a | -7.28147 | -41.95887 | 2025-10-13 04:23:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be2568ca-38ef-3212-af5f-7706431d66f7 | -7.64757 | -42.57932 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e73c23bf-3696-3a4e-8894-f2a6f0503ad5 | -7.50297 | -44.63225 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fc923c7-9827-3819-a415-d6c9af9aec78 | -7.54762 | -47.32518 | 2025-10-13 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7436a2e-26ee-3cd9-8bce-c3cac900446d | -6.82072 | -44.64606 | 2025-10-13 04:23:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0469a842-a0a5-3d8b-89e5-fdcb3a097547 | -7.14883 | -42.52226 | 2025-10-13 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README23.md)
