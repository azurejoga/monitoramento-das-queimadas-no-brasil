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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12946bdb-c476-3777-a376-fce0f5443af8 | -23.36087 | -47.174 | 2025-09-03 05:18:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 48e249c2-2a40-3683-bf9e-d8e1f6ef302d | -26.715 | -52.4423 | 2025-09-03 05:18:00 | NPP-375D | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| af93e59b-b80d-34e3-bd1d-3ceda01e97ff | -7.6851 | -48.7386 | 2025-09-03 05:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 254bb0bc-87bf-3dc9-92e1-b8926e10cb6f | -7.6849 | -48.7602 | 2025-09-03 05:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9ba00909-9cf6-31f5-90aa-ee36f7d5f4be | -7.7039 | -48.7371 | 2025-09-03 05:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 96005f32-94fe-3844-b1e5-56c57a214a69 | -7.7041 | -48.7155 | 2025-09-03 05:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a3fbe520-8e61-3e4b-bafd-83b944e4f49a | -7.7036 | -48.7587 | 2025-09-03 05:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f8e04401-1d45-3de2-8bc2-fb825c30473f | -7.7036 | -48.7587 | 2025-09-03 05:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 74abb709-859f-3763-a3f7-6094ac39df09 | -7.5476 | -61.3437 | 2025-09-03 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b66e9d5d-474e-31ea-961e-383d8eb06ebf | -11.5966 | -52.134 | 2025-09-03 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 306.0 |
| ebf8b59c-a23e-30f2-b56e-a47b8a3b4758 | -11.5963 | -52.155 | 2025-09-03 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| d9c2b92c-0819-36d4-a44f-ec5ce7d57f46 | -11.5969 | -52.113 | 2025-09-03 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 170.4 |
| 4de68034-d185-36dc-88a6-e25d0da2b76e | -11.6156 | -52.132 | 2025-09-03 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 37bc9ed5-28ea-3e36-a587-49c994b11aa0 | -11.8078 | -50.6499 | 2025-09-03 05:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 86058eac-0221-3426-823c-a42c2eef5970 | -7.6851 | -48.7386 | 2025-09-03 05:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 80.9 |
| d4c78641-42d7-3483-a297-1b7744216ce4 | -17.4431 | -47.2044 | 2025-09-03 05:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 3711613f-f986-377d-8522-550752dd80fb | -7.7039 | -48.7371 | 2025-09-03 05:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 80bbe882-463c-325d-9e5a-2ffa130557fd | -11.8081 | -50.6285 | 2025-09-03 05:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| d934bb7b-3fd5-3380-8afb-9c4654d5e840 | -11.5776 | -52.136 | 2025-09-03 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 6234e47b-a9c7-3900-8f22-949cd4836b95 | -7.6849 | -48.7602 | 2025-09-03 05:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a3ae2b13-cc99-3bfe-8534-11acc978f800 | -11.5779 | -52.115 | 2025-09-03 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| f84891c4-a8d7-3917-9e05-4381320ed759 | 2.89343 | -60.2655 | 2025-09-03 05:31:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbe24363-ee6c-3795-8199-322c0192b7af | -6.33307 | -58.17935 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 745493b2-d180-34ce-90b7-bec14ee7d95b | -5.89281 | -57.74006 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ef373054-298a-3927-b4fe-b5cbdc0b79eb | -5.10767 | -56.97263 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee374e81-c163-32ad-9cb6-e15d90bb185a | -5.92009 | -57.7225 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| aa8c6903-712a-3362-8c4b-dd0920261ea1 | -6.33836 | -58.17236 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 983701c4-a907-3dcd-99d3-bd3fd87c1dc1 | -5.91582 | -57.72174 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 04f42b12-cf3c-3600-9a51-8c6bcf3bf3af | -6.83073 | -52.84959 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2c22669-2281-37b4-91d8-5e31b7e5a39c | -5.90868 | -57.75074 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 448e5a85-5587-312d-8a97-73ad5ead377f | -5.92552 | -57.71506 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 73307b2c-63df-3749-9674-fac407941fb8 | -5.90499 | -57.7462 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 5f91d7b7-0c72-3694-af46-3fbf7a9dd103 | -5.92695 | -57.71649 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e252b5b1-e47d-32d7-baa5-ea72f068979b | -6.79472 | -52.83131 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9da02335-cd6b-3a36-b48f-a7cc92f01299 | -5.92066 | -57.71845 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d129915d-cad0-32a6-830a-b7ddd5073362 | -6.77903 | -52.81103 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a037932a-58e3-3373-9fd6-8fbe60a85f6a | -6.33725 | -58.17997 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f528fb2c-d544-3fd1-bac4-c92298119556 | -6.23357 | -55.6321 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba5359da-8c06-3e09-b946-dd4b82641700 | -7.71541 | -50.30128 | 2025-09-03 05:33:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b465cf6b-3aba-3d1f-bfd5-02fd93c21acd | -2.14468 | -53.6481 | 2025-09-03 05:33:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b086615-52f7-387b-adc9-ce72fda77036 | -6.43477 | -58.13486 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea50815f-912b-3dab-8e8f-dbdcb437b3e0 | -5.90439 | -57.75019 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ae2e61d-7191-3f54-a54f-fdfe23d86f29 | -5.92183 | -57.71024 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 719f99cd-d095-36f4-8ac5-d795bdbb76c1 | -6.84929 | -52.79333 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d4f6065-eed3-3bff-b0c4-853ef359e186 | -6.2309 | -55.93584 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f7d1efc-e580-375e-8128-19ef77d18083 | -6.80734 | -52.82901 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96596d47-b41c-3c06-94a8-e819a8113d0d | -6.85357 | -52.81667 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 781366a6-69ec-30e5-a3a3-e7900fe56ba1 | -5.87215 | -57.76162 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d553b154-be2b-3f0d-b489-2eff921f1f7f | -5.91352 | -57.73786 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a1259cc1-d597-320e-8017-7147946809aa | -5.90987 | -57.71365 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f5c5b21-d660-3e76-a38d-eee243973748 | -5.89587 | -57.74879 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1985a4f1-2fd3-32cc-887d-ce953a93e09b | -6.83037 | -52.84042 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68bd1fa5-38e4-32f2-a28e-7588f428104b | -6.81467 | -52.82055 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 104ee1ee-dacf-371a-bfc2-271480b920da | -6.34086 | -58.18441 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8cfd7d6-cdb1-3089-9a5b-b296004a3db7 | -5.9056 | -57.71294 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce7fabb0-eb4e-3bd8-b280-b98f984656a3 | -5.9178 | -57.71912 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 49976cb3-57be-30c5-b7a0-66ec27141282 | -5.87098 | -57.76956 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b6e9636e-5357-35fe-b176-90ebe3a6d4f0 | -5.86668 | -57.76916 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 9cd04875-6478-3524-95eb-037ea91d01a0 | -5.90253 | -57.73346 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 463ea75e-5dad-3e0c-bca7-52d1d14e101b | -5.91414 | -57.71434 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3614234b-cddd-3ccf-b594-014efd813161 | -5.9141 | -57.73381 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d9f2a9d2-cc82-30f4-98dc-21052c3bf4c2 | -6.4426 | -58.13996 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b46838f-7652-3931-b247-4e8cbb78a838 | -6.32945 | -58.17493 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1d07652-91d1-30f9-a1b7-20277bee2d1c | -5.90132 | -57.74152 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| bd5d3767-5cf1-3417-a611-76e2f250f437 | -6.43841 | -58.13934 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90d45864-8f83-30af-ad3e-edf011321c41 | -2.93728 | -49.45635 | 2025-09-03 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f305e98e-a2c3-3c4d-863c-11e9b81ab168 | -6.85963 | -52.81746 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5180b761-9f9d-3a4f-9dfb-c2e722d971bf | -6.82589 | -52.83968 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2189e9a3-af90-3f39-9c32-4308f2b299ec | -5.91233 | -57.72642 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fd864e66-6111-390b-8443-c64b9f8fbf7f | -6.05641 | -58.00487 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cf22476-9e39-3cfd-8b93-b35b3bf1731e | -6.52889 | -56.2103 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f81f4a3d-a69f-30f9-a2ad-9adc09e0a7ea | -6.80884 | -52.82909 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc908026-2f59-3065-8214-3294ce16e334 | -5.90013 | -57.7495 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f52ede8-82d9-3b3e-99ae-6c7c485b79db | -7.70827 | -50.30051 | 2025-09-03 05:33:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f16e9c0d-480c-3072-be34-2a1aba82a328 | -5.90619 | -57.73819 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f4cc1f74-3ba4-370b-b92a-e3863e483a69 | -5.90379 | -57.75418 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bcfe4771-8f8f-391c-a985-fb317c0d1681 | -5.91952 | -57.72646 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a886b12f-ea2d-3e5d-8ab7-f4220faa1edf | -6.33418 | -58.17175 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b98d6993-8ad8-30b5-b820-fc8525dc908b | -5.92206 | -57.71987 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 238ed3ba-4f36-3c68-940e-766394b145cf | -2.14418 | -53.65141 | 2025-09-03 05:33:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff6f95cc-acba-3cb8-b6cf-1a3f7f88f42c | -5.90929 | -57.74668 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4c738a33-5e71-31af-93d0-1a89a84cacfd | -6.35073 | -55.5617 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c23b4fd-a734-35a4-9481-99dc90d45f51 | -6.8437 | -52.8332 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a1bd2c4-d177-3994-8b9e-060027b911ed | -6.05756 | -57.99714 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07f9fec5-14ea-389b-ad83-e3767ea8b011 | -5.91172 | -57.73046 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 58af5818-238a-3e26-8b3c-33d224c1700e | -6.3289 | -58.17873 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 859d1a34-4c1d-3bd7-aaa1-95ed11394634 | -5.31998 | -55.8821 | 2025-09-03 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a48789f-0079-3130-a303-73acb28215f0 | -6.80074 | -52.83226 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f741451-1599-3e5a-bf46-1403fb86d86a | -6.80135 | -52.82782 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d5834c0-ab36-3051-a93a-fdbc69b6430c | -5.92027 | -57.73177 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a32b206d-9051-3acb-95ef-45943fc4a124 | -5.89768 | -57.7367 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79bf47c9-d497-34f8-aaf0-9b2455aac24d | -3.47918 | -59.25573 | 2025-09-03 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39c44409-6592-33e2-aac7-5e4c4ed6e173 | -4.99261 | -56.25496 | 2025-09-03 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0082256-20fc-3b9d-8dfe-cc98a4739c0f | -5.92632 | -57.72061 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 71c64e4f-35a3-3c1c-8df7-ee91f6b3bc85 | -6.44065 | -58.1239 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b6b0617-f301-375d-aa77-6440cdb78643 | -6.35114 | -55.55881 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f695f4e-c50e-316f-9992-8ec6bd38f91c | -6.43397 | -55.62172 | 2025-09-03 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7aef058-65f3-39ac-b449-b1b9149dcc4a | -6.82911 | -52.84947 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9beba446-99ad-3b99-8303-c6c2b36f7d5c | -5.91841 | -57.71502 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9570fa94-97a7-36ff-a634-e0440131de62 | -6.43897 | -58.13549 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README102.md)
