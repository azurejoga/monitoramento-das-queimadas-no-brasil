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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5af5d88-7e34-36a6-ba97-b0a22bd061fc | -6.82773 | -52.79772 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3a70149-6b16-3223-b6b3-948acf4e19d0 | -3.31831 | -48.72519 | 2025-09-11 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdcf0fb7-f046-3557-807b-5c9311658f58 | -7.92526 | -44.88234 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da0c70fc-68db-3f4a-bcc5-7b564632ddb9 | -6.31886 | -43.44619 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 20895174-9824-38b4-b90d-58991ac02a47 | -8.62907 | -47.1686 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7ece306-f837-3550-8eaa-e364310ea50d | -7.0834 | -45.34826 | 2025-09-11 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 07b9cef9-bb7d-3922-97ec-9b36d3dca281 | -7.46886 | -45.28096 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39f69745-e5cd-3888-b2ad-7bff0a1d2fc8 | -8.03378 | -48.65666 | 2025-09-11 04:21:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 660b6660-2bb3-3dde-9508-89843ca9e42b | -5.66946 | -43.33283 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 660c4f2a-1502-39df-bbbe-cf5696b19af0 | -8.4205 | -47.27236 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48a9cc32-8a71-3fcb-9ea6-4c708e20f7f8 | -8.5171 | -45.69203 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 96df5f5a-8586-332a-b944-77e25bc53cda | -5.73061 | -45.28016 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f06cc6f9-79c8-38d3-b4e5-80a0a030976b | -6.49207 | -44.49056 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdcf4f57-dcbc-3daf-af00-5eca90e4d06d | -5.22932 | -46.0932 | 2025-09-11 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff0f6943-8691-36c8-a941-3034f7e5caf2 | -5.5779 | -45.62157 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d258943-550c-3292-a8b8-d3a3556e1cb3 | -5.5229 | -42.68415 | 2025-09-11 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b777166b-551e-34f5-ad41-66084164af26 | -7.26195 | -44.90569 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 905f35e5-ab07-35ef-b346-6f40ae0d0a8b | -2.74021 | -48.6834 | 2025-09-11 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf600859-d804-3690-bf03-b5584cd1052f | -6.30539 | -45.66351 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50d9a240-04e7-39ad-99d8-3e8b81070c97 | -5.59917 | -45.36014 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 018169a0-fd85-399a-af82-6638c8ca9210 | -7.94368 | -44.88855 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c650609-3ef3-3fc5-884f-552e7459fefb | -5.73005 | -45.28367 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7730c984-402b-3fd1-b880-371c8140a9cc | -2.64825 | -45.96851 | 2025-09-11 04:21:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e9d4671-6c3d-36ab-8104-08a7f21f94d9 | -5.87968 | -45.61772 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b721f550-e981-38f8-8432-d8d469104359 | -8.51099 | -45.68743 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e45c4558-f86f-379e-87c2-9474eebbea0c | -3.6356 | -49.20523 | 2025-09-11 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6872a77-e727-30f6-a77e-150821264fcc | -5.56033 | -43.78871 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 573f8400-c9f7-3d3d-ad11-49e8a449e0d3 | -9.04914 | -45.73123 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e9d914b-bb9f-3614-8289-982f582ebc09 | -7.50058 | -48.24672 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a20d4353-c9f3-3f48-badb-627554e801f7 | -6.54293 | -43.10712 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6346239-9707-3171-9bf5-00669e7d39e9 | -8.13839 | -49.51599 | 2025-09-11 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 631b311d-9a5c-3e38-b3f6-c41e3173460e | -7.91166 | -46.85057 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5e2b4b0-87fc-3678-a0fc-435f9a34799a | -6.19062 | -45.6523 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca260bf5-cea1-3aa6-b87b-7a933f08e38d | -8.09134 | -48.22024 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05f8eab7-f6ab-3716-a24a-5d91b6c61f94 | -6.19405 | -43.39824 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f81a275-9cd2-3e7b-8721-f7b049974435 | -5.69685 | -45.32873 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97106284-0939-3500-bf6a-404d77e61239 | -6.44148 | -44.77443 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1930e12f-514c-3eb8-b917-250e2d596702 | -6.39229 | -43.5158 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aeedc1e8-8b2b-3455-a075-65caa0fac0c3 | -5.86346 | -44.21046 | 2025-09-11 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fffa0b06-c522-3283-99f6-8dbd8f062b28 | -6.19827 | -45.6577 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43d7d89e-840d-3204-a721-0393f3ec038c | -6.723 | -46.42571 | 2025-09-11 04:21:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4d3f2e11-ab2a-3f07-af88-6b085d110a6a | -5.73783 | -45.29933 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c4b32c9-be2e-3379-8a01-7c23ecc1b28f | -6.37654 | -45.1634 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc6c50ce-db1d-3320-80d1-52a9cedcb3f6 | -8.75293 | -47.11472 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e67a9007-e533-3d19-aaf9-1a85abcac675 | -6.40944 | -44.50258 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c20f6287-006f-31f1-9ce4-1143b4316344 | -8.50824 | -45.6618 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c7ff080-42ae-3a28-9e44-d7d3eec11965 | -7.1045 | -43.88497 | 2025-09-11 04:21:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42c8c4c3-deca-3d8b-bade-2f26e3e0039d | -6.09199 | -44.77927 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c26e5d6-9848-3582-92f5-f050b12c9e66 | -7.23537 | -44.47306 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 465271a9-938d-31aa-a815-84f3b5baba3e | -5.47083 | -43.42873 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| caf436d5-c4ba-3cbf-ab09-0521f5d77fe6 | -7.48106 | -45.29008 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33874b68-a72b-3dc2-86ba-008ed35773a4 | -5.73785 | -45.27771 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4746b74f-50eb-317e-b59d-f43351214ded | -4.05699 | -44.08234 | 2025-09-11 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36cd45a3-2983-3205-9967-89bb72749a05 | -6.41718 | -44.49675 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15ee34ab-2a89-3b2d-9989-0691ff346642 | -7.50284 | -48.27798 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd579781-de60-3f05-8e63-3d31893eebb4 | -8.03557 | -44.49883 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de3919b1-988d-3548-a6c4-af40fd1ed20b | -6.6843 | -44.54224 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74c297f7-5c74-3c91-b9c7-5cf09b5fd8e2 | -5.72839 | -49.22126 | 2025-09-11 04:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b2277c8-983b-33b9-a486-05d966c415cc | -6.20091 | -43.53057 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19279f14-599b-3eea-820d-35d6ff16d602 | -7.48162 | -45.28659 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21d650ca-e6c3-31d4-a5f4-e877ca266830 | -7.99022 | -45.79552 | 2025-09-11 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21ae49b4-13b3-36e9-b39c-3d381c88d8ec | -6.4013 | -42.60094 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 39922cf6-832a-36cf-b173-55abea3940c5 | -5.67839 | -45.46678 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93d59e1c-f37b-3365-a398-3744cc304dd1 | -5.08021 | -41.15327 | 2025-09-11 04:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 644575ca-724b-33ae-a186-546f2b212dc5 | -6.49876 | -45.26145 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b68d5be-1ea3-30d4-9564-598757f41998 | -6.56626 | -44.21357 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f4cb284a-af35-32b4-8259-fa3892a51845 | -6.31686 | -42.21334 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 01743d2e-259d-35a3-8bd8-4af2c6351627 | -7.08361 | -44.85196 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cec5cb8f-e822-32f4-ae5f-36ea63f60794 | -7.46942 | -45.27747 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db82b096-075c-3b12-b549-8fcad5975993 | -7.19386 | -44.96977 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a1e625c-bfd6-3fb4-ae1b-9cef7fe1f535 | -6.23276 | -46.15612 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72e5cd0f-b930-3ae8-bfff-10c03b219ea4 | -7.92581 | -44.87885 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f980d9f3-b74a-3eb5-a050-aa3199d24922 | -8.16976 | -46.07147 | 2025-09-11 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1dd79c6-8475-3d2c-be93-c1b9fa6a63e2 | -7.54874 | -42.53207 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 86c3b53c-88de-3f04-9d5c-98dc44c6975a | -5.72933 | -45.41696 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6134b41a-5d55-3bdd-9fcd-aaef5559da24 | -7.3931 | -47.37647 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 966d246a-55bc-3ba0-9ee5-a65d7f76510b | -5.77002 | -45.52851 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5af0ff45-cc0a-3f8b-b78b-36cb64fbbe94 | -7.10781 | -47.84286 | 2025-09-11 04:21:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e976d58-ab99-3101-8de2-0ff9427ec70e | -5.42591 | -43.41838 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 793ab212-9baa-37bb-b0d1-6ecde61a1940 | -7.31545 | -49.61919 | 2025-09-11 04:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36f40ba9-711a-31c7-a9fd-b30b887e6f09 | -6.30672 | -44.91977 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 875d6abe-90d9-3215-86f3-55f559fa0966 | -7.86546 | -47.98182 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9128f6d8-efd8-3f07-9b63-84a1f19ea20e | -5.42646 | -43.41484 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20ec5071-84a4-318d-8516-68958d42af8e | -5.65094 | -43.9029 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31135bbe-068f-3ba0-9290-385f6635975e | -5.9355 | -45.72145 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfe54ffc-7325-3f45-8fcf-7a8c5c1f0928 | -6.0973 | -45.93397 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b2f5fec-9c36-39d2-aa80-6aa40426cf4a | -7.49913 | -48.25528 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0831254-afb9-3aae-a81e-13ae40cc4406 | -5.51374 | -45.45173 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d77c105-5ee4-3c6b-bc9d-a4c5924957cd | -5.55423 | -43.04668 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19290104-4e3e-3555-8513-7f551762a616 | -7.69947 | -45.14999 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21de7320-ae87-3886-b416-a1023623c2ca | -8.01967 | -48.64968 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68446a60-8203-3dcb-a53e-1a28ba9a3245 | -6.1707 | -41.07605 | 2025-09-11 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2cd3448f-e55c-3761-8b95-43036bf8e359 | -8.52155 | -45.68553 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf435389-835d-393e-8f60-2f408c85f2b8 | -8.08039 | -50.18502 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c871833a-23d2-3cd6-b645-22a66bf02a78 | -7.80459 | -41.24666 | 2025-09-11 04:21:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9303aa0b-c3a2-3ba8-90c4-4c23a4419ff4 | -5.39517 | -42.63089 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f1404e24-69ce-3e65-a280-0a4107fe469b | -4.55977 | -43.74305 | 2025-09-11 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 089649d1-144f-3ba8-8749-d342b56bf9f2 | -6.34878 | -45.1877 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35198f67-4391-3b86-ac1d-cfe7f8ca87df | -6.9071 | -47.90679 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4723696-3e4f-30d9-95a4-4efdeca5dea2 | -8.1035 | -49.25115 | 2025-09-11 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README51.md)
