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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93fe0e47-7abb-3ee4-a8cb-4da60c936ba9 | -16.03961 | -44.87079 | 2025-08-05 04:17:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 9ac1999c-9d1c-36b5-94c8-0af07646d146 | -7.98643 | -43.16429 | 2025-08-05 04:17:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 709e66fd-d56e-38a9-b62c-6ea395a5c45f | -10.45064 | -44.36102 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d071b699-b66e-3e40-b56a-fec90364472b | -9.32221 | -44.84691 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a19e840-8e70-3c14-ad3e-60ffeaf9dfd6 | -14.26794 | -51.98245 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8302988f-ac7e-3fc5-aa6a-58b416fc8bb2 | -6.42279 | -44.81642 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 07a7d705-aeef-3830-919d-caa0715b0475 | -8.24511 | -45.06422 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6452927-21ae-354b-8c9a-7129091cfcb9 | -8.25531 | -45.06586 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5bda27e-65ba-3324-95fc-aa87e29e5153 | -7.1415 | -44.07751 | 2025-08-05 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab27a3b9-7688-3061-93a6-28b25f7c756b | -8.84668 | -47.61493 | 2025-08-05 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b7507365-c64c-3796-bf51-353c37895ec6 | -7.08997 | -44.68911 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 840bb112-63bb-3fb4-a39b-83d44d195158 | -7.19202 | -44.16168 | 2025-08-05 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53117b42-2570-3c67-8bcd-92ac054e0b39 | -7.9958 | -43.14796 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e219223e-d622-3a7f-be05-a87de8379c89 | -7.77307 | -45.21651 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6e4e0db-8cd9-3fa0-b39e-43027c2b3ef2 | -7.84514 | -44.94421 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4544d1bc-da60-3477-b4b8-2360f4dbf48b | -6.46385 | -43.03356 | 2025-08-05 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e3e7cdf-5aa9-313b-a27c-efb678935b6d | -7.70031 | -45.12856 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 938e2074-dfaa-3c72-8b45-b219bb9cb342 | -17.21761 | -44.83738 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd43d964-5be8-3425-bc21-b939da310878 | -9.1653 | -40.59614 | 2025-08-05 04:17:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 683da9f0-22b1-30e4-a2c9-2152f0386a5a | -6.67564 | -49.79958 | 2025-08-05 04:17:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c82d5c9-8bb0-30e9-946d-bd904d582bed | -8.01514 | -43.13319 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5c2bd0c8-0d60-33b4-b7c0-664765b7f29d | -8.00408 | -43.13858 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ccafb5de-f552-33ad-bcfa-1652d843dea6 | -6.42621 | -44.817 | 2025-08-05 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfb2b602-e059-32ba-bc1c-3fe96d2a1079 | -7.99471 | -43.15492 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0017e2e5-2791-3ba4-8187-394230863787 | -14.29638 | -52.00822 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 499d8efa-cce3-32e5-8e29-09b65000c313 | -7.20916 | -41.8557 | 2025-08-05 04:17:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0044c65d-3244-3888-995b-38b8a9e011f4 | -10.47183 | -44.3714 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fb02ad3-4e9c-387c-b041-7cf3485b69ba | -11.32386 | -47.31045 | 2025-08-05 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5397f2e6-ee6c-3eac-bfe1-258ca2af1ffc | -11.76464 | -44.97029 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad0b9070-2da3-3e54-a49d-de245cd2ed80 | -10.907 | -48.36459 | 2025-08-05 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82af82f0-68e1-32d7-865e-5a959388dda3 | -8.85201 | -47.60629 | 2025-08-05 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e9a3217-e85d-3acb-a237-6f4c84f9269f | -6.38238 | -43.71872 | 2025-08-05 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f42b5876-e112-37ff-b9e0-89ee7a0c5860 | -10.44453 | -44.37809 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17c8768c-c243-34bb-ade9-ecd5552b00d9 | -11.916 | -44.95102 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ee255f6-0716-30df-a977-36760f2420ed | -5.81252 | -46.9852 | 2025-08-05 04:17:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 125f409d-00e0-38ce-a4e8-2d52be4a0946 | -10.78837 | -46.64735 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d395b59e-2122-324f-816c-7203a7e5721b | -7.98752 | -43.15734 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f81d59f4-5462-34c3-882c-e1e8ba763268 | -9.31827 | -44.84995 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af09a34f-204c-3b06-bac6-08ee564a2b4b | -7.08541 | -44.69579 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ae4786d-52af-3f9d-a65c-a908c454b25b | -10.33001 | -47.82964 | 2025-08-05 04:17:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 47493031-6d8c-3028-9259-baaf8302c667 | -6.68095 | -49.79578 | 2025-08-05 04:17:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3052472c-6455-319b-b75e-216896922798 | -6.37848 | -43.72169 | 2025-08-05 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b505e1b0-86b7-38ef-8eb9-8e81a4f76a0a | -11.75854 | -44.96566 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 938eb84d-cd59-3887-b81e-adb3317e30c4 | -10.77496 | -46.64088 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c46b3ce5-8efa-38ce-a0a0-e4c2e823276a | -7.9969 | -43.14101 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 71848455-6f11-397b-af71-31057805f94f | -11.80871 | -44.26401 | 2025-08-05 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d40f5cd-c959-3932-84de-9c7a1497f4fb | -8.26891 | -45.06808 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ddc2e04-4977-3dda-9a92-3ff49e0a217a | -6.57712 | -46.34001 | 2025-08-05 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4619042e-ae38-3d05-af1d-01c7bf8ecc03 | -11.27476 | -44.64714 | 2025-08-05 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94e865ff-1a20-3366-9617-20d0189de70c | -11.75187 | -44.96459 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c277063-9a0d-330a-9410-66320464fd40 | -8.85124 | -47.6109 | 2025-08-05 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49ba5027-5a31-3425-9b08-1e250d317f5e | -14.27802 | -51.97944 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8701b9a1-f482-3c28-b2ae-e429a8105992 | -6.7853 | -43.24805 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 85877762-01a5-38ea-9a21-02579da5adb3 | -11.74829 | -47.54092 | 2025-08-05 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6695908b-a471-39cc-882d-431987a0598d | -17.21483 | -44.83318 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab576d22-fefd-3135-bbf9-87ce11bbf75d | -9.05218 | -45.06634 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 480a98e2-882e-3621-8906-859a6a0f5b80 | -13.0459 | -56.87918 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b843d70a-0cfb-3064-bc88-cc5b2d6f3c6d | -12.68023 | -48.12095 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f5a1508-f638-3d4e-9d46-72bd59882b8c | -12.70995 | -48.10348 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5a63aff-b84a-3d27-b87a-b5444690e156 | -12.72964 | -46.39515 | 2025-08-05 04:19:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6308eae6-0c2c-36a1-905b-51804053d81c | -12.71934 | -46.39349 | 2025-08-05 04:19:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9932f0b-2152-3fd0-ace1-1e15c45405a1 | -14.35153 | -47.10094 | 2025-08-05 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6ffc7ad-a0a9-3df2-9761-56e4a1f1641e | -20.06154 | -43.70784 | 2025-08-05 04:19:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d691e2c-8d93-3818-92ee-0effc4c3f86b | -19.79628 | -42.0092 | 2025-08-05 04:19:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c0915e6a-f859-3fd1-b7df-0fe6916f6d32 | -13.04472 | -56.8772 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eee6c91e-6ffd-3c61-96bc-3455ea9ef9b3 | -13.06618 | -56.87791 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b48890ad-16d9-382d-a28e-c55a017293d8 | -12.68763 | -48.12233 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fb4b7e2-d5df-3b20-848f-6e10f59ca58a | -13.82166 | -43.68927 | 2025-08-05 04:19:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33554ef2-82bf-3f94-86fa-88d61683c51d | -23.72499 | -47.46259 | 2025-08-05 04:19:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1c84a2a0-6cc2-36d1-8009-dea1d8b272f0 | -12.68467 | -48.11736 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdcd2d45-208a-3099-aaaf-e23fc9b27d10 | -13.08603 | -56.91039 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3d9feb43-f7b5-30c2-b32a-98c4462a85ee | -13.04064 | -56.87257 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f39d745c-bee4-3261-8d1d-9fe088e72f89 | -13.05311 | -56.90126 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bffcfde-69aa-3070-abd5-6ca60fdd0cdc | -12.98637 | -47.46571 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a9fb70d-6c19-3446-b74a-637d777630e5 | -12.71075 | -48.09882 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f1be50a-d4df-3859-aaa0-ff65fcf38f78 | -13.03948 | -56.87797 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d39d45de-daaa-3959-911d-15ec344b4b1d | -13.37378 | -43.75575 | 2025-08-05 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17adf897-fc52-30d4-88db-a1f914c65ff1 | -13.04583 | -56.8718 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0699c119-7619-3de1-ad76-945cbbd9780f | -12.71825 | -47.79594 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7be821d8-cee5-3dba-99cc-a5dad14f73c6 | -13.25937 | -46.97562 | 2025-08-05 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce11dc37-95ba-32a5-86b1-8ac3c27cacf0 | -13.05345 | -56.87505 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ad92cc12-04da-37f6-af8d-bccc5766f1f2 | -12.99063 | -47.46218 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05529970-c7f6-3737-b454-810d8e1ea436 | -12.71446 | -48.09943 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a96b7506-3f26-3647-8180-2efdd550ceb0 | -12.67653 | -48.1203 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 105a6651-a6af-36e3-a464-0841608c60d4 | -13.05001 | -56.88389 | 2025-08-05 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2b96fa2b-2ed0-3607-82ce-5197975d6ebf | -12.71605 | -48.09016 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 753cdcea-0c44-3725-a42d-f32123f7b439 | -12.68097 | -48.11669 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8daeddd-1529-3698-8959-2ad91cc8447d | -12.9882 | -47.46438 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 13da5df0-a686-3251-bb89-d5de74417121 | -12.71533 | -47.79095 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24c471cf-1292-3525-83d2-c23bcd4f9b5b | -12.67573 | -48.12488 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a5a58dfe-f766-306d-abe8-b5cfb289ea69 | -12.72683 | -46.39082 | 2025-08-05 04:19:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c18d9685-efab-3675-a2ea-9eb26807fc03 | -14.05613 | -41.99214 | 2025-08-05 04:19:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 51eac7b6-d07a-3a04-a781-611c03bbc981 | -20.74206 | -49.40159 | 2025-08-05 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 935c2b2f-0aee-37eb-bd6d-d58745907b66 | -13.22688 | -46.84874 | 2025-08-05 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1207b12c-8522-3268-8137-e4e2e478279e | -12.71897 | -47.79161 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2611ae82-6eee-38ce-b51a-b0c2a9faab75 | -12.71461 | -47.79528 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c48dada-b5a9-38b4-ad34-56589c1dc56d | -12.68686 | -48.12675 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45bb33bc-fd82-388f-9861-fd6972a2c1c7 | -12.99132 | -47.45803 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f137688-3069-34af-8b22-6e44fc7f5c6d | -12.70643 | -48.0797 | 2025-08-05 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19ca93cc-7f60-322b-8a0e-9117d0e3ef90 | -23.72264 | -47.46283 | 2025-08-05 04:19:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |


[Clique aqui para ver as próximas entradas](README20.md)
