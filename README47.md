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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98340479-1ac9-39cc-9d15-d049c1938a56 | -5.22534 | -38.1596 | 2025-10-17 04:19:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e0fb157e-6236-34f4-ae9e-758f7150fe54 | -8.25147 | -43.33439 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| f151f03c-8671-3a3d-905b-47b60fda478d | -6.27884 | -42.96928 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e9d7fa1-e454-341e-b9a1-c43c2c6f9fed | -4.96993 | -44.95709 | 2025-10-17 04:19:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffa04d69-192d-3563-8190-8174d158d508 | -5.29487 | -43.55242 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 1d22d428-7b21-3f15-9771-53f55c02ce86 | -8.38008 | -46.3143 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c3c8c85-32b1-3ca5-af8b-e18148566003 | -8.45216 | -46.18373 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad64c480-51ce-3f56-82f3-a272c98abdd9 | -5.89088 | -44.74989 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 982c8fdc-07dd-3f0c-845c-6987532e4692 | -6.40034 | -41.90215 | 2025-10-17 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d780b7f8-9553-372a-af40-1e4215018ebb | -9.41511 | -43.31157 | 2025-10-17 04:19:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e1220122-97ca-370b-81f7-2cfea9ce19e5 | -6.20298 | -41.77159 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c4d30abb-8367-3822-bdaa-042fb8dbe1cf | -5.89214 | -43.89161 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a8489ee-a641-3de6-b655-74fa5ece58bf | -5.94828 | -43.17676 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0502d286-faf3-39e2-8fd8-5672339a9701 | -7.18072 | -42.52398 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 124e4acc-15bc-385f-a152-b2b28915b384 | -10.2875 | -44.03301 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f1932c14-de74-357f-bd39-2dc81b25c86e | -4.41444 | -43.39387 | 2025-10-17 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e7e812bd-c9d1-3c8c-9c81-14e55e8aed67 | -8.81498 | -47.08451 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbf6014d-b776-3456-8b64-88aa30841194 | -6.83914 | -41.70828 | 2025-10-17 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6eac9250-f701-38de-9188-c77c09e1c752 | -8.38065 | -45.06103 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e33eb6ea-9cc8-3eac-97ed-f52c46afa9c4 | -8.27243 | -43.35643 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 39c43ec3-a0b5-3da6-ab12-6b8b736f2579 | -5.39696 | -43.24473 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9878cbb2-0f26-32ee-885a-888e7b78b219 | -8.2461 | -43.41616 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7dd12a89-346b-3172-8898-d6ddc3c71c5e | -8.8276 | -47.30968 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 07efc5a5-0deb-3d9f-a9b5-38001a520249 | -10.60046 | -47.38937 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72c4bda3-afcf-3cc2-a832-885cfb76dfa9 | -6.74843 | -42.37542 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5d206351-e70e-35b6-b18b-e411dece5a7b | -6.95101 | -47.71896 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45c66e9a-4f4f-3394-a6ae-21a0d4439a3f | -7.75292 | -42.49674 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e92db28b-98d0-3337-a033-a5b540fdf1a9 | -5.83563 | -40.81157 | 2025-10-17 04:19:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b6ea143e-f9c9-3f72-b3b2-b80119875c27 | -7.4361 | -44.74773 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d156a8b0-e8a2-394e-bfa0-2e6fead81b45 | -5.6175 | -42.67901 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bec21594-e221-3dcd-baed-a2414951eea5 | -6.349 | -41.51717 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 90b71877-3d24-3f3d-8e76-685fb6de67cb | -7.05776 | -45.05529 | 2025-10-17 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b2b47eb-ffee-3766-b7d7-d0c027ae9c2b | -6.94758 | -41.56218 | 2025-10-17 04:19:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9679338e-f280-3415-afc7-d1175fea99bc | -6.20606 | -41.75154 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 11c562e6-77d4-3a54-bcde-d8a961f86c78 | -10.50038 | -43.41503 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f3480f8-883b-3484-a9ab-ddd3fe87032e | -5.36875 | -45.87445 | 2025-10-17 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2483b62-0189-3e03-b84e-849234bd70d3 | -6.13752 | -41.725 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e635a602-c4ee-37da-88f8-f22ee6e8ee22 | -5.38514 | -42.79641 | 2025-10-17 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bda3169c-9a52-3107-b456-8d6821ba947b | -8.2604 | -44.08234 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a21e56f0-9b2f-3921-8452-bc33cdac884a | -11.40214 | -44.22893 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7af918fb-1c7e-395d-ad15-9cd565d34275 | -6.17412 | -46.74596 | 2025-10-17 04:19:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30b14e40-9327-3c0b-a449-34a7a2c3c0a7 | -5.47202 | -45.82442 | 2025-10-17 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a00c7b5d-9028-362c-9395-4a8160b93a14 | -10.27852 | -44.02411 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cad1d760-f385-3929-84ec-6ee949c24210 | -5.5793 | -41.32218 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0a228243-e517-3c24-ba89-a1d739c4d4fe | -5.09264 | -45.42984 | 2025-10-17 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1fb1e5e4-daaf-3ff4-9d5f-e48ebb09e663 | -4.37066 | -48.70755 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c3da319-ba68-3b42-8639-764e91a95af9 | -7.95081 | -44.12824 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6aeb0ffb-331b-3826-ad98-d639617f93e4 | -6.20837 | -41.76009 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a4fee459-8a93-3b78-bc25-b4363054df7f | -6.2323 | -43.0251 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff2a2b03-71b2-39fc-9591-24b747b8012d | -8.93795 | -45.24265 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb23336e-7415-3b6e-aa37-60c6ffda6ab4 | -5.36824 | -43.14243 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b794d0a0-1da0-39a7-a28c-b6feb5d32861 | -5.69771 | -42.68351 | 2025-10-17 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bff5578c-b93d-3756-8947-d22b563e34f5 | -7.31942 | -42.46578 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05033f02-c682-34aa-a77d-f3e443d22fbf | -5.35432 | -43.14388 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87e17045-ef74-30b8-9d7c-68a024317b09 | -6.83977 | -41.70413 | 2025-10-17 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a5affebd-c661-3056-a677-45f4769a8901 | -6.20667 | -41.74753 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| d5ddaa9e-11ce-3b85-a748-f8fc980ab990 | -10.27796 | -44.02781 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23512b49-2769-3f21-9369-b04f8ac90ced | -9.28323 | -45.38309 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c83559c7-8fff-3163-93fa-c72a56f2f783 | -6.43828 | -46.52017 | 2025-10-17 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5ac5f00-9ac6-308a-9d7b-d30bb7421f37 | -6.13389 | -41.74926 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e42239cb-99fc-3e6b-af04-c8fac5d8d5dc | -8.40153 | -46.22278 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f9656d7-903f-35d5-affa-4e48282b3b12 | -6.13632 | -41.73304 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4516e17f-35fd-30e2-8186-4d282fdec284 | -11.39876 | -44.2284 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67d7195a-051b-39ba-ae8f-ff678ac7fa63 | -6.54435 | -43.9191 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e0fe9840-bf84-36de-924a-8cf610b4eb17 | -6.28843 | -42.97444 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52e005c3-7032-36b5-8fad-4b1ca183c894 | -10.51584 | -43.38263 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53a64a52-ad17-329e-b523-e88f52772803 | -10.92277 | -47.86933 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c809422-b31b-3c2c-bd6b-6b03e364402d | -6.3069 | -44.72416 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef661c2a-1bd0-3a30-aa9b-ea7c72ea89c9 | -6.66942 | -40.84949 | 2025-10-17 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a9fb0844-d04c-38d0-a342-84edf71d38cf | -9.22935 | -48.59489 | 2025-10-17 04:19:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ccaebc11-fe01-392d-9b71-2f7aaab72b19 | -11.46844 | -44.20169 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d112d66-f5f7-3e1e-a51d-356799628af7 | -10.05885 | -43.83355 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 16db8c47-c438-3430-aac9-944b15159f60 | -10.13597 | -44.57781 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d2435ae0-c575-365e-8685-e5d8004ace55 | -8.82448 | -47.30901 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4f743449-5136-334e-93b7-d1b3aa6cabee | -5.69913 | -53.63827 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a456c45f-b95a-3e4e-9e60-6bfe975ee777 | -8.2149 | -43.98141 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b50bf729-2e5e-3c48-8adf-a672293fcdda | -9.1457 | -46.63941 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a50f88a7-e889-37a5-a9e1-682bd0df1063 | -6.14613 | -41.7883 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5aeeef7e-a2ac-3124-b9dd-e887f3903e35 | -8.23357 | -44.82459 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73d049ad-2340-33e9-b083-ffbd57fa4ab1 | -4.01492 | -47.41931 | 2025-10-17 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4242dc2b-610a-31f1-99f7-24a616565f6d | -7.46952 | -42.16294 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 344b9180-d25f-39dc-a933-8c2abd7c477a | -5.36941 | -43.15714 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f11c128-6f9a-3153-bbe1-c23f6f597c8d | -5.85263 | -43.88184 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c283e39-1299-393b-9ff9-636230726ff9 | -7.22436 | -47.86584 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60a5d6a0-1372-355e-b8a7-0cda890d5c67 | -11.46005 | -44.23419 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 887b9e7f-0b4e-3e0a-a81f-5bafaa8e9764 | -6.53514 | -55.05407 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca57687a-daa6-3c84-9dad-90711d018d03 | -8.46872 | -50.1026 | 2025-10-17 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1eddb8c-deb4-3e1a-97cc-ea7f9811381e | -3.13464 | -50.21282 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe8b7853-bb70-3065-a981-082c1ee0851b | -9.23841 | -44.37921 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef89c5b3-e7d2-38ab-b92a-7ba14aca37c0 | -8.96678 | -48.42958 | 2025-10-17 04:19:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a575a2a3-7429-350c-8ae2-1013aad009a3 | -3.76437 | -48.92221 | 2025-10-17 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81d044e8-3110-35f4-a3bc-e63f755fd2d9 | -3.84602 | -44.54921 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fee9d2c-8cb8-3cec-87a3-96d14e8296af | -4.93156 | -41.55681 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 98b64ea2-f10d-301b-b930-f044a8f8579d | -5.85317 | -43.87837 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c249e5e7-49b1-3068-9807-4dfe5873e4cb | -5.76749 | -46.75953 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85c40f4a-f734-30e3-8a40-fa1d21f58cc6 | -7.14623 | -39.59166 | 2025-10-17 04:19:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 90a789a1-d5c2-3b56-93c3-1f16d5ddeefd | -10.05388 | -43.86647 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a87aecb0-7bd0-363f-a31d-e748881e7bf2 | -11.4569 | -44.0487 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fa743e0-6456-35c2-8e77-49fcb3e7e7b6 | -8.08979 | -45.41862 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0107542d-e8e2-3052-af3e-149288f34ac5 | -11.40041 | -44.2174 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README48.md)
