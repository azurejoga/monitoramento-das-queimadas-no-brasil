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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ffb740f-3fdc-33f4-a3b5-d613e983df59 | -3.14925 | -49.90519 | 2024-12-13 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21c3059c-035b-3eaf-b704-62a7fc7538ae | -5.20809 | -43.29389 | 2024-12-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 6f9295a2-bdcc-33ea-93c7-a7fdbeebdb7b | -6.09846 | -44.76004 | 2024-12-13 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ea9876d0-76bc-354b-8d0c-56a7b9a12143 | -10.21285 | -47.58048 | 2024-12-13 04:21:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f1c0955-45d7-32ac-9de4-f96e77452ecd | -4.0822 | -49.33367 | 2024-12-13 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acc57e64-a20d-352b-ba75-97440b34edf6 | -3.9964 | -44.80574 | 2024-12-13 04:21:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e72c3c68-6608-3d0c-8888-e00763ef7032 | -4.45032 | -44.65292 | 2024-12-13 04:21:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1df3f67-9b40-3548-becb-8c5594b7e909 | -3.01301 | -48.03036 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2523a31-bd6b-3e33-b183-8f7a9b123bd3 | -3.26541 | -46.91681 | 2024-12-13 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77ccb9f3-13eb-3472-8db5-aa847b909ee9 | -6.4915 | -44.10616 | 2024-12-13 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97756dfd-4c7c-32e6-b866-f03e65b047cd | -6.08723 | -43.53849 | 2024-12-13 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4d3a707-9045-3214-bc4f-3ed26c422f65 | -3.33564 | -49.49768 | 2024-12-13 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54a14421-65da-3e2b-8518-78fe2e266c1d | -8.54805 | -40.69097 | 2024-12-13 04:21:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0b63b13e-4d82-361e-94ff-b0ee2beef3c0 | -2.50117 | -51.79647 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 28aa9bb5-c157-3094-8620-82d1fea88704 | -3.98432 | -44.56557 | 2024-12-13 04:21:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b54b1bc3-21ea-3f26-8b3d-6050cd3c20f7 | -9.169 | -49.47235 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3c66cfcd-07f2-3a48-8c98-97a9cf67472c | -10.52958 | -47.81497 | 2024-12-13 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f6c957e-f975-342f-9670-5b3df09417d2 | -4.73412 | -46.80082 | 2024-12-13 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d4929874-31d1-356b-bc26-809d732fa28f | -6.74014 | -38.20575 | 2024-12-13 04:21:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d988035-9a2f-3f52-836f-4b84cce4b577 | -4.65314 | -43.81932 | 2024-12-13 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8646de3f-6bf2-3351-afe0-74d1d417ebfd | -11.20305 | -53.81913 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 082a87a4-40ad-3857-a3df-74fb6bb93a0d | -14.77126 | -52.66119 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b004a7e-1ad3-3f2b-ad94-87c087b5c1cc | -11.49396 | -52.92931 | 2024-12-13 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e4bcf9f9-04cb-3551-b0a4-2f5e38f22e26 | -14.78147 | -52.63946 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6b290649-3cf7-3421-a708-b488390f93f2 | -12.10667 | -44.7524 | 2024-12-13 04:23:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e323e626-f125-37a1-a1f9-cde8b4ebfa4b | -12.03073 | -49.55066 | 2024-12-13 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bf1fdb6-4df0-30fd-a112-136b096e37a1 | -11.48041 | -48.21952 | 2024-12-13 04:23:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 627db5ce-05e2-3b32-a9e1-b8e951e1d766 | -14.76857 | -52.66226 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bef5d40-aa3d-3b06-b24d-33dfd3e5d10a | -10.29011 | -53.70132 | 2024-12-13 04:23:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff21d417-606c-301e-8d52-c1b8cb85fb11 | -11.44111 | -55.8955 | 2024-12-13 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b527510-77b5-3b4b-b5f7-00a7b2082063 | -13.68662 | -54.75769 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0beadf32-81c1-3b79-954f-65fa503c5846 | -14.78434 | -52.6384 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5ec4f53a-3430-3e55-8a6c-4d4101b34602 | -11.21187 | -53.82632 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cd88ea90-9d91-3d7c-bbc1-c41c0b661a11 | -14.15643 | -39.01982 | 2024-12-13 04:23:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9e39c242-ac98-335e-9718-3df103adbb6c | -12.30189 | -50.0928 | 2024-12-13 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05ce6d60-5a57-355a-aca8-e469d1bd0eaf | -12.02705 | -49.55001 | 2024-12-13 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f011191-5b97-3024-96df-55e40e50a903 | -14.78009 | -52.63758 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0b1d989-04f4-3f95-8ce4-3dc459e2305e | -11.49572 | -52.91983 | 2024-12-13 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef432297-7d74-3cb4-992a-9305988ce154 | -14.76657 | -52.64896 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 856cacd9-48c7-3ede-b8bd-1081ef682ad4 | -11.20258 | -53.83188 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 89488a17-601e-36c3-b7e1-8e074497fb22 | -12.02119 | -49.53989 | 2024-12-13 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8970a381-c3e0-3eb8-9f43-70516386a3f0 | -14.76306 | -52.64406 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3269cd13-6187-3b77-93a2-8a39172f20c3 | -11.44161 | -55.92325 | 2024-12-13 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c655a66-4dad-3a68-9482-ab9b5b82bef1 | -13.06494 | -52.0418 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fc3399e8-a18d-3a7a-9fb0-d97e60219bf9 | -13.07132 | -52.03065 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f058605-b80c-3028-876d-ec39f281d7ec | -13.05234 | -52.04042 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c93aa68-dc44-3b89-b749-74e192a292b2 | -12.86106 | -45.67356 | 2024-12-13 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a32ad93-7e17-3ee3-b0fa-0cfb7630ff8b | -14.78073 | -52.64361 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 71548e31-768d-34ee-8d48-2e52ea64efef | -13.06915 | -52.04256 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0d6fa00b-c646-3a3b-9fd3-085bba605e16 | -11.19715 | -53.82375 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c18d28eb-3d6e-3612-9bba-27ce90964296 | -11.75569 | -41.14033 | 2024-12-13 04:23:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3babfd7-52c1-3ca9-9155-627b0c39d167 | -14.77649 | -52.64273 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| afd7de25-f6b2-335a-963b-47a995a74ad4 | -11.20696 | -53.82545 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 39cdb5be-6ade-3fb5-9505-af60e8c10551 | -12.7628 | -49.30956 | 2024-12-13 04:23:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78968315-ac24-3df6-bf57-096f44752702 | -13.06421 | -52.0458 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ae01b9d9-4fe1-3f38-a4f6-d24aec63f0ad | -13.0558 | -52.0442 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a009a8e8-5aad-38ce-8b4b-4627c1a83ab7 | -14.7728 | -52.65301 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cef87399-14d7-3db3-9084-4fd73287430b | -11.20154 | -53.83736 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fd7087d5-9116-3ad3-9ea3-8708df3d3274 | -13.05653 | -52.04024 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad48b9d4-273f-3220-ab99-1630a7eeb8e3 | -10.72788 | -47.59015 | 2024-12-13 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f52c263-e4ca-34c8-8f79-2b2b697a6a6c | -12.90158 | -55.04638 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ddeef95-b8ce-3fc9-9b20-89e1a9655f27 | -11.20852 | -53.82726 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1b5cef57-54cc-35b5-ae3d-94155c02879e | -13.70151 | -54.76085 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 948667d4-d1b8-3ba4-a651-2fe2d470fce4 | -13.69266 | -54.75311 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 646af3d8-a9a1-3ac8-91ca-5b9269d141f1 | -11.20497 | -53.83645 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 04f08e22-738c-3476-8c68-20dac339f85f | -14.77225 | -52.64185 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e0452e05-2f63-30da-b3e4-b4a23ad17036 | -13.06073 | -52.04102 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 46cc0506-8e9a-39fe-b4b3-536c96b21cbc | -13.68879 | -54.74638 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d28413a-23da-33f0-a5d5-2131bbe1ce63 | -12.8605 | -45.67712 | 2024-12-13 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 751c1ca0-c78b-3ab8-b9b2-b0b570dab098 | -11.86015 | -46.9476 | 2024-12-13 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fae4ea1-c6f3-38c9-a3ab-50f60f82ba60 | -14.77006 | -52.65397 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f19d82fe-4b70-3020-b68c-313d568d4cff | -12.35667 | -44.71205 | 2024-12-13 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8ef6065-2846-3dd5-bb56-a7257e78b51b | -14.77299 | -52.63775 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 51781e98-ce32-338d-95d5-8e4731e83089 | -11.48261 | -48.2279 | 2024-12-13 04:23:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7c6d308-479e-38db-8c01-7087f51c50a8 | -12.35328 | -44.71151 | 2024-12-13 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08745ccb-881a-362e-8705-c8a32e14dae4 | -14.16117 | -39.02045 | 2024-12-13 04:23:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b85a2be6-46b0-3a2d-be68-90c0b75b0e6f | -14.77585 | -52.63674 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 822456ba-d7b0-38fe-8104-7c72dc1d260d | -13.06146 | -52.03704 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 21b52f6a-38cf-39af-8506-f155b04db817 | -12.76641 | -49.31021 | 2024-12-13 04:23:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5c72081-0afa-3e96-ab92-af3ca6ea96de | -14.76875 | -52.63689 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7e1f6d15-2181-3ffb-82e1-d308298f86c6 | -11.20644 | -53.83827 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6bc7af92-1159-331f-afc2-3af537c6d2dd | -11.53806 | -51.27452 | 2024-12-13 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17295895-7b66-3469-8664-6b5ced1b4315 | -12.28328 | -45.50084 | 2024-12-13 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1ae1bb9-e295-3707-8f56-10234e2a7258 | -11.20007 | -53.83555 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9d92559c-d500-3a69-9519-e4a1f424c055 | -13.69762 | -54.75418 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3773653a-bcef-3068-b19c-02b3ec5d47ee | -11.21238 | -53.83365 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4ed75e8-49b0-3407-a79c-c877a1ff37dd | -12.91189 | -55.04828 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07e68b7f-13f1-3841-bb23-b6ae9b76db8a | -11.20597 | -53.83093 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3e6c4ac0-dd4d-33ae-80a3-0f9b472aa4c7 | -14.76586 | -52.65289 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d388cf42-2f4f-3aaa-bfa8-59259587c5e0 | -14.78356 | -52.64255 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dba0baff-54e4-3998-9708-f2eeb606511e | -13.07204 | -52.02672 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83a4cfad-39fc-3de7-9ae0-ec6b8a46208d | -12.38495 | -51.45415 | 2024-12-13 04:23:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4519c3a0-98d6-33a8-8696-eb4c4e7201fd | -11.20361 | -53.8264 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 56a7245e-7d5d-3372-bcc9-4a3eadd1add6 | -13.6877 | -54.75203 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f948b639-5279-34ce-a400-d5c55d6fd0d8 | -11.1162 | -54.65075 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f21e30a-74f4-3e8c-a079-2627026cca33 | -14.76234 | -52.64801 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd6b5793-0e84-36de-ac3b-7924299eb1b2 | -12.90673 | -55.04734 | 2024-12-13 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 144d004d-000b-3ca7-8482-84452e577bc2 | -13.23613 | -48.23542 | 2024-12-13 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1c7a38d-d1d0-32d8-ba22-fe404e140cc3 | -12.30268 | -50.08813 | 2024-12-13 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc417bb5-4474-3c0e-9665-0db91dafc47c | -13.0748 | -52.03542 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README21.md)
