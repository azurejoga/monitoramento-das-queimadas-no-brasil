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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c618b48-4005-3759-bca6-249c483ec806 | -13.1918 | -48.638 | 2024-10-03 01:04:03 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0aa84bf1-905b-3755-a4fd-479c01facf28 | -13.1937 | -48.646 | 2024-10-03 01:04:03 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| deaced95-fd3a-3971-b51e-1d2a7c1dceaf | -13.7096 | -50.870701 | 2024-10-03 01:04:03 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de41c02c-7805-33be-94e6-4ff634dbcf9c | -13.3192 | -49.311001 | 2024-10-03 01:04:04 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0643b189-67d9-367f-b3f1-c3b8ab9c2f24 | -13.321 | -49.3186 | 2024-10-03 01:04:04 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e5aa3b7a-75c5-358d-b998-5d1bcb3be378 | -10.603 | -48.053398 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8734037d-2eb4-3f92-bd88-9e58bdfd2aab | -10.5933 | -48.055801 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0701c8f3-6a48-37a1-89e0-6056ac717ed8 | -10.5955 | -48.0648 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e741b234-8984-34e1-9ff3-995d7a9b9392 | -10.5976 | -48.073799 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61e349fc-4997-3071-ba21-e86005c2acff | -10.5998 | -48.082699 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3db90edc-a44c-3ad8-b397-2755a6ac8b50 | -10.602 | -48.091702 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f657c14-94fa-3351-a2f5-643daede88f6 | -10.5727 | -48.013 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38ff00fd-1616-35a1-bfa5-7e4b56c7d3a4 | -10.5878 | -48.076199 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06d04a2c-aa6b-337b-bce8-e182fd4e5ab8 | -10.59 | -48.085098 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3875d0c4-c385-3f32-b157-27f9b5fdae6d | -10.5608 | -48.006302 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19af6bb5-8da6-3e91-ab7f-dd5b46f7d37b | -10.563 | -48.0154 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49271ea2-7220-33d3-b4ff-12481fdf2fae | -10.5651 | -48.024399 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0feb40d-6824-32a1-abb1-83abb363d64a | -10.5738 | -48.0606 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11bc3743-61c9-37de-ba8a-dbad90f3ed00 | -10.576 | -48.069599 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05b88ed3-7eed-344c-a767-27d21ffee65a | -10.5781 | -48.078602 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd2e3522-ef7f-3f7a-958b-8c8ca1d33342 | -10.551 | -48.008598 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab58aa65-38c1-3a14-8fbb-c6ccef8807f0 | -10.5532 | -48.0177 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed4430f4-e9ac-364e-8cc3-36d772a7732c | -10.5662 | -48.071899 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35ac6be7-292f-35ea-99d9-018eba1e801d | -10.5683 | -48.080898 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddf51b0d-2576-3bcf-b25d-7dc364154fb1 | -10.5434 | -48.0201 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8687dc68-2eb0-3b69-9201-7164a68c6d93 | -10.5585 | -48.083302 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 941e681a-2b23-3322-bbdf-2aef56399983 | -10.5607 | -48.092201 | 2024-10-03 01:04:04 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7d1b625-7155-3f09-8881-134c8d388362 | -10.7017 | -48.724998 | 2024-10-03 01:04:05 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e491e5e6-f360-30e3-824e-a3498d6a24c4 | -11.2258 | -51.146198 | 2024-10-03 01:04:05 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cba90abe-a2c4-3dc9-8ad2-49a40de10daa | -11.2275 | -51.153301 | 2024-10-03 01:04:05 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99d83f9e-9061-3467-9649-0cd5e0fa770e | -11.2291 | -51.160198 | 2024-10-03 01:04:05 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5596beef-924c-3a48-a09b-00059e7b7880 | -10.4207 | -48.154701 | 2024-10-03 01:04:07 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f89163c4-8635-3015-a964-330e4dd80a84 | -10.4229 | -48.163601 | 2024-10-03 01:04:07 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb405aac-51af-3bac-99a7-bab0dbb368bd | -10.2421 | -47.6702 | 2024-10-03 01:04:08 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c945cf2-2b1d-3d25-9b65-e085f79a6bbe | -10.2444 | -47.679699 | 2024-10-03 01:04:08 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a6a775a-84a2-35ca-abc8-298a43547148 | -11.8147 | -47.592201 | 2024-10-03 01:04:22 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9389d621-fcd9-3ae5-a22e-f27caaf2cdeb | -11.7982 | -47.566898 | 2024-10-03 01:04:22 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd677f2b-414e-3556-86e9-1791af0b425b | -11.8004 | -47.576099 | 2024-10-03 01:04:22 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0181c5ea-e501-3a2c-b156-16664ea991eb | -10.9786 | -46.5378 | 2024-10-03 01:04:31 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c509c4e4-9971-369d-a65e-db89af312d85 | -10.9812 | -46.548698 | 2024-10-03 01:04:31 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b095147a-9135-3c64-9a2b-a51338cdb9d2 | -13.7197 | -60.662701 | 2024-10-03 01:04:36 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 407a8e66-b3a1-399f-b53a-7fb767014e5c | -10.713 | -47.6954 | 2024-10-03 01:04:40 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f534ad15-de22-34e9-a700-159e965c8543 | -10.7153 | -47.7048 | 2024-10-03 01:04:40 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c270fb7-e40f-3bea-a4f9-e93b2d6b68ed | -10.7407 | -47.981602 | 2024-10-03 01:04:40 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a01ee378-b799-3a63-87e8-da2a3b6f0556 | -10.7429 | -47.9907 | 2024-10-03 01:04:40 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e3ea077-9f16-3bef-ae89-00dc11479b2f | -11.1148 | -49.598999 | 2024-10-03 01:04:41 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1cb9909-7af9-30f6-bafe-ac23fccf0cce | -11.1166 | -49.606602 | 2024-10-03 01:04:41 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9e26670-33ba-35a9-9f5b-86766b885607 | -11.1068 | -49.608898 | 2024-10-03 01:04:41 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac8f8fc7-c043-32dd-9ad6-2c9ab2745b4e | -11.1085 | -49.616501 | 2024-10-03 01:04:41 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 076b7abe-514c-3e17-b773-fc818d3edc47 | -11.0934 | -49.596001 | 2024-10-03 01:04:41 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07b1d441-3db4-3aa5-bca6-a2da041de1a6 | -11.0952 | -49.6036 | 2024-10-03 01:04:41 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc9ffdac-9051-3ed0-9e9d-69491e872358 | -11.097 | -49.611198 | 2024-10-03 01:04:41 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bce0b6e2-6a82-331b-89bb-cdf817f5de7a | -12.6165 | -56.478699 | 2024-10-03 01:04:41 | METOP-C | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a0695139-295f-36c1-80f9-e399ecc5e773 | -11.0818 | -49.590801 | 2024-10-03 01:04:41 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce30f4fa-6c21-36e1-89de-96970755677d | -11.0836 | -49.5984 | 2024-10-03 01:04:41 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f885de8-17c3-3a0b-bc58-d303fa7c6c20 | -11.0854 | -49.605999 | 2024-10-03 01:04:41 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9840fafa-877b-3917-a382-a1208c347246 | -11.0872 | -49.613602 | 2024-10-03 01:04:41 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| beb9b880-874c-3a14-80b2-08061a7076cb | -12.6068 | -56.480701 | 2024-10-03 01:04:41 | METOP-C | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af5fb9cc-527f-3393-9e06-320786fc527c | -12.6091 | -56.491402 | 2024-10-03 01:04:41 | METOP-C | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f33b616a-1ba8-3d7a-a7c3-360593dbedcb | -7.8533 | -46.256302 | 2024-10-03 01:04:41 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca571f3e-1f26-3650-8b92-0931ed888e9f | -9.1042 | -51.517799 | 2024-10-03 01:04:41 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baddd59b-8047-3fd2-b76a-12cc0419ddb2 | -9.1058 | -51.524799 | 2024-10-03 01:04:41 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e6fb1fe-9a12-3da9-a54d-6a41384835a6 | -11.0959 | -50.716 | 2024-10-03 01:04:45 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5acd432a-b790-395d-a461-3a3f5f640101 | -11.0976 | -50.723099 | 2024-10-03 01:04:45 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f5c863f-ec29-3fed-a599-265b9440c7a1 | -11.0861 | -50.7183 | 2024-10-03 01:04:45 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2aa498d0-1e39-3824-ba0a-02019f675945 | -11.0878 | -50.725399 | 2024-10-03 01:04:45 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0ccf282-a58d-3bd6-b21e-33e5189d8e2e | -10.4662 | -48.172001 | 2024-10-03 01:04:46 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef692d53-7dae-3e64-a6e1-be6a2c138d86 | -10.4683 | -48.180901 | 2024-10-03 01:04:46 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5d36f0-3eac-3cd3-844c-a0b2c3c5004f | -10.4704 | -48.1898 | 2024-10-03 01:04:46 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 612ef67e-6671-3744-989d-12cb2d23fa54 | -10.4564 | -48.1744 | 2024-10-03 01:04:46 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8f54a71-9dc7-365b-b61d-1a69df313e01 | -10.4585 | -48.1833 | 2024-10-03 01:04:46 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d160318e-71c1-34f8-8348-541780c6b6d8 | -11.084 | -52.520802 | 2024-10-03 01:04:52 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd1bc13-0fd2-3c56-bdd7-408f5ed015d9 | -11.0856 | -52.527901 | 2024-10-03 01:04:52 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f567215-167a-3680-9fae-73b1c4463f54 | -11.0742 | -52.522999 | 2024-10-03 01:04:52 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f704ffc2-2a80-3f52-9973-5030da879b05 | -11.0758 | -52.530102 | 2024-10-03 01:04:52 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80d17c29-18e0-3979-9e41-6e862de18085 | -11.0628 | -52.5182 | 2024-10-03 01:04:52 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07b4e7ef-5e78-39e7-9575-7b10a183bf4f | -11.0644 | -52.5252 | 2024-10-03 01:04:52 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4340eb6c-1ad8-3343-af20-95a4dba5b58c | -11.0483 | -52.499401 | 2024-10-03 01:04:52 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecfd748f-6cd1-320c-9e70-430829602347 | -11.0499 | -52.506401 | 2024-10-03 01:04:52 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf803bba-25e3-39d9-9983-74717e0d93e5 | -11.0369 | -52.494598 | 2024-10-03 01:04:53 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da7c3e7e-7f1c-35e5-b9ba-ecf0a8524709 | -11.438 | -54.307201 | 2024-10-03 01:04:53 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac7de28-9674-3dfe-9887-43797da76514 | -11.4265 | -54.301399 | 2024-10-03 01:04:53 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6521e341-cc14-3cf8-be9a-58e93fdfcdea | -11.4282 | -54.309299 | 2024-10-03 01:04:53 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50ed873a-fcfd-30f7-9dde-9eecad3b4534 | -11.4299 | -54.317299 | 2024-10-03 01:04:53 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bed42f22-7780-318f-85e6-5ca7a87125b2 | -9.8907 | -47.755901 | 2024-10-03 01:04:53 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d775153-6737-3e9b-8e15-9660406c7ccc | -9.893 | -47.7654 | 2024-10-03 01:04:53 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdd078e3-2ecc-3986-bf5d-6100540b8ca8 | -11.9885 | -57.188099 | 2024-10-03 01:04:54 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f473312-b490-3260-8b8d-2f56360bdbbf | -11.9909 | -57.1996 | 2024-10-03 01:04:54 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd934454-e678-3a36-967a-34ad0a857f32 | -11.9787 | -57.190102 | 2024-10-03 01:04:54 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8d14f11-3e15-3596-91be-4554e64b4b4d | -11.9811 | -57.201698 | 2024-10-03 01:04:54 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed801dba-d169-3924-836f-47c0f381ba94 | -10.904 | -52.406898 | 2024-10-03 01:04:54 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4b44e14-3525-39c7-8688-10356b8a8e5c | -10.9056 | -52.413898 | 2024-10-03 01:04:54 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6569b144-667e-3870-b6b7-ce2c8a4ac296 | -10.9072 | -52.420898 | 2024-10-03 01:04:54 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1eaf5509-deba-38fa-a586-bddb9f80cadf | -10.9087 | -52.427898 | 2024-10-03 01:04:54 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d7e0023-e8fa-3875-9cb5-41c05313b307 | -10.8942 | -52.409199 | 2024-10-03 01:04:55 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff9be94f-2177-3201-93d4-9a95e5a015b7 | -10.8958 | -52.416199 | 2024-10-03 01:04:55 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37184899-9a28-3375-bd3e-06764ab946ad | -10.8974 | -52.423199 | 2024-10-03 01:04:55 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9747f7f8-2388-38e9-8859-3f9c2515e198 | -10.8989 | -52.430199 | 2024-10-03 01:04:55 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7a24bbc-718e-3c21-9298-a8dbb87a0476 | -12.9849 | -62.630798 | 2024-10-03 01:04:55 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d6ef91e-7c74-3688-9144-724e6383e725 | -10.5411 | -50.949699 | 2024-10-03 01:04:55 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README29.md)
