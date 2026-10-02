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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b7556b9-208c-35ae-858b-3c52efc82c0b | -3.32971 | -46.55231 | 2026-10-02 04:14:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e39c7960-ae89-32cd-8023-6b40f9dce1fb | -3.98139 | -41.51708 | 2026-10-02 04:14:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd494b40-3afc-3292-bea6-10fc9f9f219b | -3.13103 | -53.75899 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| eb10e48a-f0e7-3c8b-8298-285058c0f2da | -3.16062 | -54.08062 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0878c682-4b46-3145-844d-a6f3e35771ac | -5.72242 | -47.41431 | 2026-10-02 04:14:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7ef205b-1694-3268-ad23-068df5e0f484 | -3.29326 | -53.85195 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 1487a535-f98c-31fe-9eb3-dcd7f641b945 | -3.26872 | -50.08677 | 2026-10-02 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af5084d4-a785-337e-b702-62a5f8b5e009 | -7.20287 | -46.54742 | 2026-10-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41fff643-dec8-385c-a26c-6e3da4f3a354 | -2.90103 | -54.14589 | 2026-10-02 04:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5b0b313-a1dd-301a-afe3-f881698b3c53 | -3.13978 | -53.74833 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 365ba60b-0477-39f1-a5b7-ca5281f5fa7e | -4.07248 | -50.33092 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 297aaed7-24b4-3683-9626-0910cefdf0e2 | -5.89571 | -53.49428 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d9041ed6-3804-3fa7-9eb2-c93b426b87d0 | -5.99952 | -53.54716 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab622cf5-ad7d-382d-a086-672994de3785 | -9.84179 | -44.83103 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc2bf079-f452-303d-bdb3-e526072b3ca7 | -7.41386 | -47.52238 | 2026-10-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27981482-1440-3ec3-b091-5c0c9e912cee | -9.81554 | -44.83865 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 048613f8-0293-38a8-bcbf-fd01edc9f07c | -3.97754 | -41.52001 | 2026-10-02 04:14:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 02e974ca-5869-3be9-a07d-dcf3e01dcfc2 | -8.01073 | -42.88475 | 2026-10-02 04:14:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3c8f9242-10a4-338d-aaff-6668a78524f4 | -5.73829 | -43.2774 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7988e1ac-50bf-3500-aab5-2823c9cecb2e | -6.18589 | -52.80864 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce5b3630-e5e4-35a3-9640-97251645173c | -7.27191 | -55.60012 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 68eb0ca1-73db-38cb-b73a-b9166a939935 | -5.76341 | -45.16406 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b133f52f-cfb2-3091-8968-18b8bb22ad0f | -4.3617 | -47.77699 | 2026-10-02 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5dc380da-420d-330b-a8e9-b394e7af20f8 | -4.4546 | -47.9235 | 2026-10-02 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 0bc2f2ac-3a98-32f5-82b1-2f8309629d22 | -5.89483 | -53.49901 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0723a5db-2edb-35b3-9a00-2fe63ed64538 | -4.26412 | -50.77567 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1ed01b1-88d8-3767-a8a8-a419c29058c1 | -5.99853 | -53.55249 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64ac1196-d343-341d-a552-c948bff22721 | -6.31661 | -43.34269 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b906247-4f78-30fe-91ec-978db57a9c5e | -6.24406 | -43.77211 | 2026-10-02 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 55ce02e7-8955-33fb-bc20-04a7ea98517f | -4.30248 | -50.78205 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99821527-7441-3ad0-a5f5-10484bfa80ae | -4.28059 | -50.77819 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ba44c03-7efd-3a3d-867b-c2b0f9b0b2fb | -4.28181 | -50.77109 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2827b93-21a2-3866-9960-12a00da1b617 | -7.86808 | -44.1797 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e08c6687-48f6-32e1-8de6-4a0c426da706 | -5.23674 | -38.54877 | 2026-10-02 04:14:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6f5bda28-fa1b-31a1-b8da-fdbf477609c0 | -5.8687 | -43.59723 | 2026-10-02 04:14:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bfc332dc-24ef-3e86-809d-85c427443594 | -3.29685 | -53.85677 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 041cb23d-00ea-312b-baaa-0c4815049416 | -4.29726 | -49.09076 | 2026-10-02 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a9a574ab-400a-3c77-9972-479ab98969c1 | -4.26964 | -50.7437 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e74f7d2f-b9aa-3e22-bacd-6495fddc1965 | -6.3317 | -43.37893 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 920a18ab-1fca-388a-a6fd-ad6c6f8e9291 | -3.26818 | -50.0901 | 2026-10-02 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f6915d5-d798-3cf6-a0ae-b214e54c547e | -3.06612 | -49.37115 | 2026-10-02 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b95a984e-9d86-352b-b85a-376add3a3b75 | -3.29113 | -53.84957 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b5b3de39-9c6a-3dd2-ad74-40212289afa0 | -4.26781 | -50.75428 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0a41d2d-15e8-3278-8e8b-6eac5e74bfc6 | -8.74345 | -47.58972 | 2026-10-02 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f53428b-8bc3-3889-bbc7-befad8281c35 | -7.87278 | -44.17261 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 604ef7f8-3a73-3bd4-9800-f9493c40c682 | -7.485 | -55.00661 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c72e91e5-5010-3ea9-8644-aa59e3ab1dd8 | -8.33153 | -44.1572 | 2026-10-02 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38cee751-87cb-339f-828e-39be198b8e52 | -7.40197 | -55.59088 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b523529-5e59-3468-805c-d7a600f965e7 | -6.43254 | -55.62591 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8746e477-282a-3b9c-acb3-e61c9470060f | -7.86463 | -44.17914 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24bad975-5d8f-3d99-9aba-65054f026cab | -4.3843 | -54.82844 | 2026-10-02 04:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 982c0eff-e050-31e7-b193-b54061c12097 | -4.06656 | -51.10903 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ebb62b8-13a2-31f5-9e6d-8386d03f3f33 | -7.87435 | -44.18463 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53d4304e-a595-318b-8c54-8e2f2761d20f | -8.91491 | -49.26355 | 2026-10-02 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd0668b3-a363-3c67-a1b1-f16fecb1b2d3 | -6.15095 | -47.47072 | 2026-10-02 04:14:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0c51444-50cb-3f5b-81d6-72813e370525 | -7.52225 | -47.33554 | 2026-10-02 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bef4f294-2cd7-34d1-b2ae-2395a376bb82 | -3.03476 | -53.87261 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 176dafb4-9e20-3233-ba05-bfe81a009dea | -9.26027 | -42.4841 | 2026-10-02 04:14:00 | NOAA-20 | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fe4b7bd4-3c44-3697-9fa8-5fd9eda291b7 | -9.84398 | -44.83937 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 126d07f9-9e97-37a0-b28c-264e5305fae1 | -4.2787 | -50.7892 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9225ae3-62ba-3bc1-8bf1-880fb2c0b511 | -4.27696 | -50.76655 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3af3e5e-a45f-3d99-af18-2604d621a707 | -6.21066 | -47.47482 | 2026-10-02 04:14:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 102264a1-32be-3d05-b9b5-901526b8dd5a | -8.00899 | -47.44011 | 2026-10-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7445ae7-c688-3cab-bb79-82b8bc4de623 | -9.21081 | -45.77972 | 2026-10-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6810606c-7083-3f10-8725-2ee8de78279c | -2.90019 | -54.15243 | 2026-10-02 04:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31188195-d7fd-31b7-bb6e-96aacc8f83f1 | -4.28666 | -50.77567 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 046e6b96-186f-341d-8b00-af5cb7732ec9 | -7.7454 | -54.79959 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 473ba366-5381-3a18-bfa3-05f16e880431 | -5.58142 | -42.73083 | 2026-10-02 04:14:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8019e01d-c162-388b-b356-5c46ded97cf0 | -7.41465 | -55.59063 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9559b63a-d946-3e0a-bc53-c7a35ecd82fc | -6.90063 | -43.68025 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63c24bb7-62f6-39f2-9ceb-da01d8ea9470 | -9.79733 | -44.80822 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44fbc8ca-76c4-378d-a916-3c7daf9bfa61 | -5.7538 | -45.15334 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6e89f8d-2efe-3f7b-be7c-5c62945ade96 | -9.178 | -45.61729 | 2026-10-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 058fcd48-dd09-3fa7-906c-b7bb3e679ae0 | -6.14603 | -47.47406 | 2026-10-02 04:14:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f490bafb-bbb3-3991-bcea-be187ceb444c | -5.74449 | -43.28217 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c942dd64-48a9-3600-84ac-0b36e635bbf7 | -8.63763 | -47.8235 | 2026-10-02 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 789a12f4-fb13-3107-9f44-49a1da50fa32 | -8.96718 | -44.17487 | 2026-10-02 04:14:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26f46f04-78bf-35c8-8106-10cc097af172 | -3.32839 | -42.86517 | 2026-10-02 04:14:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0d0f689-8cd2-317e-b94f-81ba3fe223f5 | -2.60658 | -48.25767 | 2026-10-02 04:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 585cec57-a06e-3a03-b2b7-2ff02612a532 | -6.90686 | -43.68507 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2c7d038d-f960-379d-87ef-b2aeedc7cc12 | -4.05661 | -51.1187 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f38f7a21-5802-3042-97ab-ffa8f91e1d2d | -3.9803 | -41.52398 | 2026-10-02 04:14:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 04708388-0bed-3a21-9d28-1bf8fc5d0b88 | -4.0628 | -51.11644 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acce4151-1684-3bea-b481-6f54cc868625 | -6.91206 | -43.67454 | 2026-10-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d4c1b0de-6f24-346e-aea8-b639395400bb | -7.8314 | -55.13794 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b76914e6-a119-3a89-9b58-3da586e93fa5 | -8.17935 | -54.80548 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a07ddb3-9871-3004-a807-e7e578c7f75d | -6.72052 | -45.56857 | 2026-10-02 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 81819db6-171a-3e21-a01b-ed5dd0c7ea34 | -3.27349 | -50.09104 | 2026-10-02 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64abb84e-2c8a-347b-b35c-9985e6405d1f | -6.11057 | -49.03802 | 2026-10-02 04:14:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55370c76-e3bb-30b3-a8be-41b08648cd67 | -8.38387 | -46.29969 | 2026-10-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 126b0e7e-1b23-327b-8b1c-4cdc05ca0ea6 | -7.46693 | -54.99138 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8e296bb-63a3-350f-93a6-bd8a01b5f40b | -7.83665 | -55.13897 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40dfe037-e4c7-3c23-b46f-e1bbc1a8d187 | -9.5238 | -45.3251 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e4400f3-90e0-38f8-8f40-b988a570bb56 | -9.52036 | -45.34554 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2abf43fd-840d-3593-8bb3-b4f94f83867f | -4.24592 | -50.75068 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba41a81e-add5-35d3-bfe6-fd72f848a580 | -7.87497 | -44.18083 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dbb9299-0788-394b-8d5d-11dc380755e2 | -5.69479 | -47.16337 | 2026-10-02 04:14:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e735f813-d4ef-342c-9bc0-88bb600c495d | -6.08796 | -43.34747 | 2026-10-02 04:14:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41135e9e-aa44-31a9-8c42-9f7a66eaee88 | -3.27403 | -50.08773 | 2026-10-02 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e092f215-bcdf-36d4-b5a1-e745084ae78d | -7.86933 | -44.17205 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README37.md)
