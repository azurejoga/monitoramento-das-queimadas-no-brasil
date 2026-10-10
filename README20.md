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
| e54e4b05-635f-3397-aff4-60c5bf4b7a6c | -12.2906 | -63.381599 | 2026-10-10 01:47:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 822a34dc-a7d0-3e57-a4df-fa4ea563649a | -7.5699 | -61.538101 | 2026-10-10 01:47:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44b6c12b-839f-3a5c-b1fe-0b084330e08e | -7.9112 | -54.7229 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66242304-cf4e-3907-97d8-63c63d197fd1 | -3.9962 | -59.361099 | 2026-10-10 01:47:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 090c7259-c4fd-334b-8da5-0075560c97b6 | -3.1684 | -58.608799 | 2026-10-10 01:47:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1969a016-bfd8-3bd9-866a-f1775df767c0 | -7.5023 | -54.965599 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d92cef20-c5f8-3cca-a5f2-6ef85cbbf990 | 2.7205 | -60.259701 | 2026-10-10 01:47:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ec0e9489-2d8f-3a98-b464-dedc8d253052 | -3.983 | -59.348999 | 2026-10-10 01:47:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5590f8-efac-397f-b5dd-3fe034bdff25 | -12.3069 | -63.362701 | 2026-10-10 01:47:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c585bf59-3a63-3722-9c59-560bd4ccf648 | -8.709 | -62.376202 | 2026-10-10 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7a720c1-5e7e-3745-8196-15b64f8040c1 | -6.4414 | -55.264801 | 2026-10-10 01:47:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fc9b766-8fc0-31cf-aa60-9dd37b09d10b | -3.1199 | -54.145302 | 2026-10-10 01:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc3d9ca3-718e-33ce-94b7-8d172a108fa6 | -12.2923 | -63.388802 | 2026-10-10 01:47:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2b66824a-701c-3062-81eb-68caf94e054f | -12.3053 | -63.355598 | 2026-10-10 01:47:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4160f559-04cb-3c3a-92bf-af6cbcbb69cf | -12.2988 | -63.3722 | 2026-10-10 01:47:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0f5a083a-5ab6-3efd-9c64-12a363cc6816 | -3.0348 | -59.1642 | 2026-10-10 01:47:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 143b5c62-0498-32da-8016-c8310ee6caeb | -7.9256 | -63.699799 | 2026-10-10 01:47:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51cd9ae5-21ce-3475-a370-c21de6b94cc8 | -8.6953 | -62.4053 | 2026-10-10 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65f5f9d6-085e-3fd0-bc4d-ccc419036aad | -8.5661 | -66.994301 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6329f0c9-bd62-30a2-8b8d-608b57465158 | -4.5936 | -55.7276 | 2026-10-10 01:47:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bdd7b0c-3ef3-3f6a-a016-2a75f70f793f | 1.9772 | -60.6077 | 2026-10-10 01:47:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e762b0b6-6fa7-3231-8b9b-12bbc25dd541 | -6.4318 | -55.2672 | 2026-10-10 01:47:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9f7a824-062a-3be5-963a-638d6242ab4f | -8.6205 | -66.778297 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d87a85d5-bdf4-32d0-a9d6-16c83e400ced | -8.5219 | -67.027 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9429ad1-72f1-370d-92ad-325feab48bd5 | 2.7302 | -60.261799 | 2026-10-10 01:47:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b1903d36-54da-36ea-b8f1-f6dbe66f2541 | -8.6656 | -67.117302 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f9b0f32-822f-3d8d-b15c-a6ab8b394480 | -8.7012 | -62.3867 | 2026-10-10 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fb33fc39-36b6-3ff7-bc79-3f16ebce94d0 | -3.7342 | -59.4683 | 2026-10-10 01:47:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71e42e8c-2c4c-37f8-89d9-acbe4ac67372 | -8.6303 | -66.7761 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30ffbe64-295d-38a2-8f34-93ec6c6ff779 | -0.0002 | -60.566399 | 2026-10-10 01:47:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8ae7da83-8674-30b6-922d-c5c81b5d0e1c | -8.5416 | -66.976997 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de4cfd38-1e2f-30c5-b899-39ed00b89185 | -6.8141 | -59.308899 | 2026-10-10 01:47:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8cfc211e-4ac2-3f85-b0ea-b0bd1efd6418 | -3.8496 | -55.775799 | 2026-10-10 01:47:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 614d56c7-71ba-38e0-8bf0-befe89f7d596 | -10.6203 | -60.479198 | 2026-10-10 01:47:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f8e27b4-e8b3-3880-a7ac-7c7e72801dda | -8.6493 | -67.182404 | 2026-10-10 01:47:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6024af08-c907-3f9d-9b64-f8bfaf81c175 | -8.7109 | -62.384399 | 2026-10-10 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c2007778-f75b-3bf8-9399-2ee1674498d8 | -6.9341 | -59.2519 | 2026-10-10 01:47:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26550c6e-fd49-3a64-8b58-d2cd9b4ba633 | -8.6836 | -62.399399 | 2026-10-10 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 67e48bb9-6de2-3a98-b1bf-75a8cbfc9063 | -3.5482 | -54.7243 | 2026-10-10 01:47:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd02d1fe-be6a-36e5-b0d5-93e08cabcca9 | -9.3762 | -64.660698 | 2026-10-10 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b690b643-01e4-36a3-8a61-636db1b634ea | -7.9274 | -63.7071 | 2026-10-10 01:47:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a655dca-f168-3ca6-92db-5ae05e50e492 | -4.5873 | -55.702499 | 2026-10-10 01:47:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82ee7d55-7041-32d7-8f04-06eea8179f8c | -6.4565 | -55.043301 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50e07025-3057-3748-b1ed-e67aefc5a05f | -7.4585 | -63.644299 | 2026-10-10 01:47:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed53db0-e831-36d4-ab80-e66747a81fbb | -3.9093 | -58.957802 | 2026-10-10 01:47:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8588a0f6-15e7-3cd7-8c01-b1612e962cbd | -5.1906 | -60.305199 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21ca890a-3e5b-3b6c-9258-06dabb592ab8 | -10.6008 | -60.484001 | 2026-10-10 01:47:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 859458be-2525-37ec-925d-c17a0bdd31e6 | -5.2454 | -60.1908 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49e450c4-7c94-3e85-9542-88516f658200 | -6.4885 | -62.854099 | 2026-10-10 01:47:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb9166cd-8cee-3027-ac69-c382e8ad30b8 | -3.1861 | -58.639801 | 2026-10-10 01:47:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa2e14be-15ae-3cd3-a8dc-2eae22d66161 | -10.5961 | -60.4645 | 2026-10-10 01:47:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0eefe65e-a28d-389b-bfd3-a3fed8ef2ce4 | -6.4373 | -55.0481 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cae21d1-782a-3797-b303-8d74bf8b2617 | -6.4823 | -55.064301 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3f2225c-534e-3d96-bb19-70ff2363fecd | -7.9239 | -63.692402 | 2026-10-10 01:47:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c210cf36-6bbc-3055-86e9-6ac8dfca400f | -9.2604 | -62.305698 | 2026-10-10 01:47:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 099b779d-060b-385b-8d91-0b510c54b38f | -10.6106 | -60.481602 | 2026-10-10 01:47:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0eed355e-d12b-3be3-ab39-6b9f1a7bd4f8 | -6.4402 | -55.0196 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f29474e8-6e3e-3745-b02c-144d2eb2d57f | -3.8559 | -55.801399 | 2026-10-10 01:47:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdd73afa-f668-30e2-b6f5-bd2b02be0338 | -7.8903 | -63.769798 | 2026-10-10 01:47:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0d497ac-f5a4-387b-b245-b48c80aea1df | -7.5088 | -54.990799 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f631372-f254-3f40-8759-44b792ccbec3 | -8.5302 | -66.972 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| deb66274-02a6-348b-b84a-37395c0c8263 | -8.5318 | -66.979202 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 693215ea-e6d7-359f-bd36-73e48785eef5 | -5.1877 | -60.293301 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e965f9af-bf0a-3f6f-80a9-a7a981a92e14 | -3.602 | -54.612999 | 2026-10-10 01:47:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8cac54a-5d85-36fa-8d53-500bb209a5fb | -12.289 | -63.3745 | 2026-10-10 01:47:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1ea82399-781c-3a7e-98d4-edf31a0fe956 | -2.9508 | -54.0774 | 2026-10-10 01:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc342586-3a9c-3520-9981-893a0b8268de | -8.6914 | -62.389 | 2026-10-10 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c6c97b33-05d1-38bc-8f88-cf473124d05b | -12.2955 | -63.357899 | 2026-10-10 01:47:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be1fd9a9-9c13-3980-935d-6a6490cd1d64 | -3.5943 | -54.581902 | 2026-10-10 01:47:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a64024d-af7e-3b4c-bbb8-64f32e0dc54a | -3.9927 | -59.346699 | 2026-10-10 01:47:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 308e0039-91f8-342e-9b85-6e56b1b4fab0 | -3.9056 | -58.942402 | 2026-10-10 01:47:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce78700-985d-31de-842d-46c966eff7c4 | -7.5831 | -64.579903 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 580a6b5e-2b1d-39c9-93c6-d53a58c681ee | -12.3004 | -63.379299 | 2026-10-10 01:47:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 61468735-4a5e-3b63-89e8-a6de5fab6072 | -3.88 | -55.981701 | 2026-10-10 01:47:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18cff3ea-09f3-342d-9eed-bafaad6d978b | -6.4469 | -55.0457 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6768c71e-fb6f-3cc6-86e0-43c62159bb1b | -9.6018 | -61.8298 | 2026-10-10 01:47:00 | METOP-C | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9070c8d0-7c59-3206-a8e0-6c5338e0cd11 | -9.2585 | -62.2976 | 2026-10-10 01:47:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd996f4-e8dd-35c4-aa75-cbcf7e0aae6b | 2.7241 | -60.243801 | 2026-10-10 01:47:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 931f34c3-6604-3103-8c49-9bb43787655e | -5.2199 | -60.041801 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37230daa-9c88-39ab-97d5-791c732453b8 | -8.5252 | -66.995796 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 342778a3-c92d-3d26-aa3b-9367cdb3ebe7 | -3.1284 | -54.179298 | 2026-10-10 01:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f06503ad-8973-387f-a035-c008f90457a6 | -10.6129 | -60.491299 | 2026-10-10 01:47:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d6f0665-2698-33de-8367-c25e58c0d7c9 | -6.4727 | -55.0667 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1c7aaef-89dd-3f76-94a8-40471ce435f9 | -8.7123 | -62.520802 | 2026-10-10 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 07c38a5f-4452-3791-98fc-97e005575084 | -3.1724 | -58.625401 | 2026-10-10 01:47:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 288a2dff-3121-3ad3-b960-504ac2b5be26 | -6.4964 | -62.8437 | 2026-10-10 01:47:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb1babc8-84a0-30ed-88da-ed0eabf8b71f | -3.0311 | -59.1488 | 2026-10-10 01:47:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 258b5369-273c-3d0e-b3ac-bcbfbacdac13 | -5.0895 | -60.227798 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4187dbac-3810-32b4-8a57-b701a29ed22a | -3.84 | -55.778099 | 2026-10-10 01:47:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 319115e5-cf2a-3794-bdd3-6de5c819e533 | -8.5236 | -66.988602 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e29affd9-16ee-397b-b72e-fa8a536c87ec | -3.8463 | -55.803699 | 2026-10-10 01:47:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb074c51-d386-36c2-a87a-a8a9c7e0d7e9 | -12.32 | -63.374699 | 2026-10-10 01:47:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fa034af1-62d1-38c1-a464-cc13ddde842f | -6.2246 | -60.021 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| abdc9383-92d0-31cb-9dc9-c7b684e60551 | -5.0769 | -60.217999 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aaa7b5e2-efd0-3041-ba4d-e85e5af968be | -3.579 | -54.6842 | 2026-10-10 01:47:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc9a282-5a14-33ec-88fd-d3766a44a809 | -5.0964 | -60.213402 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43cc7d9a-9e9f-3b85-93cf-2a5a24fa59cb | -12.2971 | -63.365002 | 2026-10-10 01:47:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e07d2a85-3875-364d-bec4-df6a15e50be1 | -3.9865 | -59.3634 | 2026-10-10 01:47:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e19993a9-0c11-32c3-9c8f-00eec410d5c6 | -3.745 | -58.489799 | 2026-10-10 01:47:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28b70120-6bed-343e-bb13-6609eb3a9728 | -3.6038 | -54.579498 | 2026-10-10 01:47:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README21.md)
