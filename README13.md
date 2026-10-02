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
| 35563c1b-73b1-33bb-8878-9777ba82d262 | -3.2921 | -53.844898 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc857fb0-e973-31ce-88cb-ada019d4de75 | -7.6884 | -54.771301 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a9ffacf-6bbc-399f-a383-0f09283bd99b | -2.8852 | -54.882401 | 2026-10-02 01:12:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54c57876-637a-3fc5-9c3e-0069caf9f60a | -7.035 | -55.6441 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 083af15b-f2ca-3bfd-ad41-3674f23beb5a | -6.9168 | -59.284599 | 2026-10-02 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6e863ed-753f-317b-92ba-9be5df0c2142 | -8.1719 | -54.807999 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1822bff9-3d3c-3ad4-8980-add7325f8577 | -11.6892 | -43.592602 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8df1d129-b21f-35b8-9913-0fc31a1dfc11 | 1.7731 | -55.634399 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 291d9b3d-bb0a-3315-ac77-a13d485bcb72 | -6.6984 | -56.151199 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1d241b1-6e8e-38bd-9386-4909ff1a31cf | -7.8682 | -54.745201 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e2ec7b7-793d-3d60-892c-653b02d9a94d | -7.3874 | -55.206501 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7dc5ccf-0eff-3377-9842-54831b3aba9a | -6.3888 | -56.419201 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2333b2f6-c4ff-3bcb-9e8a-63fc05a7f196 | -13.0597 | -51.295502 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1f8259e-2546-3422-bae9-eb62f2a5b5fb | -13.3352 | -43.840698 | 2026-10-02 01:12:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1d50831-7a5c-3475-8d81-510dd4b1f2d7 | -7.5422 | -56.141899 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55ad68b2-36ad-3b09-8dc7-4745813d9ad5 | -13.0524 | -51.307499 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d6b93a27-0a5a-3643-99db-71c2ca32c097 | -8.5403 | -54.573002 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9097b70-1e53-32c4-a21e-865cd4d1f25e | -11.7093 | -43.516998 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3da80a03-620f-3cb4-964e-3d13149e96b8 | -6.835 | -55.272301 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7a6692b-0713-3211-8b0e-5943bd25d406 | -5.6175 | -57.2369 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d38a3b8e-6671-33f9-be4a-9d7fb1c169be | -8.2501 | -54.656399 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5427b146-78ee-389f-8044-303742cfd217 | -6.0829 | -53.3032 | 2026-10-02 01:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adfe2495-2a65-3004-ba01-ed03cef96055 | -4.2735 | -50.779598 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c016ce6d-d094-3255-9709-8ed983e9da19 | -3.0118 | -53.880199 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ca2e1fb-2db0-33ea-8d2d-10e3f1c99bec | -4.2945 | -49.0863 | 2026-10-02 01:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d26dc056-99de-317a-893f-1801e8d3a484 | -7.4123 | -55.580002 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a77f0f40-b4db-31f1-bc0e-4c0f7548770c | -8.18 | -54.798401 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d5417ba-24eb-3afb-9828-37d6c3309a45 | -7.8235 | -55.128799 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35d03e94-e32d-3da7-88ef-fcf6164977ba | -7.6964 | -54.761501 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 481b95cb-ec49-3f4a-a066-ca81934cce5c | -13.0305 | -51.302799 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83260a00-dd4f-3318-81fb-a3f59007b46d | -7.187 | -52.609501 | 2026-10-02 01:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40d6bd49-9871-3999-8d7e-7c1ff8489297 | -7.4674 | -55.0182 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de9eda0d-2c62-3690-90f0-d2cd8466f6f2 | -6.3205 | -54.792801 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bab7697-9c65-3bde-a36a-ef01345b03b2 | -3.002 | -53.8825 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3412415-19bd-35c0-8df3-1e05d9ad218c | -5.8717 | -50.1576 | 2026-10-02 01:12:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a663258e-54e5-3c03-a03c-c0b3944e0356 | -7.5509 | -55.022202 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2db83804-6f37-3d4a-9223-f6b6fa006578 | -6.3623 | -55.148399 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10f83a97-1c54-31a7-b896-9dae4a0d8478 | -3.8517 | -55.800098 | 2026-10-02 01:12:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f321800-a888-3e35-a069-ea8cf8d626d9 | -11.454 | -43.412498 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58178151-11cf-36f4-9bd3-68138ad7847e | -11.7933 | -43.597301 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa6ea250-af90-3795-b48c-e87bace786de | -6.0642 | -57.611301 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e9ce6e1-befd-3d95-8289-e7b0ca24bc26 | -7.0333 | -55.637001 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4632ddea-0143-3f3f-8387-0293600bc256 | -4.2668 | -50.751801 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f06aa6ab-3b88-3288-a3be-0b4993999f67 | -8.5483 | -54.563099 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03b0e21c-a6ff-34dc-a925-0a263984fb0e | -7.3356 | -55.605099 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f25681f-98a7-382f-8d1c-a050d164ca7e | -6.0087 | -53.556099 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdeea77f-981e-36e0-a9e4-f6d242f29577 | -3.2943 | -53.854 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9cd27a-3aa8-31d0-b3b7-83193522a078 | -12.8342 | -51.473598 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 34ad1898-6edc-3539-82c8-2d32df82ec8f | -13.3624 | -43.863899 | 2026-10-02 01:12:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a8e404b-0fe9-32a0-a594-734a67955ab8 | -4.4479 | -54.9049 | 2026-10-02 01:12:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c862dec9-dbf1-32e7-9a38-65beee590d44 | -4.2732 | -50.7355 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa5dd399-e066-3943-8ae8-19f310c5aec5 | 1.818 | -55.573299 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56969d89-cce4-3f67-97ef-357165c2c9f4 | -9.5288 | -45.329498 | 2026-10-02 01:12:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 01a54dfe-0fb4-3b88-949a-f3ca2f091fba | -7.957 | -54.9048 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48cd6fa8-30fb-3edb-8b30-b07b52708e4f | -8.1702 | -54.800598 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24e2165c-d30d-3066-b5d2-7f9c6babd8ea | -6.3872 | -56.4123 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcf14b4c-edca-3b8b-a944-e72b4ff4907e | -10.8159 | -51.087601 | 2026-10-02 01:12:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 743c32f1-90e7-3ef8-91d6-16dd46f36a35 | -9.5772 | -54.636002 | 2026-10-02 01:12:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b5cfb1d-5b5a-3617-a803-3ab4ab89b3e4 | -8.1621 | -54.810299 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e24e68d-06ad-3de5-b1f4-237554a4341d | -7.5526 | -55.029499 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6ad7b5b-1ae7-3a09-b212-e4aaec5c48c7 | -1.6869 | -55.6721 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cffc97f2-68df-3001-967b-0c550dd08627 | -7.3304 | -55.227402 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9bd11de-8f32-3d06-982e-79ecc6b66a49 | -10.8282 | -51.095798 | 2026-10-02 01:12:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1c60a87-9dd6-3c70-8df7-e73b2aeb02f1 | -2.992 | -51.051701 | 2026-10-02 01:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edff47cb-fb57-337c-8400-11dc5ea886f8 | -4.2799 | -50.763401 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5dc5e8-a616-3720-8e4a-859a8536a2d2 | -5.3032 | -55.8745 | 2026-10-02 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94c50e4a-23da-3c3f-8dcb-64afc42e5a3a | -7.332 | -55.234699 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a586ac15-1eee-33a1-a39d-6b0c220083dd | -13.05 | -51.297901 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d84875e-c7df-3e3e-948f-4eccc2f9fdd4 | -6.7 | -55.047199 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72129a7b-cd0f-3fd0-b62f-f4c9f82b6439 | -9.7899 | -53.826302 | 2026-10-02 01:12:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f62caf5-6810-334d-94e5-c92cdad95f2b | -5.8586 | -53.488499 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1778ffc1-6d58-3ebe-9e7f-f41809e16b06 | 1.7848 | -55.628201 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 598d1330-b73d-3676-a877-a1b9ed2e758b | -10.7853 | -53.754002 | 2026-10-02 01:12:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b55529e-4de7-34dc-822b-f7a0c499a90a | -8.2986 | -54.731602 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d2f4a04-33c8-3689-adf0-b80131fae80a | -4.2832 | -50.777302 | 2026-10-02 01:12:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2af9453a-4a38-3f95-935f-0b134cc12611 | -6.083 | -57.693699 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99d05816-d890-3924-9642-2d5118fa6fa9 | -8.0642 | -54.833099 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3efe1fe-a2fd-3604-9bc8-5fd9aae88a48 | -7.5406 | -56.134899 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7e9e50e-c211-35ce-8ebe-e320a6e2cec1 | -2.4629 | -56.083698 | 2026-10-02 01:12:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e380082-b26b-3dd9-b709-3807fa456f4c | -6.1662 | -57.6968 | 2026-10-02 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 049f509a-e6d6-3a53-afdd-9275a7fcb0aa | -13.0379 | -51.290699 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4975def-75d5-3188-b5dc-b480008f8380 | -6.3606 | -55.140999 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bb3e44c-ee6b-342f-a62c-6ae9c49805c1 | -3.1863 | -54.097099 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5de6925b-abf2-3a95-9acf-2718a68c8501 | -6.3986 | -56.416901 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ec8f357-ec58-3bd0-abe7-1f1c779ed626 | -5.749 | -55.750198 | 2026-10-02 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b42913ac-24c8-37c7-a14b-376e588f2220 | -3.1325 | -53.735699 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58fa2bdd-9316-3aaa-af30-8ee1f400799e | 1.7712 | -55.642899 | 2026-10-02 01:12:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90a08f05-2281-3417-8f00-9b0725864369 | -8.2191 | -55.098598 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e47677c-55e1-37f3-9245-cffe0e925032 | -11.7292 | -43.440701 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb50b31c-d047-38a2-a532-5bb28a9dc240 | -10.7951 | -53.751701 | 2026-10-02 01:12:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c74b896c-773f-3253-9ca6-2ea727f7f440 | -12.7985 | -51.411999 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ee6fd536-b4de-3604-83cb-e41fcf9e4781 | -13.0012 | -51.3102 | 2026-10-02 01:12:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c71171a-957a-3709-8dd5-1698e0db8d99 | -5.8726 | -53.503899 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8b3df72-45f0-3487-98d2-1133c218f07c | -11.6998 | -43.519699 | 2026-10-02 01:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b103812-64f9-3ca5-8a92-aa5a49bf95d0 | -3.014 | -53.8894 | 2026-10-02 01:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4eb88406-b7b3-3dbe-a274-f42d43aecdd6 | -7.4835 | -54.999001 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7326b9e-7594-33a9-bad5-146d85693d9a | -8.2317 | -55.285801 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1074895-63ee-34c9-bac2-85373856eb04 | -5.8998 | -53.488098 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bfe3324-621a-363d-8d79-5805105958d3 | -7.2881 | -55.578499 | 2026-10-02 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a1867d8-4687-3ccf-ab35-6c8497f2ea7b | -8.2403 | -54.6586 | 2026-10-02 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
