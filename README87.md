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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f52a781-440d-35f1-87e3-c95b103670ed | -9.69496 | -46.82571 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46a03e09-74e6-3e25-b49a-d7dff4b77dab | -9.43479 | -46.71563 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aec9a04f-7617-349c-b56a-9206d0a02fff | -8.04669 | -52.38652 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b407d68f-b4c7-3608-adb0-0e5b38a24aa7 | -9.60352 | -48.04266 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72c3d7d3-2858-37bc-b11b-b62265941c3a | -12.99349 | -48.02501 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 675b5bbd-c6db-33d8-9d66-40b5423d8e45 | -9.06188 | -50.4778 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a540dcb2-42c0-329d-8375-3e753d95c752 | -11.24058 | -49.40974 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3623078a-9b2f-35e8-b204-260694ee6702 | -9.04718 | -50.49673 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 767252e9-c3b8-35a1-b92f-19ffad24e345 | -8.8527 | -47.26719 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bed39060-24b5-302c-80de-1fe582dea06e | -11.76421 | -50.57894 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb5a2ab3-a9ff-38ce-bac8-26b53963bf11 | -9.44512 | -46.71573 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e5cc3a2-bb88-311d-a2b3-213e33257e86 | -8.83627 | -48.09386 | 2025-09-10 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 221a99ca-af74-3abd-8e5c-8e8c51b4ae78 | -10.02476 | -51.66034 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 475bd5c7-dc9a-392d-ab7a-7a02d300d174 | -9.44836 | -46.69869 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e543e149-e30d-3bd5-aacc-cf9f96242e7b | -7.31111 | -44.15595 | 2025-09-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17d22867-a190-30e2-9e98-8d02d41b854a | -8.85659 | -47.23716 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f122b5a5-2d31-3e94-8129-30bd850819f9 | -10.56136 | -51.99314 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1b77662-51c9-36b5-9f36-62445cccba14 | -11.45096 | -43.61785 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0054990-59fe-3da6-9680-6d7012c3aa81 | -8.25813 | -49.92892 | 2025-09-10 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72d9be29-0bde-399b-bbe6-6306d560205c | -8.84772 | -47.27226 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2f1b11b-5799-3f4f-8e13-e08e663c880f | -11.11343 | -48.41095 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fb7ee16-e4f0-3c58-b617-09d8d88a268e | -13.00258 | -45.21339 | 2025-09-10 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 269bcfbb-0f93-3136-bff1-13242ddba07c | -9.07496 | -46.97081 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 132ad1b4-e16a-3e75-b62d-1a0e87905265 | -8.01993 | -44.50327 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e632c6e-b7bd-37af-a3cb-c0b33b7a877f | -11.66702 | -46.91016 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a29d05a-7793-33f2-8a5b-e1708386fac5 | -10.01932 | -48.09664 | 2025-09-10 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 692586c5-c917-3945-8a0f-49af5dbca16c | -7.78187 | -46.06134 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65ade0d9-1c0b-3fd7-8a54-58a4c51433f8 | -9.53221 | -48.26439 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6bc9bcb6-c867-37ca-9cca-210f2646bd54 | -9.08787 | -47.05648 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ef6a319-9bbc-32e0-94f1-de870c52d51d | -10.01263 | -51.68805 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8cd91a2e-8f94-32a8-b2ae-ae0c77e9c995 | -12.01472 | -50.98752 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 6e27ec96-6dda-31fc-8c77-f09f8cb1bb66 | -9.05161 | -50.4891 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4b7f2b7-4182-3d50-bca8-cfc0ad4c11c5 | -9.01182 | -49.54148 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1b7fba8-86d7-3beb-a19f-bb9253817c3e | -11.1785 | -48.3732 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef98374b-f164-3006-937e-824d8c4d91de | -10.01417 | -51.70587 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07764cae-9445-3d42-b113-6e6d2a384f41 | -9.80357 | -47.79678 | 2025-09-10 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0023772-0698-370d-aaa9-df5bdd15b93e | -9.52718 | -48.26388 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e860f47c-0133-3b14-9155-14ed60b5b41f | -6.68322 | -44.55321 | 2025-09-10 05:04:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f4f67940-e065-3195-8b61-2b01cc2b2359 | -6.53827 | -44.78461 | 2025-09-10 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ef5050a-6e0a-30e4-8b1a-3084334d3218 | -12.04416 | -51.02962 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| c0e6db8f-ad14-3383-838f-25f80bc53358 | -9.06122 | -45.77359 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5261caf9-9d0c-3f13-b193-ca5538b93580 | -8.84781 | -47.26316 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ca095af-59ac-3072-b730-593a2f089807 | -9.51452 | -54.64163 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 31081682-ac2d-3fab-bd7f-ebd7b28ea2ff | -8.05147 | -52.32777 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6359e28-d1a4-3c41-bb3d-c50e29a5726c | -9.38717 | -49.22316 | 2025-09-10 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 531f03a6-89cf-3ed8-a411-179dbcff933c | -11.1941 | -48.37275 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 030297b9-a455-3e2e-b059-70f44c16c091 | -12.18332 | -50.62597 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 28f939d7-b7eb-33d8-9e6b-e8cdda11f1fd | -8.0644 | -50.1893 | 2025-09-10 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1fee70c-6094-3ee1-9968-c60c6b00549a | -12.82786 | -52.93487 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64a81ce7-5bbf-3cd6-8ff3-81087d5bdeed | -12.88341 | -47.96642 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 439ab6b1-b7ee-3a75-bcde-1453e2651773 | -10.19599 | -46.80842 | 2025-09-10 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed7bba79-660f-352f-b6c1-82ba602a2247 | -12.86687 | -47.96828 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 875f14f6-d4cf-3bb9-b591-7efb96f3a7d5 | -9.06065 | -49.83334 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7121645-081d-3bb2-957a-3dce4f2e12b1 | -6.84641 | -47.93938 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28ca85d0-bc43-3444-9492-8ce29aa7fe72 | -10.01616 | -51.69198 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d1ef090a-8042-3eae-a43c-723291aff2f6 | -12.05108 | -51.04322 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0af117cf-fa3b-3d33-b6df-88f5118e81ac | -7.37012 | -47.43694 | 2025-09-10 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6e8536c-6e49-3532-95ff-f7d9534b73e6 | -7.74437 | -50.74111 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00273e6c-896d-3e10-91a6-8db6d56041c6 | -12.1849 | -53.86954 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f662a4a3-6535-37b1-a875-025a76c91165 | -11.33366 | -46.53455 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74b53de5-1d28-3d70-b558-5ed0af65729d | -11.20845 | -54.98607 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a78ca2df-853f-3184-97e2-7fb4370c1de9 | -11.24481 | -49.40863 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c08ca065-a19b-35d0-bc85-24b4d8d4bb13 | -6.86794 | -47.89309 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5c992ce-6a5f-3e82-b54a-6edc9f55fae4 | -13.17649 | -47.25792 | 2025-09-10 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bd5c84b-38b8-3f1e-8ca4-3d1215f6c3a8 | -13.18808 | -47.25669 | 2025-09-10 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 967792f4-0920-31e5-93dc-253ebf63f7f2 | -9.03278 | -49.78597 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| db52a121-affe-3b83-94ea-b0ce2f8e0294 | -9.09808 | -46.97675 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2a62f30a-e6e9-3c68-84d8-8b3121ee3484 | -8.06405 | -48.6604 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b568a0fd-d113-3647-b7e3-9bdf3caa9bfe | -8.57482 | -48.95263 | 2025-09-10 05:04:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 405feae2-031e-3b42-b4af-f7caf6c372ed | -10.95266 | -46.80392 | 2025-09-10 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f8fdb1f-f350-38de-a7c8-4e16f6ed5de9 | -7.73875 | -50.75104 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 63857413-f2ea-3fb0-9976-1349fdf577f7 | -6.85812 | -47.8912 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c461ecb5-ee6e-3c19-a1a3-8083594283e7 | -10.46776 | -47.94513 | 2025-09-10 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d91d2c1b-cd7f-320c-b783-834feaec5c62 | -11.41998 | -43.58126 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c245695f-1a5f-389d-9e40-fe70d85dcb25 | -9.56607 | -48.01265 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 162a942f-20f2-367f-bff8-351296f615bd | -8.51851 | -45.721 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10bf4491-7be5-3221-a535-e1ccf4aa414b | -13.03063 | -48.0165 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41ee8292-d6bf-31fe-a105-65a5f6385763 | -11.11376 | -48.44801 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2ca0223-e0f5-33b7-8ca2-1d6ddde1ba57 | -10.71786 | -48.28246 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e22062c-dd09-33c0-b54d-13be8172cb6a | -11.1653 | -48.35464 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| faf24899-244a-3e67-bd7d-ef68cb7e58c5 | -9.99874 | -51.69969 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bf9e8cc-5b17-3527-a19c-9cf106365abe | -8.48808 | -51.33809 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b92cfbc3-649e-3a1e-9a91-77a2d737087c | -11.3178 | -46.52044 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ea3fb2d-a5a0-3d46-8cf0-2b5f2303018b | -10.02376 | -51.66735 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 57f67a3a-82a2-322e-82aa-23efb7f9425c | -9.00719 | -46.06058 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b39a86a8-5c74-3f41-b501-8498585b22d9 | -12.00609 | -50.98631 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 19436045-a1ec-3122-b17e-1317a87400c1 | -7.88291 | -46.27139 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d67405d9-ef91-3045-b9de-e3af209467e3 | -11.46574 | -49.24741 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f5290d5-15c5-3054-8a2a-236691b4f348 | -6.52749 | -51.05436 | 2025-09-10 05:04:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ce7cb5f-be4a-3cfb-a558-96d3d8252aab | -11.43573 | -43.62892 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 39a2e995-a1c7-3e83-a75b-d0428ef54bcb | -11.81432 | -46.75826 | 2025-09-10 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc1fde29-ff09-3344-bfd3-bb77c7d5e341 | -6.48545 | -55.52279 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 381a3eaf-7a8a-355f-b190-66d87c9d1397 | -10.27131 | -48.81056 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67a66d82-646b-3254-9a36-e03d0f69cbb2 | -12.84257 | -52.942 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00587f29-1619-3d1f-a383-36b9ca97e583 | -9.04793 | -50.48417 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a29f8a63-b89a-34eb-b9ed-c906f5eeb2df | -9.51396 | -54.64529 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ce40fb1-4829-3675-a335-bbb90c6a60fd | -7.25219 | -44.45351 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5faebb75-5133-3e48-951d-9ef30e7de1aa | -8.06865 | -50.19024 | 2025-09-10 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 73e4ef6b-3122-3c27-8af5-04b580cabac3 | -12.0436 | -51.03375 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| aea0f548-5766-38d6-a6fa-be676ba84873 | -10.57284 | -52.04916 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README88.md)
