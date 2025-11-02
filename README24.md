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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd23a05a-a5e0-3c07-ada2-14abec604918 | -1.4971 | -53.12356 | 2025-11-02 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9d95a299-6be6-3588-baca-2285bb039822 | -3.58095 | -51.55958 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb647ba8-0b2b-345a-b7cf-63c8022fb247 | -3.14511 | -49.42503 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eef33399-94af-3c1a-93f5-84155366c028 | -3.40675 | -51.66295 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5460df6-f21f-3239-87f0-a11eefb13107 | -3.02352 | -51.22859 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1ab5303-72a2-32a4-b37a-d0a4b3bf60e4 | -3.28328 | -51.54723 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a775a52a-01ce-387d-94bf-06bf4027255d | -3.46325 | -50.22427 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70c8abfa-87e0-3d68-a00c-502b33ef21f4 | -3.14245 | -49.42189 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bc942b4-e900-3876-ae7d-7e07afcb265f | -3.2208 | -50.58258 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acff7a84-588e-32b9-a52e-5122590916cc | -3.55504 | -50.15741 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40308b1b-5130-3f42-ae17-818687f6f37d | -3.65141 | -50.70898 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 805512db-66bf-3bb7-b671-8e652983cc1a | -3.12742 | -49.23816 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4111af6-21cd-3a56-a1eb-12ec8554eccc | -2.8695 | -51.39424 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aca81ed-4111-3564-95c8-b1623ab33b8f | 3.28527 | -61.1516 | 2025-11-02 05:08:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ceb8f92e-55bd-3bfc-8eab-e8e8285cacc4 | -0.68728 | -52.3735 | 2025-11-02 05:08:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e45cf11f-0c95-312b-b89e-be7816d4aa1f | -3.4161 | -49.99865 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78de3bc1-78fb-3165-8273-773cb8228a48 | -3.24458 | -50.79919 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74804dbd-c34a-3d7b-b7c2-b835065da162 | -3.45881 | -50.2237 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52519106-fbb0-3de3-bc21-efc9d125a2fe | -2.70575 | -54.65553 | 2025-11-02 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a66b61a0-b1ef-3fb1-bcd4-6fd7539ff3fc | -3.45971 | -50.22166 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb1a9a98-84d0-338d-aa9d-9228ab2fb326 | -3.72164 | -45.54965 | 2025-11-02 05:08:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 736f7bdb-b521-3abb-b101-ed81395cdb4b | -3.5695 | -50.26495 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8812dd1d-cc47-3b88-bc0d-7274137532f3 | -3.08196 | -51.25262 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54419804-5f58-3a39-acc4-024639721117 | -3.83517 | -51.31522 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e995b3d-e86e-3c65-b66c-38759cbe02b5 | -2.93617 | -54.16964 | 2025-11-02 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81e1236e-0e82-343a-83bf-1bd963200ade | -2.44758 | -49.03543 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a902a32d-7c4b-3b6d-8415-aa11f882db9f | -3.92825 | -49.9625 | 2025-11-02 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8941e3e-2464-3a13-b830-f9a2281b49c3 | -3.95078 | -49.99855 | 2025-11-02 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11963acc-e6db-3243-81cf-e339465ac3b0 | -3.2458 | -50.79131 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb905cc5-bc49-33a7-8e40-1e7140ea76b6 | -3.07871 | -51.25204 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a34d7c2-0f5e-3288-9013-00ea137dc7f2 | -1.42221 | -55.24015 | 2025-11-02 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2bf19e4-2e34-370f-89d2-fa84d2eb9034 | -3.32095 | -51.57092 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46a6bdfc-2e30-3cc7-aa36-9537c9a91585 | -3.44101 | -51.6539 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bd5a44c-1674-3085-abe8-a0678de2cf50 | -2.9872 | -48.7085 | 2025-11-02 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 413f7e14-2370-36db-a758-32464df9ece3 | -2.31494 | -48.58649 | 2025-11-02 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 976676b6-ef20-35bc-a584-feda2bfe1d73 | -3.5679 | -51.641 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93de5bfd-ca01-31a9-a73e-bcb2069e69b4 | -3.24034 | -50.79857 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6ec34629-99b7-35f9-b99e-46c7302bf0b7 | -2.88803 | -54.85812 | 2025-11-02 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7cd67ef9-e426-3a5c-b17a-54c22634e92d | -3.29373 | -52.95693 | 2025-11-02 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81bfecc8-5721-377a-87e6-8d4f6e278ff2 | -2.90458 | -53.95933 | 2025-11-02 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db12ed2a-8c3d-3054-8d9c-1a5a7cd28dd9 | -2.37379 | -47.71995 | 2025-11-02 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb05cddb-923c-3359-9805-ffb15328d837 | -3.52092 | -50.32121 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 046dd82b-ef77-3052-af7f-4d29c4874cdb | -3.24155 | -50.79066 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5df16545-8a1b-3273-b61c-b6442be10934 | -0.68797 | -52.36909 | 2025-11-02 05:08:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecc562bc-779c-36ed-b5db-cd555b6e2b99 | -3.02124 | -49.44749 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3eec771-ece7-36c0-a786-162bcdc31d35 | -1.42331 | -55.23318 | 2025-11-02 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4779e58-e325-3d61-8812-02f547397e09 | -3.45945 | -50.21935 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf1eb33f-6aaa-343b-9dd0-9f37aeb3d85e | -3.42907 | -45.91434 | 2025-11-02 05:08:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 657d8944-f76e-32a2-8322-2ae0a7eebed9 | -3.56483 | -51.64042 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c43fba6-8db5-3138-9774-1eb6b39c590e | -3.56735 | -51.6445 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df5880ff-752f-3983-9c0e-5323a1178581 | -3.32957 | -52.82242 | 2025-11-02 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2144f029-2ee6-3f62-9086-8c314d87dfcc | -2.10949 | -52.77704 | 2025-11-02 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 786db091-3be5-3d32-8fc6-7b8666f4dbd3 | -2.92995 | -54.02689 | 2025-11-02 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 206ca189-c205-399b-93f6-84fddb02927c | -3.6574 | -50.19323 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25c4815b-6859-3671-882e-6e5e02d76045 | -4.17982 | -47.65586 | 2025-11-02 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23d866c4-a06a-38c1-8382-242dee2de785 | -3.42541 | -50.23869 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e20292ed-41ee-3d65-a288-18c1568b7b9d | -3.65939 | -50.71427 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd724c43-0e32-3622-87df-ba927a66b9fa | -3.58057 | -51.55974 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06082121-cad0-3447-8e4d-e738974db5f8 | -3.07575 | -51.24412 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23324965-16e8-3488-88a3-04ab12d90551 | -1.49462 | -55.34061 | 2025-11-02 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65f8aa62-5dbd-3370-a00c-6badc2ea5907 | -3.91109 | -50.03633 | 2025-11-02 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9558d70-4029-3777-b3eb-9807f584f49b | -3.02198 | -49.44268 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d199cccd-1551-3746-ba03-500cafe70a90 | -3.28072 | -51.61871 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d670318-a9ff-3360-b924-3bd43d9a01b4 | -3.56886 | -50.26931 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31355763-ebd9-3ba8-98dc-901e00461653 | -3.41543 | -50.00311 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 067ca0f3-018d-3654-bb7f-7719fffff0ad | -3.45528 | -50.22104 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f6490ac2-5d30-3ac0-a0a2-b470ecaa130a | 3.28589 | -61.1557 | 2025-11-02 05:08:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a38ab1b5-3040-37b9-a235-84bbd24e2091 | -3.22449 | -50.5873 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb12abf9-d715-3b5e-8cba-cc7d52c530e6 | -3.27522 | -53.2721 | 2025-11-02 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8572d00b-c48b-3032-a0a3-65718c52a6fa | -3.28474 | -51.61934 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2ce1d19-8cab-3935-9571-4a6822123bc1 | -3.42916 | -50.2437 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5be65739-4bc9-3a38-806c-0f9237f2b757 | -3.59978 | -50.6269 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6f54ae0-13f9-34d3-bf80-f6760336fffb | -3.56886 | -51.641 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0571b69-5480-3d0d-8b90-b7e953c98e99 | -3.42379 | -45.90914 | 2025-11-02 05:08:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3fa99bd8-1542-3477-b27f-8f493acb54a8 | -1.41943 | -55.23616 | 2025-11-02 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c7cce0b-f558-3000-809e-a0933a85c2a2 | -3.6004 | -50.62283 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 732bf5f6-3f56-3f0c-b3b8-a79b17811533 | -3.72094 | -45.55428 | 2025-11-02 05:08:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| abf4de51-4669-39d5-84fd-16a121b93062 | -3.51821 | -49.72268 | 2025-11-02 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac8412fb-8905-3289-87a3-27f2d27d3bf1 | -3.83255 | -50.48959 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2d21163-1227-3a10-b116-9953fa2a61bb | -1.81824 | -55.16485 | 2025-11-02 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2f4a8e3-36ac-3c29-a25e-f07566f8f1e6 | -3.37766 | -49.97885 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2afbd597-8493-32e3-ae1f-d883c229dba7 | -3.06993 | -51.25454 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8161638e-f255-302f-84df-bf300b7a3151 | -1.27712 | -52.93146 | 2025-11-02 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c4ce089-153e-3b9f-a550-369d9c7261b8 | -3.65571 | -50.70959 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ba45c92-4b24-38d6-99e0-ee513f3a33a4 | -3.50142 | -50.47795 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91ab9326-82d0-34b7-940b-67ab77c20f69 | -3.67463 | -51.3254 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 709ee1a3-90f3-3176-97e5-26159d867ff4 | -3.45501 | -50.21873 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93d0b042-75ce-3208-a47d-ef08d065fbaf | -3.29142 | -50.20243 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 886314b1-8606-3a15-91d6-fcc15865ee97 | -3.58964 | -47.51861 | 2025-11-02 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1ad8829-4729-325b-bdc1-5c65292068f2 | -2.87514 | -53.97983 | 2025-11-02 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79253967-faf8-3d41-b0d5-f51b220c3101 | -3.61867 | -51.47389 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a74e50e1-f873-37af-9e9c-1398d44e9447 | -1.42276 | -55.23667 | 2025-11-02 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45aa227f-b4c4-3bc0-bec0-7c119588f0d5 | -3.42972 | -45.90998 | 2025-11-02 05:08:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69323180-c959-39fe-aa7f-28eaabd7b583 | -1.49565 | -53.12244 | 2025-11-02 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4b7dfcef-228a-3cc0-a085-218f02b0d2ac | -3.38866 | -54.27108 | 2025-11-02 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2c4a265-9c8e-384f-b558-2ac3408ff0a8 | -3.56834 | -51.64451 | 2025-11-02 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba08f04c-c853-341e-9531-2e6af59f6083 | -3.58342 | -50.26261 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8f04696-5cc4-371f-8754-0ba0a07cbcb7 | -3.2251 | -50.58325 | 2025-11-02 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52f37926-9824-3210-bf42-e8957238f797 | -2.44912 | -49.03246 | 2025-11-02 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0736abca-a3fc-306a-8613-8a94d3a0a7c9 | -2.26607 | -47.85904 | 2025-11-02 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README25.md)
