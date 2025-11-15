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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 181449da-edce-351f-ad49-25a2076d4361 | -12.23513 | -49.39305 | 2025-11-15 04:27:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 654387a5-f2e2-3c9f-8efa-a2634a3174c3 | -11.16991 | -48.14266 | 2025-11-15 04:27:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d9599a4d-d421-343e-a036-ba911aae268d | -11.57019 | -44.86943 | 2025-11-15 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1476851d-1755-3f58-be98-8ea2dc5fd5c4 | -10.6981 | -44.49232 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b73d782-f5be-3cb3-8dd5-83ffb1de55c9 | -11.7929 | -47.40801 | 2025-11-15 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93115bbf-74f3-3748-8100-f8f0956969ff | -10.44703 | -45.07499 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16533b9b-d08c-3cfc-919d-4976e9c330e6 | -12.44067 | -47.88762 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93f3d917-22f5-3c24-9b26-1d3e7a8bca96 | -10.34389 | -48.91818 | 2025-11-15 04:27:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03e7c2df-d15c-36f3-b1e0-80bd342120b7 | -10.35756 | -48.7279 | 2025-11-15 04:27:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83e9b877-f8bc-340d-a56e-b4c4d974e5ff | -12.36341 | -43.69814 | 2025-11-15 04:27:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9009f9c-df29-3c89-91cc-77c127c246ca | -10.37913 | -47.7529 | 2025-11-15 04:27:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d11c74c3-12a5-3acf-9b79-313f9fad8e6d | -12.67404 | -46.76594 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 147c49ec-27ea-35af-ae44-ce9f0ae9c935 | -16.44913 | -45.00803 | 2025-11-15 04:27:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74f6e280-e9c5-3802-8f38-9b810487aaae | -10.53326 | -47.93669 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ddedc90-9b38-3097-a817-798954d15185 | -12.67793 | -46.76289 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f604127e-8144-3343-9e3b-685121e31fe2 | -16.56166 | -47.61272 | 2025-11-15 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24c05cd3-f886-30f2-9da2-03ffaf3aed96 | -14.91778 | -49.08034 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 691ba384-d319-3e96-9a61-2d61a5ccbda7 | -14.94545 | -47.50755 | 2025-11-15 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 800974c9-86f9-34e2-96c6-3fbc0da7387b | -9.7024 | -48.87033 | 2025-11-15 04:27:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df0c39a3-d1b5-38cc-95f2-bbdac6b15b1e | -11.68091 | -44.73359 | 2025-11-15 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a54fddf-dad2-34e2-91a7-d456a662f9ae | -15.6557 | -43.32084 | 2025-11-15 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4e20f12a-7c83-38ea-aac0-6cf835147c48 | -11.87573 | -48.99248 | 2025-11-15 04:27:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c674396-4000-3e7f-94be-a5a0ae1c8d3e | -10.42362 | -44.94991 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9457ab6b-8ce9-3b38-a310-7b198b485320 | -11.03635 | -49.53444 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 422fda05-a792-3dad-bb0e-d791189d108a | -15.31206 | -45.40405 | 2025-11-15 04:27:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43a6aabd-85b9-3e6f-9382-ea14cd3a969f | -9.71519 | -48.8992 | 2025-11-15 04:27:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91006f7b-96b9-3402-b560-635f1c1590f0 | -14.05188 | -44.48078 | 2025-11-15 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4003fa79-1bd4-383c-9a54-e6df9070c67c | -10.35408 | -48.91986 | 2025-11-15 04:27:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a880c75-c511-3748-af4a-249f0e89f711 | -9.81569 | -48.8432 | 2025-11-15 04:27:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1cebe54b-5e14-3b05-a35e-185aedd4eecb | -11.84934 | -49.21866 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| feeba928-b320-33f3-a103-bf69cc1dd93f | -10.34789 | -48.91505 | 2025-11-15 04:27:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 231865cf-5293-3ba6-b5f0-eefcb5818b71 | -11.91776 | -46.20538 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bf18dfd9-9b33-3ae5-b31d-3d73efc3713c | -14.55869 | -45.19623 | 2025-11-15 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2869a7b-3b0a-30da-a34c-9f46b63d3fac | -12.18476 | -49.33858 | 2025-11-15 04:27:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5f6ce14-946c-393c-9118-a26ebf1db659 | -9.93082 | -47.83524 | 2025-11-15 04:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd5eb79b-ded4-337f-a336-ee3d84a1eb8f | -11.91831 | -46.20177 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e27219ff-31d4-36cd-804f-5bd66cf17ec2 | -16.56278 | -47.60542 | 2025-11-15 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d0f1975-2eed-3773-9458-5af6c3295407 | -15.52311 | -43.88519 | 2025-11-15 04:27:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1a98daa-6b0a-364e-9588-4d0c49ede918 | -9.70178 | -48.87407 | 2025-11-15 04:27:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27f5f46c-dce1-3672-9864-ddce8b0d21ad | -12.80719 | -46.45105 | 2025-11-15 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f79d3b20-b438-30c9-a3ee-9a445517125f | -12.50626 | -46.68488 | 2025-11-15 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 515f3d02-8ee4-35ae-85f0-a6370a37d74e | -9.93689 | -47.83985 | 2025-11-15 04:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81bd85b2-09e4-3a7a-a824-f1e558848454 | -12.47271 | -49.57161 | 2025-11-15 04:27:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0aac41e4-de3a-3ea4-8a11-0c72da3f1d4e | -12.75568 | -43.65552 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3900759c-92be-32b9-abdd-cd1bbef0214a | -12.67349 | -46.76953 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fb6b980e-974b-3ae7-a5ba-b216ca9bd782 | -12.24253 | -49.3905 | 2025-11-15 04:27:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00757433-f49c-31e5-9c43-d830f0f9d5cb | -9.93244 | -47.84637 | 2025-11-15 04:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19e102bb-3684-31b8-990e-a1067426b1a9 | -12.00514 | -46.76647 | 2025-11-15 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0749cf32-a1bc-3810-9f50-f2f9dd36bef4 | -11.11362 | -48.34472 | 2025-11-15 04:27:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 031b4535-0959-339b-a52f-0735fd38c1f6 | -17.28036 | -46.46238 | 2025-11-15 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34d950b2-1e3c-3391-a7ea-bb3892c701b6 | -12.59715 | -48.33377 | 2025-11-15 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad1537b7-afe0-337d-8f30-54f3e4ca182a | -13.36014 | -43.72193 | 2025-11-15 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b0cb4f4-1455-31ea-811e-8199b50a4b72 | -11.96126 | -44.96207 | 2025-11-15 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e8584e4-af43-3701-a916-f6b909f163dc | -11.75625 | -45.32277 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f314fa85-c74a-37dc-93f8-a0670ff234bb | -10.1737 | -49.31485 | 2025-11-15 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ece23e6e-043f-3c30-92b7-67347097ac76 | -12.68468 | -49.11517 | 2025-11-15 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 329a3b39-8b12-39a0-b366-6ff335ae6b1a | -12.61877 | -42.39266 | 2025-11-15 04:27:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cca6d38b-bf04-3a45-aea3-8ad34db47a14 | -12.68405 | -46.76754 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c7290d62-6e17-362b-87c6-34bc62c4dfc8 | -11.84595 | -49.21809 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| a7810b39-9893-3e63-adb7-aa2f8420ad43 | -14.67367 | -46.55997 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8476c56f-0e2f-342f-bf6a-16196ed56d23 | -17.24867 | -42.6691 | 2025-11-15 04:27:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e7cddf9b-7937-380c-aeb9-9185f79096f4 | -15.30502 | -52.99963 | 2025-11-15 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6e08598-a285-3423-8f11-7dc120ba33c9 | -12.15507 | -46.67677 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1cc035a-4aa6-3b01-9225-c724fcd9e47a | -12.79502 | -48.81717 | 2025-11-15 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 766cd4ae-478d-34f5-a66b-c9fe45b8e7ba | -12.78977 | -46.3848 | 2025-11-15 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 139f0e06-5bce-3c18-8422-24206602f317 | -12.44123 | -47.88411 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f15029ea-ce2a-3a78-89fb-698bb2205bbf | -11.32218 | -48.50715 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e38e162d-407e-3137-94f1-61d46e934a18 | -11.16716 | -48.13858 | 2025-11-15 04:27:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9fbecd43-5e35-3d66-8221-f28d87b995f4 | -11.01986 | -49.35551 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04723a39-86d8-3059-8d95-120e4d6f49e5 | -12.38765 | -48.11381 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef2a51c7-be77-310a-8562-6eb50bf7bd80 | -14.56018 | -45.19365 | 2025-11-15 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c03a7f36-b3eb-38cb-abd8-16612aa5b08d | -12.79369 | -46.38166 | 2025-11-15 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f946a063-a098-3c04-9053-62a96ca3524c | -10.5268 | -46.1837 | 2025-11-15 04:27:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d83cf30-540c-3a2d-bbfe-fa4ed8b2707a | -11.32205 | -48.52927 | 2025-11-15 04:27:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07343873-46f8-3521-95e5-4193af2d318c | -12.97128 | -48.83929 | 2025-11-15 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60075280-28be-36c8-b1c5-cb4da87b6e69 | -12.67682 | -46.77006 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7716107a-929a-373c-9229-af435c72e19f | -15.10406 | -41.97268 | 2025-11-15 04:27:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d48c7a06-742f-3871-a6e4-5d7da9bfeda3 | -12.83911 | -46.44481 | 2025-11-15 04:27:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98776e41-0401-3b32-b48b-0f323122e0c1 | -12.90865 | -45.10182 | 2025-11-15 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb37afc1-5cf1-3999-af61-31db9bfc8b6f | -14.65788 | -46.5727 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 925a54e8-327d-35cd-977b-61d938ffce10 | -12.78565 | -46.74722 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97fea8a1-bc4a-30f7-9fb8-026a7e741b8a | -12.18537 | -49.33488 | 2025-11-15 04:27:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64c60a67-79f4-314c-8d1c-5bdb9d364c40 | -12.14895 | -46.67214 | 2025-11-15 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fb61f00-f66b-3a6f-bf1b-714f3b3c70e2 | -14.65614 | -46.56124 | 2025-11-15 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97d1079b-740e-368a-a3b5-37509b702b6f | -13.091 | -48.30623 | 2025-11-15 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2740dd64-9213-3fac-a7aa-635d8cdf2a43 | -12.25733 | -44.91471 | 2025-11-15 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94015473-3b2f-33c0-9ab4-74924ccccfac | -13.72301 | -49.90826 | 2025-11-15 04:27:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f924c66-0e19-3024-b138-55a7f058c7a6 | -11.03512 | -47.98644 | 2025-11-15 04:27:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9463521c-77c7-3021-a0ef-0478df1f66f0 | -10.52456 | -46.17605 | 2025-11-15 04:27:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c25647ef-d8b6-3903-b602-ea6fcc083234 | -13.89643 | -42.90112 | 2025-11-15 04:27:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f8637199-88ba-3f56-a44c-127ab587b914 | -14.08707 | -49.48643 | 2025-11-15 04:27:00 | NOAA-20 | ALTO HORIZONTE | GOIÁS | Brasil | 5200555 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2207b85-8600-3e89-97f4-9ea973b8d16d | -11.70687 | -48.39489 | 2025-11-15 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a1480ac-0806-38f5-b922-31fdf2cb2bac | -13.47309 | -46.49108 | 2025-11-15 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66220445-e778-3383-8693-e4bcfe025084 | -12.78231 | -46.74669 | 2025-11-15 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c7e9c03-a423-3b07-b6ec-67942b56fe70 | -10.70458 | -44.49739 | 2025-11-15 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77ced68b-179b-30ff-9130-df15d4af8bcb | -9.92968 | -47.8423 | 2025-11-15 04:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e48dddfb-8c28-370a-ba86-16284aaaa261 | -12.42574 | -43.18041 | 2025-11-15 04:27:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cc2b42c-52e6-3dca-a0f8-76fb2acda065 | -11.85394 | -49.21182 | 2025-11-15 04:27:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 482d6a1b-7e75-3b4a-af41-657e2919eb01 | -12.38434 | -48.11327 | 2025-11-15 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dc55fad-bb77-3ef2-b995-1d9cb041b342 | -10.55276 | -44.9296 | 2025-11-15 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README46.md)
