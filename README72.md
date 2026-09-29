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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad9056f2-ddf8-3b92-8751-1c1354dd9255 | -6.46535 | -43.88646 | 2026-09-29 11:23:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f53762ce-0636-3ae6-90d9-469cb090fdec | -7.07965 | -41.74352 | 2026-09-29 11:23:00 | TERRA_M-M | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 1f57198b-ccd2-3566-9696-93a1af124374 | -5.74079 | -45.15971 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2d69a9ac-561d-3232-80a1-d37f5fd87d68 | -12.02108 | -47.806 | 2026-09-29 11:23:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 46b32c3b-7d2b-396f-9bec-d233abf24c25 | -6.91051 | -43.68609 | 2026-09-29 11:23:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 85e5918a-baff-33f4-bc60-d4c242b9d360 | -11.59079 | -40.18904 | 2026-09-29 11:23:00 | TERRA_M-M | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a485a6bd-cf74-3a0e-9cf6-d0cb4be0cb29 | -11.38525 | -47.46061 | 2026-09-29 11:23:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8253136d-af96-3a9e-bdc7-7da4c8f92da4 | -10.28159 | -44.61617 | 2026-09-29 11:23:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f9dcf7b2-b1c4-3b3e-967f-7700450c7756 | -11.17872 | -44.79196 | 2026-09-29 11:23:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| bc11537f-a1f3-39fb-b879-48ac51c1fe3f | -7.98662 | -44.15625 | 2026-09-29 11:23:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 45fc5e25-c26b-3325-8c2b-cd683b2908c9 | -11.39206 | -43.45433 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 9bccea09-8e79-330e-84d2-70a2ea8d3b2b | -7.83552 | -45.81826 | 2026-09-29 11:23:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| d100d00b-1f4a-3e17-9724-720c44914776 | -12.24809 | -44.61401 | 2026-09-29 11:23:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 364b5d1f-afbd-37ac-82ab-49f4e1684dff | -11.1773 | -44.80152 | 2026-09-29 11:23:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 4d9867cd-91aa-3579-b4ba-968943bd0102 | -7.0609 | -42.06527 | 2026-09-29 11:23:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1dcf59b9-55e3-3c15-b30d-f2432b9f9204 | -12.88658 | -41.73623 | 2026-09-29 11:23:00 | TERRA_M-M | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 748233ad-57aa-3367-9518-09e2454b01c5 | -6.29896 | -43.64016 | 2026-09-29 11:23:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b6405e07-c615-32c4-a9da-2ca5c271d83e | -8.98176 | -44.16647 | 2026-09-29 11:23:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 76103920-d06f-315b-8835-b5be69fa1613 | -6.44868 | -41.89185 | 2026-09-29 11:23:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 42.3 |
| 63dd3202-d1ad-3389-97be-14d291228a4f | -7.05964 | -42.07409 | 2026-09-29 11:23:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 0542450e-3fbf-3b28-9327-53e4f0cf41da | -8.36677 | -45.43067 | 2026-09-29 11:23:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7f4a5613-3ce8-34b4-89da-8042ae8085f3 | -11.45522 | -43.46949 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| cea1d033-4f00-32cc-8eab-25ffd3b4b267 | -7.51229 | -44.55219 | 2026-09-29 11:23:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f149084b-674f-3cbe-b00d-8224fea6a04b | -5.74728 | -45.18413 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d9012ecf-928c-3cd1-811b-ae3b3c7eaad8 | -7.72223 | -44.57454 | 2026-09-29 11:23:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| da147b7f-6cf3-309d-9125-3d2b96dbf9c1 | -5.73907 | -45.17118 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| ad674567-377d-3dbb-832b-01e298e0c38f | -6.28989 | -43.63887 | 2026-09-29 11:23:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 55ad6cb5-d8dc-3ff6-b090-7434ea7cbe91 | -8.4551 | -39.79081 | 2026-09-29 11:23:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 4826403a-007b-3504-ac94-42f653a8daf9 | -7.06494 | -42.30576 | 2026-09-29 11:23:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6c0097c1-8179-3e2b-ab7e-4b2c14d28902 | -7.47084 | -45.79332 | 2026-09-29 11:23:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b49fac58-7488-35ac-bd3e-d9731f9496a3 | -11.16818 | -44.8002 | 2026-09-29 11:23:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9f010dbe-adfd-38e1-b36a-6c7b9702f2a2 | -11.19124 | -45.13829 | 2026-09-29 11:23:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 0302a988-1fa7-3301-9a9f-c40f786ca3dc | -6.29124 | -43.62953 | 2026-09-29 11:23:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cbf91ec3-2d59-322a-b955-fa8f1689f878 | -6.28853 | -43.64826 | 2026-09-29 11:23:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 0e2c5814-9f92-3b8d-b65f-20d73fcc9a74 | -11.1696 | -44.79063 | 2026-09-29 11:23:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| be9861f3-038b-3768-be1c-82c6f553e55b | -13.37931 | -44.01588 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f1811ad6-f58e-35bc-b480-cd547eb5daa7 | -15.74926 | -42.28059 | 2026-09-29 11:25:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1c0e4cc8-6f06-3049-82cc-cf6b8c9d5850 | -13.16069 | -42.36095 | 2026-09-29 11:25:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3fe4a183-6fe2-33ec-9806-60a7da230042 | -13.46914 | -43.5786 | 2026-09-29 11:25:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 06ef6661-8177-3a7f-8ad4-1ce0701235f8 | -13.76231 | -41.52542 | 2026-09-29 11:25:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 5d7cc12d-9dd0-303e-9f15-f673e25bce85 | -14.11418 | -46.27663 | 2026-09-29 11:25:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 6b29962f-21a0-3239-bf93-fb3978c2878a | -13.05973 | -47.45243 | 2026-09-29 11:25:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 168d3808-6440-3189-b3b3-afd03f431006 | -13.20535 | -48.55377 | 2026-09-29 11:25:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d404fc2d-562d-3c7d-a1a1-7fa1e5e5bfbd | -13.34558 | -46.81241 | 2026-09-29 11:25:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 7090943f-2cbc-31c9-a68d-aba0c8ac0e0d | -14.13314 | -46.27968 | 2026-09-29 11:25:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 34.1 |
| f00b8c62-5f25-3752-ac11-68cbb0ac5e49 | -13.65885 | -42.08489 | 2026-09-29 11:25:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| df28b0bc-258a-311f-9646-1946e56036cc | -15.46464 | -46.1299 | 2026-09-29 11:25:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7aa78a2e-e4a1-3265-9df8-5e51c06892e2 | -15.21873 | -41.97708 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 3797fde8-aa60-3bc9-a781-02d07e352c25 | -13.31733 | -43.74314 | 2026-09-29 11:25:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3870874c-1dd8-36c1-a36e-95dc3cbe66f8 | -12.49158 | -44.96503 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1ec5800c-aab3-34d9-868f-1b736008830d | -12.94968 | -46.64758 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| f1a589fa-5fb6-3953-beba-73c07ee10ad0 | -13.55374 | -43.50553 | 2026-09-29 11:25:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 527e3c71-e8ae-38de-b57e-d204397d07fb | -15.3976 | -47.92072 | 2026-09-29 11:25:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fbcd8826-1f35-3334-81c9-de8429fb8d1e | -14.32197 | -42.1521 | 2026-09-29 11:25:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 21.2 |
| e0bee29c-ae21-391b-83e7-e00174457645 | -12.76921 | -47.28875 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| f3491e26-210e-3b39-81a8-9605bfeb1eb9 | -14.08876 | -46.31582 | 2026-09-29 11:25:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ef2d3efb-88be-3a9c-b708-f5399d6bd551 | -13.46786 | -43.58759 | 2026-09-29 11:25:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 8c4d163e-2f46-3529-91e3-84adb1a870f7 | -12.76087 | -47.27428 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| a7b1bdfe-fb8d-3796-87e2-0ac80d0eaca8 | -14.4923 | -43.26028 | 2026-09-29 11:25:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 57308144-3ab4-3f8e-a62b-3a07f34fe808 | -15.2598 | -47.62701 | 2026-09-29 11:25:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4ef2ecb6-7d2b-30a9-aa34-7a652670caf5 | -14.17226 | -41.82839 | 2026-09-29 11:25:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 4cffabb2-36f5-3435-995e-b1b8b9a8270c | -14.07924 | -46.31445 | 2026-09-29 11:25:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dbb1a95c-a602-3717-8413-f81de5fbc225 | -13.6699 | -45.78431 | 2026-09-29 11:25:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5ba6ec41-716b-3010-962a-036f3fa0bd75 | -12.8846 | -44.80738 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| a8a6d310-7672-3fa6-87c5-46f987658854 | -12.69891 | -47.26473 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ba1c27e2-969a-34e0-ae9f-1ac799c0613a | -14.10046 | -46.6473 | 2026-09-29 11:25:00 | TERRA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 88c21c93-4b79-3c6c-90ee-3c627e0cb541 | -12.6969 | -47.27729 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e006cfab-7093-3248-a7ad-b71791f0e490 | -15.21068 | -46.1644 | 2026-09-29 11:25:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 16ffc499-194d-3a87-a5c0-5e8a2751863a | -14.09038 | -46.30529 | 2026-09-29 11:25:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1a5c34c6-a110-3eea-80ed-ee467615a4c1 | -15.22233 | -43.82468 | 2026-09-29 11:25:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bef93cbe-c0bb-3937-a33b-dd788dd19091 | -12.75058 | -47.27246 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| a84d87bf-c00b-3362-846a-e9b0e76c424c | -15.25455 | -44.81914 | 2026-09-29 11:25:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bb0c2a54-cc7f-3494-b12e-df71d04df7bf | -13.66836 | -45.79436 | 2026-09-29 11:25:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| adaab7cf-d83f-3b36-a138-a3645f0464d6 | -15.21996 | -46.16607 | 2026-09-29 11:25:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 27ad13d7-3328-356b-b96d-dcdf18835b42 | -14.10219 | -46.63619 | 2026-09-29 11:25:00 | TERRA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3e9b42a8-643e-39ac-8dbe-24ce4e6f7f38 | -15.88363 | -42.65118 | 2026-09-29 11:25:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 18d98a3f-25be-3e6c-8655-873c89140ac7 | -12.74858 | -47.2853 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| a5439123-7049-3c0b-a157-d387e100ad3d | -12.95139 | -46.63636 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| a0545538-2a83-3e70-84d6-cac862e47208 | -14.12366 | -46.27819 | 2026-09-29 11:25:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 9d0a2860-e5ab-3b2c-b2e7-c6f005f3cbfe | -15.68499 | -49.40486 | 2026-09-29 11:25:00 | TERRA_M-M | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a0e464c6-35bc-327c-8287-0dc12372b7e7 | -12.75889 | -47.28701 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 51c5f16c-f7e1-3e3e-997e-694a72f8e26e | -14.517 | -48.29318 | 2026-09-29 11:25:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| df777c96-4478-3fea-ac69-bd7a13f22a88 | -13.6213 | -43.74181 | 2026-09-29 11:25:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fe085d6e-863b-3a70-9c61-d8d6335bce43 | -12.76724 | -47.30146 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e4fe75b7-4e25-3466-8a6e-9831491437aa | -12.61601 | -47.27142 | 2026-09-29 11:25:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| f9435a07-d766-3078-995b-0d5c92a014a9 | -15.75844 | -42.28195 | 2026-09-29 11:25:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 74c10cec-4a8f-3174-a17a-8467a5df3a4b | -12.70724 | -47.27889 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 18c68abd-7d32-3e72-bb3f-ea53455e7677 | -15.21131 | -41.97988 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 698a26f6-d475-3e49-8149-33f0b478b300 | -12.74218 | -47.25857 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 81e022ba-53cc-3d4f-9536-fe547d0252a7 | -11.99293 | -50.93158 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 9fb1715f-76d9-3e84-b0db-365077f6ee02 | -14.12205 | -46.2888 | 2026-09-29 11:25:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1c38153b-754a-385e-addb-45a669b532cb | -14.12333 | -42.19054 | 2026-09-29 11:25:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 693d2829-66e3-3ef3-b3d6-5dd88016ec5e | -12.60365 | -47.28242 | 2026-09-29 11:25:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c938807a-5464-372f-89e8-567b093393ad | -12.74026 | -47.27081 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 9668e1a8-8b1c-33dc-8351-616a1858f683 | -12.70923 | -47.26636 | 2026-09-29 11:25:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 7bc8dd94-5def-3ca6-adac-3362d2e61afa | -11.99802 | -50.95059 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 001d5166-ad19-34b5-a21c-b062589cc909 | -16.26019 | -41.70533 | 2026-09-29 11:25:00 | TERRA_M-M | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| f54eff31-098b-395f-9695-905bdf68f9e5 | -12.00685 | -50.93398 | 2026-09-29 11:25:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 26b58196-26ff-3a3a-a624-be837757d91b | -15.24508 | -43.27864 | 2026-09-29 11:25:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 9.8 |
| b07f91a4-5dd6-3e97-8826-5b95b0a11fe2 | -13.68487 | -42.76561 | 2026-09-29 11:25:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |


[Clique aqui para ver as próximas entradas](README73.md)
