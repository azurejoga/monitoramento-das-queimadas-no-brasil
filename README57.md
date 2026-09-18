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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57adfaf1-a809-322d-b1ad-07eaa73e4c14 | -0.54138 | -49.14035 | 2026-09-18 04:55:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd44780c-c7a7-3c7b-9bdc-81746163a5b7 | -5.22443 | -49.30563 | 2026-09-18 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07eaf14d-6304-3574-bb53-3839c0457c91 | -6.35044 | -43.37287 | 2026-09-18 04:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0347f45e-1153-3a43-aa6e-b7c42700af54 | -3.04216 | -51.37957 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45267562-52b6-35bd-9362-0bbeac1f4689 | -3.70331 | -54.17591 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94cbceec-6ffb-330b-b41b-f47472582da5 | -2.25762 | -52.0288 | 2026-09-18 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3800ba3c-e6b8-3f5b-b413-25c8b34068d0 | -5.22442 | -49.32784 | 2026-09-18 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21cfd69e-3fc0-3687-ae59-634f9e829a97 | -4.55859 | -42.94437 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d85e528d-a047-3f12-af09-3129d8db44c6 | -3.38019 | -50.44418 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 109e55ad-d258-3a19-8c44-7424900117f7 | -1.17929 | -54.17428 | 2026-09-18 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5cf125d6-4573-3fe0-bc7d-56213da711ec | -2.81327 | -50.47439 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49da7150-afa1-3fdc-b178-e8c1b2f2af44 | -3.36193 | -50.45192 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ba6b4270-b3e1-3d8c-a598-d4927e1123be | -1.62191 | -55.11805 | 2026-09-18 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9a4ee63-3ff5-3a62-98a1-999af6489f41 | -2.81714 | -50.47146 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 2c6d4cac-791c-3628-8d3d-ae3824547f5f | -4.49635 | -45.90776 | 2026-09-18 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab11cadd-fc71-32bf-8fd3-ff4368f07981 | -2.95921 | -50.32457 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e40edf90-70a8-3c38-b5da-26276d1f56b9 | -0.78067 | -47.55523 | 2026-09-18 04:55:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbd56422-be46-3a4a-a783-f03d53f4438c | -3.33351 | -54.16914 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44211a63-d004-35a8-883a-9f4e81b4dc6c | -2.10073 | -52.05408 | 2026-09-18 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75254f66-1c04-3d50-ace6-57aa55babf95 | -2.96089 | -50.33545 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be21ef96-8928-314e-8607-56fe58e58073 | -3.36913 | -50.44952 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6105623-d8e8-33cb-a04c-07064660dd60 | -2.79665 | -42.47859 | 2026-09-18 04:55:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a83c130-5abc-3f1d-8bf8-cd3aa63f94f5 | -3.36581 | -50.44899 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d44b5ff-7efe-3fe9-ab2f-c02c115cf63e | -2.05467 | -52.16606 | 2026-09-18 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e5e9df1-f5d7-3fc3-b818-d430fe9de868 | -4.43777 | -55.52518 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 709fa22d-8142-3a3e-a648-fd7823fd8950 | -4.43471 | -55.07565 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecd94aea-b7ca-3e3d-bfab-ce1a737581ed | -3.564 | -54.22487 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 349e1538-e8ec-39a2-ab24-2636def33905 | -4.58926 | -42.95518 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0f998603-88b0-3db8-8ca5-fdca1b177c64 | -4.54285 | -54.9282 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8d23d93-657a-329b-bf1b-a118280040b1 | -3.42998 | -50.6608 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca7745cd-4929-3c48-8daf-3401defde945 | -2.19347 | -47.6474 | 2026-09-18 04:55:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ca4d008-5e6f-32ab-ac63-dddfcd9786cb | -1.15718 | -47.63139 | 2026-09-18 04:55:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd970eb9-cb59-3f7a-9068-f9b2aac1dd09 | -5.75436 | -45.08968 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98df7f07-1d8c-3319-a125-b3e59ee26c8c | -3.26782 | -54.26785 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab143367-e28a-3b26-b9cc-aa536997bfdf | -5.15855 | -45.24451 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88f8e375-044c-3e19-b7e1-1f71c3e1831a | -5.18372 | -49.27705 | 2026-09-18 04:55:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7f5d9df-8808-3d16-9597-1b7ba329faa4 | -3.36968 | -50.44606 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b774fbbb-43d9-3b9c-8d3a-b137af416cfc | -2.89839 | -54.18642 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea06848f-175f-3cd1-b926-ce8a4afc85b3 | -5.12791 | -37.71228 | 2026-09-18 04:55:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 479b9fee-6fd5-3cde-81f1-0ba1a3ef7501 | -4.43371 | -55.52475 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| febb8301-54cb-3fee-bf9d-9be741216181 | -1.20031 | -54.2173 | 2026-09-18 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7271d011-7ada-3c09-87da-99c94421acce | -4.38246 | -55.03036 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3b27bee-d389-33bd-8f2d-839753ad9ff0 | -2.81992 | -50.47544 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6880dc19-dc85-349d-8cf6-2f7963d5925e | -3.49991 | -49.5136 | 2026-09-18 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9957ab7f-453d-3b38-9bed-b9797b1702fd | -5.51426 | -43.66142 | 2026-09-18 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04b06d53-4376-32f2-bdcf-9120ccb3719b | -6.12171 | -44.0353 | 2026-09-18 04:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04cf5c46-5748-3cef-b7ec-0e9eba86a673 | -3.37081 | -50.4604 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd7e799d-3f21-3cff-acac-ed7f1b401289 | -3.41075 | -39.28207 | 2026-09-18 04:55:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c3b7f02d-f941-3f95-b44e-c73fca841662 | -5.51353 | -43.66643 | 2026-09-18 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0bf91cc9-14bc-3bb5-8b0a-0c4fed067684 | -2.32757 | -47.20023 | 2026-09-18 04:55:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ca691e8-211a-3f36-93ae-90c5fecf51c4 | -1.87705 | -48.73307 | 2026-09-18 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89b3ff67-6f6f-3995-968f-53f8bb1e6f89 | -3.47657 | -54.69331 | 2026-09-18 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f04c1a72-81b6-32e5-b574-003406f55bb8 | -4.55106 | -54.93272 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1b6fa31-d950-3985-8579-889f0a550261 | -2.10023 | -52.03486 | 2026-09-18 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09e491f5-437d-3ec1-9d0b-b3b5e65256f3 | 1.95748 | -50.93326 | 2026-09-18 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8229c6fa-96e8-350f-ab19-53cdfa294213 | -5.33755 | -45.14366 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 361becf5-6b86-3442-a30b-0e2d5c7fbc9a | -6.28974 | -41.80027 | 2026-09-18 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c68307c4-2cb9-3775-93cb-8e810f889856 | -5.77716 | -47.29187 | 2026-09-18 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8191f77-0434-38e7-9034-8f23fa3bb1f2 | -4.56186 | -42.95575 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| de2edea4-2827-32af-92fe-f1cc77d67515 | -4.27622 | -55.55001 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14cf71aa-7d85-3a6b-b76a-8d567613895e | -3.36303 | -50.44502 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eea865ed-0a95-3b61-a717-b470b1a64f00 | -3.03992 | -51.37197 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7401a6d1-687e-34c7-9cf8-8a14792b9a9b | -1.37879 | -52.55676 | 2026-09-18 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28359ae1-c4b8-3915-a769-22337b080847 | -3.03936 | -51.3755 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f8bee75-8e97-3698-b3e9-c017d73e8989 | -2.24338 | -48.75318 | 2026-09-18 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a4f47b5-61df-343a-9540-6583ce3cd86a | -4.55444 | -54.93023 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66c3f08b-bac7-39d6-99f1-adafed121775 | -4.36367 | -55.64743 | 2026-09-18 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a76c69af-1198-32b9-98b8-1b0a68cf7a90 | -5.4998 | -45.51863 | 2026-09-18 04:55:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d706b0ed-cefb-3bb0-962a-69540a64bcbb | -2.61417 | -54.75697 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 09e7ca0d-713d-3d4e-a65c-39703d670550 | -2.29774 | -48.58476 | 2026-09-18 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e9731b3-1e47-34df-b22e-043bcae0ecf8 | -1.78491 | -47.83365 | 2026-09-18 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 45a9642f-4154-348b-8a2e-c9336b23b6fa | -3.57507 | -43.4639 | 2026-09-18 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a44509ce-7248-327a-867f-448e83f01eee | -1.37846 | -49.36755 | 2026-09-18 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 882d9db8-12e0-3880-a9a8-fa8e93b1b819 | -3.36471 | -50.4559 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b79692cc-addb-35cb-a300-5c8a65de790a | -2.82302 | -49.23873 | 2026-09-18 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7ec2c5e-c0e1-34d3-8d80-a5ee56192d34 | -2.95976 | -50.32111 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d021099f-3d6e-3868-8630-c1006f9de6db | -3.76058 | -51.14033 | 2026-09-18 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa337528-693e-3101-9e4a-cadaa62e2d9b | -3.43275 | -50.66478 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2bd0791-1fbb-3db7-89b9-7ca157234bf7 | -4.49018 | -55.48822 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90f3187d-ff75-39d5-9e6d-56b5fb030f5e | -3.37023 | -50.44261 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 905db9f0-6bab-3bb6-90e6-60044df14465 | -2.69911 | -57.60196 | 2026-09-18 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95b44e4e-af40-39fc-b43c-7115fafafd64 | -3.36526 | -50.45245 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b98e26ac-8925-32de-a784-c7d27ea93ab1 | -4.48845 | -55.49861 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bcf3e24-2b79-33ea-8ea0-00e7b10585c0 | -2.10309 | -52.03913 | 2026-09-18 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9622b2b6-3c4a-3203-a0e8-01d0f3036cc5 | -2.6336 | -51.70728 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1edbac6-3d05-37b8-a14e-b0db50c96093 | -2.93452 | -54.15474 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ff38468-dc19-3f41-a31b-faa6f2aa242d | -3.56975 | -43.46791 | 2026-09-18 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70b5d64d-bb09-3922-ad8b-eb96a825d3d9 | -2.82657 | -50.47648 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 1fa251f8-db91-3d91-9c1f-62868fe957b4 | -3.30451 | -57.87724 | 2026-09-18 04:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56cc892f-7eb3-333c-b0b1-6328ce844f9c | -6.34559 | -43.37216 | 2026-09-18 04:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bacd0c2-f84c-342d-8d50-0ea8f86a9916 | -3.2633 | -54.27185 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8b907900-d401-3c33-898a-46229be2fd54 | -1.21509 | -54.22453 | 2026-09-18 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35c957ab-3c50-309a-b2fe-6da6f7c7a617 | -4.53741 | -54.9373 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b75bdf98-93b4-36f1-b44f-15938d99e16c | -1.70553 | -54.88478 | 2026-09-18 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fc872f4-e6f3-3234-af86-ba7df7097913 | 1.95805 | -50.93693 | 2026-09-18 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd1dc570-7c98-35ba-ace4-883c8d82bcfb | -9.56102 | -45.46841 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3722762-a304-34e2-ac7f-ebfe9d899c62 | -7.09124 | -42.08693 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5cfbc0b3-6034-3e40-8086-6a8cb06bef03 | -7.80191 | -44.89171 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12c0334d-176e-3952-8a90-30203ef092ef | -13.60842 | -46.96328 | 2026-09-18 04:57:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c4766bc-762c-304b-b6a9-bf1b526ecf9d | -8.91003 | -45.00589 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README58.md)
