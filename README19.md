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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 100fa640-a554-3bef-9299-1e6d37a4da9f | -7.15858 | -39.4581 | 2025-10-31 04:06:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2d3142d3-f7eb-36e8-afc5-0f2765cffc4c | -4.91624 | -45.32072 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cf89f08-53dc-3fc6-b9d2-d371643195b1 | -5.4224 | -44.58723 | 2025-10-31 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 904be74e-77a1-3971-b126-09d08b5bde0b | -5.26135 | -45.51672 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 570c96c5-f1b9-3428-ad99-c532ebc330ae | -3.1928 | -46.59457 | 2025-10-31 04:06:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06539f15-e3a3-3d7c-803b-f64c584f0b88 | -3.23083 | -50.654 | 2025-10-31 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 013f550f-900f-38a9-9f7e-b46c28c85204 | -6.57232 | -41.59004 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aad4cd4b-a83a-3c24-96a4-2dfcbcf10633 | -2.79317 | -50.2873 | 2025-10-31 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5396a495-565c-391a-bf54-e394d88ce088 | -5.42076 | -44.64249 | 2025-10-31 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8511c61e-3a39-303d-8602-0d2ca842fff4 | -4.4688 | -46.5612 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79f624d6-9bea-3326-9e98-64e68a0d7fb4 | -4.01253 | -42.874 | 2025-10-31 04:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fa90cbfc-627f-3b75-9511-5c1ce276082a | -6.47955 | -43.89116 | 2025-10-31 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbc3d3e7-c679-3cbb-91e5-5437eabcaef0 | -6.16015 | -42.3872 | 2025-10-31 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| bf30033f-cfe5-3dd1-aa7b-2c6ca0e2048e | -5.0292 | -42.57242 | 2025-10-31 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 97c2ab26-7b21-3616-82c7-7e58ac1f58c3 | -4.02767 | -46.20732 | 2025-10-31 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4dd32ce-5d1b-31a4-af34-530bc28d77e5 | -5.10608 | -45.18187 | 2025-10-31 04:06:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ace0b02f-642e-3673-9bac-78e815e46f2c | -4.63548 | -49.49104 | 2025-10-31 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f894f97-f2a3-3481-90d7-ba0f2870e897 | -4.78441 | -46.87956 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0c2fa8a4-1317-39d5-9684-741763fd57f8 | -4.87547 | -47.52706 | 2025-10-31 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08da9a13-fe4a-30f3-8520-c2aa5077dcee | -5.63953 | -45.02561 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c6d11c9-e259-34b5-9536-cb2d73e141ba | -5.25749 | -45.51608 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 103d4b7f-9bb9-360b-9561-bb37498d36d0 | -5.92443 | -43.37512 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 65850a19-11a0-369d-8721-636009a80d21 | -5.21701 | -40.76784 | 2025-10-31 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4195df43-2e92-30c3-abd2-1cb049a087b0 | -3.98993 | -43.424 | 2025-10-31 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bbdf47b-c095-3daa-9442-5dc45e1299ac | -4.23225 | -48.36732 | 2025-10-31 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81983432-7c04-3d1d-9178-9a6a18052571 | -6.46601 | -43.55941 | 2025-10-31 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd0ba1e9-b638-3923-9c54-3e86afa3c1b9 | -5.25827 | -45.51125 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46549653-2041-39cb-8bb5-3f937c4f72a6 | -2.41933 | -49.2999 | 2025-10-31 04:06:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e12317e7-2b54-3dc9-a072-ee23d49997c3 | -5.9798 | -43.73063 | 2025-10-31 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d8d4ac0-59fb-34f7-afc6-453f2291a32e | -5.40452 | -43.11802 | 2025-10-31 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b80c8114-695c-3564-a582-5f7669e53f9b | -7.39863 | -42.4627 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a163120b-6084-3dae-8614-5eb11ae6c582 | -4.79785 | -46.4646 | 2025-10-31 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d4d33e9c-26da-3149-8ba9-3a1a4ef1d3a7 | -4.55597 | -45.65414 | 2025-10-31 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 203c9646-472c-3343-8760-6dd85bba3813 | -3.78032 | -40.85165 | 2025-10-31 04:06:00 | NOAA-20 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e621cd33-1c5f-326d-a5e7-95a205b85e46 | -4.30701 | -41.43236 | 2025-10-31 04:06:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a56f8c9a-aa53-32f4-88ba-6c2467d7970a | -5.23218 | -45.47729 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7f050f6-f4b7-38c9-8073-c44f5b57eb4d | -6.30235 | -42.32679 | 2025-10-31 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae22f552-4394-3fae-a27b-f6059c4b89be | -5.63091 | -41.09454 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 50555f9d-b5d8-38ea-af0d-4a7bf931656c | -7.61667 | -43.6268 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81ce54eb-8224-3cbc-a0b2-73b554543c2e | -4.67878 | -45.80807 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a36d962-b50c-35e6-aaa4-856c906c8f54 | -6.06481 | -47.28365 | 2025-10-31 04:06:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 06c1ac85-d702-3185-bca0-523a8327ec77 | -3.14181 | -49.42555 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b6092617-8328-3d1f-859a-3bd994499137 | -5.63728 | -45.01598 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86bbc5a6-375a-32f4-bfb3-b41bcdf205b3 | -7.31546 | -44.95072 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8ae38f46-6fdf-30b5-b98b-dc1cad6f1435 | -4.76597 | -43.57511 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76ebc587-b1c3-304a-b5d2-e7346a4b96aa | -6.26925 | -49.19751 | 2025-10-31 04:06:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac88c85b-5a93-3d11-b3a6-743677f2d145 | -7.10182 | -45.22295 | 2025-10-31 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44e07d46-a46f-3aa4-a387-76c17fd92bdb | -3.31518 | -45.32624 | 2025-10-31 04:06:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 59bd80a2-b607-3f7e-a547-7752605974ea | -3.98643 | -43.42343 | 2025-10-31 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86de4551-dbe0-379a-ae52-cc9189c5ca4d | -5.90238 | -44.63149 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f81f1f8-2f91-3dea-92f2-3b50b5251095 | -6.21849 | -43.93866 | 2025-10-31 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43ed54d4-37ab-3b3d-a8f7-3054ae1fd3e3 | -4.0551 | -47.50015 | 2025-10-31 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3109ef6-bc5a-3ac8-8d20-04f22d5dabc3 | -5.9272 | -44.57074 | 2025-10-31 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 172ffbc1-1f59-3c55-8c1f-1ce368599776 | -5.79093 | -40.81231 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1d7001bb-80ab-3df3-bfd4-4ff7771ff9b1 | -5.96481 | -43.38456 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 504c78c1-1c24-3d82-bb8f-7c03c5ea89d8 | -4.42285 | -43.37113 | 2025-10-31 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a7511c5-23b4-321e-a217-ec73a29771ce | -3.25319 | -42.07366 | 2025-10-31 04:06:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71c28f42-2686-3244-839d-6b06c7294f3f | -5.91178 | -44.1314 | 2025-10-31 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53c116ed-36d2-3594-9fb3-a1f97582c042 | -5.95904 | -45.56014 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fed7db24-6d9c-3729-b188-4bc13a69d6ed | -4.80563 | -43.02425 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 20afbf46-33ad-320e-8052-adba0fdce509 | -4.3123 | -48.08437 | 2025-10-31 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 193812b5-28df-363f-8ca5-adc0268e558b | -5.79533 | -40.80591 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e2b6fa26-7e95-3aaf-abc8-6e583e1e32c6 | -1.36043 | -49.02797 | 2025-10-31 04:06:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eade06b1-3309-3416-98c7-7a7a0c73261f | -3.77452 | -45.16874 | 2025-10-31 04:06:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f04fd01c-9c0f-394e-a910-737176129b39 | -2.32268 | -48.57743 | 2025-10-31 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 709cc758-c7fc-354f-b2fe-88743494c551 | -5.54024 | -48.37994 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87aa6795-5066-3925-85c6-896477c62703 | -5.50501 | -46.38132 | 2025-10-31 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db5a4d67-3ed4-37b6-be3d-0dcb095779f7 | -1.16595 | -49.2661 | 2025-10-31 04:06:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11235efc-7e39-352e-a3de-c1d47ab82e8d | -7.32001 | -42.55079 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2272488b-304d-363b-ad62-2c4b2f31587c | -5.31778 | -44.83722 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0e53c5b-e689-31b6-8cf2-9cae8ebb2620 | -6.21485 | -44.57954 | 2025-10-31 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b610a12-eeb4-33aa-8732-452b252f56f4 | -7.38041 | -39.04515 | 2025-10-31 04:06:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 189c3cfc-00aa-36ff-b1db-55ffebe4484c | -3.45434 | -45.98735 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0054384f-56f5-394a-8d2c-e8812f426d5d | -4.45227 | -49.14899 | 2025-10-31 04:06:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c51c3bf-0446-360e-9dc6-bb45036e5f63 | -4.81882 | -47.08565 | 2025-10-31 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aca3043e-b5e6-37b1-8f3f-cb4092d641f6 | -4.76946 | -45.98727 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fe49794-12c7-3de4-b076-58012c4555bb | -7.359 | -44.63667 | 2025-10-31 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 57be8735-d089-3d1a-a619-5c6dc5245941 | -6.44779 | -43.69224 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8406cf51-b7bc-3d71-a34d-9c80f16c45ef | -5.81383 | -40.84023 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 460f703b-7c7c-3907-990c-4e194bc2231d | -4.42851 | -43.71298 | 2025-10-31 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c52c259-d96d-3a0f-bd27-a94916a5c1b6 | -5.61897 | -45.98218 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f1a104f-a325-336a-bb3e-5b253662fd00 | -5.54487 | -48.38079 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba4c00c5-06bb-3412-a281-f17211374f68 | -5.14706 | -46.17153 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79d5148f-e2d4-3106-9454-cfd926a3a11e | -3.86403 | -48.03641 | 2025-10-31 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02e6f783-5bf0-3b2c-a1fc-6c7e9a4f3c7c | -5.74185 | -45.58349 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c6e16678-e678-3687-a73f-499fbfde4ec4 | -4.41264 | -46.63573 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bb930b0-403c-3629-be56-761103027c43 | -7.40932 | -43.34762 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b952924-6e8f-3fa0-8c75-18cbfb8ebdec | -7.791 | -41.575 | 2025-10-31 04:06:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4d297034-a3eb-3a90-8753-942b99744811 | -4.3026 | -41.43877 | 2025-10-31 04:06:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b9ac4da2-c400-34ca-a2d2-9112c59a6216 | -2.63275 | -48.5062 | 2025-10-31 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f72049b-8863-3624-9552-76440f437f13 | -5.59194 | -48.05006 | 2025-10-31 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5ba72360-a636-3c02-a0d5-92213d146484 | -4.57117 | -38.28417 | 2025-10-31 04:06:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0a17ba7f-c046-38d1-8993-8864ce4cc55d | -4.38473 | -43.28666 | 2025-10-31 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b47cd7d-0265-33c8-8949-a1ec66827bf8 | -2.92293 | -51.46752 | 2025-10-31 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f1aea61-8396-3851-a9a4-30519de4f15b | -6.34201 | -43.65277 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dec6d3f0-9d57-3464-a2b7-cf5267692b3a | -5.53505 | -41.70142 | 2025-10-31 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1fcc8ca8-8359-317f-bcc8-5ddba4bce886 | -7.01094 | -45.58257 | 2025-10-31 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06b8e907-4536-3799-9fd3-e0e80826d4e4 | -6.21499 | -43.93809 | 2025-10-31 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a01e83d6-d4d2-3b54-af4a-5bb4c4120bce | -3.23418 | -50.65465 | 2025-10-31 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d65f4ba5-8522-34ec-832e-20bef00000ed | -3.94426 | -46.97081 | 2025-10-31 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README20.md)
