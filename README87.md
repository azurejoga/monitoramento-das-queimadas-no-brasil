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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2c7f193-3b35-38d5-a006-992c8b7cc17c | -14.4838 | -52.1725 | 2026-08-29 15:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 848bc33e-7f09-3046-859e-0253793a7678 | -9.0057 | -65.456 | 2026-08-29 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8e8d3e46-0d6f-3802-a058-83d8a08f68d3 | -9.006 | -65.4 | 2026-08-29 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 2c140550-12d3-305c-8c37-7f1f89f9b5ff | -9.8617 | -65.0334 | 2026-08-29 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 112c58ac-9d2e-3659-9b22-87242f74c3d6 | -11.2128 | -53.9976 | 2026-08-29 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 2ca38c94-5efa-35c6-a85a-8123eff02236 | -20.941 | -57.5694 | 2026-08-29 15:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 67.4 |
| d8adbf11-a24e-325d-8a53-88d80f127a6d | -9.0059 | -65.4186 | 2026-08-29 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d228a319-5457-362d-ac3a-85808bb4cb1b | -11.7167 | -54.5244 | 2026-08-29 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 140.0 |
| b7b79a51-e0c3-315f-88d5-ef87553524ac | -9.971 | -53.9214 | 2026-08-29 15:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 200.3 |
| ebb0b8e6-6720-3dcb-bcda-dd9524512878 | -7.0034 | -59.643 | 2026-08-29 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 3924aaec-2591-3bf6-9ca7-e5582d9ff305 | -7.9838 | -45.5072 | 2026-08-29 15:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| b2dedad5-d76a-3565-93a3-997c80e2fc5a | -8.6694 | -49.5369 | 2026-08-29 15:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 2230e485-a94e-33b5-a6c7-904e1a3e0574 | -12.2093 | -50.5386 | 2026-08-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 8bd48848-7267-3ee0-b022-dbc4a8128da4 | -11.0054 | -49.6893 | 2026-08-29 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 30fc9422-9540-3e2b-8572-481c7eb050da | -12.3807 | -48.2099 | 2026-08-29 15:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 738e2280-b7d7-3fc7-be13-92009f56c1f6 | -10.7791 | -53.9752 | 2026-08-29 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 199.1 |
| 1f38d1d0-1422-3c65-b4b8-93e780b8d7dc | -8.574 | -66.9569 | 2026-08-29 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 22f2cd54-584f-3b50-95d3-a1fe7910a45a | -11.6975 | -54.5467 | 2026-08-29 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 35e79eb0-c2cf-3f93-a5f0-01874e14f274 | -7.0654 | -43.5978 | 2026-08-29 15:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9c31941c-429e-3091-b54f-65c697f39830 | -14.2989 | -51.7072 | 2026-08-29 15:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 76befe0c-1ee3-3d8e-86d4-23f3169a69b3 | -10.7598 | -54.0179 | 2026-08-29 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 314c478f-b899-385e-a664-e05529551ec4 | -8.631 | -66.5473 | 2026-08-29 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 09a7ae25-02d8-3d38-ad6d-aa3cbdab56c7 | -13.1648 | -55.6498 | 2026-08-29 15:50:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 37.8 |
| e4130b89-7d09-3e17-beac-b1ca1172783a | -3.9364 | -59.319 | 2026-08-29 15:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 49d7db4f-8903-39d6-b6df-6733133ac37e | -11.2506 | -53.9941 | 2026-08-29 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 3ccdded5-a97e-3152-a527-55d2a573a5f8 | -11.0443 | -57.2222 | 2026-08-29 15:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| c40fe77b-527a-3dba-9e89-13f84c69b359 | -9.0058 | -65.4373 | 2026-08-29 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| f963a121-15b6-3eb4-a33a-902d8c85ce20 | 0.1549 | -60.393 | 2026-08-29 15:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 25db524e-4d65-3eda-bab8-f241755c23be | -7.3849 | -55.1723 | 2026-08-29 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 472eba8a-a9e1-32d9-9340-6d1f7fe88d63 | -11.7165 | -54.5449 | 2026-08-29 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 3f81050c-3ffe-32f0-a3f3-d9315b698813 | -10.9859 | -51.0807 | 2026-08-29 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| bcb1d83e-25ee-3a93-8375-d3dbe3d90a04 | -11.9081 | -55.8891 | 2026-08-29 15:50:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| ca864699-3da4-3454-ae18-62e2951152b0 | -11.1807 | -55.1024 | 2026-08-29 15:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e6442eed-5a84-326d-85fe-7003146a9373 | -10.8215 | -50.6519 | 2026-08-29 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 6b9a6add-ff20-33f2-b6c4-c1173e655134 | -10.8804 | -50.4965 | 2026-08-29 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 1b6c49a5-febc-3135-b4ce-f2b701818d9e | -8.9873 | -65.4379 | 2026-08-29 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 842f5208-8d58-3097-894d-62197139fd4a | -3.2178 | -61.2362 | 2026-08-29 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 24332022-8892-3ae8-9c73-c92eeef51ec6 | -6.6317 | -43.73 | 2026-08-29 15:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 1115f2c3-e945-3c72-923d-13f58978ef6d | -9.0615 | -65.4169 | 2026-08-29 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| b87c4862-2fa1-38a0-a842-be331f5143c2 | 1.785 | -55.8226 | 2026-08-29 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 4186d562-d4b4-3cbf-b096-397e50e3d0c7 | -11.6212 | -54.5947 | 2026-08-29 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 76ba7178-f689-3c84-af38-2616c3bf9bfc | -9.9708 | -53.9419 | 2026-08-29 15:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 189.0 |
| 383ac066-59e6-3fd3-b85a-f281b8ab40e2 | -11.1998 | -55.0805 | 2026-08-29 15:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 71f3cf69-aeb6-3c40-b42e-5d6f1afceef4 | -11.2317 | -53.9958 | 2026-08-29 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 200.1 |
| a2bec24f-afc4-3825-9ca7-0dd17efe33cf | -6.9872 | -59.2582 | 2026-08-29 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 7c277776-4cfb-3363-98c2-6fcec2cc8d8e | -8.9428 | -63.2797 | 2026-08-29 15:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 153.2 |
| ce582d0c-43b7-3dbf-8d16-b17a21c60d63 | -6.6929 | -59.0966 | 2026-08-29 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 411468d8-2174-3df8-aeac-4ad985aa510f | -9.6022 | -55.128 | 2026-08-29 16:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 272.6 |
| bd400595-a16a-39de-b4f4-19d1318a520e | -9.006 | -65.4 | 2026-08-29 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 3ba24b4c-9e89-3e7f-9c49-1c1503ff3df2 | -11.7167 | -54.5244 | 2026-08-29 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 223.5 |
| 86e343b5-6d11-3b25-9363-09b03789187d | -9.2465 | -65.5043 | 2026-08-29 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 9761b61b-0c62-36a1-9d39-7a58abfe4325 | -6.018 | -57.8242 | 2026-08-29 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 99a896a6-0f25-35cd-b345-3e7c5399e62f | -9.0057 | -65.456 | 2026-08-29 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 12dc3370-7764-365c-b75e-6978b8507adb | -9.8617 | -65.0334 | 2026-08-29 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7a245252-19d5-307c-84ee-a851c0cd9704 | -6.6317 | -43.73 | 2026-08-29 16:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 788db2c7-131f-3d01-9a3d-8ddc92ffeca9 | -9.1711 | -49.9835 | 2026-08-29 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 479ecb71-692a-3abb-89da-d8c4c3a8ef8c | -14.2989 | -51.7072 | 2026-08-29 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 178426a0-8181-36e5-8f0e-b725fce339cd | -11.2106 | -51.2688 | 2026-08-29 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 1a251a89-1619-37fe-a11b-52cf819b49cd | -6.7652 | -63.054 | 2026-08-29 16:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 93abbb9a-f630-3d89-8cd5-05ef01467767 | -14.4251 | -53.3829 | 2026-08-29 16:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 9ce80cd1-7328-3f9f-98f0-f5b9075e31b6 | 1.785 | -55.8226 | 2026-08-29 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 18ef6886-9c2f-3d1e-984c-670b20af4d7a | -11.1939 | -53.9993 | 2026-08-29 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| d8bc5e8e-e5b7-35ca-9e05-1ab2fed68184 | -3.2178 | -61.2362 | 2026-08-29 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 88964874-7178-3b5b-b8e1-5409e2eb3a9c | -11.245 | -45.3037 | 2026-08-29 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 78415cd1-8498-3710-a979-40cac8fa5b22 | -7.0057 | -59.2575 | 2026-08-29 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 283ff257-408a-316d-8f5e-bd27435329a4 | -10.8801 | -50.5179 | 2026-08-29 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 160f647f-2718-3ecc-92ef-34afb9daeeae | -9.0983 | -65.4717 | 2026-08-29 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c3147c35-7964-3539-958a-1414ae1ef946 | -9.02 | -57.5377 | 2026-08-29 16:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 4d29d03d-601a-3607-a2e2-321dfd37cdde | -3.9364 | -59.319 | 2026-08-29 16:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| cd2e596c-db3a-38e5-bc72-abdb8bacec27 | -9.0061 | -65.3813 | 2026-08-29 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 32e3d7b8-2a52-3de3-a9e4-6e4d11a67247 | -12.2093 | -50.5386 | 2026-08-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 4fea83f2-84f3-353b-a80f-5986e246f9b2 | -8.9873 | -65.4379 | 2026-08-29 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0df3f027-af84-3482-a09f-9c7991b4c911 | -8.9478 | -62.4084 | 2026-08-29 16:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5bda2704-7999-38f2-9f43-0f173e43bf26 | -8.9872 | -65.4566 | 2026-08-29 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| bcab9ed8-43da-3fa3-ab37-937c1d320cac | -8.574 | -66.9569 | 2026-08-29 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 145bbebb-6186-3669-aaae-37bc854b0a2d | -10.8653 | -50.2203 | 2026-08-29 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| adcfce7e-26b4-3573-87b1-d91c92cd1137 | -12.2281 | -50.5578 | 2026-08-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 43e21957-c1b7-38a7-abda-577d762a2109 | -8.6506 | -49.5386 | 2026-08-29 16:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a3d4f4b8-816e-3d36-82f3-5a967e9c208d | -8.6694 | -49.5369 | 2026-08-29 16:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 0a2e8b38-505c-3ddc-aae1-e7cafa40f56b | -11.1998 | -55.0805 | 2026-08-29 16:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 9ac81f1a-983b-3dd0-95cc-692414561349 | -9.9288 | -60.4277 | 2026-08-29 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| ab635cfe-8194-3c4d-9307-aab1aa4f19e7 | -9.0982 | -65.4904 | 2026-08-29 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 50f856b9-4d9a-3c80-a01e-94957d7e0a06 | -10.0294 | -46.4139 | 2026-08-29 16:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1c25ebe2-5ca0-337f-85da-4439a2a2158f | -10.8804 | -50.4965 | 2026-08-29 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 0d879740-4932-3725-8e61-8c6be8610674 | -8.8184 | -49.6308 | 2026-08-29 16:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 10947a32-dd9f-3e40-aa39-a576d89bf47a | -6.5053 | -45.095 | 2026-08-29 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| e02b332d-b1f0-34a2-a2cd-e69a2dd689f4 | -10.8232 | -50.5239 | 2026-08-29 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| ffdacdd5-7ccb-32b8-a55d-b0e287b7b577 | -3.9363 | -59.3381 | 2026-08-29 16:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c48b5ca2-bf17-305a-b751-db665ab43f3a | -6.7885 | -55.6436 | 2026-08-29 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 0be0dd71-75ba-3d72-85a6-869e7f387c4f | -10.899 | -50.5159 | 2026-08-29 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 292128fc-912a-39c4-a485-3dfc2074297a | -13.3045 | -51.3877 | 2026-08-29 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 31483100-4ed6-374b-9225-b02dc0e23358 | -13.8563 | -54.0967 | 2026-08-29 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 995b9681-e1ac-3bb9-ab95-2838f1b4923b | -14.419 | -52.5837 | 2026-08-29 16:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 3598f33e-0e83-3c21-a972-382bf61c6679 | -1.2541 | -55.7101 | 2026-08-29 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 757c3c69-9636-3acb-aa79-0f53c3d336a2 | -8.9428 | -63.2797 | 2026-08-29 16:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 143.1 |
| c096ea50-a9fa-3598-a75e-e9bbc99115f6 | -11.1916 | -51.2708 | 2026-08-29 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 7bf46644-84da-35ba-8b20-00e856515e14 | -7.0034 | -59.643 | 2026-08-29 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 51371708-6620-3490-8eb7-0a23c91c1c85 | -6.1795 | -45.9097 | 2026-08-29 16:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 59e120ce-faae-3149-a837-5fb7b0ed4e20 | -10.7407 | -54.0401 | 2026-08-29 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 389fc598-ceac-33c5-b2de-c490103f292d | -3.6216 | -60.547 | 2026-08-29 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 127.8 |


[Clique aqui para ver as próximas entradas](README88.md)
