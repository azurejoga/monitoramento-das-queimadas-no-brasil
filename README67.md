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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55c62e73-c5f5-34f7-9ce9-e521982f9ce6 | -10.5166 | -64.5186 | 2026-08-28 06:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d81a00bd-390b-3b98-b2fa-0c79e69f0c70 | -16.1641 | -58.5851 | 2026-08-28 06:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 1226a6ab-88c5-373e-89bd-32dc436a4833 | -10.4981 | -64.5005 | 2026-08-28 06:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 35afeab1-2f61-38cd-9737-26c976733795 | -9.5241 | -67.1623 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 196b54fc-0fa5-3378-9b0d-1285fc0879b3 | -8.55249 | -70.60299 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcef1e60-87af-3d83-8748-3b5bc5756894 | -9.19019 | -72.00613 | 2026-08-28 06:31:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41cb47b8-e3d0-3db3-86c1-4c871856285f | -7.58507 | -61.33781 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf3e0451-dc49-3168-8c4e-22297647988f | -8.99814 | -65.44762 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18d53d32-6382-3b35-9b38-cf30fbbd3900 | -7.58597 | -61.33077 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 522dea74-f759-3b9d-8429-8fe0fe75ed80 | -8.94653 | -70.56236 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82e93661-4747-3665-91cc-a3c0e28ddebd | -7.60662 | -61.34081 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1baf4063-49aa-3624-aa60-9673f65f9173 | -8.9997 | -65.43598 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63a89ca7-bd2f-325f-b956-f2d5add46265 | -10.49847 | -64.50179 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1ad9fbd8-dbf9-38e2-a6d4-b67d0abb2d9e | -8.39649 | -70.73973 | 2026-08-28 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87ef374f-a4af-3008-b2d8-31d63f33b818 | -7.57434 | -61.30715 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a023dedb-e4e6-3cda-b760-1c4833119d5f | -8.95423 | -62.39114 | 2026-08-28 06:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1eff217-5dac-39a4-a3a7-e41418af51bc | -8.58497 | -70.68639 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37456682-8854-3f8e-a9c4-671e134fee72 | -7.58115 | -61.29888 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f129348-c7ce-3534-b1c1-3fb82ff7ca79 | -9.00152 | -65.43863 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dea5e1b-fccd-31af-a926-dcfbc61f44cc | -8.3046 | -70.58778 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f1b7ddb-7869-37c4-8e05-b63d1d7aadd1 | -10.50401 | -64.50746 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cd72a636-8bdf-3356-bf44-ea1f10208146 | -8.99245 | -65.44684 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6aaa0c9-5b26-3472-8617-ddca6f4bb4c7 | -9.84888 | -65.01935 | 2026-08-28 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b927c934-0164-37f9-849a-9c30436998a1 | -10.50318 | -64.50331 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f518dcc7-989f-3c23-aa2d-25613b10b001 | -10.50341 | -64.51225 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1dfb4351-a80d-367e-ad96-0ed809f3ac86 | -9.2816 | -68.78183 | 2026-08-28 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69e59df1-0dfa-34c8-888d-ff39a6952d77 | -8.98831 | -65.43439 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 688adfa5-edd6-3dfd-8670-7157f8b904ea | -8.61183 | -70.66943 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9be63028-3d43-31f4-b67c-a0d9942a3244 | -8.26926 | -70.09523 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de4f4b8c-92f7-3734-9422-1216803328f5 | -8.78759 | -70.77253 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1748e33-8120-3a04-ac6f-d2a200e3bef9 | -8.98728 | -65.44219 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5dd17e6c-b4c2-3caf-9b18-c460223289c3 | -10.08911 | -68.29322 | 2026-08-28 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44179798-d9fa-322a-8ef2-bf1e84b1bba9 | -7.58152 | -61.30831 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c3e3b5e-05e6-3cd4-b567-64aca1a14126 | -9.2028 | -65.79249 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c73a668-7cec-32da-a5af-f568769ec261 | -8.15618 | -64.00639 | 2026-08-28 06:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53995b50-04d1-3a30-b526-87d087da111f | -8.63711 | -66.53666 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d102d55-ae1c-3a14-a196-eb56810b54aa | -8.15123 | -64.00159 | 2026-08-28 06:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6cc7acf-c0b1-3d28-ad45-833631c2c704 | -7.58687 | -61.32375 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 979f0308-0cb5-3feb-b993-20df57cd46c6 | -9.53758 | -66.77446 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e8ffada-4df6-3776-9633-b99b7ed993d6 | -9.52153 | -67.16508 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e165361-40ef-337e-84a3-c638a6c27011 | -8.88031 | -66.90553 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2f73837e-db4e-3927-834f-bf48d083d68a | -8.88073 | -66.90245 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cfcd66b6-5a2a-3bac-a071-cd8b286126ae | -8.60444 | -70.21388 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 03ee1edb-d291-3826-bada-e5f9ff563673 | -10.50818 | -64.51381 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 42b7d826-8e0d-380a-8f8c-8c98d4105b5b | -7.62442 | -73.06705 | 2026-08-28 06:31:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9548470-7340-3f6d-9b39-d61e35918acd | -7.57922 | -61.31326 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4aa77acb-d7a7-30ec-83cb-cb9f4e0c6187 | -7.7159 | -70.09358 | 2026-08-28 06:31:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65c1fa29-d1ee-30c5-9faa-c0c4eaa58cd2 | -8.60087 | -70.20964 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed2b4334-b984-350c-8535-82abab760516 | -8.99865 | -65.44375 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 763976d1-0cf0-3590-b540-e99caa32e4a0 | -8.59983 | -70.21696 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d05df871-9aec-348f-b31b-f589bb24e43b | -8.94736 | -62.39025 | 2026-08-28 06:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9cff451-5164-3882-9443-ce35c541f50f | -7.57526 | -61.2999 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 34f8ede3-c97e-3365-8fa1-a7c4857d9bec | -9.00023 | -65.43204 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c2d2fbe-4c18-3298-96e5-e62fc416bdc3 | -8.99917 | -65.43988 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6dae3765-af71-36fb-9dc2-64095e2337bb | -8.99348 | -65.4391 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f861984-edf5-3065-becc-b0aa968f90a9 | -10.49787 | -64.50651 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e045415e-6410-3dde-bf04-2d7cd5d0a81b | -8.60035 | -70.2133 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ef8e0216-15e4-39cc-a1cd-8a32fd7ce0cf | -7.53509 | -70.02695 | 2026-08-28 06:31:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6e46b1b-ae23-3cb4-97ee-e358da894689 | -8.59783 | -70.20171 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e428faf5-47dc-3e19-bfa6-1ab9b1d97787 | -8.9878 | -65.4383 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a3bb82a-879a-339a-8da2-a903a1333402 | -9.00202 | -65.4347 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1932be96-3f04-30f0-a524-7a935aaf1514 | -9.27706 | -68.78115 | 2026-08-28 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80c4e26d-b2ef-38ed-8b98-e66717f70128 | -8.44524 | -70.89997 | 2026-08-28 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdc9aa78-cd00-3641-a5e7-ae5cdef31df2 | -10.49646 | -64.50712 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 21433cc2-0f5f-36ec-afe5-b3d1bab91256 | -8.64281 | -66.53419 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4a3e6d8-be4d-3276-8b67-b2d57bcc345b | -8.98884 | -65.43049 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95677861-09c7-38fc-a959-a7a729fda62b | -7.58018 | -61.30611 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3469af06-4ff1-3321-a5cb-5f4fff035fcc | -7.58061 | -61.31545 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0dd33b74-6c9b-33ad-8873-4239f20ec0d2 | -7.57826 | -61.32042 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bfa4c2db-7e2c-3cb0-987c-a44a29bcfa75 | -8.83198 | -68.66621 | 2026-08-28 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 343319f7-6a62-3450-8c6e-445763d5f7b8 | -10.50876 | -64.50902 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f9aad10f-3ede-3d5c-8cec-a4afb96590e1 | -7.71536 | -70.09718 | 2026-08-28 06:31:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 090f497b-0919-3970-9a5c-c6aa755f92bc | -7.573 | -61.30501 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0cedf7f-6ef0-37b5-8f14-ff5fb847b852 | -10.50896 | -64.51786 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7bbc5b68-e933-3005-9201-624997efadbe | -8.8237 | -71.0396 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cee443f1-1b3d-3d90-95e3-49a4580b2e6a | -9.85427 | -65.02427 | 2026-08-28 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 014c3cf3-a799-3fba-9801-b23f443a86cc | -8.59626 | -70.21272 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac5ba1f7-a3b6-3726-b5e9-f475f1d7a00c | -8.24107 | -70.49387 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14b04a35-bf92-37c9-9053-0efb94662df2 | -8.6314 | -66.53913 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6438a125-d5fc-3ce4-ae5f-d3e02b2f861c | -8.15741 | -64.00243 | 2026-08-28 06:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f156366-ba1c-3050-8cf5-732a210803ea | -8.94577 | -62.4029 | 2026-08-28 06:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a57241be-80ad-3f21-a0bc-fde3beec11a7 | -8.43863 | -70.69949 | 2026-08-28 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9637ca77-c74b-3212-8fef-8f28c8c26f36 | -9.52372 | -67.16528 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cacaa19-50a1-33c4-8941-5b4632e7b3c8 | -9.00053 | -65.4464 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 787962d2-f709-32d5-a066-8919aa68eb26 | -8.876 | -66.89861 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f097d50-2eef-3875-9c3d-b0ea4e40c1e7 | -8.5973 | -70.20538 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e61d9e34-e755-3fb0-ba0b-0e345322ecd8 | -10.50204 | -64.51289 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 1179367e-d533-3825-b994-2c56a3f4ea75 | -7.39939 | -72.62858 | 2026-08-28 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b8f8ba0-0579-32f8-b1d2-88cb57724124 | -8.76632 | -70.77979 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15792e3f-e502-3c46-be6b-488e5b3c10eb | -8.87558 | -66.90172 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 743d7a56-8f3b-3549-a27d-477bb6572b06 | -8.60497 | -70.21023 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b50cc81-0622-31b5-9b51-87f209b160a1 | -9.52194 | -67.1621 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2b225b0-9eed-3504-8d6a-77411be13ae0 | -8.87474 | -66.90788 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af33a537-4d0a-3869-80d2-2addcd24b1e9 | -9.66505 | -68.97185 | 2026-08-28 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7b105b6-4966-30a8-987c-918d898ae419 | -7.60752 | -61.33382 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6119518-2813-3846-9eef-e8ae13babc9a | -8.64237 | -66.53741 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d74cccb1-1464-3f24-8dd9-35510a3b4562 | -10.08435 | -68.2925 | 2026-08-28 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ee883a9-9f7e-37ee-a03e-61a0e582cb7e | -10.50956 | -64.51311 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 20c78d96-08d4-3154-bfd7-7922ea2a8b40 | -8.59573 | -70.21637 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80fdaa9f-d9ef-373f-b624-40624b609eb2 | -10.50462 | -64.50266 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README68.md)
