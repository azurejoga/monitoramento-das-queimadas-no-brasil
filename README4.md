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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44f18408-0f3d-313b-8e8e-c23bc1dfd3aa | 2.6724 | -60.1453 | 2026-02-18 04:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 2e2d55f0-538c-34b7-a9bb-9314648aafe8 | 2.6905 | -60.2211 | 2026-02-18 04:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 614512f3-a734-3deb-80e0-29d1e41ce5a3 | 2.6905 | -60.2211 | 2026-02-18 04:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f5ab0990-8656-3e1a-a4b7-ee8515769b0b | 2.6905 | -60.2211 | 2026-02-18 04:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6d1d619b-d65d-3fc8-acff-f73d999193a2 | -9.51585 | -46.14805 | 2026-02-18 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b23786f6-f552-39cc-85fb-f4596e306cf3 | -8.44139 | -45.13488 | 2026-02-18 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 067a7d28-23f0-396f-a4e2-bc163eb4d208 | -8.16855 | -43.16669 | 2026-02-18 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 82caf75b-a3c8-3422-86ea-d1e9e95e2ff2 | -9.89699 | -44.26257 | 2026-02-18 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21f3b184-5b83-3bcb-bdfc-9b356ae7c7c7 | -8.1651 | -43.16616 | 2026-02-18 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba72fbc6-bd26-35a1-beae-ca95135c8108 | -9.5178 | -46.14807 | 2026-02-18 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e417e1f2-de95-3524-846a-f122ff71626b | -9.11115 | -44.67768 | 2026-02-18 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9ab53b5-a23e-30d7-9aca-e5f10826555f | -9.81499 | -38.10358 | 2026-02-18 04:25:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a5e89962-ee15-3e15-80ca-de7f20f8e247 | -14.41591 | -44.59313 | 2026-02-18 04:27:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b60a90d7-3090-3b95-84ab-93ba3febf71f | -12.60083 | -46.82736 | 2026-02-18 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1ff1803-b3a2-3c92-b4df-acb1dbdb5727 | -13.49963 | -46.70854 | 2026-02-18 04:27:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e52b0875-c057-3706-a6e5-1e837a13edaa | -16.64438 | -48.49633 | 2026-02-18 04:27:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3577aa60-892c-3213-8cf2-5ecec0d704d5 | -12.81263 | -44.82896 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94afd86d-53db-3239-a33c-16c61ef9babc | -13.30479 | -44.29301 | 2026-02-18 04:27:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43f5ea02-b6be-3e30-a152-c4cf57fe4754 | -11.88352 | -45.28707 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3745d4c-b815-3e0b-826e-149cd3ab6f21 | -12.47789 | -44.5055 | 2026-02-18 04:27:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7506fb36-a423-3117-bdc1-2e4fb6134a5a | -11.8902 | -45.28815 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5bd572a-fc72-3d87-b6af-431248840d9a | -15.42015 | -41.44213 | 2026-02-18 04:27:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3f5174fd-b703-3b78-84b5-e444b6105663 | -12.42491 | -47.18027 | 2026-02-18 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73c950d2-fcc8-31f1-b167-3b25c1b9c94c | -13.0193 | -45.04913 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecc31a75-5985-3585-8d40-8fd5266d8161 | -11.89075 | -45.28459 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 065b38fe-a6f0-37c2-88d8-3c5d37ae6b92 | -12.81489 | -44.83685 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1147913f-a754-341e-b191-e6bdaf8f7f41 | -11.89354 | -45.28868 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4c9a991-6c49-30cb-b10e-cc80f5d089e0 | -16.48202 | -43.76654 | 2026-02-18 04:27:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73595756-fd10-38ff-8a9c-81e531a4224b | -12.48639 | -43.64991 | 2026-02-18 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 85938e9b-f3c1-37be-bf8b-b4f0b7622455 | -13.02211 | -45.0533 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ddccccdb-f43b-3f49-9b54-9631cc268c45 | -12.47094 | -43.72861 | 2026-02-18 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a48c9183-72ec-3f8d-9f2f-945f6d8c9395 | -13.0148 | -45.05588 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d8f276d0-aa3e-39da-9075-77a28d3e9242 | -11.88797 | -45.28049 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f03e9a5f-d191-39a7-9406-8c32900da504 | -15.41697 | -43.68347 | 2026-02-18 04:27:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4f102e6b-9786-32ad-ad16-d6cdcf42fa48 | -11.88852 | -45.27692 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc24ce8d-538d-38a1-a58d-2c102ab11e23 | -10.6716 | -59.37277 | 2026-02-18 04:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 864872c4-925b-3a0e-89a1-64d740428388 | -12.48347 | -43.64539 | 2026-02-18 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f49f99f7-2e65-3d5c-ac9e-424e7f8712a0 | -13.01761 | -45.06007 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7efe4875-18c6-30f4-83c6-a783d70e9d83 | -17.62758 | -43.92904 | 2026-02-18 04:27:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99a20aff-eb0a-354c-a93c-8a8c6987dc6f | -12.60416 | -46.82792 | 2026-02-18 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 984e0eb1-c5db-3722-bc5c-85da7f23db75 | -13.30536 | -44.26552 | 2026-02-18 04:27:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c465f6e6-a1fd-3402-a6c4-12b367d8bcd2 | -12.68842 | -46.6991 | 2026-02-18 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14621e91-c6a9-3d00-958c-eed321c1791f | -14.51428 | -43.62638 | 2026-02-18 04:27:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50d8d2bf-4570-3cf4-affd-57ab8535305e | -12.69175 | -46.69965 | 2026-02-18 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc19744f-ab29-35a5-82d7-51085fd5f94f | -11.71175 | -44.73254 | 2026-02-18 04:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30562c7b-5812-3b20-93e5-2985dae2c064 | -13.01537 | -45.05223 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f8654bcf-8289-37a1-ac43-4cc472f4fb2a | -12.47035 | -43.73256 | 2026-02-18 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cce83ef2-67db-3f95-bd25-62c851f98efd | -10.73652 | -59.22649 | 2026-02-18 04:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3172dcd0-bcfc-3701-99bb-ef741f39b6a9 | -12.48991 | -43.65044 | 2026-02-18 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e19fe22a-f427-377f-b630-4a7e287c50c7 | -16.68139 | -41.36677 | 2026-02-18 04:27:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| be72e942-3540-3308-a4fa-fded85be54f6 | -14.41936 | -44.59369 | 2026-02-18 04:27:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26b33a87-be25-31e0-89c0-266c8d9d551f | -12.81206 | -44.83264 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14ac052b-46c1-3f6d-b97c-af2609db03e0 | -11.88462 | -45.27995 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7f29151-fbb1-35c8-be75-05dbccfb8532 | -16.66511 | -40.3545 | 2026-02-18 04:27:00 | NPP-375D | PALMÓPOLIS | MINAS GERAIS | Brasil | 3146750 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a6cb7744-5f2b-3ec0-90d3-a388ef1efdaf | -11.10345 | -46.60281 | 2026-02-18 04:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0798dda2-0740-36f3-bb61-6a14cf01b587 | -12.48407 | -43.64141 | 2026-02-18 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d08937d-9fb7-374c-af7b-eb1bd9182173 | -13.01424 | -45.05952 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| baae2bea-93ce-3365-8bcd-2c1bf33c8409 | -12.48759 | -43.64195 | 2026-02-18 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90492dfa-7ab1-399a-a9e4-6192d4cd7547 | -14.51069 | -43.62584 | 2026-02-18 04:27:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8c874cf5-7c6f-35fb-9886-9bfe420d5b09 | -12.81545 | -44.83318 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7a3d118-2fa3-301b-82ce-fc8a0430f2e7 | -12.25222 | -38.32153 | 2026-02-18 04:27:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 913a5d93-ba49-354d-91f5-b72d3a78bdf0 | -11.71119 | -44.73617 | 2026-02-18 04:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51fe0feb-e290-3c05-b53d-9efe651d808e | -16.68556 | -41.36766 | 2026-02-18 04:27:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cd75d96f-641d-33cd-b0ff-b3ee51eb0713 | -11.89465 | -45.28157 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27199d80-b223-36d2-88f6-81997eaee1c8 | -12.81319 | -44.82529 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dec25dd2-a88e-3502-915e-98eb180ab60b | -12.49051 | -43.64647 | 2026-02-18 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c0a2479a-07ff-3f80-91fc-ac5a09783621 | -15.17801 | -52.30357 | 2026-02-18 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92bfb13a-fc8e-3576-8045-b9c5f986c8e0 | -16.47838 | -43.76599 | 2026-02-18 04:27:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a40108a8-0535-3e5e-9e45-e920ab0f7e57 | -11.79529 | -44.13617 | 2026-02-18 04:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d2204d5c-a9ed-3527-b135-ebfad5788b00 | -13.21113 | -47.77945 | 2026-02-18 04:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b97e7bb-0ec7-301b-b6ce-1cebca18630d | -11.88686 | -45.28761 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5c9b0be-c709-3cf0-8985-5075c6f3cf60 | -11.89688 | -45.28923 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50635c0a-4ccf-369e-b461-978894892797 | -12.48055 | -43.64088 | 2026-02-18 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85bfce91-2c14-3501-9083-0bf87d4be135 | -11.8863 | -45.29117 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce877ae0-10b2-3865-87f2-60258c012999 | -10.67033 | -59.37906 | 2026-02-18 04:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec63816d-0fb3-34c6-8d6e-ad3deabf3538 | -13.4963 | -46.70799 | 2026-02-18 04:27:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 48e221d1-58fb-3df7-89c6-e6ea1aed9410 | -13.01874 | -45.05277 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6fe1bbf6-4ff5-3fc8-85d1-77868f8a7ce4 | -15.38258 | -40.84349 | 2026-02-18 04:27:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 75b3199e-3ce7-3f44-810e-1e91597e8bbf | -14.36172 | -44.56144 | 2026-02-18 04:27:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17928c60-3f17-3983-8421-f1870dc2bb52 | -11.11682 | -46.605 | 2026-02-18 04:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 002656c2-97df-30a0-b472-527365a0d099 | -11.88518 | -45.27639 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16b21106-6644-3fd7-9f28-240336aedf93 | -11.89743 | -45.28566 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0748726a-6e24-39ac-824a-96ecc7f41570 | -11.88964 | -45.29171 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b5066b6-70ac-382f-8997-28c45ee406bd | -15.241 | -44.94501 | 2026-02-18 04:27:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 656bb60f-0a81-3ff6-ac9c-5c39dc01ef84 | -11.89298 | -45.29225 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0f75a22-2a6e-33e8-86e5-632cf3ba63cc | -11.88407 | -45.28351 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1afc710a-5647-3f97-934d-71b83390cb0b | -12.4783 | -44.50506 | 2026-02-18 04:27:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc99eb50-0c31-3b7b-b3ae-00c9afea3b38 | -14.511 | -43.77347 | 2026-02-18 04:27:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52858cf4-1f47-3e17-b801-4c5c224a9a55 | -13.02267 | -45.04965 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8147364-d020-317d-9a8f-35f8a908f1b4 | -11.85835 | -38.20497 | 2026-02-18 04:27:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 42b14e8f-2cfe-3090-992b-a7426f451ede | -10.7378 | -59.22029 | 2026-02-18 04:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c0bcd69-881d-32e1-9d7c-04cc9068b38f | -11.89409 | -45.28513 | 2026-02-18 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcec6338-43a8-3239-a6d8-03c92d78351e | -11.11625 | -46.60855 | 2026-02-18 04:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4dfec260-7303-342f-b520-7c147f1eb299 | -14.86346 | -46.40354 | 2026-02-18 04:27:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cf5190b5-e207-38a3-bb68-f8688999d280 | -15.59107 | -42.38978 | 2026-02-18 04:27:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13e35682-a3bf-39ed-b9dc-14c011e257b9 | -15.38207 | -40.84742 | 2026-02-18 04:27:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c22b3b5a-ea1c-3c4c-9a05-52a30c3f6d45 | -13.01818 | -45.05642 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f3b56c2-aac2-3a6c-be5a-4909194aa26d | -15.59195 | -42.38749 | 2026-02-18 04:27:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 914af718-9bff-3ef4-b498-ae6ad15ce757 | -12.81658 | -44.82582 | 2026-02-18 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3049e730-3918-3757-90cd-417b00a763e2 | -18.70051 | -54.98874 | 2026-02-18 04:29:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README5.md)
