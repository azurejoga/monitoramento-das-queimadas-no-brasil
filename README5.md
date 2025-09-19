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
| 6811dbf2-4542-3340-bd2d-c8c7e1926fd5 | -17.2163 | -45.9518 | 2025-09-19 03:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 8e8289af-4790-35f8-9bc5-23a5440d2725 | -6.2057 | -45.096 | 2025-09-19 03:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 3316e1fb-9d10-3451-87e9-80bab9ad8b35 | -9.1933 | -45.3114 | 2025-09-19 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| a9f0e886-5870-3855-a22e-df15f0e2486f | -17.2363 | -45.9476 | 2025-09-19 03:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 288.3 |
| fc330a16-5fea-3d6b-b75d-f402f77a9013 | -5.1386 | -47.8314 | 2025-09-19 03:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 5deedaa0-1ff6-3dd7-947b-4972bd08e6d8 | -17.2357 | -45.9711 | 2025-09-19 03:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 37b0b4ab-11d9-30d5-be65-30c9bf5aaa0b | -22.02331 | -42.21166 | 2025-09-19 03:10:00 | NOAA-21 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 38dd142b-b369-3f5c-beac-49e1b60a3b2e | -22.02113 | -42.20992 | 2025-09-19 03:10:00 | NOAA-21 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| bc0e6226-4c11-3cf7-8efd-2f3016db4883 | -10.3168 | -50.2352 | 2025-09-19 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| a718a607-0975-3cdb-b7db-39103dde97fb | -5.1386 | -47.8314 | 2025-09-19 03:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f8f0628b-1abb-3c6a-b716-f333f0c9cfbd | -7.5705 | -45.4786 | 2025-09-19 03:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| a2e46504-b68e-3a83-8a3b-1217d005ef78 | -17.2363 | -45.9476 | 2025-09-19 03:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 2aa6aafb-e14b-3b6d-b278-eaa0b9106dca | -9.1744 | -45.3135 | 2025-09-19 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| cbe0dbd3-b7bf-34f9-b612-0757fdef223b | -6.9024 | -44.7656 | 2025-09-19 03:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a735a937-bb1e-32c0-9687-8149053b403f | -12.8969 | -50.5398 | 2025-09-19 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| fe632466-7bd1-32c9-939e-a73ba3121f8a | -10.2979 | -50.2372 | 2025-09-19 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| fd460690-2d3b-3de7-9f22-4bf87fd8380e | -17.2163 | -45.9518 | 2025-09-19 03:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 053345f6-a621-35b3-a217-241f37c0a17e | -10.2982 | -50.2158 | 2025-09-19 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 66438081-7d04-39dd-b505-548468055258 | -12.8777 | -50.5422 | 2025-09-19 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 89a07268-1b25-34f3-a9f4-2119295018eb | -12.8777 | -50.5422 | 2025-09-19 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b23e9065-edbe-318c-af6c-f4f0a266389e | -12.8969 | -50.5398 | 2025-09-19 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| cac58c78-031f-326b-ae26-7cb021ff69af | -10.2982 | -50.2158 | 2025-09-19 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 7ea929a6-d689-330e-bab7-bd047bbf69e1 | -11.2147 | -49.6441 | 2025-09-19 03:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 23e02d96-f7b9-3979-afd4-2b8c9e5adc24 | -17.2363 | -45.9476 | 2025-09-19 03:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 261f4cf2-d2da-3725-883a-dcfb352f9335 | -5.1386 | -47.8314 | 2025-09-19 03:30:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b8134084-794c-3109-8470-811341142291 | -7.5705 | -45.4786 | 2025-09-19 03:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 17dfc9ea-a5fb-3b04-9b3d-bebced492687 | -10.2979 | -50.2372 | 2025-09-19 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 3bc3255f-e7a8-3e96-bc21-37c95578113e | -14.1889 | -51.3798 | 2025-09-19 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 0cc01f13-1de9-3d34-b438-2215d69a9c03 | -6.90346 | -44.77603 | 2025-09-19 03:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1c5c2ab6-3a13-3fad-b767-0a9f498c828c | -6.95612 | -42.44353 | 2025-09-19 03:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2c5dc3fa-3ab5-3f1c-b6f1-405803cb2905 | -7.57172 | -45.4731 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b60a7b1-d7cf-338c-99ea-bfea87ecb88a | -7.70185 | -44.47555 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7d6a28c-c3d8-38e1-a617-c85c687d82dd | -7.57725 | -45.48125 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a48463ef-f00f-38fd-aa3e-fd51a6f08bc7 | -7.92363 | -43.89224 | 2025-09-19 03:32:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d7d80aa-faae-3a1f-a011-0e85ca2ac623 | -6.90155 | -44.76996 | 2025-09-19 03:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 69776348-689e-3c35-9275-8963a9b42e24 | -5.16544 | -37.73317 | 2025-09-19 03:32:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 59378239-a6bd-3a82-94f4-891084a115fd | -5.63209 | -45.94456 | 2025-09-19 03:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29822737-0a6c-35cf-a590-2aff5a8996b7 | -5.14552 | -37.74004 | 2025-09-19 03:32:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bc1246cd-c071-3f6a-a4b6-021916401416 | -6.19221 | -41.19949 | 2025-09-19 03:32:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 57f9d9b6-383a-37a0-8004-3bd1f4ac26df | -7.24833 | -40.27661 | 2025-09-19 03:32:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 320e01b7-c6ff-3605-ae1d-7a688cf5e6c7 | -3.85645 | -40.34864 | 2025-09-19 03:32:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9aa21fc6-78a4-3476-89c5-2f62384555a5 | -7.54503 | -45.5013 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ae05bf0-15c5-3f74-bfbe-9b47e5b37ad7 | -7.92544 | -43.88243 | 2025-09-19 03:32:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19999317-094e-34f1-8aff-20f6ac12d022 | -6.9778 | -44.49311 | 2025-09-19 03:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1033aaff-37b5-30fc-b5f4-67e8de44a59f | -3.15368 | -43.26218 | 2025-09-19 03:32:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 382222d1-e2a9-3788-a1c9-52a3cf24db25 | -6.91112 | -44.77195 | 2025-09-19 03:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3c3a3492-d41a-3f7f-ae74-6ed37b20daef | -4.70367 | -41.96408 | 2025-09-19 03:32:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cdb764e2-19cd-38c4-8a01-833b601b77e1 | -7.36054 | -44.59222 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e2a3b7ec-93b1-3984-b037-c4b0fa9c1a07 | -7.84541 | -45.6336 | 2025-09-19 03:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ba9d591-a85b-37d6-8a6f-d6cb824ef260 | -7.92915 | -43.88379 | 2025-09-19 03:32:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7001540a-77fa-31ee-8c40-56173adb5e67 | -7.45773 | -38.77447 | 2025-09-19 03:32:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 75d97763-30b4-356a-901b-34e26f2870a2 | -7.83853 | -45.63711 | 2025-09-19 03:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 050e3eec-759b-3dcf-b73a-f05dd9fefa21 | -5.79406 | -43.908 | 2025-09-19 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19af81d9-3ad4-3831-991f-fbccc51f6a66 | -5.79335 | -45.36131 | 2025-09-19 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5b0ceca-38e9-338f-a6b7-375ab400d623 | -7.55977 | -45.49831 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 479011c9-49ba-33bb-917e-f086152d4bf5 | -5.63799 | -45.95328 | 2025-09-19 03:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2211effb-3ef3-320d-be0c-d95d2693c6c8 | -5.92232 | -45.08581 | 2025-09-19 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2a29a51-aeb0-3328-8b2d-fce83cc37829 | -6.8338 | -41.03959 | 2025-09-19 03:32:00 | NPP-375D | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f08f7a0d-766f-32df-a8f5-9bc57c9abbf5 | -7.31338 | -44.05599 | 2025-09-19 03:32:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dc94a0f1-8f16-35c5-bbf5-ab564e67a664 | -5.91567 | -45.08388 | 2025-09-19 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbc5a17d-0c8a-31cf-8d5d-a605b607514a | -7.5759 | -45.4883 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ba083963-950c-3b77-a0bc-555cfff6b5e9 | -7.55542 | -45.48361 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 739048d6-39e9-392b-9f5e-73af5edeefc7 | -7.57041 | -45.47992 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bdf74509-ea71-3e99-a471-723b4f25bdd9 | -8.13611 | -44.47602 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 980fd22c-27b6-3b5d-8522-3232b62334d1 | -7.55003 | -44.74295 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c97d600-9f0f-3ce2-90a7-c6a1d9de1db4 | -5.63079 | -45.95169 | 2025-09-19 03:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d8a9f12-af51-349a-9344-f803533ad7ee | -6.82799 | -41.04179 | 2025-09-19 03:32:00 | NPP-375D | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e9caa578-d922-31a7-ae74-26e6bc9311d5 | -4.78012 | -42.75068 | 2025-09-19 03:32:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 125c96a2-3ec7-3dc8-bdc6-e38172bbe2a5 | -5.795 | -43.9035 | 2025-09-19 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1caf313-a6ba-39bf-98ea-c45bf1509fcd | -7.55295 | -45.49681 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc00817e-82c4-30ed-9431-1e3c37647648 | -6.90455 | -44.77037 | 2025-09-19 03:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9ae4f767-a681-33ed-b526-1866f28f2e4b | -7.04023 | -46.41991 | 2025-09-19 03:32:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| baad5208-5427-3eb0-a3c6-c238e2d3f30b | -4.69859 | -41.95901 | 2025-09-19 03:32:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4cdf4e06-a21f-33f8-8811-e2167b7dc6fe | -5.63183 | -45.94915 | 2025-09-19 03:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 24c2dd89-b9a7-381f-a582-9ca2955758a1 | -7.71077 | -44.39587 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f98ef711-50fb-302e-81e7-2da7c28bd124 | -7.35329 | -44.58618 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73603364-bf1f-3ef1-ab46-dbf0190a79d4 | -5.795 | -43.90273 | 2025-09-19 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdf28deb-1dbd-3fe7-82f5-97d68e0c2d6b | -5.24821 | -38.17666 | 2025-09-19 03:32:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 464c5a55-2022-313e-8fd8-208032c28ffa | -6.89673 | -44.77525 | 2025-09-19 03:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5388ee1e-019f-39d3-86eb-6f29a7a1e857 | -7.35497 | -44.58585 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f752bd33-e1f6-334a-b2b8-39c710595786 | -5.92254 | -45.0851 | 2025-09-19 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f994f4d-1577-3684-a391-603c7fbb748e | -7.35555 | -38.96497 | 2025-09-19 03:32:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 61f34d4b-a4bd-3691-bb59-b9ba9868e746 | -6.95034 | -42.44264 | 2025-09-19 03:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3693f59b-4ece-3a2f-bed1-20b03b5481cb | -7.56487 | -45.47184 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14af8eb6-461e-3331-ae06-8e1b7d31231c | -7.36087 | -38.96122 | 2025-09-19 03:32:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 45f1b276-8208-3d7c-a5d1-10781adc2914 | -7.83726 | -45.63881 | 2025-09-19 03:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a5530717-cc83-3d79-98de-7dd1c1caa151 | -5.80143 | -43.90465 | 2025-09-19 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d61b710-f020-3b20-95db-a35d168d3d2c | -7.5449 | -45.50171 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83b9fbe3-afe7-3e2f-bc29-be4192618195 | -7.92458 | -43.88705 | 2025-09-19 03:32:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9589aafc-ba1f-37cd-b20b-619717c87865 | -5.50199 | -37.79117 | 2025-09-19 03:32:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5edfe751-d522-3a28-b933-9f1d30d5c545 | -7.70286 | -44.47012 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb157c86-2725-3c91-b2b3-8f916c9ea72f | -5.91545 | -45.08459 | 2025-09-19 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12bcd4c0-598c-3354-85a8-976ccd381260 | -7.14069 | -35.58117 | 2025-09-19 03:32:00 | NPP-375D | JUAREZ TÁVORA | PARAÍBA | Brasil | 2507606 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f5b3e5b3-3151-3670-930b-8acfd37213e6 | -3.1528 | -43.26743 | 2025-09-19 03:32:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6db6c5e-c4ce-3ead-819e-940a39678326 | -5.78856 | -43.90246 | 2025-09-19 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 828281fd-8d97-3340-94d2-343f8cfd492a | -4.69787 | -41.96315 | 2025-09-19 03:32:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5367e43c-0217-39b2-a622-87627a633c71 | -6.95685 | -42.43952 | 2025-09-19 03:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6c98e098-804a-31f0-be09-5d99feafc60c | -8.37686 | -44.68118 | 2025-09-19 03:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 93d13f46-4e21-39a1-aa96-86332025623d | -6.90818 | -44.77127 | 2025-09-19 03:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 07665170-74e9-3e95-b774-9c82d574336e | -5.46877 | -44.696 | 2025-09-19 03:32:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README6.md)
