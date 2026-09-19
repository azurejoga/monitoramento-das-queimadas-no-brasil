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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a72bc089-3a15-3710-aaa6-9cb648b45918 | -6.67178 | -50.91003 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07d68e5c-94e4-3341-8de4-54f5d2a25643 | -10.09314 | -45.64606 | 2026-09-19 04:57:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| caf18167-17f7-3b21-b3c1-d5202d9420ac | -3.35856 | -50.45533 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 143d3a9d-07db-325a-8dd9-5fdc7c2939a1 | -7.19684 | -47.8822 | 2026-09-19 04:57:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea0cebfd-d672-3331-bf94-41ec969fc1f3 | -5.86696 | -52.03848 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5a857ad-8a0e-3ea4-96c0-7cc37a315fb4 | -8.98874 | -54.43318 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c697a0e-e980-31f8-8ccc-3f751040be3c | -8.42528 | -54.72454 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60f23668-00b8-39fa-8fbb-6f2528b532e6 | -7.73841 | -47.3053 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b26422aa-65a4-36ac-95ba-e292dcd12095 | -6.00019 | -51.79759 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b599e7fe-332f-3687-b0e4-eadf39c74b98 | -5.75798 | -57.4472 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 30a2358b-d36b-35fa-8a6c-88919a9b9596 | -10.16511 | -48.51941 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e2d74cc-d221-3029-be2a-462d7bc69c54 | -6.98641 | -42.19143 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fa932781-6a55-3642-8108-54938be0167f | -9.32546 | -48.18055 | 2026-09-19 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a38f2045-44c4-3344-b001-45cc0cbbf89c | -6.32192 | -55.28515 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 413c4506-3f37-3213-9d0c-b08b010270a7 | -4.35616 | -47.78254 | 2026-09-19 04:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 97a9229d-ca38-3bcc-af3a-b40f5d85d078 | -3.63888 | -58.61645 | 2026-09-19 04:57:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7516d132-c10d-34ef-87d9-f91f8988da88 | -11.0462 | -48.30469 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bbed941-6387-31b4-9ca9-b953f12e8b13 | -4.08377 | -48.95097 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6ee07b1-fc24-3edd-af88-984e3ca7d536 | -9.90558 | -46.55287 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdaa3ff9-dab5-3d56-b2a9-61dc4161e3b8 | -6.37083 | -58.30962 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e77913a-ff76-30d6-948a-584c21ba7de1 | -9.81967 | -46.39927 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7546c794-ecee-3447-9d56-89471dbcc913 | -11.2997 | -46.77865 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b457233-507c-3de6-9e73-77995bda0ef8 | -8.61075 | -54.60292 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c71af6f-1e3d-3f23-a09c-d086135757f1 | -6.1987 | -57.77476 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e7c495c-0514-3bca-99ae-4a10a966fecf | -10.09637 | -48.42014 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16b107ce-ea00-396b-a2b6-416b6578f8df | -8.81434 | -46.94324 | 2026-09-19 04:57:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9179fee9-7d8c-3018-822b-cde307329a0e | -8.41736 | -54.73066 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d564a2b-5518-3607-a299-d70e9267ce14 | -7.56685 | -57.67225 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 95ba657f-363f-32b5-b430-27a55cec87ff | -8.12288 | -44.82897 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be54ac5c-7a87-32a2-b52e-cad4a4dd5742 | -5.89377 | -53.56289 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a2abe0a-13af-37b6-9f3b-202f27267601 | -6.02115 | -51.76777 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f6ec3e50-d2cb-3d49-a0d7-d7043b28fdd1 | -4.55025 | -54.90965 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8714a45-9eda-380f-b006-2df7460f9001 | -3.18645 | -61.11355 | 2026-09-19 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f565307f-5d4c-3b55-b43c-b65617492932 | -10.63383 | -48.69691 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1431b9ef-af56-357f-b130-706d5aca5241 | -7.59254 | -55.69615 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4f78c82-ab34-3f9a-b844-8f26a6937984 | -3.2623 | -54.26841 | 2026-09-19 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44481b81-86fd-3873-82de-b4a60acfd506 | -10.55595 | -51.31898 | 2026-09-19 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1020cec5-9558-3bd6-b8ff-d45a74fbd0b1 | -7.8555 | -44.87608 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b5950fc1-6093-3e2c-b43d-4b4b5e196f18 | -9.92873 | -46.58884 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 361805bc-5d39-3946-b2d0-8b4b0ea74c90 | -10.49632 | -46.27721 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c65446a0-3bf8-32ae-9624-a732f98e8a61 | -7.06949 | -47.53646 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e8e7116b-e019-3336-bade-d4c77d31f847 | -10.58305 | -46.5438 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ce883fe-b645-3f0c-9f34-fdfc41e1ea3f | -6.29048 | -56.03888 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 493fc56e-11c6-3b3f-a6a7-3df15dc875c7 | -6.98878 | -42.17451 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2fce6d6e-ef58-339c-8c60-2f0684359f0a | -10.97174 | -49.73996 | 2026-09-19 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f96d9c50-2df3-326a-b4cb-66a85eda64c0 | -8.77773 | -46.91856 | 2026-09-19 04:57:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27df35e7-30fc-32e4-95fd-9896d2ad6533 | -2.84772 | -57.63767 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b2c77b7-1ef4-33cc-ad56-4f022c1782c4 | -8.63607 | -47.54057 | 2026-09-19 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 354c4420-af44-3cad-abc4-a669fa3b9884 | -10.17571 | -48.53203 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3aa268a0-60e6-307b-b13e-59583466eb5e | -6.65751 | -50.91158 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e7280d1-7ad2-36be-97c7-f32ede8a8237 | -5.89654 | -53.56692 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6cdc7636-02dd-3dd6-92d9-66489e5667f4 | -5.86323 | -52.0411 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59d083dd-5835-3638-9a70-42447b183cef | -7.60268 | -45.42883 | 2026-09-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb29482b-2c7a-3e11-beef-aadafe7667f4 | -10.62271 | -48.71743 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56a89278-b295-3ea6-a5cc-82128b9efc1d | -8.29344 | -46.85091 | 2026-09-19 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2562553-cc97-39ce-86dc-86533cb4c1cf | -6.10266 | -57.62649 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a03e756-1d3a-3f08-b4dc-53d6b2cf3a8b | -8.16903 | -54.81347 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a5fa2cc-aba2-3035-b22c-80bfba945250 | -9.8887 | -49.09837 | 2026-09-19 04:57:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f99d1246-0110-37d1-a619-287edeb4e871 | -7.40506 | -49.84808 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c9863d25-cdb4-3a79-bd02-96a0222eafe8 | -5.85714 | -52.03657 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fe65784-bb40-3571-b59e-33c84ccf6bc4 | -8.61294 | -54.61062 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52f0e76f-8239-3596-96e9-6a8123b1ea78 | -9.78892 | -48.33248 | 2026-09-19 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1640b69-9725-3276-846b-bb52d98949c0 | -11.12307 | -45.29525 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5edcd901-0b42-3ac9-a429-0dd4ca0526ac | -9.25138 | -45.92393 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a83ccaf-108e-3d21-b496-ded76789066c | -6.36449 | -58.29689 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe6beaa5-35e6-3611-b587-d1b86b838ec4 | -8.47256 | -47.01374 | 2026-09-19 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 243493e1-ec3d-3f28-8369-892452eefefe | -2.90393 | -57.79671 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d427bd1d-8502-3f81-a87a-8b2bb314f261 | -7.85673 | -44.86724 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 132acc80-afbb-3c0e-9ad8-d1b0e0124663 | -11.07818 | -48.29832 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7cad9033-8765-3c91-b4d3-4a32e3c1b54e | -4.51057 | -55.46632 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30005788-66e0-37ed-aef6-2c2fc6a44815 | -7.69055 | -46.11377 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 633001f8-4198-378a-ac32-8560037e2e22 | -6.00352 | -51.79811 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b50729b-1ff0-39b0-a4b0-e269f8097ac1 | -7.86213 | -46.45083 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ec84e28c-f26a-3935-b130-632b16086762 | -5.88823 | -53.55484 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bb8e2fb-4488-3e4a-a2a4-e2eccce60a1a | -6.66203 | -50.92765 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 318c6b2f-f4db-3813-a0a1-8db923cedbfc | -9.15616 | -49.99988 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a73befd3-b3e4-3ff7-9a6c-6a488099baa5 | -6.64052 | -52.96984 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f9f6632-fe8c-3f0d-902e-0f1d992e30ae | -3.45988 | -50.61161 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c7ab8fe-8ae9-3000-b70c-3c1effed79a0 | -4.71462 | -55.68576 | 2026-09-19 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b44af73-dc85-3eea-b094-f7fa4556a920 | -5.75889 | -57.45084 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ad1a88d-e8ab-3412-9483-5a603a348320 | -7.63468 | -46.11031 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b165d2af-3765-33b4-9263-698485667a4d | -4.85529 | -48.30013 | 2026-09-19 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 843471bd-de7f-3048-8a78-c37e4ad0c681 | -6.02503 | -51.76477 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8a7c8749-76fa-37d9-8cbe-cdc4c5299606 | -10.46726 | -51.25835 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f498db4a-6684-3fe4-9b71-674b1aa85bc6 | -4.56647 | -54.92033 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf74d8ad-b4cb-33d0-9272-c953d9b0f083 | -5.57153 | -52.01638 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 173887c5-2932-37a5-84bb-ccda47c798e8 | -8.77712 | -46.92284 | 2026-09-19 04:57:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5c4b54fb-a26d-31ba-816e-8d7a2871633c | -11.07874 | -48.29425 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c1cdb13f-38c8-3c4a-b71c-cac7777f528f | -6.32363 | -55.28051 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 299fdecb-6281-3a75-a464-6a4705be21c2 | -10.39666 | -48.32258 | 2026-09-19 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdb85c55-29c8-3f2c-b915-c82bce9a18df | -9.35967 | -48.28949 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48a0bee3-92af-31a2-8de9-0f611adcf8ea | -8.46817 | -47.01319 | 2026-09-19 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6d598b22-0156-313d-a030-b2bd7e6a599e | -7.0998 | -46.44498 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4186ee61-2c6a-3eaf-8bf3-cfed82532e54 | -4.83881 | -48.20108 | 2026-09-19 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a45d1bd-519c-3bd1-9429-0fcdaf55403a | -9.69861 | -54.83481 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5b8813e-8d09-33ea-acb5-c22c7221872b | -8.61411 | -54.60346 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9bb51746-9083-35c9-9ce5-e8f28b0ef425 | -9.90765 | -46.5717 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bb2b4c90-4a6f-3c72-a077-36747fc676ff | -5.88525 | -52.05201 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4465b88c-2a67-372d-8994-3f852040b590 | -7.78477 | -44.83438 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a64d0d65-46c3-3bc3-a363-243d9c0228d8 | -6.30111 | -45.68554 | 2026-09-19 04:57:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README84.md)
