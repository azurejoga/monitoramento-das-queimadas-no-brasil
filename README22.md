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
| f9aebb2a-6ae3-3497-bcab-6e4696a5c18b | -6.93511 | -42.72672 | 2026-08-10 11:36:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 560fff5f-e69f-37e2-8cf7-6b328fe5c9a0 | -7.73548 | -37.17543 | 2026-08-10 11:36:00 | TERRA_M-M | TUPARETAMA | PERNAMBUCO | Brasil | 2615904 | 26 | 33 | nan | nan | nan | Caatinga | 19.2 |
| d1a0ce8a-60ef-3ec4-9c46-998195537067 | -9.42116 | -47.43272 | 2026-08-10 11:36:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| af801c45-4895-3819-838e-ad5e45d0912a | -7.15397 | -43.26905 | 2026-08-10 11:36:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 2a233dfc-2415-394a-911b-7df871e971c8 | -8.54499 | -45.3566 | 2026-08-10 11:36:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ffc439aa-66ee-358e-9369-e51ed689379d | -6.93645 | -42.71716 | 2026-08-10 11:36:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 0c905127-3cfb-3c24-a1c4-9470415fd533 | -7.61214 | -42.76485 | 2026-08-10 11:36:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 75e72863-eca0-388e-b157-dbe3cf476410 | -9.15753 | -48.83636 | 2026-08-10 11:36:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1017da66-adf6-357d-988b-62634409617c | -6.94558 | -42.71845 | 2026-08-10 11:36:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 094f79d0-3e00-33f4-ae6d-8adef36e7cf3 | -9.41961 | -47.44316 | 2026-08-10 11:36:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c9ca981b-cd3d-3b0c-b885-61606260a71d | -6.94425 | -42.72799 | 2026-08-10 11:36:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 6948cd04-d5ae-35a0-8834-24ccfc51d58e | -3.48525 | -43.33259 | 2026-08-10 11:36:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18ab8e88-3c6e-3241-b789-e7a531f591e6 | -13.48741 | -43.04995 | 2026-08-10 11:38:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 1449dda0-65de-35f9-bcdb-8ee1d012e6f2 | -14.27586 | -45.32011 | 2026-08-10 11:38:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 990baa77-d2d9-3296-aacb-0cf16cbb8348 | -11.47107 | -50.53529 | 2026-08-10 11:38:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 95571350-a42c-3785-843d-1e027210783f | -12.30843 | -49.98997 | 2026-08-10 11:38:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 090ce9ba-25c1-3d70-8c7d-867c8b34853b | -14.96201 | -41.33646 | 2026-08-10 11:38:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 523b751e-3999-3a12-ae97-59fea93eeeb3 | -17.50353 | -42.37333 | 2026-08-10 11:38:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| b9450910-74f6-3252-a36c-837eefa98d48 | -14.8449 | -43.65151 | 2026-08-10 11:38:00 | TERRA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 90c9eede-9d6d-3e3e-8e61-2b1a7e52546b | -17.4994 | -42.36705 | 2026-08-10 11:38:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 21bad6a8-8f55-39f4-8ccb-23b4a414a393 | -10.84043 | -46.75109 | 2026-08-10 11:38:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 039952f7-6cb9-3cf2-ac3d-565bc519c007 | -11.94305 | -41.32365 | 2026-08-10 11:38:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 59.1 |
| d69c8b03-c03c-3664-b400-c0a699ebfb81 | -10.83135 | -46.74971 | 2026-08-10 11:38:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| a7104529-bc44-34e9-95e3-413d10fdd303 | -15.63416 | -48.55597 | 2026-08-10 11:38:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9767586a-8eae-3708-b482-942b7b17ce1e | -12.31068 | -49.97588 | 2026-08-10 11:38:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cd0d414f-3815-3e19-a49b-2e876267ad0e | -14.27714 | -45.31096 | 2026-08-10 11:38:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 2386bec3-5289-32ef-a2bc-f7be862a71b4 | -15.62973 | -48.5486 | 2026-08-10 11:38:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9944719a-41b5-3b05-9046-849f9ad0dcd2 | -11.81548 | -47.33313 | 2026-08-10 11:38:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c4de2a6b-8a97-3160-9cf1-eee7f2a47f42 | -14.28601 | -45.31224 | 2026-08-10 11:38:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8a84d414-f121-3b0f-89c5-1bf1bfe4a363 | -14.23318 | -48.50081 | 2026-08-10 11:38:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9d2fe814-f001-331e-bff9-604e16cde519 | -11.48002 | -50.55302 | 2026-08-10 11:38:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f26a7bd6-647a-3e64-bf5d-acac32e44803 | -11.94896 | -41.31862 | 2026-08-10 11:38:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 6cdb3858-61b4-30e0-903f-a81d335a174c | -14.23154 | -48.51159 | 2026-08-10 11:38:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| acb8dc0f-1113-310e-848d-cc301d1f2c72 | -14.2957 | -47.16127 | 2026-08-10 11:38:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3e22a093-87e4-3d1f-ad0e-59d0ddc28638 | -15.03741 | -46.57056 | 2026-08-10 11:38:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4d44a4ba-bce7-3d16-b107-a75cc0b9077c | -10.47165 | -46.62663 | 2026-08-10 11:38:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2982b3f9-6c78-3c33-a67d-d6a87fb58e27 | -15.63109 | -42.3943 | 2026-08-10 11:38:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| ce5f8f74-56a9-31bb-8cb3-1763614dc01e | -14.2943 | -47.17071 | 2026-08-10 11:38:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 331fa123-6448-35ad-b2c7-67e6006a446f | -13.85917 | -43.64547 | 2026-08-10 11:38:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c75db71d-6dfd-3ec6-84ee-d4cf05d2f347 | -13.9855 | -43.38281 | 2026-08-10 11:38:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c2d9a87e-b450-35e5-a732-c4b1ccefb516 | -14.28473 | -45.32138 | 2026-08-10 11:38:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 127a30c3-44b5-3b9c-8ae5-31d051649f3f | -11.4685 | -50.55115 | 2026-08-10 11:38:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 55b0ceeb-3e5d-3ea0-a1a2-0d4a11e5a455 | -14.2872 | -45.3069 | 2026-08-10 11:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 16af4f9b-4183-32b4-9f87-42462f8adc06 | -17.82361 | -44.53806 | 2026-08-10 11:40:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| bd72ca5a-907c-34a5-ab52-2b5176865b3c | -17.49752 | -45.99507 | 2026-08-10 11:40:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5841ab8d-c42d-393a-917d-78712c301a25 | -20.02099 | -43.19715 | 2026-08-10 11:40:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| 4a894803-f114-38f1-98af-8afef9f8bcdb | -21.08292 | -44.48653 | 2026-08-10 11:40:00 | TERRA_M-M | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| d59025ab-1e45-38ab-a42b-3070ad04b463 | -17.21193 | -47.71668 | 2026-08-10 11:40:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2b8a2496-d847-39c4-bc1a-6ad76a11bf44 | -17.49881 | -45.98577 | 2026-08-10 11:40:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9b93b554-785d-36cc-af58-3f942e3aeb44 | -20.31813 | -44.83524 | 2026-08-10 11:40:00 | TERRA_M-M | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6486cdbb-8b28-3075-a18c-4d07a01b8857 | -17.96373 | -44.5807 | 2026-08-10 11:40:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d8008d5e-0367-355e-ae1a-6bd4195f25df | -18.6105 | -46.91585 | 2026-08-10 11:40:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0ed6ded9-e548-35d6-bf6d-13463e9632af | -17.48037 | -43.64422 | 2026-08-10 11:40:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ab5291d0-edcd-3e07-941e-d74844b0432c | -19.22675 | -52.73565 | 2026-08-10 11:40:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 584ab279-7f46-3206-ab76-a0eae599959f | -17.2209 | -47.71808 | 2026-08-10 11:40:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 4343fb12-7268-3225-b53b-396a41472012 | -17.82497 | -44.52775 | 2026-08-10 11:40:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 7931cc41-aefd-334c-ab44-5bd86dca48ca | -20.04449 | -43.75377 | 2026-08-10 11:40:00 | TERRA_M-M | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| b688a6cd-28ff-3d91-9efd-ac9f8b2424fe | -14.2677 | -45.3103 | 2026-08-10 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| bce89eb0-9a81-3ad9-b95c-ee1bb81f8b57 | -14.2872 | -45.3069 | 2026-08-10 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 571e2169-5a01-3a68-a91d-ff68b39965c3 | -14.2677 | -45.3103 | 2026-08-10 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 3f538076-0896-300d-a15d-cb8ecb87fd09 | -7.6214 | -42.7685 | 2026-08-10 12:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 675a5b27-a6fe-3fea-8088-5eca6333aaa9 | -14.2872 | -45.3069 | 2026-08-10 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 6ae76a75-80d8-3a1f-a4ba-512fa8325aa8 | -7.6214 | -42.7685 | 2026-08-10 12:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 70c85c1f-b54a-3801-98cb-e66f9d582b9f | -14.2872 | -45.3069 | 2026-08-10 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 646839ed-f4f8-3e8e-853d-c31ef2553db7 | -14.2677 | -45.3103 | 2026-08-10 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| b3358b57-1d73-3692-832c-bab85e43d434 | -11.4671 | -50.5604 | 2026-08-10 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 147a552f-8c40-3a9f-8d3c-c0be64518954 | -7.6214 | -42.7685 | 2026-08-10 12:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 3f95ec7b-ffd2-3e4f-b483-2b6ef6b25993 | -17.9695 | -44.577 | 2026-08-10 12:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 189.8 |
| ccd9b852-18f5-3447-bf10-cd29db3338ef | -14.2677 | -45.3103 | 2026-08-10 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| cb259762-46bd-3d29-8596-1bf7a0474e6d | -14.2872 | -45.3069 | 2026-08-10 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 2cdfbccc-c280-3ba0-91cc-16ff00aa2fff | -14.2677 | -45.3103 | 2026-08-10 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| e3a7b12a-ee8f-3541-b8c3-6c2b7c34d35f | -14.2872 | -45.3069 | 2026-08-10 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 206.6 |
| d79a5cec-43e8-3dfd-9272-446840099d3e | -6.9468 | -51.9209 | 2026-08-10 12:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 33cbf006-2688-364f-999d-7f1bbc0a98eb | -10.2659 | -45.8206 | 2026-08-10 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5aafe46f-62a0-3a1e-b92b-6eac93088f86 | -9.9591 | -53.3071 | 2026-08-10 12:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| e68f5dda-0eee-3a52-8527-c4441564d2f3 | -7.6214 | -42.7685 | 2026-08-10 12:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| ed806329-88e6-3871-9355-f28c2abfed1c | -14.2677 | -45.3103 | 2026-08-10 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| d7fa4a90-8822-39ba-b309-5d03bf0fcdd0 | -10.5008 | -46.6042 | 2026-08-10 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 2860fd70-4108-37da-ade5-a9dff6879a60 | -14.2872 | -45.3069 | 2026-08-10 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 38182c4d-9362-3784-b21b-b426f1aa0d2c | -9.9403 | -53.3087 | 2026-08-10 12:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| dea6b0fa-0e29-3f16-ac93-b0d9c351dac4 | -7.6214 | -42.7685 | 2026-08-10 12:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 127.6 |
| fde11149-a97d-3115-986b-3d2f67271d49 | -10.2659 | -45.8206 | 2026-08-10 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 92d09724-892d-3009-9fa7-63bed28a0d78 | -10.2655 | -45.8434 | 2026-08-10 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ac23448d-b6ef-3064-be95-06f44fb4d749 | -14.2877 | -45.2835 | 2026-08-10 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 024f8fe8-075d-3fe2-bb29-f69f8088bf69 | -9.9591 | -53.3071 | 2026-08-10 12:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 26df5cc0-b860-329d-9875-fb827e7a18c8 | -14.2872 | -45.3069 | 2026-08-10 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| dd617e57-f5fa-3979-9c1e-f8d0b94ac5a1 | -7.6214 | -42.7685 | 2026-08-10 12:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| 77e6feba-780b-3fcb-9907-861ed8e39739 | -14.2677 | -45.3103 | 2026-08-10 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 5ce27449-2ad1-3afd-9ed9-91fe48611ced | -14.2682 | -45.287 | 2026-08-10 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 5bf2021e-fe29-3214-82df-6c9c85125dbd | -14.2877 | -45.2835 | 2026-08-10 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ad0fefd6-1ad5-3d89-80f2-4edec3a7bc3c | -9.9591 | -53.3071 | 2026-08-10 12:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 147fa179-08a8-307b-911a-f8ee9f888abf | -7.6025 | -42.7705 | 2026-08-10 13:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 3001ec64-d47f-3831-9552-5b79eea40eaa | -8.3117 | -46.3976 | 2026-08-10 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f596943a-31b9-3244-be8e-b29d1c9f38aa | -10.8407 | -46.7414 | 2026-08-10 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 0c357d77-1016-36e1-af90-5dbde900450d | -7.6214 | -42.7685 | 2026-08-10 13:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 204.3 |
| 2f80a604-1065-346f-ab76-2a885c2797f6 | -8.5507 | -45.3589 | 2026-08-10 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3e799db6-a3fd-30ec-978a-f90a2583cb70 | -14.2872 | -45.3069 | 2026-08-10 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 9ba21740-7b56-3075-b32a-bafbbe6164df | -14.2677 | -45.3103 | 2026-08-10 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| c372178e-f5bc-3136-82f6-cd6f634aef36 | -11.4671 | -50.5604 | 2026-08-10 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| efbca649-19c4-34fa-8f4b-a67c2b712627 | -8.5504 | -45.3817 | 2026-08-10 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |


[Clique aqui para ver as próximas entradas](README23.md)
