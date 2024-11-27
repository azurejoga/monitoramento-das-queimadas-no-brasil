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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51969650-2677-3bb8-8049-3a6cb562f75a | -3.18015 | -48.57194 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4a4ce8d-48fb-3f42-a0c7-d1c202a23f05 | -2.68666 | -45.65722 | 2024-11-27 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 28.2 |
| f6cfec71-121b-3e26-a31c-2e1de4395e27 | -4.49927 | -46.60194 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ed9ce77-e943-3157-861b-3e33929a97ed | -4.84974 | -40.75108 | 2024-11-27 04:18:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e916555c-9aba-32cd-8490-73712b78b5a5 | -3.91613 | -50.10553 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08be4abd-1d58-34c0-a478-3abae1a887a2 | -3.28584 | -50.27439 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cd76c05-b7e6-39af-a0ba-c5a1b246bc3e | -3.17054 | -48.43141 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ecd34827-4aef-3b2f-ab1e-186531019a26 | -4.25133 | -48.67834 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ad47ae8-eed1-3f49-af6a-7a7b943d86ce | -2.53431 | -47.32528 | 2024-11-27 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7498c7db-763d-3652-8388-47a4f90a7f17 | -5.03069 | -43.59861 | 2024-11-27 04:18:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99442bcc-366c-3543-8624-81167e5c0146 | -2.81596 | -46.81952 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f982b5d-455f-3ec6-a9b6-85ec87adcb31 | -4.44546 | -46.60137 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a1430e1-4f2a-3d91-a328-a2cd966ff2b8 | -0.879 | -51.72196 | 2024-11-27 04:18:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8894472-24af-3639-abae-8887d1d857bb | -3.81097 | -46.59721 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7bb8017-d8a6-34d9-83a1-5a035b04b797 | -1.68878 | -52.61085 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91d8d58f-98f4-385d-9888-9a2e175cccf9 | -3.82604 | -45.9355 | 2024-11-27 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3757d17-3b13-3899-8d0e-4e2085029a8d | -0.99243 | -51.71837 | 2024-11-27 04:18:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e478ff9-a96e-32db-ac0e-b255d9a8925d | -4.28835 | -50.22166 | 2024-11-27 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e189135a-a59f-3627-ab6d-83bf700550ff | -0.02566 | -49.63929 | 2024-11-27 04:18:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ab292a5-ba3e-334a-b571-bda356fbc564 | -2.09471 | -46.31955 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78f55ea8-51f1-3d7f-819b-c11bc1ddceb2 | -3.97095 | -48.07049 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ad8ca80-14e4-31d0-870e-bbd4d6c9882e | -2.72002 | -46.28864 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1daffa8-47ab-3378-88e6-7b0bbe9b98b7 | -2.68299 | -48.59438 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85154447-a564-3a24-b448-51211f203f6f | -3.77872 | -46.68505 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f95e322-b17b-3d4e-a09c-8626373e7e53 | -1.91258 | -50.59685 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e14d207-8dfd-3ccd-853d-ea0051da5bba | -4.49689 | -46.1069 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a6e4c401-731c-331c-95f0-fc5c1783c5e3 | -3.15798 | -49.24772 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac4b1c78-f936-357d-b7e2-e9a1a9b39097 | -3.9679 | -48.08903 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 80e7e4f3-83b7-3abb-a074-e25558dae47a | -3.10898 | -53.2734 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d93ec3d4-7510-3e03-8d46-1faac724f7b7 | -2.562 | -46.4222 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c4ddb9a-60a8-36d4-ae40-e2b7f5d3a9e4 | -3.04462 | -48.51728 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f285f47d-b634-3edc-bee6-ae5bb39538b5 | -3.09096 | -53.27582 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 733180f3-7250-315d-85ff-646c5ccd5956 | -1.27215 | -52.1684 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 180f4b3a-50a3-3509-82bc-1ae86e338231 | -2.97597 | -51.57471 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25f4d7dc-c0eb-3ec9-8112-20513d44606d | -2.81465 | -46.82775 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61d11421-0854-32f7-b377-9d8828bc03ea | -3.74426 | -40.3159 | 2024-11-27 04:18:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0111e13e-63b7-36b1-a945-ab9f54b50158 | -2.78386 | -49.20815 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a26de8e7-5808-3251-a9eb-bf1a30bca379 | -3.35954 | -50.18478 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfaf2476-b43e-35fd-91e8-7dbc35d2a574 | -2.85526 | -53.95653 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf16151a-7c57-3fcd-8f82-fdd4693cd65e | -2.80178 | -52.91245 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 104466f9-337b-3469-920d-8295a3ad4345 | -3.59467 | -50.39137 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7836898c-3a14-32ba-a198-69fdb0c2861c | -3.0927 | -53.26514 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dbc4cef-22b0-3266-97b0-5c39b6bc65d8 | -3.24152 | -46.43464 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0b064ec-8fae-3d3f-af57-18c43f74ba98 | -2.24404 | -53.63271 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49818fd6-d5c2-314f-b8f3-ea567493fd9e | -3.49689 | -53.81579 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed1f01a6-c773-3754-8c88-95b4af1bb9c2 | -3.5013 | -44.78696 | 2024-11-27 04:18:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 824cc9fd-abce-3e35-b53e-888835daeae2 | -1.28868 | -51.72864 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5a3f873-dd8f-30d5-ab46-064eaf7027b7 | -3.1068 | -53.28192 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3eebc61-0857-388b-ba47-51d33f7cc12f | -3.75414 | -51.60093 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3064662c-d5d7-3fbd-a973-295582ec38e5 | -2.93842 | -54.78661 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3cd65064-98e4-3920-8109-2cedd19e144e | -1.22642 | -51.95455 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bb7955c-11a1-3751-b977-478981669076 | -2.58405 | -46.19232 | 2024-11-27 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e687e52b-73e0-3dca-8166-ce867fc61077 | -4.23558 | -50.02098 | 2024-11-27 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71a6efa9-adce-3c3b-87ff-9581ee351cfe | -4.09582 | -48.92247 | 2024-11-27 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e0b0eed-9852-3353-bb75-e216ddd7278b | -3.96041 | -46.90054 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa35bcb7-25df-31b7-bdae-9bae4ef42a59 | -2.64158 | -51.61405 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cf4831a-6622-34e0-9c34-8765e820a52b | -4.34615 | -45.87201 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f4f68ab-2456-3de6-b41a-a87ed385a479 | -2.55326 | -46.40864 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 278d3b02-cc84-3f35-a94c-6f3c1f98cc16 | -3.24541 | -50.14175 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4dc16e5-30ec-3ac5-aef5-d794779e2acb | -1.19087 | -51.76602 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca0337d2-f958-34bf-93fb-a83da4a28e77 | -3.24215 | -46.43076 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac77369b-f30d-35ae-af11-d07f4baedff3 | -1.7838 | -52.73456 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c201ac4-2385-377d-9103-2ef146a030fa | -2.10328 | -46.5637 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef2547c7-c458-35c6-a7a1-6d57cfa0a9f8 | -4.3086 | -48.17931 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06d408d1-5003-3501-98a4-03f9a0d79c40 | -2.90145 | -54.17733 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc3b59be-f783-36e6-a544-b55b53a34799 | -3.58797 | -50.37682 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81bc97fa-e5a1-3ed7-8ba2-e4525ec1af24 | -3.19754 | -48.59037 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3643400-f34f-3d2b-b340-2853b418764c | -2.82145 | -51.79307 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b480dcd2-a0e2-30e5-b030-59d04b4b6ca8 | -1.94267 | -45.72707 | 2024-11-27 04:18:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5b985d12-977f-31d2-be1e-7266584b3a60 | -3.7186 | -50.18766 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e212319-fbc0-30ff-95da-fdc44526d449 | -3.83334 | -46.08992 | 2024-11-27 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 343b5d66-2f24-3b64-84d9-1b5a3a282f05 | -3.76871 | -46.67954 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d305625-f2c1-33f0-9a6d-fd1e7c81271b | -3.65707 | -50.23384 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e00d8125-11fb-33a8-aaf1-25ffc848adfd | -3.80389 | -46.59625 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16c78075-30cc-34fe-8ea2-2821dc38ad25 | -0.24951 | -48.65105 | 2024-11-27 04:18:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 160eaa96-1c58-3611-b859-1d252e2b9cd0 | -1.78267 | -52.74131 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85b9956e-039e-38d3-97a1-06c3f1b91d20 | -4.49346 | -46.10634 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7b7ad9bb-3a27-3938-baf4-1759c1b99129 | -3.49779 | -50.46188 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de8097cb-f7c2-30eb-9c8e-8b81153c8f0e | -3.96562 | -48.07917 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 96cbf5b6-bae6-3aeb-be3d-16c43c81999c | -2.54682 | -46.40353 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 509c955e-a995-3321-a4fa-ca25b16f8dcc | -3.10592 | -53.25843 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 989c0cb1-0d23-3f7a-ab05-9f6a3150146f | -4.05011 | -46.85585 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ed25720-3010-30c0-a613-e4cf865a0654 | -3.86462 | -40.44341 | 2024-11-27 04:18:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 58307a41-4fac-3750-836a-c6c13794cb7b | -2.82252 | -46.82476 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c68b012b-fd87-312e-9e44-27dae579a615 | -3.84295 | -46.51009 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b186347b-c7cb-322c-a07f-8e2c657b8f97 | -3.09663 | -50.36383 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aebe607f-182b-3da7-b7b7-ebbb6af65ff8 | -3.38133 | -50.10584 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d564318e-375c-31b4-9ada-b17338220097 | -1.68932 | -52.60752 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd79e137-2225-300c-bdd5-7425e3952b56 | -3.26227 | -46.41795 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e86fc41-7148-35b1-a5a5-8ab99d27f1d4 | -3.67521 | -53.68901 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcc8fc50-d6f7-32e4-ad2e-1237fb4fa0f1 | -3.65466 | -49.95174 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6478d9c-0fa0-3d71-a24e-342e814e52b3 | -3.17366 | -48.43701 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 0c84629e-7e9a-32f5-9b27-a0fee700fc83 | -3.08493 | -53.27838 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc348ec5-2f8f-3e2e-b0a0-9567d1be8e7b | -2.55846 | -46.42165 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2757e17-43f3-36eb-9637-7db658ce424f | -4.14584 | -43.80602 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a66ee9de-96b3-3bf8-8b66-a3b98eb5ba1c | -3.11869 | -53.10619 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d436d6b-fc6b-3c26-8dff-a9f998e4def9 | -3.10421 | -53.26335 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e388b0a1-2b39-32e1-98b0-e6cb1f3f85b1 | -3.09805 | -53.2717 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d4c22e6-76d9-32db-884e-4e47f5c84012 | -3.11812 | -53.10967 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a37c0310-f927-3405-bd74-b48af25529d2 | -3.57844 | -41.9625 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README44.md)
