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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a084915-e8a7-3d9d-b15a-15b61a886a2e | -5.5847 | -51.03992 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 803bfbc3-87fc-3131-9044-701950777475 | -11.65174 | -52.04838 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e6be10fb-cdcd-3a77-944a-784950652321 | -6.49782 | -44.09932 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6012a51f-e75d-3660-b2dc-94279f51c006 | -4.99085 | -56.25306 | 2025-09-03 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34d40294-e6ce-3e51-962b-5521db8d371c | -7.70589 | -48.7296 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 20.2 |
| a83df296-811d-3d8a-921d-0d3de61ae2b3 | -6.83716 | -52.82989 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24adb3c7-35b1-37bf-bd89-e4df65d2491f | -8.4644 | -45.0638 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f223c402-32fc-39b2-9dc6-30984f2ff757 | -5.77052 | -45.39973 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95109d85-d14e-3a77-bd83-dcc0da681ea8 | -8.36699 | -52.53723 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fab46fae-8d0b-36dd-9fa8-0ec988bb7106 | -10.55149 | -50.42138 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b1d4fda-f5c3-344a-936c-6bda548e429a | -11.61926 | -52.06117 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfb0d021-f533-3cfb-82fa-2c3ef2ec7043 | -11.60498 | -52.08764 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d683744-f479-3b99-98bd-6cae4e14e48a | -10.47819 | -53.63607 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 641f10aa-c296-3d7c-ac5b-c9af5f741835 | -6.44405 | -49.53067 | 2025-09-03 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0114ab50-b249-3eda-81f3-13ccd497c328 | -10.75496 | -46.35238 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9353d0f2-3fdc-30b8-8f4a-cf78ba5c1576 | -6.34824 | -43.77181 | 2025-09-03 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eaeca364-d914-3390-8274-54434ba1e936 | -9.63474 | -46.11929 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 05acf9d5-f11f-39f8-804a-05905afad1be | -11.92396 | -46.67323 | 2025-09-03 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f914006-6b0d-36ef-92a2-0e2e01ec06b4 | -5.76361 | -45.29945 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddce3c2a-2958-3fde-a595-8ac542a15519 | -10.88557 | -55.74377 | 2025-09-03 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27fcf542-8649-34f0-aa88-107122aabde6 | -5.89966 | -46.16083 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a754f966-9132-3432-841e-01f6ec22dd52 | -8.46377 | -45.06824 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca52eef0-da29-3dad-8ecf-f4811f952d9c | -9.14256 | -49.65247 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 582a9cea-ae13-30ff-8677-b0c37d92e290 | -5.56606 | -43.08262 | 2025-09-03 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 44c08e9b-f0b4-3f29-a69f-461cf0e5a920 | -5.1069 | -56.97182 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0bbf3ec-2478-30fd-a1d5-3fa4cfce86df | -10.54581 | -50.41294 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4130f119-c891-3278-8393-7eb4c0ae5178 | -9.95575 | -51.62683 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 816528e5-c661-3789-86e5-47cf5b708b17 | -11.67548 | -52.18202 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0a866d5-7c16-393c-9815-20e68ee4a6f9 | -6.79271 | -52.82652 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99d6f349-dd89-3b1d-93df-fc1a3ecc2af9 | -6.22895 | -55.93336 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d07776f-5a77-365d-ac37-b5261a8a1924 | -10.04231 | -56.1039 | 2025-09-03 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ac61fd8-c64a-39b0-bfc9-64f64cd70efd | -5.8159 | -43.22326 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 13a004b0-c4bf-371f-a9f5-90351ea4d055 | -8.09057 | -47.59504 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9683b174-d56f-3d78-a318-6e7d6b0047bd | -7.72743 | -50.24724 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6701eda-b938-33e5-a381-3fe23b158824 | -6.86092 | -52.78907 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7209995f-edbf-3314-acee-f081fc999a2f | -8.88924 | -45.82796 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6da75917-a3f8-314e-a05a-f879517cb538 | -5.90677 | -57.753 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da431950-249b-3703-bdb9-30b86cdebc2d | -5.92622 | -57.71924 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| c8add478-a056-33f6-a5c6-fdb9493395cf | -6.37024 | -43.01014 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 138511cf-3554-3ca1-bc46-9bb6bffd9d7f | -5.8693 | -57.75619 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d5abdf59-0ded-3462-acb7-e2da2a6bf8aa | -6.46631 | -45.40242 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 453f892b-c31f-32d9-b1ee-418af3853447 | -6.83321 | -52.83299 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d965919f-d93c-3898-851f-b8405174ab75 | -6.17937 | -43.30844 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad91af7c-c5f6-3c3d-90c3-dbcdf138788c | -8.85755 | -52.01787 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69f75313-6211-3223-b89d-e5b2f64db286 | -6.22586 | -53.57556 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2178299-9c89-3fa8-843c-7d17be793069 | -10.99445 | -46.83424 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92ea2b36-a948-33b3-afc1-d3cf7ca967bf | -11.60338 | -52.11972 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dc9a6db2-fe8e-382a-bc0d-91a12fde4e2b | -7.71348 | -50.24876 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7c0830ba-1d2a-3ec9-818c-a817782f4ff3 | -6.90113 | -45.5643 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d574257-95df-319d-bb32-3e572c26fa64 | -11.01965 | -51.47513 | 2025-09-03 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fce26dc3-47d6-37a3-94f2-c459e03842b7 | -10.54642 | -50.43194 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04f65744-4a6f-37d5-a2b1-4d4bb15daaba | -5.89929 | -57.74259 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| a6ab2315-a5b9-331b-9048-0923c799900e | -9.70314 | -51.0404 | 2025-09-03 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe2843d2-66e4-3e3f-8c98-c002024b35e8 | -11.62642 | -52.05872 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4026f4fc-baca-3205-b0db-76bdb9eaacae | -11.59568 | -52.12567 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e9434e1d-1aa1-3bf0-aacd-2314351e91fe | -9.79637 | -49.98891 | 2025-09-03 04:46:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7b4f834-0fbd-3737-8b6c-28e48025a5c3 | -11.21027 | -55.06458 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 684621f8-b361-3807-9adc-cf5bdf5b5561 | -8.36677 | -48.29882 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7ffe43f-1813-3f9c-9d08-cccdfe522ac6 | -6.27254 | -43.51498 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3125e436-cbcf-335c-a193-97ab0ce5916e | -6.83767 | -52.84854 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 894e7ad1-f916-3d9f-82ce-351c2920388b | -6.43837 | -58.1255 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb433315-e696-3704-a4eb-c03d241e13d1 | -5.50806 | -42.62754 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 102463aa-c5e2-3325-8769-6ec6ded69504 | -6.78234 | -44.47023 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61bd96cf-4c55-3588-8576-8566a38b90f3 | -10.06166 | -48.08739 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc43e9c9-9cd7-3e59-9fef-3325950f64ea | -6.2296 | -43.39971 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 798168fe-e284-3dde-a739-96347c8768b1 | -5.90154 | -57.75669 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b9ed2f8-2f92-3b39-bba5-f4691ec529a8 | -6.24492 | -42.62082 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aaf92d0c-70a3-3820-bf2b-6dfe4d32643c | -7.53604 | -47.44122 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 797f433b-936c-3398-81ca-483ce814c267 | -11.67439 | -52.18903 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4a41656-be48-3e86-93d5-3a6d0923d4bb | -7.53158 | -47.44525 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 04ac8c51-d384-3020-9ce7-a4a792a4d1fe | -11.61156 | -52.06712 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d8856a6-4dda-3637-88b8-3eb0d54ba976 | -11.67051 | -52.17045 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69ccfc33-d84d-33ad-94e4-fedce7956cc3 | -7.93008 | -46.45236 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c3176b3-85f0-31fb-9999-24fefbdd311e | -6.34898 | -43.76666 | 2025-09-03 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b2f4821-965d-3238-b671-c0e7f895b679 | -6.66987 | -45.90637 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8c48a65-a1be-35b6-a822-dcda98c84b5a | -9.60802 | -55.38747 | 2025-09-03 04:46:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1a1c078-5607-3454-b814-27ebf91d69d7 | -11.59129 | -52.13216 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 97f3dac8-5c8e-3391-afd1-e284544051bd | -7.96864 | -55.29221 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96e2a0e5-9f0b-3770-8e6c-033cba03bfe3 | -11.62039 | -52.07572 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 411125b7-5ed0-3b3c-9b3f-1b151d1476af | -11.91449 | -50.61214 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ed590da-6098-3d95-9bf5-9a7db62f69c8 | -7.69806 | -44.98226 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29ce947e-1581-30de-97a1-252366acef72 | -6.97762 | -43.28185 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5549647a-ccaf-3437-bc3f-051bead03b6c | -10.1525 | -46.27835 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd20552a-7b32-37cc-9871-ba35514f124a | -6.69297 | -44.17577 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2dfdb907-5b73-330d-ba0d-2700c0de5e59 | -8.85875 | -47.92622 | 2025-09-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0c69706-6b86-3540-9a67-2fbd6e779038 | -6.37549 | -43.00617 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9225eb54-80db-36b5-a91b-d12edc5e67bb | -10.96772 | -50.92224 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d6ded50-e796-30ae-8c25-9348ce38195d | -7.70468 | -48.73756 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9f30cc02-9172-3c89-b1e6-5bce2d6a554b | -5.55714 | -43.76278 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 08dfb070-3f7d-384e-b9ad-c5c0db011cee | -10.9433 | -50.7741 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cddc9c5-8971-314d-b85e-3d7d4007d3b2 | -10.94948 | -50.77879 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfb5a68b-9604-3041-b35a-51baa9949a4b | -6.28625 | -43.59023 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 473956da-0d8a-3d24-bb78-b23d9c5a2ae4 | -8.86118 | -47.93575 | 2025-09-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df6f7550-0fbd-3b48-be25-3b32c277db42 | -7.86084 | -46.73047 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0220256-87b7-3cb7-9861-635380f7499b | -11.6121 | -52.06362 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d3daec8-0a20-3524-b707-01a4859fece2 | -5.92469 | -57.72845 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 09a4ada4-35a1-3b2c-b8ae-0c3056e19cef | -6.43181 | -55.60853 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f018a394-bd06-3a5b-b6af-1769c90be091 | -6.79503 | -52.81204 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ed583bc-3523-32d3-9e99-ba81adc40def | -11.92077 | -46.66494 | 2025-09-03 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5467bb35-ae88-3d42-8b72-dd1c9c238cdb | -5.80199 | -43.23869 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README67.md)
