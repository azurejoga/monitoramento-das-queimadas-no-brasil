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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b518c5d1-bce0-313d-8cd2-8e70229306df | -12.91243 | -54.73415 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a56010f9-7482-35b4-8faa-8f324ecdfcaf | -15.35681 | -46.29687 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afef18b1-cae0-317f-b5c7-69215ca4907f | -18.45463 | -49.43955 | 2025-10-05 04:49:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ed5f6d9-26ad-3c0b-b4f9-c4d580361f61 | -16.01529 | -50.95374 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 890d74f2-d5c3-3df3-8505-f63ae8cca339 | -18.1933 | -53.35965 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 504f44ef-5322-32fc-8c9d-eb7bf75f99d9 | -15.50687 | -46.86057 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce3e9f6f-e456-3259-9002-5e9593054c8d | -12.89898 | -54.75161 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c14710d-87e4-3b8e-9d35-aa7ba7d70223 | -17.95808 | -57.54848 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 44455d0b-c6e0-371d-945d-34886e2cb89e | -18.24793 | -53.33546 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6083a06c-6425-3f8b-9efb-d1805436d202 | -15.97847 | -50.91492 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| d18633bb-03c3-3be1-920d-d554d68d206e | -15.34278 | -47.34238 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87e23ec2-2522-3336-aa0f-1842d4128a56 | -17.11056 | -48.92808 | 2025-10-05 04:49:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 974fc17d-a0d5-36c2-b417-ad49c0a6ba6f | -15.77064 | -46.2617 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46a5f019-1c54-370f-b72b-1e683a968888 | -18.17234 | -53.36367 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c3c6effc-f59a-34bd-bb33-3d2ccc3a2290 | -15.38178 | -47.94086 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 406dfe69-1175-38f0-b27c-408bb3e25726 | -15.5828 | -52.44986 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ee043c4-2667-3ac6-ba6f-de2959f99265 | -15.23432 | -49.293 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 98826526-97fa-3681-9bbf-740baae68fe5 | -19.50286 | -50.37534 | 2025-10-05 04:49:00 | NOAA-21 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 72691389-31eb-3d9a-b9ad-636b91761d9b | -18.25236 | -53.32877 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06f8c66e-ed0f-3a72-9e38-0eeb4df52322 | -16.03688 | -50.94349 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56dc2021-997b-3d2f-8d24-d5f988aa2dc6 | -16.36685 | -51.46572 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77e5dc90-6fb6-3dcb-9bc8-83993cfbfe49 | -12.84577 | -58.76443 | 2025-10-05 04:49:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bb3673e-73b9-3c2a-91f4-ac849156e11f | -15.68644 | -46.27214 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83582825-b6e0-3aaa-bacd-caeb11920327 | -17.95919 | -57.5638 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fd973e49-3e83-3539-99da-d80d3f8c4daf | -13.84284 | -47.91325 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ce22448-caa9-37f4-a70c-8f584451a379 | -14.32683 | -47.69622 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97429fd2-47e7-3834-96a2-9176e3437459 | -14.68137 | -48.36773 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 06586cc9-6052-3e92-aa0c-4feeed9a51d3 | -14.68998 | -48.3333 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7a739ef-97b9-32b2-aa3f-40a856084f0a | -15.21979 | -56.8071 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b68003f0-69b5-3d9f-8429-48f1b1838943 | -16.16395 | -57.57548 | 2025-10-05 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2e800fa6-7dce-3415-9c7c-8ae460438d53 | -14.33578 | -47.69076 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 98a9f9db-3931-3cf5-8569-be706129f73d | -13.94242 | -48.17905 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 162a40c6-aa1f-3a57-9e1d-631c592d86b0 | -15.96732 | -55.99323 | 2025-10-05 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fa486565-94d5-3140-b0c2-2868c5d4ca1e | -15.28737 | -47.33453 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afe06f33-57ee-3057-a266-6af9a10463db | -16.05593 | -50.93418 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 470447a6-19b4-30e9-8259-0e00a9d001cb | -15.44581 | -45.8718 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3856627e-599b-312c-b911-7f9948aef1a0 | -16.02074 | -50.95734 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25ffc70f-1f51-33dc-a01a-1b4ed29a0a78 | -15.57838 | -52.45651 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a683c1b8-b9df-36c8-a932-75451448a570 | -14.6505 | -48.33116 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fca48b3e-9236-3388-96dc-74ad088bc678 | -15.87354 | -46.26189 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57255994-c8e3-3f6c-8402-663cf276d4da | -18.3372 | -45.88262 | 2025-10-05 04:49:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1469afbf-6a8e-35b8-9f71-f6a15b5e24ad | -15.58838 | -52.50233 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ac0599ea-cfb9-3fdc-9a13-b43721cee1d0 | -17.88898 | -57.63659 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 65892b5b-7393-3c68-b6f1-3a330619552e | -15.76555 | -46.26544 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9df03572-8c64-38ca-b049-a8fc3369f4ba | -17.71272 | -56.74445 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a7b6cd75-9f35-3979-a4c7-9acf2343470a | -15.59883 | -52.4561 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43457b9e-533a-34e8-8379-0f76643dcd92 | -14.05199 | -49.14878 | 2025-10-05 04:49:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c570cf91-1499-3b3a-99f2-927122e5bd14 | -14.67353 | -48.36706 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8a5cef0a-99e9-32c5-be06-b2e8f58f2d0b | -12.91055 | -54.74566 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd0c2462-9e1f-355f-8c13-aa654e7b17c5 | -16.04457 | -51.037 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 38573d73-db32-3235-8032-938cd6e4d018 | -14.41783 | -46.18035 | 2025-10-05 04:49:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5afb52cc-7afa-3bfc-b1e0-71062243251c | -15.29622 | -47.33219 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cfa3457-e924-3467-a6d0-566ca40a4116 | -14.33936 | -47.69484 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f284fd4-2bcd-3d32-9fef-3a62e23f9d30 | -15.40002 | -47.95844 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb73296c-7ed4-3843-902e-a026d37e4de2 | -15.72942 | -46.2596 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d18a1dfb-242b-3ada-8291-807acfed1e6e | -18.24188 | -53.33069 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8468e398-bf74-39bf-9ab3-28980eeb3f11 | -13.84094 | -48.04192 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 32f3a994-b282-3b5d-be0d-990638eb7a7d | -14.95396 | -46.85594 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de16619d-9fb5-3b39-9bc7-b36445971169 | -15.65512 | -49.10226 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8603b14-a662-35e7-a537-bed75273751c | -13.72698 | -48.08554 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8de1b4d4-0798-3a24-9b09-9e5534d51b92 | -13.6301 | -48.6818 | 2025-10-05 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c44d705-6a9e-3751-b347-a5bc229bc324 | -14.69957 | -48.35054 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4cff630f-52b2-36cc-a3ae-81bae2dd4cd8 | -15.23003 | -49.29655 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 251f3cba-de20-34a5-975f-39c038bd44e1 | -15.58285 | -52.49403 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81e715aa-f237-30ee-8c7b-0a6445f96ba2 | -14.33489 | -52.97492 | 2025-10-05 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb19c344-d957-34f8-96d2-e1800cf3d19c | -15.93352 | -48.9873 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c091e9e1-84a5-391f-96d2-e7765b073c65 | -13.73088 | -48.08619 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| afa551b5-657b-348a-a7dc-77b3ce2b8ef2 | -17.71503 | -56.74781 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a474cd3e-b654-3b17-8e3e-6cf829a28a16 | -14.66393 | -48.34981 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f603e6d-fd84-3653-bd95-8c9ec268aa8a | -14.65301 | -48.33562 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4631b81-8828-3860-b54f-f814174cc9b8 | -14.33271 | -47.68288 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e2c0f85a-4e48-3711-84a3-9750830e4989 | -15.234 | -56.85629 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92e2f2ed-9140-39c5-947e-af6c79f6d3f5 | -15.20411 | -56.83165 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70c816d4-a687-31cd-83c5-89b4ee9b16a6 | -19.84186 | -46.51942 | 2025-10-05 04:49:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7472faa6-8b98-3ebb-b616-9d1884502243 | -15.23618 | -49.30676 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 792362d6-29d5-325a-bd8e-9c835c104711 | -18.1878 | -53.3513 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fd92578-6c17-3932-b6c4-d7e45d0363b3 | -15.74427 | -51.00815 | 2025-10-05 04:49:00 | NOAA-21 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e18dcbe9-cf0b-343b-87d7-eb231a8e5870 | -14.33929 | -47.66419 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24e94f4d-5771-3387-9e89-69759d67b6d1 | -15.98653 | -50.90828 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 96aad72c-8a33-328f-af41-71725400f541 | -14.64601 | -48.32881 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4dd9d069-ce38-3d86-b474-41581f39d247 | -18.15841 | -53.32077 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d691e012-09c5-364a-92be-468559571ac4 | -15.38228 | -47.93708 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1901acc-1ef5-39e6-a4a5-73f1ea0a9eec | -16.35378 | -51.45974 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7801533-69d6-3598-a6a2-4348fee76b41 | -16.12312 | -53.97668 | 2025-10-05 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 47512ef6-44ad-32d7-a19a-05f37fa681d3 | -16.15167 | -57.57854 | 2025-10-05 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 489d6333-d6f2-37da-916a-d6465a2c2c73 | -17.70769 | -56.77408 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 25030c2c-3bcc-3b3c-b0e8-6ccf919b6205 | -17.02069 | -43.44855 | 2025-10-05 04:49:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9316eb6a-52d9-36c9-a65d-799b0fd9019c | -16.07034 | -50.90802 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57f73a54-3074-30af-803a-488205e3edbb | -15.22757 | -49.28705 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 840f882f-99f2-3c54-b60a-6779dc364913 | -16.94434 | -52.68195 | 2025-10-05 04:49:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2770281e-8d18-37ae-8fb4-432a235c7628 | -15.19963 | -56.83557 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f29e09f8-2d50-3d85-af1d-46a274214f4e | -16.43787 | -52.16673 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| baaf2873-8edc-3fb1-bf90-a62abd321abd | -14.7559 | -54.66261 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 17230f1a-ffd7-31db-9b5a-ae4a5d773342 | -14.68997 | -48.27396 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9aa82805-ad33-36e8-b9c3-9f8b9f31f55a | -14.70026 | -48.3455 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d5dc2f0-97e5-3598-89c4-9bffe3ac4c62 | -14.69567 | -48.35 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 86a93db4-8ff8-3625-be54-6bd708b340b9 | -15.54603 | -46.83019 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c9d7ad2-7469-3f21-b450-4b12efc177bf | -15.34575 | -46.25785 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f78b632-e73a-3b20-9d82-c40695a08498 | -14.32285 | -47.69514 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a7c4243-ed2d-3b63-bcbe-a6b1470fe43a | -14.91719 | -46.86904 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README115.md)
