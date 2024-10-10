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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d60c5ed4-734f-33b3-9115-970a2074b4df | -7.55504 | -55.36131 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67636ffc-e00e-3206-ab53-45a3014eb331 | -7.55217 | -55.35808 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e54e6e8-1ca0-3b30-9bf3-f5ab7da1ad3a | -7.39639 | -55.43118 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ab8c6d2-a238-37e9-92ee-8dc3cd11f8aa | -7.3956 | -55.43591 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cb2c90a-555b-3591-ba59-7712bd0a9c28 | -7.39335 | -55.42585 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6492f2f2-b5be-34bc-ac11-3202d5e0c5b9 | -7.37728 | -55.42804 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7848b3bb-3c73-3a3b-85fd-97d509852723 | -7.34166 | -55.08132 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64ed0fce-4b15-3981-bec6-b5579705557b | -6.64942 | -54.94815 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e830c409-75aa-354e-86fd-b9ad5eab035f | -6.64666 | -54.94538 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17a10b73-e41a-3bd1-aecf-73d0e9d4264e | -6.64641 | -54.94296 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93530dc6-8aff-3d68-8596-e2a66224f1ea | -6.64567 | -54.94753 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e48ee024-7aae-3aca-bfaa-359d2fc0823d | -6.64191 | -54.94693 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29732969-7dff-33ef-972c-2be2ed0152cb | -6.63741 | -54.95095 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e96b765-119b-3bbc-aeea-cc877d931fe0 | -6.63638 | -55.38096 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca54a9cc-7e62-37e5-a073-effd8c72fd07 | -6.58774 | -55.38775 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bb755cd-fd7f-372c-9c03-ebdd225c5dd0 | -6.58655 | -55.38546 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ec7bfbf-88ce-3ef2-9346-697104a40615 | -6.56106 | -55.39606 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7075cd25-2282-3d3b-9ce3-b97f4e1e1f49 | -6.5572 | -55.39543 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea10b6da-ab0e-3c5a-bdc4-32701692bef9 | -8.91474 | -54.92975 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b424da3-a3fb-3811-b9d4-f759ff8b8c2a | -8.9111 | -54.92913 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 347e7e9f-0141-3295-8083-e5157108ae2c | -8.07364 | -54.7796 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb3a03a2-25f6-3f28-9aeb-6ac41c6d06ea | -8.06493 | -54.78696 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a46df54-1f6f-355f-a365-eaa6d3eaece8 | -8.62715 | -55.26343 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffa360ac-efd6-3f5c-bffd-2a851d5e9d65 | -8.52098 | -54.97533 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30b08a27-d1a8-3ebc-b845-a43d655df5d6 | -8.52026 | -54.97963 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de0f3baa-5257-32dd-bd31-8ae85f0e5601 | -8.49596 | -55.16979 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd20390e-d70d-3854-9fe7-90abcbe44a00 | -8.49226 | -55.16914 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 742d27e6-6bdf-3dfd-99fe-6b9c574ede1c | -8.4893 | -55.16409 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9c37650-e648-3081-ab56-d5cb855a92ed | -8.48855 | -55.16849 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3eae9756-3743-3fe7-822e-b495efed77bb | -8.48559 | -55.16345 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c91caa5-e07b-33ad-87e1-9e2166db6e11 | -8.448 | -55.45511 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9273e3bb-2ddb-37b2-9004-9d08fe1e23e7 | -8.43968 | -55.45844 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a645ef6-7c22-3e58-b7a4-acc16a73d547 | -8.43732 | -55.47237 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2c45ae9b-c915-36f3-a5be-f3e79bb233b4 | -8.30005 | -55.10935 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6949ef8-83d6-3f0f-8d6c-c2b99bb41900 | -8.28866 | -55.38586 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fd9bd31-2b67-320d-8c50-38c55334fbe5 | -8.2879 | -55.39048 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ff82411-df51-3271-8abb-79f3abd9dcba | -8.2849 | -55.38523 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7a0f93f-4463-3fc9-97ad-771bcc9640f8 | -8.28413 | -55.38985 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16fb05bc-e345-3340-a4ba-24d2155901c1 | -8.28114 | -55.3846 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4257059d-9ad8-3223-bea3-0fe4a98ecaec | -8.28037 | -55.3892 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b8bbd48-bb0a-3338-9295-dee823563778 | -8.21796 | -55.24865 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed84ad4a-8dc8-355b-803c-4f618e87dd92 | -8.20972 | -55.25202 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf20c805-0011-34b3-ab0a-a7566d03fc33 | -8.1888 | -55.19297 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4b86e82-e01d-39a6-8e57-acec415390ec | -8.1888 | -55.14695 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bb2dbc1-d49b-32b6-a994-bc219b457565 | -8.13815 | -55.17514 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77091d33-8d81-3a8d-8d57-1cf267544dab | -8.13739 | -55.17962 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0be782bf-4064-3b6e-91a2-b6bb197cef59 | -8.13722 | -55.17249 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ecc872e-ba0c-301f-bdf8-7748f78f6a91 | -8.13648 | -55.17698 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f690783a-7da9-380b-874c-0ae186812214 | -8.13575 | -55.18146 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 511ddef6-c176-329d-9048-637e1c82f355 | -8.13443 | -55.17451 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 847bcd96-51b0-3d50-8f2a-f6b96196132c | -8.13387 | -55.31424 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88fbbf87-dc84-3aa4-9101-b68e5e6aebf5 | -8.13367 | -55.17899 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af7a06a8-db28-3304-aa39-06f17e703b22 | -8.13276 | -55.17634 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03a10edd-45ba-3638-8419-d520e820cdd6 | -9.96181 | -55.33249 | 2024-10-10 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a941c230-c2cc-32d2-800e-00832c7ff28e | -9.96109 | -55.33686 | 2024-10-10 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f29ed99-8bfe-320d-908f-8dd9808f7ea7 | -9.96071 | -55.33537 | 2024-10-10 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84d984c0-1df4-3edf-9c11-c1bdd69f577a | -9.95814 | -55.33187 | 2024-10-10 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb49adca-aef5-3fa0-9fab-5e1fe99af8d0 | -9.95778 | -55.33038 | 2024-10-10 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6747a50-8049-3ec7-95b5-5dcb23e169b0 | -9.95741 | -55.33625 | 2024-10-10 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c792c14b-d080-39af-bdde-2bade479d5f9 | -9.95703 | -55.33475 | 2024-10-10 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f4dbdf7-ff9b-30de-bcd8-819268855daf | -9.95336 | -55.33414 | 2024-10-10 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de72fb54-d514-314d-9481-7f20fef53440 | -9.95151 | -55.32627 | 2024-10-10 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4df2fc9c-fa81-31a0-a289-c1d3b224f634 | -9.95079 | -55.33065 | 2024-10-10 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dafe1cdc-18bf-3b5e-848e-a214e116653e | -9.48868 | -56.08107 | 2024-10-10 04:44:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57f94bd7-a065-32e1-a6b2-fe3f57440b40 | -10.79409 | -55.84427 | 2024-10-10 04:44:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d08186d0-514c-34d7-84c1-b49e9b2daab3 | -10.79331 | -55.84885 | 2024-10-10 04:44:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b077852e-ae15-3a28-98d8-92d9e6e65249 | -10.48347 | -55.61591 | 2024-10-10 04:44:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72a6dd22-666a-3356-ad41-31670b9d2263 | -10.48272 | -55.62035 | 2024-10-10 04:44:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 226c71c8-4063-3c8e-bf1e-5957f54c4792 | -10.47977 | -55.61526 | 2024-10-10 04:44:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91c31577-9902-3d0c-bab7-76414b26d3c4 | -10.35983 | -55.86241 | 2024-10-10 04:44:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b6748d0c-0bd0-352b-adee-ee0bac32f7a4 | -10.35905 | -55.86703 | 2024-10-10 04:44:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 5771af4f-5dba-3708-96f2-71cfee3292c1 | -10.35607 | -55.86175 | 2024-10-10 04:44:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| c6262be7-024f-3e74-bdcc-9d4b5fa82f63 | -10.35529 | -55.86636 | 2024-10-10 04:44:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e1bff170-8d2d-3c04-b72b-5e06636f138c | -10.35153 | -55.8657 | 2024-10-10 04:44:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 596b601e-c605-39a5-897b-6a085b5c6f46 | -10.12159 | -55.18278 | 2024-10-10 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 948db228-0712-36cf-aa60-e6e466d8688d | -10.04875 | -55.6358 | 2024-10-10 04:44:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0620c254-3768-33cd-9aa5-13acb62bc2be | -10.90863 | -55.78716 | 2024-10-10 04:44:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98120ad2-14aa-3399-96e9-be36c568a744 | -10.90784 | -55.79183 | 2024-10-10 04:44:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 505cc35e-8300-3d76-b3ef-69db2f8dadf5 | -3.59936 | -55.42036 | 2024-10-10 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2009ec9-74d4-3195-a217-e74351ff37a4 | -5.07215 | -56.23056 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f0960e4-c59e-350b-a4d1-73491661b285 | -5.07152 | -56.23434 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f801d67f-6b40-33ab-963d-986b9b8ba4c5 | -5.00672 | -56.17656 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbd1e57e-7cbc-39fe-b48c-7b58a67b348f | -4.92007 | -56.25992 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dcfc058-76d1-348d-ae68-6883eb4b7123 | -4.89984 | -55.91085 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c8746a5-81ec-3724-b378-57ebb0c8c857 | -4.89576 | -55.91011 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab0f1931-3c61-3b54-b055-8daddb8945ff | -4.8634 | -56.00295 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4616d59e-4b37-327c-8cab-0ecc43436aa4 | -4.85526 | -56.00112 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e084274b-7054-37d1-8e43-ca78c6359e69 | -4.85466 | -56.00468 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b04375f-0e8b-3afe-9dc0-4ad4c3a9f3ce | -4.83352 | -55.80711 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbc19929-c000-3016-b6e6-74a69f78ba88 | -4.83291 | -55.81079 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 477009b9-3b81-3b78-b69a-60a82208988c | -4.83006 | -55.80273 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bf7cc57-229e-301d-bf88-2a6d473d91c5 | -4.82284 | -55.89776 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f7d7f1d-8a97-3b3b-8fff-86da6d23fba0 | -4.69944 | -56.0416 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7947702f-38d0-30b0-9a41-e501ed9b9a11 | -4.66273 | -56.10952 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df7584e2-cacd-3762-b1a3-cf4902fade16 | -4.66211 | -56.11329 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6035354-86ac-300c-811f-d7c69b39e148 | -4.65859 | -56.10876 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9dd89521-8b16-3b01-8ddc-f321f4387b7e | -4.65796 | -56.11253 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 639b4ea8-d8a9-3bb0-831c-2da0e8edf3fd | -4.64395 | -56.01762 | 2024-10-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7743c075-cb38-3c46-bb39-0443e9128dc3 | -4.60379 | -56.12029 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f092c0a4-7122-3142-bcdd-bdd815e2e487 | -4.60317 | -56.12412 | 2024-10-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README113.md)
