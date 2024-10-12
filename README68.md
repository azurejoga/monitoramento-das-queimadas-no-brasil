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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0c926b3-69da-3767-9da0-8e3ebd9de658 | -2.18746 | -48.24954 | 2024-10-12 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1233dc2-0bcb-3a93-b915-d7e0d82bfca7 | -4.37904 | -48.61617 | 2024-10-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8cdc8251-0a49-3f20-9571-56036eb8e0d5 | -4.37851 | -48.61975 | 2024-10-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9dc54aff-0c8b-35e3-b658-cb738ff90d0c | -4.28965 | -48.62845 | 2024-10-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 035ec8e1-8798-3c9a-b8eb-edd2ddc34f54 | -4.27894 | -48.23125 | 2024-10-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fcd0d1b-a9f4-3a06-b526-955d6f788be7 | -4.27481 | -48.23055 | 2024-10-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d682443-d828-3951-bb0d-890ad9e90909 | -4.27424 | -48.23426 | 2024-10-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62565996-b342-34a4-984a-1c804b20a80e | -3.91986 | -48.34456 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cb0048c-76a9-3093-b9c0-d12f2c98a94e | -3.91931 | -48.34819 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6006c704-48db-31ca-a47a-e847fe15407f | -3.91876 | -48.35183 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04f7d5e3-74a4-3f0a-958a-5971c2e3ee13 | -3.91821 | -48.35547 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 990f285c-b76e-3766-8e48-e209eee9f55e | -3.91577 | -48.34397 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 671403ab-22cf-3f7c-b298-da00e4fbcdef | -3.91522 | -48.34758 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cdbbc23-bb2a-38ee-a3eb-cafedac950f4 | -3.91467 | -48.35121 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 588576d4-f1b3-3b8d-822d-8599c391e2cc | -3.91412 | -48.35483 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9369aacb-3a18-3ecc-89ea-019a2559eea2 | -3.91003 | -48.35423 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e580c4a-0614-32ae-b2a5-e4890dff8389 | -3.90948 | -48.35786 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7797823d-9eff-3ce4-9766-d057d11212b3 | -3.70667 | -47.92587 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 45bdb746-6a4d-3eac-8a1b-3add0c43f897 | -3.7061 | -47.92977 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 93d13255-15db-3cf7-99cb-524cca5506ab | -3.70248 | -47.92523 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee0ba19c-89ed-34ba-a6a9-1bf3bb64d3ba | -3.7019 | -47.92913 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0336fabd-120b-3684-972c-24eeef585238 | -3.69828 | -47.9246 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 599ee778-e4ce-3d0d-9304-e95c5e24e6c6 | -5.09411 | -47.93065 | 2024-10-12 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 122668db-1fe9-3342-964e-a7fefd7a4fa3 | -5.09157 | -47.9279 | 2024-10-12 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7669eb0-07d7-3c6e-85ff-0367c3871ebf | -5.09096 | -47.93196 | 2024-10-12 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e21b61e-7183-3340-85c1-ba6dbac792c0 | -5.08981 | -47.9301 | 2024-10-12 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ecf2858-dd48-3906-8e8f-aab67c1ab6aa | -5.07232 | -48.08396 | 2024-10-12 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 090eb750-5825-3926-915b-931351b0073e | -5.07232 | -48.08246 | 2024-10-12 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32273c42-6d16-3b31-9e70-9323f138889f | -5.06808 | -48.08336 | 2024-10-12 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed3dafd8-5c6e-3a86-8e18-12f2269a3fd0 | -5.06807 | -48.08186 | 2024-10-12 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ba0dc88-4d8d-3de0-b741-4656703942ca | -4.95468 | -49.14456 | 2024-10-12 04:57:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08161098-0197-3f61-a1f8-ae0a67fb6b4e | -4.83432 | -48.93528 | 2024-10-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd05eb1f-6bc2-338e-8e2f-847fac78d450 | -4.74061 | -48.87877 | 2024-10-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af8b728d-727b-3ff5-9f09-b49a8c191f2a | -4.69884 | -48.62302 | 2024-10-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9496b9bc-79f3-3a24-8e1c-22ae2b0a5a24 | -4.69477 | -48.62245 | 2024-10-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4889c7f3-934c-3e4b-b9c6-97134b90c7ff | -6.42496 | -48.26883 | 2024-10-12 04:57:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 8.4 |
| bd897b65-960b-3ee5-8b08-4ee89f88fcdb | -6.42069 | -48.26822 | 2024-10-12 04:57:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 311818dd-518e-3f79-9b28-a798155c68c7 | -6.4201 | -48.27226 | 2024-10-12 04:57:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 8.4 |
| af683545-acbe-3767-a9ad-b7b63597cf89 | -6.40437 | -49.16857 | 2024-10-12 04:57:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a21e1369-40d5-3b37-845f-b83af2febd8e | -6.08128 | -49.12804 | 2024-10-12 04:57:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 950abef4-c37d-304a-aaed-4e4e717aa4fc | -6.07273 | -49.13036 | 2024-10-12 04:57:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c7041a8-abd2-31bb-a640-eae4c6102467 | -6.06872 | -49.12976 | 2024-10-12 04:57:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40a80a36-1882-3f42-8f99-ed7311062e14 | -6.06821 | -49.13323 | 2024-10-12 04:57:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7137cbee-4c1f-3bad-9803-dd24e9ac9186 | -6.06267 | -49.03138 | 2024-10-12 04:57:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecb79e29-57df-361c-962e-6fc336d5455f | -5.97603 | -49.2437 | 2024-10-12 04:57:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c18de9dc-dadf-34ec-a10b-2cd62baa5c4b | -5.73349 | -48.46918 | 2024-10-12 04:57:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e61e05a5-b70e-3f2f-a6df-7410831fbe7e | -5.71596 | -48.50148 | 2024-10-12 04:57:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3fd20aa-3e70-37ba-b482-bd6a9bb0aec5 | -5.51272 | -48.0857 | 2024-10-12 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a68ee72-e0a1-39a3-a2c2-742ae56b961a | -5.50845 | -48.08502 | 2024-10-12 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffb5c97e-d569-36b2-85a0-c0529191f72d | -5.50554 | -48.97106 | 2024-10-12 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64a22b1e-0b01-3e54-8774-aea59b12deb6 | -5.50554 | -48.0821 | 2024-10-12 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cbc1362-0e93-34b0-af8c-4331885a790e | -5.50494 | -48.08607 | 2024-10-12 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7f13410-7eb2-3eea-a509-cebc142b173e | -5.50434 | -48.09005 | 2024-10-12 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2e7e411-45b3-38e9-a7d2-fc7dc865078e | -5.50419 | -48.08434 | 2024-10-12 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f50e218d-079a-3dc0-be47-5c8061ac016a | -5.50362 | -48.08833 | 2024-10-12 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7670846f-6986-3fa8-9769-31bc8a361de2 | -5.44602 | -48.91889 | 2024-10-12 04:57:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2be45dc8-ec08-3363-b073-e198b5a58cc8 | -5.25162 | -48.0419 | 2024-10-12 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 9f7223b0-508d-3766-be0f-685a7752d6eb | -5.24795 | -48.03726 | 2024-10-12 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b40726cb-81cf-35f6-b730-6651088d6e50 | -5.24736 | -48.04126 | 2024-10-12 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| fbfd7868-58bd-37df-877b-5d589e515e56 | -5.24677 | -48.04526 | 2024-10-12 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 32c10ade-f3a2-3004-8b09-1c5c8aafe904 | -5.24251 | -48.04461 | 2024-10-12 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c167b47a-6639-3da7-b85e-70ddc0aedc92 | -7.07579 | -49.25143 | 2024-10-12 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 000ec527-1034-3474-bf2f-2f17068943f7 | -9.1873 | -48.95443 | 2024-10-12 04:57:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f0ecc75-c8c0-3d6d-9cfd-9628ecd1dabd | -9.18304 | -48.95394 | 2024-10-12 04:57:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7e350bf-834e-3b5c-9175-25b5dbce9786 | -9.03104 | -48.80778 | 2024-10-12 04:57:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47e5aa4f-fabd-3d75-892c-390e037f5548 | -8.06767 | -49.77637 | 2024-10-12 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 802a5665-5595-3ee8-8fac-b760b0427f94 | -2.20014 | -48.84472 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e471843e-3c47-3345-80d8-be972d06dff4 | -3.46385 | -50.60952 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 249a57d2-c488-3389-bdcd-29e5efe4491d | -3.46092 | -50.60488 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0f4b692-0a89-38ab-8c1c-95d6de0ef2ab | -2.94904 | -50.49426 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10447aeb-9bc0-3180-afdd-4b83ed2ee9ac | -2.92988 | -49.49738 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a3a03eb-738e-375c-a233-633fe5100c4b | -2.90573 | -50.39635 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fbcd8f4-ae8c-30c6-ab29-3696bb9c526d | -2.90216 | -50.39579 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38334cc3-cb2b-3327-9c05-65f42407e6d3 | -2.84352 | -49.86899 | 2024-10-12 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe213ec8-f058-328f-a478-109ff167320f | -2.83609 | -49.52699 | 2024-10-12 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab10a9ef-a2dd-30e0-b78d-be380b5d5fdb | -2.83541 | -49.53149 | 2024-10-12 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 6f89f2a5-f0b7-3329-ad07-4124de2b7aca | -2.83235 | -49.52639 | 2024-10-12 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c5261bac-839e-3fde-9cfb-67006914f5ac | -2.83167 | -49.53089 | 2024-10-12 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| a555cf96-058c-3f75-abb5-734be578f29c | -2.82793 | -49.53028 | 2024-10-12 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88d2258c-e5c9-3ba0-99e9-97b8ecb21755 | -2.77681 | -49.22867 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6747740f-a261-3947-b14d-b3d1fab636a4 | -2.7761 | -49.23334 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 302842c7-aaef-3d67-b7bb-cd4917d706d9 | -2.7723 | -49.23274 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbf3328a-02fe-3283-aacc-0108b3522296 | -2.73745 | -49.53645 | 2024-10-12 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd34726c-0767-338e-8b52-f5c36f1cc69b | -2.73264 | -49.1593 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ee67b62-9893-3f2e-bfc9-f1e281e4a406 | -2.73013 | -49.15697 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18bbeab6-2510-3c04-a3ff-a1299504ebd6 | -2.72527 | -49.78763 | 2024-10-12 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eaf44da-1d9d-34e4-a595-1e773d325b58 | -2.72325 | -49.47897 | 2024-10-12 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 032dd2f7-af70-3cd5-b849-1030e7ccd5e9 | -2.72256 | -49.48345 | 2024-10-12 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1765cc3f-e6a8-3db0-a177-9d8f3374c1d4 | -2.72018 | -49.47387 | 2024-10-12 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 384c3bc8-4f8a-3a0a-9245-f85019ec29bf | -2.7195 | -49.47836 | 2024-10-12 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3835965e-3521-30bf-ba53-a2315d1aa1db | -3.33431 | -49.13118 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3f0251c1-666e-34be-8d14-99afdd792768 | -3.33377 | -49.16073 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 520f4800-4425-3db5-838c-a31c46139776 | -3.29625 | -49.10893 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07b1209a-600e-3111-b640-d3fe14448c3e | -3.29401 | -49.11023 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00b8b5e8-0cd5-39e3-92de-5eccb235e6a4 | -3.29313 | -49.10354 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e429011-0e06-316a-b70f-8d9e1353277e | -3.29159 | -49.09995 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7018ff4-5c8d-37b2-8966-f30a2d2a99ef | -3.28844 | -49.09449 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62c513ca-6e34-387b-a2be-a671652d349c | -3.28616 | -49.09751 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29dffa1c-6ccd-3535-866a-0c9583780f75 | -3.28457 | -49.09392 | 2024-10-12 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3da258ce-ed54-3f2b-b27d-4e8696c0549b | -3.1643 | -50.43807 | 2024-10-12 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README69.md)
