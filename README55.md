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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| febcc213-4eff-3266-a28a-7f1f18ad149e | -6.12718 | -43.98176 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 84a25af5-372a-3af7-bf1e-4a1488b1f169 | -6.12825 | -43.97432 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 51b430b2-3949-3ef6-ad70-9b437bc568e9 | -8.11176 | -44.41441 | 2024-11-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6776f2b-3e62-3f27-a0fc-c2a32d09f763 | -6.50002 | -47.49451 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c43d5e13-11a3-3d68-a2c1-507680961176 | -5.23566 | -48.14569 | 2024-11-06 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0244539-34ab-30b3-800e-8bbecfd0c0a6 | -6.49031 | -47.48923 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| b4160e33-c4ec-38bd-a4eb-c031fff8e0e9 | -6.95541 | -47.86154 | 2024-11-06 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db9d648b-87b8-3da5-9f22-3b96cf051661 | -6.50699 | -44.68265 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6ee0550c-bfda-3da1-9059-2ef6ab419fdb | -5.39616 | -46.66244 | 2024-11-06 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50c9bb32-11f5-3197-8d4a-84f289a20651 | -7.26178 | -48.0343 | 2024-11-06 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53711b1c-5106-3b57-82d2-76559f57a15a | -9.60628 | -49.54161 | 2024-11-06 04:38:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a8b6198-0fa5-3720-b9af-3e2cb88c4c0c | -5.93652 | -43.77622 | 2024-11-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 361a3811-7dfb-32a6-8a0c-f2504d8fcbfa | -8.26113 | -44.85099 | 2024-11-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c98eebe-e4aa-3554-9222-00f7f7647002 | -10.52377 | -42.40105 | 2024-11-06 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1af49aad-ddec-3556-b175-606fb64d5864 | -6.4983 | -47.48277 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e299c23c-dfe8-305e-bb59-731ae9c9df2b | -6.42832 | -43.77584 | 2024-11-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fc1fc8d-cb4e-3443-8e20-533411d258b8 | -6.13194 | -44.70184 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cde55e9-317f-3f4c-bc1a-49774de37efc | -5.83973 | -46.27039 | 2024-11-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45092cf3-a0ae-39f3-b2ea-0aa86a0e77c6 | -6.12199 | -43.98853 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e5f77cb-3128-3fe2-acc0-a5bf08012738 | -5.19756 | -48.23692 | 2024-11-06 04:38:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d91ce3d2-72c3-37d5-baaa-9c713c195295 | -6.1334 | -42.55015 | 2024-11-06 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 78cdac75-acac-321f-ad75-f69456de163c | -8.31903 | -43.56477 | 2024-11-06 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49a6b631-84f4-3390-ac54-f99af4f6a818 | -6.12408 | -43.98512 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7d6a07d-7ae9-3910-94a6-3e19824f8dc7 | -6.66241 | -47.27962 | 2024-11-06 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97a84ed8-e166-357c-a5ce-cb6e8adc69d2 | -7.22251 | -42.88555 | 2024-11-06 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9782406-9933-36df-b0d1-293a8ccab34d | -6.58433 | -47.12744 | 2024-11-06 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df60eba6-0d04-38ef-9a1c-899ac0fa29ea | -6.72392 | -46.35519 | 2024-11-06 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36dae0cd-c4bf-3d25-9605-538eb83e46fe | -6.13815 | -43.96424 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fabbbebf-70bd-36d6-b58e-791fa757c6de | -8.28043 | -44.92477 | 2024-11-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ed6f3ce-fe94-398b-8fb5-dacb564aaf5f | -5.98736 | -45.36943 | 2024-11-06 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af5db202-3cbe-3b51-b38c-72e17ae718d4 | -6.50625 | -44.68764 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 118830f2-c71f-35b7-907c-5b23eb03adab | -6.51553 | -48.49867 | 2024-11-06 04:38:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b74009e-9588-3822-9ae5-6f1be6ca603b | -9.60351 | -49.53758 | 2024-11-06 04:38:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81c6a686-2835-3da2-a7ae-ab73454657a0 | -6.82108 | -41.32434 | 2024-11-06 04:38:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2e8eb167-82e4-3078-a13f-92807c9a017c | -4.40316 | -59.53432 | 2024-11-06 04:38:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f48bfbc4-6f85-35be-9276-28c7704b064d | -5.93987 | -43.77312 | 2024-11-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a9631ec4-5cc2-3e09-901b-13a237963af3 | -8.50345 | -42.08654 | 2024-11-06 04:38:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0c34bc3d-f704-30f8-9222-b9f1c84c8b6a | -6.49659 | -47.49402 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9d574877-c4bf-3987-b34b-d5d98c421f2f | -8.26283 | -44.84636 | 2024-11-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7786708-c328-3a5d-aaf6-b5cd081ab883 | -5.61171 | -45.92616 | 2024-11-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d21da390-be84-3de2-a3a6-67d7d54a7b56 | -5.6782 | -46.33029 | 2024-11-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68cb772e-0fa3-3141-8a8b-f290aed0c294 | -6.49602 | -47.49776 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6d54bf04-be1c-352b-a061-2cf68203ba4c | -10.54591 | -45.13918 | 2024-11-06 04:38:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2ffe4430-adc3-37f2-ba13-332d5c7133bc | -5.64044 | -46.67697 | 2024-11-06 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7a06dc2-60b1-3c57-a26b-f3bc4da704db | -6.61746 | -43.69177 | 2024-11-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de12107d-eee5-3b0b-a596-f6fd4083834c | -6.13706 | -43.9718 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8598771-1826-3c85-80ca-2393bd07c40b | -6.41766 | -48.38619 | 2024-11-06 04:38:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 231cad19-953c-3f7f-9bb6-cb6ccc10c325 | -7.08895 | -48.85003 | 2024-11-06 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf14cfa2-f7ce-3ce1-a1c3-51ead63ef5a1 | -10.61182 | -48.75412 | 2024-11-06 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d50f0edb-56be-3094-86b7-61419f04839c | -6.49156 | -39.96973 | 2024-11-06 04:38:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ed9121b9-e3f8-302a-bf7b-592f4a43aad8 | -10.95306 | -44.40744 | 2024-11-06 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1df44e3a-d37e-3237-a59e-5fa4fb31ee52 | -9.89223 | -42.08938 | 2024-11-06 04:38:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4aa789bf-99d5-3c9d-adb7-f6d45c28cf04 | -6.36346 | -47.92459 | 2024-11-06 04:38:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e3e59f2-27df-3877-a6d0-d05cc4ff070d | -6.12464 | -43.98144 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c9618659-0706-332b-8fa5-29a03cf01c2c | -6.25733 | -46.90169 | 2024-11-06 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 133ed27d-bdc2-38f6-9ee0-bc0b54743243 | -6.24853 | -47.30787 | 2024-11-06 04:38:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f93dffb-b263-3353-869d-0a9836d9d932 | -10.61237 | -48.75042 | 2024-11-06 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 466780b3-daac-392f-82aa-396f508c3be6 | -5.76353 | -47.07079 | 2024-11-06 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2cb05ebb-31f6-3ed8-921f-6905f2048115 | -5.21547 | -48.0776 | 2024-11-06 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 061ae58c-2688-34fc-9e8f-f65ebf256d8f | -6.26796 | -44.96973 | 2024-11-06 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a512604-f2ef-3973-9bd7-56bd6c7864ae | -10.94875 | -44.40686 | 2024-11-06 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aad4ca58-e425-33e4-a64e-9f62b6ba4327 | -10.04621 | -44.76517 | 2024-11-06 04:38:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d8fc4ee5-f64a-34fd-b8e4-4efeeee4b9f7 | -3.66231 | -58.58591 | 2024-11-06 04:38:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 252bf526-cf07-3bce-a80e-339ec09400b9 | -11.13174 | -44.95615 | 2024-11-06 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cb19d1d-4029-3552-8aee-0fdc44319a16 | -6.1098 | -43.96775 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1faa7ec5-c278-35c1-b760-c3adff99f31b | -8.49788 | -42.09084 | 2024-11-06 04:38:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8510e4ea-8313-35a1-8bb6-16bca6235673 | -5.66575 | -45.93852 | 2024-11-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40e0425c-d58f-3358-a4a8-a159900d9f98 | -6.26024 | -46.90613 | 2024-11-06 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d0d70a0b-d84b-3594-8d82-c41798191023 | -6.52259 | -48.43145 | 2024-11-06 04:38:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdfb4f93-2107-37ce-9014-b8ae636e5779 | -5.23845 | -48.14973 | 2024-11-06 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9598a21-7b4d-3f74-8b21-1a9ba3ed1a99 | -6.12358 | -43.97742 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd306618-dbe2-3046-8144-43c64dafd321 | -6.53466 | -39.73548 | 2024-11-06 04:38:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 901c2044-7707-3470-bb06-e18c40779321 | -5.19701 | -48.24043 | 2024-11-06 04:38:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9e919c8-94ce-3798-be8d-b90192772150 | -6.58275 | -43.51644 | 2024-11-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1c6e501-b23e-3f00-afd1-dacee4c20482 | -6.13106 | -44.70277 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21e9ae2e-2d64-38a6-9667-7013fa3ecac5 | -6.4824 | -44.68441 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f348fdc8-db25-3e60-9e25-6ba09c75cd3f | -7.37709 | -48.17066 | 2024-11-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1b6fafd-ddc3-33e1-822c-ee12f14d456d | -9.82682 | -45.23921 | 2024-11-06 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c007dacd-3e00-3463-b16e-5500fdb88b0b | -6.61189 | -43.61512 | 2024-11-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96f47760-1816-3042-b9a2-8075bfc91cfd | -6.27286 | -47.21885 | 2024-11-06 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a69fb24d-eb79-3c42-bf95-eeede582d5fe | -5.14927 | -48.24389 | 2024-11-06 04:38:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c41f4f3b-bbac-3487-87da-847081300ab5 | -3.58684 | -58.599 | 2024-11-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e65a8e7-ea05-3202-a954-a1ce987f7e85 | -5.83263 | -47.18831 | 2024-11-06 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70527e9f-9d58-3578-8968-26ca7f66130f | -6.13238 | -43.97493 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ddc7b90-afcd-3f0c-99aa-d417aeb73c58 | -3.73855 | -58.53436 | 2024-11-06 04:38:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dbd88aa-0bf2-393a-84fe-ec9c5c860a68 | -5.93928 | -43.77699 | 2024-11-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4ec12375-28f9-3a36-8198-f6714d8fadec | -7.22769 | -42.88166 | 2024-11-06 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e29c98e-c40c-3fff-82ea-4360a5d9dd8e | -6.93543 | -47.78342 | 2024-11-06 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1da9a56-046a-3162-a940-7c7b7172e619 | -6.61596 | -43.61074 | 2024-11-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acf87f0e-2e89-3871-96ea-3322f653f015 | -10.05037 | -44.76574 | 2024-11-06 04:38:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c9838959-e11b-321f-8070-686698cf95a4 | -5.93708 | -43.77234 | 2024-11-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3c60f18d-661a-3367-a429-aaf2d87c474b | -7.52354 | -40.14851 | 2024-11-06 04:38:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b61c849-0dcc-3f92-8087-c7f373e1eb89 | -6.50229 | -44.68705 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2659443f-36ee-3d26-8de2-1d2beb4b07d9 | -6.12666 | -43.98542 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb4ca0e5-9907-3a67-923f-c10f93d42fd7 | -8.5069 | -42.09753 | 2024-11-06 04:38:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ea84ff5c-0ca7-33c2-b289-d731a0a3374f | -6.49979 | -44.67644 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 7a5669e1-4671-3105-99b9-f0778c2ffa7e | -6.50773 | -44.67761 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 33e1e05c-30ea-3268-a6c4-51bce2071657 | -5.50661 | -47.16765 | 2024-11-06 04:38:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4aad864e-e499-3375-81e6-c63cf33a4617 | -6.36454 | -47.35172 | 2024-11-06 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27b591d6-e2b0-3066-9eae-aac975d3d0eb | -5.63984 | -46.6809 | 2024-11-06 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README56.md)
