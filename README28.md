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
| 7473b6e4-10a7-32bb-a023-8404e0f28a05 | -8.4714 | -44.49799 | 2026-09-20 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 821fe9d4-0bf0-3587-bdfe-b88cad071f98 | -8.17204 | -54.7545 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bae4f3c-7fc0-3ee8-a45d-a35da77a3aa1 | -8.84554 | -44.92349 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c7f7e67-ba0d-312b-80bc-cb0c1fc58dee | -8.76972 | -48.72307 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39f5b169-35c6-3584-ad33-01ab6b8419ba | -7.74883 | -46.76775 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd02b505-440a-3db1-8684-cbbae213bacd | -11.65726 | -43.42746 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01b76239-0b1f-3e06-8f8f-4967c909057e | -9.01583 | -51.42284 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f39d6ec4-4167-3cca-b766-11084f4163f8 | -5.23424 | -47.58492 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e981bba-d25a-38e4-b9b3-d825a1bbc2ae | -10.4819 | -46.29078 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15af837a-cd2c-3aa1-83d3-357da8605a65 | -6.30797 | -41.7561 | 2026-09-20 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 23980148-de17-3c5f-ae73-169c044b8906 | -9.01205 | -44.98181 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca3f831e-9b94-329b-bb97-5e33f49dfe2f | -6.96877 | -42.57979 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e5b2d35c-f682-3100-95f9-dc90738de540 | -10.28244 | -50.26346 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9a477bf5-af91-3aa8-ab60-2f07b4708be3 | -8.17988 | -54.73767 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bcf1af23-e2c7-334a-bd05-527e85e608ec | -8.14173 | -46.80688 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8b06195-fcb1-31b8-bf84-8455975a46f1 | -4.31939 | -46.41998 | 2026-09-20 04:19:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56af81c9-48de-357f-9f54-acf7cf9fd52b | -9.82494 | -46.44296 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f459dd50-3278-35f5-b3df-27efc5078a68 | -10.3106 | -50.21865 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 81eba898-9c64-3f23-be82-f49c60e73c3d | -9.39613 | -40.30697 | 2026-09-20 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 017606b7-e5f0-3ac0-a3fd-035489ffba21 | -7.75129 | -49.19844 | 2026-09-20 04:19:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a6d7b96-7225-38ef-9b42-86d69c97bc0a | -9.39956 | -40.30751 | 2026-09-20 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 82f616c8-d2bd-318a-bb5a-089560f0afc7 | -7.84389 | -44.90934 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eba1c022-e6f2-369b-8631-b2bfb8bc962d | -8.97045 | -44.66622 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bdf7cbc-1b7f-3cc4-acc9-ab903e61d9c0 | -6.32372 | -47.62946 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 586a260b-c19b-355e-a82f-34507413ac8f | -7.84028 | -44.90877 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d8aec8c-7422-356c-9bb1-025388377a6d | -11.48476 | -47.76312 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50eea1ad-7a3f-38e8-9a0b-d680fc47e996 | -8.26108 | -50.86142 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42836ec5-8bbd-359f-bec7-e745b6381590 | -6.99216 | -49.8079 | 2026-09-20 04:19:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3698b579-3cc6-356b-a358-ae7ffb5636fc | -12.01103 | -44.68515 | 2026-09-20 04:19:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6945fdd0-abd4-385d-86e1-b8da4677f74a | -5.73265 | -53.45601 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 682dda4f-0db8-3312-a54c-b0bd5932d34e | -7.16267 | -47.46556 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d21b6833-2db0-3adb-9089-b1ba9d9a8c2c | -6.91414 | -42.89988 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 07cc52cd-06ac-3a98-8cb7-0d434d720109 | -8.75707 | -48.66484 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 925e2da0-21ca-37e0-b3e6-fa3131301374 | -8.16739 | -54.77809 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3afa7981-762e-3c24-b9f9-05de672f8d11 | -8.18425 | -54.76297 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bcaac42a-3555-3f95-bca0-0164bf389d2d | -9.76627 | -46.04125 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0f4818b-3429-3575-be04-92ad92eb4118 | -10.46992 | -45.0939 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b11d1523-f3de-30d9-9868-f7707f103a1a | -7.57436 | -46.30624 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bcfcd6e3-d046-32ea-8bea-d8c4e0c0bc5e | -8.16767 | -54.74148 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94ae3f4c-17a3-3508-9e20-198799e771f5 | -7.58605 | -43.435 | 2026-09-20 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0de82089-8cc2-3c37-a60d-7fbd6fb16694 | -11.21541 | -48.35993 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7bb31b4-cf05-3c95-afa7-b43b187f29b2 | -5.85384 | -53.52442 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56bfdd01-3401-3cd9-8eb3-54edd9577cbe | -11.09325 | -48.29339 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cb65e760-f1df-3f22-b2f5-800b518e6251 | -5.84095 | -53.52199 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 919112ea-2bff-3cc9-96ea-e44e6eae3721 | -6.48218 | -43.56859 | 2026-09-20 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6e705da-77c0-33e8-97c3-b23e50e081d0 | -5.45498 | -44.31901 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce6b5c2e-cdac-3c4e-8b24-3eef194eb2ed | -5.34896 | -44.82829 | 2026-09-20 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a7eb2c8-5a97-35f2-90e0-4d7968a760ec | -8.61645 | -54.59605 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fba4cd27-1b83-3238-9eac-1df946de1090 | -9.96627 | -46.54725 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b548f0de-e6ac-39c8-b3b2-fadf7e7e18c4 | -10.30864 | -50.2695 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e102aed8-6b18-3fac-8860-e63e604117c9 | -9.81363 | -48.32765 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 331510d7-1c5a-3de4-8854-3a920b1497ff | -9.60789 | -45.3725 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7e70ab1-19e6-3bc6-976d-0681b7abc9c7 | -5.46382 | -47.66497 | 2026-09-20 04:19:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8107f97d-4a57-3560-ab30-398b85025dc2 | -7.45063 | -44.73438 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b83a420-fcdd-3c48-8ed5-5f26f8b94944 | -7.31487 | -55.62126 | 2026-09-20 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af9d47eb-65ff-3b8d-aa0d-4125c15f7a17 | -10.27956 | -50.25173 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f78fcf20-9216-3f8d-9787-f371099df97a | -7.40859 | -46.61949 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e7c99b8-d2a5-3a14-883e-650c38264486 | -5.79147 | -51.86098 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 559dd03d-ce7d-3970-ae57-1cec2e169c9d | -5.84171 | -53.55497 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 113a5d80-a971-3dc2-b556-fdae5303f468 | -6.92541 | -42.90134 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8f88629d-ad8c-3be2-9b46-8c88a509e96a | -8.16985 | -54.75399 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 463396e2-285d-31e4-8eb4-988a91870e26 | -6.3612 | -43.36158 | 2026-09-20 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 686ea8c2-4b33-3056-b19e-f7c471d54597 | -10.1012 | -45.65821 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d364e2f6-b593-3412-8439-ede12e64e199 | -9.96244 | -46.54654 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21f54d03-f4f5-3927-9e39-cfac7be15baf | -9.72391 | -47.21412 | 2026-09-20 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a84a13ee-d084-36bd-a0c5-2537fef1be19 | -9.77379 | -45.07 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ba900b5-ae5e-3597-a957-0dcbb8f07e99 | -6.98425 | -45.80753 | 2026-09-20 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b00a34e6-864b-3c09-8e99-2b252c7fb130 | -8.37114 | -47.1943 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59db1c26-ddc0-3839-ad7c-ba5bcc4fa46a | -11.08586 | -48.3108 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3f0a154-402f-3875-952a-ed6ed18c6163 | -8.8691 | -45.94828 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 027facdc-4611-315b-b406-00d718b0d574 | -9.27827 | -48.24937 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47b8c95b-dd89-394b-bd2f-9ff94aa2136e | -5.28994 | -49.34342 | 2026-09-20 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4697fab-6f98-380b-92f5-209f70dc16fe | -6.60354 | -45.53315 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97099440-61ad-3f8d-93cc-7b010e96728c | -5.65522 | -43.36924 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93f2ec1d-1113-3639-a5a8-72af044e3e3a | -5.80208 | -42.5428 | 2026-09-20 04:19:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2370db2a-afd8-346d-befc-7201119c9e0b | -9.37652 | -45.37064 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70f849f9-2125-3115-a43d-5356f577142b | -8.50466 | -47.43092 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e816e83e-f52e-3dfa-9a55-23649f6614e1 | -6.75553 | -47.91861 | 2026-09-20 04:19:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf0ada9e-b362-3a6c-bd1c-4bda2ceabc16 | -5.41069 | -44.27382 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a73937b3-b141-3b17-bdc7-6c0ac01c04b9 | -5.8474 | -53.52321 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72fe944d-8cb3-3229-88fd-10dcb2639d24 | -7.55875 | -45.41422 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42178107-3802-390e-8d06-75b9b9c2e808 | -9.78167 | -46.08598 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71fe0b39-170f-3606-b08e-3a844e6fb926 | -4.07443 | -52.12054 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87c9a686-d75c-31ca-95cb-6f91582ea3d9 | -7.1301 | -42.07645 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 017c7556-f251-3923-b32d-79f632bcfe88 | -8.72754 | -44.87014 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc2842ee-ca6d-30c0-aa4f-21a6ee827079 | -10.77773 | -46.32441 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c5dadae-4a3a-321d-89df-2ff3a0169e52 | -10.30378 | -50.26859 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| b9ece2eb-25a8-32cb-b2ff-6523a608d354 | -10.54979 | -46.74941 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e5acaeb-81d9-3d22-aa43-e394a38cd792 | -5.83715 | -53.54316 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee8e2e9e-5101-3967-a159-ce80ea1ed40d | -8.15798 | -54.82579 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 042faf89-20d6-3769-bf57-182883c28b6c | -9.01135 | -44.98601 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3660e7dc-a7ed-38f4-bfcf-8ea2cf929b32 | -11.24059 | -48.38927 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 390b4241-1e5e-3367-90ae-83b739446aa9 | -7.62373 | -45.42344 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02542df3-a407-3d40-9149-5987a294a919 | -9.56916 | -45.46991 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a95b3992-9a58-396c-96ae-471fc32e14b6 | -10.13671 | -47.68258 | 2026-09-20 04:19:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6df16c8-2f7e-3e9c-9803-bebbe8ca8a3a | -6.33843 | -43.88197 | 2026-09-20 04:19:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08e25a87-9ac0-305b-b765-2ef6286598ef | -10.31389 | -50.21482 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 026e1024-276c-39e2-9c4f-a35d573c99c8 | -9.21378 | -46.21682 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dab635fe-190d-3919-a6a5-2880d2bd57b6 | -6.9682 | -42.58332 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 94038986-b037-3fc1-98ca-346bd1c2fbac | -9.79737 | -48.31938 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README29.md)
