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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03df2665-b15c-3d3e-b05c-0c8e8ea21a23 | -2.6966 | -57.5889 | 2026-09-19 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 27370c39-4e1a-3c02-9eb0-6e90e0e72926 | -8.7734 | -48.6651 | 2026-09-19 14:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 0ed20af6-1cb6-3b28-9bbd-2cd741f07c19 | -13.2222 | -51.7382 | 2026-09-19 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 62b2aafc-fea8-3964-b0fb-26dce3ba9aad | -7.7656 | -44.8688 | 2026-09-19 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 928b089c-0510-3c61-9410-886906f3eecf | -8.3365 | -50.8608 | 2026-09-19 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 1616688f-baa7-327b-a7e1-2aebe557944e | -11.3355 | -43.403 | 2026-09-19 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| be163a9c-5bc9-30b5-ae38-17fe9a3acb63 | -11.3817 | -44.0319 | 2026-09-19 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 03d5bd9c-c741-36f2-803a-d1030fd13859 | -4.5587 | -42.9523 | 2026-09-19 14:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 8c7ad8d6-f979-3b5d-b9e7-99f207ac6c2e | -12.2688 | -49.1907 | 2026-09-19 14:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 1fbaea4b-f8e8-3097-892d-7b568ceb812d | -8.1688 | -54.7432 | 2026-09-19 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 00b1c035-3f4d-3c83-b766-22716f132811 | -9.238 | -46.1894 | 2026-09-19 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| c62f582e-ea02-362c-9d60-0252fbe61965 | -11.155 | -42.7885 | 2026-09-19 14:50:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 122.9 |
| 9868a190-cbfe-358c-95f7-1f2690e11fae | -11.6798 | -54.446 | 2026-09-19 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| d8442700-39a0-301f-97a3-11d9f0dad5f6 | -11.3604 | -44.1521 | 2026-09-19 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| b5ba2e48-2099-35f3-92ce-05d70fcf2e06 | -11.8934 | -47.6322 | 2026-09-19 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 42fcd325-2d32-3a64-a4b5-bfd755525904 | -12.5949 | -49.1265 | 2026-09-19 14:50:00 | GOES-19 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 55ea5b0c-c638-3093-979d-022050035d68 | -6.3132 | -45.6076 | 2026-09-19 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 8ac0ec6c-41e8-32dd-bfbf-afe892150a1b | -10.911 | -53.984 | 2026-09-19 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 0c19f4d2-5519-3862-a4a5-a6284c617b21 | -3.1514 | -58.644 | 2026-09-19 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 09fe20e0-fe00-30f6-b680-c385374a321e | -12.5761 | -49.1071 | 2026-09-19 14:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 68fcc1d0-f916-31a3-b3be-382a4f350207 | -11.3237 | -44.0639 | 2026-09-19 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 014eab08-f330-39cd-bba7-28f77ecfc2cc | -1.2174 | -55.7302 | 2026-09-19 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 936b76b3-a645-3656-a6be-94569c694ab9 | -2.8975 | -57.7793 | 2026-09-19 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 2468731a-24e0-3a0c-b294-62e156f17f06 | -7.577 | -44.9098 | 2026-09-19 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 1faa1c75-a779-304a-b400-8bd2ae6eeb56 | -5.2335 | -47.5645 | 2026-09-19 14:50:00 | GOES-19 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 5fd9c4d3-55bd-33f1-a2c4-73fe253785aa | -5.5661 | -45.5491 | 2026-09-19 14:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 97e8a660-4f4b-3fa0-bdd1-c7cea833a38e | -7.8027 | -44.9108 | 2026-09-19 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 714068a1-e1ef-38f8-a085-ea3e529fc936 | -10.0956 | -48.4226 | 2026-09-19 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| e3bcd09d-37ca-3438-b8a9-8743da2056f8 | -2.0765 | -56.585 | 2026-09-19 14:50:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| bbaac94d-0f71-3473-a00e-be18ed245b4e | -2.8974 | -57.7987 | 2026-09-19 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 234.1 |
| 28738701-e9e2-33cb-8577-20d416753a34 | -10.9301 | -53.9618 | 2026-09-19 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| c9bfc52c-3c73-3694-a2d2-ce8c7f4d36f8 | -11.3621 | -44.0582 | 2026-09-19 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 51e8ed51-28d6-385e-8caf-4c90e61e9b5d | -10.932 | -50.8742 | 2026-09-19 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 47800bde-3bfc-34ae-826e-6ad544ddef31 | -10.5368 | -46.7343 | 2026-09-19 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 4c9fcb7b-75f4-3551-9e7d-29cce98e4673 | -12.2879 | -49.1883 | 2026-09-19 14:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 229.4 |
| b23cccc6-aa90-3846-a0b4-9810527af6ae | -8.7731 | -48.6868 | 2026-09-19 14:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 158.3 |
| b45926ea-72c2-3ac4-b764-5bc147324301 | -7.8843 | -47.6333 | 2026-09-19 14:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 415a471f-fe33-3098-b9b0-cc4357c57b4b | -10.9133 | -50.8549 | 2026-09-19 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 196.3 |
| c1cc2796-0238-3c3e-a2d5-8372251404e1 | -7.7118 | -44.6451 | 2026-09-19 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 419.0 |
| eede6f3a-8337-3f44-8c57-918bcd11d47d | -9.2606 | -45.9164 | 2026-09-19 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1e9560de-7f95-3959-8383-3ef834229de8 | -1.6396 | -55.1517 | 2026-09-19 14:50:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 75a548ae-3b90-30b4-91a8-456651e1d9b1 | -13.2414 | -51.7359 | 2026-09-19 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 894d02e2-cbf0-3657-91f8-93f09edee12e | -8.6173 | -54.5924 | 2026-09-19 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 58f10c52-7169-31f1-bd21-810f00298e73 | -9.0167 | -48.7505 | 2026-09-19 14:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 95.7 |
| d74873a6-7c1d-32af-860c-1c47f218c3aa | -11.0223 | -54.1379 | 2026-09-19 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| cadce812-6100-3c68-a338-1f9e8d4ff5d7 | -8.4503 | -45.8448 | 2026-09-19 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 31cce5ca-e84f-3793-a982-dea84d398724 | -9.0358 | -48.727 | 2026-09-19 14:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 897fe774-880e-3c5d-bfff-745654e864b4 | -6.941 | -55.0366 | 2026-09-19 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 3ae9cbc7-53fa-3943-af59-e1d12573eacf | -7.7844 | -44.8669 | 2026-09-19 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 2ef60aa0-bf1b-3e40-9bc7-97463eda2c39 | -7.026 | -42.0924 | 2026-09-19 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 137.4 |
| 316a95b0-5325-38a5-9a97-96ce524f922e | -10.567 | -51.3137 | 2026-09-19 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 9817f087-8f0f-3618-8894-0e85d21ff716 | -3.7534 | -40.2188 | 2026-09-19 14:50:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 127.0 |
| e8bc201d-4657-3873-9d44-fe9bec89a2a9 | -11.4912 | -47.7292 | 2026-09-19 14:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 97540955-beeb-3dc6-9c4b-96d512d7c73b | -7.7629 | -46.7389 | 2026-09-19 14:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 0ea7f042-b148-37b8-94ef-2e874eedf46a | -11.0065 | -48.3187 | 2026-09-19 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 6775b496-0a09-39a0-9e9a-df7243e12961 | -1.6583 | -54.9329 | 2026-09-19 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 51043744-012a-3cc9-8030-48237c306c13 | -2.9157 | -57.7983 | 2026-09-19 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 215.6 |
| 07c4f08a-ecb4-35c8-8dc9-908dc6c6bb0c | -10.7133 | -50.258 | 2026-09-19 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 130a37f9-800e-35cb-ba2e-9f533afa0b8a | -11.0226 | -54.1174 | 2026-09-19 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| dabe1ff5-16dd-32b5-a118-7b1153987fb7 | -11.8549 | -50.0437 | 2026-09-19 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 30ad9bc9-3e50-35fa-bab4-55f40c9906fd | -8.9412 | -44.3995 | 2026-09-19 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 192.1 |
| a0b59c46-25cb-3b2b-9f64-f3c8bc5440cb | -4.5772 | -42.9746 | 2026-09-19 14:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 6d083a20-238f-3012-a7b2-b039c82baa04 | -11.0062 | -48.3407 | 2026-09-19 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| a68c8e3b-6d78-3b60-9d5e-f3288e958c07 | -5.5663 | -45.5265 | 2026-09-19 14:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| bd92077b-cf02-37af-986c-b93f5664a2f8 | -13.0173 | -46.9352 | 2026-09-19 14:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 4833487a-8559-3cfe-8a11-4dea2f5bc645 | -7.8598 | -44.8595 | 2026-09-19 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 172.3 |
| bd8f2970-486f-3a51-8436-c602196cb410 | -1.5859 | -54.4153 | 2026-09-19 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b536a25c-2884-37aa-b0d4-6559d74d7dd6 | -5.7431 | -57.5814 | 2026-09-19 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 36aae766-aa31-363f-9ced-cc9dcb6927cd | -5.7756 | -47.2903 | 2026-09-19 14:50:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| ba21aa05-e2da-36a8-ba70-25536023ee85 | -10.7994 | -50.8881 | 2026-09-19 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 1469372c-f540-3eba-8ad8-fa3b6b01558e | -11.3359 | -43.3793 | 2026-09-19 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| a6499dbf-b595-37f3-ad26-9d5678dee0f4 | -8.4295 | -54.7464 | 2026-09-19 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 19a72471-901d-331a-80e8-7d05b8edf6ed | -6.4402 | -58.138 | 2026-09-19 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a15fb279-8289-3242-aa37-37bea1efddec | -12.1471 | -50.8668 | 2026-09-19 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 22efea19-2a0c-3083-9980-d70ef2a508e1 | -13.0173 | -46.9352 | 2026-09-19 15:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 0600c814-fd9d-3462-9836-27c0a8e1eb7d | -14.1347 | -45.171 | 2026-09-19 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 76c2ed15-619e-33df-813b-966b7d090676 | -7.6384 | -46.1254 | 2026-09-19 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| ef70b60c-c0ee-3b06-9f71-5bb21fd5960e | -2.458 | -57.9033 | 2026-09-19 15:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 9173c7c9-0694-34a2-9cfe-82726e80a718 | -13.884 | -47.9929 | 2026-09-19 15:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 9806f75f-2139-3ed1-ac5a-4752d3f9ce4b | -1.5859 | -54.4153 | 2026-09-19 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c31f19ac-0bd8-3634-a8a6-31646df6b2c2 | -10.913 | -50.8762 | 2026-09-19 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 281.8 |
| d921c4ef-63c0-3cf1-869a-1c053f7de8e2 | -7.0029 | -49.7551 | 2026-09-19 15:00:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| f636a62e-ad25-37a4-8fe3-5d29b76f02c7 | -7.7844 | -44.8669 | 2026-09-19 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 2931254d-a23a-3e78-84f0-6f64bb2dc566 | -10.567 | -51.3137 | 2026-09-19 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 154.4 |
| 6f860410-cd1c-3220-94d1-de627f691710 | -10.5364 | -46.7568 | 2026-09-19 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 3184a3d7-9c4d-3b28-834f-a38d7a2fcfe5 | -7.7626 | -46.7612 | 2026-09-19 15:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 335.2 |
| 8c4f9cf3-b4d9-32b6-b38a-c72143e50bda | -9.0096 | -44.9209 | 2026-09-19 15:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| cc818c1f-8d36-3a94-9775-029d78b622e1 | -9.257 | -46.1873 | 2026-09-19 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| e2c2bf40-f477-38ea-be80-b4a5e03260ea | -12.5949 | -49.1265 | 2026-09-19 15:00:00 | GOES-19 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 427d2134-29b7-3377-8b2a-0285933a4506 | -11.9303 | -50.0993 | 2026-09-19 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 9c1f5e42-ac62-36e9-826e-db7c43145c66 | -11.0223 | -54.1379 | 2026-09-19 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.8 |
| a8328986-d9e9-3e1f-b6eb-d2ad15acb463 | -8.1688 | -54.7432 | 2026-09-19 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 256.0 |
| d24ce715-b03f-3a19-9f2a-6c9c987aef77 | -6.4122 | -43.1662 | 2026-09-19 15:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 77be8b57-1f20-3848-aa43-1ae91d075786 | -4.4284 | -55.5043 | 2026-09-19 15:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| ce66710b-1de8-39ab-b701-5568aa4e0ace | -11.234 | -48.3571 | 2026-09-19 15:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 262.8 |
| 3a038cd4-eff6-3ba4-a480-f21afc5057d4 | -4.5772 | -42.9746 | 2026-09-19 15:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e72bea55-c7d3-3140-8d89-db9c41cfb072 | -11.3359 | -43.3793 | 2026-09-19 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 685cb11f-4f76-31ff-9df9-0e0b21a9def4 | -11.3609 | -44.1286 | 2026-09-19 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| e5671eee-d8c2-3687-a136-bd57e6891bea | -11.318 | -51.7218 | 2026-09-19 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 194.0 |
| 9c3ed21e-1337-3b5e-8d02-46bd6c33b9b9 | -11.9115 | -50.0801 | 2026-09-19 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |


[Clique aqui para ver as próximas entradas](README119.md)
