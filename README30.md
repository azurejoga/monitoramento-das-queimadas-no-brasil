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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee89623d-e47a-3775-904e-ede1b917255e | -2.89479 | -48.29888 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1bbe14a-b547-3a31-91f3-59938187c47a | -3.94779 | -48.99773 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 56cf5638-5cb4-358d-ac2a-8f81d7a87006 | -2.33657 | -46.5671 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4648e8d-49a0-3229-848f-c249996b971c | -3.54472 | -49.98398 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4500c64d-9dc4-3453-9da6-536985361a28 | -2.20667 | -47.74694 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00a80726-a082-3766-a77d-125d7169e457 | -1.53181 | -52.20897 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d59d3b1a-2aed-3794-badc-0cccdfadce60 | -2.11319 | -47.89458 | 2024-11-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fddb371-03d9-386c-97b1-0a3233897fad | -3.23105 | -50.27652 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ffb0cde1-8b39-3c92-8c28-9ec262b4ad10 | -3.24932 | -50.30886 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8102eda8-8bb2-34d1-8370-917f15c08f62 | -4.49002 | -44.48111 | 2024-11-10 04:14:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a39f93b-852f-31df-8e8f-12a02f9ac860 | -5.6727 | -41.7625 | 2024-11-10 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dde28374-fc37-3123-91d8-ea08a8cab4be | -2.09861 | -46.54939 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| deae790d-b8be-3f5c-8a07-53be5cb97e77 | -3.14839 | -48.58123 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 351633c3-af63-3f04-84bb-eef892d11fdd | -3.14014 | -50.43406 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b6ddeac9-63d4-37a6-97db-efa6a36e5e80 | -2.24378 | -50.72141 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85936ca7-2655-3369-9435-7b019fc492f6 | -2.64753 | -51.8816 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a7f842c7-eb7f-3fea-97b3-64d7d98ae7a5 | -2.65825 | -48.56266 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76c97d86-1448-312a-a2eb-c2719338cbe7 | -2.68494 | -51.82275 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5d23bca-5f3c-3fc1-aa8f-079558c5b473 | -3.04842 | -49.5456 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8b6d2894-ff55-37b6-a0ed-08b0fca70587 | -1.39973 | -52.36428 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c5c7121a-493f-3d2b-ac6b-d2922840d5b5 | -2.62274 | -49.47224 | 2024-11-10 04:14:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b38f818-f49e-3c69-9327-76db5c8664a7 | -3.27058 | -53.70448 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b291100-effa-3f08-bdad-054c20adf838 | -3.24613 | -50.30636 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| be823716-f942-3969-ac4b-35d1f652ba52 | -5.52994 | -41.69341 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| afb7906e-3c0e-3650-995b-fa8a4efbb903 | -2.86249 | -48.44602 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cec67064-1834-3238-a679-140e24a20e4e | -1.83923 | -52.15503 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a943350-a3cf-3f9e-bc36-6b35113dc214 | -3.35516 | -50.05737 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77e6dd42-0e1c-3a4b-b314-8ae4e1a2e4a5 | -4.85157 | -48.48457 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c180c26b-3f49-360b-8e1e-66154d3d810c | -4.15896 | -45.74949 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bc85d8c4-a481-3184-8258-dc0474e01938 | -3.51221 | -49.49906 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3560f6f-9237-3c7f-82b0-fbc618f2cf1b | -5.41975 | -47.69877 | 2024-11-10 04:14:00 | NOAA-21 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15f53151-1cf4-3f65-9e79-fe270ca23e0a | -1.54193 | -52.21852 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6d882910-383f-3d48-b8c1-4f4114a6fff7 | -4.52256 | -45.6995 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8daff46e-5b38-3af3-b190-d0a57d5b52e4 | -2.81395 | -51.8061 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 276ccd2c-ce16-385b-acc1-d31e592d5aba | -1.67008 | -50.49033 | 2024-11-10 04:14:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a0a0dd8-8f71-3572-bd10-cbdfc5cb5172 | -5.63958 | -46.97729 | 2024-11-10 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc39dbd2-c9ba-3eb0-bfee-8a03c26afdb9 | -3.95657 | -48.99907 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8ec962aa-ea16-3954-add0-055326446c4e | -3.8701 | -49.95192 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 98bd3791-de57-3e22-a7ee-0f7e34015b84 | -3.92294 | -50.25352 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adba225a-a5fe-34cb-beed-bca270d737a4 | -2.67952 | -51.82183 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21f7e06d-246a-39de-88ac-9af98668682b | -3.16862 | -49.09491 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ea304c8-995b-3564-bb31-cf5f6ddaf140 | -3.51293 | -44.02575 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea002619-aca5-38ff-bca9-aba600ab0323 | -4.2781 | -50.66753 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8d2b4db0-3542-3618-ac11-e6fc2e916a07 | -6.23319 | -42.93087 | 2024-11-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fb79c477-5b1c-3fec-ad35-7567ee7b31e0 | -1.87325 | -54.18165 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f3b5f2dc-0c40-3b71-a687-d5954978e535 | -2.29442 | -48.55514 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf968a95-b0b4-3989-b821-81c6cdd31fb9 | -3.08834 | -50.42955 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d085c712-8bce-33fb-b0ef-d81cc7a682d5 | -4.51448 | -46.34219 | 2024-11-10 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fe2c56a-52fd-36e8-a897-8ec1ca6ee03b | -4.20414 | -48.54586 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9bce73ef-1703-34c5-83f4-b73542ebc17d | -2.45934 | -46.32759 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ac01838-56db-3c97-a213-8b541d4c4d14 | -2.0364 | -46.54467 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 668caf88-10ac-32d9-a637-bf58dacce551 | -0.10914 | -51.75788 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc757ddc-2531-3a06-adca-405a36c75338 | -0.04375 | -50.79275 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be5d7c98-9d3a-35e8-9073-0e0306f70df4 | -1.49886 | -51.56162 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b07419bf-9a5f-3206-bfb0-ed489066620a | -2.14226 | -46.68594 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2893881-2410-3405-80bf-f2e9c4d0e6d3 | -2.60815 | -49.81623 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0bd464d-d84c-36cc-981b-30ab9f77aa66 | -2.65416 | -51.88282 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5f57a199-fdac-3ff0-ae53-8da5211c900a | -3.22671 | -50.68612 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c1685787-1165-3934-ab3b-c4d9df0a6f0f | -3.21743 | -46.48947 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fc26276-67b4-3c53-ab01-f119b421cf75 | -3.95332 | -48.14393 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36057151-0c94-30f5-bae4-281e0fb21b4a | -5.0623 | -50.00614 | 2024-11-10 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 05673928-4b94-30a0-b837-25586da79dff | -4.11615 | -48.49997 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ecc78c3e-b9c7-3766-919b-6218ed96adf6 | -3.53591 | -49.25953 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 054274e9-ca25-370d-9a87-89744389f01a | -2.17191 | -48.31219 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63d440ed-fbe2-3c1a-a927-638c2cad0db1 | -2.69516 | -51.69008 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95171c5b-bc13-35a8-9e7d-aaebea5bad4f | -4.06412 | -48.31319 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 487a90ec-5d95-3844-a42f-6aa157c5c9f9 | -3.12759 | -50.44887 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b641adbd-181c-3e1e-a26d-3f4f99f7cdd8 | -2.62732 | -46.76698 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3d4e6abd-f7dc-3be1-a7d1-768cbc16a491 | -3.67032 | -50.26386 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d843b464-7454-329e-9098-283a0e71ae05 | -3.98453 | -46.41279 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 581cbcca-ce18-345a-ae47-7b0206be5791 | -2.3782 | -48.568 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b5b7a5a-90de-31c4-b132-a5822e373e44 | -2.3196 | -48.53743 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5251812-a0f6-328e-aa90-24f3e669219c | -2.09684 | -48.82651 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 3b78d50c-1e4e-3541-8565-00aa6c9fc096 | -2.83696 | -49.0512 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b93d1609-6501-3bf5-aba8-a6adb549414a | -2.62589 | -46.16485 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ac08730-24ec-3c60-adc6-e2c0f371addd | -0.03436 | -51.12664 | 2024-11-10 04:14:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| baa1dcb3-47c5-31f7-a676-09aa0de0b094 | -3.67741 | -44.71424 | 2024-11-10 04:14:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d633732d-adb7-3afd-9ba3-d99dfe152485 | -4.21749 | -45.44998 | 2024-11-10 04:14:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3fdc61f-a067-3bc8-8923-c2b6212b65f2 | -2.65771 | -48.48191 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3fb29cfe-85be-3f40-80d0-e78504d3b422 | -3.2962 | -52.95266 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 090e7526-c408-3bb8-94ed-7ed3003f98e2 | -2.24035 | -46.36296 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab423762-61b6-3bc7-9458-5723c781bfe6 | -2.23093 | -53.77506 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1abecc0-c952-3d8e-85de-45fbf31337cd | -5.53549 | -41.67962 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| da1af72a-3842-3a02-977f-4dd380692cc7 | -1.53119 | -52.21284 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 70212b7b-4e6f-3d95-b1da-1fdc635f793f | -2.65772 | -49.87104 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92ea18dd-1168-3c14-8d5b-e753eb08d7c8 | -3.18637 | -50.58361 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 41a7d4e4-2929-34bc-b742-46c64b7e7e2c | -2.62461 | -54.39818 | 2024-11-10 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2ac4636-8aa3-34ee-ab89-8a882a7b8d0b | -4.8514 | -48.62336 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b8836db0-7489-3984-afa6-27fd0717df9f | -3.12989 | -50.453 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d816afd6-d29a-3026-91c7-65a915359fa8 | -2.57197 | -47.3423 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdb55ccd-060a-3af3-bd6a-773c79f27b27 | -2.17397 | -48.87771 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bae7e02f-a9df-3f7e-bc7d-027b640ccf5a | -4.93908 | -45.56699 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a351f0d3-4c82-3620-8a73-35d540978a5c | -2.66318 | -49.12904 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 086b27ae-0e22-3d3f-b5aa-4c0383f0e05c | -2.46131 | -49.78566 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4f2c1a0-2a38-34c6-9454-32b6ccffaa97 | -2.46585 | -50.3974 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f3d9d0e4-c5d5-3f97-8b6c-13ddbac209e7 | -1.28678 | -53.71133 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 71ad96e5-c1fb-38bf-881f-aba64d11826b | -3.02753 | -51.52982 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a78c9fe7-f502-305f-8280-1bb181dc4ac8 | -2.90713 | -50.40144 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc7d1e05-8e22-3fe2-a539-2f9b1e0ec9c0 | -3.79517 | -47.46935 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f119e276-8877-3c13-855c-59414c4b91ba | -2.19278 | -48.3742 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README31.md)
