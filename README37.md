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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4718538d-2d7b-325e-89e2-053dd6808251 | -11.31236 | -47.84945 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74919bdf-5a22-3ef7-a6b4-cb9480e1b47a | -7.65619 | -46.27297 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47573f22-7e71-3098-9c20-a7e9f464fab3 | -11.52882 | -50.48621 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58aaa93f-1b19-31ea-81ad-88206753ea5d | -10.7143 | -48.31818 | 2025-08-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bb96eb2-e766-3efe-bb9a-bb122f7906a4 | -8.7499 | -46.7141 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b7034ad-5f1f-36e9-b1a1-90ede0db7ade | -13.04922 | -45.21804 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e37ea02d-51b3-3e7e-832d-1d148567fbce | -7.63102 | -46.27694 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7b5186d-82f2-3736-a50e-d9e103bd995c | -8.85945 | -52.041 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78524fb1-48c5-37a2-9c82-ccb0a2b361c3 | -9.15982 | -59.49459 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4eb53ce3-8c28-35d1-bb8e-4761e55dd514 | -11.51505 | -51.86948 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| df752220-3ded-31cd-9927-b68b9be42103 | -5.74511 | -57.60506 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01e5751a-9e27-3d8a-b9bc-d85b0b8d3d10 | -8.1815 | -45.08796 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 143f6750-d5f0-3a44-9a4d-f2065e86f5f0 | -9.18375 | -59.62452 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4aa6add9-2331-3941-9b94-d7fadc9c14d0 | -5.802 | -59.21623 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 706814e1-0ef5-3b70-b609-2dd66b05f5ef | -9.15267 | -59.50864 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0928e4f7-428c-3893-bc46-177f67e84d00 | -8.23895 | -47.46413 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6008e975-cdad-3e85-8225-e6c6d5af3970 | -9.15937 | -59.50539 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe7adda8-7d42-345c-92ee-1e6c7de2c593 | -11.52386 | -50.47426 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9074547-8f2b-3a99-ba51-87de189d4a85 | -8.90193 | -62.45401 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d9609a4c-ecc5-3e6b-bfcb-02b7c8436b36 | -8.91317 | -62.4346 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2dc9ccb9-d236-3d80-85f4-6e30e8c28353 | -9.13829 | -60.77278 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0c6c4da7-1e59-3c7a-b44c-9ade9ca0d702 | -5.45134 | -60.18633 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f74ee2ac-22fc-3ee1-8d3c-f5cdf0caa83b | -7.60042 | -46.24892 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0faf5ab-0f72-3f7e-9ea1-03d9364606e6 | -11.53045 | -51.86379 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 492e54d4-d6a9-3ccf-958f-fab4af8fb321 | -6.45909 | -53.39888 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff0aeb69-d292-31b3-af7f-cd228acffad0 | -11.5333 | -51.86837 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66edb4c0-ba98-3af5-a9f5-f091a78c4cac | -8.37043 | -49.29969 | 2025-08-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2dc97de-6011-389a-9df9-e29142316e4a | -5.74971 | -57.57805 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4a0f4f4f-3981-38b7-b357-b62a0fa097d0 | -11.54619 | -51.89944 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9683f42a-6ee0-34d0-ab2a-80389571f073 | -6.89191 | -45.69714 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf14becd-a3d1-3a7b-a20c-5f1c05ef84dd | -8.11209 | -47.14225 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b82acf6-41f3-36dd-b138-c09bce9f15f5 | -11.54685 | -51.89545 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a30d1911-c6e6-329a-bc39-a20e78b8a15b | -7.02319 | -44.65042 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b46f270c-abd0-3cc0-9a97-32b3b1e8c7db | -13.48105 | -47.03849 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45c9c125-54af-3598-aed7-e229ddec4a7b | -7.60471 | -46.2651 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1392ebb2-4db3-34eb-baf4-436af17184fe | -10.41286 | -47.19163 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23ea3306-7a25-3274-9406-d0cdb57d45ae | -9.16577 | -59.47101 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e1780d82-257b-37e4-9c5c-4c7ac6db01fd | -6.68602 | -58.8632 | 2025-08-24 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9f926e2c-71a4-31b5-82bc-85c5f63c9ebe | -6.65681 | -55.4189 | 2025-08-24 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4581a3ff-3833-32d8-8233-43eec9c0f6bf | -13.04265 | -45.23687 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 583afc7c-d371-3aab-aa10-717639cf0d00 | -11.53179 | -51.85577 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2c7954e6-fb52-32d8-bb06-74470587fdbf | -11.13945 | -46.33409 | 2025-08-24 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77442344-0fb5-3826-9fbd-22e507280052 | -9.80385 | -61.2132 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d748bd7-d251-383c-af43-0b1621fc19f4 | -12.72162 | -48.10083 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3774409-96f6-3741-b0de-16f1383b4739 | -13.47382 | -46.88643 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8fdc066-29da-320e-ab69-3d9f0ff3a8dd | -11.28595 | -44.9768 | 2025-08-24 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8d31d3f-b329-360a-968d-50273c590deb | -5.42025 | -60.17432 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 2d95615a-8be8-3b8f-ac84-b9ea0b847274 | -7.28031 | -43.66263 | 2025-08-24 04:34:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d81cf6a5-894a-3f55-8b12-5ba6bdb35a94 | -8.84302 | -49.90068 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff28ed7e-c8e3-3c67-a83c-b9ca2c68970c | -9.16646 | -59.46027 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 86c9484e-0ba5-3fed-8400-5faad2d13f16 | -13.4379 | -47.03282 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 45378820-ea60-31f1-9ddd-12d328056772 | -11.31851 | -47.85428 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e38475e-3768-30d5-88b2-cd8440d2b236 | -8.11153 | -47.14582 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0442b5a9-596e-3570-81bd-35e3881d92c9 | -9.16336 | -59.48396 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 66684fc8-c41d-37b6-9964-33c5caf41816 | -8.73687 | -45.45881 | 2025-08-24 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c6ece00-2ef4-3e69-b343-32480a31dc5b | -11.73442 | -51.70274 | 2025-08-24 04:34:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 930921fe-be9c-3cbf-918e-ca0324b93b18 | -7.69837 | -42.12696 | 2025-08-24 04:34:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 551f6ec0-8ec6-3238-a716-becfb292c930 | -10.60793 | -44.32378 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| d67f52c9-b668-3ba2-9509-f3bebb99d239 | -7.78585 | -61.56932 | 2025-08-24 04:34:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5e75d8e-9a29-3b82-83e4-36de8046abf0 | -5.7429 | -57.5844 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7592038a-a3fd-3fda-ab67-12c9fc74cbc9 | -8.9057 | -62.4479 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7beab379-6a93-3f15-b006-be3e6163a2d2 | -12.73283 | -48.11772 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 151c8560-6a53-39b7-9ff9-53c9855b25d5 | -10.70434 | -48.31665 | 2025-08-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3557e70f-32d7-37dd-85a6-bd4cb7f02f35 | -6.31287 | -59.87474 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d74f2aa0-4778-3e0e-b3ee-aa9cd210874d | -8.11544 | -47.14277 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3585adde-2383-3fd9-801a-c9a68a797fa1 | -11.53782 | -51.90626 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37a9713e-9c34-39bd-9d75-e2e02b3496c2 | -14.16294 | -43.66692 | 2025-08-24 04:34:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1639bace-15ff-3cc0-b98a-f8404bca9652 | -10.71484 | -48.31467 | 2025-08-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47e73587-e76a-3642-b339-d90ee37a5363 | -11.10697 | -44.76564 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 549ca720-1812-3d55-ac4e-97e610e2c337 | -5.61594 | -60.24012 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28f31bf8-303e-34f1-88e9-583dcc28e482 | -11.05159 | -44.61478 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 445dad1e-c3e3-3eee-bde2-651304f1fd6f | -8.21858 | -45.11769 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6fc71fd-168d-3b61-91ed-b3cb885aa955 | -8.2199 | -45.08287 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 254afae5-5fc2-3255-99ad-dd4a34195606 | -13.05174 | -46.32769 | 2025-08-24 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d22020d2-266b-3e5c-b783-838b8a3f9eed | -6.87398 | -59.81529 | 2025-08-24 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 54d865ac-4981-3ec9-a1ef-312d237ebf04 | -12.94905 | -46.28879 | 2025-08-24 04:34:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fb53e6e-adef-3e31-b6ad-4ef731b4e06f | -12.5442 | -45.61746 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfb235d6-fdc1-340f-946f-a43a5f13f799 | -9.51915 | -60.51226 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 384f6b64-9d6b-30f7-af55-c94fd3ba25c2 | -13.41305 | -51.79225 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a44a194f-37ce-3d5c-acf3-c370a61a1dfa | -7.0288 | -44.63789 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fab3b10c-feac-39bf-b674-93ae28e51543 | -13.36491 | -47.50238 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8636637f-bfa6-3e38-a6d7-b345b113a66f | -9.17068 | -59.46988 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3dd9d9b7-1156-313a-93b9-7236e10906a8 | -12.7384 | -48.12635 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41aa8b0e-f758-33d0-904f-531d770bb5d8 | -13.05552 | -45.22886 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62a8e8a2-9a3b-36e8-bd4f-87c7edfbd096 | -9.25483 | -59.63799 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa863b71-676a-3788-bc58-6ed7ade21b20 | -8.76872 | -46.75122 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ebb8e3e-2b39-331c-9b6d-296f81a71858 | -5.60942 | -60.23896 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5a237491-0a6d-3274-a4ee-2e67b91d376d | -8.75399 | -46.75645 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 05a59307-22cb-3cdd-8461-4012e8c2b5b2 | -10.10706 | -57.76567 | 2025-08-24 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed9c1227-cb16-3669-9042-908f7d9bc370 | -9.20589 | -59.4765 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 78e096ad-6d2b-3761-8aec-95ed26f672d3 | -9.68352 | -48.34557 | 2025-08-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d5d5e22-3a24-362a-b281-2c38d5580b3b | -9.1736 | -59.59335 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0213ea3a-2370-3718-a1c1-e67e85501da1 | -9.8325 | -45.95007 | 2025-08-24 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fb326bc-6514-3960-a3a8-e59270826cc8 | -9.23554 | -60.92583 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9937a875-51cd-3848-b7ae-1316df7df1a8 | -9.47729 | -48.18377 | 2025-08-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1784482e-ef41-3670-aaaf-3107323fb759 | -9.22912 | -60.92468 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f18dfe01-5f42-3bf4-9ac1-efc6b3870166 | -11.17788 | -55.0276 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f8be5cf-7bae-3824-97c2-caef37db567f | -8.18086 | -45.09223 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a47aeaab-6158-341a-8fa3-735a2e7e878f | -13.04853 | -45.22291 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6122bd95-ac72-3543-82e8-6103186f9ff0 | -7.60819 | -45.24353 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README38.md)
