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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79adafa5-6a7c-3034-bbc4-fa4f581b7697 | -13.66702 | -44.30771 | 2026-10-01 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c8edd17-6423-3155-bc6b-750a6e73a3e1 | -9.21599 | -45.81616 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1252fa9-3c52-3e57-b961-b08cf85c7ead | -8.38893 | -46.29137 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b384c7c-b318-3349-8d06-ed49a3861994 | -11.44117 | -43.42149 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 386b0b98-1187-3e1a-8fe6-b84ffd189612 | -11.43058 | -43.42258 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a52343d-587e-3547-9295-0e2c6da8cf49 | -11.41305 | -43.40762 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e6dfd3d-8fd2-312b-987b-79e734c7e600 | -11.46687 | -43.45094 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0d5114f-e48a-325b-a4ee-d13d5d7fb2ca | -12.50848 | -43.10534 | 2026-10-01 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 04cc311b-94b6-3909-a3cb-0f5800edb20d | -8.04486 | -42.86358 | 2026-10-01 03:38:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 287f1f58-1105-3d99-b1fc-2c4f72c9e6c3 | -11.1753 | -45.11987 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 184921a2-0e8a-3459-a566-9eeb9b3306ef | -7.84755 | -45.81479 | 2026-10-01 03:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4b956ce8-67a7-38c0-a300-5d7f7d127e60 | -11.16889 | -45.12287 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eaba3ea6-1403-3336-a70f-336a3e11d669 | -11.44955 | -43.43225 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ee516e54-6384-3a6d-932a-98aeabd1ce59 | -8.20478 | -45.50063 | 2026-10-01 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b9aaca67-2d12-3666-b698-598296745a7d | -11.38742 | -43.40586 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f25108c-86e7-342a-b802-19840c50c4ac | -9.21391 | -45.82302 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 05ef0990-a5e3-3d3a-a220-d311bea52f01 | -12.60954 | -42.16863 | 2026-10-01 03:38:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 509ab2ac-3965-313d-8075-9df7022d2849 | -10.32612 | -47.79168 | 2026-10-01 03:38:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b75e8b6c-48ab-3a55-9193-bbc14b2afdb5 | -7.49799 | -45.79825 | 2026-10-01 03:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d084d184-1585-3292-808f-332ba120a864 | -12.35676 | -46.38433 | 2026-10-01 03:38:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 01fee80f-107b-3ac1-966b-556c6ed23f2f | -7.56523 | -47.21409 | 2026-10-01 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcaf40cc-8ce5-3b0e-a59c-34e76054b170 | -7.49641 | -45.79465 | 2026-10-01 03:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10a2a1b0-6f11-3b7c-ad3b-fd1dabab3cdf | -8.38617 | -46.29445 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 25263391-fc08-354e-abec-c926ed8c1c5a | -8.62104 | -45.37016 | 2026-10-01 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e18e54f8-ae0f-3269-b819-9d9915105590 | -11.38797 | -43.4029 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64825907-66de-3fb8-9cf6-94d95b103e90 | -12.56336 | -43.07404 | 2026-10-01 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5fc37bcc-c4f8-3ba4-a370-6c94945af508 | -11.43616 | -43.42055 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a9d6d67-4f6c-34ec-aaff-0aa9a39e6c5e | -11.45571 | -43.45496 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22c41b8c-ef9a-3598-b723-fe0cdb87ff52 | -7.53977 | -47.12564 | 2026-10-01 03:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 812ff212-9f10-3bbe-8083-34048b55a832 | -7.51038 | -44.54249 | 2026-10-01 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a8321e0-9cdc-385c-af22-418326db626a | -7.61627 | -44.55298 | 2026-10-01 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc40ec13-52e3-3838-9944-4e9474be3b8c | -11.46184 | -43.45 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 866a4b13-a096-31a4-9b51-2f9c8241b149 | -13.88819 | -44.45307 | 2026-10-01 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99efe798-992d-3cce-b8d0-641ffc576e03 | -12.18614 | -48.44523 | 2026-10-01 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 672a08ce-746b-3070-b7b0-5ef7593d7fce | -13.38442 | -41.33761 | 2026-10-01 03:38:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 11cf3a17-7a0f-386d-861f-b994f6ae7139 | -10.84198 | -48.70667 | 2026-10-01 03:38:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ec58693-7f1d-3322-a8d6-2c59cccb2406 | -10.32741 | -47.78519 | 2026-10-01 03:38:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52f1656a-95b0-303f-a0d5-b790665dbeb4 | -13.86306 | -44.44516 | 2026-10-01 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cc53b03-dbea-3373-a8eb-d79284c9b55f | -11.44958 | -43.45989 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71e22c6a-81f1-38e0-8dd5-59cecc3b02fe | -10.73881 | -44.41617 | 2026-10-01 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ab8e7931-b7f4-3ee2-9eb4-dd0ef067fc5e | -8.12593 | -43.52693 | 2026-10-01 03:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc9bab4d-5499-3942-9359-d2d92e24d7a7 | -12.20044 | -43.83277 | 2026-10-01 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6788761-9815-327a-86fa-b89cde0d977b | -10.90531 | -43.84769 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1eb9492-1d07-35ac-b35b-1ddc6a59bfa2 | -13.86367 | -44.44205 | 2026-10-01 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 175feede-78a5-3623-92f9-2f671ed056f0 | -11.45958 | -43.43422 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ef288fd4-7e8e-3aec-9b5f-0ea5546e8399 | -11.38445 | -43.36572 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9efc7045-fe41-3411-9edd-ee9c0d3a0773 | -12.85822 | -44.33405 | 2026-10-01 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5015dbde-f56e-33ac-98cc-27f312fff608 | -11.4687 | -43.4537 | 2026-10-01 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 4070ec5f-4d58-3d61-bafd-a797b7160f3d | -11.4503 | -43.4091 | 2026-10-01 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 98e7c62d-c34e-34a5-b55f-b957f97f6791 | -14.8568 | -51.8454 | 2026-10-01 03:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 26b1cb39-8d6d-3db2-9c3e-f23715234160 | -13.6479 | -53.9336 | 2026-10-01 03:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 23d642c4-33f5-384e-82a1-bd9d7582bd9a | -11.4311 | -43.4121 | 2026-10-01 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3ee2cc4b-6887-30e5-9540-c2f4f6f10e32 | -3.295 | -53.8597 | 2026-10-01 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 2fbfa20d-5bd5-32f1-9f3f-a31a453a6c6d | -11.4499 | -43.4329 | 2026-10-01 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 7041c524-6dbd-3ba4-bed7-7c296d1fe89b | -14.4031 | -51.265 | 2026-10-01 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 9d6efdec-38d2-3ad9-8262-c02bd953a8c7 | -10.7853 | -50.5279 | 2026-10-01 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ce20f17f-0103-3378-9909-fc9b57aa6c6a | -14.3834 | -51.2892 | 2026-10-01 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| a41de804-b4c5-336f-97bc-fc2046d5350b | -3.1245 | -50.289 | 2026-10-01 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 33fa30b5-fe42-38e2-9605-6eb4a2ebfaa4 | -3.1655 | -54.0844 | 2026-10-01 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| a303d407-1200-39cf-ae40-ee0505807b50 | -5.7561 | -45.1747 | 2026-10-01 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| e31368d1-ca77-3561-83b8-55fa2c6432b5 | -3.1061 | -50.2686 | 2026-10-01 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8d459889-8a9e-38df-bd2d-af3b4e51570f | -5.7563 | -45.152 | 2026-10-01 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 9ccab9aa-5b0e-3707-99fe-a06437148bdd | -3.2766 | -53.8602 | 2026-10-01 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9ce2b168-2f06-316c-8618-b34b95d07fa2 | 1.7853 | -55.6449 | 2026-10-01 03:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 6bb1a8d1-6283-3b1d-a5da-d314c91f4948 | -14.8564 | -51.8668 | 2026-10-01 03:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 8be25256-436f-37b4-a391-7d2551c984eb | 1.8036 | -55.6447 | 2026-10-01 03:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| ad9152d0-d6e3-38a2-a6b1-1a3d664c6fcf | -14.8949 | -51.8829 | 2026-10-01 03:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 7407455b-d726-3214-9b88-356fdc1dd810 | -14.8762 | -51.8427 | 2026-10-01 03:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 165.3 |
| fa2ead4e-947b-330a-91e7-50dc61c2e695 | -13.6671 | -53.9314 | 2026-10-01 03:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 7ad7fb49-d459-3d8c-9d1b-e4c1de8e40b4 | -14.4225 | -51.2624 | 2026-10-01 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d5d79e0d-dedf-3fe6-830c-6233781525e9 | -12.1857 | -48.4345 | 2026-10-01 03:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 9932f0b0-22eb-38d0-8e97-224afa8c6fc0 | -11.4691 | -43.4299 | 2026-10-01 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 327f8e16-cb63-3038-b9b3-cc6895b4bf85 | -14.8758 | -51.8641 | 2026-10-01 03:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 7e701189-6242-31a6-aa40-e56e7a6ed1a3 | -3.106 | -50.2896 | 2026-10-01 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 738c60be-26b6-336c-8022-eee4b6903a6a | -3.1839 | -54.0839 | 2026-10-01 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8d91aa3d-eb8c-3a2d-a107-b842cdeea981 | -3.1655 | -54.1045 | 2026-10-01 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 3ec42f24-6dbb-307f-9675-04805e32183d | -3.1838 | -54.1241 | 2026-10-01 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e5a16f87-cebf-3478-82b7-fed1ac5d5210 | -11.4495 | -43.4566 | 2026-10-01 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b023f4a7-4e6e-32dc-8264-75a3c8f707fc | -3.1838 | -54.104 | 2026-10-01 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 187.2 |
| e5ef8d6d-6599-3d0a-b9b7-1b22aabcb833 | -21.71282 | -47.13327 | 2026-10-01 03:40:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2e11bc9-0e75-3929-b7e5-179e9bd1a175 | -15.85025 | -41.70459 | 2026-10-01 03:40:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c42b8d63-9529-3b71-8fa6-e636992d2e44 | -16.1645 | -42.86427 | 2026-10-01 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 919ca5d6-37f8-3b27-b44d-96a1350025fa | -19.25912 | -43.75162 | 2026-10-01 03:40:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fcea0d8-41ce-3db0-929e-dd4b3e67e673 | -15.95581 | -41.89519 | 2026-10-01 03:40:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 59c584f3-48cb-39e1-b6dc-62f4152a9f03 | -16.13262 | -43.74518 | 2026-10-01 03:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a5979a4-cd1e-3ef7-8bf7-594aba7106dc | -16.13846 | -43.7404 | 2026-10-01 03:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f375012-7679-3d7c-a3e6-dd6f4c734166 | -19.23338 | -42.95022 | 2026-10-01 03:40:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| ee89c300-784b-3389-9eec-eee825597b6f | -15.64368 | -44.713 | 2026-10-01 03:40:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87aa341e-9187-3660-89fc-52b476c448ef | -16.18869 | -42.88279 | 2026-10-01 03:40:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa28d4bd-257c-33de-aefb-5ced487b9bbb | -19.25822 | -43.75621 | 2026-10-01 03:40:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dee5804-5e73-31af-af0a-645e83990110 | -15.85301 | -41.71307 | 2026-10-01 03:40:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 82f412af-aa09-3a1f-b14c-15d572785cc2 | -18.65985 | -42.26139 | 2026-10-01 03:40:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5431f972-712e-3b5c-970e-b8492c7c34ee | -19.23464 | -42.94625 | 2026-10-01 03:40:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d279c254-c736-3611-b997-d35d75be7742 | -20.53971 | -45.76867 | 2026-10-01 03:40:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39ead011-eebc-3a2f-aa59-7cacc7646b7b | -18.27839 | -42.18555 | 2026-10-01 03:40:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 12d118de-03cb-31f7-a663-b5fd643fe18d | -20.27346 | -41.3343 | 2026-10-01 03:40:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 084396a6-c996-36a2-8f21-22db80c5c746 | -19.22994 | -42.94534 | 2026-10-01 03:40:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1f98b528-21a0-3116-8a92-7b9e5dad4b37 | -18.05583 | -51.14532 | 2026-10-01 03:40:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 986859d6-1b81-391b-beb7-507e3e66a8bd | -20.8972 | -47.41555 | 2026-10-01 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dfaf19a3-0f15-372b-a6e2-bdbbf709caa8 | -15.85716 | -41.71385 | 2026-10-01 03:40:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README25.md)
