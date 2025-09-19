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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dd8f130-015d-3d1f-a419-adfb33817761 | -5.8332 | -46.35578 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8106b12e-f520-3d99-847b-0758b236c4ad | -8.87357 | -50.14737 | 2025-09-19 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33257bf1-ad76-3547-8ff1-6d6d5a39c394 | -5.75983 | -43.39182 | 2025-09-19 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0c9ee40f-9e55-3fd9-9a5f-7a81d147473d | -11.16825 | -45.36124 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c25a916-b4f7-3ae7-97a6-e67ec6097fd8 | -5.8825 | -45.74556 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a94677d7-d426-300e-96c9-faf78c4e8363 | -10.24565 | -48.03651 | 2025-09-19 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| aba44fa8-431a-326b-8257-2be8db3ed154 | -12.10623 | -44.84537 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3caa2530-ddf5-3e81-80ff-1301d6cf8b9a | -5.80342 | -43.64235 | 2025-09-19 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 118ecd3b-cdd4-3833-941d-d93ec8f7a761 | -5.80815 | -43.64299 | 2025-09-19 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66cd1db7-4f0f-3e18-a820-d3fa4d97318d | -5.2652 | -50.76894 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06ec587f-8459-39f2-9e87-b106b0010d66 | -7.56938 | -45.47291 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 76fd12b8-25f2-350b-bcca-1d02ab4451a8 | -8.04306 | -45.72707 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61b90409-6885-3e64-8c8b-12db22d2dbe9 | -10.04489 | -49.20262 | 2025-09-19 04:46:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 931c0ecb-7b40-3ac8-96f2-863b3afd1e86 | -8.04784 | -45.72378 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e7f1a3b-98a0-34e7-a16a-a679cedabf57 | -9.17056 | -44.89468 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05b13624-6e64-3906-947f-809eec8d34c9 | -8.02948 | -45.7008 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 29e74c6f-b151-3faf-8c8b-024541a0045e | -9.189 | -45.31027 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cd137c4-e9e2-3648-8ea4-139102a3cb63 | -11.08916 | -41.06398 | 2025-09-19 04:46:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| abbbcc6f-eddc-3e12-94cc-6b87a3c7cad1 | -7.55114 | -44.78117 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc091806-ce6a-3e29-81fc-aa090c952ff6 | -10.29072 | -50.23373 | 2025-09-19 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a4e0e3f1-b6af-34fa-b922-3026c4317a27 | -7.36356 | -44.58259 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b341e93-95d8-361b-886c-f16ab06f4690 | -10.36767 | -42.45808 | 2025-09-19 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b56589c-56c7-3152-9f1d-4eb886116b00 | -5.86992 | -45.88839 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fdf64c7-c410-3bed-ac57-f73981ec9d67 | -7.58532 | -45.48328 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ea0eb80-37d0-3a1c-813c-af4944f48d1f | -6.20867 | -45.10811 | 2025-09-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 719c392b-3acd-3816-9ddb-e53b2bad8441 | -10.33 | -45.24867 | 2025-09-19 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf1c5e77-d138-359e-9a97-dc2c22c39948 | -5.4739 | -46.68498 | 2025-09-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c061549-3ddf-3c7d-aa77-eab7eb5d1795 | -6.95951 | -44.76491 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d49770f0-c54d-3e50-adfc-772fa9030b97 | -7.84712 | -45.61557 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29b70be7-795b-3a0b-8f0e-66c5ced60419 | -7.44185 | -42.62775 | 2025-09-19 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8efdb053-d529-3752-a965-d4cf89c23e0d | -7.04435 | -42.00591 | 2025-09-19 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cfdec22e-3716-3d1c-860b-ea140ae9ea45 | -5.82884 | -45.91502 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fef40426-a330-3420-959d-b576b6e94b6b | -7.58033 | -46.72438 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e66ca09a-6afa-3cc8-a4fe-8ef65dee60e1 | -11.21484 | -49.63375 | 2025-09-19 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 03c3a092-ee43-3b63-928e-68b51c538667 | -7.1895 | -44.42034 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 91521b9a-062c-3096-ac13-e039c5af3e15 | -5.6236 | -45.41134 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 975193ba-4c39-3a8c-900b-1a8dddb260d1 | -8.0205 | -45.70321 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d95d3129-4bef-327a-9cf8-9675c46d0f5b | -12.09738 | -44.80382 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 732dd9a9-c120-319b-acd0-857787a881a0 | -5.80078 | -45.35725 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64f4a0e4-17de-3c3b-bff4-decc2cf923b7 | -10.92038 | -45.64985 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12e83775-3ac1-37b1-9c14-fdb82f1e77b1 | -5.80021 | -43.75159 | 2025-09-19 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc2706e2-f146-3049-a885-51f14fc88436 | -11.45727 | -43.54549 | 2025-09-19 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcd1e49f-f993-3f2c-8708-4462b680dd99 | -7.23774 | -46.59746 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ca0a63e-f197-36e2-91e3-01e928c093d5 | -5.79966 | -45.71433 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b96bf818-6340-338c-a2c8-830be3934475 | -7.43734 | -46.38571 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 408fd762-4bf3-3f18-8c43-577dd8e983fd | -7.85499 | -45.62122 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e845ac4-f45c-3d12-a488-50a8c057ddaf | -7.84769 | -45.61152 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2004e382-d83a-3deb-8b5d-0afccf32a077 | -7.5623 | -45.49192 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 907a6271-6d36-3725-b14f-ecfa28b206c6 | -9.87088 | -46.43797 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e52dd95a-a0db-3215-be37-11b8164a2ce4 | -6.81704 | -47.84915 | 2025-09-19 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0902888-ddad-39cc-9a02-eee405f750b0 | -7.38553 | -44.29317 | 2025-09-19 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5e61cb4-a951-31ab-9ca2-f2593891a3ac | -10.69502 | -46.46601 | 2025-09-19 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac861764-ab00-3681-be88-94ba57d0ea9c | -7.56142 | -45.46761 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c7d5ea5-9bca-3498-96a4-a4f8d70d549a | -9.76692 | -48.57677 | 2025-09-19 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20dfc2ba-ae9b-3d4c-876f-4aab4ed04554 | -5.88565 | -45.72404 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 527a1507-4e62-3734-a15b-bb076506aaf2 | -5.77192 | -45.90224 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c1067cf-c205-3e7a-8023-e46c18542a7c | -8.90583 | -46.12986 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fb55106-53e7-35d6-90e7-fcd714175f7e | -6.59379 | -45.58091 | 2025-09-19 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 386ec6c4-586f-367a-9e32-eebab61d39cc | -13.12876 | -41.0522 | 2025-09-19 04:46:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dfadcafb-516d-3978-bf88-d9a87f850c85 | -5.79758 | -43.75389 | 2025-09-19 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f9867cc-4f60-340a-a37a-83e21f3d098f | -7.54409 | -45.49752 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc620fcf-47a2-3ee3-ad4c-219e481d5970 | -6.42224 | -43.87312 | 2025-09-19 04:46:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3793621f-9f20-35f3-a763-7411fec30a07 | -5.77859 | -45.96833 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b53d3e0-901e-3553-85b5-aa74e9f48b4e | -11.59964 | -49.82263 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a152863e-345b-3b02-ba53-536b025ff50c | -11.17978 | -45.36945 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 204e4ce0-4563-3400-9e3c-eec53e822899 | -6.92633 | -44.90673 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1513f84d-28ce-389b-996b-1a79ce14fcd3 | -9.13701 | -49.86325 | 2025-09-19 04:46:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8d293483-d03e-382d-9851-842fa35f1f4c | -5.82582 | -45.90729 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fce7b7e4-f0ba-385e-aa42-cb3896512230 | -7.86154 | -48.14692 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a04b11b-b6eb-39e3-8386-aea685fa9ca5 | -11.16151 | -45.33369 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4532f77-ef7c-3cb9-bc0b-41dd3128aecf | -7.01382 | -44.63737 | 2025-09-19 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 714f1891-ddfc-37c2-8930-972222d2bdcb | -7.57252 | -45.48138 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fb8bc6d9-9c59-3015-84d1-65187d73f6d1 | -12.73297 | -47.74333 | 2025-09-19 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1199cd8c-c899-3d58-9e17-25fedf2428b3 | -5.82531 | -45.91084 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1363bb79-86aa-3cdf-9924-dc3d3ebf1a76 | -5.79659 | -45.35661 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87412866-71af-3d1b-82db-e43fd616e8a7 | -7.84959 | -45.6288 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e65eeabe-68fd-3e9e-a1ba-44cc86434edf | -5.80886 | -43.63788 | 2025-09-19 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 146a88c8-1c51-3a81-b712-f505e1c5e994 | -6.93044 | -44.7536 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0e4f3cf3-5f4e-39c2-bc13-352714f7d9f5 | -7.92646 | -43.88289 | 2025-09-19 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9e8ee3d0-0b18-3e4f-8bdf-701cfe557314 | -12.09619 | -44.81342 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 213b82b4-8a47-3fc5-ba4a-15b6bb2a20c2 | -12.48088 | -44.74047 | 2025-09-19 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63658506-0c3b-33c5-b3ed-e3ce78015610 | -7.3161 | -44.05184 | 2025-09-19 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 136ccd3f-9094-3574-8599-9bd90baf3b58 | -10.35769 | -47.8779 | 2025-09-19 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2f519c6-1733-3a8d-ac2f-a88af46b619d | -17.08759 | -43.33356 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e442fceb-0a5b-33c6-ac19-32d12eaf9921 | -14.83005 | -60.24266 | 2025-09-19 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f04f6708-6fad-3e6b-83d9-4a5bfb5e709a | -15.01634 | -55.32434 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b2ea89a-8427-3156-99ce-4956e7411d5e | -17.22376 | -45.95651 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20e92e74-8b3c-36db-890d-4f5b28ac4534 | -15.03448 | -55.33932 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8a90b65-1ead-3e83-930e-44db9c2b8534 | -17.08433 | -43.34553 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86885cd2-c4ff-39a7-83ed-703cbb6b448b | -15.32902 | -42.05393 | 2025-09-19 04:49:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d81cd87a-b67c-38b3-91ce-26bec97d1269 | -11.81799 | -57.62896 | 2025-09-19 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 93f9befb-0e65-3333-a62c-c552d2a6d39c | -18.95836 | -42.08212 | 2025-09-19 04:49:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| bee33f23-0ca6-3adb-9869-d25e0983365c | -14.13121 | -44.59422 | 2025-09-19 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af9ba530-22ec-3335-a1c4-294bd5668a57 | -17.09237 | -43.34203 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 36669014-9381-3bbf-a02b-279775abd0bd | -15.03576 | -55.33168 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31b05d82-e271-3672-be1b-868b4023d86c | -11.81329 | -57.6319 | 2025-09-19 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3ee1fdb6-7f3e-3af6-95db-08251a10b121 | -16.69122 | -54.97332 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a038276c-e9e9-3f07-8029-e7555a8bf33a | -18.02165 | -50.94337 | 2025-09-19 04:49:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 274d8f71-0675-3dbf-9a22-c1d984e63e9e | -17.09109 | -43.3351 | 2025-09-19 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| db46ecf3-b9f7-3ef6-8b56-3efef93526c5 | -15.91082 | -59.44252 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README29.md)
