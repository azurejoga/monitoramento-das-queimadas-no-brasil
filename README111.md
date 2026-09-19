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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7224111b-e112-30fa-9a67-1a830d9fd42d | -9.0087 | -44.9897 | 2026-09-19 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| c041d057-de01-328b-b6a9-f9c9a715ab6f | -10.7133 | -50.258 | 2026-09-19 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| d75c1f0a-3bec-304f-9138-f59070ef3cdf | -12.027 | -50.0015 | 2026-09-19 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 267.6 |
| e41cedd9-997b-39c9-b7e4-78d6be9af965 | -3.3311 | -59.8101 | 2026-09-19 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 9dfd657b-40ee-3ec2-9f2e-f0ee149f8263 | -9.2603 | -45.939 | 2026-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 233.5 |
| 5b768382-badc-3e1e-829e-487b9b8642b1 | -9.0096 | -44.9209 | 2026-09-19 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 157.7 |
| c26f9306-e505-33d1-9ae4-988800130d98 | -4.5585 | -42.9758 | 2026-09-19 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 3b509086-0755-3fa7-9565-b5948ba2d7a9 | -7.5203 | -44.938 | 2026-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 049e321a-abd5-3c45-991a-33c3f55a2740 | -3.7128 | -60.6211 | 2026-09-19 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| cab287b7-2179-3741-867c-ab50f1a968a3 | -11.836 | -47.6398 | 2026-09-19 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ffcd3f30-8704-31d5-aae9-c9f8d25b078f | -9.2567 | -46.2098 | 2026-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 56b99af7-06f5-3e54-854d-985421e7721f | -7.4479 | -44.6934 | 2026-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| bbb024af-ca46-3849-96b4-994482ada1da | -8.6173 | -54.5924 | 2026-09-19 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 50819096-c8f0-3978-8bb9-3b050b785c8f | -7.7847 | -44.8441 | 2026-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| c92b5cd0-5ed8-3ceb-9cbd-e4efabdaec55 | -12.5761 | -49.1071 | 2026-09-19 13:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 91d97e0b-2e5c-3136-b78b-c9fc80207e02 | -10.955 | -50.5738 | 2026-09-19 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 5f9958ce-f9b9-319a-8f07-51cd4425d25a | -2.9157 | -57.7983 | 2026-09-19 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 7391947d-cd5c-303f-aedc-9241f9a0838a | -8.8639 | -45.937 | 2026-09-19 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 7bb8b969-606f-30fc-ac8b-97ae649b0b9c | -11.8746 | -47.6125 | 2026-09-19 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| d6a21d40-59b5-3c52-be97-6c041c702d73 | -11.8546 | -50.0653 | 2026-09-19 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 43b04f7f-f83c-3493-891b-c9efd52ca4de | -7.8598 | -44.8595 | 2026-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 56f56858-5ea9-3e1a-9e61-d1367dbfbe4b | -2.8974 | -57.7987 | 2026-09-19 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 224.0 |
| f8a5b8cc-d806-3c69-9ebb-02238acfcfb7 | -9.0358 | -48.727 | 2026-09-19 13:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 2ce14d02-9b52-3c36-b405-7a1e2af89994 | -12.5952 | -49.1046 | 2026-09-19 13:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 212.5 |
| b452054a-72ee-3abe-96c4-e5170be032ab | -12.1531 | -46.9707 | 2026-09-19 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| e73495f7-cdf8-3c2e-9ab6-d28988c5abd0 | -11.8549 | -50.0437 | 2026-09-19 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 4bacb0d1-1fbf-3667-8e7b-8731cdae7599 | -11.1038 | -49.4406 | 2026-09-19 13:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| d8ad2b89-769d-350d-b8c4-5493979a2281 | -10.7715 | -46.3001 | 2026-09-19 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| ec2d09ca-5067-3c19-9b09-c4eef8d8ad2e | -6.0196 | -51.7893 | 2026-09-19 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| f7e1577f-89fc-3bb6-a939-8ca301611f1f | -7.5391 | -44.9362 | 2026-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 135.5 |
| cf04020f-2568-3505-85a3-58a82845486c | -9.2414 | -45.9411 | 2026-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| c61a0c10-17e7-36f0-abb3-bf1dcbc4b75a | -11.8742 | -47.6348 | 2026-09-19 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 163bc10d-12d7-3b20-9d09-a1b391701f9b | -5.6408 | -43.392 | 2026-09-19 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 1161cfe8-c5c1-319c-90ee-15e5e19b1775 | -3.7129 | -60.6022 | 2026-09-19 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 5aea9a67-7127-3274-a1c5-2d031ec0dd33 | -11.083 | -48.2875 | 2026-09-19 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 4f2a39ec-e6c1-3243-8d1e-6524c2a604af | -7.0451 | -42.0666 | 2026-09-19 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 168.7 |
| 97e8154c-20df-3a7d-b77d-7ae812a5fe70 | -11.3355 | -43.403 | 2026-09-19 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 92fb6bee-957d-3ec3-b38d-a15614ae27d9 | -11.3813 | -44.0554 | 2026-09-19 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| b28d81fd-8116-3b52-bac1-aa629766cbe7 | -7.8595 | -44.8824 | 2026-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 9f9c2683-6da5-3ac9-8593-4e373666e812 | -12.1535 | -46.9482 | 2026-09-19 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 90d840f1-714d-3d37-8738-e73e2fe46bdc | -12.6896 | -45.94 | 2026-09-19 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| e1f9edf5-6c4d-30bb-91ac-af03e28cb5c9 | -8.4296 | -54.7262 | 2026-09-19 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 45930e42-63e0-312f-9303-ffa12344adb9 | -9.7501 | -46.0863 | 2026-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 86a88920-4456-3cbb-a957-08f7d796db7e | -12.1339 | -46.9734 | 2026-09-19 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 09a7ab68-f8ac-36d7-a469-a38984aaf1d5 | -3.3494 | -59.8097 | 2026-09-19 13:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 120.5 |
| cced7214-6151-3eb5-b6f9-9634b8f9bc5a | -11.155 | -42.7885 | 2026-09-19 13:50:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 141.2 |
| a31f4f13-eaef-361a-99ae-d180b5386478 | -11.0827 | -48.3095 | 2026-09-19 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| f700a64a-98d1-342e-b7bf-389c6e4c987c | -10.9133 | -50.8549 | 2026-09-19 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 72a6073f-8577-31d0-ac20-0cdafb3cad21 | -2.6966 | -57.6084 | 2026-09-19 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 1e1669ea-7feb-34b2-b85b-fb92b5143908 | -10.5364 | -46.7568 | 2026-09-19 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 4d796af7-b4ab-3542-8065-5e63bfcfb906 | -8.9907 | -44.923 | 2026-09-19 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| a58cded7-d1d1-3a2b-89f9-2f944df54feb | -6.0009 | -51.8111 | 2026-09-19 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d7278000-d830-3afe-8e09-c5553d9da49d | -5.6596 | -43.3906 | 2026-09-19 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 260ab3e8-3ea4-3ee0-b473-2b88191bd6d8 | -7.0262 | -42.0685 | 2026-09-19 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| d605f9fa-ee34-3473-af53-3ae4b6646a56 | -11.1035 | -49.4623 | 2026-09-19 13:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 0d2b5303-e7be-3729-8cc7-ae9539b66539 | -7.6087 | -45.4298 | 2026-09-19 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 9108c8f8-2a6d-39a1-8fe2-730a1a061643 | -7.0448 | -42.0906 | 2026-09-19 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 653.6 |
| 3b09e356-d267-31d5-aa5b-87ed3bb425f6 | -13.2414 | -51.7359 | 2026-09-19 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 5aa15094-58e0-38e2-94fe-5a2327c30160 | -3.331 | -59.8292 | 2026-09-19 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a89b3376-39c1-3c0e-bde2-866e7e6bdede | -8.45 | -45.8674 | 2026-09-19 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 82c014da-6003-334b-82ee-f45b32e8a853 | -12.4841 | -50.0532 | 2026-09-19 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 3d7f9fb1-5d3d-3083-9ebe-b0f36723e810 | -10.5368 | -46.7343 | 2026-09-19 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 842bc949-efe0-3b1a-afc3-fa625ba44a00 | -11.234 | -48.3571 | 2026-09-19 13:50:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 6a036d78-4ed3-336c-9e96-e0341ce06728 | -12.5032 | -50.0508 | 2026-09-19 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 803630c4-c230-3899-b43c-f9d1dd5c3f24 | -6.9224 | -55.0376 | 2026-09-19 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 437c2eee-d80d-3c50-8de3-08d32a8ac50c | -10.7133 | -50.258 | 2026-09-19 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| a3876212-082d-3328-81fe-ba953e8721a4 | -11.0801 | -49.7672 | 2026-09-19 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| ac3d9962-dcd8-3a3d-88cb-55341e8efd2c | -2.8974 | -57.8181 | 2026-09-19 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 94fea492-c35f-387e-b176-7fd2f957d91a | -11.3817 | -44.0319 | 2026-09-19 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| ddee9daa-a9dc-34a7-b008-eaa0a8e02f44 | -8.4503 | -45.8448 | 2026-09-19 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| ccaf5872-91d2-322b-af24-1fa95e8e9fd4 | -6.941 | -55.0366 | 2026-09-19 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a0a72588-6c5a-32e1-a2a7-0481adc77c20 | -12.7085 | -45.96 | 2026-09-19 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 261.1 |
| 28ef148a-f9a3-33c0-bf1b-9cc57571cb9c | -10.911 | -53.984 | 2026-09-19 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 45c68b7d-b1ad-3e3c-9e17-007ab678c96c | -8.7731 | -48.6868 | 2026-09-19 13:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 173.3 |
| 31bedb96-c9d4-32b7-8404-d0473c79f8b4 | -6.0194 | -51.81 | 2026-09-19 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| eb249ffb-7110-377c-925d-3f9803a586d9 | -5.9344 | -42.0966 | 2026-09-19 13:50:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 132.3 |
| 16693a81-1d37-3f46-9e3d-76ec5c69fed0 | -2.8791 | -57.799 | 2026-09-19 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 66608b46-e42c-394b-ba69-ba10d9593ce6 | -7.7629 | -46.7389 | 2026-09-19 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 329.2 |
| 058109b2-67ab-3903-a5bb-95f7aef84c4a | -10.567 | -51.3137 | 2026-09-19 13:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 4d6c15d6-00d7-3ca0-b9c0-631c7e5c07aa | -10.6703 | -50.6465 | 2026-09-19 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 24e62c16-2b31-36a7-b88b-220a5586cdc8 | -3.6946 | -60.6025 | 2026-09-19 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 44bb527f-8c35-37eb-9cca-55ff44e79df7 | -6.2582 | -41.6858 | 2026-09-19 13:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 431.8 |
| c124f67a-ecf0-3f9f-afd1-5aeb4665aa67 | -11.0611 | -49.7693 | 2026-09-19 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| dbd9fcaa-cd5b-3e45-9486-7558a128af14 | -13.2222 | -51.7382 | 2026-09-19 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 1a13faec-d774-36f0-bc76-a1fff2e8650d | -11.8934 | -47.6322 | 2026-09-19 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 4cc6a66f-47b5-3245-820e-2e1167d83d0e | -11.0065 | -48.3187 | 2026-09-19 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 954a95a6-5761-3fbd-b1a0-f4b46f05c9bc | -9.0355 | -48.7487 | 2026-09-19 13:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 86.5 |
| cad21372-0cfe-3d86-a352-f7ce2e455282 | -10.0956 | -48.4226 | 2026-09-19 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| ceb411cc-2d24-3d1f-b8a2-c4dccb0857a9 | -11.874 | -50.0415 | 2026-09-19 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| e29744fc-8512-3d71-ad1a-dc75c6208f8f | -7.026 | -42.0924 | 2026-09-19 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 405.3 |
| 31ca57a9-7051-348d-9459-9776ea60c8a4 | -8.7919 | -48.6851 | 2026-09-19 13:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 249.3 |
| ae3c7468-1195-36c2-b896-884af107c4b5 | -7.7626 | -46.7612 | 2026-09-19 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 181.0 |
| f223fbec-11d6-34ee-935b-5e4f306f55ed | -2.8975 | -57.7793 | 2026-09-19 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 19293dc8-76fc-3f00-866f-00981ac7574d | -6.2585 | -41.6617 | 2026-09-19 13:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 330.3 |
| 870c0484-b8c1-3bff-90c9-fd9891587731 | -11.1369 | -54.0251 | 2026-09-19 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 353.5 |
| f190a2aa-aaf8-3b39-96c7-ded7a4db2702 | -8.411 | -54.7274 | 2026-09-19 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| fcf8e3be-2f13-3dde-886e-db4cfac4a09e | -7.0451 | -42.0666 | 2026-09-19 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 144.5 |
| 18b051de-63b7-346e-ab33-47939873ac7a | -10.6703 | -50.6465 | 2026-09-19 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 170.2 |
| fd10f74c-8830-391d-933d-91f9bd516ffd | -6.4667 | -45.2116 | 2026-09-19 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 61790213-dcd2-36b0-9e64-a964e472d90c | -11.8937 | -47.6099 | 2026-09-19 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |


[Clique aqui para ver as próximas entradas](README112.md)
