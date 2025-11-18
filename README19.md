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
| ca7abb88-cace-337a-b367-c8de3f7eb07a | -7.92225 | -42.77303 | 2025-11-18 03:29:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ed57f03b-cbd0-34e7-96e9-96cd6c0419c5 | -10.24038 | -36.2924 | 2025-11-18 03:29:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| e20bd09b-24c6-3b19-82da-5db444104994 | -7.57255 | -46.29824 | 2025-11-18 03:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e662add-2214-3a12-a15e-de50a70551a0 | -6.73642 | -35.11933 | 2025-11-18 03:29:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 87d384aa-e538-3189-b895-4070efb8e3f5 | -6.93253 | -41.53978 | 2025-11-18 03:29:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 157608cc-8f33-3d49-911f-8e238c0c3f1a | -10.51487 | -43.96967 | 2025-11-18 03:29:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 108db175-4151-3121-9c17-1af66147099c | -6.81606 | -39.13696 | 2025-11-18 03:29:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 549b0bfe-b96d-3192-a102-dc2f28a74b6f | -6.72583 | -35.21836 | 2025-11-18 03:29:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 06a955f4-285f-32f8-bc57-d5a668750fae | -10.86459 | -44.08822 | 2025-11-18 03:29:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4fb68be-84ae-3a28-91b5-06b493614d2e | -8.18959 | -39.34317 | 2025-11-18 03:29:00 | NOAA-20 | TERRA NOVA | PERNAMBUCO | Brasil | 2615201 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8bc70c59-e4a6-3dc2-b84b-7079014c14c2 | -8.63818 | -45.49322 | 2025-11-18 03:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cb2639d-eb14-3778-9615-b38f251310ba | -8.79382 | -44.39523 | 2025-11-18 03:29:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 15b18a4a-f7e0-3122-83f7-95470cbf47b6 | -10.51068 | -43.95971 | 2025-11-18 03:29:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62715674-0978-30e0-be13-d988b4139775 | -7.4215 | -42.76235 | 2025-11-18 03:29:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dd9087c5-82e7-390e-b53e-edfe19b2c8ba | -4.195 | -44.2247 | 2025-11-18 03:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| cc8b595c-3fe3-37b4-8b52-5cd02e4ad68c | -4.1762 | -44.2486 | 2025-11-18 03:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 581d2594-24e7-3bcb-95e6-a32bf56aaed1 | -4.1949 | -44.2476 | 2025-11-18 03:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 7a57737c-4685-3085-beb6-651fff5033f4 | -9.3969 | -48.4523 | 2025-11-18 03:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| a79b567a-5edf-38d6-8853-95ad3fa531c6 | -4.1764 | -44.2257 | 2025-11-18 03:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 6cdae0ac-3e75-3f24-a386-e2245e0bf861 | -15.47424 | -43.18267 | 2025-11-18 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8a96b76a-2497-33ba-a055-0134ffc15007 | -15.52371 | -43.37107 | 2025-11-18 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5964d5e2-30c2-3a92-aa09-bd6ba71cfc92 | -17.68284 | -39.2145 | 2025-11-18 03:32:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4d54af22-85b8-3b4c-9c32-31d49fda8742 | -12.69941 | -46.77848 | 2025-11-18 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c63d428d-be89-3802-8c8d-b6474fc6ae62 | -10.84657 | -44.8859 | 2025-11-18 03:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6be2c488-10e7-3224-bab7-377b5b87c7fb | -15.50259 | -41.53619 | 2025-11-18 03:32:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e04ecf95-33a1-3359-93af-80815c6b1c25 | -13.25924 | -42.52946 | 2025-11-18 03:32:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f9a329af-1b8f-3db8-bacf-4884fb463dd5 | -12.74627 | -45.43625 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e85768b9-87ab-366a-a0db-16c1dd031bea | -12.68964 | -46.78249 | 2025-11-18 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6ee03d48-a85e-3f27-b87f-445a03465616 | -14.21388 | -39.76976 | 2025-11-18 03:32:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7b2a0ba9-4193-3447-bbc1-aa973ca44d2f | -12.74728 | -45.39962 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65e99900-7a8c-3811-9128-fa987f9395b3 | -10.85688 | -44.89899 | 2025-11-18 03:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 773f98ab-0cd2-3749-8467-fba8eb76480f | -12.86151 | -46.05412 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41721f60-6403-370f-8b32-1af535b60abf | -12.84912 | -41.49435 | 2025-11-18 03:32:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b1f3b7c3-dcea-310b-b3cf-452e8a0253e3 | -12.85747 | -41.47664 | 2025-11-18 03:32:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 95a40999-50f0-37b2-bae2-581fae9d4709 | -17.68861 | -39.2115 | 2025-11-18 03:32:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7a870525-7dbc-39c7-af8e-ebec4e112ac6 | -12.64333 | -43.44852 | 2025-11-18 03:32:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6d47b77-a07a-3316-9cbb-86dd2060d766 | -15.46006 | -39.2367 | 2025-11-18 03:32:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c9b6798b-8f30-312a-9bad-cb90e6b84ea2 | -11.39846 | -43.31836 | 2025-11-18 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ceac2bc-7664-3776-b6ef-edd3291e24bd | -15.50164 | -41.54122 | 2025-11-18 03:32:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 97688a0a-6cc4-3b36-a06c-d2c097b02d5b | -11.66229 | -44.74103 | 2025-11-18 03:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 966b261c-54c8-3f8e-bdf5-a5da4f398e28 | -15.47488 | -43.17944 | 2025-11-18 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a34fd6f0-19f8-3a3c-8d01-3f364f60cc08 | -10.84032 | -44.88477 | 2025-11-18 03:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8e428dd-1f3c-3169-8094-ec32a61b931f | -12.73288 | -45.43826 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 43a7df0e-d82c-33d7-b0cc-b50d1d2598cd | -13.83971 | -41.79499 | 2025-11-18 03:32:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 35390294-1061-31b7-8e03-6a7bfa85aa14 | -13.33436 | -43.18736 | 2025-11-18 03:32:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e4888e3b-ed23-3b71-a167-2acdad557c22 | -17.88493 | -40.11547 | 2025-11-18 03:32:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7546a69c-511e-3eaf-bf25-8bf4aa81d175 | -12.86254 | -46.04912 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6479560b-685f-3a90-a060-6f93e5741ec6 | -11.92794 | -44.8095 | 2025-11-18 03:32:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41209708-2f37-3257-b7da-70806530e83f | -12.75345 | -45.43288 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 907d4866-d7a4-3513-9297-a0a3218c6cdb | -11.43273 | -43.3214 | 2025-11-18 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| fc4b2f6a-d733-3c42-824f-250e100db717 | -12.86244 | -46.04996 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 64d71ab1-8ec8-3c5b-b1be-d6152e5c84ab | -10.85793 | -44.89378 | 2025-11-18 03:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e11ea1e6-2c0a-3802-98db-f5e3e3a68728 | -10.84208 | -44.88717 | 2025-11-18 03:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 118b9217-5d8f-3a04-8223-a0250eebec47 | -15.5097 | -41.53978 | 2025-11-18 03:32:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b4c7597d-6874-3e13-aa50-291025172488 | -12.71106 | -45.38686 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0162278c-2ae8-3852-ac16-4f2ad0a5d632 | -12.69765 | -46.77781 | 2025-11-18 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 77f6a64c-a2b3-33bc-900c-96625c0433ec | -12.73389 | -45.43334 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a4c72532-5404-3a9c-b452-64e5cb3ee0a4 | -13.83727 | -41.79686 | 2025-11-18 03:32:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1fff9552-6ef9-3b27-ae8a-75b01382ad49 | -12.87059 | -43.59397 | 2025-11-18 03:32:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| add7f3ed-9a4a-31b6-aa34-b5718c8c236d | -12.69633 | -46.7841 | 2025-11-18 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a1cf5f30-12e5-30a1-a89f-b12d90255e8d | -11.39212 | -43.32105 | 2025-11-18 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0257742d-9798-3cee-9237-61fd52ee4cbb | -12.70205 | -46.7989 | 2025-11-18 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ffba49f7-f397-3469-8991-a57eac688480 | -12.72139 | -45.39952 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 926dc75e-d5fc-3dba-92e1-85aa8ed0ed4c | -11.39137 | -43.32488 | 2025-11-18 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34b86d89-d696-38dd-b576-7229ed737dde | -11.69127 | -44.72266 | 2025-11-18 03:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 338f0b52-e223-3df5-ac52-1935ec428add | -12.73489 | -45.42845 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 30a58353-a485-305d-a485-03ed38a9ec10 | -15.46973 | -43.17835 | 2025-11-18 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8f43d139-7ed9-3df7-a24d-408ea9de992d | -15.50051 | -41.53761 | 2025-11-18 03:32:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cf71c6f9-0904-3f2f-954c-11111d84824e | -12.73908 | -45.43969 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 491c9641-cb77-399a-851a-748783c86102 | -11.61285 | -43.90676 | 2025-11-18 03:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 032f4152-3101-3ecd-986c-ebb6815ab4a4 | -12.70039 | -46.79832 | 2025-11-18 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c459dbb-253e-3dd3-a5d9-f64432fc312d | -13.53261 | -43.01348 | 2025-11-18 03:32:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 16945e93-5186-3f34-996f-4bfa63f405fd | -12.12253 | -39.74724 | 2025-11-18 03:32:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 96383551-dc16-3330-b371-80beee7d7140 | -12.71623 | -45.39315 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac48df57-ff79-38ae-9ca8-d163ae850b8a | -17.68383 | -39.21576 | 2025-11-18 03:32:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 81400f0d-05f7-3797-a28f-d939835b1b8a | -10.84306 | -44.8821 | 2025-11-18 03:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7813ed95-b6f9-3ce5-9ea5-fce4b20a2c05 | -15.50718 | -41.53731 | 2025-11-18 03:32:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b60ffa6c-897f-3781-a45f-dd22cad01a97 | -11.68616 | -44.71666 | 2025-11-18 03:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 489697d0-9557-3ff6-9d7a-637a7e1aeb57 | -12.85635 | -41.4826 | 2025-11-18 03:32:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| c153cc54-9500-3f02-ad76-dd2896119f22 | -11.61368 | -43.90258 | 2025-11-18 03:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29594372-ff8a-3eef-99c8-f764e21f7592 | -11.8829 | -44.20996 | 2025-11-18 03:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41e833fd-73a7-3eda-9228-3f6732781664 | -12.74107 | -45.42995 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1381c4c1-75ac-3dc5-9f42-aed02177076b | -12.74106 | -45.39838 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1380158e-7c0d-36c8-81c8-4cae520d09eb | -12.69907 | -46.80464 | 2025-11-18 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1827eebc-fbb2-3c32-b5e4-9f2eb464510c | -12.69095 | -46.77623 | 2025-11-18 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1099a1c0-59d0-3f32-96f1-c5cabb736af8 | -12.71523 | -45.39802 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7e88b5b2-fe6b-33a2-896f-39e5b80a7463 | -11.42714 | -43.32026 | 2025-11-18 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aeac1402-cb1b-3da8-97db-1f7899d1faf6 | -12.74008 | -45.4348 | 2025-11-18 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a0db8de1-7fc9-39de-b08c-c838b3ede18b | -12.69271 | -46.77694 | 2025-11-18 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 84c5f596-107c-3d88-ba0a-c3638e195a9c | -12.86506 | -43.59276 | 2025-11-18 03:32:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 463c4ac6-cd3f-32f2-be5f-471b9e39b529 | -12.86096 | -41.48476 | 2025-11-18 03:32:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| abc2a548-410a-39ad-b31a-dfc1a18d41bd | -13.33366 | -43.19086 | 2025-11-18 03:32:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5eb12eb6-beac-32aa-affa-5e3241f61a35 | -15.50512 | -41.53867 | 2025-11-18 03:32:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a4ae1cd9-6576-351a-90be-ac28d659a11d | -17.69055 | -39.21604 | 2025-11-18 03:32:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c3c2abcb-a5e3-399a-bf36-d25a1def0a5b | -11.57231 | -42.4208 | 2025-11-18 03:32:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57bfb27a-56b5-316e-b278-84fe9fc3df13 | -12.69136 | -46.78319 | 2025-11-18 03:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 91ecef11-4d2a-3691-9ecd-280f81f12a3c | -11.39771 | -43.32219 | 2025-11-18 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93dee435-631a-3413-9cff-e4847b26ef06 | -12.17357 | -43.46229 | 2025-11-18 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5e72f45-4d33-34a4-995f-afea1765b52f | -15.88984 | -42.17422 | 2025-11-18 03:32:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5aff0c55-9220-37af-9c4c-ab22cab6ce52 | -12.85972 | -41.49136 | 2025-11-18 03:32:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |


[Clique aqui para ver as próximas entradas](README20.md)
