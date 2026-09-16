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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a356ca9-f5d6-3e12-af21-6eac1b00cdb2 | -11.61396 | -47.29665 | 2026-09-16 11:08:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 8f7b83ee-d9af-37ef-9083-ad171d4f9724 | -13.98567 | -42.71516 | 2026-09-16 11:08:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 41410355-6893-3f3e-a2dd-d8ddb0cd216c | -14.14036 | -42.12427 | 2026-09-16 11:08:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 33.9 |
| 776d3047-5d31-3ed9-bae8-711da0a32891 | -11.79531 | -46.5923 | 2026-09-16 11:08:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| c423f296-abb1-37a1-8ec3-2fecf55cd0a0 | -10.60298 | -40.94331 | 2026-09-16 11:08:00 | TERRA_M-M | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 5793d46e-5363-3cfc-8e19-bfe5132504d9 | -11.36625 | -43.94852 | 2026-09-16 11:08:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 159bd2f9-1ff7-3337-ab2d-eb19d88504c0 | -11.83483 | -37.57644 | 2026-09-16 11:08:00 | TERRA_M-M | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 2e54f759-7c53-380a-9fe3-31ddaa324201 | -11.84292 | -37.58407 | 2026-09-16 11:08:00 | TERRA_M-M | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 53a7d05a-60cc-3398-8a86-cc298a34a759 | -11.61026 | -47.31795 | 2026-09-16 11:08:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 025b1b8f-7bbd-3626-86bb-cc59e01a5c9f | -11.36879 | -43.93292 | 2026-09-16 11:08:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9cb1bbc3-639b-3ea5-9c35-3292a204e76b | -11.89291 | -43.83009 | 2026-09-16 11:08:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 0dd2b5b1-e3f1-31cb-9e98-55a5ffe1e708 | -15.27411 | -42.80809 | 2026-09-16 11:08:00 | TERRA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 36b36ed4-c601-3a1b-8923-ad78f07b578c | -8.85559 | -44.89022 | 2026-09-16 11:08:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e796fd12-28b3-3f0b-b099-f9cd62bd17ca | -14.61874 | -44.30545 | 2026-09-16 11:08:00 | TERRA_M-M | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 3c1a0e47-932d-3d1c-99d0-3dda5374a742 | -11.83059 | -39.17817 | 2026-09-16 11:08:00 | TERRA_M-M | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 3c7a1611-1ae8-3a72-8a73-40907b5ffc37 | -10.08479 | -39.50554 | 2026-09-16 11:08:00 | TERRA_M-M | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 29aa2027-d497-3c1f-b86f-aba50b7dce78 | -13.63736 | -45.97213 | 2026-09-16 11:08:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 61e83761-03dc-3d92-a30f-6d6b5088da79 | -14.14207 | -42.11334 | 2026-09-16 11:08:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 2aa2a646-3cce-3ecc-9cb2-f1aaeb636502 | -10.51176 | -36.95262 | 2026-09-16 11:08:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 278af1f9-bbd8-3999-ba2c-906d3b8964d2 | -12.53718 | -47.09796 | 2026-09-16 11:08:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| f819a5d1-a138-3431-b201-4bff17ae04b0 | -14.07063 | -40.20751 | 2026-09-16 11:08:00 | TERRA_M-M | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| fb5e4b52-5589-36b0-ada4-d0631aaf44cd | -13.24403 | -41.94818 | 2026-09-16 11:08:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e7ccaed7-ebf8-3731-bd62-442d6ca85792 | -12.36462 | -38.98436 | 2026-09-16 11:08:00 | TERRA_M-M | SÃO GONÇALO DOS CAMPOS | BAHIA | Brasil | 2929305 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 552ed71c-7be5-39cf-ae3a-435be3a50965 | -8.95798 | -44.40724 | 2026-09-16 11:08:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c4a083eb-ee29-360c-ae31-9556847fc959 | -14.62107 | -44.29082 | 2026-09-16 11:08:00 | TERRA_M-M | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 6fdc3bf3-cb90-3023-9479-02cce652aaff | -8.96078 | -44.38934 | 2026-09-16 11:08:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 358f39bf-1168-37a5-8a34-151745f221f2 | -10.06261 | -39.59567 | 2026-09-16 11:08:00 | TERRA_M-M | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 71e2a1b0-5360-3483-8927-872487238fa9 | -11.8442 | -37.57466 | 2026-09-16 11:08:00 | TERRA_M-M | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| e0dffd54-0723-3e90-8c79-2013a56bb5b8 | -14.62155 | -44.29698 | 2026-09-16 11:08:00 | TERRA_M-M | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 472b1be6-a521-3183-8381-3ac693c22642 | -10.8492 | -46.1998 | 2026-09-16 11:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 44d9d8cc-f853-3519-8773-26c89f9eaba1 | -17.28567 | -39.78037 | 2026-09-16 11:10:00 | TERRA_M-M | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f1e501fa-d5b0-3218-b446-4ba894a901e3 | -17.5974 | -40.18132 | 2026-09-16 11:10:00 | TERRA_M-M | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 6f44bbe6-e54d-363c-bd30-79dd8de8b958 | -17.59871 | -40.17211 | 2026-09-16 11:10:00 | TERRA_M-M | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 8e987502-1bc7-3237-af3b-7c604002b2b1 | -10.9046 | -46.3056 | 2026-09-16 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 13c68adb-e215-35c2-bc80-51818a244331 | -10.905 | -46.283 | 2026-09-16 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 29ea416e-23ca-3b1a-b0c8-46385279dee4 | -10.905 | -46.283 | 2026-09-16 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| ceb4f90f-5931-35e3-bd56-b09857921017 | -10.9046 | -46.3056 | 2026-09-16 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 2a9d04c0-f55e-32d0-acb5-2665f25f4184 | -10.8492 | -46.1998 | 2026-09-16 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| a8843509-09a4-33cd-8016-dcb78ccdd710 | -10.905 | -46.283 | 2026-09-16 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| f0b0ed3a-0b34-317c-80ce-b0b16e7274e9 | -10.7726 | -46.2322 | 2026-09-16 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 00110324-2d14-3728-be2a-338610ad3c42 | -10.9046 | -46.3056 | 2026-09-16 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 0b6fd48e-84a3-35ba-b9da-05c43510f112 | -10.0982 | -45.6141 | 2026-09-16 11:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| aba68e8c-cb4e-3e95-afed-8e262099ffdd | -10.8301 | -46.2022 | 2026-09-16 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 72ed53ac-8e10-3afa-a985-087a87740e00 | -10.8492 | -46.1998 | 2026-09-16 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 2914851d-877c-3593-90fb-5cc0e4d79b20 | -8.5617 | -44.5112 | 2026-09-16 11:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 7e086c0a-ded6-3cb8-b70c-53e00c6f4dcb | -10.8495 | -46.1771 | 2026-09-16 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 28c70d01-5fb5-3f66-b0d9-9aba3b1de388 | -8.5428 | -44.5132 | 2026-09-16 11:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| a676aa97-00b7-3402-9924-869ca354f28c | -11.6123 | -47.313 | 2026-09-16 11:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| fcf3e0c3-62f1-38aa-95dc-88a2ce8ba6e2 | -10.8305 | -46.1796 | 2026-09-16 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 39811587-ba4b-324d-81b8-5f192dd9f371 | -10.0982 | -45.6141 | 2026-09-16 12:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 8338c999-be0c-3133-9e7b-617c93721fc3 | -5.6311 | -51.6858 | 2026-09-16 12:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| bb721aa6-8c21-3344-b8a2-bd3bcb4c11aa | -10.8492 | -46.1998 | 2026-09-16 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 6f2596c2-05e3-3a54-83a7-f30660d0147c | -11.5932 | -47.3155 | 2026-09-16 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 98912e91-7321-39e6-8589-0dcd0a6825ef | -10.8305 | -46.1796 | 2026-09-16 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4c9b8ce5-e1a3-3017-b5bb-7cdd20eea077 | -11.6123 | -47.313 | 2026-09-16 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 1bd5b442-989f-3930-b252-7d3b31f59182 | -8.5428 | -44.5132 | 2026-09-16 12:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| e27ffbe9-0727-3556-8bc7-7508cede4ac7 | -10.8495 | -46.1771 | 2026-09-16 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 3ab23312-dc39-39fd-a9d9-7d12ec75d088 | -11.6123 | -47.313 | 2026-09-16 12:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| fed90e23-e295-34d6-bf6a-b3e79e05df10 | -11.5932 | -47.3155 | 2026-09-16 12:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7dce804c-ea88-3fb5-940e-864608f7a89b | -10.1179 | -45.5662 | 2026-09-16 12:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| db3a508f-e61d-3dbb-bcf9-525a7f6a9423 | -8.5428 | -44.5132 | 2026-09-16 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| dbf29e85-69fc-35df-b26b-e013c573ef10 | -6.8032 | -59.1693 | 2026-09-16 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e0c535c0-b72a-3f1c-ab5b-dd2055aaa244 | -10.8492 | -46.1998 | 2026-09-16 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9368cab1-41fe-3cd6-a576-8d5bcc829cea | -6.7892 | -48.6563 | 2026-09-16 12:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 2fe4041d-91c0-3b28-b848-4715b437a7f2 | -10.1175 | -45.589 | 2026-09-16 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| bc792b29-b00d-31f1-8d88-ee4c5e7d277f | -13.2239 | -51.6318 | 2026-09-16 12:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9da66a3e-d050-3761-bbf5-b108c50aa9a7 | -5.6311 | -51.6858 | 2026-09-16 12:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 8e84032a-8483-3816-b067-b35a6564a58c | -10.0982 | -45.6141 | 2026-09-16 12:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f090c1d5-a4cb-3503-9eef-3507c146130c | -10.1175 | -45.589 | 2026-09-16 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 94b47367-7734-330b-941a-651271db2bb8 | -8.5617 | -44.5112 | 2026-09-16 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ebdc0476-6eaa-3a56-9cb1-45e185dcff5a | -7.3561 | -44.4956 | 2026-09-16 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 6c7c624a-a4bf-3d67-8a7f-35f2c63c6808 | -6.8032 | -59.1693 | 2026-09-16 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 6292dcc3-02c0-3686-8b2b-0e004d18d553 | -8.5428 | -44.5132 | 2026-09-16 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| eb5e1d78-7334-300f-a0e9-4d52278a5fe8 | -10.8495 | -46.1771 | 2026-09-16 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 7cac06a2-8f5f-341b-a435-1f3c766440e4 | -6.7892 | -48.6563 | 2026-09-16 12:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 81.2 |
| f3468cdc-0e57-300c-a652-2da68003ba31 | -10.8492 | -46.1998 | 2026-09-16 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 127b7ea6-0a32-3fd2-9fe4-f3ac8c944062 | -13.2047 | -51.6342 | 2026-09-16 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 6ea48d81-98fe-3946-884c-aebe68e89402 | -13.2239 | -51.6318 | 2026-09-16 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 266ab4ec-7fe0-3fd6-b669-f586c593e286 | -10.0982 | -45.6141 | 2026-09-16 12:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 265.8 |
| 6f461e8c-5d51-3067-91b5-c547740e5609 | -13.2047 | -51.6342 | 2026-09-16 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 24522e92-8d4d-3a7e-90de-80531a6c8c95 | -13.6337 | -45.9732 | 2026-09-16 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 3e440936-17cc-3892-87e1-a40a635ab488 | -8.5428 | -44.5132 | 2026-09-16 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 6dd262df-d2e1-30e5-bf1c-2ddecd539b30 | -13.2239 | -51.6318 | 2026-09-16 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 67746089-46d4-34a9-9cdf-ef6635a9a9f0 | -8.5617 | -44.5112 | 2026-09-16 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 1e73e152-e764-38f1-8126-7d4b63fd7319 | -10.8495 | -46.1771 | 2026-09-16 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a2d98149-3bf2-3eeb-a46b-2217cb957203 | -8.8588 | -44.8919 | 2026-09-16 12:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 730a0b95-c425-3ea2-871e-6b6adf5a2cf5 | -7.3561 | -44.4956 | 2026-09-16 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 29381e2d-ad06-329d-8def-40327a9616b9 | -6.8032 | -59.1693 | 2026-09-16 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 9e8fddee-d7b6-3bf7-b8e9-350c5958d2fa | -8.8585 | -44.9149 | 2026-09-16 12:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| fdb6c0e9-2bdf-3b51-a297-543ac73093ad | -6.7892 | -48.6563 | 2026-09-16 12:30:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 20b4674e-3b16-3b00-9a7d-2af9652a2f3f | -13.1855 | -51.6365 | 2026-09-16 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 170.3 |
| ce2bff93-b321-314e-a3e1-8ad61d582d40 | -10.8492 | -46.1998 | 2026-09-16 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 42889815-94e5-3db1-ab16-78cbe60c04ba | -11.5432 | -46.8745 | 2026-09-16 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 45ba0115-c22e-3e3a-9232-b12f38711aeb | -7.0454 | -42.0427 | 2026-09-16 12:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| 1f5b8c13-7f3d-3423-b1cc-0c4a4585b0b9 | -8.5431 | -44.4902 | 2026-09-16 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| bf16771f-0d00-3bc9-8baf-626326a6c0fa | -13.2047 | -51.6342 | 2026-09-16 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 200.4 |
| def4daba-e4b6-3bcd-97fd-f929ecc1337b | -8.8588 | -44.8919 | 2026-09-16 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 418329fb-ef94-36ef-946e-94c407268936 | -11.417 | -51.416 | 2026-09-16 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| cbde2912-1eb6-34e6-840e-e8cc502eea41 | -6.7892 | -48.6563 | 2026-09-16 12:40:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 95.4 |
| dc992c1d-64ec-336d-b893-9442f98aea62 | -13.2239 | -51.6318 | 2026-09-16 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |


[Clique aqui para ver as próximas entradas](README69.md)
