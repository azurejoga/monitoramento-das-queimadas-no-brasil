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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af0f10c8-a74b-3f9c-ac67-bbae30a0ecad | -12.44206 | -44.74696 | 2025-09-17 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f30d6ae-aa26-38b9-b004-ffe135220203 | -14.59653 | -46.32515 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dc543a6-ad23-3353-963e-2f4e63ba81fb | -7.72215 | -45.29829 | 2025-09-17 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f20998e-9df8-3414-936d-e6343846c2d6 | -9.1167 | -44.87167 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 213a306f-54a1-39f0-bd80-b1346668eb6e | -11.50774 | -43.7093 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8dab4f1d-fdae-308e-bf9e-450d62fa0e4c | -8.34868 | -44.71732 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 407d5b03-b82e-3595-953f-c2136f5cef2a | -12.70899 | -47.9817 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cf548f27-a143-3673-85b9-547de62f91b0 | -12.69889 | -47.97018 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| de70b64a-cded-3b65-8783-2fd2d12579c0 | -12.75277 | -47.96365 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| faf671cb-0347-3ed1-99e7-d3df45a11877 | -7.71731 | -45.29364 | 2025-09-17 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05bf0e5a-86e8-3bcc-8259-aefbafc4cff0 | -13.36926 | -43.77475 | 2025-09-17 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 644af557-ec99-39af-8b44-3e75a1e0f5b3 | -11.04048 | -42.24968 | 2025-09-17 03:45:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 958f4003-bcba-368a-bc11-1bc3c324e95f | -8.92592 | -46.27376 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f45cca71-665f-30d3-8585-f7f19616d5b8 | -8.13656 | -43.64896 | 2025-09-17 03:45:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5608be3b-0d38-3431-b1cc-d4b43c77fab4 | -8.56094 | -46.36871 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc98223b-fec6-3758-9856-bc22822dae72 | -7.67619 | -46.6393 | 2025-09-17 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d4ddf55-1cc7-30a9-bee8-c65030a1d8c0 | -10.81999 | -42.70354 | 2025-09-17 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 27d2d526-e59e-3acb-b61d-3d11b7c910c9 | -8.883 | -46.18699 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 742fb55c-0f92-3f42-9a05-a9c21cd57cc1 | -8.96782 | -46.01392 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 99d7dcd8-1451-34b9-921f-3df806d8e736 | -11.02747 | -45.06529 | 2025-09-17 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 04fd00b3-b378-3056-94ca-0f09951a6365 | -11.46452 | -43.55851 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4eaa9a3-e5c9-318d-8875-570d32910764 | -9.11271 | -44.86416 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a73775f1-8bce-3f83-9fc2-2fe52a5acd09 | -9.11332 | -44.86089 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9250eca1-461f-3634-8450-07218e066f4f | -14.62034 | -46.39597 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05d35e9f-f271-37fc-b75a-7367875d3431 | -12.10853 | -44.81601 | 2025-09-17 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40a786e3-0c8d-3075-9935-1202730a5254 | -13.22006 | -47.2891 | 2025-09-17 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ebade244-177b-3b6f-93b4-90fc738e5a27 | -12.09639 | -44.82646 | 2025-09-17 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dca5755-f6e6-3f1a-a955-ccc8b818b285 | -8.47061 | -44.73083 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4a8f4ff-2c68-31f3-8c99-dbdf1cc06a24 | -9.60361 | -40.57405 | 2025-09-17 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 573f136a-d93e-36a0-8912-7a7723dc8db3 | -8.15891 | -46.7596 | 2025-09-17 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 720909c5-e5f3-3a95-a6fe-c47f72999041 | -15.76769 | -41.6165 | 2025-09-17 03:45:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| aa91f246-76b7-3d26-8f01-214e48c14b6c | -15.76799 | -41.61381 | 2025-09-17 03:45:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b124e07c-ea3c-3cb4-b95d-8097db076ae0 | -9.24489 | -45.65062 | 2025-09-17 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca4c77e5-07b1-3fbf-aa23-886fe99e9e31 | -7.76789 | -44.72914 | 2025-09-17 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f7d16ab-0d29-369a-b2fc-9e88bd1b5808 | -11.02294 | -45.06135 | 2025-09-17 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 53e3ad17-6066-3a40-812a-11802408bfab | -8.3481 | -44.72062 | 2025-09-17 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b4ddcad-5430-352c-ba00-efa101fa2582 | -11.49845 | -43.68204 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c318056-13e3-3c18-a4b7-cecbb39251ad | -11.49258 | -43.61332 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59757a16-5f47-3375-b6f4-0f07cedc5d4e | -7.47741 | -46.10355 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c38d586-ba27-3128-85f9-fde780947eaf | -9.55086 | -46.30197 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54d20944-b1f4-3b91-981b-057fbe857ad1 | -8.98691 | -45.75399 | 2025-09-17 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22e0941c-4af7-3549-a823-95d264d005e0 | -9.54591 | -46.29708 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30f40fff-2366-30a1-99e0-fb4747980991 | -12.70622 | -47.97913 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89e7226e-4570-3cb2-8276-a39b818aab0a | -9.06161 | -44.87548 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8a9e9b4-cad0-3bc0-b313-8f054c8f4fea | -10.32373 | -46.59985 | 2025-09-17 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2cd3d93c-2457-32c2-9200-6ba7607a058e | -8.93015 | -46.28292 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72a5650b-7b04-3f13-8241-e50c1adbdbbe | -11.46739 | -43.56882 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 758dee83-0db8-3cbc-8861-0c5c00b88bff | -8.65577 | -46.40652 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 47e11845-2c9f-3b7d-a2fb-3d39de52bb33 | -12.35667 | -47.06408 | 2025-09-17 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eec82c61-9bd4-3815-b6bd-2795d6bdbc70 | -12.70392 | -47.97606 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9942880c-e1cb-3cdf-bb91-e860ae00bc43 | -9.05792 | -44.8364 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 620bfd27-6682-343e-bc3d-8b72b8d59276 | -9.09864 | -44.94017 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9628521d-7910-30d0-83fe-0597e36c5c36 | -8.93882 | -44.48868 | 2025-09-17 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b356eee2-46f4-322c-92f2-0a8c946ac1c7 | -12.97846 | -47.94868 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56bc9cd6-c7a8-36e0-b0f3-5b0ff2653f0c | -9.36401 | -45.37963 | 2025-09-17 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe930f53-36a5-3b4c-9b21-abb40bc0d6b0 | -12.10356 | -44.81531 | 2025-09-17 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b95a42f0-75fa-3a3f-b342-4daff879bf9b | -15.10114 | -41.0678 | 2025-09-17 03:45:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| cf35047a-76e5-313c-b609-4514f1da0aa1 | -12.70218 | -47.96867 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6e19306-daf2-3f18-bade-200fbd95cec7 | -9.46078 | -40.37552 | 2025-09-17 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7868f096-ae40-3798-97d3-ec8c94021ac2 | -11.47283 | -43.56489 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c4e9777-4cc2-3b36-b990-34861851d50d | -7.49107 | -46.127 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbe4c734-08c3-3d6e-93ac-92a159058d58 | -13.23025 | -47.29699 | 2025-09-17 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4499b01e-4d68-3de0-8c2f-679e1162bc11 | -12.72563 | -48.023 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36fe9cd9-42e8-366a-9825-6d6792fe8d10 | -8.53493 | -48.97424 | 2025-09-17 03:45:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7540ea3b-ce82-3f90-a131-37e10f1f2e11 | -8.95922 | -46.32502 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14c58d2d-41ac-3102-b18b-d16eef561e4b | -12.34987 | -47.05709 | 2025-09-17 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 60aa1a7e-6866-331b-883b-2c4eb27061fc | -12.70118 | -47.97351 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06bfbe82-c4b0-39d6-9837-4e124fc6c598 | -11.46911 | -43.55929 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c9bf143-4323-3cc8-aea5-77ad368b53b9 | -12.7476 | -47.95866 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9445c80-38ff-322c-b98a-d4fdc6430ead | -11.49172 | -43.6157 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45e684d6-d79a-3553-b867-23f1b213c166 | -11.12666 | -45.11478 | 2025-09-17 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e29a4d3-da9a-3092-88cd-e712457a0bd1 | -12.06814 | -46.56659 | 2025-09-17 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f902c54-4f9c-3817-8bae-7c33ee965b4d | -9.32182 | -48.76384 | 2025-09-17 03:45:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 64c31a4c-a865-3cc2-97b9-5a8db9c967a5 | -10.20494 | -42.54243 | 2025-09-17 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 12ccac1f-1ac2-3aa1-a529-312d2964cb81 | -12.00383 | -46.68864 | 2025-09-17 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71bf8a4f-a21f-37d0-a340-9f7ca1edc157 | -9.06994 | -44.94907 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 578e320b-a5e9-35ef-a1ea-84a41890d1dc | -8.78312 | -47.81015 | 2025-09-17 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4dc409e-0c67-34a5-aee3-19009592a4f1 | -9.09922 | -44.93705 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb63ce15-1072-3d0d-848e-cd3c9825fdad | -8.9629 | -46.00908 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bad0f5f3-bab1-3a58-b433-be97fdd39f42 | -13.20769 | -46.7801 | 2025-09-17 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31a0fcc9-2db9-3af6-a398-e8a01d857894 | -12.36224 | -43.20427 | 2025-09-17 03:45:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7506e3e2-4d61-34da-8545-58f17165fb53 | -12.4959 | -44.6918 | 2025-09-17 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af4b9e7c-90e6-378d-bb8e-c6023b95b116 | -14.15464 | -46.13647 | 2025-09-17 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 788de5be-e9ba-3a57-abe5-af531e11b3dd | -8.63217 | -46.4365 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06954ef1-cfdc-3153-952b-f9881d3169d5 | -12.86345 | -47.13893 | 2025-09-17 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 232354ea-2a6d-3f65-95f7-c0ced73cbfd5 | -11.93528 | -38.33184 | 2025-09-17 03:45:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 746653c5-1078-347d-973d-8c7e36995d5f | -12.70335 | -47.94781 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 24665c7b-aa7c-3a2f-b8d5-872a95633c48 | -8.96425 | -46.32981 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13864ace-07aa-3cbd-a043-dcc194144919 | -14.61438 | -46.3713 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d717013d-a15e-39e2-8250-851b5e9888dc | -15.77145 | -41.61723 | 2025-09-17 03:45:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f3da9325-c729-364c-82da-fb86cd541c4b | -12.6999 | -47.96513 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cd5c4f9c-95ba-319d-8e18-6d503f69fcff | -11.49715 | -43.61428 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19b670ec-c42e-35e7-85b1-d147b8d91382 | -14.86296 | -45.12095 | 2025-09-17 03:45:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc11726a-ac40-32d9-a43d-4f39b96402fc | -14.60788 | -46.40419 | 2025-09-17 03:45:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40d414cb-b901-3a14-bfd1-dd93413eb631 | -12.1025 | -44.82102 | 2025-09-17 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cd1f841-14d5-3a05-a2ad-748936302bfc | -12.74676 | -47.96278 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62ddad9e-d12d-3c85-a882-a156991167a3 | -8.95785 | -45.75647 | 2025-09-17 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b23fadec-91c5-3a5b-846a-a70479be61ab | -12.70991 | -47.97708 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be18d355-7a96-32db-bf2d-02c1840f5d73 | -8.77195 | -46.09637 | 2025-09-17 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ca0718d-a08c-37ad-891f-854921a95c2b | -12.97164 | -47.95192 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README14.md)
