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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a306811-edb5-3576-83be-6c8b4da90bdc | -4.38822 | -49.75655 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6c495c27-6224-3cec-ac4e-dfa385a171f0 | -4.38748 | -49.76116 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d30b7c19-59eb-308e-abb6-b1438faa9a73 | -4.38519 | -49.75139 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e15c1e7e-b8c4-35e0-a991-6227a85b9e98 | -4.38446 | -49.75594 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23c725aa-462d-35b1-844b-d85aa6c9b915 | -4.38373 | -49.76054 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08a4c832-2714-32d2-8562-a8e1a26e58d1 | -4.3807 | -49.75533 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 822a65f3-df46-374e-b41c-b203034991ef | -3.78457 | -49.48146 | 2024-10-27 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93395597-ea8e-37db-8b79-bc08f41d819a | -3.78085 | -49.48084 | 2024-10-27 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aecf3745-64cc-3eaa-841f-ae8991a668bd | -4.40037 | -49.77722 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74d03fff-6444-333a-bbfc-8b6e3b458c56 | -4.39735 | -49.77446 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50cd1c97-2251-3247-ab4b-f5328c80bae5 | -4.39208 | -49.75963 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bd27e80-9a3d-3fae-bdda-9f7c2e833b38 | -4.38143 | -49.75078 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfb8f2e3-47cd-3283-bc1b-e65169d5e6da | -5.06281 | -49.61127 | 2024-10-27 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0bd3b34d-16f4-3e54-b38d-eed1f086e35f | -4.99178 | -49.76805 | 2024-10-27 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d126e8c-df0d-3a95-a144-6789ba07c4db | -4.97539 | -49.77461 | 2024-10-27 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9aafc128-f9c4-3674-b634-fbd235278d40 | -4.97165 | -49.77402 | 2024-10-27 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 587089df-ce65-3c67-a0dd-580166a34b34 | -4.78002 | -49.87675 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c71d93ae-2cb0-3c14-9f22-7a668d9657b4 | -4.6305 | -49.5987 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9131a371-6f0b-3580-8393-3d014af8ab96 | -4.62607 | -49.60261 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 850dfadb-86a5-31d1-b49e-45ccce087a22 | -6.40877 | -50.79242 | 2024-10-27 04:23:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4425d8be-54e1-3c85-9158-70abefb60c7f | -6.40457 | -50.78967 | 2024-10-27 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3250402-53df-349e-82ae-123c613c3a84 | -6.40376 | -50.7947 | 2024-10-27 04:23:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32a6bf94-e0c2-362b-9869-68f018b761d7 | -6.20569 | -50.85097 | 2024-10-27 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a08a6ef1-742a-3763-a45a-76febc8867fd | -6.19705 | -50.85453 | 2024-10-27 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47dd682b-3ffb-3515-93df-c96ff63d2e39 | -6.19395 | -50.84899 | 2024-10-27 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5abc3358-1ee5-3d1e-b412-9da1ec86df8a | -6.18528 | -50.85273 | 2024-10-27 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d643197-331b-37d8-a1ff-8e40a8d464fa | -6.04343 | -51.14748 | 2024-10-27 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5abbb670-7112-340c-b4ce-b05770b3f83a | -6.40765 | -50.79538 | 2024-10-27 04:23:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f26d9cfd-e5b7-3001-9607-d188f83f9237 | -6.40488 | -50.7918 | 2024-10-27 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb306e9b-9224-3f59-88ce-2087ca4f8329 | -6.19787 | -50.84962 | 2024-10-27 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 098bbcc1-cec9-3bea-a6d8-d338e4aaa387 | -6.19003 | -50.84839 | 2024-10-27 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8e9d45d-e6a3-3669-b683-b9c65ff35f47 | -6.16676 | -50.8908 | 2024-10-27 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f944714a-ae00-3b39-b0e3-4b240444fa3b | -5.67822 | -50.00875 | 2024-10-27 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cae6728-82b9-32ba-a73d-cc8c26bd7c66 | -5.67448 | -50.00808 | 2024-10-27 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8858caa6-b4f5-3ec1-a900-9934ece97347 | -5.24634 | -50.69406 | 2024-10-27 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fccea42-f98f-3a11-8280-64268c51ce17 | -5.14731 | -50.75803 | 2024-10-27 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fe83637-ac1a-3db2-8c10-68b1d121fc36 | -5.8201 | -49.9013 | 2024-10-27 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 335d186c-effe-3449-9388-6b40bb3ddcae | -5.33939 | -50.95897 | 2024-10-27 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 355ccfe8-e238-311d-b478-8a15eafd92de | -5.23415 | -50.27859 | 2024-10-27 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f80f1ac4-94e0-31ef-916c-46e2d635cfa4 | -1.58022 | -50.45039 | 2024-10-27 04:23:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70341779-f6a0-35ea-aae5-4022b063b067 | -2.2037 | -50.82486 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f535220-4699-3dd7-b8b7-cb0ea031f965 | -2.6003 | -51.77267 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 328891cf-f150-311c-a265-1e04a629ddaf | -2.5996 | -51.77698 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee95fe3c-fd7f-33ae-b27e-4763c91afc13 | -2.5989 | -51.78127 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5ebd9d9-30e9-3e31-8778-7015b02bb9e0 | -2.55332 | -51.23427 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76dc7c35-ae15-309f-82e7-d9f01d6c87b2 | -2.54838 | -51.18486 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 63596a9b-09bb-3e33-977e-e463c784ec12 | -2.54773 | -51.18879 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eff3287-4af0-3e72-aedd-02756a764613 | -2.54422 | -51.18466 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 69aba377-1d05-363c-affc-9eebeb900414 | -2.54415 | -51.18419 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ff34f801-3ef6-3343-9f6a-aebc66d28b21 | -2.5436 | -51.18858 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2226bf1f-29f5-3747-b696-ac1c42713c20 | -2.5435 | -51.1881 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5d3dae0-d2d0-3474-9b86-56004f45fe04 | -2.54298 | -51.19251 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91906a2a-9366-3ac6-bb9a-8b5e3be372a8 | -2.54286 | -51.19202 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 344f1fda-6555-31cf-9905-f7fdf8ed5a47 | -2.54237 | -51.19645 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0a7dbfb-8de3-38b8-b325-5ccfc4d42b68 | -2.54221 | -51.19594 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac10fd41-2077-375e-9ff5-68ef97b7fef8 | -2.53999 | -51.18397 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b8a83ae6-aaa8-387e-8aca-25669760669d | -2.53992 | -51.1835 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 77aee363-b976-3fee-8575-9e41038c2ee8 | -2.53937 | -51.18788 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ecb8977-faae-3cbc-932b-03b7a1687a13 | -2.53928 | -51.1874 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 68176f76-bde2-3625-8e13-c3162da6b034 | -2.53875 | -51.19182 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74c5a780-5436-3eab-875b-00b54e3ba346 | -2.53863 | -51.19133 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 165c8250-9d52-32dd-a1f5-47e92d2c43ea | -2.53813 | -51.19577 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8afa4182-a389-35a7-90df-0f111aa64fda | -2.53797 | -51.19527 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a16139c-a14f-369b-83fa-062415c743b8 | -2.53751 | -51.19971 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b24083a2-4498-3a3e-a98b-3a82d07682f3 | -2.53732 | -51.19921 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 016ec077-5027-30d0-a71e-6f86c7e5c0e5 | -2.53576 | -51.18328 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| aa7d473b-1c08-3bfd-afc0-e0cbcfcbc334 | -2.53569 | -51.18283 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 4e137b25-f215-312e-88f6-4e81c329e5ac | -2.53514 | -51.18719 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 95854d3c-e0e5-32c6-9096-4844e3fd1f32 | -2.53504 | -51.18672 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 84c75ae8-ef7d-3581-b88e-1bd41d672d57 | -2.53452 | -51.19113 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f255d3a8-5b56-3cb3-a368-801e1a3e5019 | -2.53439 | -51.19065 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c85d36bd-7c7f-3aaa-a711-a9756e46d7b9 | -2.53389 | -51.19508 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb33edf5-92cf-355c-9cea-684ced66b218 | -2.53374 | -51.19459 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48213b35-47a5-3e6e-b8cc-e2e92596b3c4 | -2.53327 | -51.19904 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 951ba9e2-cd90-36eb-a5c7-c13f9064fd8b | -2.53309 | -51.19854 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae8e16a2-fd2f-3a16-8553-6c96c590c91c | -2.53152 | -51.18261 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| fef547c5-243a-3c21-ae19-590c7914f657 | -2.5309 | -51.18651 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9d65d780-06a2-3465-ab6f-52b96c342b11 | -2.53028 | -51.19045 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 2b52bf20-2854-3bcd-8731-bd5dcfe8672d | -2.52966 | -51.1944 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be2b036d-57e6-3e53-8c8c-4651b34afe08 | -2.52903 | -51.19836 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ec109f0-4eda-30f8-a41e-86ea0f25cc1b | -2.52667 | -51.18584 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c06289a-0a46-3ecb-9769-c05affbf59b1 | -2.52605 | -51.18977 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66910f47-c253-3f8c-a436-184320d34af7 | -2.52542 | -51.19371 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01d52f3b-a0b5-3c0c-b9a4-cd6457c6bf26 | -2.52243 | -51.18517 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 003e5190-d70c-3498-a50b-6d248df1e871 | -2.52181 | -51.18908 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3adc4982-17a2-398f-a692-f2f96a1fd4ca | -2.40583 | -51.18363 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16e2ff5b-a01c-341b-9d9b-1e4fb47e8c42 | -2.4052 | -51.18758 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 079ace05-7e78-3eec-b33e-527e5d55bcbe | -2.29822 | -51.28946 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cce57580-bc8a-3c3e-9be4-1bb5eed6a881 | -2.27513 | -51.2691 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d675ac8-ffa5-3114-a063-6eacb3114c85 | -2.26488 | -51.25101 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6310b6df-1f99-35a4-bea1-3a3ccacf77c2 | -2.26424 | -51.255 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83255e30-9463-3fe8-a81d-3571f9747cba | -2.54967 | -51.17702 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03534360-fb46-31e7-b424-bcf28cb058ff | -2.54903 | -51.18094 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 504a5e20-473b-3cf4-bf33-0b71827b46a3 | -2.54673 | -51.16853 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91280a78-6d14-39d1-9e6f-3c463cfc9097 | -2.54609 | -51.17244 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e35ff463-760f-3d96-841b-0932f774b9f8 | -2.54607 | -51.17288 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 862b278b-45b7-31a1-945a-00b41ecd85e7 | -2.54545 | -51.17681 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 412ab8fa-6871-346c-b573-3d91e6208720 | -2.54544 | -51.17635 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dec246eb-9326-354d-8998-ef5dd55d1b45 | -2.54483 | -51.18074 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b1f6eefc-5c79-3d38-a153-74e1aa3638ca | -2.5448 | -51.18027 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README50.md)
