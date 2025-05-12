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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c110e44-10a2-3bb5-b74b-a464b667672a | -10.49378 | -46.17929 | 2025-05-12 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9746e8c2-ad51-34a9-bc6c-5ee5c4f85ed5 | -14.20488 | -45.48032 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ca3dbf7-b0fe-3e49-886e-0f3302f9c2c9 | -11.89447 | -56.41245 | 2025-05-12 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68083367-47fa-31ca-8649-8ba4e0256862 | -11.91768 | -54.40702 | 2025-05-12 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75a5224f-5aa2-3f95-be65-d5dc7d7f2e1e | -14.65459 | -45.13093 | 2025-05-12 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 845af8a8-922f-38c8-a8e3-10b047c38c91 | -14.20176 | -45.47503 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5548db7e-f33a-3e0c-aa0c-ac99be91704c | -10.45369 | -49.07828 | 2025-05-12 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4877315b-3be4-3832-aab5-db77905ff537 | -13.04218 | -53.72749 | 2025-05-12 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a24cd9cd-8d8d-3187-b215-749b7d9f31ed | -14.19485 | -45.46915 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2156ccf3-0b4e-32d1-9f4f-f37643a5760c | -14.19797 | -45.47447 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d100f6da-77df-33ae-81fe-f54f58a2c46d | -7.59313 | -45.86071 | 2025-05-12 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03d8e4f4-22dd-3a08-88a3-837dee5ad665 | -11.91698 | -54.40637 | 2025-05-12 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beb854d2-57bc-3b80-a943-bca1965ef439 | -14.20481 | -45.47682 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ad23a9e-55c0-3f27-a269-2d949177076a | -11.88982 | -56.41158 | 2025-05-12 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b216417-8714-3c9b-b786-3d46c6d6c421 | -13.08857 | -52.28901 | 2025-05-12 04:32:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 065a7229-cf9f-3d23-8e1e-fbec3d67819d | -13.60572 | -47.97313 | 2025-05-12 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 95817725-82f9-3a5c-ae9c-aaac987e6d63 | -10.48618 | -46.18214 | 2025-05-12 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc616b3c-e0a5-3438-9700-4471ebfa176d | -12.1742 | -54.2327 | 2025-05-12 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cf619f3-3340-337c-ae5a-42c0474dc655 | -12.16956 | -54.23549 | 2025-05-12 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 41e52289-bb76-3939-88a8-2222678b390a | -14.19865 | -45.46972 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 337c14e3-c9be-36e4-989a-8e1896b29363 | -11.38785 | -52.93969 | 2025-05-12 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83759c6f-f272-3552-ad5e-a3871ef40a66 | -13.60628 | -47.96945 | 2025-05-12 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| feb1713e-cb82-3e89-ad04-b93ff8dbdeb0 | -14.20109 | -45.47976 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35e58044-6998-3c35-bd22-1de6685d4852 | -14.19106 | -45.46861 | 2025-05-12 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5643daa-cd98-31a2-814b-7a41215a4d39 | -11.39537 | -52.94104 | 2025-05-12 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47264cd9-f284-3569-9a1a-b0a158457f1c | -11.89536 | -56.40751 | 2025-05-12 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b3473c2-6390-3784-a07c-6ff967c03368 | -13.05071 | -53.72411 | 2025-05-12 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 13ebd99f-bf1e-3efd-b343-b742de62ac45 | -20.17291 | -46.83741 | 2025-05-12 04:34:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 123a0dce-56b3-323f-b00c-fb6e876731c3 | -20.16958 | -46.83481 | 2025-05-12 04:34:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a086420-3953-3d94-9bb0-86d8cc490584 | -20.17353 | -46.83266 | 2025-05-12 04:34:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba6432b6-98cd-3313-87b5-47f615ad4a41 | -18.19444 | -45.60633 | 2025-05-12 04:34:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a415ff0-1b04-3ffe-8d97-2785bb9f5cc9 | -15.07783 | -48.94425 | 2025-05-12 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0531f18-3d65-3fbd-8fd2-79d71256505f | -20.17341 | -46.83509 | 2025-05-12 04:34:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4974b2d-7fb3-318c-b053-c37c045d86c3 | -18.61972 | -44.7527 | 2025-05-12 04:34:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47e50be3-aacf-33b7-a8a5-d4fa9c714ed1 | -20.6088 | -51.23579 | 2025-05-12 04:34:00 | NOAA-20 | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e57e4c14-c321-3f36-91d7-6381871cf82d | -19.96944 | -44.21747 | 2025-05-12 04:34:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4e86691f-e8fb-334f-a2b3-9dc2dd0b0e10 | -17.77887 | -42.80766 | 2025-05-12 04:34:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8926b4f1-1f26-3147-b698-fd11f7be7533 | -14.54986 | -49.10956 | 2025-05-12 04:34:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7b4a695c-1482-3e0e-9bd3-069278d7226b | -19.02166 | -57.62034 | 2025-05-12 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6b465743-c3c1-3d00-a457-291cc689c213 | -14.54931 | -49.11314 | 2025-05-12 04:34:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec78af27-fa19-3add-95fa-647c79d16353 | -18.13317 | -47.91808 | 2025-05-12 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4966590-c431-3f32-b716-2c1354da0747 | -15.56821 | -47.85587 | 2025-05-12 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df7a3af7-424e-3f6e-869a-8ed21c11c182 | -16.68192 | -43.88368 | 2025-05-12 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b925b74d-d563-3315-a9e9-d77f7ddc79f9 | -13.61917 | -54.87792 | 2025-05-12 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1a9f79a-7e5a-36e2-b13e-29bf46141fca | -23.33691 | -46.77213 | 2025-05-12 04:36:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a1ace7dc-be69-3d9f-b801-b12405482542 | -24.24338 | -50.73807 | 2025-05-12 04:36:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 333d7983-205e-3c91-a249-7c7d8b2367d3 | -22.09892 | -50.23328 | 2025-05-12 04:36:00 | NOAA-20 | POMPÉIA | SÃO PAULO | Brasil | 3540002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 67069cbd-47ec-3351-a8da-f66b9c03d68a | -23.21615 | -51.68805 | 2025-05-12 04:36:00 | NOAA-20 | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7894e5e3-7378-3648-9dd2-370630969921 | -26.93476 | -48.75296 | 2025-05-12 04:36:00 | NOAA-20 | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 63f7565e-53ea-3969-bb22-230deab6f9fc | -27.17086 | -49.00352 | 2025-05-12 04:36:00 | NOAA-20 | BOTUVERÁ | SANTA CATARINA | Brasil | 4202701 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1d289529-04d7-3189-b0ba-69ddfb54ae65 | -29.48664 | -51.97191 | 2025-05-12 04:38:00 | NOAA-20 | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c6902034-1a87-36a2-9160-1fb9ee4ccd88 | -30.15012 | -52.02289 | 2025-05-12 04:38:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 65930794-d333-3b32-b5e2-34adbb3b90a8 | -11.90241 | -56.40864 | 2025-05-12 05:23:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c6ba337-6d02-399d-9f26-12e0f57547f6 | -13.09089 | -52.29161 | 2025-05-12 05:23:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67cba0d8-7365-34bf-b1f3-b63d2ff39ce2 | -9.92527 | -59.90358 | 2025-05-12 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 33a6c34d-6039-30bc-91b4-ec7ce4311a5b | -11.38802 | -52.93851 | 2025-05-12 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85b0fadd-0772-3d3f-9936-e9485b033bed | -13.09133 | -52.28797 | 2025-05-12 05:23:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c228bcfd-afa5-3441-aee8-1d13b2b3a454 | -13.04935 | -53.71971 | 2025-05-12 05:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26d79748-4f68-3d97-a666-589bf77dc892 | -13.04861 | -53.72559 | 2025-05-12 05:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3036577c-96d6-3d4d-a927-7d23b0bba23e | -11.8978 | -56.41181 | 2025-05-12 05:23:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0c96001-e6a3-32de-b4b3-6666f663cde8 | -13.0436 | -53.72501 | 2025-05-12 05:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e54285d-07fc-3f08-ad45-e896660d7578 | -13.05399 | -53.72321 | 2025-05-12 05:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97750f48-2355-3e98-a7e0-23585f765eb6 | -10.74852 | -62.81853 | 2025-05-12 05:23:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57044ef9-d277-3999-bbc8-73825e36e0b8 | -13.04397 | -53.72208 | 2025-05-12 05:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac8fa47e-cc7b-3c83-9f37-a8941dc72471 | -12.17462 | -54.23236 | 2025-05-12 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09a3a5c6-9157-3384-bb61-40dbcf726be0 | -11.8937 | -56.41121 | 2025-05-12 05:23:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c7d729c-ac12-387b-8102-4851ce0c1bbb | -10.68523 | -57.59963 | 2025-05-12 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de02cb80-9824-37fc-8b80-d77e13db511c | -11.91685 | -54.40202 | 2025-05-12 05:23:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c284471-44ca-386b-8e80-f1d3406cd182 | -11.91907 | -54.40347 | 2025-05-12 05:23:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33c4d366-eb1e-375d-b611-070d2c40d11e | -13.05362 | -53.72615 | 2025-05-12 05:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cc04e97-2b19-3165-93fc-d2ac3dc432a3 | -11.39317 | -52.93919 | 2025-05-12 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 899410ee-8235-340f-bcc2-a3af49ada551 | -13.04898 | -53.72265 | 2025-05-12 05:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e474bc93-626d-3b7f-a68c-e6d2d734f085 | -12.17394 | -54.23771 | 2025-05-12 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ea732b1-fdb9-3c26-8b20-7809912de459 | -11.62426 | -54.9401 | 2025-05-12 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daa4cc09-ebe6-3efa-b313-bde8cac3b6fb | -11.40784 | -52.94745 | 2025-05-12 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee7f9a08-37ac-3773-9ff8-afc0696e4476 | -11.40745 | -52.95057 | 2025-05-12 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cc7675a-033d-3ec1-846b-6ecd6d71f0e0 | -9.56862 | -57.89693 | 2025-05-12 05:25:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88830ce9-4771-3f5f-9949-bf931e623b18 | -8.97832 | -35.54912 | 2025-05-12 12:00:00 | TERRA_M-T | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 47ee02bd-8f4d-3b8f-a1b3-6eb0bbaf27c7 | -7.40376 | -43.34547 | 2025-05-12 12:00:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 81748a98-69e9-324a-8fbf-b4b4747de0b6 | -5.61445 | -38.21992 | 2025-05-12 12:00:00 | TERRA_M-T | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| b3fad6e2-7245-37cd-a839-7d343428483e | -8.98849 | -35.5441 | 2025-05-12 12:00:00 | TERRA_M-T | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| fcbb3622-e4f6-3b08-b593-a137d50383b5 | -7.57464 | -37.2291 | 2025-05-12 12:00:00 | TERRA_M-T | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 6f2339d7-b957-3156-af30-6d443fa2be4f | -5.62345 | -38.22116 | 2025-05-12 12:00:00 | TERRA_M-T | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 17.3 |
| a594118d-734f-3983-8787-2bb8914a72c0 | -13.67975 | -45.41585 | 2025-05-12 12:02:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 4fb08a43-2e3c-37e2-8c25-e4e6e45d0c92 | -14.20274 | -45.47162 | 2025-05-12 12:02:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3cf5c291-c7b5-3ffc-84ed-d39624c4a299 | -13.69044 | -45.41761 | 2025-05-12 12:02:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 57cb694d-46eb-3189-a275-88beddcd1867 | -14.67156 | -45.12119 | 2025-05-12 12:02:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 25b17461-b93e-3b40-8712-c6c6997befed | -14.3069 | -41.76687 | 2025-05-12 12:02:00 | TERRA_M-T | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 4e890e29-b7eb-39b1-996b-a5cdce33f4e5 | -14.30824 | -41.75774 | 2025-05-12 12:02:00 | TERRA_M-T | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e58e7335-00f2-30bf-b731-d85c919e3593 | -16.29446 | -45.10675 | 2025-05-12 12:02:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 23c656b1-25d2-31e1-8888-089afa5b3cda | -17.55854 | -46.53918 | 2025-05-12 12:02:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 36.5 |
| b343845e-cab4-3f76-bce2-bb66085ca8b1 | -17.9034 | -44.40846 | 2025-05-12 12:02:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 45ee1fe4-8473-3f11-86af-560953fcfb2a | -16.29639 | -45.09481 | 2025-05-12 12:02:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 38d5ec64-b4fa-3766-b03b-7ae820bbb7d1 | -14.69486 | -42.50922 | 2025-05-12 12:02:00 | TERRA_M-T | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 9e3312d3-7b0b-3026-a659-def565713dda | -14.66956 | -45.13376 | 2025-05-12 12:02:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d2b239ef-04d6-3601-9205-9589aaa40744 | -16.30641 | -45.0965 | 2025-05-12 12:02:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eb6f4536-ddf8-330b-b8fb-2d897c9756b9 | -17.55615 | -46.55344 | 2025-05-12 12:02:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 46d3f4c1-119f-30f4-b406-b0d2393c9ac5 | -14.661 | -45.1227 | 2025-05-12 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 786b8b0b-c7d1-3478-95da-4eb3b008d029 | -14.661 | -45.1227 | 2025-05-12 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 832a8b1d-26c2-384a-80f9-fe53166fba80 | -14.661 | -45.1227 | 2025-05-12 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |


[Clique aqui para ver as próximas entradas](README4.md)
