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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0bea05a-83c4-35ce-a218-361ee8eaed12 | -6.44965 | -41.74676 | 2025-06-21 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4a900742-98f9-3525-8f81-d27789257cb4 | -7.01781 | -48.29976 | 2025-06-21 04:32:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1af6fa0f-38bc-38b4-9e7c-211ba2567a75 | -3.043 | -49.42543 | 2025-06-21 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2361122-74d8-3afa-83b6-3a1f04ff45e5 | -7.22539 | -43.06808 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 69384037-0386-398c-9919-e4a61deeb235 | -3.96722 | -48.13485 | 2025-06-21 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 93afce35-5277-36cb-af1f-4202c92edf71 | -4.54126 | -48.01252 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d9313750-90ae-3425-8961-4bdf963c2e51 | -4.54457 | -48.01302 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 75f4e0f8-4f22-39a9-9349-8d7f0f8d4615 | -4.37725 | -48.08252 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63c4ebc8-ca4f-3664-93f9-b6df93aead65 | -4.5352 | -48.00805 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 161787a6-2ec7-3deb-905c-ebfda713ace6 | -3.04122 | -49.43677 | 2025-06-21 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 918515a3-af55-378a-9757-fbed1ec1afdb | -3.69904 | -53.75819 | 2025-06-21 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 665180a0-8af4-30eb-a46e-eef43373ef6d | -6.55075 | -47.80508 | 2025-06-21 04:32:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22a2acdf-3eec-35a9-92a2-2fe540da8aad | -4.3778 | -48.07905 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f45e5d3c-72e1-3727-b7f7-c66bec38e402 | -3.6265 | -47.53011 | 2025-06-21 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 93792ccb-69bf-3afd-b4aa-35150ed0513f | -3.97054 | -48.13535 | 2025-06-21 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 68cff74c-3a48-305c-9d91-64137876e2ec | -7.21783 | -43.06324 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 11d149e7-d14b-34d3-9497-310117270bdc | -3.62482 | -47.51932 | 2025-06-21 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9dc685a5-5318-3929-8378-ab6eb57fb87f | -4.5385 | -48.00856 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| fdc111d6-8eb7-37f1-a5a8-71aeece342f1 | -3.04241 | -49.42921 | 2025-06-21 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79617496-d141-37fe-8171-bf6794a5cd83 | -3.03837 | -49.43245 | 2025-06-21 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c9c8b39-fea9-3ea3-8898-7a47695c9248 | -4.53742 | -48.01545 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8c336404-1369-3dd9-b918-056b84a05f98 | -3.62374 | -47.52618 | 2025-06-21 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ce2e394-9f58-35a9-b7a1-af5b274be8c8 | -4.55009 | -48.02095 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6286f0f-3bc5-3fdc-8458-e2ec567a76ba | -7.22136 | -43.06744 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| c4b1c745-1a71-3943-a5f0-a407fa68bf08 | -3.589 | -49.43647 | 2025-06-21 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4bdbb58-d276-38fa-a33f-357999af1a30 | -3.04408 | -49.4411 | 2025-06-21 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 069f177f-99f7-35e7-b32c-d313624a7dae | -2.45242 | -47.50724 | 2025-06-21 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8751ae57-79ca-3362-b93d-24a85eef24af | -4.53796 | -48.012 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| e4f7fef5-ce6e-3fc1-b99c-04dcdcd538dd | -3.42309 | -47.61087 | 2025-06-21 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 322b3565-fd0d-3fab-84d4-4b72ee7c7900 | -3.96777 | -48.13138 | 2025-06-21 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3dd9a3e2-17dc-34d6-a063-4deeb6b1b85e | -3.41979 | -47.61036 | 2025-06-21 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9246d3c8-28c3-3d11-bdd1-804eba9bb85e | -3.11579 | -48.96231 | 2025-06-21 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f21a58e4-134a-3a4b-b33c-f679cf95509e | -7.22891 | -43.07227 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 2fff4606-ea3e-38bd-b6e8-cc4abd9796cc | -7.21718 | -43.56968 | 2025-06-21 04:32:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 14c4073f-cbfb-3642-88a5-7c4f82392ef5 | -7.37082 | -44.56782 | 2025-06-21 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24907c36-b47a-3239-8260-dc6351f00617 | -3.96445 | -48.13087 | 2025-06-21 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 78fceab8-3bc8-3654-b3f6-b8d84a59d5e9 | -7.22841 | -43.0758 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 0036321e-4c25-3225-a199-7e3e0336051e | -3.04182 | -49.43298 | 2025-06-21 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7aed8c57-4f9e-3d81-a51b-7ead1b796a51 | -7.17954 | -44.8749 | 2025-06-21 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7191af88-30f8-36ef-b1da-4cea72f8c5f3 | -4.51539 | -49.24776 | 2025-06-21 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd75869e-2452-3ebf-8455-014740935af3 | -7.15848 | -43.20639 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b471a176-9ee6-30c8-8d2b-570dfab66d4c | -3.96391 | -48.13434 | 2025-06-21 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ac80651f-2117-3470-a223-bad9aded8273 | -5.41684 | -47.56932 | 2025-06-21 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 919e1bb5-abc1-3b0d-8b9f-f1dea08dda0a | -7.17555 | -43.60858 | 2025-06-21 04:32:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db38d6aa-d882-321d-821e-2f0513dc2f07 | -5.77757 | -45.90322 | 2025-06-21 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f953997-55ab-3fcc-9a40-2f6920ff922a | -4.54402 | -48.01647 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 002b5d2e-5488-35b8-9e7f-4aa9155bd883 | -7.27354 | -45.36258 | 2025-06-21 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7d81344-af1d-3124-8331-7e2b82449110 | -4.51258 | -49.2436 | 2025-06-21 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e85abc0c-a194-3d8c-adb7-0d01cabb0bcc | -4.53189 | -48.00755 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 63ecfee1-53c2-3646-93f9-59757679f335 | -3.97108 | -48.13188 | 2025-06-21 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7b20ba33-9d5f-3ec0-a3d0-2e62cc26e8fb | -3.03777 | -49.43623 | 2025-06-21 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1d88ea4-08d1-3000-b834-aa3196ea48d3 | -4.55063 | -48.0175 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acfcd473-e02e-3409-a753-7e5147446847 | -3.62758 | -47.52326 | 2025-06-21 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0451c6fa-b5df-3fb4-b5e6-47c0bd392c1c | -7.30859 | -44.5809 | 2025-06-21 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c189b9b-0bd0-3ffe-a95b-a1fc25f3606e | -6.96831 | -44.14942 | 2025-06-21 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6bd0a408-a63b-321e-82b7-a82eb30de5eb | -3.62865 | -47.5164 | 2025-06-21 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cb7dde5-c820-3e76-a8ee-303f96cfa704 | -4.54787 | -48.01353 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 43eb413a-28ef-3db6-8da8-4f9b0b6cbec2 | -6.65903 | -42.46114 | 2025-06-21 04:32:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f663685f-416c-368c-91fa-6232f1deeab9 | -3.31648 | -48.72023 | 2025-06-21 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d026de3-8936-358f-a80a-305093392b0f | -7.23903 | -44.6745 | 2025-06-21 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 774ce613-c14e-3fd0-b9a5-4ab84621eb5f | -3.9058 | -49.32164 | 2025-06-21 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4d40a6c-bead-3acd-b9e3-275893526bf7 | -6.58564 | -41.76956 | 2025-06-21 04:32:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a384d32f-b9c3-3f00-88dd-510775f4b325 | -7.30617 | -44.57164 | 2025-06-21 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86de9c44-1cea-3ef7-890d-0f8373994b6d | -7.30921 | -44.5766 | 2025-06-21 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3842763a-910b-3ebb-852a-5dee93e0e49c | -5.777 | -45.90692 | 2025-06-21 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfde649d-fc52-3a5a-bb7e-13ec6f49e868 | -7.27 | -45.36205 | 2025-06-21 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25d1ca9e-1355-3b96-9d44-4068d198e16b | -6.65436 | -42.46402 | 2025-06-21 04:32:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dfbbb386-9500-323c-9751-c752b0340f9f | -3.04063 | -49.44056 | 2025-06-21 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4c55c2ce-1faa-3872-a539-f40b57be8bcf | -4.53135 | -48.011 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2247bc92-a552-3747-88fd-31f2c4fd981a | -5.75268 | -43.05289 | 2025-06-21 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d25b9578-a3e7-3b10-ab72-b9d5c4cd81b9 | -5.10855 | -43.14462 | 2025-06-21 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b72c31a6-5f3d-3892-b49f-ec8040eac197 | -7.15797 | -43.20986 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c7eb90ab-045f-384b-b7cd-e171856009bc | -4.54072 | -48.01596 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 79bd4a67-0dd6-3ad6-b81e-16d2d59c2d53 | -4.54733 | -48.01698 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 853e33c1-7dc7-3422-93f4-a01a3f3abe27 | -3.04348 | -49.4449 | 2025-06-21 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bb82da0-412b-3fe8-a991-3426ba7fdf20 | -4.38111 | -48.07957 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 614ee8bd-cd42-3113-a33a-eb1bc3deca5f | -7.22187 | -43.06387 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 0f176304-d80b-307c-8298-b5e3d08b772a | -4.53466 | -48.0115 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6ee2a2d8-f3fa-3a8d-8cbd-23050fbdbd44 | -4.37889 | -48.07214 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0635e22a-70a7-3424-a19c-6abe58114946 | -7.21733 | -43.0668 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7bd90b4d-28c1-331d-8bf7-78ce58605016 | -4.38274 | -48.0692 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eca9c39b-3464-3dfa-a77a-ead8ddd40b8c | -6.93508 | -43.79729 | 2025-06-21 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18f88b12-6468-386a-8c48-01f2ba311aeb | -7.14681 | -44.04192 | 2025-06-21 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0877783d-c3fe-3893-b5ef-32271ae745ac | -3.62811 | -47.51983 | 2025-06-21 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f1c6db8d-7563-393a-92b8-057f14233624 | -7.56283 | -45.11945 | 2025-06-21 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77b82b37-61d2-3182-b8ee-b41c8cf450f8 | -7.15899 | -43.20292 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b1d8a3c8-c242-3a7c-9b7a-8cf9402aa017 | -5.78098 | -45.90375 | 2025-06-21 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2312459b-9969-38a4-953a-33b19152041b | -6.89499 | -42.29102 | 2025-06-21 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 94754f98-9f6b-3a02-8ef3-039d115e5d64 | -5.66915 | -46.60462 | 2025-06-21 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e51c81d9-8513-3a7b-862b-ecd6074cd58d | -9.26317 | -57.52595 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6e639132-36a7-3d15-8549-a166fe78fe80 | -9.25217 | -57.52751 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9591e35c-7f4c-36b3-adea-e6419e138f10 | -8.37617 | -46.97149 | 2025-06-21 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b3a5ddf-d415-3216-91b5-012e9530377f | -8.0196 | -47.65622 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3cfbe22-b811-3c5d-a323-93dd9ee715c4 | -9.26177 | -46.9124 | 2025-06-21 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c757d44a-2331-3211-9a15-ca3e8b94f42c | -10.24137 | -46.80763 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af4d195c-0ce9-3115-a9d8-b04ddb37e0ec | -10.46054 | -47.02907 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0eff1a96-d109-3269-b2e8-c0945129bbb6 | -9.26344 | -57.81789 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d109ce54-a216-369c-9b26-41e54624ad19 | -13.04871 | -53.71259 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8aafc499-35eb-39e7-be74-4f5c93b764fb | -9.4659 | -57.83615 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 737bca3f-f5b8-3396-8773-0db4873dd686 | -7.80988 | -46.05476 | 2025-06-21 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
