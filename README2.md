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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a1444da-1418-3bbf-844a-d53baefb5e5b | -9.2358 | -48.589401 | 2025-07-30 00:02:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7dddbbf3-6907-3973-bf29-ae5e2e9f9d80 | -7.2107 | -43.103298 | 2025-07-30 00:02:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f5afcd6-a0ab-38bf-a9c2-a5952fb952a0 | -7.0959 | -44.3666 | 2025-07-30 00:02:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d3d91f2-43dd-35ab-b06b-d05fac496abc | -7.1568 | -44.043701 | 2025-07-30 00:02:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 93693a04-bf80-3d55-8f64-92290eb2866d | -9.1501 | -49.830601 | 2025-07-30 00:02:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c212c39-0573-32fa-8ee3-ffb0f5af9780 | -6.3986 | -53.3265 | 2025-07-30 00:02:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 005bcb70-ffe2-3b2d-a4cb-19f91eab9075 | -9.0535 | -45.059399 | 2025-07-30 00:02:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| be5f3b30-0795-3651-bf67-e45baedcdf51 | -7.8689 | -47.8573 | 2025-07-30 00:02:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a51b8f32-7d52-3f84-ade3-008811f6c4cf | -4.2962 | -48.054501 | 2025-07-30 00:02:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc0c5166-bd3d-32b6-8578-bfde61129f1e | -12.8135 | -43.0826 | 2025-07-30 00:02:00 | METOP-B | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aa4b8514-1f60-3592-aaab-2107bf290ff5 | -13.8807 | -43.805801 | 2025-07-30 00:02:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 152f2724-004b-312a-bc86-075ff8e96fcc | -10.0968 | -46.960499 | 2025-07-30 00:02:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9fdf715-1dd0-368e-86af-5d7a798bb93d | -7.0635 | -44.9547 | 2025-07-30 00:02:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46d3167a-5627-3e93-8aef-0a5dd44faa57 | -3.4958 | -49.034302 | 2025-07-30 00:02:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 122614fb-6d72-3edb-bcf5-561c77df224b | -13.0729 | -47.370201 | 2025-07-30 00:02:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3d05cc4-96e3-3de2-8179-d7068dbb394b | -11.3497 | -51.225399 | 2025-07-30 00:02:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 976e67ae-9ab5-35c4-811d-444abcd18072 | -12.4591 | -44.0793 | 2025-07-30 00:02:00 | METOP-B | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| af35698b-3978-3727-9dc4-b8125ec9e445 | -8.5166 | -43.3144 | 2025-07-30 00:02:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e3cd8bc4-96b3-32e4-b696-f58ace1c623f | -9.1478 | -49.819901 | 2025-07-30 00:02:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca8a155b-5f26-3136-9bfb-594cf451e0dd | -4.6494 | -43.124599 | 2025-07-30 00:02:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78835f7e-2d4a-3fd7-9a7f-146434f6e7f0 | -9.1892 | -43.144901 | 2025-07-30 00:02:00 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 25de06d6-bdf9-320d-8496-dc61fef1f899 | -10.5173 | -44.884602 | 2025-07-30 00:02:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c84feca0-132a-34bd-965c-0b0b4052c3be | -9.1909 | -43.1521 | 2025-07-30 00:02:00 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 51e6d182-ae31-3a4d-b7ac-444a9ebcb6d1 | -8.6258 | -45.497002 | 2025-07-30 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2821acd7-9a65-3ebb-ae8e-3a4489e7d2bd | -10.7024 | -48.8512 | 2025-07-30 00:02:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f82d2d03-b2b5-37a0-8a2f-0748eb30872d | -9.4035 | -45.477901 | 2025-07-30 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cc143c7b-d3e8-33d6-93da-543e0d7362d5 | -2.9064 | -48.2794 | 2025-07-30 00:02:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 851e29a4-0568-3718-ac23-788b1fbb3e65 | -6.0251 | -47.550999 | 2025-07-30 00:02:00 | METOP-B | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a3f9f59-b7ff-39e2-9472-b62e5abbf17f | -11.9859 | -46.6814 | 2025-07-30 00:02:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f124a86-b916-32c7-ae95-9242e15e76fd | -11.9957 | -46.679298 | 2025-07-30 00:02:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1ccbe99-3259-3a2e-b168-3e71ebf93cf3 | -9.2699 | -50.208801 | 2025-07-30 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a50068f-c43e-37b8-8084-5b44f8f9bcc2 | -9.1696 | -49.8265 | 2025-07-30 00:02:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a6654c8-338b-3665-a080-276a67d62006 | -10.4654 | -46.7183 | 2025-07-30 00:02:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0fe2e91-4a91-3e6b-b376-6d9573372d88 | -3.1865 | -48.798599 | 2025-07-30 00:02:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9b97a1e-315a-3d0f-b66f-e1a0eadb67f8 | -6.396 | -44.7351 | 2025-07-30 00:02:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80c37c10-c5ee-324e-be13-be76108dcf82 | -13.7899 | -40.0653 | 2025-07-30 00:02:00 | METOP-B | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc92eee6-1a65-3712-a4e6-86e129b267d5 | -3.6841 | -42.193501 | 2025-07-30 00:02:00 | METOP-B | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f7276db0-cee6-3e84-b522-0eba81369c3b | -4.8434 | -42.981701 | 2025-07-30 00:02:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8738a41-b49e-3da1-be74-b2192c74c56c | -11.9876 | -46.6894 | 2025-07-30 00:02:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65333bf9-972e-3e25-bb1d-ee3f2c990264 | -7.9479 | -44.078899 | 2025-07-30 00:02:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 817cb710-6dd7-3e7a-9257-41e2992c6b39 | -8.9488 | -46.732498 | 2025-07-30 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19a32176-4ed0-3dd7-b8ec-1d7e2dd0b45f | -16.694099 | -41.0042 | 2025-07-30 00:02:00 | METOP-B | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0371f154-34d2-375b-bc06-297dba7250d8 | -3.5884 | -47.508301 | 2025-07-30 00:02:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2e3c898-a8e8-3b0c-b485-a51efe800ad6 | -4.8234 | -42.8946 | 2025-07-30 00:02:00 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8c7edc97-dbef-3f97-91b7-235bab7bb5f1 | -9.0551 | -45.066399 | 2025-07-30 00:02:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d643e35-a17c-3be8-b471-334935690da1 | -6.1313 | -44.429699 | 2025-07-30 00:02:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e307fd38-5d68-3019-b685-944bc292b8c8 | -4.3869 | -49.022301 | 2025-07-30 00:02:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 451bf75c-4d19-3f0c-913e-3c3405135999 | -10.9638 | -44.484402 | 2025-07-30 00:02:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 553da063-3945-366b-9d50-5abee24a69ab | -2.9095 | -48.247398 | 2025-07-30 00:02:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d424a0b-16c5-3e6e-ad3c-d130694b0539 | -7.1536 | -44.029598 | 2025-07-30 00:02:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a42c9ffb-69df-32b4-b70a-798b4a98278d | -2.9081 | -48.2869 | 2025-07-30 00:02:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38d70086-f00d-3ba7-86a1-34e03c27ee0c | -12.5493 | -44.722599 | 2025-07-30 00:02:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 942671f5-cac5-3f3e-8d54-dc504c8d7ae9 | -9.1576 | -49.817799 | 2025-07-30 00:02:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78bfc1d7-b16b-3316-8c61-93e39883eb31 | -3.5039 | -43.251202 | 2025-07-30 00:02:00 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3b62a52-9192-3b6b-a72a-2a5d885f1f89 | -12.4607 | -44.0863 | 2025-07-30 00:02:00 | METOP-B | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b44793f9-1d3d-3e34-a716-e4fe06dd11d3 | -2.916 | -48.230202 | 2025-07-30 00:02:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1525ba7a-aebe-3353-81cf-25db0d0cd642 | -8.024 | -47.673302 | 2025-07-30 00:02:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50ade155-cbe1-31ab-af7e-dc54523dd6e3 | -7.8594 | -46.7314 | 2025-07-30 00:02:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0b20d18-24c3-3213-86e9-7a4404076bc3 | -9.6344 | -43.835899 | 2025-07-30 00:02:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8056aac8-2f3a-390c-a9d9-d08eeeb0300f | -10.7102 | -48.839199 | 2025-07-30 00:02:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a9ac507-fa69-3a1e-90cd-201a628dab8a | -7.8707 | -47.865299 | 2025-07-30 00:02:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf6e83f1-f455-3adb-89d4-d0effb3ab971 | -7.7803 | -44.982101 | 2025-07-30 00:02:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9d779201-b095-3618-83e7-55128c5f8d95 | -10.1327 | -46.936401 | 2025-07-30 00:02:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16ff15fa-753a-33d9-b71b-b1330043a375 | -7.2269 | -43.0839 | 2025-07-30 00:02:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 02d1d1b3-37e2-3a43-9958-b8476a40caec | -7.3406 | -43.763599 | 2025-07-30 00:02:00 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 949ac273-4af0-3d02-a035-f3f3546df58a | -8.6377 | -45.876301 | 2025-07-30 00:02:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c72e59be-3e7c-33d5-b2f4-ffa9bebd2754 | -13.5365 | -45.6306 | 2025-07-30 00:02:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e022f434-9c39-3dd2-afb1-8a370f179da5 | -7.9365 | -44.0742 | 2025-07-30 00:02:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0a2ff3bf-889c-395b-9e1b-d41f414b01dc | -12.4792 | -47.271198 | 2025-07-30 00:02:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f626543-44ec-37ee-a617-d3ae40866d2b | -10.6157 | -45.2374 | 2025-07-30 00:02:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2ddc1b3-ba34-3288-80d0-b30af2d18929 | -4.8252 | -42.902599 | 2025-07-30 00:02:00 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 71676491-b757-3b37-8241-2fa02830bad8 | -9.1598 | -49.828499 | 2025-07-30 00:02:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99692884-1ca8-3952-80b4-4a86b930e261 | -4.8902 | -44.9557 | 2025-07-30 00:02:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f171ca60-9f9b-3358-a1a0-1c7a1df602af | -12.4674 | -44.070099 | 2025-07-30 00:02:00 | METOP-B | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 965c0178-e040-39d3-a1a8-a72a493916bc | -12.4689 | -44.077099 | 2025-07-30 00:02:00 | METOP-B | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c14b37a4-01bf-3f0c-86b8-391859958180 | -11.9226 | -44.538898 | 2025-07-30 00:02:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad56617a-2e55-3b91-aaac-668d34aa9560 | -15.7178 | -41.927601 | 2025-07-30 00:02:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c37b3da7-895d-36d3-872a-973515e86205 | -9.7508 | -48.556198 | 2025-07-30 00:02:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f06e5a1-b53a-3d09-8b00-59d0bdc35e29 | -8.957 | -46.7229 | 2025-07-30 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72f6e140-6784-3146-a9cb-07581b773370 | -7.8562 | -46.716801 | 2025-07-30 00:02:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 890af240-d2de-39dc-a3f4-b41130a40686 | -9.7528 | -48.565399 | 2025-07-30 00:02:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04335c12-b0ed-37af-8b1a-b7777b446f44 | -8.6887 | -51.188499 | 2025-07-30 00:02:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb99ad1e-ffba-376d-b036-981e538f2844 | -7.3112 | -44.682201 | 2025-07-30 00:02:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f027b3e4-4fee-31d3-b2fc-e88911bca7ac | -6.8885 | -44.7262 | 2025-07-30 00:02:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9938c0d9-dfc8-3bae-8f3b-12456632cac6 | -7.2808 | -47.984501 | 2025-07-30 00:02:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d088aee2-1ee9-32e1-98db-137f5dbc621d | -3.8783 | -41.027401 | 2025-07-30 00:02:00 | METOP-B | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4e7dcc8a-80be-3c39-b3ce-b6795157944e | -9.0437 | -45.0616 | 2025-07-30 00:02:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8a2f055d-6507-37ec-a7af-547f1df0f473 | -8.6279 | -45.878502 | 2025-07-30 00:02:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23192526-fc1d-3384-aabd-a02b0c68024f | -15.708 | -41.929901 | 2025-07-30 00:02:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3f7b8f7-ecd2-3009-a59a-c6799bc75e91 | -11.5612 | -44.254101 | 2025-07-30 00:02:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95bed6fa-2124-3528-9a3d-5c98f15b4b4e | -11.4711 | -45.105499 | 2025-07-30 00:02:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 61f267ee-0a9e-31b8-a17d-943145825cdd | -4.9182 | -45.079899 | 2025-07-30 00:02:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b58a576-02e1-34be-ace5-68a942d697a9 | -9.2339 | -48.580399 | 2025-07-30 00:02:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6496b822-bccd-3ec5-a897-77b0f056581d | -4.6458 | -43.109001 | 2025-07-30 00:02:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bcccb34-7f36-342c-b43b-fcd594e587c4 | -9.4051 | -45.484901 | 2025-07-30 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 142da598-9f8a-3c45-9400-c161a53b4e20 | -8.0305 | -46.902199 | 2025-07-30 00:02:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da836263-2506-34ed-9624-0f8a5639a939 | -10.0934 | -46.944901 | 2025-07-30 00:02:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f0bbe4b-36fa-309f-9a37-9966713348a6 | -6.261 | -46.108601 | 2025-07-30 00:02:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56d54069-dfb1-338b-98ac-b9dd3ddfa007 | -9.6315 | -48.5243 | 2025-07-30 00:02:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5817c67-a857-3e53-9cc1-7d1407f3df1e | -5.1082 | -45.145901 | 2025-07-30 00:02:00 | METOP-B | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
