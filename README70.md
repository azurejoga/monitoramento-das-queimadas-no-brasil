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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd9258d2-169e-3452-b3ed-1ecbd114afa8 | -1.60658 | -46.88236 | 2024-11-24 05:14:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 74d60df1-34b2-3075-a95e-e4a1c2c8f261 | -1.44853 | -55.22385 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab46411d-df21-3895-a350-11b180a273df | -1.72088 | -52.4888 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87d06a9d-12e2-35fb-b9cb-52775696ff3a | -3.03289 | -49.45232 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1bfac2b9-7b50-354d-b396-e270fc135be2 | -3.49823 | -50.46964 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2daf973-162f-3232-9a36-9867adc744b6 | -2.2123 | -50.8769 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1098abe-257c-3754-a1ca-d0d7113a46d8 | -1.06347 | -51.75364 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38fab278-8fd4-3096-a8cc-0984a149e450 | 0.40947 | -50.85755 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a29763d0-6f47-3579-a377-6d5a5a7d8220 | -2.03848 | -52.10066 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73df8a0f-720c-3705-a440-266427d94c29 | -2.01297 | -51.17059 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 285157ec-647a-3f20-b4b9-f3bc570b133e | -2.81699 | -52.86093 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 215bed14-b915-35bb-aee6-60b617856f38 | -3.12371 | -53.1043 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31a77c15-7035-30ef-b88a-1342ea52251e | -0.04271 | -51.60143 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 374e3986-b017-3d79-8422-fa568102b043 | -2.17685 | -53.795 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a111b36-2ac6-3b41-9940-afd773cbcc01 | -2.28336 | -47.311 | 2024-11-24 05:14:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bf61bcb-a547-300a-8322-388506a85b54 | -1.13449 | -51.67719 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84411834-0e31-3027-92bb-ecbb521edb0e | -1.64449 | -53.87101 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a07b9b0-4948-361e-b6da-40b0a48ea712 | -2.21063 | -48.91008 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b784f1ea-c2ad-3af6-b10e-9fe5002cf4b0 | -3.23839 | -54.24048 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad6714c9-f0dd-3639-92ed-72f05892839c | -1.69387 | -52.61142 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8d1a088-308f-3e8a-94ac-2fd6e197e09b | 0.40501 | -50.85824 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ed41856e-0949-3648-99ee-1ba708a82659 | -2.27824 | -53.62902 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d905c2eb-bf38-3fd4-b0f9-d5f3c61dfe6b | -1.69759 | -55.01465 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee0d0b80-533c-3921-ba15-969018879e10 | -2.94473 | -51.43071 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 602ebc0f-2047-30c1-9300-3c53f7b93f37 | -2.61884 | -51.79541 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22f5e8e1-a0c1-3de6-a03d-08568dcabe9d | -1.48014 | -52.51681 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa8995cc-5133-388f-bbb1-4836181d9bb9 | -3.0693 | -50.95292 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6be93305-794d-3fa4-b77b-e6dbd02bfd07 | -2.44593 | -49.08343 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9c7ebe2-5d0c-3b3d-936c-c6644785cc41 | -2.82317 | -54.03182 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ef3b4e3-7ce3-3da2-bf56-24d232416d3f | -1.19754 | -51.76844 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d82273a6-aa89-341d-800b-2c96054c1d53 | -0.95961 | -51.64398 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abcf148e-0c4c-329c-b2be-41854a6271f2 | -2.45168 | -49.081 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1246881b-c8ec-3942-aac2-2ba8d755d0c1 | -3.26785 | -53.81979 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d4c12619-42cf-34ba-bc71-1cdcdc9ed425 | -1.60788 | -52.57661 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85f8cdb1-ce0f-3bd2-a53a-1e197258a856 | -3.50172 | -50.46589 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fea284d6-3327-39cd-a36e-af7ca131194f | -1.22895 | -51.73608 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4774dc9b-d69f-3637-b735-9053644f3259 | -2.15036 | -50.91801 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 832a50c6-40b8-3431-9897-4ff4852e70bf | -3.22602 | -53.93957 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f691bcee-002f-3285-bf02-8a464f738e51 | -3.04066 | -54.02197 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c21ea0a2-6c52-377f-b4bb-11bddd6cc5ba | -3.95483 | -45.99697 | 2024-11-24 05:14:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0aee520-4485-3cf6-bf83-53b7106e2462 | -2.83743 | -54.0151 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afb11dae-9cfd-3795-985f-0ebf2b9af7d2 | -1.38504 | -52.3371 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a3f9e7b-ceaa-30f0-953e-e7160854c3c5 | -1.27866 | -52.24499 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1e3a410-0a2d-39ec-8ee4-1601b791d235 | -2.86058 | -53.9665 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5c40a6ed-5e30-3ce5-9caf-693c0c11052b | -2.21705 | -46.39236 | 2024-11-24 05:14:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 47425312-ed5b-3a7c-98e6-e3ab8325f777 | -3.18695 | -54.32468 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2e943aa-6ca7-382b-9da7-0eab6d25dc2c | -1.44948 | -53.39925 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b58a014b-767a-3e31-b2eb-c4288c1cde2f | -2.7548 | -54.07309 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 261564db-4ff9-37db-a1f8-73b0bb7bb086 | -0.87703 | -52.76891 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b479099-8ff9-3f65-8557-2988ca75ca6a | -2.14884 | -50.92094 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| af86e9c1-89d7-3556-a322-894061d4c5de | -1.4568 | -54.50564 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4210050f-4354-3c9a-a0db-6d3441be9e99 | -1.72556 | -52.48576 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3670e998-4cbb-3792-92b7-b0ca7add1b69 | -3.10779 | -54.00637 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afdad6eb-5393-3e90-b65e-3a05ccd0e202 | -3.34127 | -50.50514 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 387f1992-c0cc-365c-9a10-02ff93a0a366 | -1.59749 | -52.58982 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3fcbb4c1-8741-305d-9c50-4cbc8ca2ddef | -1.58307 | -53.8222 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af6ce7bc-ff66-3f10-88f4-7bd690203597 | -1.24031 | -54.01046 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 79f07b8a-42b3-3469-ae60-2b5334c7cb75 | -3.95428 | -45.99181 | 2024-11-24 05:14:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f94d4153-d01d-303a-9068-d6c5c903cc5f | -1.72343 | -53.25687 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f479964-5db4-3519-b0fa-f57b93c02688 | -0.57152 | -51.72274 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b71e4245-94a1-3cf8-8916-13f72f1ce089 | -1.73385 | -55.24567 | 2024-11-24 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8660228-3ee6-3c8d-a469-5864e4a00bbb | -0.37398 | -51.55136 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cce941a-75f0-3e88-ab43-409d1c48b201 | -2.23618 | -53.66474 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cee6b7ce-54c5-3806-bd4e-b71d40dd8fa7 | -2.74147 | -49.11466 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d388c3c-7d75-3572-9a08-40ca4eb317cb | -3.28567 | -53.83269 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b14fd8c3-0bdf-3aeb-985d-152e3104925e | -3.28879 | -53.8381 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c2e6f8c-2e9f-3475-819c-85301c817b04 | -2.75859 | -54.07367 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 413e95b5-0be4-3f47-b9d2-e0a21f04dac9 | -1.12309 | -53.3866 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 555791af-8f93-3c36-9219-11f165eb3efa | -1.20986 | -51.74554 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8a273ea-ee22-3212-9f6e-494ba79070cb | -1.22464 | -51.73542 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e0f8b87-4457-36e2-8160-6bfc8fbacc7d | -3.10641 | -53.10548 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c25880c5-1079-36f7-b283-eb07fc30ecd2 | -2.4632 | -49.03975 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4a7ee92f-d440-334e-9b66-88a2c3b98ec1 | -3.23057 | -53.93545 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5576068e-b426-3be7-a111-8b6adb97fcb6 | -3.06341 | -53.22373 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60645069-a365-3138-9ab9-01768c011ce6 | -2.45121 | -49.08422 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 467ef3f7-3ea9-3f88-8e4e-5c029a34f391 | -3.28751 | -50.04141 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba8fa53b-b479-3ab6-8f7b-b515104286db | -1.04393 | -51.73833 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c0d58a0-3551-345a-9cee-960e724caa6d | -1.20556 | -51.74487 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63fa5565-8401-3b62-a6bc-7ce2eb1b1740 | -3.27721 | -53.83625 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1541ad51-d339-3229-a21d-827004fb3c16 | -1.51074 | -54.18527 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| dfa654c3-5f9e-33aa-bcf1-61f07cd42494 | -1.2449 | -51.7468 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39b39948-23b2-35b0-ae34-a1aca46e1af2 | -1.28854 | -51.73114 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c070d7f7-d573-3697-953c-c1346a7b6b70 | -2.7387 | -47.54056 | 2024-11-24 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 991874ad-8e34-30fe-9a08-fe15e058fe7e | -2.82095 | -51.79201 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44794314-3216-3354-b3ce-0c76a632cf60 | -3.23691 | -54.09926 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bb45f57-a61b-3a76-8363-2212c077e818 | -3.29817 | -53.85424 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce0a440b-a425-31b4-a4e7-54c21aafba37 | -1.51812 | -54.1865 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c389cf62-3b57-34f8-a3de-3354d9f0c527 | -1.58781 | -55.87273 | 2024-11-24 05:14:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f199ac6a-2106-3736-af6d-6d716755601b | -2.76616 | -54.07484 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2600e236-d096-30c1-a195-433295dbd0e4 | -1.11847 | -53.39084 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c057c7b4-82bd-306b-bafb-e47626e8a11b | -1.60902 | -54.41347 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e7191b77-637c-3d1a-a624-867ffe127967 | -3.10467 | -54.0011 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35c2620f-0320-3663-8851-904f47d16283 | -2.51357 | -54.11179 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 27bafee9-3e1a-3c4a-b2fd-2db65a4e292c | -2.17745 | -53.63614 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62aeb93e-b4af-3e1a-8c86-ffb16eb1e84a | -3.25746 | -53.70467 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4823eaad-094d-3f05-ac7e-33a22b5ed172 | -3.13718 | -52.98597 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0178f9a9-a107-38b6-99d2-aed6ad7fdf4a | -3.48874 | -49.91817 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93a20b9c-0fac-3623-88c8-93a07183623f | -3.355 | -50.51272 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ecaec45-c629-3d2d-944d-6eeff287078f | -2.28928 | -47.31187 | 2024-11-24 05:14:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f20698e-3f67-3160-9d8c-a416f353e835 | -2.3241 | -53.86766 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |


[Clique aqui para ver as próximas entradas](README71.md)
