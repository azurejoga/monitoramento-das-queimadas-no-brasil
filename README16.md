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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffc06e8b-5cf7-35bd-97c4-b75f9298996f | -5.0748 | -45.11188 | 2025-11-01 04:38:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02566b05-afa9-30ce-96a2-c623ed8c6122 | -4.8063 | -48.71845 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddd6bcf3-58fc-33ac-811e-d4a3f224bde7 | -7.38641 | -41.9338 | 2025-11-01 04:38:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2e9216d9-4953-3ef9-b988-932da526b280 | -3.46018 | -52.8729 | 2025-11-01 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51fe2b4d-6b4a-3e01-bdf5-205550400c21 | -3.03599 | -53.7932 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70f17210-c36c-3e74-a491-ddb41b850417 | -4.40487 | -48.21379 | 2025-11-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 60ee6e6e-a966-3c83-a7e3-85654569a4d5 | -3.25183 | -52.91273 | 2025-11-01 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff5db873-9173-3503-a867-3cf697dd4b70 | -2.65112 | -48.50875 | 2025-11-01 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dd0c3d8-b7ca-3138-8c46-a2bd5cff17a4 | -5.48925 | -43.08731 | 2025-11-01 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 597b7a03-554c-3429-8665-8d5a9d5e38b2 | -2.79408 | -43.34587 | 2025-11-01 04:38:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0805cb75-6598-3ef1-a3dd-57d1042412d5 | -2.92955 | -51.46389 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59641b72-3f72-3f8b-8c12-ab076398b386 | -6.99663 | -46.52694 | 2025-11-01 04:38:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abdf99af-7e79-3ea3-992a-07798fd3e642 | -5.88256 | -44.52005 | 2025-11-01 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86ec7120-84f6-351c-ab20-9fb61a51f8ca | -7.57787 | -46.85397 | 2025-11-01 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dccd3a2-b3cc-34bd-9363-677a60f806f1 | -3.37182 | -51.57513 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 243d34fd-0903-3e3e-9417-3fa7fbb5d5c7 | -4.66329 | -45.70244 | 2025-11-01 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6b6eeb7-3500-3875-8099-1a23f1eecba3 | -5.59214 | -50.06049 | 2025-11-01 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15a27af6-4e93-314d-b74c-92c75b50f936 | -7.34687 | -46.21135 | 2025-11-01 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7258c5cd-1c16-3325-8ba2-fe94bc405918 | -3.43596 | -42.54268 | 2025-11-01 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 356f777c-f459-32b1-87c0-da463817d505 | -4.77665 | -46.49849 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 419a252a-961c-3bf1-a6c7-9eb7dd7c92be | -4.79827 | -46.47389 | 2025-11-01 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc8d2436-4e81-30ab-95f8-2cd3e2e9f5a1 | -5.95469 | -45.58061 | 2025-11-01 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b4fbba5-5ea5-3e18-b848-43931851b8ff | -1.25982 | -54.09527 | 2025-11-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9053cdb-8e17-327e-8595-86a6aa59ac78 | -3.01741 | -51.36523 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdb0377b-4c09-3be8-9522-ef7992cdaaa9 | -4.95213 | -43.44805 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6932ca29-2f6c-39c6-8b3b-1be6dbb8583e | -3.60562 | -50.6211 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 817de325-0769-3a16-a7cc-9804d9afa1ac | -5.28559 | -42.9722 | 2025-11-01 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0dd287a-83aa-3d65-bf94-3c75f225d222 | -5.26229 | -45.60671 | 2025-11-01 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6ed29293-e971-3790-b508-ffa8ab1504ba | -5.68325 | -48.65842 | 2025-11-01 04:38:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad358848-7845-371a-a502-2d7419c87a64 | -2.79813 | -43.3465 | 2025-11-01 04:38:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9273f0d2-a3bb-375e-98fd-391e20f65839 | -5.45377 | -45.40258 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 399a30c3-60ba-355e-84f0-7747e55a747a | -4.68105 | -46.8217 | 2025-11-01 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e02ad082-634a-32d9-b504-1e1c2305a23f | -1.85593 | -54.54734 | 2025-11-01 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0fd43270-ebec-3577-b146-7a03ccef7e3b | -7.36048 | -46.99979 | 2025-11-01 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c61d8fcf-b3de-37ac-b879-3606cf391d7d | -3.10966 | -45.22908 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ebc08b37-5014-3965-97ce-21e725386ade | -7.08039 | -48.31102 | 2025-11-01 04:38:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bef838ff-19cb-3c8a-86f6-90f9ef4e70be | -3.66852 | -51.71497 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 978c0b06-1509-39a2-b023-488d19f54d05 | -5.13297 | -43.3885 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 927537af-9d7d-3cc8-b398-d71d46dd6d6b | -5.62076 | -47.12212 | 2025-11-01 04:38:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eb75185-6bc9-3b1e-83b3-285f5a8b00e3 | -3.10836 | -45.23751 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 51a145b0-e2f8-31d2-bade-a9fc235cbbd5 | -3.75164 | -52.17374 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 686750f5-45be-35cb-87c8-5767968b4f0e | -4.09138 | -43.557 | 2025-11-01 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba4660f4-ff26-3cba-a729-48edc7c91b28 | -5.88649 | -44.5206 | 2025-11-01 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 46f3bf16-8a8c-3a2f-9946-96296f7af407 | -3.07213 | -51.25125 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8a5500f-19cc-36d5-a9fd-80ad5b106771 | -5.12878 | -43.38792 | 2025-11-01 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c8d664bb-d218-3284-aa35-9fa34842cd75 | -2.6327 | -47.95085 | 2025-11-01 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c34d8f8-2718-3fb6-9146-29be8f8d9265 | -4.85207 | -47.52816 | 2025-11-01 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1b5dcc5-b8c5-307c-b8f6-f22671da5dc9 | -3.23516 | -50.65524 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1738cf80-7325-38bd-96ac-f18398a8f19a | -3.48822 | -50.21297 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1da77300-0121-34d7-970e-872825824ee2 | -3.23208 | -50.586 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| c0c32937-d602-3199-9525-c63faa2d8adc | -3.52823 | -47.553 | 2025-11-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a81d4cd4-a22f-3d72-9e67-a2cd563ed14a | -5.80608 | -44.54748 | 2025-11-01 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c72938e4-f1b0-35c3-bfa7-25b3bd2242b5 | -3.23267 | -50.58228 | 2025-11-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 274d6b43-f332-349c-a244-36cb75b2d603 | -1.9399 | -54.18466 | 2025-11-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb16a7f4-b6d0-3e70-8755-86e71fa9e566 | -5.51474 | -48.18717 | 2025-11-01 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfe6a418-944c-384f-8727-b929c549961f | -5.90881 | -44.64025 | 2025-11-01 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 860c5061-6e0a-30da-a48d-db27982a96b0 | -1.51695 | -54.52193 | 2025-11-01 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d99e3328-4533-3679-a695-dd5164df1258 | -5.64076 | -46.80489 | 2025-11-01 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc5cf4e1-9df3-3cec-ae78-dd56b2b3ea03 | -5.45748 | -45.40311 | 2025-11-01 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce5910de-3212-3380-abf5-f4002bb233a5 | -3.59335 | -54.04274 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09cd3c55-d112-371c-888e-6b6f23f7a86c | -3.76079 | -52.21063 | 2025-11-01 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd70feb9-663b-36eb-abb9-f6b491952d69 | -4.94335 | -45.51095 | 2025-11-01 04:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f3485a9-c47c-30d9-b8c7-0c6cb006a332 | -4.70596 | -46.44804 | 2025-11-01 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5b4fce3a-984b-3254-aed8-8b136bb188d2 | -5.91985 | -51.41811 | 2025-11-01 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a3da436-5f59-353a-aa97-20ceb1c912dd | -5.09512 | -47.71155 | 2025-11-01 04:38:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3eb5bf91-a96c-36fd-9012-07e32c4edb08 | -8.56964 | -40.91251 | 2025-11-01 04:38:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 98f031e8-b4ab-3e5c-a856-9024e2a5896c | -3.59394 | -54.03902 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0ae2995-e54f-3ad7-ad66-8d78a78ce35b | -3.47356 | -53.4979 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eb51638-817d-39d1-a26b-32a50195c27e | -5.0133 | -45.82199 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42313594-b44a-3b0e-8a47-9b594369bb18 | -5.40265 | -48.25206 | 2025-11-01 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3cc5248-1bc9-3f7b-bad3-45bb3484e547 | -5.54207 | -48.38395 | 2025-11-01 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bcc7e33-ff27-3c8f-9c85-a9cef07c9ccc | -7.3505 | -46.21191 | 2025-11-01 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf877f9d-6d6c-3703-94d7-dc2e93c46ab2 | -4.08677 | -43.56002 | 2025-11-01 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c59fb93-cfb7-3ea0-9f5e-7a2d1ad9eeec | -3.07633 | -51.244 | 2025-11-01 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d1064e2-7eec-3204-80af-7f5b354f69bf | -5.60119 | -49.07619 | 2025-11-01 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a06ba91d-4d27-321a-b2fa-2c1529b40312 | -3.46185 | -52.86977 | 2025-11-01 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5940979-4982-356f-a503-1951a625d9c2 | -1.49437 | -53.12349 | 2025-11-01 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d010d8e-142b-3a82-9a40-c1855d36daba | -3.58572 | -50.81266 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 063eccfa-060f-3c18-9768-06c4034badce | -5.14232 | -49.87099 | 2025-11-01 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cb719de-df31-397a-9fcc-1f778d97be77 | -4.55065 | -45.80014 | 2025-11-01 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d01bb039-cc87-3bef-b562-d3d1202b4b86 | -6.56667 | -52.79698 | 2025-11-01 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2ceeea0-8461-3399-a353-fe4441ebd271 | -3.6022 | -50.62057 | 2025-11-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a38b85a8-b332-391f-b79c-a5d6946e3931 | -4.80626 | -45.72961 | 2025-11-01 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7389063-fb79-3df6-8386-50f4b25b415b | -3.74429 | -53.39652 | 2025-11-01 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 233fe935-7f15-3e89-9b2b-2b5ee1349449 | -5.53871 | -46.53838 | 2025-11-01 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8154c569-b4fc-3619-96fe-31857cc861cd | -1.99963 | -46.39318 | 2025-11-01 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e8a3303-7063-30a6-aaea-a1a0b7c49fec | -3.11693 | -45.23017 | 2025-11-01 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdc6ab3f-8261-3e86-b0f3-e6710e7b2007 | -4.95553 | -48.26091 | 2025-11-01 04:38:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cff19d72-85b5-3e5a-9dcf-172542bd5264 | -5.22249 | -44.80012 | 2025-11-01 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c325665-d3e6-3c46-945b-0778c989ab0e | -4.57507 | -49.41119 | 2025-11-01 04:38:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40ee4594-1c49-3433-8dee-f4ae221389cd | -5.09089 | -45.42533 | 2025-11-01 04:38:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f561d48-0133-3e13-b5d4-e5576544e439 | -5.26166 | -45.61092 | 2025-11-01 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6b1fcaa3-4c3f-328f-9c26-3198ccf85601 | -4.14718 | -50.68606 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35430e61-fb88-3ab3-ad53-f81dc1976983 | -4.79479 | -46.47334 | 2025-11-01 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ddab287-ad0e-322b-9505-e01a560ab7e1 | -4.57177 | -49.41066 | 2025-11-01 04:38:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13f9c892-f473-3daf-8d38-371aafb39146 | -4.45082 | -44.21488 | 2025-11-01 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fbe6f219-fca5-33fb-a217-e3c8e3ec7fc1 | -5.26113 | -45.61218 | 2025-11-01 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 00dd016f-1531-32b2-af11-dd244e8b8451 | -4.50047 | -45.66995 | 2025-11-01 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69ba33ec-66f4-3334-b357-23eab86721d2 | -5.92775 | -43.36852 | 2025-11-01 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bfe79139-1c5b-3fbc-be2d-739128285721 | -4.55221 | -50.30637 | 2025-11-01 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README17.md)
