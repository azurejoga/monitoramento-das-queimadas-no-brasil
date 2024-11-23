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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc059541-bbd0-36e7-90a0-19dab7ffeab8 | -2.68234 | -46.0886 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41ac92d7-1a55-390e-8908-9084a9f351cb | -1.96808 | -47.83466 | 2024-11-23 04:16:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b4b2d15f-1532-3560-a7c9-834a0fe7ddf3 | -2.82345 | -45.15915 | 2024-11-23 04:16:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 703698bd-1832-33d9-886d-4d67b1cc321e | -2.69083 | -46.19182 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13304782-0295-3b0a-838a-ff34051e75cb | -2.71927 | -46.10219 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 557a8ba6-78e9-3474-8439-43a16abdfb76 | -2.27856 | -47.71202 | 2024-11-23 04:16:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e4b626b-e13a-3ff5-8133-86284d701e87 | -2.7054 | -46.09998 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8d0c0b0-fa92-3891-8d90-2af9f21702cd | -2.66011 | -46.25016 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dec287dc-b145-328b-b573-7cbad94102a8 | -2.63755 | -46.23467 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f00a6b0-d216-3eaf-b587-28d87ee9ba1e | -1.60324 | -52.58321 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48763377-a68b-36a6-9d8b-db0dcae1b4bc | -3.1804 | -46.55217 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdc6bbad-b35c-3337-8f32-75bd2d431aca | -2.66157 | -46.60508 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99d21e1d-80ff-3423-bdf7-2088bae20ffe | -1.25331 | -53.36304 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f57017e1-e0ae-3f83-bcf2-602a040ac1f8 | -2.62896 | -46.22143 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 592bffd4-86b0-31f7-8074-b9bcfe5c0060 | -3.847 | -42.47601 | 2024-11-23 04:16:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5cc57ba3-a68d-3381-a382-3cbf1f077ca9 | -2.50378 | -46.22658 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89fee174-bdbe-36ef-a118-85f75533fd8d | -2.58066 | -46.54308 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5294e354-292e-3b48-897c-c85d998c1ea3 | -1.50362 | -52.04137 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95e31e98-e552-3d98-93ec-921ae987f6cc | -1.31003 | -51.75136 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bd113a1-c7e1-3061-854d-e3bdf609a3d2 | -3.14398 | -44.48772 | 2024-11-23 04:16:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ca60c45-df66-336d-ad18-331b1e4c8d12 | -2.4467 | -46.54403 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71a323ab-2d8a-388d-878c-bdc62a0568b7 | -1.78082 | -53.62883 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2616beab-953c-3404-b85e-46104d721cae | -2.68043 | -46.25738 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7f49e52-a8b2-372e-a3bd-73c4364647a3 | -1.24826 | -51.75027 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3c8483e-3c7f-3594-876b-4074dac11a76 | -2.73677 | -47.54296 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c40e7a5b-5376-3a19-b37f-d4ded3a3132a | -1.21351 | -51.74158 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37432ff2-738f-3669-a44a-4649da29a696 | -1.22514 | -51.79741 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 775ae101-1116-39e1-a1ff-3266b8a3612b | 0.15712 | -51.23265 | 2024-11-23 04:16:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bde9fb48-7e9e-3582-9710-1a8f72d19c9a | -1.10832 | -53.39612 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a4c77eb5-d68c-34b4-9c3a-48ff698e31da | -1.7156 | -52.49158 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97e16152-68ce-3794-a933-9aac8f56adfa | -3.95375 | -46.72401 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e3e33d0-2161-3efe-b8ce-49e8a65b7ee7 | -5.96901 | -46.30258 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d89007f8-a86c-3ce9-88a8-4bd0863152a5 | -4.74094 | -46.89706 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d2ac367-3e8b-3da3-8a6f-12c8049e01d6 | -3.83023 | -52.25487 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c5f2ff-5099-3e13-a720-75520a3a4c25 | -5.46958 | -43.24026 | 2024-11-23 04:18:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a14f14a4-0849-3f64-b079-a8970ba42dd2 | -4.35888 | -43.8919 | 2024-11-23 04:18:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20d588bb-0fc7-3d03-ba1c-c823085a9974 | -3.21405 | -51.42229 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4d4532bc-202b-30bd-b60a-50775b59f503 | -9.73054 | -37.02904 | 2024-11-23 04:18:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2cb4c3a1-bd0e-3e95-b6c0-e17582637b0f | -4.70524 | -45.84974 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7a71a16-2c64-30e8-82e2-48d5af70def7 | -5.57096 | -50.9506 | 2024-11-23 04:18:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c7f474b5-bad0-3aff-912c-eb222efa0b63 | -4.60231 | -46.49532 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| f6f08cad-46cb-3a33-9d5d-915be4c93200 | -3.10926 | -51.20035 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34bb615e-3fcb-3a32-a974-0be499434e46 | -5.94236 | -46.18597 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb7eabce-cf34-318a-b903-04476745206b | -6.49653 | -47.0395 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 533c14be-ebe2-3485-b4ec-a8d874cff852 | -2.15922 | -53.7828 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a389c94e-8c6e-3bd2-abca-44dd2f981028 | -3.80733 | -51.33833 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2ad173a3-550d-3efb-8398-1186762d695f | -3.93724 | -48.14748 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cae77572-5f22-38bb-91ca-12aa57eef3e9 | -3.80875 | -48.96907 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4421980a-4484-38cc-a33e-d4db21f23597 | -5.5629 | -43.7289 | 2024-11-23 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd97172f-0b38-317c-b8b5-5783d2e7660b | -4.04049 | -49.28191 | 2024-11-23 04:18:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4d012e1-437a-37e3-a422-5c83548aec8e | -3.22072 | -53.9385 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad4c30f1-1833-36b0-9df7-84e4109acdab | -4.1264 | -50.00331 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1976c47-4d4e-3b44-86ac-704986d0d9fc | -4.60638 | -46.49208 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b447178-3d4a-35ce-9aee-9be5e368a07b | -4.65803 | -45.6796 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15c4fb4f-657e-33d5-9fa0-4cfa23b23b99 | -3.89506 | -47.93215 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc2becf5-b9c5-3c3e-8e2d-f626c96b5bac | -7.21481 | -47.06111 | 2024-11-23 04:18:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e35e9d74-f464-3799-9134-64464164ee19 | -4.112 | -45.87662 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6fd3bd52-292c-3d38-b4c2-598a38d24ce7 | -6.33058 | -46.03532 | 2024-11-23 04:18:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d6f52310-3cfe-3d39-871d-380f46b71f81 | -6.30602 | -44.88073 | 2024-11-23 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a396c1a-8013-3f10-9000-936bca097326 | -4.10379 | -48.9174 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff92e052-39ff-3355-ac39-40adf2b8d246 | -2.68348 | -52.07605 | 2024-11-23 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 64c6f416-5232-334a-a10e-a1c072475cce | -6.14551 | -46.68752 | 2024-11-23 04:18:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ddb08ae-e02f-397f-a717-ca2d923fada6 | -6.29871 | -35.05584 | 2024-11-23 04:18:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 8808420f-05b8-3874-8fb5-96531315f73e | -4.52785 | -42.92088 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be62d9bf-9897-3d75-8a6a-33658518b3d5 | -3.66898 | -47.13615 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c27cbb04-ae48-38a3-9f24-4ee690b705b1 | -3.46357 | -48.25211 | 2024-11-23 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c74440c-bff7-35c3-a145-b6861d7ba4f7 | -5.56827 | -46.28789 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f9f9dfee-55af-383b-afe0-8561a5c467f2 | -6.05982 | -44.04887 | 2024-11-23 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0530bab7-156c-38b5-8ea8-65bdac042a04 | -4.57335 | -45.6477 | 2024-11-23 04:18:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3404af37-fe3b-3fee-98a2-c829fe6a0315 | -4.53177 | -46.43341 | 2024-11-23 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9a4c31cf-471b-3a7e-9abb-eb2c9d3c8a92 | -4.97139 | -44.96384 | 2024-11-23 04:18:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddf46544-f39a-35b9-b168-5ccc16b22db9 | -3.79284 | -46.6643 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cef2851-46fe-3823-83f4-30d15f2b64a7 | -2.57636 | -51.88307 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb7b66da-d2ea-345f-85af-3f72440fc5d7 | -4.42531 | -44.11744 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03faeb82-d749-3b71-87da-a2f00bd686b8 | -8.71128 | -44.00807 | 2024-11-23 04:18:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d918756-eda6-3381-beda-6f8295f032af | -5.58524 | -45.20727 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2d59505b-85c3-33dc-aa8d-dfb7b5539844 | -3.25451 | -53.27122 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94718887-6b51-319d-93ea-833309eddf21 | -3.89586 | -46.65538 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e303b89e-70b5-3bf1-a6de-2f09c9fd9b25 | -3.52477 | -53.51576 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c304e6bb-f7d6-30e1-aba9-e10d2b00b9b9 | -4.87398 | -42.70188 | 2024-11-23 04:18:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83c5b26e-9d6a-34bb-af0f-7ce81ebfdaa8 | -4.69112 | -45.8513 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27ee24cc-5315-3aac-9d33-a6296d441a80 | -3.24347 | -54.25719 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97c2d0b5-54a0-35ed-96c9-c0bb1262cc59 | -3.6596 | -51.57811 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ed44c23-c9df-39f0-ab9f-fedbcd40c676 | -4.07142 | -46.84757 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77fb91d4-2be3-3217-bc3a-f19f272f63d5 | -3.82758 | -48.97931 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21fb5e34-dae0-3d1e-b5a1-0715f1ea3b1a | -4.53232 | -42.91426 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ccad6b39-f694-380d-aa5f-3e28efafd420 | -3.24913 | -54.22853 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa0cd8f0-8f7f-38e4-b50f-e7bd907e3df7 | -4.16462 | -46.80891 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21b98edc-b87f-35ab-a82b-20eb734f2548 | -6.49529 | -47.04724 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 543be874-8bc7-302d-a9d2-cec1a4a98909 | -4.53288 | -42.91069 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| de4e2f06-dc08-3076-894c-3ed44a0a17e8 | -3.25284 | -54.24136 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4eb2ed2d-6d90-31f5-ace3-edf0ab62cab6 | -3.95136 | -47.96463 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e41b2034-6e2f-3b47-9ba6-eeb841f10cca | -4.73182 | -44.09208 | 2024-11-23 04:18:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef27ec47-e4cc-3672-bd60-80b10f33dd7a | -6.15423 | -46.67733 | 2024-11-23 04:18:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6049896-d736-3094-a343-705259864c02 | -3.1784 | -54.32625 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef20beb9-dee8-3500-acb3-9bcfbbe74cf7 | -4.25222 | -48.69605 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| b594b568-a67b-33fd-842b-43bc87d2d113 | -5.22146 | -44.90754 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5fcedb62-49f8-3090-9b7d-5941ddc06c30 | -3.21529 | -54.24842 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eebf70d9-7d96-3852-a0e7-15108dc83ceb | -4.41978 | -44.10952 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d693554-3d80-3933-9660-84f4b1b02646 | -4.66196 | -45.67653 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README36.md)
