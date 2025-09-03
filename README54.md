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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dda796e3-c106-3ef0-b51e-7396dc72f101 | -8.06348 | -52.36933 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fa360cc-96ea-3840-99b1-7a40100ccd21 | -6.42795 | -55.60789 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94ed472e-e786-3b34-bb27-0a43a8958b86 | -10.00832 | -46.89967 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 496323e1-9e7c-3f13-830b-0965f53620c1 | -5.89778 | -57.75158 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 407be4da-9a51-350b-8761-a15e186cc064 | -5.78718 | -46.45845 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caf42f0e-3df5-30ed-ac7d-30c1c8ba8b14 | -6.27518 | -42.66549 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e6594e37-8a56-3254-8638-adc3d2ae05a9 | -10.91833 | -50.87056 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f5ec161-d030-3ef4-8f25-5073cb4514a8 | -6.69683 | -44.18187 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4d2def9-a31b-3478-bf65-f867534725ce | -6.83206 | -52.84024 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2adea558-1a69-37ec-9d2f-4d12db657254 | -6.78491 | -52.81038 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f58f965f-4663-3cc1-af15-7294ab0336e9 | -6.48377 | -49.17791 | 2025-09-03 04:46:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85081144-0a96-30f4-8b54-72662306433b | -6.97642 | -43.27983 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a891c0b1-8cf5-3908-86d9-784a7bc8fd91 | -11.5902 | -52.13916 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 742d38fa-d3a6-3117-913c-a63516f0f950 | -11.07082 | -52.00215 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0700db60-dab9-3c29-860d-034534723a6a | -9.64684 | -47.85405 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3623e901-4b34-33d5-9ae4-24f036414cf0 | -11.04614 | -52.05199 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a41200f2-ee17-326f-8cb9-9335089476cb | -7.93207 | -46.46687 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16af2e5b-4023-34b3-b75c-b8d5328042ea | -5.1119 | -56.96846 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b97d3062-0c1a-3ea4-9705-a01432b32134 | -6.25855 | -43.29834 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae87118f-a2ba-37b4-9b57-b1fea1b61e23 | -7.13323 | -44.56924 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e59b89e2-1eea-3147-8130-f97501526230 | -9.13854 | -49.65573 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dbb2cf5a-e11f-3e71-b8ba-becfb5a63815 | -10.44961 | -53.62023 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5eef23b4-477d-31a0-92ae-3fd76c802b07 | -5.4813 | -51.22491 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88cf54ae-d09e-3653-8dc9-7685b1178647 | -9.74866 | -46.91655 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3e494a2-e305-3bb6-8c54-f7ccceaa70f1 | -6.99121 | -43.10381 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84dc9c51-bada-378a-9593-9537bf3924f1 | -11.62764 | -52.13796 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 547cc0d6-d34e-3972-9d9a-fc192885b50c | -6.79782 | -52.8162 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee06d1fd-8ae4-37b7-a60d-f6bbd8390180 | -11.61166 | -52.13182 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3116193a-0b75-39d4-b5c4-b185b121425f | -9.75366 | -46.91014 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69e03726-6044-3ab6-9f35-283985313ef5 | -11.81915 | -51.4487 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5d8d8dd-0dde-33a0-922a-1d0f206a0640 | -7.01059 | -44.34917 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 402f347f-b59d-3105-a2ad-c63453e349f4 | -6.45473 | -42.38404 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a03cc93d-9d2e-35a6-b756-19f173168ed2 | -6.97053 | -44.33405 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffede98f-2b00-39a5-a873-c18fffc51c6c | -7.70684 | -50.26992 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 007763bb-9f04-3b21-bbc1-940ca00bcdbe | -7.50127 | -45.35506 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ae2e494-9d3a-3862-8959-cbce4d546668 | -10.45694 | -53.61767 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a2fff81-1a8e-3a87-8ee8-8363a32ef077 | -11.59698 | -51.94247 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7a8c628-07f8-3af1-83be-2755f444edb4 | -11.60447 | -52.11271 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 396c10bf-cf49-36d9-a2cd-484e2e68f967 | -6.49851 | -44.0944 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d9311a8e-658c-3505-bd4b-7aa3c1323b48 | -11.60938 | -52.08115 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa77dfa0-ef19-34b6-9d27-801e4357c3c5 | -6.8068 | -52.82501 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d516306-d556-3c61-a225-96428efcf1c1 | -8.88603 | -45.82541 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0fe5bca7-ebee-31f9-b701-f60b377442e7 | -6.433 | -58.12943 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 919f2e1e-7094-3cdb-8c92-77c34d9227fe | -8.06015 | -52.36883 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7802e93d-b8aa-3256-92fc-e5e842b9609a | -9.64048 | -47.03365 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1314c6bc-3ad9-3c14-9c04-b05b131981f1 | -5.69008 | -45.94758 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2aecca4c-b06c-3af7-b3af-d55cac2cd5ca | -8.55204 | -47.47717 | 2025-09-03 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 825ae652-dcb1-3352-a37f-12a66c29aeac | -6.78154 | -52.80986 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a3e363e-9934-3f8d-91ea-b0b7838a112b | -9.63222 | -47.06329 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0760e17-df15-3b91-94be-d3f17ae35e3d | -7.66876 | -42.7133 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fb9208af-48be-33dd-8740-c0736cadd1d5 | -8.88887 | -45.80561 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b628b2d-8161-36b2-9b03-82fbe0a44a1c | -11.61221 | -52.12831 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e0f0f0d-7860-3f6f-98eb-5ceaa5ce132d | -6.80795 | -52.81778 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 621825db-1767-3fd1-84b2-e66a84679262 | -6.98552 | -46.11106 | 2025-09-03 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8579be69-55e4-3a87-a626-69bd8bbd3c24 | -5.7948 | -43.23143 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 853cbf61-9cbd-36b8-9534-ea5116f43d4e | -6.34657 | -45.66562 | 2025-09-03 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b114edd9-9f04-3543-b575-1b129039f279 | -8.04851 | -52.35633 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 896bd23f-833b-32f2-973e-64a18cd9f742 | -10.00276 | -46.90984 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db7d2aa8-bc32-3ce1-b1ff-1902393d812a | -11.06876 | -52.08062 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 369fbc0e-422c-3d27-a78c-4a784cb3bfec | -8.85424 | -52.01735 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8909ecb-4a23-3c96-8ca6-33ccadcd71eb | -11.14046 | -46.34146 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68ee2b32-06c8-33e9-b17d-86c0a0b8c42e | -11.58853 | -52.12813 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b4a27549-cb9c-33bc-a04b-331416dca79d | -11.6512 | -52.05189 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3764a53-0da5-30fb-8a5b-b8de52d241d7 | -11.80108 | -51.54441 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0104596a-1902-3567-85f3-dc0b370f1d05 | -11.61595 | -52.06064 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39afc569-2ba0-39e5-bde0-f5f3f80db715 | -11.40201 | -46.85881 | 2025-09-03 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67ee0468-c062-3375-b59c-9676f22546e8 | -6.82868 | -52.83971 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d0da88f-e62b-303b-bca6-8ae16e9cea90 | -11.22876 | -55.08432 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50fb4261-5491-302f-b787-9e13909f2daf | -6.7877 | -52.81456 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a87185f7-3d4d-3fd8-8ab5-80d261a8ce83 | -11.56548 | -47.61386 | 2025-09-03 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c29cd99-b165-395f-8007-27793f3bd9a8 | -7.70756 | -50.31014 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da4142f2-b88e-3ffd-93f6-1423f385a3d8 | -11.62533 | -52.06573 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c49766c-f585-33d2-a034-530ef5d3d756 | -6.35176 | -45.65905 | 2025-09-03 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35f8b555-5345-35b2-b1e2-4ce5a76ddbe9 | -6.46887 | -45.41357 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 69a05ae9-dae7-3141-a103-25aa3f16e845 | -5.90344 | -43.35344 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe7c7624-32be-34d0-9fb0-7c3fff633080 | -6.97375 | -43.23548 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1eaed620-f5c7-33c2-be3e-f3f50d5ac1d2 | -7.481 | -44.83183 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8fc99df-986a-39b3-92af-3f2ee5cfe5df | -10.28141 | -54.24207 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1bb02f6-394f-3a3d-aeb5-a9265fb5f42d | -7.63816 | -43.92264 | 2025-09-03 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a563f0d5-4c44-3764-957b-0f5b569e29c2 | -7.86009 | -46.7356 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc631954-4e5c-3bb4-a716-6a5075eebd50 | -8.97953 | -50.03691 | 2025-09-03 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4a8dada-c77c-3ded-bc56-6d4f679e59a9 | -8.86912 | -52.03039 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3d5b165-1fd8-3bd2-8119-6416f8057a38 | -7.78016 | -50.96483 | 2025-09-03 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e50c547-5d9f-3e92-b627-035a5525ef20 | -3.88572 | -54.2123 | 2025-09-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f20d2fd9-be58-30f4-b8d0-7377b5c55dd8 | -7.50737 | -45.34314 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b7dc0ca-d043-31c3-aeef-c58a3e8e4309 | -5.89925 | -43.39008 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08ad23c0-ebdd-3bef-887d-34bca9b216fd | -3.87554 | -54.22866 | 2025-09-03 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 17fda2aa-9951-3797-b068-20bf1f245836 | -8.04574 | -52.35233 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16986600-385b-3625-8604-e60556e0d6a1 | -5.75627 | -45.3502 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 222912c3-388e-3235-bb88-0288704eefed | -9.33443 | -55.2262 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5e77b15-322d-3474-95ef-bf31fd59cb18 | -10.49669 | -50.31866 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 921cfc67-b15f-337e-8754-9552e18dcbb8 | -10.0078 | -46.90332 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39953e00-a1ec-359b-a402-e74cd66dc6ed | -11.61101 | -52.07063 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2506da3c-fce4-3b57-b387-d522805b58c2 | -5.93143 | -57.71559 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57ada7b5-fb10-38fb-a090-9cb30cca474f | -6.37178 | -42.99883 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80ddd314-aa67-3f6d-b733-d0606820e3af | -9.95797 | -51.63432 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc1c3850-9bf7-3b1a-9532-02599a0cf728 | -10.34754 | -48.14642 | 2025-09-03 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4366c4e-1c02-3681-a66a-55223121cbdc | -6.85159 | -45.54753 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3fcf0ec1-59aa-3a4b-9a23-dd98b4131a2f | -8.37103 | -48.29513 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5db401f-1f38-3f45-828e-962b4204c0f8 | -11.07744 | -52.0032 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README55.md)
