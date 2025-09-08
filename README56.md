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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa171b1c-146e-3ed6-90c0-115b69d152a3 | -7.40208 | -61.63488 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 63c44a13-3e05-36f9-a6b3-881f3048436f | -6.59785 | -44.00635 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9181761e-f6e1-3eb8-9785-0da181913b60 | -7.66943 | -50.29659 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c8eb0564-a7b1-346f-b97e-21650a2699de | -8.03532 | -44.03485 | 2025-09-08 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0eafa80-888a-3c53-8e92-e45032d872af | -4.99419 | -56.25327 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4c4ed5f1-c279-35a2-b614-695cf8e995cc | -10.00052 | -51.65656 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ef4e397-dbf8-3cde-9b7f-98cbc8dcec83 | -9.95422 | -51.19071 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0d6637b8-e16b-3748-828b-c084e58cc734 | -6.22714 | -49.41578 | 2025-09-08 04:51:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0f5fdd2e-d18d-3af1-9fd5-72d09ae4ea09 | -7.78699 | -52.13689 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35981849-1bd9-367b-84cb-5f7f3603434f | -9.24096 | -57.06804 | 2025-09-08 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a60182fb-f8ef-30d8-af35-f7534c8bda0c | -8.48634 | -45.16943 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 360cd2c8-1046-3d26-8a6d-396057318cc5 | -7.82562 | -45.42336 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dddb99bf-7c7e-30aa-a07d-dfe76d62ebb8 | -7.6195 | -44.6659 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba913c25-c482-3b16-90d3-cc5c577c3beb | -10.46895 | -53.61353 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a86600ba-b375-3090-baad-567788a89fc6 | -10.0016 | -51.62601 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d7e44ec-3915-3515-9d6f-a660298b34a0 | -6.95083 | -62.92875 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6cd1bb88-3d3b-32d3-81b6-5589042884cc | -6.37819 | -45.91342 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2782c556-3e25-35e7-aa4e-12fb50bdf2e7 | -9.32969 | -55.18965 | 2025-09-08 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caa4660d-37af-36b1-a83e-1ef075d3c360 | -9.51368 | -48.25205 | 2025-09-08 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97142e44-f052-38f0-91eb-d3ca06d68d6d | -5.9126 | -52.46575 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e5e5701-ab9c-3d44-bf5e-dbbe43c065dc | -5.42331 | -42.855 | 2025-09-08 04:51:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6cc1957b-f398-3459-b32a-36fef6a3f880 | -6.23323 | -43.50955 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3feba196-3d9c-3316-a3ae-7a18eb32ef64 | -8.16205 | -44.85093 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59317516-7d27-38ee-83f6-f16f419e9dfd | -5.676 | -45.45224 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 004682c1-db48-3f60-b4ec-f190fd8150be | -9.99603 | -51.68646 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6a73f14-e466-39a6-8da2-502b6318deb9 | -6.92286 | -44.34094 | 2025-09-08 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e067728b-6229-35df-83d5-9c7b48515c5b | -5.871 | -44.18648 | 2025-09-08 04:51:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7f39fe7-9089-32a9-bd94-12c078f1dc6a | -6.20312 | -53.26165 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 451f0ae1-04de-310a-a34a-4d72c3099090 | -5.88066 | -43.96438 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68da5dd6-424e-356a-a513-92b442ac89e5 | -6.61308 | -44.01136 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e042155e-2f50-3d98-8342-44c0319300e3 | -10.00901 | -51.62326 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 732c58ae-9afb-349b-80bc-274676d3ee1b | -6.35547 | -42.59043 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bba52e15-9a8f-3102-8a35-089868acdc9b | -9.20488 | -59.38667 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9084ecfc-d245-31b4-bda2-3675a145ab99 | -3.73328 | -49.68892 | 2025-09-08 04:51:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9c5e9ee-fd3b-3d07-8e94-98c9d86f4d03 | -10.82436 | -47.73529 | 2025-09-08 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d060226-458a-352a-821c-ba39ed9eba57 | -4.66296 | -46.35604 | 2025-09-08 04:51:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f2e54f7-b3c0-3d67-b9e2-f669b84cbe45 | -6.82985 | -52.80154 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7a9ad2e-4526-3c6e-900e-a313c887c4eb | -9.81717 | -53.32348 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 088c7030-cb50-3ceb-b0af-df1340651c78 | -9.81663 | -53.32696 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 02a51c28-4817-3405-bc16-3a8fc39955a9 | -9.20116 | -46.05024 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a025311a-7a8c-3b17-95ba-30795a9ca834 | -8.8758 | -47.90644 | 2025-09-08 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 712884f2-3637-3ea8-bf76-accdc9d1951c | -6.64058 | -42.97149 | 2025-09-08 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5b2ba24-aea5-38a5-9a17-1a979e1523e1 | -6.46533 | -43.95781 | 2025-09-08 04:51:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b99a16d1-da51-3f0f-9582-2988b631faa1 | -9.78385 | -48.33932 | 2025-09-08 04:51:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14232031-7d21-3cca-ae71-5912310ecb46 | -8.20713 | -44.78399 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd3b1eb7-a5ac-3cc6-b91d-7a041d350438 | -7.08396 | -45.20291 | 2025-09-08 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c806293-784f-3c24-b2d7-7b71673d040c | -6.34699 | -55.55573 | 2025-09-08 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8b44d33-2ccd-3ba5-b3af-309353f92768 | -9.79815 | -46.23112 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 214072a3-896c-3798-8761-fed22a2a6172 | -4.26889 | -48.18627 | 2025-09-08 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2c3266e3-53ba-3055-82af-9537bdca4a47 | -7.39184 | -61.63311 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4b64b382-98ca-3ec8-820c-cae2bf6debe6 | -5.81045 | -45.65302 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6c9811b0-60dd-3a67-a479-97bf094c6307 | -6.2743 | -53.41526 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ec11959-1944-36de-8240-e6740d32219a | -6.26769 | -53.43561 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a54811c-202d-34c2-bcb8-850ded903482 | -10.47004 | -53.60655 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3d756ad-326e-3181-b6eb-6cd8c6d76038 | -6.63636 | -53.36251 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6963c353-6f6d-35f7-8d57-411175ce96af | -10.00394 | -51.65704 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 575be2d8-115a-3b18-b1e8-aba2090c9c70 | -5.43938 | -48.90466 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b63deac-7d86-36b8-961d-52889a560f3b | -10.4618 | -53.61596 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22466c94-4bc6-33a2-97dd-8fe53e919737 | -8.8924 | -51.0522 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b78126d-e4c9-37ad-9301-0cd04080af3b | -6.62199 | -53.34604 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4646449-1385-32c6-838b-9eded796aa31 | -7.11031 | -44.13924 | 2025-09-08 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5470a25f-7fd3-368f-8b32-cfe41876d9e9 | -7.77266 | -61.37512 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61f9df1b-e1be-3887-93c7-6f26ea4b0933 | -9.72507 | -43.97958 | 2025-09-08 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eecabb8c-51c9-35b7-b8a6-e49cc26387ef | -6.22142 | -43.59364 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 806a3511-2955-3acf-997a-af283f18ad49 | -6.86672 | -47.91383 | 2025-09-08 04:51:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e515c237-56df-3f54-b9e1-59c4e8286b06 | -5.44901 | -43.43921 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbf58f96-1791-3eea-b9a7-56c0b4c4ce8c | -9.1442 | -46.06567 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c45add12-a6f1-3a17-948b-b48d152fe3c5 | -9.18035 | -46.06238 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12f19b82-68f9-3c5d-b1b2-49f97524e0d1 | -10.14686 | -46.21516 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 39770063-b315-3cb3-97cd-3d8d43fd96aa | -11.28639 | -46.50064 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 744a25c9-75f3-3f7d-be95-00dce28aa425 | -8.62337 | -40.19979 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6a050236-30b3-37c3-a8fa-fd7aafeea8a6 | -7.08539 | -43.89057 | 2025-09-08 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cd10a12-38a4-30ba-b988-de85244aff88 | -7.82525 | -45.42383 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 422cec24-29b5-3ba2-a6ca-c3847d9a657e | -7.67541 | -50.25583 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e00fdfb-9486-3e53-bb3c-bc07e0dd2d42 | -7.56846 | -44.66951 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b87452f-fda9-3cb9-9f01-ff56333ee138 | -6.30598 | -43.83035 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 239775da-5a13-3199-ae96-629b95d736c8 | -5.96956 | -53.59917 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19526624-5bb0-35bb-b919-bcb0ce8118b4 | -6.63192 | -53.34759 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d35c7bf5-fdca-372e-8579-bf49b12e1b4e | -9.88822 | -56.14438 | 2025-09-08 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 73acebe1-0d85-3818-812a-5f3dc7f48193 | -6.2048 | -53.27256 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 972bd092-0688-36b1-8ec5-eb5f5e6b26e1 | -5.87722 | -46.0953 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6dcdc73-94ad-3643-886f-dca2bc9cb00c | -6.83645 | -52.80258 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5989e292-9548-377c-aa9d-c23f9f3957b9 | -5.87805 | -43.96874 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 967075c8-b00e-37b0-8c0b-b43ca24e998e | -8.85702 | -52.00751 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa55e6fe-4ec7-38fb-90a5-81a851d007ee | -6.25582 | -43.68814 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f37faf1-8298-3048-9e1c-af673fe327b8 | -6.44169 | -45.99894 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dd8f1d2-e13f-3f9e-99d7-9d95417b51fd | -7.70978 | -44.72063 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba0a3a1d-01ac-32c6-9bc7-9828d4e0c15f | -9.8221 | -53.31355 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 506bd988-5a36-3211-8a3c-6c048a1b767d | -4.64233 | -42.18094 | 2025-09-08 04:51:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 49696bf7-3b6c-33f0-9b63-50f6f4ec0722 | -9.88472 | -56.1438 | 2025-09-08 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 57cbd958-f345-3be2-b629-132b3a45cdcf | -9.17288 | -59.36874 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8b039819-647b-3685-afe1-39fcdee5e714 | -11.33698 | -46.57193 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d3e20c3-03dd-3265-9214-269a62ff4308 | -10.16096 | -46.21739 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb8b3df3-09cc-359f-ab80-9456724d833b | -7.18591 | -59.84074 | 2025-09-08 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17a9c347-e0e7-34e9-ac10-3482dd7d4289 | -7.94112 | -61.79664 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32719754-8d73-3413-a3d5-f67b8c29224f | -6.13902 | -43.29823 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3d023bd2-2130-3598-acdb-246c76260dad | -7.70441 | -44.79563 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be0f4158-99ae-3351-bd7b-7f72d931ef30 | -7.72766 | -50.3417 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0eb51eea-0b0a-34cf-b8cc-26e54266a594 | -8.21045 | -50.14068 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2b56ab7c-9d00-3f8a-9456-4a8da46b7fc5 | -6.30643 | -43.82716 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README57.md)
