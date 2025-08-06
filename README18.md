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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1623f9cf-807d-36a9-afc3-8f6129dd91ab | -4.55523 | -50.30311 | 2025-08-06 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c3f8df8-c595-3376-9318-97be8b1fa54e | -6.74744 | -45.29809 | 2025-08-06 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90c0c157-86b4-3644-890c-dea28a0905b5 | -9.51204 | -46.7307 | 2025-08-06 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7a7c905-b169-3357-b396-b3772aa965ec | -9.07594 | -45.05042 | 2025-08-06 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1d2f4d9-1e2b-3bc7-90cf-b2e03b6c295d | -7.99886 | -43.13728 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 74455273-2953-3e02-95c5-b3730a1cdd11 | -5.42636 | -47.14852 | 2025-08-06 04:19:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31b88754-6a60-3cd0-b5ad-1485d797a227 | -11.74365 | -45.00968 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c8620c4-ec70-3aa1-bfc4-aae946e3b4e5 | -6.25696 | -43.07766 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f4b566d-48e1-313a-a241-2c203c65abcc | -8.02006 | -43.18266 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| d3d4d07e-46a9-351f-b5f3-5e2ad9d65e4f | -10.44128 | -44.36499 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0525e71-adcd-3ea4-924b-ceaed94fdc4a | -7.38991 | -44.62663 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6eb2a574-6f10-35ab-b04b-4b7f456df632 | -11.89793 | -44.97882 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a010992-a440-35e8-b4cc-493c5b0ffba6 | -9.62848 | -40.59137 | 2025-08-06 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f6fbef77-1459-3298-b154-9ba60f678707 | -8.53733 | -47.47802 | 2025-08-06 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0516856a-dc4f-34a8-80b4-edded7acb1bb | -11.74012 | -47.54556 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbce5e24-48c0-3efb-8759-387c2e12bf27 | -11.43587 | -45.13607 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 05620390-ab8a-37ed-8315-6bc792177277 | -11.73774 | -47.56026 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53318ffb-e5a7-3cc8-9202-47a91733e6bd | -6.92471 | -43.33816 | 2025-08-06 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e8e6d07-9ce5-33fb-929a-1ed8a924d57e | -10.48106 | -44.375 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03c7dbc3-1ddc-3198-ac75-7483c84ff21b | -11.43533 | -45.13961 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 82639468-990c-30a9-8c0a-d757409a6d52 | -6.41208 | -53.37366 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d34cafd-af20-3443-90c6-4156cd7f9d34 | -8.04824 | -46.34425 | 2025-08-06 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f100f869-7e02-338d-ad3a-c1feb561c858 | -7.191 | -45.47914 | 2025-08-06 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 229d8b9f-d57b-323b-abca-41279866e267 | -7.82493 | -47.22115 | 2025-08-06 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4631d687-2bd7-39bb-b029-1b4e83ca8911 | -7.06914 | -44.39859 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6acd4434-1746-3e5a-bca9-ac251bb446e4 | -7.67471 | -45.10548 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9489f2ad-c4f9-3bb2-a752-cd229c4bf0c6 | -11.78815 | -45.00942 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8256a8a0-0d4a-31a9-af9c-0a50379799bf | -7.58569 | -45.30435 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8959773b-1e0b-3c41-96dc-8177e36bd103 | -7.36423 | -44.16174 | 2025-08-06 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51373afd-1a21-35cb-999a-1b7fae9f5046 | -12.02343 | -44.82434 | 2025-08-06 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67fda9be-0b60-3aa5-8bad-3e2afe7a3da4 | -7.08229 | -44.35783 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9bc24e1d-6730-3e49-9501-0ad5687182d5 | -11.64586 | -50.15855 | 2025-08-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61176394-bb9c-37eb-83e7-57435844caf5 | -5.59407 | -51.12952 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f2fd2be-8b1b-30a9-8353-5d58dc8b4c60 | -7.6714 | -45.10496 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ec3fcff-8366-3ff2-8d16-90fc7cb7d48c | -9.50928 | -46.72655 | 2025-08-06 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77dd6aa0-91a7-3599-8954-a7f573f89408 | -12.42799 | -44.70121 | 2025-08-06 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aeaa60de-2be1-3101-8a3b-ea429ae511eb | -6.42336 | -53.36945 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62d71fdc-b174-330f-817b-6d021d1e90b1 | -6.43703 | -43.11555 | 2025-08-06 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d668573b-2192-3686-bd73-3ef7806521cf | -8.75468 | -46.4143 | 2025-08-06 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4db7bf35-4a36-3064-9f36-4730b2b3f2a6 | -11.73277 | -47.54809 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 326909a2-4f0c-3f8c-8e6c-88543f4099bb | -12.5101 | -44.77407 | 2025-08-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54a30068-ea1d-3dac-bce9-bf042ed34f1f | -11.43478 | -45.14314 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1fbadfd1-3df0-3760-accf-66bf6eb3b7d1 | -7.37198 | -44.15577 | 2025-08-06 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6505140-8bbb-389b-b491-f6b569b40800 | -10.90845 | -48.38026 | 2025-08-06 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d4c089f4-fed9-3a95-97bd-ed5286e29320 | -7.20659 | -41.84946 | 2025-08-06 04:19:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 54b21f9a-d8e8-356e-885e-1dd875f3a0c3 | -11.92351 | -44.02934 | 2025-08-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65c4dd04-6394-3e48-9d15-deaaa2063729 | -5.79547 | -46.99539 | 2025-08-06 04:19:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f601869-238c-3f3e-9922-8bb4a2d53cd0 | -6.98737 | -42.09822 | 2025-08-06 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 81001fcd-7f32-3465-a530-b0db3c460295 | -6.26806 | -45.25748 | 2025-08-06 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc04a644-4a8f-3cab-a0a1-37c5c3741688 | -7.90994 | -45.5301 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbb66d6a-1d7b-354d-aa1a-5e1c42203056 | -8.99169 | -45.69279 | 2025-08-06 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d27525d-143f-344c-af44-6ed247d1e8ed | -8.02063 | -43.17891 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 117f2590-80b7-33e3-9f55-7cef6f270a66 | -11.74589 | -45.01735 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43f0806b-a352-38e0-9027-8a716ef2246e | -9.35729 | -40.33873 | 2025-08-06 04:19:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0b10934f-35dc-3a8d-aa7b-4c6b2f25eebb | -6.41372 | -53.36448 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8aa1444-73d9-395e-824a-5951f20da152 | -6.91943 | -43.68345 | 2025-08-06 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0b6f2d20-a3fc-3ceb-9526-12dfe6ad8d97 | -11.90844 | -44.95497 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73791ff3-78cb-3d6a-acd8-08e265b11961 | -8.83673 | -47.6201 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6577f0b0-4ff8-30d5-ab20-1b021bf8fa3f | -10.429 | -44.37774 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 427e1ddd-a3dd-3026-9178-3a5a259d7f99 | -8.98838 | -45.69226 | 2025-08-06 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7747d094-50d1-3aa9-a0bd-96fcd2eb51c9 | -10.97308 | -45.55676 | 2025-08-06 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f59f2ca-5947-3443-9ddf-8811232f2ad6 | -7.39654 | -44.62764 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab663aa0-0e9f-3ee8-aa4c-e854bf8b8d95 | -10.1186 | -51.67354 | 2025-08-06 04:19:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1803953-7856-35d9-9a13-05b463c9ed5d | -10.6493 | -45.23957 | 2025-08-06 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 279f9be9-884e-3d84-ad01-9bef15ff5dc7 | -7.90608 | -45.53305 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bca5dca-d947-36e0-981a-498bdf14d3aa | -12.03688 | -44.01928 | 2025-08-06 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cda62a6f-ebeb-310e-90bf-3952e72a4395 | -8.84429 | -47.61739 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc1a948a-7d25-366e-a91f-1e1a7c306108 | -7.24645 | -44.61116 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50b80cd1-0014-36cf-8b6f-90c81321c406 | -9.70317 | -51.95039 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4170651-f76b-345b-8f7b-1c87708e39da | -6.48675 | -45.54926 | 2025-08-06 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e63959a-d33c-3d0a-b65d-862ee803854a | -7.45394 | -49.2583 | 2025-08-06 04:19:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 281f0ca4-37fa-3671-a6cd-f918c7e156f7 | -10.434 | -44.36751 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eebc5d71-9fd2-307e-a5e5-eae1a34b4b8a | -5.28286 | -44.95562 | 2025-08-06 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5586f427-12ce-34cb-a0bf-98e352a41d81 | -7.08175 | -44.36131 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d872252-8e4a-36a8-b680-bb993bc7dff8 | -11.92294 | -44.03314 | 2025-08-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d76bbda7-c01c-3b22-9bd8-9c9174d86be8 | -7.58129 | -45.31076 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eab409cc-c6c6-3c23-a067-a89e10273ffa | -10.90495 | -48.37967 | 2025-08-06 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fa3d3de2-aae9-3fc7-b512-3ad2f1325af4 | -7.38715 | -44.62262 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72729a23-2222-36b3-bcdc-15ee7a4009a8 | -9.76934 | -49.74779 | 2025-08-06 04:19:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b43c378a-c8cd-3fd9-92d3-e2823e350786 | -6.71887 | -43.57626 | 2025-08-06 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f805f5b-9155-3286-aa1c-4b7db80befb0 | -6.28889 | -45.74381 | 2025-08-06 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1659921-fa8f-3606-a02c-e4755be899b3 | -6.64066 | -43.88007 | 2025-08-06 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8b7c9621-414c-3a55-a2ee-c8402bca8747 | -9.47245 | -57.85297 | 2025-08-06 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bab53bb0-d161-3738-8dd3-f86c09777ea5 | -8.62739 | -50.01557 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 246c929c-0582-358a-8e96-2cb187d09e19 | -6.94664 | -51.63387 | 2025-08-06 04:19:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9345873-6d38-3c27-a44d-98d9aa897bc2 | -6.95646 | -41.57989 | 2025-08-06 04:19:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 19174d40-8944-3292-9dd4-4d981f4ec913 | -11.42923 | -45.135 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 16928d13-78e7-3efc-802d-01a89384b858 | -10.64653 | -45.23552 | 2025-08-06 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6356493a-9a87-35ac-a4fb-47fa45958efa | -6.95093 | -50.45671 | 2025-08-06 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 161633e5-3e66-333b-939d-fa4d9aec47fa | -7.21379 | -41.85058 | 2025-08-06 04:19:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 97e68888-9f50-36b5-a8b7-748f45c3fc9d | -11.89848 | -44.97525 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84d40059-6f03-335b-a228-5015fe35c218 | -11.73298 | -47.52541 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bcdb774-7ebc-3e0a-8b46-75e1ed9a3468 | -11.7425 | -44.99488 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae5c18ab-b711-3d66-a9db-d90353c451c0 | -10.46306 | -44.33512 | 2025-08-06 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2316266f-8b4b-3433-b29f-064028598614 | -12.55205 | -44.73468 | 2025-08-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32fbbb05-d0ff-38ed-8eb6-c4a9b741a995 | -6.91888 | -43.68702 | 2025-08-06 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34b7fc73-88cf-332a-9639-01d05bb1c6a2 | -7.83573 | -45.2267 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c49fabd4-ea1a-3067-8dbb-0cf599b04925 | -8.03518 | -42.67367 | 2025-08-06 04:19:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 71239953-a7f4-3dba-b695-8410f097f572 | -7.667 | -45.11136 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ec48ace-726c-377d-af99-c5c28d200a25 | -11.91011 | -44.94414 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
