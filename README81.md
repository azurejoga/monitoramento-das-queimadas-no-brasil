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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fc1a8e3-024b-333b-8792-a7be7dabde21 | -9.45844 | -60.56507 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44af9aac-6bd8-35cc-afb3-376e73ed71e9 | -9.16855 | -65.79304 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2267e083-ccbe-3cd3-a4f0-4b9f07f5808c | -12.43088 | -63.91117 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a9a72c2-f4d1-3b5a-b59e-fad373eb4a9f | -9.78001 | -64.25455 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6e70567f-51a2-3938-b6ca-13444df90ca0 | -9.25289 | -65.89529 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffc76e07-c97f-387a-af79-63a96fb8f60c | -9.12114 | -65.77793 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2b39eac7-1d6b-3f34-80e8-ee4af19879b6 | -9.00312 | -64.15858 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28a7dfed-b2d2-3da1-9a28-a596ad3bdcd2 | -14.30102 | -53.29258 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ebf9911-3483-383d-8913-99bd38904101 | -10.45624 | -57.96626 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95dfb219-b799-308b-b4bd-285d5dcbbd16 | -9.40957 | -60.5699 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 744fb6fc-1f20-3bad-b3ad-b8ff57231123 | -7.55616 | -63.84109 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 414f06f4-552e-30aa-a518-4d5f0644fe0e | -11.31038 | -55.22248 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32a04f69-c12b-376c-bd19-b0e748ab4243 | -9.78847 | -64.24483 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f18a8ce-85db-3b84-a103-ccdea0b14911 | -7.78501 | -61.31909 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04f7d723-f305-32bf-8d33-34729f3ce3eb | -10.45169 | -57.96914 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ced1db8c-666d-3158-a0af-38fb8dafd332 | -9.15991 | -65.77895 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7403cd5-094e-3b34-88a9-e3e9510a8689 | -8.03845 | -70.09899 | 2025-08-29 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f46e9caf-639b-36aa-870c-d212bc0f0d87 | -9.6525 | -64.95197 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4325ca57-1839-34e3-b713-775307b59e05 | -13.22932 | -57.13419 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7d33e48-a006-34e8-9e0d-dd136b677a6d | -9.11554 | -65.78962 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c815412e-b161-3abd-8db8-e403b12a74a5 | -8.18528 | -61.38434 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03e58b90-b6a9-3c08-a346-08be00f88b4e | -13.00632 | -56.91785 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bd5ffc3-ab15-3f8c-b424-346332e555cb | -8.12381 | -61.21404 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cde2f281-d5f5-38e4-b9bc-5f300aa01dc5 | -8.77612 | -71.30548 | 2025-08-29 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ecce789-18fb-354a-855a-3bf525bc201e | -9.47087 | -60.30791 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d09c689-2d94-3806-a330-c2f986f60359 | -9.00327 | -65.72167 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56e83c25-c3fe-3393-8b67-d25f8c8183cc | -10.0222 | -51.11169 | 2025-08-29 05:29:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f2752cd-ee5a-3c18-bdab-e36dfec6575b | -9.78234 | -64.24011 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f1a2154-4ed8-392b-a8a0-4c4a57ec9b02 | -12.62919 | -60.25179 | 2025-08-29 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bc4fd88-c206-3ff8-b2ba-c881e9233b10 | -8.93139 | -71.2763 | 2025-08-29 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa8e8cf0-ae07-3232-b345-9ba5087644aa | -9.10337 | -62.67996 | 2025-08-29 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d8ce237-52ad-3b42-acfb-6b1470124c92 | -10.37664 | -59.39383 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f125245a-1a83-3f3c-9d32-d9c630e82747 | -9.58115 | -68.57164 | 2025-08-29 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aed9d2e2-ff58-3fbd-9eed-32f322c83e73 | -9.11979 | -65.78611 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 643339ed-6ff1-3b7f-b5dd-dcac85720ac4 | -9.76598 | -64.25594 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 64809e5c-53d4-3673-a3dd-0852c4bac77c | -9.54049 | -68.57816 | 2025-08-29 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90228358-d091-3272-b1ba-511f71d46703 | -9.78569 | -64.24067 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3294e83b-7cb5-322f-8d77-e133fd670b47 | -9.54232 | -62.39263 | 2025-08-29 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1384a9e-e51f-34fd-8fec-7f2605959967 | -10.85146 | -60.81507 | 2025-08-29 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b4c8dab-7100-31c2-a79b-b6fa759d1a65 | -9.24114 | -59.78838 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ff119dc-4b2d-334e-97c8-cd97b726b856 | -12.9973 | -56.91652 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44a3a63c-97fc-30be-add8-2f5d58d417e9 | -10.36898 | -57.82351 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e2177aa1-a94a-33a9-8504-8fc4192a6c52 | -13.02498 | -56.91557 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41de1ce3-a060-3521-b425-37d3a792f7d7 | -10.34706 | -59.19354 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6173e39f-d12f-3e2f-8062-78fe0d00d009 | -8.92634 | -71.27529 | 2025-08-29 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9365a40e-75fe-3c9a-a1c8-667431b13385 | -13.00691 | -56.91323 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36055d4a-977b-37b7-ba10-4a9fbc5e2332 | -9.76934 | -64.25648 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9ab28ae7-1423-3ab5-b96e-0075a0dcf742 | -8.9512 | -65.96862 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a4042e5-7936-3560-b493-e404e8efaaff | -10.37601 | -59.39821 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33dede8d-42e1-3d62-9470-e6dd08a36696 | -9.15853 | -65.78713 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b741237-6d60-30dd-a020-d744e96be0a6 | -9.90705 | -62.14356 | 2025-08-29 05:29:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a1a6eaf0-18fa-3d5b-8d96-6c6127cb97a4 | -10.36755 | -57.80444 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6df0761-f875-3701-bb16-a9200ab2c785 | -9.17177 | -59.57418 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 32c84caf-feb0-3658-94f9-6cf7ff2c19b5 | -7.62637 | -60.85255 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 728846cf-a688-3857-8e3e-f081cb2ecefd | -12.9946 | -56.90186 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cd4c603-0248-3591-98c6-9fe1b20b4f5d | -9.54504 | -65.68995 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecda99d7-3ce3-36ec-9a01-091190859abb | -14.11931 | -53.96228 | 2025-08-29 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c501ddfe-fc5d-3e0f-ba4c-422a460b5804 | -12.43582 | -63.92284 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3920e93e-0c4d-3ced-af41-b2c51c5fe531 | -9.10771 | -65.79256 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2decbbb-ec21-3d26-ad99-7decdafdd02e | -8.17688 | -61.37206 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 74c9da51-89e6-3717-93c0-f539199036e2 | -9.16141 | -65.79182 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9c1bccf-5b4f-3187-bd4b-15d6aa12ab39 | -12.22408 | -64.22927 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 116c52bc-a596-3e24-9b3d-8ef3ff3b1d3d | -14.30686 | -53.29334 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74b4d45a-a698-311d-b140-04d33b2d1d49 | -9.2515 | -65.90352 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0505e4e8-a5ef-3248-be4b-fa0e36bd481c | -9.45584 | -63.09394 | 2025-08-29 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e756ea0-6279-38f5-ac07-9107b13dde7c | -10.53289 | -64.36945 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 791da3da-f5cb-307b-a02b-d1dd8d16eb2e | -8.90507 | -60.75612 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af5eb32a-4f86-3fa0-9116-d361e94e3db0 | -8.89625 | -60.5656 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa49a7b5-70ee-3969-a23d-b221a689f61e | -14.51509 | -52.99575 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46b5705a-99e2-3935-bebc-957798a7b06f | -14.3487 | -53.23815 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c0f41b7-cec8-312c-a63b-ce16fc920bde | -8.95912 | -65.96564 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c242b52-4800-3f40-857a-66953f7a898f | -9.7727 | -64.25705 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 23d1f0cf-d6a9-3d11-a060-e35043222979 | -8.18473 | -61.38791 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59281310-7f9d-3352-8224-fea41ffd8c6f | -9.12316 | -65.76567 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bf939039-7c9f-33f2-8568-0a2b33156dc3 | -12.9916 | -56.92517 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5e9f70b-9c77-31d0-9086-8c59022d1ca6 | -9.15189 | -59.57682 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05cf8fc6-7f76-3233-99e1-9e3d9bcafbe6 | -9.16275 | -59.55984 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24a49455-42d1-37b7-82fa-a03b01a9a7a6 | -9.88089 | -64.69391 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a8a811f-b579-398f-8ce9-c4f593e41a35 | -9.15827 | -60.93222 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e460782c-51f0-3c9d-93eb-b12cef78b1ed | -14.50579 | -52.07797 | 2025-08-29 05:29:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e403518c-b820-3bb1-99fb-620034c04eba | -10.37252 | -57.82784 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0bf0d181-b25a-31ce-b114-debbcde20c1d | -8.17857 | -61.3833 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6c7ccfc-47c3-3865-9b20-353e226b70e6 | -10.07187 | -62.89195 | 2025-08-29 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9302808-450b-38c9-9c43-3e1182e06698 | -8.90164 | -60.75559 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3b42dea-2ef7-3a27-bba8-de5c06a5d602 | -10.32582 | -59.18138 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13a73115-1723-3fbc-bea7-c6ee503ffb23 | -8.18974 | -61.37771 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd217d9d-eb9c-3576-9071-6b3c39e4887b | -8.17798 | -61.3649 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a6d1345-3a3f-3690-a661-51fd2a7fa5b9 | -9.46249 | -60.56172 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e3e811f-529f-332a-851a-be5e573fb7a6 | -10.45372 | -57.95498 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aec38115-be46-356a-96e8-e57e6e7a2032 | -9.12606 | -65.77036 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 749db813-a8e7-3acb-9b81-3c3966741268 | -9.78059 | -64.25094 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ebfe74aa-02ea-37b5-b7ed-60768845f4b8 | -9.24832 | -59.78948 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43bca3ec-820d-3536-81d1-cb36fb8572dd | -12.427 | -63.91414 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 20e4c97a-a089-368f-b374-4e33b4daeb2c | -9.78905 | -64.24122 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17d7dcbf-7a66-3aeb-819e-bc221debcf1d | -9.17858 | -65.79897 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c14b9ec-69c9-3484-8d96-067e4382da6f | -10.61649 | -54.91286 | 2025-08-29 05:29:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b92f248-a0c2-30f8-8261-a6c5f5b87822 | -10.36808 | -57.80074 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33d3a90d-e597-309a-ab19-a18e63f45144 | -8.11596 | -61.22022 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91641325-0b0e-3046-afa5-3a8eb775019b | -8.17743 | -61.36848 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 33c00b70-9ded-3044-8b81-757a4381e4c0 | -10.46041 | -57.93726 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README82.md)
