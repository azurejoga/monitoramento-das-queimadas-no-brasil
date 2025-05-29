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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d279fb2a-feb0-31ab-b505-475709f8092b | -11.79161 | -54.77691 | 2025-05-29 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 577a4846-03d7-3e1d-b2d8-946778ff774b | -14.21303 | -47.71975 | 2025-05-29 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d370472b-fde6-3e56-b4d9-029eaea46637 | -10.83411 | -54.03474 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5baebba3-260d-32cc-aab8-9bb17f466886 | -10.93783 | -55.32477 | 2025-05-29 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbff5bf6-b46e-39e0-9c50-4668955af5bd | -12.1128 | -54.66417 | 2025-05-29 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bc41da1-e9e3-3d63-adb9-ec5f5ddf64e1 | -13.08246 | -45.27986 | 2025-05-29 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2222602-5d42-3e43-a5d7-17014f47241c | -11.29737 | -53.98156 | 2025-05-29 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc690ef3-b64d-3088-8c97-f60f79fd8204 | -15.07747 | -48.94653 | 2025-05-29 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 433a63c5-5890-325f-ad50-fff6dc0feffa | -10.72749 | -49.54289 | 2025-05-29 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e6b56431-222b-3ded-8085-a177a8890141 | -14.21175 | -47.73083 | 2025-05-29 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9235116b-8354-3523-8cc3-0bc2b1da965a | -10.19823 | -52.64977 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5ed0c2a-a79e-3221-b164-d7e00bbbb658 | -10.8117 | -54.03961 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fecf7de-a3cb-3496-8f71-ebab110f96d0 | -11.81107 | -55.06839 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b09c11af-dfe3-3dbf-947f-a30d149dff45 | -12.39591 | -53.24495 | 2025-05-29 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7844f898-b0b2-3a6c-a510-55fca75a7dab | -10.73044 | -49.29533 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| df48c20b-f47e-35c3-948a-12d9706c54aa | -11.08041 | -55.05523 | 2025-05-29 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e274d1dd-ea85-38d1-8802-666657394892 | -10.81877 | -54.04068 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2c6b2fe-f888-3da0-929d-033c55094969 | -11.5743 | -47.44672 | 2025-05-29 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7efea10b-3261-3e14-8211-81ab26e06fd0 | -12.30826 | -47.27312 | 2025-05-29 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee388a36-015a-3d91-801b-2a9de2eb190f | -10.7355 | -49.28512 | 2025-05-29 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8668fbb5-d851-3c1a-b354-37f5b030506c | -11.40431 | -52.95269 | 2025-05-29 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdcc239f-27f6-38fd-868e-94c7fcec7c47 | -14.21133 | -47.73456 | 2025-05-29 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ecdf63cf-a6a8-3689-a22e-598e5459dd78 | -10.32939 | -57.49231 | 2025-05-29 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edae388c-203d-3018-8498-24d644343536 | -14.66513 | -45.08664 | 2025-05-29 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3dfd4b9e-4d86-3000-905e-6dc69d226361 | -11.80765 | -55.06785 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d8d18ea-90ac-366f-984d-cd3c8edfbd03 | -13.66196 | -45.42531 | 2025-05-29 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 66be3ffa-c4b0-35f4-9eff-39ba02e749e9 | -10.81643 | -54.03207 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f4acd8d-f0f1-3e74-9233-4b8443177f31 | -10.82057 | -54.02859 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c56ff86-bf8b-3865-9943-85b8b218427c | -10.95109 | -48.15369 | 2025-05-29 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc7fd799-4013-3624-ad08-a4e9fb95e1de | -14.21345 | -47.71613 | 2025-05-29 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a6fb448-b16e-3558-8a2f-33d7b0055d22 | -14.21815 | -47.7241 | 2025-05-29 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ed72b6d1-262a-3e4a-90d2-1b9e7f25f9d8 | -10.83291 | -54.04279 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed9b77e3-b069-3b33-830d-39984b2abfbb | -11.80423 | -55.06731 | 2025-05-29 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57da99ae-9adb-3587-b609-7213e8858f23 | -10.8355 | -54.05011 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7cf39f7-f286-3a47-8a1e-c1182ef28f47 | -11.82138 | -44.27139 | 2025-05-29 05:06:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bc6d31b3-efd5-3cda-9c14-74f088206158 | -12.39207 | -49.96764 | 2025-05-29 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c860c135-1669-35ab-a4f0-b7b998125d7b | -11.78816 | -54.77636 | 2025-05-29 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a24bb1ae-4b61-361f-8d87-dade11b101ec | -10.83231 | -54.04683 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83577feb-f4da-3f8d-b6bf-62edc51bbd0b | -11.81538 | -44.26451 | 2025-05-29 05:06:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b325ebae-4687-3a01-b579-b6f4c8059d05 | -15.07789 | -48.94307 | 2025-05-29 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c4e37b9-4bc2-3f82-8316-992eaf6c1738 | -13.65964 | -45.42503 | 2025-05-29 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5cf39f3a-f3ec-3879-a8e6-89fba669dab4 | -11.28864 | -46.43999 | 2025-05-29 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a794ab98-21cd-31e2-9a5b-709558f5328c | -10.72218 | -49.54718 | 2025-05-29 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eef5602f-85d0-347f-9941-fef8a2081df7 | -12.3087 | -47.26936 | 2025-05-29 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf3fa4ef-ac09-3e42-839f-773e1fd19c0f | -10.72154 | -49.55217 | 2025-05-29 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e3cc855-0461-3cda-92be-9da9d4b20271 | -13.666 | -45.4258 | 2025-05-29 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6853aa5b-1d9a-3fa7-a630-6cebfd36ea90 | -10.8235 | -54.03315 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b231dd43-5bbe-39d4-9056-cf7e9085404b | -12.38681 | -49.9719 | 2025-05-29 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e77600b-c976-3197-8ff6-2e80984e8b30 | -10.9412 | -55.32531 | 2025-05-29 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 438b321b-6763-34ff-9529-57c5ccdd53b1 | -11.13633 | -53.9225 | 2025-05-29 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46376f90-e678-3736-beb2-81c7ed0a855c | -12.30915 | -47.26555 | 2025-05-29 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46dee468-813d-39de-81ad-764fe7987402 | -14.66572 | -45.08849 | 2025-05-29 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c034dc58-ce31-3c0a-86e7-81ec8ab28ad3 | -21.52921 | -56.0282 | 2025-05-29 05:08:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 68c006a6-7493-3d7d-b36d-d27f415eeea8 | -18.3814 | -44.52026 | 2025-05-29 05:08:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a18667df-bd4a-35a6-a6ff-a48a88028e19 | -14.2182 | -47.7167 | 2025-05-29 05:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| be3f05a0-158f-3f20-bfa6-4795533a47db | -25.19043 | -49.32838 | 2025-05-29 05:10:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 77c0adac-ff94-3bba-a67f-40bc7df610bc | -2.65489 | -48.80217 | 2025-05-29 05:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d82037b-8795-33e2-928b-c183baf949cb | -2.65886 | -48.7966 | 2025-05-29 05:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3efbf06-81ba-3bbf-aefc-67f391bf4d9d | -2.66158 | -48.80309 | 2025-05-29 05:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51400602-107c-3fab-b5dc-796d5545247d | -6.21615 | -57.7732 | 2025-05-29 05:29:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1116248f-1df8-3a2b-8b91-c4659751c9f6 | -2.65574 | -48.79626 | 2025-05-29 05:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9621c88-6757-3ccd-99b9-ee0eff2afd36 | -3.31528 | -53.79168 | 2025-05-29 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12ac8449-ccbf-307b-988c-4056728431c9 | -2.65797 | -48.80243 | 2025-05-29 05:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 344b890e-78f3-3ec3-b4c8-807087607fda | -12.46676 | -53.32019 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec503607-876f-3090-ad3a-7f8fde1f3d61 | -8.01416 | -49.6869 | 2025-05-29 05:31:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95bfaf81-9510-3fe0-a9f8-2360caf86ae0 | -11.90986 | -54.40984 | 2025-05-29 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26d625d3-5146-3d07-bb0c-b3940e7a3922 | -11.81042 | -55.07668 | 2025-05-29 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23f42803-be73-31fb-92c3-6df30ca5c391 | -12.38538 | -53.25882 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 148aa620-d4f7-3aae-9851-c7da2eb37869 | -9.35738 | -57.54785 | 2025-05-29 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7da2bee-8478-3f33-9ef9-aeaa4a8f6732 | -11.13892 | -53.91363 | 2025-05-29 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edeb07da-ffaf-3e4f-9ece-74f7f6889884 | -12.41252 | -53.32314 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 373cfb10-e439-3790-9c6c-3250525fa90d | -12.41776 | -53.32785 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 96d1b4bc-2bcf-3eff-9818-e963170096fe | -9.20166 | -49.47025 | 2025-05-29 05:31:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 47c58ad6-2fc1-31ae-9317-841887e3a1eb | -9.35791 | -57.54411 | 2025-05-29 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb423c94-4ce6-3fb4-98a8-b02948a54387 | -10.83028 | -54.04425 | 2025-05-29 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f66a1425-a848-3831-bd59-99169fbe0f7d | -11.80611 | -55.07004 | 2025-05-29 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4479aa9f-1e7c-3d7a-8d8e-96620964ae62 | -9.20082 | -49.47693 | 2025-05-29 05:31:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ccdac2f3-950b-3138-b148-ea246f634ab9 | -9.20667 | -49.47031 | 2025-05-29 05:31:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9096d2d6-3ddb-3486-aeb4-f5f81ce5c626 | -12.31872 | -49.99064 | 2025-05-29 05:31:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b77c7c9e-ce7c-3c32-a2a3-5c2cc0639534 | -11.91432 | -54.41728 | 2025-05-29 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ccb3300-332d-39ae-afc8-755d24f3dfec | -9.2086 | -49.4714 | 2025-05-29 05:31:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c4b25b15-785f-3e9b-a593-49395557b9e4 | -11.29837 | -53.98428 | 2025-05-29 05:31:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 887120b6-2406-340c-b3dd-ec9847460392 | -9.21284 | -49.47795 | 2025-05-29 05:31:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e2ca4c42-0bfa-3052-a5e7-dee40daf2b67 | -11.0393 | -50.77713 | 2025-05-29 05:31:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d58cb1ea-043b-3a11-bd3d-ea224da197ea | -12.43019 | -53.32135 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de360ddb-4607-3a6d-9667-03079538abcc | -8.74544 | -49.76349 | 2025-05-29 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bec8cf83-da42-3e13-82db-96817a9a1b20 | -11.14622 | -53.94271 | 2025-05-29 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3fdef9a-b85e-3b4b-a5fc-d4af511a25a4 | -12.41825 | -53.32387 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 361c7bd1-e560-3fa2-8a14-25b1acfd99c6 | -11.29297 | -53.98349 | 2025-05-29 05:31:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0868bc26-3f4a-3277-95b5-a5ee18fcb58a | -10.8352 | -54.0482 | 2025-05-29 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce009424-5be7-31e8-aa70-74a90d4336bf | -12.10616 | -54.6674 | 2025-05-29 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64815ed0-04f9-3236-9882-6980b59b0157 | -8.75105 | -49.77101 | 2025-05-29 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b98d057e-2c04-32fe-a617-feae8aa17147 | -11.80106 | -55.06934 | 2025-05-29 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1504321b-f13b-313b-9c17-755b83653ce6 | -9.20588 | -49.47694 | 2025-05-29 05:31:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 82910eb6-9721-3305-9513-404a74964886 | -12.42571 | -53.32299 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9096a6e9-a51b-3443-9192-813ae14a328f | -9.36203 | -57.54475 | 2025-05-29 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8946183-1512-3d31-9593-022bdbf3a36a | -11.90902 | -54.41658 | 2025-05-29 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42ef52ea-dc36-3af1-97ef-61d610b56e3b | -12.38317 | -49.97003 | 2025-05-29 05:31:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cd1fafd-e648-3089-86f6-39181b1eee79 | -9.35685 | -57.55158 | 2025-05-29 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea03a5b0-7181-3ca4-a260-54a0d3b09cd8 | -12.46629 | -53.32417 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README17.md)
