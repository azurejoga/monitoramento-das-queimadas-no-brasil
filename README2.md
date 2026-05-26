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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77b69ca8-54db-39aa-8753-927f90cb5989 | -11.3551 | -52.935902 | 2026-05-26 00:14:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25cf8bad-d53a-3dcf-a9d2-bd9d4564bba0 | -6.5226 | -55.041801 | 2026-05-26 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3353176f-c5ad-3e3a-8f7d-0095b07b4a9d | -11.9652 | -56.788898 | 2026-05-26 00:14:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04749b8d-a7f3-3924-9f00-64ccb47d531c | -11.1671 | -55.886002 | 2026-05-26 00:14:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35e8af69-7ed1-3f3f-95df-fbed77cecbc0 | -8.9765 | -47.9702 | 2026-05-26 00:14:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9a4e704-cfbf-3ee3-b02e-e9b666e59ea5 | -17.250401 | -48.2924 | 2026-05-26 00:14:00 | METOP-B | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a1aa2173-f7af-31f6-82d1-7e72800c45db | -7.0116 | -44.988602 | 2026-05-26 00:14:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c8acd9b-5663-3a06-b777-7cbc9c7c609d | -11.3649 | -52.9338 | 2026-05-26 00:14:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8a8232d-9648-3d96-9288-eec4959d08ed | -5.7885 | -45.133801 | 2026-05-26 00:14:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58257f5b-edaa-3657-968c-eb69de3249ef | -5.7939 | -45.1267 | 2026-05-26 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b3f7863c-e8c9-38e8-8f29-6d3df054fd2b | -11.3773 | -52.9496 | 2026-05-26 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 629c8fee-199f-3df5-86cb-b7d5083635f8 | -11.1903 | -55.9101 | 2026-05-26 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| d7989868-4b70-3d0c-8998-f245f9f343ef | -11.1714 | -55.9117 | 2026-05-26 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 8dd8a61b-5db6-3628-97f9-98252f6c2284 | -7.1355 | -44.0553 | 2026-05-26 00:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| fbdf05f3-0fc6-3eab-9e21-aa6ddbf569bb | -11.3584 | -52.9514 | 2026-05-26 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 4b3bcd9b-ea88-37b5-851e-fa26c8b22d81 | -11.3581 | -52.9722 | 2026-05-26 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 384280c8-7e5a-3152-8f96-e4235045e863 | -17.2463 | -48.30676 | 2026-05-26 00:26:00 | TERRA_M-M | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8abe97ba-8113-301d-b9c3-0baaa3a26621 | -20.27564 | -50.72235 | 2026-05-26 00:26:00 | TERRA_M-M | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 5999c4fc-dc9d-3490-9c21-f0e25e527099 | -21.32108 | -47.07885 | 2026-05-26 00:26:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 89619954-5626-365f-9b7e-5b09cb3578d6 | -21.55533 | -47.06136 | 2026-05-26 00:26:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 52.9 |
| d5052ded-3d50-3132-a1c7-a8946c176877 | -20.27695 | -50.73173 | 2026-05-26 00:26:00 | TERRA_M-M | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4727f7a0-629d-374c-b492-e8ccfa48ca27 | -17.95262 | -54.46596 | 2026-05-26 00:26:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 41ab0a27-489f-32de-96c3-5947bb955a3b | -21.55329 | -47.04865 | 2026-05-26 00:26:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 68.2 |
| aaa212eb-c47d-3d37-8169-be2babe09698 | -21.319 | -47.06615 | 2026-05-26 00:26:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 77f27601-2065-3f6e-a23b-1c0c3bb72c9a | -21.26935 | -49.47867 | 2026-05-26 00:26:00 | TERRA_M-M | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 58c2664f-edac-3072-a239-0692b43a6b5f | -17.24447 | -48.29482 | 2026-05-26 00:26:00 | TERRA_M-M | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8599c25d-9b87-3d31-8a37-7a01f6553add | -11.74849 | -54.79686 | 2026-05-26 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fb7f3c18-71bd-318d-aeb8-de304fe7213e | -12.05626 | -57.426 | 2026-05-26 00:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 73d18589-726d-3a10-a777-91dc1b20e883 | -13.96515 | -53.88216 | 2026-05-26 00:28:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3bd3a13a-82e2-3a48-8197-6d9e3be7ce41 | -11.91275 | -57.03737 | 2026-05-26 00:28:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5a609d6e-5d41-3d1b-8101-c83b74922346 | -11.36248 | -52.95972 | 2026-05-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 168.4 |
| ddac8c22-9b34-3531-a0eb-560d7b1963c8 | -11.54917 | -56.92914 | 2026-05-26 00:28:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 85860b91-25ff-3954-9505-291fcfa3b988 | -11.21449 | -53.83134 | 2026-05-26 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 538ede62-cb50-34ca-803c-3b97341ce49b | -10.60401 | -44.33465 | 2026-05-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| b579be39-8406-3764-b3b4-513d413cc0ac | -12.05267 | -57.41779 | 2026-05-26 00:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 58642a70-fe39-3455-b8bf-cc1649e253a8 | -11.54334 | -56.93641 | 2026-05-26 00:28:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ecd7bc0f-767f-3991-9b03-351f53c17cae | -11.97554 | -56.81012 | 2026-05-26 00:28:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a6bdf525-a76a-3c0e-8976-896caf3873a0 | -12.45776 | -54.45167 | 2026-05-26 00:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 287ede6d-93d1-3127-9899-82b511a1fb8e | -11.55076 | -56.94213 | 2026-05-26 00:28:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f1ec075a-4fe9-3954-a299-a69ebb94ecb5 | -14.6683 | -51.80541 | 2026-05-26 00:28:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 84343356-c99d-3642-ae4a-261d9d1b2708 | -11.9651 | -56.81152 | 2026-05-26 00:28:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 63c50312-2689-3bb0-b366-d242ab7d1122 | -13.28114 | -48.87145 | 2026-05-26 00:28:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 65e48890-f516-365e-8000-0d0799bdd140 | -13.27917 | -48.85894 | 2026-05-26 00:28:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 47678677-dccc-30b0-a925-a05a7f96eeb5 | -13.2826 | -48.86427 | 2026-05-26 00:28:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 635d6e58-b70f-37ff-bb47-cb95263719ba | -10.87655 | -51.21629 | 2026-05-26 00:28:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a285dd43-1fcb-3180-989a-cf914033da7d | -11.61191 | -54.18106 | 2026-05-26 00:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e61da3da-e8e0-3d25-a26c-1a62c238c257 | -11.79545 | -57.00459 | 2026-05-26 00:28:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 081d2c6f-078d-37a7-9cd5-478149f8141c | -10.60774 | -44.34065 | 2026-05-26 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| dafd709a-68a0-383e-a253-67d0955d0005 | -11.36124 | -52.95079 | 2026-05-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 115.9 |
| a7c1a80f-33ef-3026-b59e-8f5753982e75 | -13.66163 | -55.30635 | 2026-05-26 00:28:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2858430d-1d55-3146-9618-173f1dea993a | -13.6506 | -55.29673 | 2026-05-26 00:28:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| bf2800c3-08e7-303b-90ec-53526ba1cf39 | -10.66442 | -49.72406 | 2026-05-26 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 943fe54f-0db1-387c-882b-da3ad9e0329a | -11.95094 | -54.09951 | 2026-05-26 00:28:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 111ed698-71ff-3778-8d4f-82a7057960c0 | -12.45903 | -54.46128 | 2026-05-26 00:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 218731d5-367d-353f-8b2e-b81c00662d39 | -11.35244 | -52.95206 | 2026-05-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 0b5c422a-0583-3ab2-a8d7-616dac49a030 | -11.74057 | -54.80796 | 2026-05-26 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 675183ce-3767-3b05-965d-425fa87dd52a | -11.35367 | -52.96099 | 2026-05-26 00:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| e98719c4-28ac-32eb-862e-7fc82e7a6cfa | -10.63412 | -48.33172 | 2026-05-26 00:28:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 17d20d7b-5151-375d-9e2f-665beaf57d51 | -11.21325 | -53.82228 | 2026-05-26 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed3f7d6d-72a4-3a27-8cde-fcbed7c700f5 | -12.44863 | -54.45293 | 2026-05-26 00:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f9285955-be82-35fe-8406-b2c540f68b54 | -13.66025 | -55.29545 | 2026-05-26 00:28:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 33.1 |
| b7147dd1-fbea-3d9f-ad8c-441fa52cf1aa | -11.1903 | -55.9101 | 2026-05-26 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 325425d2-9d62-34be-8d33-1db37d9ade4e | -11.3773 | -52.9496 | 2026-05-26 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 9a430fe2-0f9f-30ac-8de5-65ac96368ddf | -11.3581 | -52.9722 | 2026-05-26 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| df9db8fc-4610-369a-b27c-a19bafb2a3d3 | -11.1714 | -55.9117 | 2026-05-26 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| ddef678a-7c0c-3e8a-83ae-8ed688de0666 | -5.7939 | -45.1267 | 2026-05-26 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| f73fdaa0-1621-3045-bb7e-3a30bb693de9 | -7.1355 | -44.0553 | 2026-05-26 00:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 654161c6-ca9b-393e-9eb7-29451adaba09 | -11.3584 | -52.9514 | 2026-05-26 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 157.2 |
| a9f0843f-2705-3e6c-81f0-e1ed0e016978 | -9.29647 | -45.48132 | 2026-05-26 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 2854829a-fa9a-3c70-bfa6-b2ad13656f8d | -10.92194 | -54.11413 | 2026-05-26 00:30:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 0d576b83-1c16-3d67-87d4-a451d2832c9e | -7.14115 | -44.05687 | 2026-05-26 00:30:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 90000396-f83c-34dd-867d-d00382f1e783 | -5.78998 | -45.12654 | 2026-05-26 00:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 38c42014-8311-39d4-a6be-2f02d3328fd0 | -11.1781 | -55.92296 | 2026-05-26 00:30:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 4923a6e2-dc9b-31bd-95c6-99860c779aa8 | -7.14584 | -44.0509 | 2026-05-26 00:30:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 40.6 |
| f0dc3705-c015-3ffc-a72e-9a7e17b99bc2 | -8.97999 | -47.97776 | 2026-05-26 00:30:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 292fa381-09d4-3bde-9a35-e0e5b0c6daef | -8.55342 | -45.99846 | 2026-05-26 00:30:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| d8916422-efdc-369e-ae84-10882af7b99d | -10.36817 | -51.91177 | 2026-05-26 00:30:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 028f9f14-9d12-34cf-af4f-b231b2a5fcb6 | -9.4486 | -50.84945 | 2026-05-26 00:30:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 06d82d1e-ac1b-39b4-b4d0-42dae3800073 | -8.71186 | -55.0054 | 2026-05-26 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ae66a940-110e-3fe7-a592-f40accd1a46b | -7.147 | -44.09289 | 2026-05-26 00:30:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 45.8 |
| d1acf4cb-2859-35f1-8c3b-8d2dd178725a | -10.8442 | -53.75179 | 2026-05-26 00:30:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 37e1952e-cbbc-327d-b0d8-ae74c21bfdbf | -5.78354 | -45.12086 | 2026-05-26 00:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 9e076e6d-3046-38c8-a025-6167b05f24af | -10.92317 | -54.12331 | 2026-05-26 00:30:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c8fd9dfc-d3ad-31e1-9ddc-6047b8b91b8b | -9.30072 | -45.50753 | 2026-05-26 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.4 |
| b95100e6-834e-3c75-a06d-3bb68dd7de70 | -7.15193 | -44.08691 | 2026-05-26 00:30:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 41618e83-a313-36c0-8b7e-632bfbc64ae4 | -11.18782 | -55.92166 | 2026-05-26 00:30:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5591bb00-75e5-3460-8d21-2b71c5fc7284 | -8.71062 | -54.99617 | 2026-05-26 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 7c472d78-538d-3b41-9490-c751506f0554 | -8.98256 | -47.99467 | 2026-05-26 00:30:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| fc144d26-befa-347f-a3ea-935f68cbb614 | -8.52434 | -54.77321 | 2026-05-26 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 883463ec-a309-3b3c-805f-e653c18a7e8c | -9.30307 | -48.59099 | 2026-05-26 00:30:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 58ab198c-0dd9-387c-b347-c492bcdd6f95 | -11.1767 | -55.91208 | 2026-05-26 00:30:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 184.1 |
| 63a987a6-fb47-370a-937b-0099eab30d35 | -11.18641 | -55.91075 | 2026-05-26 00:30:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 8bcf8da0-2f93-3316-956f-bfcda5ef7c4a | -6.51937 | -55.06552 | 2026-05-26 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d267a01e-0a08-3892-87b9-4eaabdd678f3 | -4.42802 | -47.73672 | 2026-05-26 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| eaa1d729-001e-3537-89e2-8b58cddf7d08 | -11.3581 | -52.9722 | 2026-05-26 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| a3b4f996-2938-3754-803e-469aba303688 | -11.1903 | -55.9101 | 2026-05-26 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| d6a226b0-4c36-3883-92f4-2cd452a44e77 | -11.3773 | -52.9496 | 2026-05-26 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a537ac66-afbe-3388-b50e-5069cc329571 | -11.1714 | -55.9117 | 2026-05-26 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 7e085e0c-71b9-36c7-880b-46968abbdd4b | -7.1355 | -44.0553 | 2026-05-26 00:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 95748af6-9ae4-3386-bdec-31e854d19c36 | -9.496 | -40.3337 | 2026-05-26 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 40.7 |


[Clique aqui para ver as próximas entradas](README3.md)
