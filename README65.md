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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43752ee1-f88c-3394-a800-642f63d6c6ea | -10.6641 | -54.1491 | 2026-09-14 10:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 6e8893ae-63e7-3759-ba0f-ec03173806cd | -10.6641 | -54.1491 | 2026-09-14 10:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 36f0fe8a-6487-352f-bf51-a7f500038007 | -10.6829 | -54.1475 | 2026-09-14 10:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| b6a02807-ac43-3827-886a-44b2808a5061 | -10.8093 | -46.3179 | 2026-09-14 10:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 6f4cb0ba-5702-3c17-a3f4-d0fb03d50f63 | -10.6641 | -54.1491 | 2026-09-14 11:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| ff45e933-2c0e-3afb-b6b5-a7cb1686b452 | -10.6829 | -54.1475 | 2026-09-14 11:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 774003da-3900-3138-81e0-c54f13044867 | -10.6827 | -54.1679 | 2026-09-14 11:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| b0d9d56f-e967-37c0-9000-c1dbd8f8ac54 | -10.6829 | -54.1475 | 2026-09-14 11:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| be9a6931-3b72-3fb2-85b9-1d8e13141d4c | -10.6641 | -54.1491 | 2026-09-14 11:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| e90a7f56-e07d-36df-a86f-db4d292ee035 | -2.91 | -50.4 | 2026-09-14 11:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05210651-9988-30e0-9501-e6fedc5af902 | -10.6829 | -54.1475 | 2026-09-14 11:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 5afe80d5-e9bd-396a-81a0-e1dcb5efea60 | -13.3059 | -51.3022 | 2026-09-14 11:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 319b1ba7-4a7d-30e1-afc6-f343ed266b40 | -10.6641 | -54.1491 | 2026-09-14 11:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| a23a12e7-f1d4-3973-8f42-d38f5a2e8803 | -10.6827 | -54.1679 | 2026-09-14 11:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 68e5ca3d-5151-3e92-9bde-411e51e69c91 | -3.794 | -44.10363 | 2026-09-14 11:28:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| edbe9692-d495-34a5-92d5-83cfd5864612 | -7.46759 | -45.95815 | 2026-09-14 11:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 8e4af27c-2a17-3f9c-a476-45df7996cd95 | -8.06865 | -45.347 | 2026-09-14 11:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 19bad5a5-54b8-3c81-a77f-619d0d2bd0d5 | -7.97268 | -43.98215 | 2026-09-14 11:28:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 568ec533-ae8c-331f-9ab7-9ebe85112d17 | -7.05499 | -45.27564 | 2026-09-14 11:28:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| da52f035-97a1-3cee-b230-812c498cdd87 | -5.5658 | -39.25138 | 2026-09-14 11:28:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| ebf95235-227a-3d02-a4d7-a663106f6595 | -7.16121 | -42.1072 | 2026-09-14 11:28:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 4d79ff6b-5972-319f-a3bd-67f2dd2a22fa | -7.46593 | -45.96909 | 2026-09-14 11:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1903281c-e07a-3b1c-8f6e-9ccb7c32100b | -6.93764 | -42.71401 | 2026-09-14 11:28:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 97201fe5-e4b4-3610-b466-9203cf79105f | -6.36784 | -43.59612 | 2026-09-14 11:28:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f4b93f1b-c940-3b18-8640-7b4354661858 | -4.85084 | -45.21242 | 2026-09-14 11:28:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f8dd94c1-ff84-3a60-8c6c-d662298a5fd4 | -7.09209 | -41.81451 | 2026-09-14 11:28:00 | TERRA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 0b8995ec-7d40-390c-98fe-6244c0d9327d | -7.78063 | -46.53125 | 2026-09-14 11:28:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 84c56f63-ff67-34ac-860e-df1c2d1c5df2 | -6.947 | -35.27258 | 2026-09-14 11:28:00 | TERRA_M-M | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| efce03ea-4629-3263-acb0-e469f0727a81 | -6.33693 | -43.35822 | 2026-09-14 11:28:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 01633461-ad2b-387b-9355-d9cdac6bfb11 | -7.09764 | -42.10761 | 2026-09-14 11:28:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 31583f8d-5188-325e-a220-108dd340bb42 | -4.22008 | -40.60912 | 2026-09-14 11:28:00 | TERRA_M-M | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c37d85ea-d832-39ea-9b69-b19c34c4fa17 | -7.13577 | -42.09454 | 2026-09-14 11:28:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 73c41d5d-d6b5-394c-83cc-6bcb0ba6b501 | -7.1078 | -42.09985 | 2026-09-14 11:28:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| bacb9cfe-fdb0-3b61-af32-11b09cb10bbe | -3.22936 | -43.03001 | 2026-09-14 11:28:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b04e081b-212c-3287-8089-0fda1a07e6e7 | -7.09338 | -41.80535 | 2026-09-14 11:28:00 | TERRA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| e2e06f05-142d-37dc-9e8e-a3179a7d9473 | -3.59734 | -41.36563 | 2026-09-14 11:28:00 | TERRA_M-M | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 5c775e2f-4da4-3f41-b8a6-f62444f480f2 | -6.34451 | -43.36836 | 2026-09-14 11:28:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 032be19c-3539-34d7-996a-9129b4951d72 | -6.75345 | -45.01088 | 2026-09-14 11:28:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e008684c-f71c-3b15-9f98-2f814ab2f7ef | -6.33566 | -43.36712 | 2026-09-14 11:28:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| d53934d9-c629-3d57-978e-a4595e24bc8f | -7.56471 | -37.2562 | 2026-09-14 11:28:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 11a9f7ce-ac27-37f4-b4a8-c2e481c9d59a | -7.04555 | -45.27424 | 2026-09-14 11:28:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b14c5b52-3441-3851-a050-3ca02f6ef826 | -7.01844 | -44.63953 | 2026-09-14 11:28:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 559f2688-d7ad-34af-9b31-ee4288fa4320 | -7.0908 | -41.82364 | 2026-09-14 11:28:00 | TERRA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 89fb3cc9-e161-3349-9848-29b3adb329b1 | -3.7926 | -44.11326 | 2026-09-14 11:28:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a37f0166-96c7-32b7-a896-83203c5be660 | -6.92882 | -42.71278 | 2026-09-14 11:28:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| c487c6c5-d295-31bf-937c-b720f3a5b335 | -8.27215 | -37.44789 | 2026-09-14 11:28:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 79f12a26-b094-32aa-bb7c-f16a5749450e | -6.80523 | -43.18393 | 2026-09-14 11:28:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 898271a2-011e-31d3-9acc-2dd965ebe8c0 | -8.1197 | -44.05264 | 2026-09-14 11:28:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4d816b45-cbe0-3e54-ab38-143ca782c8b9 | -7.01985 | -44.62997 | 2026-09-14 11:28:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| c14dbe21-cdcc-34c7-8ace-109dbd9753b5 | -7.16248 | -42.09821 | 2026-09-14 11:28:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 79d646e9-5c9f-3c68-b67f-7624409db1de | -6.29876 | -41.68661 | 2026-09-14 11:28:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2c512c05-32c5-3071-9ec5-f0c1604dc8d6 | -5.1952 | -38.97688 | 2026-09-14 11:28:00 | TERRA_M-M | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 650d35e0-5639-3851-bfb8-8dcef8452464 | -7.12288 | -41.7907 | 2026-09-14 11:28:00 | TERRA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 141202ab-9ec9-3d83-801d-39c5793815dd | -5.19688 | -38.9648 | 2026-09-14 11:28:00 | TERRA_M-M | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| e69c1622-c120-3bd5-bd15-138bc04c4a6b | -8.04958 | -45.54247 | 2026-09-14 11:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0a300781-4fdf-3f56-810d-ce2dd5000c3f | -2.88302 | -40.87057 | 2026-09-14 11:28:00 | TERRA_M-M | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 835c4a22-a9e3-324e-a2bb-f2d48965f875 | -10.6641 | -54.1491 | 2026-09-14 11:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 8d4e415b-a0a2-3292-bb86-313b8d3b323a | -10.6827 | -54.1679 | 2026-09-14 11:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 9ae8c118-8679-3c31-9ee4-2f5b4d055448 | -10.6829 | -54.1475 | 2026-09-14 11:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 3102b979-7e5c-30e0-a6fa-4e5ae649ef78 | -13.6349 | -47.8969 | 2026-09-14 11:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 05001e77-26d6-3681-840a-8a2d360ef2b8 | -14.173 | -47.44325 | 2026-09-14 11:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 9533b48a-c6db-39bb-9068-2c5a18ce0247 | -16.27116 | -40.75687 | 2026-09-14 11:30:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 03ac96c5-3b92-3b61-b8a8-5efe6f7f5927 | -9.46072 | -47.84764 | 2026-09-14 11:30:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5982e8b6-c369-3127-90ef-4d84d308e367 | -10.44006 | -48.64318 | 2026-09-14 11:30:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 0a497103-4b2c-31dc-ad47-3f2cdf3e1e41 | -16.24602 | -43.01978 | 2026-09-14 11:30:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2a3196f2-d13d-39b0-8172-c31279b1a320 | -10.80904 | -46.31401 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| cfaf4ec7-5da1-3075-a32b-1a0bab608080 | -10.81698 | -46.326 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 48458110-8844-32e2-b268-102b44909ae4 | -15.58062 | -48.80306 | 2026-09-14 11:30:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 254537c2-543b-3854-b38f-080143537cdf | -10.80432 | -46.3175 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 39f1a2cd-f12e-3947-b9b8-6511ccb62079 | -13.58837 | -47.90201 | 2026-09-14 11:30:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| b7921cc6-f0fc-3feb-8be4-fbe0f8aeac53 | -10.29862 | -45.30367 | 2026-09-14 11:30:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4e7d64df-591a-3960-9a87-32ec29d50c04 | -10.81068 | -46.30337 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| eb1fb913-acdc-3ae4-8f89-149ce87c6c0e | -15.54925 | -48.7976 | 2026-09-14 11:30:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| d7086b08-a0dc-3e7e-9463-42df0ad74642 | -13.40958 | -41.61486 | 2026-09-14 11:30:00 | TERRA_M-M | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 43f692e7-3641-3619-9f46-05397e5bb563 | -9.0957 | -45.88888 | 2026-09-14 11:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 0b8418d8-4968-3457-a9a8-8d846d173132 | -12.53563 | -47.15499 | 2026-09-14 11:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 55cb82ec-2b66-3cd6-a264-6ece94adf595 | -11.24173 | -43.44575 | 2026-09-14 11:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| da6be00d-5e52-33da-9d41-35554a1380ec | -9.19917 | -44.43129 | 2026-09-14 11:30:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3f2dd30d-859b-37a0-a2d0-ff4025f25c3e | -10.81534 | -46.3367 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8e8ad49e-27a9-3e50-8109-614e61bb63d7 | -8.81044 | -45.88105 | 2026-09-14 11:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| f614c541-70d5-3dc3-9885-3b36763571a9 | -13.5903 | -47.88953 | 2026-09-14 11:30:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 40571214-8ad1-35c7-83c8-9125c05f6320 | -15.54715 | -48.81065 | 2026-09-14 11:30:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 35b1f961-66ca-31bf-91f5-26697a602689 | -13.63878 | -47.90438 | 2026-09-14 11:30:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0dc30d86-eddf-3b48-86d4-6edf4e9f6b9b | -10.80274 | -46.32815 | 2026-09-14 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0b2c3524-f3e7-351b-88a2-43d15697912b | -16.27262 | -40.74472 | 2026-09-14 11:30:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 293c7066-0fb9-38f9-b3c7-9ea6926f0089 | -9.03306 | -42.43262 | 2026-09-14 11:30:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| bc0c9b69-8bf5-3873-9689-e88edbc36cb6 | -13.41106 | -41.6039 | 2026-09-14 11:30:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 3599a991-86cf-3332-b43b-5946f5de14d8 | -12.77571 | -43.93548 | 2026-09-14 11:30:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 52715245-2cd1-3e04-8833-604e53b42829 | -8.61672 | -44.44037 | 2026-09-14 11:30:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0a0b7eda-3b20-3b5d-a797-5488bf57dffa | -11.18208 | -42.81576 | 2026-09-14 11:30:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 706f20c1-fa9b-3534-bcbe-e0b708e25bbb | -11.34157 | -46.77625 | 2026-09-14 11:30:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 17613286-da92-3adb-80c7-6eddd7e84bea | -11.55997 | -39.58118 | 2026-09-14 11:30:00 | TERRA_M-M | NOVA FÁTIMA | BAHIA | Brasil | 2922730 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 518062f1-efc2-3455-9948-f1853f7b6018 | -9.48984 | -45.46266 | 2026-09-14 11:30:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f49a1dc5-a12d-3f27-bd31-e4fc734159c0 | -13.57821 | -47.90038 | 2026-09-14 11:30:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 8e8474af-3c88-3262-980b-1ee590b825ab | -9.48836 | -45.47257 | 2026-09-14 11:30:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| b5ac04be-a335-3651-8c12-1f9c7bcf1547 | -13.28754 | -51.30895 | 2026-09-14 11:30:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 5a89f69b-7db0-3ce9-a7f0-b066dc487ac9 | -14.18274 | -47.44493 | 2026-09-14 11:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 516e85d5-ab48-3d11-ae4c-1b371a531a44 | -12.4049 | -44.40407 | 2026-09-14 11:30:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 62047a83-b604-3883-b231-cf70b30eeb66 | -13.30081 | -51.31127 | 2026-09-14 11:30:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| cf031b8b-a547-368a-bd1c-532e62a6c27b | -17.13674 | -44.77785 | 2026-09-14 11:30:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |


[Clique aqui para ver as próximas entradas](README66.md)
