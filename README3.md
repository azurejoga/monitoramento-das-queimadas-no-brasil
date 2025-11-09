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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c949e122-d1f3-3f60-bf0d-6625de89f4b4 | -5.20747 | -44.41902 | 2025-11-09 00:34:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b8161131-89bd-3c2a-aa41-b9f8ec67958d | -3.09278 | -49.26433 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| b5e1d168-accc-3d0b-8afe-e976c25ce9d6 | -8.18516 | -46.20512 | 2025-11-09 00:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ff85bc4a-a12d-3e40-92ca-5f00743ed585 | -3.32567 | -44.37739 | 2025-11-09 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 12fddb07-4c63-32cf-9f56-e7aa3be0244c | -3.64723 | -49.87554 | 2025-11-09 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6af534b0-597f-3e44-8950-e383bd3c7ce5 | -4.88699 | -48.59685 | 2025-11-09 00:34:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 56cde2e7-1808-3cfb-a4b7-d737205a4def | -3.33117 | -49.12502 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c350f1db-2986-3874-a8e0-1ab1b6b538df | -4.3813 | -45.50498 | 2025-11-09 00:34:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 60b1600b-1c01-3c9f-ba50-6c11c081f28a | -3.84617 | -47.40309 | 2025-11-09 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ab717985-c007-315f-a614-18d0cf59d7ab | -4.60959 | -45.57042 | 2025-11-09 00:34:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 061f9a90-c5a1-34a6-86bb-82d935d9f7eb | -3.33946 | -44.38178 | 2025-11-09 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 4f264d22-116a-38bb-83b8-52bbf8743751 | -3.80461 | -48.89412 | 2025-11-09 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9aa12c2a-d175-3fe8-8249-8b9e69269d60 | -6.34375 | -46.76982 | 2025-11-09 00:34:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 912d30cf-2f23-364d-9483-3ab8397180ad | -9.47746 | -48.74225 | 2025-11-09 00:34:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 0aad0bdd-6757-382b-bee7-5d7a67676a3b | -4.46704 | -44.66022 | 2025-11-09 00:34:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 06fcdce4-0ec2-3811-b85b-3bb57740c206 | -3.08037 | -52.91376 | 2025-11-09 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f44a0f94-5355-3ccb-adec-915103b36344 | -3.26202 | -50.08218 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1a854838-6a34-389f-bb23-45acd92e2439 | -2.11186 | -47.65022 | 2025-11-09 00:34:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c29542b0-1a94-3bca-9303-0c946c9b2149 | -4.63868 | -46.38968 | 2025-11-09 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 34.2 |
| e1f9712f-50ee-3af9-ae70-2003614a0c4d | -3.3325 | -49.13458 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4e1719b4-783c-3667-8dd2-f54078193113 | -3.34147 | -44.39525 | 2025-11-09 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| cef1879a-51d3-3571-aba1-2abfd9949679 | -4.1332 | -49.26208 | 2025-11-09 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 85079eb3-33fc-3aa8-8d9f-e52035a8666b | -3.50761 | -50.0566 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 517bfab4-7266-3e70-92d7-5f422864dedf | -3.9784 | -49.86823 | 2025-11-09 00:34:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 077e63a5-7b14-3dba-b621-b8e388949d75 | -9.33232 | -47.84309 | 2025-11-09 00:34:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 86cd45d5-034f-33a2-a041-7f26ce59c839 | -8.89834 | -47.89863 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 38a3895d-cf72-3b18-a127-56194e144118 | -4.68322 | -45.84068 | 2025-11-09 00:34:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d63e2dab-71c3-37c3-aa80-c9e65e68256b | -4.68528 | -45.85469 | 2025-11-09 00:34:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 019be4df-4a13-3e1d-8daf-4c159d959bd0 | -3.79815 | -48.91472 | 2025-11-09 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7273e99a-c355-37c2-a758-348bcad652f1 | -2.70762 | -49.54349 | 2025-11-09 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4ee0f84f-6ff0-3255-8c2a-c40b9e237036 | -4.62997 | -46.40439 | 2025-11-09 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 0f485878-31b9-38d4-898b-a8ef7c98754b | -2.84245 | -49.51804 | 2025-11-09 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d81f1324-6859-3db2-9914-8701d9baa785 | -5.30146 | -47.28029 | 2025-11-09 00:34:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0ffdded5-cc21-3ca7-bc13-5b9a39930bf4 | -3.2517 | -50.13816 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e435d825-9efd-389b-a39e-ecda562c7435 | -3.47567 | -48.97534 | 2025-11-09 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a049e4e0-43a3-343c-a3a9-4f401d838ac7 | -3.26594 | -50.04519 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5dc33835-e3ff-3e37-a6bd-2590755a7abc | -2.94741 | -49.34834 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b55be29c-ff36-3581-a157-9e1793ea810b | -3.49747 | -50.04894 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c003f974-3754-3cb5-91c0-9725408beacc | -2.11021 | -47.63848 | 2025-11-09 00:34:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 08cdca37-2fd0-341a-8150-15640751f0bb | -3.05982 | -50.21369 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 321d5f5a-2721-328d-aaac-131b596b5930 | -3.69219 | -51.39028 | 2025-11-09 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 21f0d884-5d73-3fc6-ae99-3ee6e00bfb1a | -3.5637 | -51.125 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 4288aabc-fcdd-344d-9042-9a5f158feadb | -2.54813 | -49.19765 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb3d2734-9882-35a0-bc0d-c2aa53ef7e4e | -2.83359 | -50.4448 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0e8ba32e-688c-3565-ae20-a1bb0d628155 | -4.39966 | -45.94475 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0b231f2d-1b6c-3f87-ab79-e32154e04989 | -9.48218 | -49.03538 | 2025-11-09 00:34:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc37d9e8-4d3f-3cd6-8f35-44944105bbe2 | -3.65719 | -50.27369 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3b43db56-97bb-3951-89fe-18fab6dbea32 | -9.47176 | -47.35217 | 2025-11-09 00:34:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 53c644ee-abdb-3b95-aeb0-a6c811163b08 | -3.86484 | -49.38437 | 2025-11-09 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 17031f28-ba83-3fa2-8505-313ae0635bd6 | -3.14601 | -48.73268 | 2025-11-09 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 44ca4f5b-e56a-3b54-96d0-992cd83480bf | -5.28575 | -44.94164 | 2025-11-09 00:34:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 84e7b7f4-d0d9-3c88-b1bb-6a3b04930de0 | -5.72856 | -46.47533 | 2025-11-09 00:34:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2e5c94f3-2e7e-31b2-92b3-69d044747fee | -3.79541 | -48.89548 | 2025-11-09 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 533aa605-b2cf-3c87-98b9-357cac80ce8e | -4.87218 | -49.0126 | 2025-11-09 00:34:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b8f9b37c-fb36-35fa-aced-2704367d1293 | -3.50636 | -50.04769 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aef31524-1b38-37ce-8e28-d2fe49d77375 | -5.31097 | -49.51401 | 2025-11-09 00:34:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8f3b0267-5e17-3362-9d80-166a7973f42d | -3.36782 | -49.51981 | 2025-11-09 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b5f9f780-cfba-394e-9027-b6a8f07ff509 | -4.11773 | -47.29837 | 2025-11-09 00:34:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 561dbe1c-7af7-33f5-9c18-febf44b46897 | -6.01699 | -43.78555 | 2025-11-09 00:34:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 82e42251-b24a-36ff-a502-dbb6edfac02e | -7.4154 | -40.06701 | 2025-11-09 00:34:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 50.7 |
| 18374f51-600f-3969-9448-b0b5f3086571 | -2.93964 | -49.35901 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 77c6fa2d-dc05-34db-89eb-180ea0ffc692 | -7.49738 | -46.6128 | 2025-11-09 00:34:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| cd488f0a-8648-3f81-981c-8ffe102a5df5 | -4.1874 | -46.22488 | 2025-11-09 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 98ce3b81-22a9-369e-8c26-5863c92e4bb5 | -3.03458 | -50.30497 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1eb97dc9-5aad-313b-ad91-aba237ce222f | -3.61942 | -49.27708 | 2025-11-09 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 11707f3f-9b34-3c97-ae56-95ed8af6b15b | -3.87074 | -51.21738 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2bf16dae-b01c-371f-813b-1dd2869f21e2 | -4.79931 | -46.00647 | 2025-11-09 00:34:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 815f86a2-4877-3a4d-b699-ad14f7e068bd | -4.46442 | -44.64212 | 2025-11-09 00:34:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| e5c1e59b-d204-374c-90a5-02043332792a | -3.07982 | -49.37137 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2abc5541-77a7-3e77-b652-3be4d2683337 | -2.96745 | -49.82135 | 2025-11-09 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cf9f9343-7e66-3cc1-a8eb-72a00a6981d1 | -3.41536 | -50.263 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d7a4a2ac-78c6-3288-b7e2-f07a497677a2 | -5.78042 | -49.83554 | 2025-11-09 00:34:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2c0a6fe5-3a7f-3140-b0da-7052fb30f70f | -3.1042 | -50.20742 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| db9f158a-3519-3d74-9491-e0129cec33c0 | -2.51939 | -49.44936 | 2025-11-09 00:34:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e5fd713c-75d3-3604-bfc9-e7f86491095b | -3.33846 | -53.24612 | 2025-11-09 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1b968aee-5356-31d3-bd70-f2f8b14cf58f | -3.58837 | -41.65952 | 2025-11-09 00:34:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 852b8c79-aaa0-38ff-85e9-ecc541041670 | -3.3238 | -44.36396 | 2025-11-09 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 7c7745db-9ce8-3e5f-b70e-d94be74fec95 | -3.30992 | -50.16623 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 60ffc624-f30d-3b3b-a2b7-5cdf3aec6e69 | -4.83314 | -45.60978 | 2025-11-09 00:34:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bcb9c434-ddf4-3c77-aeb3-885e0fab8eff | -3.32335 | -49.13591 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| dfb0eda2-2e9e-37d6-b697-1af53f3403af | -3.83077 | -51.12368 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 28e0414c-297f-3df4-a0fb-f3e72f70e1ca | -5.27639 | -44.95987 | 2025-11-09 00:34:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| e136e5ba-fb6f-3b13-a457-a2b497a1e662 | -4.20809 | -47.78311 | 2025-11-09 00:34:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| acece199-974f-3f9b-be6a-1062324683a3 | -2.60076 | -49.23889 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 7b568095-aee7-3d72-993c-f04934fb697b | -3.34345 | -50.20081 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 39210dd4-3009-3daf-b5aa-52fb09f8f8a1 | -5.13778 | -45.72736 | 2025-11-09 00:34:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 3b37a2d6-5b15-32b5-8125-8b0fa8571f9e | -4.87087 | -49.00326 | 2025-11-09 00:34:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 14752055-6ff7-3782-9b9f-bb0b5291d9fe | -7.17168 | -44.94935 | 2025-11-09 00:34:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| f197d86c-1017-3e3f-b9c4-4f23c679d07c | -2.54002 | -49.19542 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 56ba4de3-e778-32ff-837e-f3022b8d0f1a | -4.58199 | -45.62067 | 2025-11-09 00:34:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 18a05d82-aa17-3e72-8034-a18f3b2a8fd9 | -4.58394 | -49.38922 | 2025-11-09 00:34:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 000c99dc-7e28-3ad8-adcf-0325aa938f87 | -6.028 | -46.56534 | 2025-11-09 00:34:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d821067e-0150-3ae7-9601-c1d41a5ecd95 | -4.11678 | -49.79975 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4303027a-2ab3-3aca-8cae-cb8fe16b79d0 | -3.59722 | -41.65294 | 2025-11-09 00:34:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 3056144f-2205-30c6-bb37-07f99fcbf70e | -4.27473 | -45.96073 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cb43b53a-9655-3abf-95d0-5baac5a0ec61 | -2.64165 | -49.20786 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 10ef3505-3301-3807-ac94-12a2caf60607 | -6.34208 | -46.75811 | 2025-11-09 00:34:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8827d78d-9f41-3e38-bea0-cdd4b7b7e450 | -2.21672 | -51.37835 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7c5e399c-9154-3237-8014-d149a745023f | -3.1019 | -49.26302 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c6f10c22-5ab9-32f2-87dc-47880b0468fe | -4.63667 | -46.40932 | 2025-11-09 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 38.6 |


[Clique aqui para ver as próximas entradas](README4.md)
