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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2034276e-6b7a-3fe4-9c11-de8e237edac3 | -7.85418 | -43.57716 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cf01b17-5968-33eb-9012-1b5e5dbc5cdb | -7.51455 | -44.36769 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a1c1452-5e2a-323c-b980-973d2e668b94 | -9.08418 | -44.81635 | 2025-09-15 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17247334-cb41-3e53-8950-71501448f504 | -12.0036 | -46.66796 | 2025-09-15 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b74a085-386c-37ce-b105-d436dab24e22 | -12.59444 | -45.71481 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0fdbd9a7-af17-394d-b277-f971c9768563 | -9.09056 | -44.81769 | 2025-09-15 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fcb4052-3773-352e-bc36-e3ac53a71db6 | -7.87756 | -43.58628 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 219.9 |
| 4605d004-1b6d-3664-8ffa-41598eba8881 | -7.88969 | -43.58855 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 4503e449-1793-323d-95aa-9dfcd09f93b8 | -8.90679 | -45.49893 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18846299-09b1-3269-a53a-db3b8c7c4864 | -11.33655 | -43.49934 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 305e68ce-f1fe-3e62-ba72-a1001763f77d | -10.93486 | -45.50451 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a32e1d65-9deb-3bef-bbe5-e7401629c1af | -8.90995 | -45.49877 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5c8614ca-02e8-3f0d-83c4-8c9a06be5de5 | -7.86252 | -43.56219 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c39962a-0291-3529-9cbb-67231855dd86 | -8.61968 | -45.73483 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f881ab7c-e019-34a7-8a39-0f7af77517aa | -8.91229 | -45.50646 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6c28ee54-17fa-3739-9284-702007460257 | -11.44827 | -46.92863 | 2025-09-15 03:30:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20958359-5207-358b-b9f7-5a83d13f4781 | -7.67191 | -44.48965 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e940e98-ed99-32e3-9eaf-5658c3031b4b | -11.33347 | -43.49316 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9782b556-2614-350a-9947-84c3292fd266 | -11.79147 | -46.65503 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a39597fd-e755-30f5-a3cb-b87fa3430230 | -8.82389 | -40.67336 | 2025-09-15 03:30:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 40d06e32-fdca-3f6a-a189-a95cc9bc1b68 | -7.85996 | -43.57619 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4be6688-f028-39c9-8648-0f59ba790857 | -7.85561 | -43.56571 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99ab1ff8-23f2-3cad-9c09-53fc715715a7 | -7.8539 | -43.57507 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dfa9b21-8153-3932-8720-05b804c3dc57 | -9.23183 | -45.67179 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b67fd15f-0ad4-3b22-9e9f-a4595e3c66b6 | -10.92235 | -45.59861 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f89e4780-3d84-321a-ad94-8c0ee13d5fcb | -10.93424 | -45.50923 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b018d08-ccd5-37e1-946f-02e2daf812a0 | -7.88195 | -43.56309 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e0ac6aaf-e955-347a-b03e-aeebb9f049e6 | -8.79128 | -46.0636 | 2025-09-15 03:30:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 123237a3-3cb0-3d88-8d73-3e494ffe97be | -7.87403 | -43.60498 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7bfb778-ab7e-340d-aac7-f2b4960b4c21 | -10.92957 | -45.49749 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 83bb8f21-9f29-34f9-9743-6c97c1a21d5c | -10.68609 | -46.25307 | 2025-09-15 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3aa66af1-1ecb-3a69-99e8-dbf162dee2bc | -10.78659 | -41.69917 | 2025-09-15 03:30:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8def04e8-fefd-3cfb-a106-caba14331695 | -7.8758 | -43.59558 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c5c96dbf-99e6-3219-8b7e-5742785e5827 | -8.20072 | -45.54357 | 2025-09-15 03:30:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b2d87a09-2b2c-39da-8911-1cb02bee987f | -11.76211 | -46.65649 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31b07948-f43d-307f-807e-f674fe1125ff | -10.7224 | -44.78024 | 2025-09-15 03:30:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5545a377-88d4-381d-a971-f23e1a457590 | -12.79279 | -47.944 | 2025-09-15 03:30:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a034fe98-749e-3d64-adad-510a26224349 | -7.88756 | -43.56227 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 171.3 |
| ea26324d-7f2e-33bf-a20f-569e362a1c3d | -7.8923 | -43.57468 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 520.8 |
| bc9251f4-f385-3ee9-95b7-f66a536a4530 | -9.19429 | -45.24872 | 2025-09-15 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a01afb6f-61d1-32b0-81ac-13ce32f833dc | -12.005 | -46.6613 | 2025-09-15 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5206a96-c35b-3499-9c58-d124751d8be2 | -8.89179 | -46.1712 | 2025-09-15 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de6f5562-867a-3c71-8cb7-fe11741fb799 | -7.87464 | -43.56448 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 59a86ea9-3077-3243-983d-9f484725b187 | -8.6516 | -46.36954 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 99b4340e-244a-3a0a-917d-0f7109aaf0e7 | -7.85935 | -43.58297 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 2f012b30-4467-34df-ac17-66a3d0bc1231 | -8.91667 | -45.4648 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21f579d9-7a2a-3bc1-b16d-a2e66f9823e9 | -8.9111 | -45.49296 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a47756d6-e5ae-3a24-9d94-791eabfe7d12 | -10.89167 | -45.45304 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 420ede1d-c35d-3ca6-b6cb-80d1b3ddc228 | -8.90567 | -45.5048 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95f81cae-8cf5-3204-97a5-ff318b1e480f | -10.92682 | -45.58085 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53540a1b-cce4-350c-b0aa-13b292c16412 | -7.89404 | -43.56545 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 2568b17b-884f-37c3-8169-c340ab4d5435 | -7.87668 | -43.59093 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 219.9 |
| 51650efb-9b2c-3d4b-bbe7-2f163ae053ec | -8.59376 | -46.36567 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 125009bd-8970-3c8e-a2aa-107be406556d | -7.87548 | -43.55986 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3f4ca4bd-25ef-3d37-a739-2dc77fe565e7 | -7.86943 | -43.55869 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a1f6be6c-1459-36f8-96f3-03547ee58411 | -13.28569 | -43.79042 | 2025-09-15 03:30:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c4cde41-a6a1-3dc0-8388-f860c8576c74 | -7.87061 | -43.58982 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 219.9 |
| 1dcd2021-f24a-3117-8149-da0ce748fbb8 | -8.89858 | -46.16586 | 2025-09-15 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9bfda46-d9c3-3335-99f0-7c781d4c5a36 | -7.50581 | -44.37341 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60ed8e39-0d82-3f4d-b08d-1e56d910df22 | -11.77515 | -46.66501 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2699a127-cbd7-3079-a1d8-c816eedb6efd | -12.03873 | -46.53475 | 2025-09-15 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a03d3eef-176c-3423-8dfa-da3b133b0183 | -7.67968 | -44.48685 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ed04fdd-874a-3af0-842a-ae6459dccbca | -8.81893 | -40.67252 | 2025-09-15 03:30:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fd0bf1f8-f141-3c1f-8d2e-312685fa783a | -11.48329 | -43.61263 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05e0c259-6273-31dc-82fc-2a0dd8899270 | -12.59278 | -45.71583 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90654612-de71-3f6c-a9f7-0abf60366aa0 | -10.7296 | -44.7765 | 2025-09-15 03:30:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc810e76-fd86-305f-b105-b774d8c35341 | -8.78676 | -46.04676 | 2025-09-15 03:30:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 669eb189-7417-3db6-b0ff-35c42c9eabc8 | -7.85685 | -43.56318 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 496842da-f7e1-3574-9d66-49a147442487 | -7.86688 | -43.57265 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 514.7 |
| 5d997bf2-67c1-3126-bfbb-797fd7be99b5 | -7.87997 | -43.60416 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13954482-0c40-33a6-9248-b5c8c5dad88c | -12.11058 | -44.83978 | 2025-09-15 03:30:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceda1494-d3ea-3d59-b669-046bdcbc81de | -8.98424 | -45.77016 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e440c3e7-c4a1-3509-adc4-d94b141ce483 | -10.89806 | -45.45466 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c0005df-7055-3f35-b0e8-8aa3759e35a8 | -7.88281 | -43.55853 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9e024089-b257-36c2-9f38-aaa93a3637a2 | -11.33354 | -43.51516 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49e43e78-9abf-3f5c-a382-5c8ab3b3ff78 | -12.11661 | -44.84131 | 2025-09-15 03:30:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ef91a64-e2b1-3fbd-93ae-b91e3ebfc38d | -12.16731 | -44.10182 | 2025-09-15 03:30:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfccae61-966d-37a4-8fb0-e4b8c1229263 | -7.88971 | -43.55516 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e35e8cae-37fa-3564-845e-beb4501c7003 | -10.65269 | -46.24374 | 2025-09-15 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 331d0612-b648-3e75-84b8-4cb052f39a0d | -10.63698 | -44.21114 | 2025-09-15 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59d81c19-c3a1-31cd-a891-9b69ac8e10ae | -8.62031 | -45.73729 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 04a817eb-8c19-3f82-b7a2-f878ec68f821 | -7.88275 | -43.59206 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b97f05a3-70b4-3b42-8d48-6b76d0fc3af6 | -7.84436 | -43.86288 | 2025-09-15 03:30:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fa0ebf9-3b71-38e3-99ec-6834c8094c59 | -8.79861 | -38.41393 | 2025-09-15 03:30:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d461c9f5-60f0-3ea9-8466-e38c6709f6ea | -10.93847 | -45.52188 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc153de0-2a55-3400-99f8-ce38d23a639c | -7.86796 | -43.60382 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69ef65b2-d650-3e24-ac98-39ba61ce786c | -7.87932 | -43.57698 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 874.2 |
| 244be509-1e14-3e1d-9a0b-f7f4be78f03a | -8.78559 | -46.05258 | 2025-09-15 03:30:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c5c71e9d-8abf-37a5-bfca-230a4a347f18 | -12.00397 | -46.66129 | 2025-09-15 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bb9a8a3-11e9-334c-8679-08471f30f9ed | -8.95569 | -45.80233 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 985bbc50-e228-33c7-93bb-f0950b047a8d | -7.87815 | -43.57962 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 319.0 |
| 9fb897a1-3340-3108-9c56-220f714a3077 | -8.65016 | -46.37683 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2f344418-9948-366e-9ccf-28dddde1c96f | -7.87502 | -43.56654 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 478.1 |
| 3e15e37f-615a-34eb-ac22-8e62b9ce6ac4 | -8.61846 | -45.74117 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 515b35bb-f401-3db8-b060-06ef476e7f3c | -7.86517 | -43.58203 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 787.2 |
| 02ab9877-32b6-3a35-86b4-a19c6d1a95d0 | -7.88152 | -43.56105 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 70060dc8-2cd8-3b56-a607-12ee8ebdff80 | -10.29883 | -45.39353 | 2025-09-15 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bca18c9-0e0b-35d0-82bf-6fbcd9fcd996 | -12.09339 | -44.86221 | 2025-09-15 03:30:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 739dbac7-1d0c-338b-a7fe-340335beee8b | -8.07706 | -44.50866 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 821e9a4e-1df5-3f7b-a0cf-e96049d39a63 | -11.33729 | -43.4954 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README12.md)
