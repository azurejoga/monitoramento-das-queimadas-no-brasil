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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b07a315a-3512-3d33-9aa6-b3176a290298 | -18.48859 | -45.12868 | 2026-09-29 03:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d3ca9c6-01c0-3991-9a7e-9f6796a72054 | -18.57244 | -48.42708 | 2026-09-29 03:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d035cd34-487d-3fa2-b9d7-fcba134a1b9f | -18.08314 | -44.39333 | 2026-09-29 03:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f637a942-b7e1-31a0-bbc8-f873e4db64c7 | -21.70034 | -47.17358 | 2026-09-29 03:34:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 80e74f19-e630-3227-9f34-aa2514d318c4 | -18.56547 | -48.42459 | 2026-09-29 03:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 931d52bf-675d-3711-b0f7-6b3b8367b80f | -17.59514 | -43.71719 | 2026-09-29 03:34:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3b105b9-1264-3aab-9730-2019858b1185 | -18.10915 | -44.35736 | 2026-09-29 03:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62b2363f-8485-35fa-a92b-104589c18efd | -18.4025 | -42.31065 | 2026-09-29 03:34:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 93371f39-3f9e-3e06-a768-2242d32d0c92 | -18.40753 | -42.31187 | 2026-09-29 03:34:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d6b37fc8-4842-398b-8c7d-a9e669751d98 | -17.97673 | -44.49382 | 2026-09-29 03:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d2c9b66-0882-3bfb-8922-3a5843961bfe | -20.43745 | -46.34645 | 2026-09-29 03:34:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea7696dd-5e88-3bdb-ad52-6d57c79a2215 | -18.1083 | -44.36126 | 2026-09-29 03:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8632d65-ffb3-389b-8f4c-90997b020638 | -18.10429 | -44.35196 | 2026-09-29 03:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cb5391b-f783-3a74-8534-673ca368d171 | -18.40181 | -42.31399 | 2026-09-29 03:34:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 26758037-d50c-348c-a5d5-f2b23c8667df | -20.44095 | -46.35097 | 2026-09-29 03:34:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3e3f221-0539-3daa-93b4-87808afa00e7 | -20.44364 | -46.34789 | 2026-09-29 03:34:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60032a1d-c8aa-3df3-a2db-1fdb3a491b91 | -19.00302 | -47.876 | 2026-09-29 03:34:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3d0e762-5f9a-3359-b938-4caa7e4f7435 | -17.61805 | -46.67249 | 2026-09-29 03:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00040a0f-b557-3e6e-94b6-a2f24d3768a8 | -19.36266 | -41.49986 | 2026-09-29 03:34:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a78e298-94ce-34e6-9432-5f2759c569a5 | -18.84556 | -41.99928 | 2026-09-29 03:34:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dba89c65-f2f5-39aa-87ad-8ec0a5ae0c60 | -17.61445 | -46.67202 | 2026-09-29 03:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f056042b-ed86-37b4-854d-cd83df15111c | -20.21118 | -48.56921 | 2026-09-29 03:34:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcbd8d97-0bf9-3ea4-b23a-572dc3155b95 | -20.44234 | -46.34505 | 2026-09-29 03:34:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63785f1f-d95c-324a-8035-3ae2c040b11d | -18.2689 | -42.20829 | 2026-09-29 03:34:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| d7d8d5b8-3808-3dd7-be31-4241308129ed | -18.56354 | -48.43249 | 2026-09-29 03:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 56c21751-6288-35f9-809f-a077369b1425 | -18.11401 | -44.36275 | 2026-09-29 03:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc8b95c0-c24e-3d6e-92ca-18a91692f607 | -11.4115 | -43.4388 | 2026-09-29 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ced60991-9d5e-3a3e-a224-823c9a641349 | -7.8486 | -45.8138 | 2026-09-29 03:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| ca6d0cff-e49a-3a2e-9981-abea8ca98e28 | -3.8202 | -55.899 | 2026-09-29 03:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 37f7b6d3-617a-36b9-a2a5-66d89c2a4267 | -15.2511 | -43.2743 | 2026-09-29 03:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 131.0 |
| f8edef1a-4944-39ee-8b26-ed0d09927fa3 | -7.8297 | -45.8156 | 2026-09-29 03:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 2ea8ffea-d716-36ef-9a7a-0d88bfc7b0a2 | -11.4302 | -43.4596 | 2026-09-29 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| dae08461-abea-39dd-9837-9f15b030063e | -11.9748 | -50.9295 | 2026-09-29 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| afa5c4f3-0bfa-3605-87e1-522e074b997f | -11.4307 | -43.4358 | 2026-09-29 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a1c86b62-41b4-36c9-ae13-86a848f21823 | -9.177 | -61.4073 | 2026-09-29 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 775004d5-5d1f-3807-8241-d131f6d6bfc2 | -11.4298 | -43.4833 | 2026-09-29 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| c420cdc7-3517-3a2a-b85e-ac446371f84c | -11.411 | -43.4625 | 2026-09-29 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| e0a5befb-2e3c-39c2-9cfe-7e5231a8d0b1 | -15.2517 | -43.2501 | 2026-09-29 03:40:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 60.1 |
| a8da9071-b412-320a-ab27-997e17c337a0 | -12.7421 | -47.2684 | 2026-09-29 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 27b15574-d9f5-3330-b4d3-cc82ebb14f11 | -3.8202 | -55.9187 | 2026-09-29 03:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| f703ee9e-adf7-3d87-8016-a15725122562 | -6.2947 | -43.6427 | 2026-09-29 03:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 0bfe262a-91d2-351e-9c99-98edfc9c516a | -11.4307 | -43.4358 | 2026-09-29 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 22b06525-c3d9-38f4-a3a1-52b7222da63d | -7.8297 | -45.8156 | 2026-09-29 03:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 2dda7dea-2075-32de-8ef9-1aeff17dd4e2 | -21.0658 | -48.8428 | 2026-09-29 03:50:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 130.7 |
| 5f934c8b-1534-34cf-96ee-d332f72c6ab9 | -11.9748 | -50.9295 | 2026-09-29 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| d451f6c6-f10a-3ffa-9812-6f0172ae2073 | -3.8202 | -55.9187 | 2026-09-29 03:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 815ae284-671d-3222-bbf9-b0a3d2f1bccc | -11.4302 | -43.4596 | 2026-09-29 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 5737af2c-38fc-374b-bdcd-e9f4d6dc4436 | -10.2147 | -46.706 | 2026-09-29 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 464444ad-087d-3f77-88b4-3cf1b237687b | -11.4298 | -43.4833 | 2026-09-29 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 38c225bf-b824-332c-99b2-90bc21a6b798 | -11.4115 | -43.4388 | 2026-09-29 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 22e1ff19-773d-3ae6-85ed-94dd001c843f | -9.177 | -61.4073 | 2026-09-29 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4ac0fdab-ae7d-36a2-b49a-505d9a4728a3 | -3.8202 | -55.899 | 2026-09-29 03:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| feae43b4-28d7-3bb8-974f-b80ea4790f81 | -21.0665 | -48.8196 | 2026-09-29 03:50:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.5 |
| a3eb6ab1-b723-3afb-adb7-8a11e85b7f0a | -11.411 | -43.4625 | 2026-09-29 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 538e7ac7-9943-3496-8ad3-a19400442977 | -15.2511 | -43.2743 | 2026-09-29 03:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 02786d0f-0dee-30a6-adb3-c0188c0aa6bf | -7.8486 | -45.8138 | 2026-09-29 03:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 8bb95d7c-8662-344a-9314-7313b4e55f67 | -11.1775 | -44.7832 | 2026-09-29 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 3523f555-8af5-3342-9995-8c9982b6eb48 | -7.8486 | -45.8138 | 2026-09-29 04:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 371beeed-d847-3f8f-9be7-6cbd2749f4ca | -15.2517 | -43.2501 | 2026-09-29 04:00:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 489d933a-f9f7-3584-b37c-604873dc047c | -11.4307 | -43.4358 | 2026-09-29 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a2f8481b-ef78-3dd8-9839-3795adc08b43 | -11.4115 | -43.4388 | 2026-09-29 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 5424321b-8af4-3736-8aa3-7922c1f4b715 | -7.8297 | -45.8156 | 2026-09-29 04:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7b3403e3-9696-3dfa-8f58-8a2833a29e31 | -9.177 | -61.4073 | 2026-09-29 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 86fe1b15-be79-34cd-905c-c68ddf3cc952 | -15.2511 | -43.2743 | 2026-09-29 04:00:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 130.0 |
| afd6525b-01e1-3c9a-87fb-91915eee4ca6 | -11.4302 | -43.4596 | 2026-09-29 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 37a7ea9f-7689-3afe-99dc-33e10db8f6e1 | -11.1775 | -44.7832 | 2026-09-29 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 854807cc-40a1-3db2-9b7d-9318606c37c0 | -9.177 | -61.4073 | 2026-09-29 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d2978bef-3fc0-3444-b541-f73a78e3f1e4 | -15.2511 | -43.2743 | 2026-09-29 04:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 190.1 |
| 5c35bf5a-2122-3f4f-8ff8-1c648511f2ab | -10.3894 | -61.2502 | 2026-09-29 04:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 4046ad60-4879-3f5b-a7b3-aae73edc0ff2 | -15.2517 | -43.2501 | 2026-09-29 04:10:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 4408f337-0e07-3556-972a-3e297b32eaf1 | -9.9595 | -50.1431 | 2026-09-29 04:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| dd8fc548-41f2-3076-866c-900202197135 | 0.53088 | -50.81367 | 2026-09-29 04:12:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ca50f4b-a619-3590-9f0a-fa05ebd3d28c | 0.52556 | -50.81445 | 2026-09-29 04:12:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7186b249-368a-3b56-a3e5-a9367ba88674 | 3.82533 | -51.77227 | 2026-09-29 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38288833-4bee-3d60-94f6-f820f156d122 | -0.50435 | -49.12341 | 2026-09-29 04:12:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4c1885d-1618-3880-adb3-eedbc770f819 | 3.82769 | -51.77213 | 2026-09-29 04:12:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 539fe0ba-bac8-32a7-9c89-1b588ab5321a | 0.15446 | -51.12248 | 2026-09-29 04:12:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed33cef5-c933-3c6d-a571-6fe2cb38000e | 2.08346 | -50.74939 | 2026-09-29 04:12:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 333496ce-d179-39d6-81f3-9599e015b806 | -9.04782 | -45.00126 | 2026-09-29 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10f0a6e0-d76c-3d4e-b8bb-35def7e3641d | -7.24925 | -43.37363 | 2026-09-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3987bb10-2389-305d-8d39-51802e5cde15 | -4.82339 | -45.63587 | 2026-09-29 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 17b2a696-b719-3b3a-90e1-b684066d3a2d | -7.22053 | -45.08476 | 2026-09-29 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 303dedd0-ec80-3d1a-9c63-982628715949 | -7.47633 | -45.81207 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc94ac17-1d99-35e0-96b3-3afbfac8241f | -9.43947 | -41.82232 | 2026-09-29 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd15224e-583f-3e8e-9f02-504be7c20be2 | -9.07562 | -43.13092 | 2026-09-29 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 32bb9184-4e64-3762-a50b-49c5c01e6e15 | -3.70701 | -54.2136 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb4996e8-e5d9-37cc-bba5-e0685fe1eea5 | -3.26574 | -50.14038 | 2026-09-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4abbdd71-b1dc-3b75-9577-f77fb044f11e | -9.76692 | -36.98209 | 2026-09-29 04:14:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 13.5 |
| fd59f5a7-bbfb-3f04-a043-13ec148571bb | -6.14708 | -52.90975 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 811c9149-925d-3e85-8de4-63d0afaae144 | -8.24543 | -45.44236 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbabdf24-df6a-3dcd-9301-43f3256df432 | -5.73303 | -45.02604 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 302e06a5-ed63-3b6e-ba78-afb80891d8fa | -3.15014 | -54.08453 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3904563-9e9c-34b3-b933-bbb72104dad4 | -8.32281 | -44.16557 | 2026-09-29 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cb3b071-0715-336d-8d74-4d4a708fb478 | -7.67346 | -44.89031 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 884fc6bf-fa56-3a76-911b-0e15a62562d5 | -7.26073 | -45.33876 | 2026-09-29 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44e9ea21-8705-39a1-92f4-94abb3e25188 | -9.77216 | -36.97811 | 2026-09-29 04:14:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cf79c261-eb0f-3879-ac70-212d4b2a91cf | -7.26521 | -43.37966 | 2026-09-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4010e4a4-1724-3f83-a145-aedb9e4cebf5 | -7.54469 | -44.58902 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2360262d-6024-3ab2-9cb3-fc18ec329c75 | -4.49678 | -49.64181 | 2026-09-29 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f42acae6-67b2-3f0f-8ce5-0d7fe61f883b | -5.48606 | -45.12135 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README14.md)
