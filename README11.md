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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 302fc8da-a768-3fba-9410-f685401aa4e0 | -14.20534 | -57.40646 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6c72b3be-83a7-3269-abbe-fd4c0d106aa1 | -15.1168 | -52.95254 | 2026-01-16 05:08:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81f249c0-d25a-3942-a012-1a85a3c098f6 | -16.10639 | -56.76115 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d168462e-c7a9-3733-9466-22f18dd705bc | -13.69148 | -55.67982 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| aad35941-758c-3558-b35b-5de8fae6916e | -17.61108 | -46.66053 | 2026-01-16 05:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b11236a7-102c-32e3-8271-906027d8dd91 | -15.44401 | -56.32885 | 2026-01-16 05:08:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 952a089f-bd74-34e2-a2f4-d26ab872de0e | -13.69891 | -55.6771 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 306457db-ddd6-3da6-9dd8-59c5da1479e2 | -12.92082 | -49.4833 | 2026-01-16 05:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 49a92f8f-fa90-31bc-bf46-98f69b80e238 | -16.45716 | -57.5683 | 2026-01-16 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8a507407-d8d4-3a24-82fd-a0ac596bb72a | -15.88238 | -57.79516 | 2026-01-16 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f2de499b-aa19-33e9-9944-50daa7a18591 | -15.42984 | -56.33047 | 2026-01-16 05:08:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2e2d3ced-9d95-3bf2-b8c1-eaa44f7eb594 | -14.21639 | -57.40099 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7389b061-4f8b-3066-9aa7-df71ee2f526d | -13.69606 | -55.67276 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f76ca9f2-8f19-37bd-922e-04fd92039102 | -17.61582 | -46.66112 | 2026-01-16 05:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a25804ab-669d-3613-b882-bfe484afc638 | -16.11427 | -56.75481 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 10d329f1-c71f-3659-b175-f7b0ff480e11 | -16.10358 | -56.7569 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fcfacf5-fdfd-3a53-8ee6-8fb95b0f7a10 | -15.77761 | -55.75198 | 2026-01-16 05:08:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b5e7022-db61-3511-9a27-a89fe85905f7 | -16.40581 | -54.5355 | 2026-01-16 05:08:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 283da0fd-9edf-33d1-b340-9a556c3071be | -15.59335 | -57.34269 | 2026-01-16 05:08:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b13d2a55-9fce-3173-93fa-e4cf66736c5e | -14.20589 | -57.4029 | 2026-01-16 05:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9123adb8-2abd-318f-b337-0eadc0c6ee41 | -16.11483 | -56.75109 | 2026-01-16 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5fd949e5-13ae-3201-af20-4968a587ecc6 | -15.43381 | -56.32724 | 2026-01-16 05:08:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7176ca96-35bd-366b-b5e8-629b54d2bf87 | -18.8119 | -51.6134 | 2026-01-16 05:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 50f3f435-dd43-3bc1-96d2-6f60fa70a054 | -13.6993 | -55.6773 | 2026-01-16 05:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 70290f6b-ebad-3133-95b0-6e7589bc4e85 | 2.7634 | -60.315 | 2026-01-16 05:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6305a911-0a0b-3f90-990c-72b9e75f2a41 | -20.43418 | -57.83126 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a8b903d0-38dd-3514-b88e-a707b263fb82 | -20.7299 | -55.15966 | 2026-01-16 05:10:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82b25560-d6fa-3403-8eb5-546ec0f3edce | -20.43812 | -57.82801 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 453ed5cb-38f3-3c88-b955-5260b58aa229 | -22.02969 | -56.30775 | 2026-01-16 05:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7143235-0e35-3889-8e92-c559fed0ec5f | -20.72549 | -55.16389 | 2026-01-16 05:10:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a81267ec-7c49-3543-a4e9-9a74ea07084d | -20.42447 | -57.81926 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 67b813c2-24d4-3805-a2cd-80963630bbbd | -21.22604 | -56.25291 | 2026-01-16 05:10:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5229914d-97bd-3628-a151-6e4eb8634a5f | -20.41779 | -57.7947 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 2772b6a9-63ce-3f21-a565-7da81134c982 | -20.44654 | -57.84115 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e35c50b4-3173-3953-89b5-277d68913232 | -20.42117 | -57.79527 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1863d0ad-987c-367c-98f3-201f0da974ef | -19.17625 | -57.54359 | 2026-01-16 05:10:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 762ec2d1-c0eb-3031-ade0-28cabe42d5c9 | -20.44317 | -57.84058 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 36ae5652-4119-382d-b559-e978698460a5 | -22.03392 | -56.30386 | 2026-01-16 05:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74d39aa2-1d9e-3f7c-b652-12707d158a6f | -20.41104 | -57.79357 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a1883c4d-af21-3c7d-a402-6b3d94f6d277 | -20.44987 | -57.86511 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| eff52428-f223-3bf9-ae27-8134ff5f9fdb | -20.43022 | -57.85789 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d126bdb3-00d1-3063-8f73-18806f45207b | -20.43699 | -57.83563 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 158ccb22-5482-3f00-87a7-3d5500d77b55 | -20.41707 | -57.84532 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2a7efb38-1019-3d75-8fdf-506ce09f503c | -21.22964 | -56.25344 | 2026-01-16 05:10:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af84d1e0-c909-310a-8c3d-a2d0fed54fa5 | -20.42685 | -57.85732 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 78e55ee1-86b0-3964-a6c1-a3ff7572a33b | -19.1249 | -57.57798 | 2026-01-16 05:10:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 557692b9-34fa-38f1-8ac7-06fd63402a74 | -20.44036 | -57.8362 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 73a4c2f6-84c1-3260-8363-8a91185bc738 | -20.44373 | -57.83677 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1c769934-9537-3299-a471-dbccd5238646 | -20.38233 | -57.80046 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 177f4eb5-ed41-3773-b54a-25e8cb595e68 | -20.43639 | -57.86283 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| efbade34-6509-3ff9-a3e0-70d0e04f0630 | -20.45044 | -57.86131 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| a9f6e662-1792-3ffa-a153-b615c0d8c1d4 | -20.43756 | -57.83183 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 85070075-a8c0-336e-9c06-6b60c9c38b61 | -20.4137 | -57.84476 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3d33651c-c600-3511-9534-f315ce16fa80 | -20.43642 | -57.83944 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 569e85fe-c3e5-3010-bcfe-d438464d0cad | -20.40767 | -57.793 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1c931f78-bda0-3e92-b7b8-f5a1bd06b7ef | -21.35652 | -56.86712 | 2026-01-16 05:10:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 907d1c90-2c11-364c-b3ed-4ab4c696c1b5 | -20.43138 | -57.82688 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9fafb01b-811d-3f06-b3b0-77e19c14bc41 | -20.41442 | -57.79414 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 64cfa3dc-f93d-3dec-a926-61dcd21a283f | -19.17289 | -57.54298 | 2026-01-16 05:10:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8ee41a27-8340-3c50-9e94-f325ada5013c | -20.72926 | -55.16446 | 2026-01-16 05:10:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd473b7e-0a98-3884-88eb-17283b9be63d | -20.43976 | -57.8634 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| eaf5f73c-1c41-377f-90e9-72cc6b994be3 | -20.45609 | -57.84665 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 647b1169-698e-3094-8610-3c4ad7edaefc | -20.42965 | -57.86169 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 122a31e0-6e0a-31b8-b090-92c380d89723 | -20.43979 | -57.84001 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b144a870-4226-31d1-9c86-315333b04665 | -20.46226 | -57.85159 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f963f5d4-8c49-32f8-a904-91e543aee091 | -20.73304 | -55.16499 | 2026-01-16 05:10:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11cd8486-eadf-3d92-aae8-bcb173860ceb | -20.45324 | -57.86568 | 2026-01-16 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 81236091-6cb7-38a0-8043-05542485c087 | 2.7634 | -60.315 | 2026-01-16 05:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b9383ea2-99b6-3a63-b62b-b67b2a8735c3 | -18.8119 | -51.6134 | 2026-01-16 05:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0e0da949-6ed5-39e1-9d81-797d73c940b8 | -18.8124 | -51.5914 | 2026-01-16 05:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 46f7d44b-9fa1-34af-bf7f-1cc2641934b0 | 2.7633 | -60.334 | 2026-01-16 05:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| ccc946e6-0486-3748-ba65-da3c7c5f30dd | -18.8119 | -51.6134 | 2026-01-16 05:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 88c21c74-1b25-33db-9ab5-fe52276bdaf8 | -18.832 | -51.6099 | 2026-01-16 05:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| faf4eb4b-29df-3bbf-9da6-315f712102ec | 2.7634 | -60.315 | 2026-01-16 05:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 18e5de90-42b6-3b46-b816-4accf252f000 | 2.7634 | -60.315 | 2026-01-16 05:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 7fc52d04-841e-39bd-b539-741777fb0b11 | 2.7633 | -60.334 | 2026-01-16 05:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1b96438a-14d6-35db-a4e5-fc9a18e934ab | -18.8119 | -51.6134 | 2026-01-16 05:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 5b282b32-4d1e-363e-8bd4-3750d9f5732b | -18.832 | -51.6099 | 2026-01-16 05:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| b95ea985-d564-30d6-839a-5e37281eb719 | 2.7633 | -60.334 | 2026-01-16 05:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 104e3384-e139-3e5a-ab83-15208021b58b | 2.7634 | -60.315 | 2026-01-16 05:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 6e50fed3-fd41-33ec-a4dc-4af24da79d33 | 3.06146 | -60.10098 | 2026-01-16 05:52:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 070da536-2e2b-3f4f-bc08-5b27f287d859 | 4.19467 | -60.58213 | 2026-01-16 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 43842b15-e465-388f-a1e6-bc2997764fb4 | 3.81536 | -60.97884 | 2026-01-16 05:52:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3000deda-15f9-36ab-b2c4-48558caa08b2 | 3.59069 | -60.81139 | 2026-01-16 05:52:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36ce3f4d-34fb-35ec-9d15-c38b3a6909f1 | 4.19608 | -60.58327 | 2026-01-16 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06ab6ab9-7877-3a57-af8e-889f1e69a7d3 | 4.05326 | -61.466 | 2026-01-16 05:52:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8ca31a0-7867-36d3-8303-c53a8e514bae | 3.82374 | -60.45962 | 2026-01-16 05:52:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97dcae26-3015-39ea-83de-ecfa104f0221 | 4.05638 | -61.46023 | 2026-01-16 05:52:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1da00efe-4e74-3521-b8e1-5e743896f582 | 4.19544 | -60.57943 | 2026-01-16 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a98eea4-ba04-32a3-81e5-b1d900141ec3 | 3.81949 | -60.46033 | 2026-01-16 05:52:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff523717-068e-346c-b192-05944ed486c9 | 4.02352 | -60.43376 | 2026-01-16 05:52:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ac41013-c253-30a2-8f26-482c97f8c93d | 4.0493 | -61.46663 | 2026-01-16 05:52:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14febb60-e379-369e-94d6-98cae9c7a77e | 4.06117 | -61.46468 | 2026-01-16 05:52:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04bf8d7e-4353-3334-bde2-0f444cd9c845 | 4.1919 | -60.58395 | 2026-01-16 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46d631b2-5e67-3c72-961b-fecca9dfbdb6 | 2.94157 | -60.33957 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f725ed5-206a-38aa-bcfe-50a44ba8ff60 | 2.76489 | -60.33207 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| df9a89e1-5885-3147-b38c-e8e9a76f3ac8 | 2.76215 | -60.31531 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0fc5d24c-250d-31b6-a866-7a26e674de00 | 2.94091 | -60.33543 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a45bbb05-1519-3fd6-bd73-d8b902eb6b5b | 3.05777 | -60.10603 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef6a5acc-713f-3d45-8c4b-39204d0595cf | 2.75412 | -60.32095 | 2026-01-16 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |


[Clique aqui para ver as próximas entradas](README12.md)
