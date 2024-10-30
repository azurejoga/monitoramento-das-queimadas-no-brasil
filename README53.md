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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 118b3f38-909f-310c-8e48-27cbf7ef11c1 | -16.82808 | -56.6978 | 2024-10-30 04:23:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5c0f5e8c-4258-361b-bbae-e2b661626a8c | -22.07994 | -46.90281 | 2024-10-30 04:25:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 895d1fc8-e138-3c08-94cd-b2be7ab8e15f | -22.55466 | -47.70298 | 2024-10-30 04:25:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 17c42d72-8849-3c1e-9177-3a4df12474e7 | -22.55134 | -47.70238 | 2024-10-30 04:25:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2bb4115b-bd79-362f-a693-92715a73bd80 | -22.51249 | -47.711 | 2024-10-30 04:25:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a8909b23-c597-3511-958d-089cc582870f | -28.03687 | -49.95059 | 2024-10-30 04:25:00 | NOAA-21 | URUPEMA | SANTA CATARINA | Brasil | 4218954 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8e366f5a-eb7e-3aff-8742-db315fcb982b | -22.54168 | -48.81138 | 2024-10-30 04:25:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10af3c51-8e34-32a7-a8f4-e43c79103acb | -23.85495 | -49.49325 | 2024-10-30 04:25:00 | NOAA-21 | RIVERSUL | SÃO PAULO | Brasil | 3543501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1be2b1d8-19d9-3c71-ad4f-eb71c6c4262c | -24.16009 | -50.20597 | 2024-10-30 04:25:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c8480407-04d6-314a-9df8-190ef5c6c22a | -24.15674 | -50.20531 | 2024-10-30 04:25:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 362e394a-aafb-3594-9abd-d6c6379de3e6 | -23.98707 | -54.11622 | 2024-10-30 04:25:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 00707128-cc17-3521-9a6c-5e4933f0bba4 | -24.24203 | -50.74088 | 2024-10-30 04:25:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 078bdb66-ecab-33b6-b195-97320f09f721 | -23.98617 | -54.11183 | 2024-10-30 04:25:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| acfe00f5-2fd7-36a2-a5e4-20eb3deec3b4 | -23.14652 | -52.66758 | 2024-10-30 04:25:00 | NOAA-21 | MIRADOR | PARANÁ | Brasil | 4115903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3112055f-abdb-32f6-92a1-79d92cb702fa | -23.10313 | -52.09418 | 2024-10-30 04:25:00 | NOAA-21 | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8bd3ad35-c41a-3735-b5a5-10801814909b | -23.98507 | -54.11739 | 2024-10-30 04:25:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| c1b40d55-bfa2-3a5e-b52c-1681a383e5aa | -23.98312 | -54.11533 | 2024-10-30 04:25:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a925f125-2bc0-3b82-88e9-87d8069cc654 | -21.56442 | -54.2117 | 2024-10-30 04:25:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e35fd97-22a9-3ce3-aa27-4fa0d7b38b5e | -21.56372 | -54.20823 | 2024-10-30 04:25:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 909f47ec-5a85-3e9d-8fa0-fcfb2c41f38e | -21.56292 | -54.2124 | 2024-10-30 04:25:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54a138a3-9261-3664-8692-6f5d281ddf77 | -21.55956 | -54.20732 | 2024-10-30 04:25:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b022551-8fd3-3a67-b67a-fccc1735a70f | -21.20005 | -54.44135 | 2024-10-30 04:25:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d146c31-9bec-3e83-bdc8-c2b8c31734de | -23.75241 | -54.50641 | 2024-10-30 04:25:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 942eca3f-ac87-3f3a-8888-b5104fa5bde3 | -24.00948 | -54.14035 | 2024-10-30 04:25:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| b9748b79-833b-3d75-8d73-6565c1c36759 | -24.00839 | -54.14593 | 2024-10-30 04:25:00 | NOAA-21 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 5beed982-a764-3602-8d8b-561f99d96250 | -24.00731 | -54.15151 | 2024-10-30 04:25:00 | NOAA-21 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| f6b0869e-fec0-3816-a5a6-f66718ca4159 | -24.0064 | -54.15616 | 2024-10-30 04:25:00 | NOAA-21 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fe10bf7f-71a6-3040-93fe-ab1c1dddeed7 | -24.00244 | -54.15527 | 2024-10-30 04:25:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7079f1f6-5c0a-3411-b4e5-93908ce8023b | -23.99208 | -54.11155 | 2024-10-30 04:25:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 753b6b79-2d38-3f25-aca4-3ae9b5e44908 | -23.99012 | -54.11272 | 2024-10-30 04:25:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 6ffafb1a-70f1-3014-9881-e0ae5e5d5071 | -23.98813 | -54.11065 | 2024-10-30 04:25:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| cc111f41-2adb-3eac-9fe4-67204995ef7f | -20.88414 | -57.25889 | 2024-10-30 04:25:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b05513b-ba00-31e6-b383-469435a767ae | -2.833 | -49.2413 | 2024-10-30 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 35865a0b-f1e9-3c83-83a0-203ff7406e57 | -3.0734 | -54.167 | 2024-10-30 04:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 4fd0a5e1-1426-3a9f-bec7-aba63b096030 | -3.0913 | -54.287 | 2024-10-30 04:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 45f37882-c06e-39a3-b16b-ddbb87f7f5db | -3.1097 | -54.2865 | 2024-10-30 04:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| dae29148-ffbe-36b1-97a4-0be724816a3b | -3.1098 | -54.2665 | 2024-10-30 04:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 2b58b662-0992-37cc-9999-71f767f1843f | -3.1281 | -54.266 | 2024-10-30 04:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| b0b74e50-b7d4-38a3-8f19-82699f66784a | -3.1601 | -50.6021 | 2024-10-30 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 8b7819c0-503e-310d-8d30-09f4a3eca0a0 | -3.1602 | -50.5812 | 2024-10-30 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 42c0fcf9-cb74-3619-8d12-d7b86a0ebab6 | -3.1786 | -50.6016 | 2024-10-30 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 7615ea60-d5bd-32c8-b2bf-d9c7a67e77fa | -3.1787 | -50.5807 | 2024-10-30 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 387d0450-1355-364b-9ba0-7c2cfe54efcc | -3.2535 | -50.3479 | 2024-10-30 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| c0d58715-dec9-30fb-98d0-ef6ad44f067c | -3.2535 | -50.3269 | 2024-10-30 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| c675458a-ccb2-3a1c-a607-4693a2c59b09 | -3.2719 | -50.3473 | 2024-10-30 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 475d0b11-8846-3807-80bd-b7a2cc9b2df3 | -3.272 | -50.3263 | 2024-10-30 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 3a422813-8d32-3a0c-a2d5-b71f183b108d | -3.5631 | -47.3847 | 2024-10-30 04:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 96c2847a-6fb4-30bf-9a5a-43cca727c76b | -3.5632 | -47.3629 | 2024-10-30 04:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 403c48d0-17a1-3c21-8d57-781149df0c61 | -3.5817 | -47.384 | 2024-10-30 04:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| e3afecda-ffc0-375a-ac64-2d55d4b3cd67 | -3.9486 | -48.1291 | 2024-10-30 04:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 406a52a0-7198-35ea-b9da-668918847ed0 | -3.9671 | -48.1283 | 2024-10-30 04:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 447702fb-cec3-3e09-8096-1b8432f5f124 | -4.0681 | -50.024 | 2024-10-30 04:25:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ba5679df-c3b4-34a9-ae11-cb844d98cad0 | -4.0682 | -50.0029 | 2024-10-30 04:25:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| a5ea44bb-efe5-3b82-8e7d-3150aa507399 | -4.0866 | -50.0232 | 2024-10-30 04:25:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 65e79b47-7717-3fd3-9345-9e3162c10d0f | -4.0867 | -50.0021 | 2024-10-30 04:25:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e9f856a4-c327-3782-9b89-ad6f66b522ae | -4.2496 | -50.6677 | 2024-10-30 04:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8d63da8d-0159-3e7b-a7a2-a0dd249e615f | -4.2681 | -50.6669 | 2024-10-30 04:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| a6af109a-b614-3484-b0a0-94906b951c3d | -5.9788 | -45.3621 | 2024-10-30 04:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 522a610a-f382-37fe-83bc-cad51bbf116d | -8.8533 | -49.8629 | 2024-10-30 04:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 50f8ef9e-ca45-33a0-a6e6-27c5e8cc9d16 | -10.7175 | -44.916 | 2024-10-30 04:26:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 21b39584-4198-3d65-bc55-14f63221312e | -19.5862 | -56.7136 | 2024-10-30 04:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 8e508131-d727-34c8-a99a-b5e079d5560a | -19.6063 | -56.7108 | 2024-10-30 04:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 129.0 |
| ef320826-aba4-3803-aa3c-f61ca4ba4817 | -19.6067 | -56.6898 | 2024-10-30 04:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 0b72917e-acd5-30ec-8250-5c05ea858b4f | -19.6264 | -56.7079 | 2024-10-30 04:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 510b913e-d0d5-3360-a94c-a0360d5f3bd7 | -30.1518 | -52.02746 | 2024-10-30 04:27:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 2772ba0a-e494-30c9-8c87-18f1081134c0 | -29.81514 | -51.17612 | 2024-10-30 04:27:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 366d5095-7b34-395a-92ba-d6ed9474111c | -29.70886 | -51.15873 | 2024-10-30 04:27:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 41580a37-369f-3a13-a2c8-ae1c12d26326 | -2.833 | -49.2413 | 2024-10-30 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 3ebab025-7eaf-39a7-a060-46e51913dde0 | -3.0734 | -54.167 | 2024-10-30 04:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 67801f1c-2562-391a-8e63-c2b6c8959adb | -3.0913 | -54.287 | 2024-10-30 04:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| c4637a93-8683-39cb-af68-33db5f1bbc01 | -3.1098 | -54.2665 | 2024-10-30 04:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 2a0fcf98-6434-3aa4-ba56-4b8cae7b53d1 | -3.1281 | -54.266 | 2024-10-30 04:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 94177a94-3eae-3391-9d11-969d81c42505 | -3.1601 | -50.6021 | 2024-10-30 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| a6e3392e-f022-3a19-985e-a48120a9880f | -3.1602 | -50.5812 | 2024-10-30 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 25ff6ad0-c3bb-3c3e-a175-96cc4ae62636 | -3.1786 | -50.6016 | 2024-10-30 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| b910e49c-64ae-3ee4-98d2-af77bab3a841 | -3.1787 | -50.5807 | 2024-10-30 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 14d50828-a3a4-3827-ad4f-850ccfd7a53a | -3.2534 | -50.3689 | 2024-10-30 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| b3d0bc1e-b919-3252-a06b-d7edd5f18c93 | -3.2535 | -50.3479 | 2024-10-30 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 171ceb28-ad39-3dd9-aedb-5b9ba54ca3cb | -3.2535 | -50.3269 | 2024-10-30 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| e70d5ace-4c30-33d3-9ad6-cc6c3e4e89f9 | -3.2718 | -50.3683 | 2024-10-30 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 7cf8d1cc-c898-37c5-ab13-0b93b9479c9b | -3.272 | -50.3263 | 2024-10-30 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 435d9c42-52b5-3437-8336-e3da689fad38 | -3.2719 | -50.3473 | 2024-10-30 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 977d8c89-147c-36e7-8c50-66fd3c7a714b | -3.1097 | -54.2865 | 2024-10-30 04:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1f83f402-0c68-3cf7-92ec-cd3977edc854 | -3.5817 | -47.384 | 2024-10-30 04:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 8a2f35e9-159a-378f-a95e-4b48ce70a54f | -3.5632 | -47.3629 | 2024-10-30 04:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| ef3ca9c9-d650-3483-a197-cea0de0c3e27 | -3.5631 | -47.3847 | 2024-10-30 04:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| f7ae8727-2fd2-3dd6-bfa8-a78d02e9b648 | -3.9486 | -48.1291 | 2024-10-30 04:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 534e00c0-8f95-37df-9a5b-fdf185653950 | -4.0866 | -50.0232 | 2024-10-30 04:35:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 604a11d2-9f02-3a46-b95c-66092b92ec1c | -4.0682 | -50.0029 | 2024-10-30 04:35:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 50f0f0cb-37d5-39bd-8fc6-8329974743ae | -4.0867 | -50.0021 | 2024-10-30 04:35:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0052bf40-f3a8-3dbf-84d0-d6629ba204aa | -4.0681 | -50.024 | 2024-10-30 04:35:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0ac8a0f2-9a49-377e-a90a-a241b7de5ba4 | -4.2563 | -43.4368 | 2024-10-30 04:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 975ddb24-2f1a-3cf4-9612-46facb2a8c6a | -4.2749 | -43.4357 | 2024-10-30 04:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 179b4aca-bfd3-3f45-9591-2ae06ae2d756 | -4.2681 | -50.6669 | 2024-10-30 04:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 60f42382-5f18-3d0d-8746-d7b30e54b7fa | -4.2496 | -50.6677 | 2024-10-30 04:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 1d52073f-4aa3-31bd-a4ce-5a398f7a47b1 | -5.9788 | -45.3621 | 2024-10-30 04:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 1b187a8e-0cbd-36bc-b7ee-16ae6883e051 | -6.8592 | -59.0511 | 2024-10-30 04:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 925b978b-751b-3089-b7cf-7bf09cace76c | -8.8533 | -49.8629 | 2024-10-30 04:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| da44eeb2-c7b5-39a3-8f8a-be187f7da8f2 | -19.5662 | -56.7164 | 2024-10-30 04:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 6eb9521f-4a10-3f65-a2ac-251f750dff79 | -19.5862 | -56.7136 | 2024-10-30 04:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.3 |


[Clique aqui para ver as próximas entradas](README54.md)
