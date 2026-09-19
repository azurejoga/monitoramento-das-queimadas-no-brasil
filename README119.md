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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bbc7151-1c85-3f8d-9636-531ffb2e476b | -11.0845 | -49.4644 | 2026-09-19 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| c3fe50e9-4ae3-3a22-af6d-1f1ca3c80c63 | -11.0827 | -48.3095 | 2026-09-19 15:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 86dfae04-2d07-39ee-a87c-f9d93548b1b6 | -8.3771 | -45.6716 | 2026-09-19 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 197.6 |
| 7c150326-64e0-323b-84ee-1eedac115930 | -12.5761 | -49.1071 | 2026-09-19 15:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 222.9 |
| 92e0318c-291d-304d-ba97-9634f9edf3f4 | -11.0611 | -49.7693 | 2026-09-19 15:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 0bfb9987-28ed-3b5e-b019-54276f7d2164 | -8.7731 | -48.6868 | 2026-09-19 15:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 149.0 |
| a9f4ab93-8422-32f2-93f9-51670d724cd4 | -4.0089 | -41.2748 | 2026-09-19 15:00:00 | GOES-19 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 200.5 |
| f03294ec-ac0a-3933-aba2-574c40178cb0 | -7.6572 | -46.1237 | 2026-09-19 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 578b28ac-32fb-3f76-9d72-f5a1f9ec1527 | -5.3957 | -45.8522 | 2026-09-19 15:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 7f2c9387-690b-3d18-94a6-a20ba8ccebab | -11.1035 | -49.4623 | 2026-09-19 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 212.2 |
| d793e01a-b449-3514-bf32-6d5601703e41 | -6.9224 | -55.0376 | 2026-09-19 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 46521d0c-6ed5-3890-b3c9-b1a711434ada | -9.2606 | -45.9164 | 2026-09-19 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 206.9 |
| 8bf725a1-169f-3195-826a-5c10ee909411 | -2.8974 | -57.8181 | 2026-09-19 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 55712234-2bec-3833-a894-28e60d74daf9 | -11.9487 | -50.1402 | 2026-09-19 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 2733435d-705c-349b-91f6-032f83aa2fe2 | -8.4797 | -57.6282 | 2026-09-19 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 389743a0-9903-3e90-b7ab-3f50cd2d8cfc | -3.3183 | -57.8677 | 2026-09-19 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d0a9c516-6520-3cf2-bc63-1d0f339fb81c | -2.9157 | -57.7983 | 2026-09-19 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 211.4 |
| eff811d6-f71a-3d68-a460-78df15381890 | -8.6171 | -54.6126 | 2026-09-19 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| c0b80331-55fe-3564-ab12-300faab10f3c | -7.7118 | -44.6451 | 2026-09-19 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 298.9 |
| 90fd358f-1354-315a-ac55-9d655dc70bcc | -10.7715 | -46.3001 | 2026-09-19 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| e5acad77-84ae-3859-abc2-d3fe5422a607 | -11.4354 | -51.4563 | 2026-09-19 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.9 |
| f91779b1-7d92-3ee0-aa57-40895b62b2d8 | -7.5703 | -57.6962 | 2026-09-19 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ed959b76-3dcd-3e89-9d4e-9fde9ab394b6 | -11.0608 | -49.7909 | 2026-09-19 15:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 251d22df-590a-30c3-911f-420391ea6ef8 | -7.7847 | -44.8441 | 2026-09-19 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 98c9427d-cfbd-38a0-9f1c-c1bd3f9cca9e | -11.0226 | -54.1174 | 2026-09-19 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| a4fd1baa-585f-350e-864d-1dd5f0d97d85 | -8.411 | -54.7274 | 2026-09-19 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 9f3a613e-9d7f-3a1e-9349-14ee039b9f2b | -9.0167 | -48.7505 | 2026-09-19 15:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 43028cb6-c848-3a73-8085-7381529423c8 | -2.8975 | -57.7793 | 2026-09-19 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a62eaa09-b8d1-3f76-b153-96103b1d9892 | -8.7919 | -48.6851 | 2026-09-19 15:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 276.8 |
| efb3d59a-4dfd-3afe-944e-7953d843f8c2 | -10.9133 | -50.8549 | 2026-09-19 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 255.3 |
| 6364d3d2-4214-351f-8922-2a33f8fea56f | -12.6037 | -50.9405 | 2026-09-19 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 52df4ba3-be22-39ff-9e45-cad78779a941 | -8.3774 | -45.649 | 2026-09-19 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| f46a7375-ade7-3957-92bd-bd753f1a6883 | -11.3355 | -43.403 | 2026-09-19 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 556aaa08-18e6-3d02-afba-d502385d9110 | -8.9907 | -44.923 | 2026-09-19 15:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 45148f10-5bef-3d57-9d4f-cf8e611c1605 | -3.4638 | -58.213 | 2026-09-19 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e0687dfb-c8df-3bb7-8646-bfa499d64254 | -11.8549 | -50.0437 | 2026-09-19 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 6521f55b-cd80-3539-aa97-45c7ede2badd | -5.4142 | -45.8734 | 2026-09-19 15:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 18ab42a9-76b0-3fa9-95ad-5a9f84d02d85 | -11.949 | -50.1186 | 2026-09-19 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 7347077f-2269-3d97-b4ae-7ccc91e43a03 | -2.8791 | -57.799 | 2026-09-19 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 4a42ad90-65b7-32bd-8d73-b6a7ddea6ae0 | -7.7631 | -46.7167 | 2026-09-19 15:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 04188e82-b0d3-3b96-9706-377f8e342cdb | -10.9301 | -53.9618 | 2026-09-19 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 2d9c6e72-5552-3769-8a95-993299650e3f | -2.6783 | -57.5893 | 2026-09-19 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 287b293e-3341-33af-add6-db443a71a775 | -10.911 | -53.984 | 2026-09-19 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| e44a8397-a8b2-3c9a-8a55-4df79227f4e8 | -11.7823 | -49.8152 | 2026-09-19 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 6b91ddce-f212-33a5-b55b-de66d974f86c | -11.8746 | -47.6125 | 2026-09-19 15:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 153.4 |
| f19a8d34-c143-3285-a373-f5726285109a | -9.784 | -45.059 | 2026-09-19 15:00:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| ebc71b2c-7952-3b7c-a825-5f3e66b61576 | -7.8598 | -44.8595 | 2026-09-19 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 961af1c5-29d1-347c-949b-8cde7e67d2ec | -7.5704 | -57.6766 | 2026-09-19 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 2608855d-1df1-3790-aaf5-235d6b2b7485 | -5.3347 | -48.9857 | 2026-09-19 15:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 064db8bf-282b-3ff0-a23e-227251d6248f | -9.0358 | -48.727 | 2026-09-19 15:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 134.1 |
| f6b4756e-3fcd-3ef4-a2b0-ee9f6b24bce9 | -12.604 | -50.9191 | 2026-09-19 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 37fb9a05-86ad-3214-897a-b3f119b40d0d | -3.7311 | -60.6208 | 2026-09-19 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 71148e8b-51da-35c7-89af-2ea2d110df83 | -6.2034 | -45.3453 | 2026-09-19 15:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 9bb81a10-3bf4-3f1f-9443-f0ce767d141f | -10.5368 | -46.7343 | 2026-09-19 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 235.8 |
| c4ef0bc8-0433-37cd-a5ec-fe5aa85f998c | -11.9112 | -50.1016 | 2026-09-19 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 7bd94b2c-64b3-3e96-b5b9-9b27e1d3466d | -6.9393 | -43.0953 | 2026-09-19 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| dae91860-7fc0-34a4-9cb7-7e21f18ce3de | -7.7656 | -44.8688 | 2026-09-19 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 726276ca-4906-3270-96ff-8a7f24fed808 | -10.7991 | -50.9093 | 2026-09-19 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 93b514a3-d433-335b-8888-7fc616c15609 | -13.2417 | -51.7146 | 2026-09-19 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| bc077a23-f640-316e-a74e-7349dd6dc7c8 | -5.2335 | -47.5645 | 2026-09-19 15:00:00 | GOES-19 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4abb0e6d-91c6-36a8-8d1c-b65481033bad | -7.5888 | -57.6953 | 2026-09-19 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 547759d5-38b7-3eb9-999a-93e8a82f2030 | -7.7629 | -46.7389 | 2026-09-19 15:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 232.1 |
| e5c82170-f3c8-337d-8679-9ba587d232a9 | -13.2414 | -51.7359 | 2026-09-19 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 336.7 |
| 3189c287-4855-3ebb-8b1a-4ecc3696b137 | -13.3175 | -51.769 | 2026-09-19 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f452153a-1282-31d7-a65f-59b2d75a2b7f | -10.7133 | -50.258 | 2026-09-19 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 52e58012-b90d-3bc7-bff0-ecd2e82ce18b | -9.2567 | -46.2098 | 2026-09-19 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 306.4 |
| bf26b6aa-6a5e-369c-a59b-3c0febcfb832 | -10.5667 | -51.3349 | 2026-09-19 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 9c08d142-38e8-3273-a736-396d970a9276 | -9.0355 | -48.7487 | 2026-09-19 15:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 138.2 |
| a422679c-0358-3d61-9ecc-1a8f7814df9b | -10.932 | -50.8742 | 2026-09-19 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 217.8 |
| d4bf2f0d-1c26-3d52-9d13-a98010719702 | -5.7431 | -57.5814 | 2026-09-19 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8b2aaf68-5f42-335a-acf3-836fa4088961 | -11.8934 | -47.6322 | 2026-09-19 15:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 56ad4d03-721e-3b57-8ab0-a493dcf44e8b | -9.6087 | -45.3772 | 2026-09-19 15:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 40a3af91-c46c-3d71-b29c-23d8d1650f2d | -10.7994 | -50.8881 | 2026-09-19 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| cd533865-f249-3da3-b37f-0652cdd0d089 | -5.1439 | -55.9543 | 2026-09-19 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| bb06edf6-093b-3538-b215-b664da557b5e | -3.4272 | -58.1945 | 2026-09-19 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 6a85519f-ee87-327b-9d41-fe95887c64a8 | -3.1514 | -58.644 | 2026-09-19 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 784e2d17-0fa3-3a79-bc64-eb6766abac28 | -8.9412 | -44.3995 | 2026-09-19 15:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 124.9 |
| d79ed06a-94d4-32b5-aa78-8868fcdf3c30 | -8.7734 | -48.6651 | 2026-09-19 15:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 10dd6162-2bc6-3d1b-bc4f-cad993a6e072 | -11.3813 | -44.0554 | 2026-09-19 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 8a574c22-c717-3085-88ea-d6c30c9dfb8d | -13.6274 | -48.2988 | 2026-09-19 15:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 13da66d9-ebf7-37b5-be57-3880e856910f | -3.4462 | -57.9812 | 2026-09-19 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| dda7b232-cb40-3051-bf6a-e7a95e216ca7 | -9.6013 | -45.9003 | 2026-09-19 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 8f444dbc-6433-3a9f-936d-51df8c6a1247 | -13.2222 | -51.7382 | 2026-09-19 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 90650a1c-b23e-3506-8303-be2bc873c5c8 | -8.6173 | -54.5924 | 2026-09-19 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 02e28436-e15a-330c-9982-8bb2aab5ef32 | -8.3365 | -50.8608 | 2026-09-19 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ec31f740-cb4d-3d13-ae9d-4e46c4071fb3 | -1.6022 | -55.5682 | 2026-09-19 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 82067434-e01e-37d2-a2ed-a93fb2970a46 | -11.299 | -51.7238 | 2026-09-19 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 3955aa95-488b-3ad3-989a-0a6c2f4ea23a | -9.6202 | -45.8981 | 2026-09-19 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 224.5 |
| e9b66d49-ca83-340b-a168-764e9551494c | -8.45 | -45.8674 | 2026-09-19 15:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 8cb43f0a-c71f-35d6-8999-6a26e327fa58 | -2.8974 | -57.7987 | 2026-09-19 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 214.1 |
| 100dfb1f-55ae-3b38-99d7-a950d1b848a6 | -8.5986 | -44.5762 | 2026-09-19 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 8dbddda7-3f5a-3d27-bba7-ee637c4a4132 | -10.6703 | -50.6465 | 2026-09-19 15:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 349d9eb2-78cc-34a4-99ac-acdd2a490048 | -6.2585 | -41.6617 | 2026-09-19 15:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 42bf34bb-0f0a-3eca-9ce7-948344a22f42 | -12.0662 | -49.9321 | 2026-09-19 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| cdf1cd1a-2b00-3121-bdfe-0586360de0b4 | -10.0956 | -48.4226 | 2026-09-19 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 293.3 |
| 05d9e4b2-d090-300d-a540-be863f70c990 | -11.3604 | -44.1521 | 2026-09-19 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 9c38ba68-10e4-3fc0-bd87-8cb5cbeec193 | -11.3237 | -44.0639 | 2026-09-19 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 4283bee8-ad6c-3f69-a01a-2265bcca37f7 | -12.1969 | -50.1102 | 2026-09-19 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 7bfd7262-4264-368a-8be5-a8acbc043db5 | -9.2603 | -45.939 | 2026-09-19 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 23b1efa8-6395-347e-8f94-1886a0c59a35 | -9.6277 | -45.375 | 2026-09-19 15:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 153.4 |


[Clique aqui para ver as próximas entradas](README120.md)
