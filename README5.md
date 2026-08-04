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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c1a8ba4-33fe-3cc3-902f-a367753f0dba | -6.167 | -47.3078 | 2026-08-04 02:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| bf07c7a6-3a60-3c8d-a83d-196b23f6f839 | -8.3544 | -45.9897 | 2026-08-04 02:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 20411980-be1a-3dad-8f73-a2c0ea91e7de | -6.1855 | -47.3284 | 2026-08-04 02:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 1784809b-07ee-359c-89c8-6300cd1fd1f0 | -6.1668 | -47.3297 | 2026-08-04 02:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| fa8f22bf-409b-31e0-a3ff-bd7b77656a7b | -3.6639 | -49.4686 | 2026-08-04 02:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6e8c4fea-3afc-3aef-8089-2b2773ae1714 | -6.1857 | -47.3065 | 2026-08-04 02:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| d7d4eb1c-61d5-35d2-aaee-19d7342f667e | -6.5514 | -55.1569 | 2026-08-04 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 41161c80-4544-3668-9021-762cedc016c7 | -8.3546 | -45.9671 | 2026-08-04 02:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| a2e58609-ddc2-3c4e-8a07-56bc317c8b9a | -10.5741 | -46.7745 | 2026-08-04 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| b110622e-90b4-3173-b8d3-5f88db86cffb | -3.6639 | -49.4686 | 2026-08-04 02:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| a52d60a4-b4e7-320e-b714-b10d5cdc221b | -11.2213 | -54.855 | 2026-08-04 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| f0da2ff9-9ffd-3f30-89c0-d605438d930a | -6.5697 | -55.176 | 2026-08-04 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 95d3c366-94c6-34c6-b558-9845f8592da8 | -8.3544 | -45.9897 | 2026-08-04 02:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 8a2764d1-77de-393a-aef9-d4e5c8bd6103 | -6.5699 | -55.156 | 2026-08-04 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e0166c2b-2579-3808-987b-4ffb3fcfb858 | -6.5514 | -55.1569 | 2026-08-04 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3e3155b2-f45e-3a06-9bbe-c9ea0b1a6420 | -8.3546 | -45.9671 | 2026-08-04 02:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 65f4fa39-f2ff-3657-a1eb-5877101d6ba9 | -6.5697 | -55.176 | 2026-08-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 29020107-e8e3-33fa-a996-f8c5717868ac | -8.3544 | -45.9897 | 2026-08-04 02:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| de34b5e0-47d0-39b4-b8a2-64640013f2cb | -6.5699 | -55.156 | 2026-08-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| fb6663a0-218c-31eb-9128-3f22d62747bc | -3.6639 | -49.4686 | 2026-08-04 02:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 55e86f09-d8a0-3a81-92d6-bb4634c8f713 | -11.2213 | -54.855 | 2026-08-04 02:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 3dd1e3cf-5cec-3a52-ad19-2553ff3c0fe6 | -8.3546 | -45.9671 | 2026-08-04 02:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 7d78eaf0-3815-3470-b41a-209b1430964b | -6.5514 | -55.1569 | 2026-08-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| dbbc77d6-e646-38dc-bb01-02dfc50aa133 | -11.2213 | -54.855 | 2026-08-04 02:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 7ed07dcb-6346-390e-989d-b2aac4fd3d88 | -8.3544 | -45.9897 | 2026-08-04 02:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 8b041279-4ebe-3d39-aba8-4bc0e27272a8 | -6.5699 | -55.156 | 2026-08-04 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 1401f332-8cea-37bd-b079-67223b1a00b2 | -6.5514 | -55.1569 | 2026-08-04 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f00637f6-ec7f-31b7-bf43-b4259c4216f0 | -11.2213 | -54.855 | 2026-08-04 02:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6d9b48e3-3a20-3935-ac21-2d86225474e5 | -8.3546 | -45.9671 | 2026-08-04 02:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 5d75a036-a609-3e07-8972-b6a30dc8e788 | -6.5514 | -55.1569 | 2026-08-04 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| ca84e75f-fd28-375c-a9a2-e77d66d0dcb8 | -8.3544 | -45.9897 | 2026-08-04 02:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| cb9ccff2-65f5-3aee-9879-a1bf9a0108b5 | -6.5699 | -55.156 | 2026-08-04 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 323e1667-1a8c-3494-83ff-bb673ad8cce3 | -6.5514 | -55.1569 | 2026-08-04 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| bdcd6db9-a3de-3157-a84d-f2708af72892 | -8.3544 | -45.9897 | 2026-08-04 03:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 7996d161-d555-386e-80ba-ead073bbb422 | -11.2213 | -54.855 | 2026-08-04 03:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 8c25df32-128a-3c63-b686-bb1b3e577ad6 | -8.3546 | -45.9671 | 2026-08-04 03:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| b6996fc2-8e77-320b-ae35-9793930fe821 | -11.2213 | -54.855 | 2026-08-04 03:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 3e661beb-2b03-34c8-8c99-09b6c9fa15e6 | -8.3546 | -45.9671 | 2026-08-04 03:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 1d26d520-eb66-31ba-821f-cfd6e7007142 | -8.3544 | -45.9897 | 2026-08-04 03:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ee8339fd-df6d-3c2d-a23c-8e388314e017 | -8.3544 | -45.9897 | 2026-08-04 03:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 0736a005-dd6f-3433-b746-413bf42765de | -8.3546 | -45.9671 | 2026-08-04 03:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 0b879212-70df-38e0-ae4f-7610c33a7f87 | -11.2213 | -54.855 | 2026-08-04 03:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 00140d4f-98ae-3eec-b2a9-d53520eb7571 | -4.31337 | -38.49106 | 2026-08-04 03:21:00 | NOAA-21 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 42075b74-63fa-388e-bc25-b74832be229a | -4.31848 | -38.49183 | 2026-08-04 03:21:00 | NOAA-21 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f55649cf-590b-33e7-8e8f-3c37ce0802a8 | -3.96484 | -40.05487 | 2026-08-04 03:21:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 91015145-a5fb-3bf3-8e2d-0611ae7bce97 | -3.9655 | -40.05095 | 2026-08-04 03:21:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b9b1669-19da-3a17-b598-8c3d81432162 | -4.63528 | -43.13173 | 2026-08-04 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9bb42483-6473-3cb2-b4ef-9fd012e5348a | -4.63636 | -43.12555 | 2026-08-04 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 68060362-f0d3-3738-b98d-ac028e961906 | -5.42315 | -43.4267 | 2026-08-04 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 900af122-14e1-386f-b157-32bf3c373071 | -4.90925 | -43.47259 | 2026-08-04 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d58cafa5-05e7-3e5c-a27d-a9d0f8977b76 | -6.49586 | -42.23476 | 2026-08-04 03:23:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 10ed3ec6-8b07-331e-9dc3-3bbdc4ccff07 | -4.64209 | -43.13289 | 2026-08-04 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be3ad872-7549-37e3-add7-b8d426db934f | -4.63757 | -43.12682 | 2026-08-04 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 83408298-d599-331b-90e5-3fd5cb08abe2 | -4.64326 | -43.13413 | 2026-08-04 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 80c52a9c-51f3-3d39-964a-5c1ad26393d6 | -8.79037 | -38.49559 | 2026-08-04 03:23:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 34fcefab-20b2-35a1-b2ee-0cb83094bedb | -6.48026 | -42.22874 | 2026-08-04 03:23:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 6b90f7f6-f973-3f19-8bb7-3b3fd2f0a4c0 | -4.63645 | -43.13299 | 2026-08-04 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7a443715-5d30-3df6-96fa-21e4020b06ec | -6.29584 | -43.82664 | 2026-08-04 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 120697d6-120a-3b43-98fe-438840c4bf5e | -7.1443 | -37.78125 | 2026-08-04 03:23:00 | NOAA-21 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30cf182f-ce81-3270-81ac-ad13acc122ff | -8.7886 | -38.49839 | 2026-08-04 03:23:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ba6db7ce-18c5-3d7d-a81c-b161fda16b01 | -5.422 | -43.43291 | 2026-08-04 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6be2c8bd-830a-3c1c-ad57-4c9024c2a677 | -6.47397 | -42.22775 | 2026-08-04 03:23:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7fad8070-d840-335c-b2da-d1bb09aeded1 | -6.29701 | -43.82051 | 2026-08-04 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75e28405-d767-3a52-8522-d1e3e4e0d1e4 | -4.64317 | -43.12672 | 2026-08-04 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ba4dc49-e5ed-3f12-8282-36c938311bb9 | -6.48114 | -42.22388 | 2026-08-04 03:23:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 39220ad1-6a3f-3bfb-9af7-422d02044cfc | -4.64437 | -43.12798 | 2026-08-04 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 95b11f5f-9e0f-3dd1-87f0-1b3a0f04d44e | -17.87052 | -40.05211 | 2026-08-04 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 48494cb2-2be6-3617-84d3-4457075bc4eb | -10.75726 | -42.09623 | 2026-08-04 03:25:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 898f2278-0b13-3551-8110-5b2d3a330723 | -11.83331 | -38.26011 | 2026-08-04 03:25:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7cf4996e-f251-3d87-9302-1eca4c5ccd55 | -17.86606 | -40.05119 | 2026-08-04 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3a7eb44a-4252-3e1e-83b0-c2079a2323af | -14.25943 | -45.2611 | 2026-08-04 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 515d5cda-26fe-313d-9608-e51f9715e1bc | -14.26475 | -45.2683 | 2026-08-04 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14c22407-849f-345c-9afe-39be8f0c4c7b | -17.86515 | -40.05581 | 2026-08-04 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8c246178-e6fc-3df0-8e26-062dbd000c6a | -17.86312 | -40.05272 | 2026-08-04 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4187a4e8-fce6-3fb8-9e67-e3195e6a83b7 | -14.25821 | -45.26675 | 2026-08-04 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d741ac4-c312-30c1-ad5a-f5a4388473ed | -15.04524 | -41.99184 | 2026-08-04 03:25:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 66966172-ba0e-3f4e-884d-b5a51cba28b5 | -14.26596 | -45.26266 | 2026-08-04 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fdac526-5482-3243-ad6b-69ecf51cda7d | -11.83252 | -38.26448 | 2026-08-04 03:25:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 184f47d9-f2af-3df5-9d8a-71b1e8481f61 | -15.04456 | -41.99524 | 2026-08-04 03:25:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 59ec15ee-c429-358b-af71-c1f9e9d3d9e4 | -17.96679 | -47.14367 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32de334b-9595-38c1-b40b-f0607e31f4f0 | -17.98155 | -47.17404 | 2026-08-04 03:28:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cbfb5816-0212-3097-a871-d57efef27738 | -17.98304 | -47.16775 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 15f499db-1ddf-3369-9289-ce5e0a4c933f | -18.57941 | -39.91812 | 2026-08-04 03:28:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d35461d4-bd64-3585-b3b5-c98ac9bcf402 | -17.95737 | -47.15468 | 2026-08-04 03:28:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d60ad8ff-aa08-3ffb-9592-7345d626ad17 | -17.9775 | -47.15942 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c3985293-21c1-368b-b101-2ea4492e42f3 | -21.03442 | -45.51405 | 2026-08-04 03:28:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 901121b7-6085-3bbc-a3ad-44d9db7f8c56 | -17.9776 | -47.1604 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0edd6507-dc2b-3866-a375-6cf829161ce9 | -17.95994 | -47.14222 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c926609a-68cc-371e-a7fc-5ad000e817b9 | -17.98298 | -47.16683 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d7d24bee-2a10-3ee3-9082-540850bda7ff | -17.95879 | -47.14872 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5cbde674-6fe0-33e7-bc15-45e2490f368c | -17.95728 | -47.15363 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a33a4ac2-9087-3f77-8984-13491145909d | -20.98886 | -42.83599 | 2026-08-04 03:28:00 | NOAA-21 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d2febcfd-800c-33f8-ae7e-e96975753165 | -17.98155 | -47.17298 | 2026-08-04 03:28:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 80452a13-7da6-3790-b325-43783c9fe721 | -17.9899 | -47.16797 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5290ccb7-1fc5-32c9-99d8-c25a18935230 | -22.17802 | -42.11289 | 2026-08-04 03:28:00 | NOAA-21 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dfdecebf-dd53-3fd2-9e5f-63b79abf5398 | -17.98997 | -47.16888 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b51c88fd-728e-3bb8-ae20-46e6648541ff | -21.25913 | -41.7956 | 2026-08-04 03:28:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4f747d9f-d31d-3cf1-b58a-7e54bd44a9a2 | -20.31536 | -42.00603 | 2026-08-04 03:28:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 82c9f705-9ec7-322c-bda7-00a83bc1c9a0 | -17.9844 | -47.16205 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8be8de1c-7223-37d5-8152-f42f5ba9e36b | -17.95866 | -47.14771 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README6.md)
