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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92257789-8686-37fb-829b-407725ef344e | -8.8304 | -50.49308 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb0104c4-dd03-3ec8-961e-f43ac44d716f | -5.01559 | -56.09463 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2089a24b-068e-32c8-bad1-6499a5509cda | -8.08715 | -55.34262 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e862de71-e9e9-3fb8-a24a-03f5473e5863 | -6.00424 | -57.70827 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2933356e-ec08-30e1-9734-d92801c848c7 | -6.19685 | -57.78067 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f875f573-ba52-31da-84cf-0526a8a7e9a9 | -8.32592 | -50.83641 | 2026-09-22 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25cdea9b-ef14-3767-b039-d1a45285fd56 | -3.06474 | -61.28835 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a869bf33-a8db-32b3-ad61-9370e32d7e44 | -3.01223 | -54.17921 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d697cf6b-341e-3979-bbba-24da9d0fa740 | -6.10117 | -57.62094 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64c20ca3-200f-3dbe-a132-b0bb90061314 | -3.01294 | -54.1748 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11524249-60c0-3759-ab06-5971cebbb08f | -6.15965 | -59.94533 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e506519-fa07-31ca-852f-5fe5c0491e3a | -6.34927 | -57.89074 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4b07f253-72b8-3c87-bfa4-b4ef3ed53288 | -3.29176 | -57.861 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e828ee9f-b5be-377e-8820-bec18360ff28 | -5.80826 | -52.08203 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da62773f-b62e-3960-850e-ce17f9605d8c | -5.32858 | -49.23609 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd1a38d5-72ce-37c8-9df1-b757220ef49c | -9.69768 | -54.32577 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 372218f7-716f-300d-aa48-2c023b21a311 | -6.69423 | -59.95913 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 898caebb-da27-3c39-bb56-cf7a83907a10 | -9.52822 | -45.38925 | 2026-09-22 04:46:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f77aa33e-4a2b-3191-9a97-66d1f0f5f2c6 | -7.42044 | -49.84674 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7015c4ad-48ec-3ade-8b6e-26520a9e48a1 | -11.67998 | -43.45337 | 2026-09-22 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9305672d-a918-3f5b-a747-9bd1ab4055f3 | -6.62477 | -59.91898 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a194fb5a-654f-3a8e-81d6-ce55cb0e000b | -3.27364 | -50.01565 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3b284ed-ff7a-34a1-a402-b8146a563722 | -6.83232 | -55.52932 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c405d6e1-99d1-36b0-9954-4db19f76ee7b | -4.68149 | -40.14685 | 2026-09-22 04:46:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8f2d33c3-e70b-3b10-a30e-3607a21c4d56 | -5.87627 | -52.12513 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1927e1bf-7641-3547-a081-0ebd34ac12c0 | -3.10765 | -60.71786 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cbd636d-987b-30b6-99a4-fc20277433d6 | -6.37587 | -58.29027 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67a043d3-0f79-36d0-9fd4-93b7c2621f2c | -5.2348 | -49.22954 | 2026-09-22 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4c45136-dd6a-3970-aa79-1ee329764bae | -6.78603 | -48.67936 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da3e39b4-af2f-34a9-b86b-8c23228ca23d | -5.19046 | -49.33815 | 2026-09-22 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7764a483-d71d-3348-a057-ee30413c2426 | -6.90984 | -45.51722 | 2026-09-22 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| acf7f17d-09a5-3e9a-a436-0454db354623 | -3.43622 | -58.03007 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72fb49a4-124c-3b6c-872f-b6ddc20e0642 | -8.43116 | -45.81512 | 2026-09-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ef93743-9a22-3e11-a7c5-08efd467556e | -5.53871 | -51.5891 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a760269a-d83c-37fe-880f-3db29ad5001e | -9.97434 | -50.25399 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b14108d5-83d1-33c4-bf78-1de20d04d3e3 | -7.57844 | -57.6829 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acdc43ae-3cbf-3806-aa73-ce48c94f51b0 | -7.77944 | -44.80732 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7baf21b-3b69-3d81-a366-c5b0d4258879 | -5.57191 | -48.97377 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98b5bb69-1efe-3c5c-beb6-26896d2499bb | -3.01967 | -54.18035 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d98fe93-490e-3070-a019-09adfee87909 | -6.08128 | -57.63111 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bd32f6fe-1b5f-3629-8a8c-ade29bdaaf38 | -6.45223 | -59.97361 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd3a6700-062f-3ffa-bf0f-2d763478112c | -3.28668 | -52.59877 | 2026-09-22 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ad30533-a70e-3f03-803d-6c1ed5bf9786 | -9.61338 | -43.93903 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5c6e393a-b6eb-35f4-aad2-a754926955cd | -8.6251 | -54.62798 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 48f7a932-f28d-3cd6-babd-e83e8faa7115 | -7.24602 | -55.61211 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8c8853f-ec67-3381-8ac4-a5b83bcea369 | -4.05879 | -56.31081 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e332bd00-bba6-3f19-9581-0248e10cb52f | -11.10605 | -48.32663 | 2026-09-22 04:46:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b25b4344-4daa-3371-a3de-5943145409d7 | -11.10187 | -48.30175 | 2026-09-22 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efea918e-88c2-3de0-9276-c494efd6cd58 | -5.91907 | -55.69205 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 551f2d7f-2750-3e3a-98c9-a47d201c9f3b | -8.31085 | -50.38045 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b45fee2-1e16-3286-b3ca-61efcba840db | -11.11045 | -48.32265 | 2026-09-22 04:46:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 401492a5-4027-35f1-8a20-6726ec455a08 | -3.46933 | -59.54885 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7df389c4-dfbf-39ba-807a-994cf27964e7 | -6.35184 | -59.96045 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 183753f7-33f7-38ab-9c46-3d4e8155dc3b | -7.41652 | -49.84974 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68a05b2e-36f1-3c71-9137-420aa26a14f5 | -7.2621 | -55.58605 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79759729-2305-3c6d-a788-524ad94faf93 | -5.60107 | -48.22697 | 2026-09-22 04:46:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 442a79a5-6573-3f71-8344-b9ddfae31eea | -8.48841 | -44.75367 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| daa60939-d20c-378c-932a-47b4a2ee4b02 | -4.22371 | -48.61634 | 2026-09-22 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6b8e80ac-994b-3e44-9ed7-acd660e0fa82 | -6.23844 | -51.01035 | 2026-09-22 04:46:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1b9ecb12-95a5-3e5d-bf89-5671370d1ddc | -5.81488 | -57.73506 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7eec1d76-b46e-3493-9dd3-81e267ca520e | -4.2104 | -59.91413 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87876183-6a13-3cab-82cc-6c109f52e5f5 | -6.91795 | -59.62955 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87192a4e-b71a-35e7-aec5-14986a1bbe16 | -9.68997 | -50.8526 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c8f0edb-cba4-37c5-a9f6-8b89fdf3ac1c | -7.58782 | -57.68018 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a570be78-d385-3b0f-904f-87628e65e123 | -9.3854 | -47.75678 | 2026-09-22 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d39383d2-bb64-36e6-8660-1efefa0cb249 | -6.72697 | -55.05755 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4e5cc9a-c03b-3941-9aaf-7fcddb9cc992 | -6.46598 | -59.99601 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 106e4358-a2d5-30fc-b908-f34fa114c252 | -3.05978 | -54.41529 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 131fb8e7-b090-36ed-9deb-8ef4e3680c5c | -11.02461 | -48.2736 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c154112b-cf3e-32a9-8b50-19f106fc3a5b | -2.93287 | -57.79374 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 462b1ff4-e017-360c-96e8-9673e759cb1e | -7.53199 | -46.21157 | 2026-09-22 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a55c838b-fbbd-3652-aa2a-2aedb559d24f | -8.91642 | -50.93194 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f409bef0-6aaa-3a61-b107-a7ffc8abdb1c | -3.45455 | -50.60374 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17c1af50-f6d8-3f71-8bae-4e4de75debe1 | -2.88641 | -54.08107 | 2026-09-22 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b6e64050-206c-35c9-8e16-b82c6389e26f | -7.58064 | -57.69621 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e30ffedf-e73c-3ce5-a19f-2837b58705a0 | -6.07097 | -57.87055 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2ee67b6-be04-3a62-bc01-318048c1a59f | -6.22807 | -56.03979 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91d292cf-fa98-387d-b81d-f31d64e261da | -4.6825 | -55.62299 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| bfdc797d-f212-3daa-a77e-33b4170ad839 | -5.84595 | -53.54979 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3aca28a-1f85-3c87-9165-a69aee678556 | -5.85355 | -52.03142 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab92d4c0-3d60-31c4-b492-0785db06f83d | -4.38848 | -55.0326 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47ef7bd3-33a8-3574-82f3-2b5748ea748b | -3.83672 | -59.38315 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2dfb747-3ced-3cb9-9c9b-500e0eebcd3d | -7.1343 | -48.43207 | 2026-09-22 04:46:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a600730-4f6b-3e7c-aacb-fcd8368d5a34 | -9.61758 | -43.94531 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d3a94430-6d65-3ff3-9a98-a31ea774e4eb | -8.78939 | -44.26823 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d4a216d5-0954-3e8d-be17-3a42942ffc53 | -11.67957 | -43.45662 | 2026-09-22 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 724cacf1-347b-36bb-9687-609753f83cc7 | -3.78906 | -60.74846 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 704822f3-741d-3813-ab33-5c89dae4541a | -8.3466 | -50.74588 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab66393b-3e15-318d-b033-92408688d3e8 | -9.87402 | -55.72849 | 2026-09-22 04:46:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 339a2bd8-530e-3989-8d47-36fe89f4f55b | -6.79713 | -58.78837 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67161de6-32df-30b2-870c-69bc91c08608 | -7.43056 | -49.84844 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd902f79-ec0d-3d54-9b02-c335d45f28ac | -4.3023 | -56.26339 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d546ee02-bfb7-3cb5-a2b9-3479a4ab8a5f | -10.68695 | -48.72446 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 97ca46a9-af09-3cef-8c8e-52d068dcfd8a | -10.50123 | -51.28076 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0537639a-a0e9-387f-aeb9-0c8931dbd8b9 | -11.10542 | -48.33101 | 2026-09-22 04:46:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f144a4f0-cde2-3fdd-b32d-b8ea7d1ba775 | -3.92902 | -56.04646 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20aadd07-0cc1-3ab3-b0df-9c20d77ae21f | -4.64882 | -50.9925 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0799b0c1-f20e-3bf5-9977-d64beddad574 | -3.37708 | -50.40207 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c65d044-9d7f-37af-bd33-281a4f7be0b2 | -10.91097 | -47.37367 | 2026-09-22 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b5167ad-1bc1-3a22-b041-5341b3e06ed8 | -4.27792 | -56.25603 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README54.md)
