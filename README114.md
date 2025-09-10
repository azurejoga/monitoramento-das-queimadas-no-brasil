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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4faccfae-15f1-36ba-9f4b-da1a402b648a | -6.8521 | -47.9143 | 2025-09-10 14:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 24da8da5-760f-3e1e-983c-c3c5a2ccfb4a | -6.3808 | -44.4205 | 2025-09-10 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| be904460-b32c-3e44-ac7c-01973f4d9c7e | -6.3993 | -44.4419 | 2025-09-10 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 42544819-2a15-3530-8347-eb1e85d44a07 | -9.0756 | -47.0558 | 2025-09-10 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 0475992d-136f-344b-9f70-794fa0f3b4d5 | -11.9535 | -51.081 | 2025-09-10 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 229.8 |
| d08391e4-6a65-3afe-8e2f-949de60efe29 | -8.7549 | -47.0885 | 2025-09-10 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 8bbe6d60-7480-3994-8938-163c4365cc16 | -15.1378 | -52.3826 | 2025-09-10 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 3ef92405-4404-3133-95bf-5e2e9ae9f468 | -9.8838 | -50.1719 | 2025-09-10 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 4ad5e693-55dd-38ea-a8ae-cdaff4489e68 | -11.1187 | -48.4369 | 2025-09-10 14:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| cae51212-3484-3767-b757-057da3823579 | -12.1803 | -53.863 | 2025-09-10 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 3784345d-9097-3e70-814e-5fd1b83bb168 | -6.8895 | -47.9115 | 2025-09-10 14:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 187.4 |
| e4bfef7a-0945-3728-9283-692589fddff9 | -8.0794 | -48.6407 | 2025-09-10 14:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 171.7 |
| adee50f5-43e5-3170-9c3c-ee979a041780 | -11.4648 | -43.6668 | 2025-09-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 327.0 |
| 111ad379-d2d7-3306-b923-5338fd5607c8 | -9.6821 | -46.8791 | 2025-09-10 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 430cb497-a16a-385b-a9bf-c3b7ee696342 | -9.7223 | -48.0907 | 2025-09-10 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ab753f53-078f-30c8-b99d-fd3f69a8e4ad | -7.522 | -48.2318 | 2025-09-10 14:20:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 166.8 |
| e0d1125f-877d-31dd-84cb-d5fcebd73185 | -6.204 | -43.3241 | 2025-09-10 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 628b1184-df1c-3c0c-bd51-a7206784a8dd | -9.8649 | -50.1737 | 2025-09-10 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 1ae2d47a-0462-3af9-b31f-ff676eaa11f5 | -15.1374 | -52.4039 | 2025-09-10 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 797.0 |
| 2de00a36-91c5-38c5-89c7-db19d7687b7b | -10.7369 | -46.0785 | 2025-09-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 598.8 |
| 0725776d-8db9-3339-a44f-d3fa7ccc0e3d | -8.994 | -46.0808 | 2025-09-10 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 9fc7cba1-e5ac-387e-9cd9-1b41f686f7bc | -7.4639 | -44.9433 | 2025-09-10 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 3e250c28-440a-3e6e-9c3b-545cae45a7f2 | -12.9477 | -54.793 | 2025-09-10 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| dcbd3386-5fd8-3751-9f0f-c20c58d1f19b | -11.4469 | -43.5988 | 2025-09-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 273.2 |
| 8e710a23-70c5-3e27-b145-25a484642b64 | -6.2597 | -43.3895 | 2025-09-10 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 42f8a456-5dbc-390d-a570-15358579d9f1 | -8.0416 | -48.6656 | 2025-09-10 14:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 675b2430-2153-3142-a2f2-a7843be48b38 | -11.4281 | -43.578 | 2025-09-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 79a30fb7-d599-37d4-92be-1fae89badddd | -8.9943 | -46.0583 | 2025-09-10 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| c795cfee-f8a9-34db-81f3-6fd7beb323e2 | -11.7602 | -46.4621 | 2025-09-10 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 240.8 |
| 9a669426-14c3-3fd2-97fc-bf8594556ed0 | -14.907 | -55.8546 | 2025-09-10 14:20:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 55e2adf3-1dd2-3e49-a6c8-d094eca74ee4 | -13.1367 | -54.9171 | 2025-09-10 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 50bc83b0-77f4-3087-8d6f-b505f181d414 | -7.5546 | -45.2307 | 2025-09-10 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| c1ed2294-d016-3712-bd88-87e9b7dd03ac | -12.9474 | -54.8135 | 2025-09-10 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| d001dea2-01f3-3300-9367-c78cc3abed36 | -15.2683 | -53.8012 | 2025-09-10 14:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e6cf8e8c-bd31-3e4a-9070-379b7ad186f9 | -5.5702 | -42.9062 | 2025-09-10 14:20:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| d32822f9-8a99-3ad5-95de-dec36053c375 | -15.1569 | -52.4013 | 2025-09-10 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 276.1 |
| be52e344-1f70-3de1-841f-5f6579e96b39 | -9.7589 | -51.1383 | 2025-09-10 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 75ed839c-28c5-35ca-8722-4ffca56a01d2 | -6.2043 | -43.3008 | 2025-09-10 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| ef38271c-75cc-3687-9e55-ad60d2e5a27a | -11.4097 | -43.5336 | 2025-09-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 9e8a7358-2de2-309b-8e6e-832b92b1c547 | -10.7373 | -46.0558 | 2025-09-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 346.5 |
| 434cd839-5ce4-3ec1-9a8b-bc270aa6aa3b | -14.9067 | -55.8751 | 2025-09-10 14:20:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 6927a8fd-d90d-34a3-82c2-626decab1576 | -6.8897 | -47.8897 | 2025-09-10 14:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 4cea3d09-0bec-3601-b13b-c4de0e9da482 | -13.1176 | -54.9191 | 2025-09-10 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 92580782-c225-3548-9d18-939365a852a0 | -9.8646 | -50.1951 | 2025-09-10 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 8921421b-1e35-30e4-8737-bf7ee44ac75a | -9.1142 | -46.9851 | 2025-09-10 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| d69f267c-6850-3513-895c-6c1d88a3d6dc | -5.9002 | -45.7955 | 2025-09-10 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 6b591541-e2d4-38a5-8b73-315e2bf81110 | -12.5796 | -44.6412 | 2025-09-10 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| a9dd73c0-dd87-3947-92c9-facd903f1dff | -11.4657 | -43.6195 | 2025-09-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 523.1 |
| e7d58c12-4dee-3964-819c-f81803d9ef08 | -15.655 | -53.8771 | 2025-09-10 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 1a8c138f-2d56-3e31-bd70-23b96962b919 | -12.1993 | -53.8611 | 2025-09-10 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 1e510a3b-9bab-3bac-9675-b163d6b94116 | -7.5033 | -48.2334 | 2025-09-10 14:20:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 10f05d0a-0615-397b-8736-dc7cfca6224e | -11.3905 | -43.5365 | 2025-09-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 285.8 |
| 2f258720-9ed2-3177-8cb6-58724f998e98 | -9.0957 | -46.9648 | 2025-09-10 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| fa1ef5f3-455e-33c0-9879-f6e64ed89ae1 | -5.6738 | -43.9 | 2025-09-10 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ecf6ba27-e2f2-33c4-a876-f326e9aef144 | -19.282 | -47.9946 | 2025-09-10 14:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 135.3 |
| b45b5cca-08f1-39a9-9415-83daedfea598 | -8.7361 | -47.0904 | 2025-09-10 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| e2b2720b-43f5-3b1e-a61b-5cdc936c8756 | -3.9883 | -44.4872 | 2025-09-10 14:20:00 | GOES-19 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e8f932d7-fcd8-39d3-ae00-0724ad205f11 | -9.325 | -46.74 | 2025-09-10 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 189.0 |
| dbee8de5-45e5-362e-8220-6294c2f9d73c | -14.7542 | -45.3156 | 2025-09-10 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 494527ef-6308-3d30-90c0-e929c427f235 | -6.2407 | -43.4144 | 2025-09-10 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 7ac34262-441f-398f-9079-c4826bae8539 | -9.7011 | -46.877 | 2025-09-10 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 5976e0a0-20e7-3f58-8dcb-4ba23f6abc6a | -13.1364 | -54.9376 | 2025-09-10 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| bdb80c31-a2e0-306c-a860-2b68fadede87 | -9.7599 | -45.4048 | 2025-09-10 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| daa84ff6-1ab4-3bbf-9f37-92ba09de4f2b | -6.2409 | -43.3911 | 2025-09-10 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 22ecfe8a-f97c-346a-9eec-3cfe6f0a4902 | -6.6198 | -53.3576 | 2025-09-10 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 81d5bc6e-cb0a-3a4d-8800-8b4897863e99 | -5.397 | -43.4332 | 2025-09-10 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 3fb520b3-c64f-37a1-b1cf-b55002c70a81 | -9.0132 | -46.0563 | 2025-09-10 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 4df3863b-b790-3830-a395-f8a6ac385f44 | -7.5594 | -48.2288 | 2025-09-10 14:20:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 177.6 |
| b9b97f43-b120-39d4-a82e-530b0e2ad33c | -9.7591 | -51.1172 | 2025-09-10 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 179.9 |
| f5d4b302-cb9e-308c-b142-9935b3c15085 | -9.3437 | -46.7603 | 2025-09-10 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 144.6 |
| ba5c895c-ab5d-36e2-afe0-30e730ce8f45 | -11.4452 | -43.6934 | 2025-09-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 265.1 |
| 79a7f8db-2c9b-3862-abc6-6cd59166a64c | -9.0579 | -46.9688 | 2025-09-10 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 533bf533-8297-3b80-835a-a5e53cbb9774 | -12.1889 | -50.6267 | 2025-09-10 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| b72c96bf-c9d1-35e4-841a-027d703f0dbf | -15.1021 | -50.1249 | 2025-09-10 14:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 8ceb6617-c306-3ec1-b04e-75d16f7b1607 | -6.1616 | -45.8214 | 2025-09-10 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 42c583b1-b607-3839-8a6f-0907b98ecca5 | -6.1896 | -41.0398 | 2025-09-10 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 177.3 |
| 5205b81d-5a28-33ef-a886-343335d523df | -14.3882 | -53.2826 | 2025-09-10 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| fd94c52c-91e2-3a9d-8123-688b95333ad8 | -7.7439 | -50.316 | 2025-09-10 14:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 63e5d0b3-671b-337f-98ed-d3d1f114156c | -11.4702 | -50.3461 | 2025-09-10 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| fe7ccef6-1549-308c-abc7-c481590d464a | -11.2196 | -54.9975 | 2025-09-10 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 1d9f852c-49d1-3e46-861e-ed5224c3c37a | -6.8519 | -47.9361 | 2025-09-10 14:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 46dded95-c2ea-3114-9e9c-4a7c08611142 | -6.3806 | -44.4434 | 2025-09-10 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 232.0 |
| 46fd2ebe-6232-34a0-a728-4716012f3d8b | -15.2686 | -53.7801 | 2025-09-10 14:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| c3e1094b-3204-3361-8cef-532adb5a5796 | -11.1245 | -52.0359 | 2025-09-10 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 353.2 |
| 3d71ae93-d513-3719-b53f-de2ea86a1e1a | -11.4652 | -43.6432 | 2025-09-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 409.6 |
| 6e1d6cee-a6f4-3391-bda0-ad329c3ac26f | -14.4816 | -53.4598 | 2025-09-10 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 045f2a34-dee5-3709-b02e-52c2a2bcacc4 | -14.8877 | -55.8567 | 2025-09-10 14:20:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3d4cc27e-ffd5-3155-851e-84590229d054 | -11.3389 | -46.5419 | 2025-09-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 5f703bfd-9f8e-342e-bf7d-3355d4c808b4 | -15.2881 | -53.7777 | 2025-09-10 14:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 0258523c-3fde-36df-ab2b-3adac016b852 | -9.0768 | -46.9668 | 2025-09-10 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| e0a7117b-3da1-3106-9d71-fc4c87911ee7 | -11.2834 | -46.4365 | 2025-09-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 7c4372f6-1563-3258-bdc9-7b186cc9f614 | -14.4054 | -53.4063 | 2025-09-10 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e6b9c013-cc44-337f-aa38-fb4b2a117407 | -7.5218 | -48.2536 | 2025-09-10 14:20:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 276.7 |
| b863bdcf-721b-3833-8729-7d36e950a6f6 | -6.2595 | -43.4129 | 2025-09-10 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 227.2 |
| bf5a7394-966a-3313-8a57-2d500173e207 | -10.0155 | -51.7031 | 2025-09-10 14:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 2bf12ec7-865b-30c6-a501-90b8457acac9 | -15.2877 | -53.7987 | 2025-09-10 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 146.4 |
| dca242d7-48b9-363e-8ce4-4e6cca4b2c06 | -6.3804 | -44.4664 | 2025-09-10 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 968dd2c2-ae33-3c8b-9223-0c86d9de70cb | -9.8835 | -50.1933 | 2025-09-10 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 4bbbb36a-b70c-39ba-a5f9-e6562d6abf99 | -11.1247 | -52.0149 | 2025-09-10 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 279.9 |
| 4af9a7b9-c9f8-3ac6-aa1f-8413deb8d108 | -6.2085 | -41.0381 | 2025-09-10 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |


[Clique aqui para ver as próximas entradas](README115.md)
