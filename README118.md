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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c23113c-1399-35cf-9a2f-9025f325d92b | -7.8029 | -54.72313 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 38c41bbb-9563-3e1b-8ca9-cc258ae6b917 | -7.80225 | -54.72791 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 089fc9f0-649d-3cac-a6bf-c70cfeb83fef | -7.79818 | -54.72192 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fec99f9b-0af6-3140-a030-523f1a4d6c0c | -7.79795 | -54.72528 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 151a33f4-982c-30fe-9787-9c996bfbf267 | -7.79753 | -54.72669 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bb03e46-5d2e-3a75-94ac-a3aa56a8530b | -7.79584 | -54.73997 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5563bd0f-02ff-3ebe-9c52-325f501f3f69 | -7.74549 | -54.78559 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbb3b3c1-8d2e-3f59-b0e6-6e4f6be46f5d | -7.74476 | -54.79073 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c553e19-1b08-3118-90f0-ea9ed7fdf09a | -7.73595 | -54.78422 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc25cd93-3d1c-3cdd-9908-b65f2b6bd743 | -8.52002 | -55.18784 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f122a86c-260e-3a36-8582-5e344f5c1832 | -8.51532 | -55.18719 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fda04210-4ca4-3e6b-895e-cf2c9cbe5621 | -8.51465 | -55.19214 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d5bac8b-31ab-34de-93b1-89cd4b862b0d | -8.50058 | -55.19016 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85d8df5e-b58f-3e09-9bc5-24e80e9ef1c0 | -8.49588 | -55.18953 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67dd2a17-87ba-3d88-9332-4f6cf3eaa864 | -8.40918 | -55.03643 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa1abd99-68e4-3dc2-bc3c-9df9a00d6bf3 | -8.40512 | -55.03086 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10d37145-24ca-3f84-bd8f-239986acac94 | -8.31894 | -55.01796 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9e306fb5-f5d7-3511-8c4a-806c19d16a13 | -8.3149 | -55.01223 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 303ac84b-2700-36b5-95e2-3464b9929c93 | -8.3142 | -55.01731 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c8b919e1-2880-3c1f-9567-0a3095997b37 | -8.31154 | -55.00142 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0497245-3a38-3705-8bec-270edd9aea79 | -8.31085 | -55.0065 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4a0e9b4e-96c6-3585-a364-c559147d9cee | -8.31017 | -55.01152 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 29dbf84d-fb4a-315b-9f3a-bd9650e1f851 | -8.29581 | -55.39101 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87a96416-443d-3348-ae6e-fcf08a08b224 | -8.29514 | -55.39573 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b3ad591-9562-3638-9cdf-e0d4ebb99798 | -8.2912 | -55.39034 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3296300b-f00d-3354-8180-d7b6da40f7d9 | -8.29054 | -55.39508 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1019d33-41ce-339a-8f57-c09774fe560c | -8.75241 | -54.98814 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e39fb9d6-d62c-3919-9cc0-f4ddf0cbcd9a | -8.74766 | -54.98733 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6ebb2b6-6324-32ec-bd74-c6d04805f65e | -8.51934 | -55.19274 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67f7fb32-0922-3860-ba01-8f9536d2a0eb | -8.51867 | -55.19764 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2720f52-ac31-3e77-b0bb-07ea13062153 | -8.4912 | -55.18883 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f913637c-3fe9-3f9a-bac4-a6778c772dc9 | -8.40581 | -55.02576 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d94f3a99-2f7d-37e6-8c94-aa55f32b6fdd | -8.32298 | -55.02364 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c1fdb2fb-467b-3fee-b233-7ea41b860461 | -8.31628 | -55.00213 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 452b1e53-3cec-3847-8da2-3a283ef428f8 | -8.31559 | -55.00719 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0fe15dac-ed7b-3750-8d3f-5274cc98ed22 | -8.11976 | -54.79746 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79831185-acce-3011-adbf-b0b4339631ae | -8.11905 | -54.80265 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2285b91b-bc6f-3b07-9d8a-5e5a64503cad | -8.11835 | -54.80783 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f35c5458-6301-3a68-b06f-f3650661cc76 | -8.11569 | -54.79147 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dec6fcc9-0526-32c3-a6a3-2b81bb6d3c68 | -8.11425 | -54.80202 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65eb2e93-cf71-3ab0-a928-3c5cd84a74f3 | -8.11018 | -54.79604 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2d321e6-f377-3b23-9bd3-6e2ed274fc9b | -8.11851 | -55.35608 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38914d38-3381-3334-a3d9-6df8a67422a7 | -8.11509 | -55.07747 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e87942e-c779-344a-9338-79e0c7877091 | -8.11389 | -55.35545 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93572661-6d4e-3715-97d6-376ea81f19b2 | -8.11369 | -55.08749 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1ae40f2-fd61-335b-9a36-856c00889f7b | -8.11109 | -55.07172 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc72f1f4-c498-3f55-824a-f41da2520f26 | -8.1104 | -55.07674 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a846b294-c825-3f15-a5f0-5ac21d029da2 | -8.09926 | -55.39227 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf4a898e-30d8-3777-a543-4a727f385fc4 | -8.09858 | -55.39708 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24dc0820-f0eb-3190-80e3-d15cd82fc3c9 | -10.68756 | -55.53524 | 2024-09-27 05:27:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ec12a37f-c0e7-3091-8c31-2d86c3c5a61a | -10.68381 | -55.5365 | 2024-09-27 05:27:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cb67e998-58ac-3eb5-b2eb-96bfc6d9c6b1 | -7.06831 | -56.47224 | 2024-09-27 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5da4e251-ae78-3bec-81d4-aefa53d9e29b | -7.06944 | -56.46445 | 2024-09-27 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f72ee17-770a-32aa-9e7d-26f9fc4e79f7 | -8.33336 | -56.49454 | 2024-09-27 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d6a96fd-6a76-3183-95d8-283489f50c05 | -8.32908 | -56.49397 | 2024-09-27 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5380dcf6-72cb-3d12-8f74-680511df8b5c | -8.3194 | -56.50076 | 2024-09-27 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4eca60a-fb2b-3b42-b5b5-f2d78a2128e9 | -8.3248 | -56.49337 | 2024-09-27 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55e4ffbc-cbad-3543-adef-fb1f1b7116a9 | -8.31513 | -56.50017 | 2024-09-27 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95fe859a-be5b-3ca7-973f-03688027985f | -10.53318 | -57.78121 | 2024-09-27 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e918551-04d5-38f6-915d-28855b46cb9a | -10.52507 | -57.78008 | 2024-09-27 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a32f647a-322c-3a6f-8a0d-631d92f591da | -10.53368 | -57.77763 | 2024-09-27 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5845f01d-1956-35d8-9165-573a1b426393 | -10.52457 | -57.78363 | 2024-09-27 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a45a446-4f8f-3c20-8769-f6f5ac76a2c7 | -6.86818 | -58.93166 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94f184da-8f01-3078-8add-d959fcbe7347 | -6.83149 | -59.04141 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f31f2d2b-333a-3d92-b75f-aee8fb6fc014 | -6.8279 | -59.04087 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d03eec44-e09c-344c-bf57-12720566fad2 | -6.82727 | -59.04496 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2d1d35a-8f79-3cf3-8c82-bba42dbc6088 | -6.82665 | -59.04904 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 111e3194-49d1-3942-849d-092246c71ad9 | -6.82369 | -59.04441 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 155274d9-9f3a-3cf7-8ceb-1dcb1bd394d9 | -6.762 | -59.06445 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b9e41f3-b189-38ab-9b35-75c32b690d7d | -6.76138 | -59.06853 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a2fbe92-b486-310c-bcf4-b515e90f5893 | -6.75959 | -58.90789 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d9fc34f-c154-36ce-817d-0925ded79686 | -6.73868 | -59.07348 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6862f281-ea40-3bde-bc65-5d34ba890ab8 | -6.72784 | -58.84136 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e610f32-c44b-3b57-8101-e3ffeadf1a8e | -6.708 | -58.92352 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a1fd230-7492-366d-afb0-3378d54d1907 | -6.7044 | -58.923 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3da8728-c708-3e2b-ac8e-35cabada9b47 | -6.70377 | -58.92716 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 199d2eec-45b0-3d84-b91f-77070836c7a6 | -9.23767 | -59.39711 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 60af56ec-e73c-37be-b8c1-36f42a3f85b6 | -9.08852 | -59.39751 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3de8cb87-4d31-34fe-94bf-40e2c419906b | -9.0849 | -59.39696 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0d7a4b4-58a1-3ebd-b074-74d9002a5f87 | -9.13914 | -59.40504 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d78dacbf-a79b-3325-a1d4-d0070e8044c0 | -9.94127 | -59.5651 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78c9908c-b351-3832-9ff5-aacdadf96c4d | -9.38916 | -59.61315 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a7c5342-9ca3-38dc-9985-ce9dd2dff5f0 | -9.38435 | -59.62089 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 968b6aab-fbd4-338d-b375-c21721fe76b4 | -10.07029 | -59.34659 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c45e0a8-7f88-3879-aa4d-7a93c88bfcba | -10.06966 | -59.35092 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3f9b335-5a9a-34f0-9beb-d380c145129c | -9.38794 | -59.62142 | 2024-09-27 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 078b4060-bf0b-34f1-a2e3-875796c3a0d8 | -10.34825 | -58.91832 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aace7316-b7bb-35ec-a254-afaca5dd5dd6 | -10.34384 | -58.92224 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4aec072-290c-3599-8cd4-24696369018f | -10.06821 | -59.41242 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d1d561b-16a0-3364-8770-9dbda14d1d8b | -10.06601 | -59.35032 | 2024-09-27 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39e8a085-4581-3f2d-b28d-825678bd71c0 | -12.15497 | -59.73767 | 2024-09-27 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9cf6ade-e2df-3493-9eda-5647ccc6a6b4 | -12.15306 | -59.72991 | 2024-09-27 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d0cc525-3c7b-3c8c-ab3c-e033e7e25290 | -12.15241 | -59.7343 | 2024-09-27 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61ae995d-4735-3280-b409-2ae61917fe42 | -12.15191 | -59.73271 | 2024-09-27 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0857e057-e507-3282-bb7b-d92996731e4a | -11.51271 | -59.48831 | 2024-09-27 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6dc256f-40a2-3b26-8924-a8bd71692f0f | -11.49939 | -59.44979 | 2024-09-27 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fb93b67-957a-302f-a02c-fde6f7a37fbc | -11.49699 | -59.44024 | 2024-09-27 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8359708-9c6d-3bdd-a10e-60a4d04d3df2 | -11.37504 | -59.1361 | 2024-09-27 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a55a082-d415-38f7-addb-854b0d9ef40c | -11.37432 | -59.13798 | 2024-09-27 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7938904-520b-3917-8445-3db2dbbe24e0 | -11.52752 | -59.4905 | 2024-09-27 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README119.md)
