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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6838a22-4aef-3e43-a179-d70db879b7b2 | -17.3048 | -42.6182 | 2026-06-06 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 1f28b8ac-6a20-318c-bac7-4ba939e946f1 | -6.0502 | -47.8841 | 2026-06-06 00:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| b8891d21-71db-3859-baf5-4d6885c094fe | -19.7513 | -53.5407 | 2026-06-06 00:00:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 78f219c5-229b-34ad-bbab-16a67e4b90cf | -17.3041 | -42.643 | 2026-06-06 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 280.2 |
| 71655a61-bc49-366c-91c0-7f88548a8634 | -18.0 | -54.2889 | 2026-06-06 00:00:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 49.1 |
| d924dd72-9afa-33e6-8dda-7ebdea56ea64 | -17.3242 | -42.6381 | 2026-06-06 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a9822915-124b-3e75-920e-08d849b085e1 | -11.5309 | -52.7887 | 2026-06-06 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| a15f06e3-9081-3e09-8805-c0d86376d065 | -11.5686 | -52.8057 | 2026-06-06 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 3d18bf01-28b8-3b3a-98f6-f380b29ccbcd | -11.5496 | -52.8076 | 2026-06-06 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 335.9 |
| c04ff3bb-3223-31e6-8718-d207bb5bc378 | -17.3034 | -42.6678 | 2026-06-06 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.0 |
| ee08bb2c-713a-31f2-9a94-31286e71dea8 | -12.5103 | -46.2863 | 2026-06-06 00:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| bddbee58-b004-3f25-90ce-078af981c6e0 | -11.5306 | -52.8095 | 2026-06-06 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| d4ed2563-e887-32b1-9370-84764d786a54 | -11.5688 | -52.7848 | 2026-06-06 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 174.4 |
| fffcce18-fc98-3e5a-bedc-800460b8eb48 | -11.5499 | -52.7867 | 2026-06-06 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 366.7 |
| ebcc504e-0f1f-39b4-9f05-d54dbd16d256 | -6.05 | -47.9059 | 2026-06-06 00:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 5bcb1841-9bf8-3f07-8a07-f406b9936a16 | -19.7513 | -53.5407 | 2026-06-06 00:10:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 70.0 |
| c09262da-2897-361e-825f-2cd6b8e3185b | -17.3041 | -42.643 | 2026-06-06 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 4cb9a769-8ad4-34cd-b1b6-904677d5eca0 | -11.5499 | -52.7867 | 2026-06-06 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 325.0 |
| 80dd32a4-6f40-39da-a7b6-d42bd63dbec7 | -11.5496 | -52.8076 | 2026-06-06 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 219.3 |
| cef6c9e2-70f3-38c3-af63-daf5f5627f97 | -12.5103 | -46.2863 | 2026-06-06 00:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 7c6d3628-4716-36da-86b9-0bd6fce657f1 | -18.0 | -54.2889 | 2026-06-06 00:10:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 4d0df5f3-33e2-3b97-95d0-41c7a1e7d18a | -11.5686 | -52.8057 | 2026-06-06 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 153.0 |
| da4a3ed5-e095-3e82-a944-119a9913ae07 | -17.3242 | -42.6381 | 2026-06-06 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d1612ad1-57ad-3147-9766-afe2dbb66c72 | -11.5309 | -52.7887 | 2026-06-06 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8a3d233a-a575-35d0-ae17-c7bf32b7735d | -17.3048 | -42.6182 | 2026-06-06 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 48ff10ef-8403-331b-86ea-35928bdf97a8 | -11.5688 | -52.7848 | 2026-06-06 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 228.7 |
| 7184e59d-77aa-39bb-af14-dd3822343747 | -11.5686 | -52.8057 | 2026-06-06 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| e953ddbb-572f-3bc9-b7f4-796079c5fbef | -11.5688 | -52.7848 | 2026-06-06 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 8e8c48a5-e4c0-3518-862d-52c366339c1d | -17.3041 | -42.643 | 2026-06-06 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 6ebcbd99-19c0-3a28-8770-ccc26fc0ee15 | -6.9793 | -42.8798 | 2026-06-06 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.2 |
| b8aa6292-2029-3fe5-a71f-2fb69d0cc97f | -17.3048 | -42.6182 | 2026-06-06 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d883391a-aa32-3f89-b32f-3caaf121ed36 | -17.3242 | -42.6381 | 2026-06-06 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.9 |
| bf9aa8f0-1a98-3074-aa2b-5156146f7f89 | -12.5103 | -46.2863 | 2026-06-06 00:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b67f0838-d9a1-3210-9029-9181e924251f | -11.5499 | -52.7867 | 2026-06-06 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 338.6 |
| 77a08b4e-643e-3efd-8fae-9c6536678b5c | -11.5496 | -52.8076 | 2026-06-06 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 272.1 |
| 2997fe44-743c-3b1a-b98a-748126f67b16 | -18.0 | -54.2889 | 2026-06-06 00:20:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 36e65e0d-538e-3c58-9c50-45e441dbfe2a | -19.7513 | -53.5407 | 2026-06-06 00:20:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c1d02a32-7cfb-3151-8542-b6252f3b68d4 | -6.0502 | -47.8841 | 2026-06-06 00:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 0aac6994-3935-3e1d-b98d-16e2e187bee6 | -11.5686 | -52.8057 | 2026-06-06 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| df03b8b1-dbe4-308a-b983-e2f3e65761ba | -17.3242 | -42.6381 | 2026-06-06 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 032b3c7a-6c44-351b-8f2b-6968d0ba9bdb | -11.5496 | -52.8076 | 2026-06-06 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 273.0 |
| b9f9a84f-7ff3-321b-9377-8846d1b03c09 | -17.3041 | -42.643 | 2026-06-06 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 94674fea-e2bd-3e68-a976-b81f7ae6598a | -11.5688 | -52.7848 | 2026-06-06 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 6cceddea-f938-3975-90f7-b51cebbbfc7a | -17.3048 | -42.6182 | 2026-06-06 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 52.2 |
| bff739b1-aef1-3eb2-89bf-87147e498fd1 | -19.7513 | -53.5407 | 2026-06-06 00:30:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 51fc5266-ad5f-3a28-ba29-29a0dc2d5b42 | -11.5499 | -52.7867 | 2026-06-06 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 291.0 |
| 34cb64a1-edab-3ce3-ba81-01e2aa27b882 | -18.2119 | -49.9535 | 2026-06-06 00:30:00 | GOES-19 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 54.5 |
| c9ae9f68-88fb-3e69-8af9-c3bf26e3449c | -19.7513 | -53.5407 | 2026-06-06 00:40:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 70.4 |
| bf0fc737-f987-3cf8-b2cb-4cf5d8114994 | -11.5309 | -52.7887 | 2026-06-06 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 5cc3ff73-6ef1-3da4-8ed9-7e30e5b58752 | -11.5496 | -52.8076 | 2026-06-06 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 0608a121-d126-3e0b-8249-92cb7bf192ab | -17.3041 | -42.643 | 2026-06-06 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 2430f9fe-a98b-345c-9656-89c87369ac3c | -18.2319 | -49.9497 | 2026-06-06 00:40:00 | GOES-19 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 846f49ed-55a6-31f4-9f92-cf0db795dd2c | -11.5499 | -52.7867 | 2026-06-06 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 248.5 |
| d5b66c1b-4ed6-3c52-be5a-79a4e571eac0 | -17.3048 | -42.6182 | 2026-06-06 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 6e653cab-0ff0-3340-9bdd-8e95b06d2a0a | -18.2119 | -49.9535 | 2026-06-06 00:40:00 | GOES-19 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 10476692-bbe6-37db-9d34-f26029bb914a | -18.2124 | -49.9311 | 2026-06-06 00:40:00 | GOES-19 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 3e7e79d0-89b4-33b1-a06b-83f4f85234d1 | -11.5688 | -52.7848 | 2026-06-06 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 166.2 |
| e8af58c5-7c29-3350-85fd-d8e5060bcd69 | -17.3242 | -42.6381 | 2026-06-06 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a4ab0ce5-4647-300d-ba94-de64baf8356d | -11.5686 | -52.8057 | 2026-06-06 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 0ac49d60-b12b-3eb8-b2db-b657f24e3a67 | -11.5688 | -52.7848 | 2026-06-06 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 9ff0f776-965f-3fde-b037-c30fe40ea635 | -11.5686 | -52.8057 | 2026-06-06 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 25ec531d-accf-3b9e-8269-2b739650101d | -19.7513 | -53.5407 | 2026-06-06 00:50:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4bbc1b42-c5cd-3511-8c5a-b4512826c50b | -17.3242 | -42.6381 | 2026-06-06 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 34492c03-d137-36ea-a16d-82cfd732162e | -17.3041 | -42.643 | 2026-06-06 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 7eee4ee1-3044-3c76-9ed3-6f8d00abbdd3 | -11.5499 | -52.7867 | 2026-06-06 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 238.8 |
| 36fc23b8-166e-3e4d-937a-77ffe6d9e8ae | -17.3048 | -42.6182 | 2026-06-06 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ae8e2e58-bc80-358a-a09c-5d5ac4ceb154 | -11.5496 | -52.8076 | 2026-06-06 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 2fd86dd0-63e4-3767-8745-d720f5b48b5c | -11.5686 | -52.8057 | 2026-06-06 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 3d674e48-bb78-3eb2-b68e-2f82304e2302 | -11.5496 | -52.8076 | 2026-06-06 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 6de197ea-5f30-3a60-be19-a9f0d90365b6 | -19.7513 | -53.5407 | 2026-06-06 01:00:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 53274197-f122-3e62-a779-22216fe267c1 | -17.3041 | -42.643 | 2026-06-06 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 9990a883-02b1-3dc8-bda0-99f20832fbaf | -17.3048 | -42.6182 | 2026-06-06 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 51.5 |
| ea1a11b1-46a3-3cb4-8241-1fe01a6569d6 | -11.5499 | -52.7867 | 2026-06-06 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 179.8 |
| 49269bf8-1be7-394a-86d8-5eeeb945de28 | -17.3242 | -42.6381 | 2026-06-06 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 2e8a1034-f10a-3c5e-8646-b2c8a52d4a96 | -11.5688 | -52.7848 | 2026-06-06 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 50b77662-910b-385d-b6ed-dce453003d19 | -14.45503 | -54.89254 | 2026-06-06 01:05:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 6e95cdbf-acd7-3db5-909e-1e80494deb1e | -19.74452 | -53.54428 | 2026-06-06 01:05:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 103.2 |
| fd583ca9-edb3-35da-9410-39eb9bf97ec4 | -19.74841 | -53.56601 | 2026-06-06 01:05:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 0d1849d0-ca4a-3b13-8608-6ce576c0de0d | -21.84942 | -55.82368 | 2026-06-06 01:05:00 | TERRA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bd72d81a-fe3c-3a81-a294-a5ea0e317e52 | -18.00212 | -54.28658 | 2026-06-06 01:05:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 9200338a-3f5a-380b-89e9-21b006b3ddc2 | -16.60298 | -58.2407 | 2026-06-06 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 9e41f457-96c0-3a45-bd2c-b7a8e82678c1 | -21.98307 | -57.60898 | 2026-06-06 01:05:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 25e749e9-88e9-3a56-aa6b-34989666c41a | -16.13911 | -58.49774 | 2026-06-06 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| ca4444eb-4eb9-3690-8a2b-26bb26101ec0 | -16.60118 | -58.22909 | 2026-06-06 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 2a22229d-91df-3dc4-94ae-4388eac068fc | -14.45873 | -54.89827 | 2026-06-06 01:05:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 9b96908c-14a5-3fc8-b33e-727c42b2579f | -9.17181 | -58.06553 | 2026-06-06 01:07:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| dff82120-6900-3c9f-b5d4-253ea768c034 | -14.08621 | -58.88684 | 2026-06-06 01:07:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| b67617dd-627b-3b26-a042-ab016ec8823b | -11.55952 | -52.77859 | 2026-06-06 01:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 79549d56-c1ed-3031-aa67-a8cae3ec7f34 | -11.54908 | -52.77382 | 2026-06-06 01:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 1968427c-9501-3995-8d99-23e826cc012c | -10.03553 | -59.34341 | 2026-06-06 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 49267803-45ed-37b6-a953-f8c726ed74cd | -11.54316 | -52.78161 | 2026-06-06 01:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 64b66d57-81db-3ae3-b3ff-f20682234f10 | -14.0845 | -58.87537 | 2026-06-06 01:07:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 1f9cc68e-1c4c-3782-b08c-b57a49fbabfa | -13.49706 | -56.56555 | 2026-06-06 01:07:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bdcc814a-199c-3b2e-8899-62242aa2ce9c | -12.79691 | -54.86777 | 2026-06-06 01:07:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| fb2311f5-9cfb-3480-bb4b-47bcab2d13fd | -11.05259 | -56.91883 | 2026-06-06 01:07:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| cec5d6c0-2e85-30bd-97e8-fe10caf79b86 | -11.55541 | -52.80948 | 2026-06-06 01:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 317.7 |
| e5d606b8-5c36-30ae-99c2-9a4b8f5cf8db | -11.54924 | -52.81722 | 2026-06-06 01:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 174.6 |
| d3ac3919-44c9-33c0-8de5-57cc97c84af0 | -9.1701 | -58.06013 | 2026-06-06 01:07:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 14f67d44-5ddb-3707-b9f6-52c345148043 | -9.1725 | -58.0754 | 2026-06-06 01:07:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6142f406-f4ce-371b-9c2f-76b193b49027 | -11.56558 | -52.81435 | 2026-06-06 01:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |


[Clique aqui para ver as próximas entradas](README2.md)
