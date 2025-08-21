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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62d6ed74-a245-316b-88da-5fb4a4115d66 | -18.3038 | -45.5257 | 2025-08-21 12:50:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 9ca2d575-f73a-3329-8fe0-b02d673b34a2 | -7.0164 | -44.6413 | 2025-08-21 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 765b75f0-0ef5-39df-836c-05ef0b89a7ad | -7.0166 | -44.6184 | 2025-08-21 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 50d58798-5504-3054-993c-d2698b630894 | -7.6296 | -45.2464 | 2025-08-21 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 619c9ff3-acb4-3e2e-83fa-799abfa705dd | -14.8543 | -47.9279 | 2025-08-21 12:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e46757aa-6595-346c-a798-b414b76b9039 | -12.9533 | -46.2419 | 2025-08-21 12:50:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| fca05e6d-f273-3169-831f-49604341d798 | -4.58699 | -47.71424 | 2025-08-21 12:51:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 308b6ce2-233a-3501-a469-81a4fb144fe4 | -4.7862 | -45.32322 | 2025-08-21 12:51:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| cb98af41-91e6-337d-a934-30334cce6b61 | -3.41947 | -48.88298 | 2025-08-21 12:51:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| f8e9165c-5e52-3717-baf5-3a1c48375165 | -0.75179 | -47.74461 | 2025-08-21 12:51:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| ffb645f0-186e-30f7-bd62-f0cd4003ddbc | -2.46777 | -47.74403 | 2025-08-21 12:51:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| ddf589c9-6fd1-3632-96e6-c8c177105609 | -3.47259 | -48.98363 | 2025-08-21 12:51:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 20141567-b6bc-3911-91cd-68a258ba8897 | -2.46482 | -47.76474 | 2025-08-21 12:51:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 4cc0c052-e4b2-3670-9f86-138d70fbd426 | -1.85362 | -54.97227 | 2025-08-21 12:51:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cf3008a5-efb1-3ea8-9319-d3376e6d1100 | -3.04264 | -49.42866 | 2025-08-21 12:51:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| dcf7df1c-1ae8-3ef5-a7c0-6f7c7282d33d | -3.4606 | -48.98209 | 2025-08-21 12:51:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| cb6b3316-6bb1-3668-8d97-473fa4a355c3 | -4.57597 | -47.73089 | 2025-08-21 12:51:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 3f33716a-f328-355e-a85a-3d31c94adef4 | -5.89956 | -45.0801 | 2025-08-21 12:51:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1faef7e7-1369-3462-92a9-bd6a704f9aba | -3.80661 | -47.60272 | 2025-08-21 12:51:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| f536fa1b-08e2-3827-a35e-8bbffca52e33 | -4.77991 | -45.31576 | 2025-08-21 12:51:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 19255e04-b25d-3ab5-938f-00213230cb35 | -2.46534 | -47.75045 | 2025-08-21 12:51:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 935e8a07-3d37-3438-977d-4aa115f0ffb3 | -2.47612 | -47.19591 | 2025-08-21 12:51:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| ea1fd74d-dcac-3747-9151-ec914d83719e | -9.18757 | -59.63974 | 2025-08-21 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a0c03673-c585-3dd5-bf2c-37e07159055c | -9.56649 | -48.1158 | 2025-08-21 12:53:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 961f91e2-6f59-35b6-b015-acf779eb8db9 | -6.53534 | -45.47058 | 2025-08-21 12:53:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| fa8a5877-6026-36c5-9019-4a75bb3b3ec5 | -8.76742 | -46.69334 | 2025-08-21 12:53:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 86d06e1c-cc6a-3c70-9ea7-7b18188a476d | -7.63455 | -45.24816 | 2025-08-21 12:53:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 2a8f338d-d1bb-3328-ad44-714936167995 | -8.86801 | -62.40257 | 2025-08-21 12:53:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8be6a760-214a-336f-a964-658d772b66c4 | -8.87844 | -62.41046 | 2025-08-21 12:53:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| e22e38f6-7be3-309a-a9a9-dddb87dd5650 | -6.5284 | -55.37718 | 2025-08-21 12:53:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1964589e-568c-3f64-aea3-034aff19b88b | -10.93088 | -56.83053 | 2025-08-21 12:53:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| eda76eb9-5709-3d94-8e16-e0579b73c42f | -10.51737 | -50.35693 | 2025-08-21 12:53:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 3942f88c-9151-3f83-acf1-438397aef7bb | -9.70865 | -46.05994 | 2025-08-21 12:53:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| fadd0c6c-cd82-3f7b-8992-443b61bbd768 | -10.52941 | -50.35843 | 2025-08-21 12:53:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| b97532de-9409-3ad7-a3c3-754569159839 | -8.4873 | -48.23388 | 2025-08-21 12:53:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 9df5878e-8d97-3ec7-918e-3d12913f9fa8 | -6.43116 | -45.49261 | 2025-08-21 12:53:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 7400d45b-9be3-3a43-a1b2-b2c40aec2e42 | -9.05788 | -49.29922 | 2025-08-21 12:53:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 3825b5b2-4946-3b40-9776-c7012500df62 | -5.88587 | -57.75135 | 2025-08-21 12:53:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9f66b2b8-c504-3113-b086-68be9048136a | -8.8498 | -52.04399 | 2025-08-21 12:53:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ab49994c-9ef6-398c-81ae-8a4cafe3108c | -9.71311 | -61.29343 | 2025-08-21 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 92b64354-237c-3e43-ad54-f11f9e083393 | -9.18952 | -59.62714 | 2025-08-21 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 9336cac7-ac0e-3c73-98c5-ec1944af0b93 | -9.22677 | -60.34074 | 2025-08-21 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 78e5e463-bd6f-3c07-b876-ea7e6a63777e | -9.71385 | -46.06577 | 2025-08-21 12:53:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 4f222fd0-978b-3017-9194-49dcecb70d32 | -10.51957 | -50.33954 | 2025-08-21 12:53:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 05b9e778-94c7-3579-98d7-8012702f8f80 | -6.44539 | -53.37496 | 2025-08-21 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 042f593d-63c9-33f7-ab3f-56f7afc9d8d2 | -6.26656 | -52.81857 | 2025-08-21 12:53:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1f8038d7-ae7d-3819-8070-4371fe281158 | -9.56308 | -48.10824 | 2025-08-21 12:53:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 4bb4d41c-5def-3e0a-b2e4-1587140bb013 | -11.8166 | -50.64567 | 2025-08-21 12:53:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 65e9c0f5-6d1f-3f43-836f-6747ba611067 | -9.70439 | -46.09557 | 2025-08-21 12:53:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| d411b73f-f326-3451-bef5-537b292cf8bd | -11.81449 | -50.66299 | 2025-08-21 12:53:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 65a2c0d0-d02f-3ceb-a4f3-208f20941d1f | -11.5189 | -50.53708 | 2025-08-21 12:53:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 057373e1-0a72-36cf-9b29-744732c39316 | -9.23021 | -60.33284 | 2025-08-21 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| ae9f3ec5-f4b2-3f01-9fbb-ef8d380e27cc | -8.48434 | -48.25762 | 2025-08-21 12:53:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 8a679c79-7e17-366f-ab91-604dbeecf152 | -10.28326 | -46.77626 | 2025-08-21 12:53:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 9632588f-cd5a-3518-b77b-c90c21993a2a | -8.5012 | -48.23526 | 2025-08-21 12:53:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 524cb7d5-fd4e-3c06-a2c2-96a2e9c882e4 | -10.92781 | -57.54295 | 2025-08-21 12:53:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4777e8a4-9233-36a4-8a21-bbe03f1eb4ec | -8.67368 | -48.82375 | 2025-08-21 12:53:00 | TERRA_M-T | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 0d4da86b-716d-3d96-bb91-f32b6c682171 | -7.04927 | -59.82392 | 2025-08-21 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a12519d3-cd83-300b-b164-886d78f7f6be | -9.55982 | -48.13403 | 2025-08-21 12:53:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 6293b611-d640-3bc4-825f-0990eae0365f | -11.59899 | -50.38475 | 2025-08-21 12:53:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3df88d06-72ce-3a6c-a9ba-7f70fe542052 | -8.49817 | -48.25927 | 2025-08-21 12:53:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| b901580b-26e3-36e6-9085-74cbefd52590 | -6.52967 | -55.36836 | 2025-08-21 12:53:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8285e212-8b2a-3e11-8c0e-a0c7d7a9289f | -6.81566 | -51.37941 | 2025-08-21 12:53:00 | TERRA_M-T | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7d13dbbf-cb51-3d7b-a265-de9dfea3a3e2 | -5.90287 | -45.08728 | 2025-08-21 12:53:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| dcb93224-b109-3c00-91aa-e37b1b318847 | -7.06022 | -59.82571 | 2025-08-21 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c2df127b-2e90-38c0-94e7-14f94d1a3b4d | -6.45459 | -53.37622 | 2025-08-21 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1c8e496a-b8be-32a7-9dd7-d2dc4461d742 | -11.60122 | -50.3667 | 2025-08-21 12:53:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1a862aa6-5194-3859-a627-163debc4950f | -9.69724 | -46.06298 | 2025-08-21 12:53:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| cbd10ad4-a265-344b-af6f-7ddeec63e3a4 | -6.54067 | -45.47765 | 2025-08-21 12:53:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 299f8810-2a73-37e2-a336-9c6a0fdbe4c9 | -11.63166 | -51.58498 | 2025-08-21 12:53:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0fd8c351-bc61-3936-a7d7-b462a40f6435 | -11.64277 | -51.58639 | 2025-08-21 12:53:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 2afc0858-8ab8-3018-86d5-652e75cea06b | -14.36415 | -51.97808 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 81729f7b-c218-3ed1-862e-0ad1652133a9 | -13.48565 | -47.05769 | 2025-08-21 12:55:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| af01531c-5b61-3611-9764-9c78d33bba23 | -14.75384 | -56.01841 | 2025-08-21 12:55:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 59b20c60-685a-383e-ac9f-eadad99fdd13 | -14.83949 | -47.92006 | 2025-08-21 12:55:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| e63fdc75-f5d8-32d2-96ae-147a27de7568 | -14.57389 | -51.94542 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bf7b1638-7f36-39a1-b9d2-9d297ba82be1 | -14.63784 | -54.86359 | 2025-08-21 12:55:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 48013d8e-4678-3d3f-974d-a5a24f7bcc64 | -13.05069 | -46.8107 | 2025-08-21 12:55:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 29862054-c569-391e-93a3-2b5cac02231f | -14.36608 | -51.9628 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| c125ef4e-a89e-3b67-bc65-b6c98d0a5ad9 | -13.39402 | -46.23629 | 2025-08-21 12:55:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 5bc0daee-e7b0-3ca1-8bae-742d8c34edeb | -15.01498 | -54.84317 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 7120409c-5a8d-37f8-9644-6cc29bee8d61 | -14.75253 | -56.02769 | 2025-08-21 12:55:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d96cf25e-5e6a-3eb1-bd68-bde13061df34 | -11.81144 | -55.52139 | 2025-08-21 12:55:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 87351e32-8a85-3c7b-b8d1-10fb6701df95 | -13.14781 | -54.92041 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| b9f26734-78b0-3914-bd58-a2e5ada50c24 | -13.33238 | -54.4307 | 2025-08-21 12:55:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 74595364-9e3c-3275-b8a0-b51181315ab8 | -14.3653 | -51.96913 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| f3a47d11-b9ab-312d-b484-0c9e70eb77a1 | -13.49249 | -47.06503 | 2025-08-21 12:55:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 162042e6-fcfc-3913-a336-1ba915d46922 | -12.88863 | -46.0668 | 2025-08-21 12:55:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| a5f66479-70e8-3492-be9d-71fe9ecf0266 | -15.55453 | -50.56067 | 2025-08-21 12:55:00 | TERRA_M-T | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9d3e2ee3-73b6-3c8b-8526-e6e56f3ebd49 | -14.32485 | -52.01905 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 37.4 |
| b1b19389-c43d-3d61-93e3-aa7c81f7364f | -14.31366 | -52.01752 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 68d3ebea-50ad-32ae-b712-9650b2086b3a | -14.74992 | -56.04627 | 2025-08-21 12:55:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ad187944-099a-311d-8316-094548f24f4d | -14.75123 | -56.03698 | 2025-08-21 12:55:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1c73e530-c133-3873-9986-825c52eab7f9 | -15.01365 | -54.85323 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3565e72c-cad4-37c4-bf98-3b97875d5ec6 | -15.00822 | -54.84655 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 2677a81f-5898-35bc-8c93-2504295872c3 | -12.37774 | -49.98996 | 2025-08-21 12:55:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 4079494b-66df-3e83-8bae-0e705bc828c2 | -14.84781 | -54.93137 | 2025-08-21 12:55:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bf259342-7ed8-39c2-8075-d5254aab8107 | -12.45966 | -47.32611 | 2025-08-21 12:55:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| b463a4f2-3a2e-3c22-aa55-25a28e1e2054 | -12.94197 | -46.24511 | 2025-08-21 12:55:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 01c286a3-af78-3b30-94df-e469d640a048 | -15.55415 | -50.56625 | 2025-08-21 12:55:00 | TERRA_M-T | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |


[Clique aqui para ver as próximas entradas](README62.md)
