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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9003032-af9a-3ee1-b0f2-8bccec4def09 | -11.8627 | -46.0622 | 2026-09-02 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| fc897c2c-5b7f-3f09-86ec-c5b55e53f4be | -11.8244 | -46.0676 | 2026-09-02 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 206d6854-6f03-3758-af7a-dd18208e7707 | -11.8623 | -46.085 | 2026-09-02 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 986aeeea-9d0a-323e-a2e5-802e10100cb2 | -11.8435 | -46.0649 | 2026-09-02 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 300.1 |
| 203c2b60-1de3-385e-a630-8a14eaa39dbc | -11.8431 | -46.0877 | 2026-09-02 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 1c1e7de5-5aee-3dc6-8232-4c1bc4896f33 | -11.677 | -50.4939 | 2026-09-02 11:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 12d6e8a1-11ec-3764-b0a1-de758e38b527 | -11.8435 | -46.0649 | 2026-09-02 11:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 447.0 |
| 1999f006-c2a9-3cf4-a9d7-3a1ada874f2a | -11.8435 | -46.0649 | 2026-09-02 11:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 418.3 |
| 5c688950-c052-3fd1-bc1b-41de78603187 | -11.8439 | -46.0421 | 2026-09-02 11:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| b8d41dae-5735-361a-91cb-adddb48c367b | -11.8244 | -46.0676 | 2026-09-02 11:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 4388053f-8a02-3170-b92b-9a3e5c22c99a | -11.677 | -50.4939 | 2026-09-02 11:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| a24453d5-4798-3782-8952-99cb767521a2 | -11.87 | -46.08 | 2026-09-02 11:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 999ef195-a119-38e7-8645-d5ada9b8c7c4 | -11.84 | -46.07 | 2026-09-02 11:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ebe4871-48b0-3fc7-aecd-ef7cf9c90099 | -11.677 | -50.4939 | 2026-09-02 11:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 5fcfed31-36dd-3e10-a40e-5b8d7b244867 | -11.3767 | -45.423 | 2026-09-02 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| e2f995d9-2399-34cd-88c5-d58a614f20f7 | -8.4671 | -54.7035 | 2026-09-02 11:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| c1535cbb-b468-31a3-b19f-755f72dd50ff | -10.4145 | -49.9898 | 2026-09-02 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 4aec0fa4-5b60-391b-8012-30de0b8163f0 | -11.8435 | -46.0649 | 2026-09-02 11:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 197.5 |
| a97d2b36-9518-3a90-a0f3-dce3ca5094bc | -11.0557 | -51.5173 | 2026-09-02 11:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| b5c223e4-912b-39e9-a2f5-0a95d36dcb2c | -11.3579 | -45.4027 | 2026-09-02 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e215b31e-3549-3500-9130-be0a1c46a05e | -11.677 | -50.4939 | 2026-09-02 11:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| b7a0c1ff-4e51-39f3-ba01-3699b98a67e1 | -11.3767 | -45.423 | 2026-09-02 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 700cd026-3c25-3940-9267-9bf2a9fdbddb | -11.6773 | -50.4724 | 2026-09-02 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 1bd49533-1ddf-33ff-bc6e-342bdb51c377 | -8.1112 | -54.9483 | 2026-09-02 11:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 3e3432c8-ca86-3d04-83b0-bb7229bb4548 | -11.3579 | -45.4027 | 2026-09-02 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 87d9bd12-71ac-3b35-8541-2517f20fa742 | -8.4671 | -54.7035 | 2026-09-02 11:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 8a47cead-c7bd-3a05-b7e8-49223196aed6 | -10.3196 | -50.0211 | 2026-09-02 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 55e1d5ae-bd13-3b61-b85b-a552b33900ac | -11.8435 | -46.0649 | 2026-09-02 11:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| ba272cda-479d-3adf-b7de-0742aefbf29e | -11.677 | -50.4939 | 2026-09-02 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 3bea4d89-d036-3699-9b07-8b2e28bb5c98 | -3.0601 | -48.74841 | 2026-09-02 11:49:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 77326afa-17b1-3fae-9ddf-e21801a39048 | -5.73005 | -38.57425 | 2026-09-02 11:49:00 | TERRA_M-M | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 660dd346-31cb-3c2d-859f-fd02b9329159 | -7.29711 | -49.80905 | 2026-09-02 11:49:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c28ee95a-a7d9-315a-8799-c87d44ec3f67 | -3.24647 | -47.24929 | 2026-09-02 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cf4935e3-db95-3d4f-adec-971be2e4a301 | -8.41597 | -44.97562 | 2026-09-02 11:49:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9b1b00e8-0319-3ab9-9d9c-b42917cf7e5f | -1.33188 | -47.80078 | 2026-09-02 11:49:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 744b6f98-69b2-3ee8-8082-999de74a1e80 | -5.08228 | -48.47511 | 2026-09-02 11:49:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e4c8bc9f-68ba-3404-9a9d-fad69bbc8e39 | -2.49198 | -47.11343 | 2026-09-02 11:49:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bf4c36c1-790b-3165-9832-4da14a709316 | -3.85342 | -44.05442 | 2026-09-02 11:49:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 0d8c3630-65ca-3ad6-9f14-69c71cfc0fb0 | -5.50833 | -49.80098 | 2026-09-02 11:49:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 25050a36-0a56-3855-bab0-52bf44f8d5fd | -4.37071 | -47.77249 | 2026-09-02 11:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 584ba878-d2bc-3264-977b-d4448026c05b | -7.44586 | -48.25914 | 2026-09-02 11:49:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| de1f725d-9ff8-3839-8e89-1aa783ef698d | -7.22999 | -42.74509 | 2026-09-02 11:49:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 88f8ef5d-2a05-3bd9-89e0-d94c1a7ff8cf | -6.67291 | -43.41453 | 2026-09-02 11:49:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0dced360-6d67-3038-8c8f-b0472017bfa7 | -6.6749 | -43.39931 | 2026-09-02 11:49:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d43cad18-bde8-3794-a019-52589e94c332 | -5.08355 | -48.46625 | 2026-09-02 11:49:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 868ac50f-1691-3778-907e-ce90d897c011 | -7.29575 | -49.81845 | 2026-09-02 11:49:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6a78c103-906b-3f4e-9189-2f1497544bab | -5.71987 | -38.5795 | 2026-09-02 11:49:00 | TERRA_M-M | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 44.4 |
| a4124aac-0bbb-3fb8-b15d-2090c7e94b69 | -3.06142 | -48.7393 | 2026-09-02 11:49:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 15c67d86-c1c7-3c67-935f-982143d33c4e | -1.33062 | -47.80963 | 2026-09-02 11:49:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 109a8b4d-10da-3d00-8f37-9bd908dc4e45 | -3.24437 | -47.90882 | 2026-09-02 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ee59ef4-55d0-3108-afd3-bd82fc5ddebf | -7.52328 | -47.32778 | 2026-09-02 11:49:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9f6e28b3-e022-325f-acab-bb872aac45de | -1.57647 | -47.70945 | 2026-09-02 11:49:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4b7366d1-1624-32d1-9971-a98d00e10f82 | -3.23764 | -47.24808 | 2026-09-02 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1b854210-4ded-300c-8aba-2fc324e6e9af | -7.07768 | -44.35812 | 2026-09-02 11:49:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0a131de1-86e9-3d8a-b822-9eb07646311c | 0.1681 | -51.51927 | 2026-09-02 11:49:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c02fdc3a-0476-36dd-899e-02e4df4fec40 | -4.11853 | -51.02726 | 2026-09-02 11:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 663a5e7b-eef7-3b39-a1a8-04194668219d | -3.25194 | -47.91882 | 2026-09-02 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| adc07151-5c78-32ea-98a2-2c2faa5e1c5e | -8.68829 | -39.58643 | 2026-09-02 11:49:00 | TERRA_M-M | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 104444dc-53fd-3689-a73d-9fafa5669f6d | -7.44713 | -48.2503 | 2026-09-02 11:49:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cda07cf4-904e-320d-9d5f-7f092952ea7b | -7.25467 | -47.53158 | 2026-09-02 11:49:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c00d8b7a-de8b-3327-b4e7-91b098f0c316 | -3.84312 | -44.05291 | 2026-09-02 11:49:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f1fa96ff-3469-3621-936f-b6cad0cd19ff | -1.17355 | -48.13667 | 2026-09-02 11:49:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 62a23b29-ee92-3825-8814-732eb7e10f0d | -3.2532 | -47.91004 | 2026-09-02 11:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| e6f40518-ffea-3c86-8b35-aaa0b98ced1c | -2.5008 | -47.11466 | 2026-09-02 11:49:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e5dcc394-fadc-3291-9fdf-543828378f14 | -8.4673 | -54.6833 | 2026-09-02 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 282.5 |
| ed647200-32a8-392c-b4c8-eebf0e3dd690 | -10.4145 | -49.9898 | 2026-09-02 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 41e5373c-b345-3e68-a064-44569e83307f | -9.423 | -37.8286 | 2026-09-02 11:50:00 | GOES-19 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 105.7 |
| 644512b4-841a-3bcb-9f4f-e883d2b5f4cf | -11.677 | -50.4939 | 2026-09-02 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 5519944d-1214-382a-ac1b-ca07e11c8076 | -8.4858 | -54.7023 | 2026-09-02 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 8e15bd98-a2e9-357f-b6a9-b9590a6912bd | -8.4669 | -54.7237 | 2026-09-02 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| e5d5bb92-3824-352d-8f84-78e239a89cf1 | -8.4485 | -54.7048 | 2026-09-02 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| db919e1d-1997-3eb8-ad5b-2dd75ba602f5 | -11.3579 | -45.4027 | 2026-09-02 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| c153746f-8d65-3743-85e5-cb2821284b2a | -11.3767 | -45.423 | 2026-09-02 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| d8fe168c-07e0-3020-bf8b-c9aec49fa5f8 | -8.4671 | -54.7035 | 2026-09-02 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 396.4 |
| ade05b51-a6e6-339e-a8b8-8e9dc1714b7d | -11.5483 | -45.4446 | 2026-09-02 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| b8aae8f6-5a3c-386c-af42-73f664c1aa74 | -10.95581 | -50.46458 | 2026-09-02 11:51:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 74de1d5e-27db-3ad2-9eb0-ea1ee35345d6 | -10.77412 | -44.74283 | 2026-09-02 11:51:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 7b281481-b7b7-3cb7-ae74-512bccefe674 | -11.67084 | -50.49677 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| dd9e5a6e-f923-35fe-a52a-f783bb508b7f | -10.42451 | -49.99459 | 2026-09-02 11:51:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 8b37e869-a238-33bf-8c66-93a66481e439 | -12.37326 | -48.15313 | 2026-09-02 11:51:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 60c33f36-6547-36f9-96f9-a899bd3381b4 | -12.96494 | -43.24448 | 2026-09-02 11:51:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 11d3e2eb-133d-308c-8ac7-119b366b9b3c | -10.09056 | -46.73621 | 2026-09-02 11:51:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0923dc50-cb53-39f2-9204-d00b9cb6c2e4 | -11.3571 | -50.62191 | 2026-09-02 11:51:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6aeb5d84-94ea-30e9-b4ab-706c235d938c | -12.12925 | -47.0527 | 2026-09-02 11:51:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1dc2e5ea-51a8-3d1c-97b0-361671fd9d91 | -9.70552 | -47.20451 | 2026-09-02 11:51:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| a88baee0-f773-38ce-b8ed-f73940ebc825 | -11.65426 | -50.48485 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 78962f4e-311a-3a66-96b6-fb7e429bbbc2 | -11.47863 | -45.08427 | 2026-09-02 11:51:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7b8cf7e7-5d38-3692-bcf2-78a3e5fd5822 | -10.05514 | -46.67328 | 2026-09-02 11:51:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3a83a6f5-6402-314d-8a7c-79375340d7ae | -12.1103 | -47.0501 | 2026-09-02 11:51:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2b664d95-bc5d-386d-b3a5-99c28c64b921 | -11.86155 | -46.08539 | 2026-09-02 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 412.5 |
| ff62233e-31e1-38c7-b7ad-02083e5b67ca | -9.66775 | -48.27061 | 2026-09-02 11:51:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e7a59a3e-e754-30e7-9113-7693e399094a | -11.30596 | -45.17186 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 2e6f7cea-19f8-3568-b96a-a623c2044cc7 | -11.09837 | -51.56016 | 2026-09-02 11:51:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 2bc181f6-bbdf-3167-8138-118738d7b02e | -10.30787 | -50.03678 | 2026-09-02 11:51:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 77b63a49-5285-36b7-a31c-3b16e4b7cd4e | -10.78317 | -44.75811 | 2026-09-02 11:51:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 89b7d5bb-c2dc-381d-9336-1e6a6e7b8ba5 | -11.67982 | -50.4981 | 2026-09-02 11:51:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 0f90825a-0808-39ed-b92f-3b0924c59ade | -10.78725 | -44.75088 | 2026-09-02 11:51:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f34d930d-410e-3765-9f7b-e8de9cdbf068 | -10.41559 | -49.99329 | 2026-09-02 11:51:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 12d1072e-dc31-3f74-9977-6abd8baa5153 | -9.66902 | -48.26155 | 2026-09-02 11:51:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ad0add16-4f62-3b5d-9e9a-ac1081bcaf86 | -14.11641 | -45.50125 | 2026-09-02 11:51:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |


[Clique aqui para ver as próximas entradas](README69.md)
