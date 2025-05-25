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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 811e14fb-6424-3a0f-95b2-8d3b83f221d6 | -8.05151 | -43.14532 | 2025-05-25 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 40c094a2-dec3-35e7-8bdf-5538988fa902 | -10.9409 | -55.32009 | 2025-05-25 05:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58688e1b-0120-3370-abbd-28aecd790075 | -7.22193 | -43.11927 | 2025-05-25 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 728e68c0-8f72-38c8-96cd-81a7f126b693 | -7.66084 | -46.09447 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 16a8b8ef-87c1-374d-80f9-f82963df87c7 | -10.36412 | -47.96645 | 2025-05-25 05:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 653efc3b-bdb9-3a45-a8f7-7a260c3acbe6 | -11.1435 | -48.1124 | 2025-05-25 05:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3441d10-b93a-3dcb-afcc-3d506f25782e | -6.55727 | -44.48682 | 2025-05-25 05:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9599f5c-470a-34de-9978-6af9d4839432 | -10.74116 | -49.2884 | 2025-05-25 05:06:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46d386ab-d8b1-3b08-bf51-0cc3fe7cb4fc | -11.1342 | -53.91994 | 2025-05-25 05:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15ec22ef-dd6a-3dda-aaf0-3b787e9d1cb5 | -5.12112 | -56.1152 | 2025-05-25 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d6a25ac-8b5f-39a3-8943-82d6db17288d | -6.55662 | -44.4915 | 2025-05-25 05:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 134cdd79-dc43-3b9d-9a45-80fdf2aa8689 | -7.64896 | -46.09666 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fcdc8a8b-a1d8-3920-b1e9-e1cf9fb184b1 | -9.03509 | -48.93959 | 2025-05-25 05:06:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fea0ee87-3760-3c01-a5e8-ee336577e734 | -10.93521 | -55.31163 | 2025-05-25 05:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 530a6d6d-b717-3d68-a5bd-51f7b38b2423 | -8.90272 | -44.78178 | 2025-05-25 05:06:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b7895cb-727f-3187-bab3-ec6ad4c0a7f6 | -8.75264 | -48.03838 | 2025-05-25 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5520cd2-dcbe-37dd-aee4-41b3217c399d | -7.22274 | -43.11314 | 2025-05-25 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d1de51e0-2b50-3187-8146-718d5e530815 | -7.65928 | -46.10611 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0501c4c4-d8b8-3577-bacd-657c6479e0dd | -11.57474 | -47.61991 | 2025-05-25 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ad686de-a5b4-336e-bf00-571f577253a8 | -11.57428 | -47.62343 | 2025-05-25 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29e99a4e-7073-3d2e-af9d-ea7092893194 | -6.84258 | -44.62463 | 2025-05-25 05:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85d3554e-ab13-3a49-94f2-bbecd8a2fb86 | -11.57519 | -47.61644 | 2025-05-25 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 37929812-3028-3fd4-8dd6-11a82c07c66b | -11.57185 | -47.61184 | 2025-05-25 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 65453f48-4681-3487-a7cb-93f6303fba27 | -7.66031 | -46.09843 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 26b79a77-50ee-35c4-b351-bb01852af30f | -11.57601 | -47.62296 | 2025-05-25 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e66b1fd6-6006-37ab-8ef8-624bc7bb3ad3 | -7.65979 | -46.10234 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 756b7366-9702-3694-8a26-2805da2d76fb | -10.72566 | -52.47504 | 2025-05-25 05:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60041ec4-814c-312a-a295-d5ff41cbedc1 | -11.76009 | -47.25679 | 2025-05-25 05:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 720df560-558d-3d6a-a43c-20f14317c4df | -6.56017 | -44.49482 | 2025-05-25 05:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 993d661f-0d8c-3df5-85e0-ea5e53eafc7b | -7.20753 | -43.12343 | 2025-05-25 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e7ded973-e1d3-366a-8827-a4f73050bf38 | -11.75405 | -47.25984 | 2025-05-25 05:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 166248af-50dd-31a3-9c8e-dcf0e9176128 | -9.03474 | -48.94086 | 2025-05-25 05:06:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6587b0f-bfa0-3c7b-8ce9-01d4bfab6cdf | -10.73794 | -53.88232 | 2025-05-25 05:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15f7c752-dcea-348c-9725-3cbc9dd82577 | -6.83641 | -44.62371 | 2025-05-25 05:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a46c08a-b11e-3b2f-8ff9-3861f60093ff | -5.32378 | -55.94439 | 2025-05-25 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e2d2cf0-514b-3561-9830-ee7bb72d0274 | -7.65515 | -46.09366 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4f992dc8-fc99-3f98-820a-bbf6f9a0bfd2 | -6.83579 | -44.62824 | 2025-05-25 05:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec90e4cc-2aae-3197-8e50-7479c70be88e | -8.06764 | -43.12851 | 2025-05-25 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e99dd711-d3f4-3d99-8f8a-cd207cafd291 | -6.56076 | -44.49038 | 2025-05-25 05:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aef73c0f-b131-3682-9918-b70922a833a5 | -11.61632 | -47.99514 | 2025-05-25 05:06:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc8d0ad0-0fbd-3a19-85d0-ebfe3753a23a | -11.56601 | -47.61445 | 2025-05-25 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b8eb9fe3-1093-3432-a0db-e17e49693bc0 | -8.73034 | -47.98676 | 2025-05-25 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3eed3507-74eb-3551-8f29-56fdee84e76d | -8.0523 | -43.13916 | 2025-05-25 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1ba7ace7-82f2-30a6-9486-e6dc24a35e65 | -11.14019 | -53.92939 | 2025-05-25 05:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06dca307-e81f-3219-b9eb-26a2fe6c221e | -6.63808 | -55.01233 | 2025-05-25 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3d3e376-d3ec-3432-8eb4-6539e3b366f4 | -11.7545 | -47.25616 | 2025-05-25 05:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5418c16-687d-32be-a447-7c8adddcd368 | -7.65411 | -46.10149 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c3745ad1-7dbc-3208-84ee-9cf2a3169c76 | -10.37814 | -47.9812 | 2025-05-25 05:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74f87891-eb75-33c2-b275-da9a0536e33b | -8.75304 | -48.03542 | 2025-05-25 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e8afbed-ba03-3955-9662-17ad6205582b | -6.55448 | -44.49003 | 2025-05-25 05:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d13b095-286a-3d77-aa66-666c56819121 | -8.06844 | -43.12224 | 2025-05-25 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 61000c18-b521-3e2e-ac44-95afec0ce606 | -7.86651 | -48.05547 | 2025-05-25 05:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e013e361-623b-3ceb-8b92-6f5ce118e471 | -8.72953 | -47.99261 | 2025-05-25 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b1842f9-19d9-38b8-a130-ab4c00f96ace | -11.75963 | -47.2605 | 2025-05-25 05:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa07cc13-b476-3199-a6d1-b09fb0a8feab | -11.61589 | -47.99847 | 2025-05-25 05:06:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 597b15ac-dffd-3807-a405-950d296850fa | -11.57143 | -47.61526 | 2025-05-25 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc9b7ba2-ba98-3330-81c7-c7a7838c5bf5 | -10.36734 | -47.98272 | 2025-05-25 05:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 342e3826-8e0b-3c52-b3ea-33916e1586fe | -7.20673 | -43.12957 | 2025-05-25 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3e7b1715-4160-3e1e-bd9b-f1daaa401386 | -11.57686 | -47.61598 | 2025-05-25 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f21f34f9-04f8-307d-8070-1b4c1d1dd534 | -11.57644 | -47.61945 | 2025-05-25 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c74b2f6-0456-3917-9916-3ac37b11d65c | -10.93805 | -55.31586 | 2025-05-25 05:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ffc1855-dc6d-32d7-8a39-9520706d0561 | -11.13659 | -53.92883 | 2025-05-25 05:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aefbcde-2f16-3fe0-9a1c-9d37824317ae | -7.21433 | -43.12443 | 2025-05-25 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b2a0a67b-ce18-358b-8d9c-451280b69ea2 | -6.55597 | -44.49625 | 2025-05-25 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7611821a-5a8b-381f-9030-8623ba60cb3c | -8.05997 | -43.1338 | 2025-05-25 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 55068337-4dfc-39bb-be6d-f545230caf02 | -7.6536 | -46.10527 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 77890edf-af0c-3a37-8eb4-5bba1c19b516 | -10.72635 | -52.47015 | 2025-05-25 05:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 812f599f-d292-3f6a-8925-c00d21ff13b6 | -7.22872 | -43.12038 | 2025-05-25 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a1fb183b-0f09-31fc-8abb-7be93da12cdd | -8.05919 | -43.13993 | 2025-05-25 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 50dbbc19-c7f6-352d-8518-e357c4f201f8 | -11.56976 | -47.61572 | 2025-05-25 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ef46f4a-1543-3777-82b4-b52ee828be03 | -8.06686 | -43.13463 | 2025-05-25 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 349e9158-d912-32ad-a9c1-bc23dd34003a | -10.36371 | -47.96967 | 2025-05-25 05:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb964a96-bc2c-37c9-a4f6-e9b03d142509 | -7.66548 | -46.10308 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0687a052-018f-3a0f-963c-d605ec799ea6 | -11.14391 | -48.10921 | 2025-05-25 05:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c660fdce-43cc-3774-861d-dbdca052848f | -7.22953 | -43.11425 | 2025-05-25 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f1be3455-233e-3a76-8662-a88ca391971d | -10.35852 | -47.96875 | 2025-05-25 05:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| acbd6782-f421-313c-94a3-e30ae86f4a32 | -6.63473 | -55.01181 | 2025-05-25 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 953081ee-1300-377d-8235-2b92f469046c | -7.65462 | -46.09762 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0c3c23dd-f8f3-3d0e-b117-32ef1872ca8d | -6.55385 | -44.49481 | 2025-05-25 05:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3895ecb-09e0-34d5-96fa-a8adeb91a59d | -11.5702 | -47.6123 | 2025-05-25 05:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 80b9e486-605d-39cc-801c-f4f8309eed67 | -11.13682 | -53.91772 | 2025-05-25 05:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66fa92cd-923e-3f3e-8368-d73ffa7f7fda | -8.44014 | -49.62694 | 2025-05-25 05:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f881f877-d266-3e42-aade-61aa238c0d30 | -7.66601 | -46.09916 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e730fe33-1e0d-3f51-8177-1c00ed48476b | -8.89642 | -44.78102 | 2025-05-25 05:06:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0df82a5-e1c4-31b2-a2ff-5a7e4cd9b59d | -6.55511 | -44.48522 | 2025-05-25 05:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddc3b045-8382-3b77-9f0c-352d78a59acc | -6.8352 | -44.63252 | 2025-05-25 05:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6103449d-25b1-372c-840a-a09fc8aa327d | -10.74185 | -49.28322 | 2025-05-25 05:06:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f611604-7f29-3b27-9eee-1666d0f8e005 | -7.64844 | -46.10056 | 2025-05-25 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f72baffc-97c4-34b4-bb28-78e4fb3345d5 | -8.72993 | -47.98968 | 2025-05-25 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67bfb903-e2a9-3f10-988b-59627308fbcb | -7.21513 | -43.11824 | 2025-05-25 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f5c182d7-8ab4-3513-b78e-e1cb2618430b | -11.1378 | -53.92051 | 2025-05-25 05:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 455ad333-a112-3289-8495-43835011969e | -5.12446 | -56.11572 | 2025-05-25 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa020e50-a724-3797-8dbc-c7f8ff303514 | -10.37294 | -47.98046 | 2025-05-25 05:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34766499-2e8c-3b8c-876c-132da1c194b4 | -12.37259 | -49.988 | 2025-05-25 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ade8c406-1710-3969-a636-a051db445063 | -17.15553 | -54.00796 | 2025-05-25 05:08:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a913d9b-2477-3364-b360-1b0f493bc180 | -13.3655 | -54.26464 | 2025-05-25 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 832402a3-1a3b-3154-9932-c9831fea5d9f | -11.8883 | -56.41473 | 2025-05-25 05:08:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71dc98c0-24c7-3b6d-8cda-709e6679e7be | -11.46688 | -61.94139 | 2025-05-25 05:08:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a2ca4de-a07f-318c-89a2-3d99c3e160ab | -12.14011 | -54.66278 | 2025-05-25 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3041bb13-7169-3e4e-adfa-3a54fc07133e | -13.09849 | -52.2901 | 2025-05-25 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
