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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15fdfcf4-910e-350a-bf0d-2cab14856cc7 | -3.60553 | -55.46791 | 2025-11-24 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 721733ea-3abd-340a-a0ef-f9dc7c54e864 | -4.5285 | -45.61673 | 2025-11-24 04:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 476d497b-bc4c-31f5-b04a-ad387db8b47c | -8.72793 | -48.02931 | 2025-11-24 04:57:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff34ca64-b6e0-39b4-91f9-416e5a5fe1fb | -4.52299 | -45.61928 | 2025-11-24 04:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9b26d2a-0f7f-3b9d-94df-068fe1b6de17 | -8.72526 | -48.02717 | 2025-11-24 04:57:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 167f19d8-d91c-35b5-b6e8-208ca6af86c3 | -4.16617 | -48.59138 | 2025-11-24 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 079fb664-3807-3f56-912e-0470e46bdbc0 | -3.72481 | -50.4771 | 2025-11-24 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 522175c1-f0ef-3514-8fc3-a66425a0728d | -4.16672 | -48.58776 | 2025-11-24 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1151f2f9-2f30-377f-b568-66d44e464978 | -4.31126 | -50.74216 | 2025-11-24 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13894462-6ee6-3eb9-9dfe-7738f88e1727 | -4.06362 | -50.98338 | 2025-11-24 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9757ce8-8eb2-36a5-bcb2-608bd819fa07 | -3.09839 | -51.5044 | 2025-11-24 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ec80cf9-5663-3b24-be32-f412799b0a37 | -4.44976 | -44.32588 | 2025-11-24 04:57:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 705384c4-632d-3ee1-8e23-368e8a7db3ba | -3.43052 | -52.62966 | 2025-11-24 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee70f4fa-8016-38bb-91bc-963a78d535ce | -2.98563 | -52.62842 | 2025-11-24 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5b81911-23d5-3eaa-a2da-e225b9d8111a | -4.16212 | -48.59071 | 2025-11-24 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 677cffa9-61f4-3ae9-85e7-0dfcf4444ec3 | -4.10988 | -49.06794 | 2025-11-24 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cc1da61-6f53-36e7-a219-ed030fa74d07 | -4.8299 | -43.83117 | 2025-11-24 04:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a462a42d-ef48-3a73-86f1-3b6f7070c6cc | -8.65919 | -47.85894 | 2025-11-24 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61323072-fea2-36f6-a070-d8d043a79300 | -8.14985 | -46.81494 | 2025-11-24 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21170608-7c39-3d9e-a390-415f3b278a59 | -4.82115 | -43.83394 | 2025-11-24 04:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f871e566-5852-39e1-b1fe-25d26469a9f0 | -7.29519 | -45.43715 | 2025-11-24 04:57:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edc34a04-557b-3fbf-9808-8ae44db338fe | -3.96407 | -50.3295 | 2025-11-24 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f833968d-dd02-310d-afe6-f175b25e917d | -4.23916 | -48.90344 | 2025-11-24 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da5c0f84-02fb-37b5-a5aa-c098cc041361 | -4.10518 | -49.07232 | 2025-11-24 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ca1e8b6-7501-34e8-b861-acac93de421c | -3.40983 | -49.46778 | 2025-11-24 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 062a10fb-6463-34c2-b843-760d580135af | -4.44925 | -44.32945 | 2025-11-24 04:57:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c0506e1a-e041-3e5f-bb54-3dafdea715be | -5.93528 | -45.58062 | 2025-11-24 04:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f778b25b-8d5d-3592-aadc-e8a534aa133b | -4.2124 | -48.69949 | 2025-11-24 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e93732fc-9375-34c5-ab18-909f408c23dd | -8.58498 | -54.61087 | 2025-11-24 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14f9a379-391d-3a36-aaff-36ec0ddbbe2b | -2.85833 | -53.00594 | 2025-11-24 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c99f2f5-7e88-370b-989f-135fba82725f | -4.31413 | -50.10035 | 2025-11-24 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88299b3f-aa38-309f-8815-90a322ad3aad | -4.16266 | -48.58712 | 2025-11-24 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e886336-ea75-36f9-a556-649edd70f951 | -4.31944 | -55.38833 | 2025-11-24 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4013c822-8b07-36c6-a870-98abb9e03a84 | -4.52386 | -45.61346 | 2025-11-24 04:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3691417e-7c04-3e7b-89e9-8a4c044785db | -4.61797 | -45.63525 | 2025-11-24 04:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b406b087-622f-3585-a728-d86fb984f26f | -4.16504 | -50.40957 | 2025-11-24 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f3d4ef2-07f3-3885-86f6-874661c2d57c | -2.86163 | -53.00645 | 2025-11-24 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 965f69de-500d-38df-ae4c-3091c775ee3a | -8.14751 | -46.81614 | 2025-11-24 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88b272a9-c7b6-3685-bbcf-e098ffc8f319 | -4.21644 | -48.70013 | 2025-11-24 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32d420f2-376f-37ad-89f8-e7cfc19c9e6c | -3.74109 | -50.96413 | 2025-11-24 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 193799b6-23ae-307a-a8d8-5fb2a41d7462 | -5.93571 | -45.57763 | 2025-11-24 04:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae3072de-3d90-3988-ac5f-e1e7ba477675 | -3.62081 | -52.49672 | 2025-11-24 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd33dcbe-b36a-331c-b039-aeacfb5b9577 | -4.66341 | -46.05373 | 2025-11-24 04:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 432936b3-f33a-311e-b9b5-deae5bf0e172 | -5.18266 | -60.30519 | 2025-11-24 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6768174-9038-308a-9576-71927183c4e8 | -7.30047 | -45.43795 | 2025-11-24 04:57:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc4dae91-0687-3387-99a1-baa709163af9 | -4.81744 | -43.83722 | 2025-11-24 04:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5ecdb4b7-86da-3765-a742-eb366c9d66a2 | -5.0738 | -49.99917 | 2025-11-24 04:57:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a17996f0-9640-33ce-b3c4-58e2b537620d | -4.16375 | -48.57989 | 2025-11-24 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0034322f-f1e8-3efa-8e72-3479e3b918a1 | -8.67548 | -47.8423 | 2025-11-24 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40372382-0bb8-3669-8a22-ae636aac91e8 | -3.96772 | -50.33006 | 2025-11-24 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42b359cb-32d0-311e-ac10-ee06c33193c0 | -3.49003 | -54.04233 | 2025-11-24 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92afd804-f6d4-3cb6-b8b4-2e340a1b433a | -2.95776 | -53.28209 | 2025-11-24 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e335a82a-1f34-3c71-adf7-7a6662998912 | -6.55033 | -43.21306 | 2025-11-24 04:57:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fde44432-1487-3657-ab47-76b1d64ef973 | -4.62661 | -48.65578 | 2025-11-24 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f2a0d8c-1f8c-39e2-9949-4f30468206c7 | -3.85768 | -48.98431 | 2025-11-24 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15fd16c1-9211-3ef9-b528-25d38a39f476 | -2.86218 | -53.003 | 2025-11-24 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a85eb4c9-1ab9-3088-811c-1639f232dd59 | -8.65983 | -47.85427 | 2025-11-24 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08533e9c-e0bb-3b6d-8469-60f74a2c7fba | -4.15969 | -48.57927 | 2025-11-24 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b39c7e2-1105-3cf2-8f2c-ebd0ec3649c9 | -4.52892 | -45.61388 | 2025-11-24 04:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8798f4d0-7c1d-3ff1-b15f-a8e539b6c079 | -2.92996 | -52.72308 | 2025-11-24 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af847790-879d-31ef-819c-fa844969bc72 | -4.71109 | -46.45874 | 2025-11-24 04:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 50c2498d-4561-3fb2-a149-54e42d7b0be8 | -3.5559 | -53.12903 | 2025-11-24 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1b28d327-3d6d-3ac8-905e-f553af050688 | -3.76353 | -50.39331 | 2025-11-24 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1651b9f3-5c32-3073-805f-3fa69dca2e4c | -3.42997 | -52.63314 | 2025-11-24 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 919eba26-7e31-32ed-874f-f64ef92d9ca9 | -3.81665 | -53.73805 | 2025-11-24 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95df23b0-3b73-3456-a9ca-f11583660206 | -4.81854 | -43.82941 | 2025-11-24 04:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e085d9a3-c04c-3e26-ad07-48b82912d52c | -3.74065 | -50.9647 | 2025-11-24 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e66ab57-70cf-3e42-90e9-01df69a06023 | -5.81852 | -48.68433 | 2025-11-24 04:57:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bbeee07-cb16-344e-9bb7-590dda8e1d4d | -4.82173 | -43.83003 | 2025-11-24 04:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4d7de2b7-281f-352b-97da-1516c8a21163 | -3.48078 | -53.9699 | 2025-11-24 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 582e9ea5-568f-3693-94d9-99218946327d | -8.67091 | -47.84158 | 2025-11-24 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f19fe0a-d3a6-3f72-9515-d888a39b5209 | -4.16321 | -48.5835 | 2025-11-24 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 007e25b4-92b5-3239-855c-f8dbc9df6916 | -4.81489 | -43.83697 | 2025-11-24 04:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c547702-13c0-3c7c-b9e7-027e97a6a092 | -4.81547 | -43.83307 | 2025-11-24 04:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01245899-f32e-3a20-b724-e122f981977e | -3.73883 | -48.8652 | 2025-11-24 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbe824bf-74fc-3212-be86-123b21612a5e | -5.81799 | -48.68807 | 2025-11-24 04:57:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed1ad576-eb2e-3b49-97f5-16b8dc61a7b1 | -3.48409 | -53.97042 | 2025-11-24 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d69afde-7d3e-3748-9eb8-9e4688dd4c60 | -4.62301 | -45.63585 | 2025-11-24 04:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d17b2dc9-4442-3169-ab36-c079c0cb2ce8 | -8.14826 | -46.8106 | 2025-11-24 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ce0c1b2-4ea2-3371-996b-8893c533c861 | -4.81799 | -43.83332 | 2025-11-24 04:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f6f6e5a-6456-3dee-b454-60c0764091b6 | -4.52343 | -45.61637 | 2025-11-24 04:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed19590a-c0e2-3372-9fec-168e0f12fb70 | -2.95722 | -53.28553 | 2025-11-24 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04813198-a834-3966-b7a4-838f9cc5c2cd | -16.33466 | -50.88967 | 2025-11-24 04:59:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e505f1b4-560e-3181-891a-e25f834aa700 | -15.6716 | -52.63954 | 2025-11-24 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c5a37cf-add1-39a6-ba6f-5f9752e84785 | -11.5187 | -49.67887 | 2025-11-24 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 862e74b1-0874-39af-ba24-e3de147cf070 | -16.76271 | -51.35253 | 2025-11-24 04:59:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7781f814-6e82-36af-a037-d399a11cb7f3 | -11.52291 | -49.67949 | 2025-11-24 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c0983633-8867-3396-b5a4-792f6d03bb1b | -11.51817 | -49.6828 | 2025-11-24 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a684515d-dfc0-3dc6-8b87-4d53daa39295 | -12.28761 | -51.20689 | 2025-11-24 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67955734-b29e-39d1-a96b-ffd9806cf493 | -17.13467 | -50.26271 | 2025-11-24 04:59:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55a42d2e-1a5f-315e-aa89-0f4d80329b36 | -17.13455 | -50.26507 | 2025-11-24 04:59:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3453661b-a8c4-3518-b705-b285cf38478e | -16.76678 | -51.35302 | 2025-11-24 04:59:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2335701e-b2f2-3882-9eb0-76b5a6beedac | -11.52712 | -49.6801 | 2025-11-24 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad731961-b107-3857-81a4-bf2903278b5b | -17.13411 | -50.26709 | 2025-11-24 04:59:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0229d6df-d491-30e4-8e50-3445e834bd4e | -16.02037 | -57.08507 | 2025-11-24 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15ca7cfb-cff5-3eea-90e7-32009b3aa596 | -16.76627 | -51.35682 | 2025-11-24 04:59:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f519abfc-f8b3-383a-92d3-fe4307bd7d12 | -19.18196 | -57.32894 | 2025-11-24 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 46959fb2-cb6b-3e0f-a430-41a7f4d02b87 | -19.18139 | -57.33258 | 2025-11-24 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9d800a5e-a054-3e9f-8663-35076e38549c | -17.04915 | -52.74759 | 2025-11-24 05:01:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6621bee4-271b-32c9-a5bf-c80651a18bd8 | -17.5423 | -54.04122 | 2025-11-24 05:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README13.md)
