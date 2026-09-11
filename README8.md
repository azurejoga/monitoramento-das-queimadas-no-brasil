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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fd619b3-96b2-338a-943a-c766eda29588 | -7.81098 | -42.77901 | 2026-09-11 03:47:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a50ba556-b31a-3245-9aee-a2b76a501213 | -7.13405 | -44.57315 | 2026-09-11 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a86124d-c09e-306f-ba24-9edf2da7c9a5 | -10.15617 | -36.31264 | 2026-09-11 03:47:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 18c32da5-41ba-3e7f-bc44-2f1d5cb77524 | -8.49131 | -44.74857 | 2026-09-11 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 822ee9b7-1451-3d7d-b148-6c5bde015e9a | -7.4174 | -39.14417 | 2026-09-11 03:47:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9ac48d8-b023-3a23-b486-8d89420d7dc0 | -7.98944 | -44.00567 | 2026-09-11 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41662ee2-9086-3852-968f-f8886d385251 | -7.0262 | -45.11267 | 2026-09-11 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8725f22c-3e1b-37a0-8226-a8c58210bdb1 | -7.99011 | -44.00195 | 2026-09-11 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65a32093-f95a-3614-bdeb-965c0a5e46f8 | -9.32489 | -45.6484 | 2026-09-11 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f96eab6-097f-3439-a0b1-0a236949123f | -8.48859 | -44.75233 | 2026-09-11 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e560053d-5038-3e44-8abb-ba27291b2cfd | -9.31606 | -44.36317 | 2026-09-11 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2ba4877-28c3-3f78-b460-cbcfd54351d0 | -9.7182 | -43.38995 | 2026-09-11 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8615d309-c7d7-34cd-8e04-8cafde404b60 | -9.6828 | -43.46443 | 2026-09-11 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b22e6db0-723d-3186-8257-bf60e207bebc | -8.4894 | -44.74812 | 2026-09-11 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a528e1d-9ad7-3ebd-ac78-4c74c7be853a | -7.3472 | -44.19689 | 2026-09-11 03:47:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cab0e29-1db1-30ec-9b1d-83053d10582a | -9.31195 | -44.35426 | 2026-09-11 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c062ed1f-4f23-363b-9a82-9624dd30d982 | -9.70052 | -43.45704 | 2026-09-11 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 68ee565a-fa5c-315f-b604-fd7cf8acc4ee | -9.5382 | -45.46196 | 2026-09-11 03:47:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5e77bbe-79a3-3e02-8e2b-19b1f0c4a80f | -10.10459 | -39.12714 | 2026-09-11 03:47:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 247e6ee0-4b01-330a-b8b7-80797bade1c1 | -8.49021 | -44.74391 | 2026-09-11 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f63de891-e32d-3654-83fb-26652905cc86 | -8.90322 | -43.88577 | 2026-09-11 03:47:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc206ae0-9ba0-31a4-8106-011461fd48d0 | -8.90873 | -43.88673 | 2026-09-11 03:47:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d27194b3-f319-37bd-a8f7-b32e75fdb9d1 | -3.32152 | -42.29903 | 2026-09-11 03:47:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8dfe7848-7093-30dd-bbb1-2267532914bb | -7.35368 | -44.194 | 2026-09-11 03:47:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0f10ba2-729d-3515-9b02-efd8b73e7ec8 | -7.13481 | -44.56911 | 2026-09-11 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c12bf7e1-7251-3997-b367-867772c7b140 | -7.34791 | -44.19303 | 2026-09-11 03:47:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62fa868d-d357-363e-8098-fd3063c25604 | -8.77528 | -44.18167 | 2026-09-11 03:47:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f16fddb1-5761-39a3-9ca1-0e95a1e65c7b | -9.78327 | -43.44569 | 2026-09-11 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ecd9e89-bb8f-3c4c-9bc2-dd1c06ef4618 | -3.51685 | -43.25484 | 2026-09-11 03:47:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 976ba894-a486-3c93-b21b-ce6975ebc5f2 | -7.97259 | -44.0024 | 2026-09-11 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f58cb61-b0c6-38c7-89fc-3d93cd577608 | -7.27817 | -38.9829 | 2026-09-11 03:47:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 365620c1-2eae-3851-b780-ad306e04ee83 | -8.07775 | -38.2255 | 2026-09-11 03:47:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41025c90-f26a-3092-80b6-82e7f3fa5ba9 | -3.51656 | -43.25771 | 2026-09-11 03:47:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5080555-598b-39cc-9a50-aa83469ae969 | -7.97185 | -44.00642 | 2026-09-11 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb742563-df8d-3241-9d3d-2d257c1f5cf1 | -9.68341 | -43.46111 | 2026-09-11 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 715971d2-722b-309c-ad40-0cbdfa22e3b0 | -8.63522 | -47.4207 | 2026-09-11 03:47:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 112684b4-e246-364d-aaef-2d0a05fa1a77 | -9.31043 | -44.36216 | 2026-09-11 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73f905e9-8896-3a4d-ad6f-f88c366dffdb | -7.02711 | -45.10788 | 2026-09-11 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd7865e8-aa5b-33fe-833f-5d9984b79a7d | -8.48516 | -44.73867 | 2026-09-11 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3f0738f-84a3-308c-8fa8-631d6beaeaee | -6.69509 | -45.47655 | 2026-09-11 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bcb2ef4-db5c-3bc6-8d45-38930d031a3c | -9.31466 | -44.35572 | 2026-09-11 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f851acdf-8800-3778-b3f4-ccdf4ef76e19 | -7.14974 | -45.86628 | 2026-09-11 03:47:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b5a9dbe-d6c0-3298-9b8d-335f8d95b942 | -8.93691 | -44.40369 | 2026-09-11 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42aaf56f-e970-3c2a-af22-9f60eb82c961 | -7.17945 | -43.60903 | 2026-09-11 03:47:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e62bad33-3e4f-33a3-ac59-479aca498dcf | -7.14872 | -45.87167 | 2026-09-11 03:47:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a8f24bd-9f7a-3661-b800-b9ceeca8e75c | -7.02676 | -45.11294 | 2026-09-11 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29958ee1-e102-3eb4-a265-546ce21ce0d3 | -8.62817 | -47.41849 | 2026-09-11 03:47:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45282e7d-3b8e-32d6-8109-391eb0446326 | -9.7786 | -43.4415 | 2026-09-11 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 774271c7-bd49-3ef6-b386-171ebf4fc776 | -9.69987 | -43.46062 | 2026-09-11 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7e7b4182-f5e1-3407-9f35-805cd72d0aea | -8.63498 | -47.42001 | 2026-09-11 03:47:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ad2b17e-6582-3db1-b1c5-ccbe8d894337 | -8.02929 | -43.84859 | 2026-09-11 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f2d05ea-9425-3daa-b39a-76b0103d4c14 | -3.56029 | -41.11648 | 2026-09-11 03:47:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6778ddd7-8003-3f26-b337-82605eab8ce4 | -8.02998 | -43.84477 | 2026-09-11 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 87d7d481-c0ce-33cb-97c8-07f06b65a658 | -3.32697 | -42.29987 | 2026-09-11 03:47:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a12bfb21-adb6-390f-a661-ef48d4eca097 | -8.94264 | -44.40453 | 2026-09-11 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56cf8c88-df36-31a3-a619-706b128180b0 | -8.48624 | -44.74323 | 2026-09-11 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42e6765f-19f2-3cc5-9142-4a2fdcca478e | -7.18569 | -43.60624 | 2026-09-11 03:47:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59dd3289-b871-3d3c-a974-72b985f44140 | -7.97329 | -43.9985 | 2026-09-11 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04e1fe38-0894-3684-a966-37b2f0cfc99c | -9.32576 | -45.64389 | 2026-09-11 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8c8af08-244a-3633-b3ea-00f77eab7b86 | -8.62841 | -47.41914 | 2026-09-11 03:47:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7019835-2152-3516-87e2-9666188c6810 | -7.00764 | -43.86991 | 2026-09-11 03:47:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f54590c5-8f85-3ecb-83ea-ab518a8996e8 | -7.80636 | -42.77486 | 2026-09-11 03:47:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d02ffdbf-fd20-3c9b-b0a9-0f764be6f8a1 | -7.4646 | -46.14267 | 2026-09-11 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b535ad4d-ccdc-3eee-b334-d4156b493abc | -8.3892 | -46.29938 | 2026-09-11 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c3d130d0-a5d7-313d-91bf-5c1307e3267f | -9.53715 | -45.45903 | 2026-09-11 03:47:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8236d1f1-e28f-378f-95a3-b9d0feba70e1 | -8.27866 | -47.78839 | 2026-09-11 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0287dfba-cb08-34db-a82b-37aea4fab0ec | -8.91068 | -37.36155 | 2026-09-11 03:47:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 70795316-c75b-35de-aa3f-4cba69386148 | -9.31393 | -44.35963 | 2026-09-11 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fd99440-a622-36da-9f36-93d0ab84f80f | -7.81154 | -42.77591 | 2026-09-11 03:47:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 27b004b4-906f-3c4a-b8ed-596a2d484041 | -9.77334 | -43.44054 | 2026-09-11 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2bc61e4c-93d0-37d8-bb17-36e786c081f2 | -8.03307 | -43.84732 | 2026-09-11 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 79d8a42d-f7f4-39ad-b0ba-a787cb234234 | -9.31119 | -44.3582 | 2026-09-11 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57a254c5-410a-356f-9aae-bd2d8dce3d1e | -8.48702 | -44.739 | 2026-09-11 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 430c8b7e-02e6-3cb2-8713-a6767640ce45 | -9.74424 | -41.96629 | 2026-09-11 03:47:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 19dad407-8e73-3881-bef0-136d35b0daf5 | -3.32212 | -42.29546 | 2026-09-11 03:47:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e5fc69e0-7921-3aeb-a8e1-728892aafb70 | -6.70141 | -45.4776 | 2026-09-11 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0295afa-362a-3646-a287-7e1c8e6d7edb | -7.02764 | -45.10814 | 2026-09-11 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a2e66bf-32ae-3f48-8f08-9679088f674d | -14.91531 | -44.67276 | 2026-09-11 03:49:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef5378ae-0183-38b8-b817-10a5bc848623 | -14.67184 | -44.13182 | 2026-09-11 03:49:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 583a5eb2-0079-3198-8bdf-b3676ba12dd0 | -5.48337 | -45.13236 | 2026-09-11 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcd248e3-2298-3b00-824c-aa494ddecdc0 | -5.20001 | -45.55901 | 2026-09-11 03:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 34dbed87-e23e-3889-92e4-a302d041a413 | -10.97959 | -47.89264 | 2026-09-11 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75edef3b-837e-3a4a-8c3a-876263e70543 | -10.77714 | -45.93369 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f77aff9-09b1-3cfb-88ab-a966000618ca | -11.4126 | -43.94973 | 2026-09-11 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce51b658-a992-3019-8430-735547c4cc73 | -14.89456 | -41.69926 | 2026-09-11 03:49:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4da4e1a7-5cec-3fbc-87c2-e4dcd1477438 | -13.77411 | -43.64261 | 2026-09-11 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0630670b-80ae-3c7a-a6c9-4abbcbc51dae | -5.42129 | -41.84738 | 2026-09-11 03:49:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96de9620-c3b9-3a3a-8d57-132d6ec723cd | -13.54962 | -44.1696 | 2026-09-11 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 275ea746-c9f0-3cdc-8892-480fbd44cdb9 | -11.40267 | -43.94431 | 2026-09-11 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fede92c-b26a-3467-aa62-a6319e051ed1 | -10.77109 | -45.93244 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37a591f2-f4fe-31ec-be76-5d0693bc671b | -5.20648 | -45.5603 | 2026-09-11 03:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b4fd3af3-d005-3bd5-8579-e7a448d2d038 | -10.4895 | -48.65733 | 2026-09-11 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c70b4c68-f071-3a92-ba86-655f714d41ae | -13.5051 | -44.06906 | 2026-09-11 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5a4702e-99eb-3055-abb7-326e5ca75f18 | -10.78226 | -45.93957 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f1e3b5f7-9164-3bbf-9fc7-9f6cf47587bf | -10.74884 | -45.91785 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b6063ba-7ef1-31b6-a045-7f0fdfca8ea9 | -5.48432 | -45.12706 | 2026-09-11 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1d5aed3-6f7f-3507-897e-173815c1ccc6 | -13.76916 | -43.64159 | 2026-09-11 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be8290f5-3424-3f72-afbd-97d1c89da0be | -14.91014 | -44.6716 | 2026-09-11 03:49:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14f75730-7893-31bc-9719-9441c198be22 | -10.77624 | -45.93823 | 2026-09-11 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e02868fe-bd67-30d0-b485-cc715486f0a2 | -14.65495 | -44.12167 | 2026-09-11 03:49:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README9.md)
