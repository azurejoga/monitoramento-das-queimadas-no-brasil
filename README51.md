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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95f6dccc-3cbe-354e-ac5e-ebc38a0abb40 | -14.7768 | -60.17929 | 2025-09-27 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10f2974f-638a-3ade-bd50-6d9fc88fb5be | -11.43563 | -44.99088 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff746035-6f64-3f46-b144-07a4dfbb8944 | -12.65143 | -51.66989 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26cc014a-5b2c-3187-9067-b32e3f3e79c8 | -11.42706 | -45.0194 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abf85586-253c-3117-a933-01ea0beabb14 | -12.3039 | -44.35456 | 2025-09-27 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ca49f46-d493-3e12-9ac5-b5ea144b0bd9 | -12.6481 | -51.66936 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a104290a-8d2a-3b3a-ac2a-838367ed82c2 | -12.03006 | -47.0708 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f153f3b8-83de-3a49-9bd5-aa5ac9606bbc | -13.18362 | -47.39795 | 2025-09-27 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c742a413-8f28-3329-8485-2c16dc18a1dd | -14.43168 | -44.88643 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96536217-fa9f-339b-be9b-55c28a2a1ae6 | -12.62049 | -48.14162 | 2025-09-27 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f14e483-598b-3872-a278-a0719c1e975f | -13.61759 | -47.31429 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dde51cc3-934b-36db-9c43-9e787a75145a | -11.72062 | -62.59225 | 2025-09-27 04:46:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f48e629-0f04-3c58-81eb-a430d48a737c | -11.43707 | -44.98035 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 61416e1b-a048-3d9c-aecd-f762ba24450b | -14.8306 | -45.63172 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0e52ae9-a8ab-31a3-bd3d-445b5f172bf5 | -13.6305 | -48.07778 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af132190-ad72-38ea-8bf5-450cba88fc68 | -14.87912 | -45.54663 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30479b78-3b33-39ca-88a4-692a0c5ff75e | -12.02909 | -47.07802 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6297942c-fb5b-37fa-85a9-409d54349fe6 | -10.80466 | -45.37356 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d8bab96-c5fb-3c79-b6a4-c9522037a439 | -10.11962 | -45.33414 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e84a008-3316-3593-9d3d-10d8746287ac | -10.05521 | -59.36403 | 2025-09-27 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9ff8207-9364-3e4d-8caa-b23b160fa9e1 | -11.50812 | -47.74892 | 2025-09-27 04:46:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14e3ca0f-732b-30da-af75-fd16553c0ac7 | -15.9013 | -57.4936 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 83893ea4-09c1-3a1e-aec5-70332a7ed242 | -12.65198 | -51.66633 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dae44cac-fe87-31e1-bfb1-b199efbc141e | -10.58603 | -46.27564 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3051c0cc-335a-3583-bb79-709faec8c536 | -15.88832 | -46.19007 | 2025-09-27 04:46:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55a20181-5a68-3d4a-a164-7c8befce7928 | -12.54115 | -45.84903 | 2025-09-27 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9c82331-2891-3396-a7d3-d187dfc213b3 | -10.28462 | -45.21185 | 2025-09-27 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f696e174-acfa-3dad-be2b-a9073b67f690 | -15.43249 | -48.21621 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0564ef8-2483-38e8-b7e1-88bd59a29168 | -14.46112 | -46.84988 | 2025-09-27 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 082b8eb1-01e4-3ebf-8325-d37ecdbfa0b4 | -15.20516 | -50.1862 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd40f5e2-db3a-3131-81d2-4aba7d9248c0 | -15.27254 | -46.45665 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 46bc1f03-e435-3c41-b389-dbb8b238bfda | -13.72625 | -48.66838 | 2025-09-27 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b34ea55-fd2a-30b1-a817-fd99741c624a | -11.77803 | -43.76013 | 2025-09-27 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 966df549-f7c0-37da-92c4-fb15c56cceaf | -11.78376 | -44.86791 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e45c72a-2dd9-3b20-a118-5e8b038d901c | -11.71392 | -44.40737 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3bf21d8-01dd-365e-9693-bee66071ac68 | -13.37676 | -47.83102 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bc186d03-ed53-37d3-969e-7e1026148ba3 | -11.67661 | -44.46748 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7257f6d-149b-3334-b3e9-ff628876ae00 | -12.02806 | -46.5069 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26a3fc64-4f89-35cb-b45f-a412db634504 | -10.11845 | -45.34282 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0bfa2647-43de-3618-9a30-1ffc0a1026a2 | -11.4305 | -44.92415 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d37306fa-4e10-3c20-8846-8458512a7657 | -11.64615 | -52.87439 | 2025-09-27 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4acc6774-bde6-390b-b13d-74df6b456733 | -12.03104 | -47.06358 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dd278365-cae0-3df4-8339-cb3f2468ad71 | -12.96796 | -46.91027 | 2025-09-27 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 674d95de-4066-3cd2-be0c-ee46655565b2 | -10.93134 | -48.82889 | 2025-09-27 04:46:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfa82815-9570-3062-9c51-a7b89a93f6b6 | -12.05465 | -47.65334 | 2025-09-27 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b83eb75b-d616-3d50-8833-c9a70c39d559 | -9.79107 | -50.91994 | 2025-09-27 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18dd9a80-fc1c-3c9c-8ba2-0e270339710c | -13.62664 | -48.07697 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca848797-0eea-3848-9ca4-0f7e547b1dd0 | -10.49304 | -48.03797 | 2025-09-27 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d31e0180-7361-3373-90fa-e85299c18f15 | -11.38542 | -44.97921 | 2025-09-27 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee9aaef9-8ead-3db6-8c47-6533fceacdfa | -14.88041 | -45.53645 | 2025-09-27 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db5284c4-fd86-31da-ad3f-900671d69a26 | -12.0293 | -47.07476 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b134f4e3-6ad4-30f0-8868-b2de9a6ecac0 | -12.54558 | -45.84965 | 2025-09-27 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba49ca44-501a-355d-8871-ad771c19a590 | -11.24118 | -45.5593 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3ec2753b-d251-368f-83b3-ee89ed67d272 | -10.03874 | -52.08922 | 2025-09-27 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e882a202-000e-359b-8c54-a5b3010ce234 | -15.00876 | -54.99458 | 2025-09-27 04:46:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db7602b9-48ac-3b6f-ab62-59e09e8f35e9 | -15.00812 | -54.9984 | 2025-09-27 04:46:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5aa1b5e2-be87-3062-acc6-c6cf715c7f7c | -15.26268 | -51.47473 | 2025-09-27 04:46:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 77496e7c-874a-3d7e-a8c1-037435a31956 | -11.89641 | -49.90015 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a52a22ca-2c78-3403-b7ef-1d3d89fbac55 | -11.29638 | -47.81434 | 2025-09-27 04:46:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ff9f908-1d16-332a-9cc4-cf5873e28eff | -11.96992 | -47.91112 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86c5be23-6080-3872-9e04-86fdc1ac0821 | -15.2843 | -46.43495 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38da6d5e-f618-3337-9149-dc5b9f204ec4 | -11.24178 | -45.5549 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 28411e77-2b57-3371-9969-3a930c160abf | -10.03929 | -52.08572 | 2025-09-27 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99b02e73-d61f-3895-8607-345b1101943b | -15.01843 | -46.96466 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1cc1c63-0ca9-3403-aa04-d2b7d74e810c | -13.51692 | -47.41413 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3df7ac1-9214-3d4a-a3e5-62cc84a3ced8 | -11.24621 | -45.55552 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ba42f486-c454-3288-9227-97c30ef7412b | -13.18024 | -47.42303 | 2025-09-27 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85abfa12-4c32-3079-b0d7-a20a89ae661d | -12.03541 | -47.06089 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 175f5131-7bb6-372b-8276-f299f053b895 | -10.81301 | -45.37899 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2398dc24-105d-3cb3-9ecc-8dc816e2d231 | -15.42566 | -48.21302 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b3a9b48-92db-3fe4-8a01-2477c13b5559 | -13.64278 | -48.07503 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfd78056-b1da-3c07-877f-f50d799e14a9 | -10.12343 | -45.34537 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1797895c-ea18-3680-9d28-e26d8e411f9b | -9.89472 | -49.12638 | 2025-09-27 04:46:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03283ccf-bae2-38fb-b9c8-03dbdc8a5be5 | -15.93275 | -57.49411 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| caa17e1f-37ce-3141-853e-e29f6a735b94 | -11.43167 | -45.02006 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8ce06be-5065-3cf4-a0fe-978ae4d5dc49 | -13.70396 | -47.89181 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 82344b29-6fc9-3317-8c28-937ab3671c8e | -11.35264 | -45.01414 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6326abb1-d734-37b9-9103-174fa4bbd0bb | -12.64921 | -51.68411 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4beb76e0-d352-35e7-99af-72063a80854e | -11.38364 | -45.0282 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5192d168-88b3-3ef6-b1a5-b398a47bb722 | -15.9347 | -57.4973 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dab61c75-af56-3acf-9c5e-0f49d4b63b29 | -10.89214 | -53.73839 | 2025-09-27 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d7e18f1-4212-37ad-a9cd-20fdd4883522 | -9.86194 | -48.81325 | 2025-09-27 04:46:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1ae5723-6f98-3c3a-b9ab-882c187403f5 | -9.40928 | -54.69275 | 2025-09-27 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a469b384-1cab-3169-9710-27d0916ff899 | -12.95446 | -46.91623 | 2025-09-27 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb27e5a6-e984-30b0-a364-f0b64cf7c9e0 | -11.3606 | -45.02504 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 60b61189-f8ab-3244-ab1d-3aed3908950a | -17.11151 | -46.87004 | 2025-09-27 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7c3ff4a-eb96-326f-9754-69e61aa10088 | -15.90038 | -57.49884 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89ffbdf9-8921-395b-ad11-55b3eda2109e | -10.97026 | -49.57064 | 2025-09-27 04:46:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eebe8d67-e6f3-35c2-8195-bf0def79d53c | -15.03695 | -46.95575 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 595524fb-11d2-3de3-b3e3-3cd981756b38 | -11.67111 | -44.47215 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea9704ca-0503-3e5f-be4f-01347b3f1aac | -10.13189 | -45.3101 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6e34f16-be90-30e2-bca1-67fc4665b042 | -12.64976 | -51.68056 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0afde5ee-23c0-3537-bfb9-9c212729ed62 | -13.60295 | -47.29996 | 2025-09-27 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74b37c4b-7389-3d6d-b0f3-024713e5e070 | -10.11344 | -45.34658 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7b53367-d51b-3bf7-80b4-358b9136a234 | -14.51393 | -48.01255 | 2025-09-27 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdf16e61-4195-38f8-8579-26e9f36b57ed | -11.40794 | -44.91602 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0cff883-ca3a-39d9-a399-e64bc3fb3585 | -14.95475 | -47.50621 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70eac8e1-ee8f-3c84-b20d-9a7ac63c9c70 | -12.10005 | -44.31348 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| defeb46a-85c5-3643-b151-fa7ec1ae7795 | -14.47992 | -47.70863 | 2025-09-27 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9eb4f44e-776f-3bae-bf2a-22c13c6eac17 | -15.75729 | -48.50348 | 2025-09-27 04:46:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README52.md)
