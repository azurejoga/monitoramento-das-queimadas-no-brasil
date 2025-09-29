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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 073f51c5-a02b-35ff-a0ff-70f84e339aa3 | -10.8227 | -46.6763 | 2025-09-29 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 60894a5a-2a49-3f4f-b49a-6ee684e7a384 | -6.4317 | -43.0942 | 2025-09-29 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 619d27f8-c6d9-35ec-86c3-165a0eab5743 | -11.3826 | -45.0774 | 2025-09-29 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5435b41c-27d1-3d51-a780-a2284f7ae35d | -9.4007 | -54.6984 | 2025-09-29 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7f519313-d576-3c8d-a93d-f77fec68dd50 | -11.3638 | -45.057 | 2025-09-29 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 9851a1cc-0ffb-32fe-bcba-d8ca7e3c3cd8 | -11.8172 | -47.6201 | 2025-09-29 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| ca8efe7e-2b1a-3dfa-b89d-7f99b37dd72d | -13.011 | -49.4423 | 2025-09-29 13:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 8582ac21-02b4-3051-80c8-a583927bbd91 | -10.6239 | -48.5386 | 2025-09-29 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 537fc91e-ca58-34ef-9c5b-0b1ef4664b93 | -7.2999 | -42.8486 | 2025-09-29 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| b4c7d1c9-2cb6-3025-97f9-623862de53f0 | -13.3796 | -48.1577 | 2025-09-29 13:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| aecf85c7-0357-39a6-b708-553b2006c3e6 | -7.2214 | -44.783 | 2025-09-29 13:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| a44c6752-aaf1-3602-b998-ab8a30f66d4c | -8.2854 | -45.4772 | 2025-09-29 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1b213eea-1295-3805-82c9-e17eb9a4d3d1 | -15.6127 | -46.2465 | 2025-09-29 13:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 162.0 |
| f012c3b9-9bc2-303a-b69b-42c486105c78 | -11.3443 | -45.0828 | 2025-09-29 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| c3e3155b-056c-37f4-acef-2f65fe9ede4e | -9.7674 | -46.1971 | 2025-09-29 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 202.2 |
| b3bc5cb2-1334-3a93-9113-0dbaa244bea4 | -14.7176 | -45.2057 | 2025-09-29 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 67a68068-c0c3-3fc6-9a11-d9e5250447ad | -6.0811 | -42.4644 | 2025-09-29 13:00:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 20cfd96f-d5d0-3f5d-8bf2-c5bbffb8e339 | -7.8566 | -46.7527 | 2025-09-29 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| cb7564db-070d-38c2-99c4-7213f1d85737 | -7.2216 | -44.7601 | 2025-09-29 13:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| cc4c35d7-1f15-3d23-89f1-1750b6151319 | -6.7482 | -43.3704 | 2025-09-29 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 8ae1c609-1e9c-3957-9b0d-01bf7c4d0521 | -7.4676 | -46.2974 | 2025-09-29 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| ca89a1f4-242d-3d45-978a-c8f24d1595ff | -9.8852 | -45.9122 | 2025-09-29 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a5858532-ae60-30f5-a1f4-515549dfb196 | -7.8378 | -46.7544 | 2025-09-29 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 37e2686b-b298-3cb4-9df8-799dbe1c22e5 | -7.8163 | -47.0003 | 2025-09-29 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| d566387f-5417-32a3-ab20-7b22b31fe1ab | -11.8482 | -51.7916 | 2025-09-29 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 18a9f200-65ab-3257-a361-2b0196a57bfe | -7.3653 | -42.1058 | 2025-09-29 13:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 49fd8122-6af2-395a-bac8-0349364f9ac4 | -13.7695 | -47.9211 | 2025-09-29 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| cf27531a-6b12-3c36-b326-7de9807ed65a | -9.7671 | -46.2196 | 2025-09-29 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 1ca29836-c5f7-3627-a8a8-4a18548cecd7 | -9.9959 | -43.6172 | 2025-09-29 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| dfe369ab-42b7-3531-b8a6-5ac296289a5a | -13.2346 | -50.9691 | 2025-09-29 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 235.4 |
| d4c69671-c5a4-35be-919e-0e256ab57797 | -15.0496 | -46.9675 | 2025-09-29 13:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 0783d8fc-5691-30ff-b730-2d00eeb12b56 | -6.4319 | -43.0707 | 2025-09-29 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 402dd548-0047-3a61-9117-91c089078b16 | -12.863 | -46.9582 | 2025-09-29 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 80412ba8-c658-385d-a8a0-6a010d6f414a | -11.3447 | -45.0597 | 2025-09-29 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 2b710d1a-982b-36aa-8211-0e72a5a5ce75 | -8.2662 | -45.5018 | 2025-09-29 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f1171447-d79d-3574-8b45-bc5ff8c8876f | -8.2665 | -45.4791 | 2025-09-29 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 97e86041-d8b8-3236-a85b-ff4bb5c942f9 | -13.2005 | -50.716 | 2025-09-29 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 1ecda7a8-fb6d-38b6-81ed-99e7d6c474d2 | -7.3464 | -42.1078 | 2025-09-29 13:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 0a384961-1ae6-3366-a770-e285579338c9 | -15.1933 | -48.4765 | 2025-09-29 13:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 245.8 |
| 8e88a912-6db0-3214-892b-02b07cb8db1e | -7.2402 | -44.7812 | 2025-09-29 13:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 0c21ab62-3f82-3c18-be66-c325e2730bb8 | -6.0609 | -42.608 | 2025-09-29 13:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| ac90e4de-4e87-3dae-936d-6d0cd24421f0 | -7.3001 | -42.825 | 2025-09-29 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 84785048-5935-3386-9eeb-ab58a80a2f09 | -8.1614 | -46.3899 | 2025-09-29 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| df087e34-1ff5-3e97-bc96-5ce820b203e8 | -7.8165 | -46.9781 | 2025-09-29 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c8a30d2e-e599-3161-b14d-5f6fe7908fbc | -15.219 | -50.1071 | 2025-09-29 13:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 05a9bc63-8682-3831-9479-131772a0e812 | -9.0913 | -45.8673 | 2025-09-29 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9e355bb3-d895-3af0-aa5a-8031851de045 | -11.3447 | -45.0597 | 2025-09-29 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 34d08388-f36f-359c-b9c2-45f57e002845 | -7.365 | -42.1298 | 2025-09-29 13:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| d9095929-1e66-3782-b7ab-37afdd5ebcc1 | -7.7226 | -46.9865 | 2025-09-29 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 91768689-2265-3878-aad6-d604aaa3e443 | -12.9736 | -45.1819 | 2025-09-29 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| dd44f43d-cc8c-38bc-ac1b-688b8eaccc35 | -6.7482 | -43.3704 | 2025-09-29 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 62.1 |
| deb81f4e-9dde-3771-a559-b1a24e93be47 | -9.9959 | -43.6172 | 2025-09-29 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 199.5 |
| fd457b52-05b6-3c6c-ba16-3af43a517cdb | -13.1816 | -50.6969 | 2025-09-29 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 5fd7123f-0467-3d03-b37c-0caec3beb9b6 | -6.4319 | -43.0707 | 2025-09-29 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 04776a6b-d350-35f5-8b51-4acc2fc6d886 | -8.2848 | -45.5225 | 2025-09-29 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 252.5 |
| 4d4f0c4b-cf99-3bb7-8146-28199baf56cb | -7.2216 | -44.7601 | 2025-09-29 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 750c1643-6289-33e0-af31-a58e8754bac4 | -15.1938 | -48.4541 | 2025-09-29 13:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 17fd7bae-210e-37ce-800e-39ac09568279 | -13.011 | -49.4423 | 2025-09-29 13:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 2d9a2c32-85a4-3544-8c24-c1a297e4c95e | -8.2659 | -45.5244 | 2025-09-29 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 200.9 |
| d1539a92-f9e0-3f70-9478-6d75b7833632 | -17.7144 | -46.6865 | 2025-09-29 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 49389fd0-87ad-3266-9647-e2f3615b4d77 | -7.7414 | -46.9848 | 2025-09-29 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 9c2d9844-33a2-36c3-a7df-a7c091a6440d | -11.925 | -48.0273 | 2025-09-29 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| d57d3d67-2c27-340a-8e80-e3d1eec2e88e | -9.7674 | -46.1971 | 2025-09-29 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 893127db-4f3d-3ac1-af36-da24d615c5bb | -9.8852 | -45.9122 | 2025-09-29 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 8682bede-8bba-3f50-85b6-437dd8745e77 | -11.3443 | -45.0828 | 2025-09-29 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 019cb398-be3d-31ae-b643-4c37cb62e53f | -9.8848 | -45.9349 | 2025-09-29 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| a6dc795c-43f8-3548-a6ea-905d5e0cf03a | -6.9692 | -43.7927 | 2025-09-29 13:10:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f6717bdf-ee07-3a0d-a880-4c10836a95cf | -8.2854 | -45.4772 | 2025-09-29 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 5acc8a0d-e59b-3a75-8011-01daf66d0581 | -8.0034 | -47.0497 | 2025-09-29 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| efa6cf98-02d1-3a80-9ef7-b710cf62bd0f | -14.5336 | -48.4268 | 2025-09-29 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 639528d8-abb9-3796-b0de-7e0893d91544 | -7.4488 | -46.299 | 2025-09-29 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 583fbb90-6b07-377f-8e02-28ab22a3b313 | -13.3796 | -48.1577 | 2025-09-29 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 162.5 |
| c0c9e17a-d4a0-3559-9e55-eb5373ece544 | -9.9768 | -43.6197 | 2025-09-29 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 23b4f67c-0ef6-3027-b4a1-ca4b691bf696 | -7.2999 | -42.8486 | 2025-09-29 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 7e22d6ba-485e-3e97-a2f2-2452a60a7a72 | -15.2194 | -50.0851 | 2025-09-29 13:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e2c2af90-6429-3543-a63d-bdf1e8ff7d4f | -6.4317 | -43.0942 | 2025-09-29 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 583755bd-b540-3c51-861b-afeec38fc6bf | -14.6049 | -45.0161 | 2025-09-29 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| d0e22ff6-aa61-389b-abe9-ed45328c0b53 | -11.8482 | -51.7916 | 2025-09-29 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 10dbdaf3-3bf8-36fd-8e90-4bb0dd5cb43d | -7.8165 | -46.9781 | 2025-09-29 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 6cda7901-b90c-38af-b230-375b27a5d1d4 | -13.2346 | -50.9691 | 2025-09-29 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 219.9 |
| bcdb4f92-aedc-39c1-9900-d4b81c82451d | -11.3638 | -45.057 | 2025-09-29 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| dcb95dbe-1d22-3038-ac44-d05d613780f9 | -15.6127 | -46.2465 | 2025-09-29 13:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b0ac6d49-5fe8-3fb9-a38f-d77483661cc2 | -7.2402 | -44.7812 | 2025-09-29 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1ecb5069-349d-351b-9672-27059b74ea65 | -7.3464 | -42.1078 | 2025-09-29 13:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 137.4 |
| f84579d6-6956-35e7-b16b-74281626c95d | -8.2665 | -45.4791 | 2025-09-29 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5d8f88fd-5e34-33c8-88ff-4711c59ebda5 | -7.2214 | -44.783 | 2025-09-29 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b0c884f4-fae1-3824-9a5e-45653990b3b4 | -9.4007 | -54.6984 | 2025-09-29 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 00250b38-04bb-3ab7-851c-50b5b81660a3 | -11.4405 | -45.0461 | 2025-09-29 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| d4b72433-b567-3e56-b9dc-fb6f4869319d | -13.3989 | -48.1549 | 2025-09-29 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 10cbb196-9e6f-3ea5-8a56-79df2a459583 | -9.9963 | -43.5937 | 2025-09-29 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 30faf42f-810e-3865-9328-d2754ab3f64d | -7.3653 | -42.1058 | 2025-09-29 13:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 175.6 |
| 9f6ca8b9-12c2-3645-9ff8-c00430418e59 | -7.9628 | -47.3184 | 2025-09-29 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| d81e8b2a-a632-355d-8146-bb6889ebd6a9 | -7.4676 | -46.2974 | 2025-09-29 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 818b2502-969b-3646-86e5-0488818dbb71 | -15.219 | -50.1071 | 2025-09-29 13:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 361f404f-5467-353e-84eb-268b0b0767b1 | -7.8566 | -46.7527 | 2025-09-29 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 67aabd8d-b1a0-3141-a874-49ecf7e0c86d | -8.2662 | -45.5018 | 2025-09-29 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| f300527b-f6ff-3ecb-b788-5dbfb4adc649 | -7.8378 | -46.7544 | 2025-09-29 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| ab07c95d-eb7f-33c8-8301-fdd3e09af94e | -9.9772 | -43.5962 | 2025-09-29 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e5de8fbb-e029-397b-97f6-74d266366628 | -11.3826 | -45.0774 | 2025-09-29 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b9e61938-28e1-3a05-b0a1-20bbfb3df32e | -10.6239 | -48.5386 | 2025-09-29 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |


[Clique aqui para ver as próximas entradas](README91.md)
