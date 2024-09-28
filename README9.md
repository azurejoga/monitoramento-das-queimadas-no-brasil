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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7298ba28-27d6-3f78-bdb6-e41481565df5 | -5.7562 | -47.065399 | 2024-09-28 00:14:54 | METOP-B | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2f208f6-9cce-3701-bdbc-bfaa811807f5 | -5.7581 | -47.0742 | 2024-09-28 00:14:54 | METOP-B | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 953ec528-f07c-3206-8f50-42aabb13ccd1 | -5.3785 | -45.398602 | 2024-09-28 00:14:54 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04a603ad-3c23-3f5b-9569-fbc022ae0a46 | -5.5601 | -46.266102 | 2024-09-28 00:14:55 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c352c236-f329-3a8f-aa3c-b2fa8d36a71b | -5.5618 | -46.274101 | 2024-09-28 00:14:55 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45c6ed12-1868-3c5d-8b1c-7bbd5b310b8e | -5.1905 | -44.923698 | 2024-09-28 00:14:56 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f037b05-a820-344a-925f-0b86981d6070 | -5.1921 | -44.930801 | 2024-09-28 00:14:56 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8305da04-1e2c-3aa4-81e3-c7196bc5bb42 | -5.1937 | -44.938 | 2024-09-28 00:14:56 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 993ca89e-f5c2-3c94-bdae-383b3b9642b2 | -5.1953 | -44.945099 | 2024-09-28 00:14:56 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5eec5f4d-4e0d-3cb2-9a43-55c534864be7 | -4.7304 | -43.241199 | 2024-09-28 00:14:57 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fdc34eab-18d6-3164-99d3-25969a24a34e | -4.732 | -43.2481 | 2024-09-28 00:14:57 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54f2ab0b-229e-37af-bb9d-303ace3c430a | -4.7418 | -43.245899 | 2024-09-28 00:14:57 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e86b301a-dd41-3deb-b57a-4907ed0d6a7c | -5.1529 | -45.401901 | 2024-09-28 00:14:58 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 769b6811-75dc-3d4e-9ccc-2336404e40ac | -5.1545 | -45.409199 | 2024-09-28 00:14:58 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42dcd4af-6486-3ed8-872c-85961b43c301 | -5.9457 | -49.165298 | 2024-09-28 00:14:59 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a67f59a-3b11-3e05-8764-33c8844dab83 | -5.9483 | -49.1772 | 2024-09-28 00:14:59 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8421cf-5a90-337a-9a99-c9a7b06a5e7e | -5.9359 | -49.1674 | 2024-09-28 00:14:59 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2a698bd-21c1-3c69-8bcb-61574e19be42 | -5.9385 | -49.179298 | 2024-09-28 00:14:59 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07ae0518-8fde-3c29-b3c1-59bd9903811b | -5.9411 | -49.1912 | 2024-09-28 00:14:59 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a192dc6b-b85d-317b-bbd1-a99335f1b7ba | -5.3446 | -46.593399 | 2024-09-28 00:14:59 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd89f0f-0d24-3fb4-aea8-2623658ac9ab | -5.3464 | -46.601601 | 2024-09-28 00:14:59 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ac2d8a2-11ee-3ca7-bbce-7110429a4d74 | -4.6529 | -43.811401 | 2024-09-28 00:15:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcb8f3df-bd35-35d2-848b-ffc259603039 | -4.4391 | -43.046501 | 2024-09-28 00:15:01 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 264c2415-813a-302f-8ad8-100ff55117f2 | -4.4406 | -43.053299 | 2024-09-28 00:15:01 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb7ed957-429a-3ed0-bc93-242dfbff3b30 | -5.0902 | -45.814301 | 2024-09-28 00:15:01 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 77c720eb-1b35-3aa4-9324-6332493c8a25 | -5.0919 | -45.821899 | 2024-09-28 00:15:01 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13431561-955c-321a-9cb9-175c0b34afec | -5.0936 | -45.829498 | 2024-09-28 00:15:01 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6771b9c1-c074-32c9-bbc0-53903d4f688c | -4.9846 | -45.385101 | 2024-09-28 00:15:01 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e03ce98c-a8fd-3661-b1d1-c0bac813de52 | -4.9862 | -45.392399 | 2024-09-28 00:15:01 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e11ab4f3-cf03-3768-b3bb-e8ce1e200baa | -4.9878 | -45.3997 | 2024-09-28 00:15:01 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f528fa6-0df8-38e3-814c-1059c59db0f0 | -5.3779 | -47.165501 | 2024-09-28 00:15:01 | METOP-B | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78d32a15-980f-37d1-a017-bc7d70803ec1 | -5.3799 | -47.174301 | 2024-09-28 00:15:01 | METOP-B | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3cad3931-ca50-396c-a8ab-ae79b01106bb | -4.8595 | -44.870201 | 2024-09-28 00:15:01 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69cc8a85-87ff-39d5-a978-c4f1c37b3370 | -4.9764 | -45.3946 | 2024-09-28 00:15:01 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0b65178-46c7-388b-8922-c58826c549a0 | -5.1061 | -45.978901 | 2024-09-28 00:15:01 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18b00e7b-afcd-3ea1-8da2-bef0cb73287c | -5.0695 | -46.092201 | 2024-09-28 00:15:02 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb7aef44-df78-3b0e-a877-b50b842db73b | -5.0712 | -46.099998 | 2024-09-28 00:15:02 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81dbdc8c-318c-3e19-a4c5-683db583a153 | -3.9649 | -41.505402 | 2024-09-28 00:15:03 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9d43face-1cf0-3419-bfc2-f9980b5019c0 | -4.9325 | -45.659698 | 2024-09-28 00:15:03 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7cbb176e-dacf-3994-a467-f0e8b8790cad | -5.3288 | -47.690701 | 2024-09-28 00:15:03 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e1d8932-0d16-392b-82e3-b1ee44d8ae31 | -4.2583 | -43.021801 | 2024-09-28 00:15:04 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 394a9e95-9d1a-3402-b5c4-db54b4cbef84 | -4.2598 | -43.028599 | 2024-09-28 00:15:04 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4fef81b4-7c2b-3e8e-a57b-d70562126d8d | -4.7822 | -45.261799 | 2024-09-28 00:15:04 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff0194ba-31b5-3276-b4c6-e29aec60c8d2 | -5.319 | -47.692799 | 2024-09-28 00:15:04 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b08b565a-2b36-3aaa-9608-d3585390aaa4 | -5.4533 | -48.355598 | 2024-09-28 00:15:04 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7674d52f-c6d8-3c36-a335-11866c827f2b | -4.0894 | -42.458599 | 2024-09-28 00:15:05 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5571404c-c4c8-3c3c-bff8-034a30748636 | -5.3732 | -48.222698 | 2024-09-28 00:15:05 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ba557c22-42d5-3d0c-adae-86c59e16dde5 | -5.3634 | -48.2248 | 2024-09-28 00:15:05 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 906bbd35-d299-3eae-8cdd-dfd17f8b2180 | -3.9199 | -42.257401 | 2024-09-28 00:15:07 | METOP-B | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 278a697b-7b09-397d-a350-57d7a70bd8f3 | -3.9215 | -42.2645 | 2024-09-28 00:15:07 | METOP-B | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ac484f5-4256-37f9-afc8-25787b57a04f | -5.2164 | -48.161499 | 2024-09-28 00:15:07 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1a7955-7f7f-34ff-976c-3207d3c99797 | -5.2186 | -48.171501 | 2024-09-28 00:15:07 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1411da08-76bf-3798-9a91-1d20db6ec677 | -5.2066 | -48.163601 | 2024-09-28 00:15:07 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0eb62c71-d57b-3db4-aa49-5a5b70c70463 | -4.0261 | -43.225399 | 2024-09-28 00:15:08 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99ab20b7-1b9d-3bdd-9429-5fcbf88cfda5 | -4.0277 | -43.2323 | 2024-09-28 00:15:08 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f1bf4ff-2edb-3651-b13f-590389d03008 | -5.2329 | -48.424599 | 2024-09-28 00:15:08 | METOP-B | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7bbeaea5-edb8-3e2a-af30-5f91c5c0759e | -5.2351 | -48.435001 | 2024-09-28 00:15:08 | METOP-B | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e38d80f8-56b3-30ab-a1a2-57da78e190cd | -5.2051 | -48.344101 | 2024-09-28 00:15:08 | METOP-B | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8345c8f9-1449-3e1c-88db-7179da1f1a99 | -4.0396 | -43.467098 | 2024-09-28 00:15:09 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b35db13f-3b13-3fce-b688-06a9a39e081d | -4.0412 | -43.473999 | 2024-09-28 00:15:09 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b412d66-d51f-307f-b88d-1252e05a005c | -5.2608 | -49.212601 | 2024-09-28 00:15:10 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7641d441-f94d-3b6f-88cd-9745df4fd195 | -4.5604 | -46.3923 | 2024-09-28 00:15:11 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2fbc52ec-3932-3d8b-b102-9eef90ef159a | -4.5621 | -46.4002 | 2024-09-28 00:15:11 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91ed69cd-7072-38be-9837-40e4c5aa23d3 | -4.5506 | -46.394501 | 2024-09-28 00:15:11 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0ff0622-082a-3457-ac2a-439274810dc8 | -4.5523 | -46.402401 | 2024-09-28 00:15:11 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4139af86-7ca6-3b24-b177-08a010031e04 | -4.4333 | -46.3293 | 2024-09-28 00:15:13 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4768fa68-5359-37fb-8093-c9571fa6c1d0 | -4.435 | -46.3372 | 2024-09-28 00:15:13 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5c931773-b8e9-33b9-a7d0-73e0cd059262 | -4.9109 | -48.592098 | 2024-09-28 00:15:13 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45cf203e-ff17-36e8-9a14-ee249b8e9aed | -4.9132 | -48.6026 | 2024-09-28 00:15:13 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2a17fc0-f855-3f66-8696-dab1c8d6909e | -3.5141 | -43.057301 | 2024-09-28 00:15:16 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b302857d-7348-3413-9b20-256b7291e8c7 | -4.5844 | -47.990398 | 2024-09-28 00:15:17 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c6ea9ad-fddb-32b3-94bd-23b3887e30ba | -4.5865 | -48.0 | 2024-09-28 00:15:17 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf83920a-5347-33b3-b285-6ce95165993a | -4.5747 | -47.992599 | 2024-09-28 00:15:17 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7917af7f-7f3e-360a-bbdb-d42bf0511f65 | -4.5768 | -48.002201 | 2024-09-28 00:15:17 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 187053e5-7670-3af0-a87b-7b87057f83da | -4.5789 | -48.011799 | 2024-09-28 00:15:17 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bee63f24-5dbc-3b7a-b808-602e3ef75bb9 | -4.581 | -48.0214 | 2024-09-28 00:15:17 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c818ad7-ce2e-3cb9-b285-06818b91c976 | -4.5691 | -48.013901 | 2024-09-28 00:15:17 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c536772a-cb03-3c97-a163-7b2b5bcd84ef | -4.1403 | -46.676399 | 2024-09-28 00:15:19 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a854b22-7749-3877-964f-ad783872c830 | -4.1421 | -46.684399 | 2024-09-28 00:15:19 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd2302b-c79c-3a7a-ab60-158a88787d29 | -4.1305 | -46.678501 | 2024-09-28 00:15:19 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c3762d0c-c498-3c75-b43b-42a177c19e28 | -3.2532 | -43.042702 | 2024-09-28 00:15:20 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59dce75d-75bd-3c2f-8770-0cab8ba0158f | -3.2547 | -43.049702 | 2024-09-28 00:15:20 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dffc569-0333-3034-848c-df79df0bf8e6 | -4.409 | -48.078701 | 2024-09-28 00:15:20 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e2e90b6-8b2c-3a9f-a367-18fb07a3a0de | -3.2956 | -43.503399 | 2024-09-28 00:15:21 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5178818-2b82-3bf4-b3bb-725991f02327 | -3.2971 | -43.5103 | 2024-09-28 00:15:21 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4803b26-4030-3b4e-b05b-3d0a768ab0c0 | -3.2987 | -43.517101 | 2024-09-28 00:15:21 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 078367fa-f023-368d-81ec-20c2736f98bc | -3.9137 | -46.442902 | 2024-09-28 00:15:22 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2fc39bbe-7ea6-3984-881c-4e32d4197cb7 | -3.9154 | -46.450699 | 2024-09-28 00:15:22 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1c7d494-6df8-3fa9-b6f2-a94a2e840f37 | -3.9172 | -46.458599 | 2024-09-28 00:15:22 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| edfa9f48-d35b-39cf-8b9b-ba066f83f1af | -3.9039 | -46.445099 | 2024-09-28 00:15:22 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 740a3e34-d499-31a8-a7d2-2bf9db724bc9 | -3.9056 | -46.4529 | 2024-09-28 00:15:22 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 666051f2-3b4a-3df0-904a-7d41a736db9b | -4.3999 | -48.691002 | 2024-09-28 00:15:22 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb5ae05-f74b-321d-8b1a-9dc74783e65b | -4.4022 | -48.7015 | 2024-09-28 00:15:22 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17d2c39d-3872-368d-ad68-ad547ebab6d8 | -4.4027 | -50.672199 | 2024-09-28 00:15:29 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9092d2c6-9ccf-3ffe-a38c-5779ca3eab21 | -3.6967 | -47.595001 | 2024-09-28 00:15:30 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb73cc0d-fabd-369a-8653-28b337000969 | -3.6987 | -47.603901 | 2024-09-28 00:15:30 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e226645-837c-3933-9a53-da1b972e3799 | -3.3181 | -47.0005 | 2024-09-28 00:15:34 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f071e87-61d4-3bb1-a218-7481d80e2ea8 | -3.4636 | -47.654999 | 2024-09-28 00:15:34 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f60bdd0f-ddad-3496-b23c-bf5326a80910 | -2.9539 | -47.3498 | 2024-09-28 00:15:41 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff00f6a7-d97f-3c6c-9630-7519456f96f6 | -2.9558 | -47.3582 | 2024-09-28 00:15:41 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
