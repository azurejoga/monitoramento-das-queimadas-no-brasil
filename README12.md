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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee0cf400-d39b-35e6-bfdd-d7af2c8891e8 | -6.96488 | -44.75099 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0c5f0cf-9484-36d8-a993-fc45e10992e3 | -5.51842 | -43.86883 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| abde0053-1634-3625-b15d-7aade0b26e74 | -8.98413 | -48.94559 | 2025-09-21 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c3e88c9-a357-346d-b776-15ad95bf50af | -5.33746 | -44.90232 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0b7311ba-6008-30e6-b524-f4d1097274e7 | -7.51783 | -41.33688 | 2025-09-21 04:08:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 55370ba6-356f-3de5-ae7d-295a29815647 | -7.94227 | -44.09542 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 84ecae5b-fa32-348d-be3f-cd04a06ff91f | -5.64685 | -43.88057 | 2025-09-21 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33df3dc8-d44f-3da6-98e9-4a2c36832787 | -6.3899 | -43.30594 | 2025-09-21 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 294afa29-e765-35d4-9238-abf213b852b8 | -7.19399 | -37.22684 | 2025-09-21 04:08:00 | NOAA-21 | CACIMBA DE AREIA | PARAÍBA | Brasil | 2503407 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8fb488d7-f5ec-311c-a78d-a20d58be7e8d | -10.04109 | -46.26773 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dd5a23b-66a8-3853-b4bd-7252053691a7 | -6.18599 | -43.13294 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 65ff3650-9dea-38cb-a2a0-1a279ed27060 | -10.03736 | -46.26714 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe7ef9aa-23ad-3c97-a657-606c6bd76d1c | -4.46251 | -44.13326 | 2025-09-21 04:08:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 292f0e9b-bdcc-3e5a-94e7-bc3e1dcea9c4 | -5.63257 | -45.95338 | 2025-09-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d75c4c32-9780-3603-9554-4babd259e5d0 | -10.31736 | -45.23405 | 2025-09-21 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47c54329-8c8d-31fa-b386-e02446580d2c | -9.01349 | -44.96624 | 2025-09-21 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be917c4b-17b2-36e8-84cc-147e842c3bec | -6.25195 | -43.74787 | 2025-09-21 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74ee753a-9b68-33cf-8ae6-0f2a30e1db32 | -7.71483 | -44.47326 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 485c9193-4469-3585-859d-f9db61c9ce34 | -10.29737 | -46.0875 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b91a17b5-0523-38d0-80ed-e9ccadcf2470 | -8.94401 | -44.20212 | 2025-09-21 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89ee6f7a-a678-3b91-a6ca-3a7267c9cba8 | -6.41779 | -43.85157 | 2025-09-21 04:08:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f7b1323-19bc-3bd3-96fa-e4b269172f5a | -10.36475 | -47.90715 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70cb9f30-7b62-352a-8fa8-90f6b0f3d054 | -10.34746 | -47.88548 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bc12176-cc78-3f4e-bbda-53edfcfa363a | -7.35663 | -44.57228 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca23faa8-3751-3cc0-ac0a-0f0e4eda958b | -7.4497 | -42.61792 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 04ebd71e-997c-3842-afcd-4b37621a2b95 | -11.02474 | -48.27329 | 2025-09-21 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c7b1def-4f8a-3c76-b86c-8dbceaca1526 | -6.09031 | -41.0238 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fcb243a4-3049-3e3b-b238-8c6c56e72073 | -3.30417 | -52.58889 | 2025-09-21 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16c01695-1025-370f-bc63-b843d03053a4 | -7.92953 | -44.10883 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2705fbf5-aaa4-3e6a-b6e1-88be385552fc | -9.02427 | -44.87789 | 2025-09-21 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e25d94d-d1a6-3bb7-bd33-f1954558b3e0 | -4.69663 | -44.87563 | 2025-09-21 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73023acc-a2e4-363d-8bda-5e918aa50282 | -11.55839 | -42.82642 | 2025-09-21 04:08:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83d6e1d0-3429-3d84-af48-c441c0f0ac87 | -6.24925 | -43.43803 | 2025-09-21 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdd22525-9512-3cc6-8a23-0fce7ae8c4e1 | -7.93236 | -44.11315 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c008ed7-55e5-3aa8-bbe6-aeff89da9d52 | -5.2482 | -45.33895 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e22b68a0-0d14-3c10-884f-d34e93b7e4ba | -7.918 | -44.11472 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5ec98c9-37a3-3cb8-8fac-47a0d1ecf17f | -7.60125 | -45.4972 | 2025-09-21 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3337fe68-e0bd-3488-bde0-5b28fb1a13d2 | -10.02064 | -46.26483 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2732ce6-0708-39b5-86fd-520587fa2b50 | -7.37423 | -44.57825 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c76d43aa-415e-3354-a080-1c45f1d035fa | -9.18021 | -44.76543 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70bc1cf2-c7bc-3365-bdce-5861a1270343 | -8.01485 | -45.72186 | 2025-09-21 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7835393-ef2f-3d77-8b8f-48f53adec398 | -11.20807 | -42.19278 | 2025-09-21 04:08:00 | NOAA-21 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| b42a387d-69e5-34a4-806a-b8769b11f26d | -8.83976 | -43.03913 | 2025-09-21 04:08:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ba75e07a-31b3-324e-b6ca-812fb36d6e2f | -6.56416 | -43.46875 | 2025-09-21 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9af1e21-a166-3e58-9bd2-39e3d6397080 | -10.32151 | -45.23081 | 2025-09-21 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94736a8d-9b29-33dd-9649-efc5cd54bdca | -5.27678 | -44.81335 | 2025-09-21 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac974fbc-05a9-3fff-88dc-2d8a2016a8c5 | -10.27019 | -46.11412 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64d23057-e22f-3af2-a808-c4f68f7cb362 | -4.64707 | -46.31455 | 2025-09-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62667496-8433-36d8-b1d5-b7828d311046 | -3.60804 | -47.53138 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ad3863a-64c3-3805-832e-3a8bc6506259 | -5.00303 | -45.17707 | 2025-09-21 04:08:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d8c1854-0a40-3b5f-a118-8f5df68a5fba | -7.93014 | -44.10506 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1988947a-dd5b-325f-a422-06dbbd61a5a3 | -5.42499 | -43.27422 | 2025-09-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9b81f2f6-4728-34cc-9be2-24a2917965bb | -10.32503 | -45.23135 | 2025-09-21 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb73db35-220f-33b7-8de4-90cbad949743 | -7.93884 | -44.09487 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c6be4630-120f-3b57-b8ab-18153184c0f0 | -7.21715 | -43.75436 | 2025-09-21 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f58e2d6-05e8-3dd9-8929-2bf91ab1f6da | -10.0905 | -46.08862 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e6e4660-9022-39a9-bb46-c1f62294a9bd | -5.79816 | -50.20284 | 2025-09-21 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cdd89413-6901-33b1-8a33-65252a528a1f | -4.51033 | -43.52071 | 2025-09-21 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f889b09e-de1c-31d6-a52d-60f8debf2fc4 | -10.24045 | -46.48982 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2d33793-e0c4-3750-b0f3-11933bd11964 | -7.416 | -44.54387 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40754f3e-fb0d-3368-816b-48edf7d17269 | -7.95377 | -43.89381 | 2025-09-21 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d0c4f81-2f69-3bed-a9e8-7ce839791de0 | -10.57316 | -48.58754 | 2025-09-21 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9b54079-a99a-3042-a75b-41dc068d7983 | -7.73201 | -44.45596 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 210b5607-ee3f-3a45-a377-bb928bb28e8e | -7.56164 | -42.2118 | 2025-09-21 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0b4af373-7b8f-361e-a53b-979b85c6866e | -8.83644 | -43.0386 | 2025-09-21 04:08:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1a8e4516-7105-3c47-b0b4-4405ea36f3b4 | -10.33229 | -48.69533 | 2025-09-21 04:08:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3253778b-ece5-3f45-bd1d-891aca704171 | -6.32907 | -42.96375 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e43a5e90-06e1-3e5f-b3c3-aac9dcc5e46f | -7.92388 | -44.1002 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f07b88b7-3205-3161-88e3-a1e3a87317c6 | -5.28614 | -44.68818 | 2025-09-21 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aa963fa-8ae1-3fa7-8714-8304e0eb5e7f | -5.40747 | -45.27227 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a29dab1-9473-3880-a35f-838a30c0a307 | -11.26289 | -40.9665 | 2025-09-21 04:08:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8768c0a2-8409-3855-b004-208d6447a441 | -10.36129 | -47.9028 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2473fe54-36f9-3842-aae6-f06d4dcac5e6 | -6.22853 | -44.65903 | 2025-09-21 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1143f3e0-6f9e-3c05-a4d3-16e90216ba91 | -11.47554 | -43.54763 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e72b408-e65c-31b4-89d2-58924dfe9f45 | -4.63664 | -45.61213 | 2025-09-21 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad48fa2c-b293-32f7-bd2e-c901ae47ee70 | -3.3075 | -48.71521 | 2025-09-21 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85db947d-7ed4-3e36-84c3-929d71900a38 | -5.45131 | -45.50021 | 2025-09-21 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94765e08-32ac-3ac6-81ca-6c1a24df64b0 | -6.25265 | -43.43859 | 2025-09-21 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bdd9b0a-6825-3b1b-830b-7a810d35e28d | -7.56494 | -42.21233 | 2025-09-21 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a220bb02-e6d9-340c-a7f8-7fafeb1e0e62 | -5.09201 | -48.42163 | 2025-09-21 04:08:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f972615a-5cac-3fa6-8672-bd3f377cd54c | -3.32744 | -52.54126 | 2025-09-21 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d728688-712d-3064-8692-4eed5728ff37 | -5.52191 | -43.86935 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b3fb2dd8-e2aa-3567-84fa-42d5181b8cb7 | -5.74562 | -43.3777 | 2025-09-21 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7eaacfb9-1ce2-30eb-81dc-2cf4974d0337 | -6.19888 | -41.20032 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0a82c603-b4b1-3bbb-9fed-27e167509430 | -5.47436 | -45.3812 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14ecbbae-e48e-3048-8f48-03528ff9d7e1 | -6.67787 | -38.50054 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 37c3d31c-cf44-350f-b7a6-cd5a663e8a3d | -8.281 | -41.68123 | 2025-09-21 04:08:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d85b8336-5e41-3bd4-a4fe-7f3399026b99 | -7.05039 | -41.95705 | 2025-09-21 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 60beed17-a63a-3b58-9558-813c8e11537f | -11.51183 | -43.6189 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55f8df27-bad6-338b-a36b-1b991cf4c23d | -5.69757 | -51.75298 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5f479e1b-ac05-3a59-ade5-c4640b6294bd | -5.52951 | -43.86655 | 2025-09-21 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e0c1a25d-15da-3e4d-abd9-03802662f663 | -5.25125 | -45.34395 | 2025-09-21 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbbb8b2c-e9b5-321b-8752-a23ffd8aa3eb | -5.40085 | -43.53392 | 2025-09-21 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cc5a469-d09c-3cc7-943b-78027b9e2f66 | -9.06149 | -47.01419 | 2025-09-21 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d0b1040-cb5f-3736-88da-a72d9c3e2bf7 | -11.28135 | -41.85054 | 2025-09-21 04:08:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a2e04fe2-edc2-3e1d-b6bc-8d50ecfada58 | -7.93702 | -44.10617 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de7a93b3-1583-396d-8200-66a614ca9d50 | -10.33866 | -47.88766 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29d00e3b-278f-343f-a032-c470c566bab5 | -7.73329 | -44.44815 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a5911b2-ef14-38d7-940d-31d1040d8bf5 | -7.92327 | -44.10396 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e610b9f-c091-3b5b-aa0a-833402e3373c | -3.35561 | -48.39714 | 2025-09-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README13.md)
