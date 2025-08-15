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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7224cdd-8c3b-3384-9778-4fb052838a76 | -5.6029 | -45.380901 | 2025-08-15 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 444605d4-5a7b-3b72-84cc-eb859bb11093 | -14.0729 | -46.3172 | 2025-08-15 00:21:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3ab6baff-12e2-3202-8eb0-72bd8e9be875 | -9.0364 | -40.512299 | 2025-08-15 00:21:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| accaa406-7628-309b-99de-be56038c8c8b | -4.2229 | -47.204399 | 2025-08-15 00:21:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e0b2e92-52bf-3edc-b45e-f6d8f1fe3048 | -3.3783 | -47.608601 | 2025-08-15 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ef75254-f340-3702-a95d-b1fae96e3c5f | -12.3036 | -44.3414 | 2025-08-15 00:21:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f4f95a39-ee89-37d5-9ab7-77350721270c | -6.9601 | -42.8703 | 2025-08-15 00:21:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a5d64177-4b40-3e06-a025-ab750ba96e74 | -8.5183 | -43.328201 | 2025-08-15 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2821ec0-eb1b-3db9-88dd-d75f3014b7c3 | -12.7511 | -44.416698 | 2025-08-15 00:21:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10847288-d5f4-3b29-bb13-021fc78484a8 | -7.2904 | -43.8223 | 2025-08-15 00:21:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 64a64b38-c9a1-3601-ad4b-77f87820d171 | -4.1887 | -40.751099 | 2025-08-15 00:21:00 | METOP-C | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 87b3d059-a2f0-3231-bfbc-5471b2407cd0 | -6.9111 | -45.201401 | 2025-08-15 00:21:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a41e026f-045f-3982-959a-3e811536d581 | -2.9065 | -48.296902 | 2025-08-15 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8040b3de-d4b0-39d7-8ab7-cccd4af62d37 | -12.4157 | -43.4907 | 2025-08-15 00:21:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 995f11ea-a465-3418-8e98-372b858398f9 | -12.7627 | -44.422501 | 2025-08-15 00:21:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfe85693-1abd-3a24-87d7-3448d4737be2 | -11.9196 | -43.433201 | 2025-08-15 00:21:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 86f93bf8-e070-3436-9703-3da5449ccbe4 | -12.5907 | -46.949501 | 2025-08-15 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0efd21ae-9287-3632-b4ec-952c424ee030 | -21.1929 | -45.6945 | 2025-08-15 00:21:00 | METOP-C | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 93edc9fd-5b50-3b6f-a536-795cfee5ce3e | -4.5955 | -43.309601 | 2025-08-15 00:21:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e277d6b-0ff7-3000-a728-5ba9e6fe4eac | -4.5986 | -43.3232 | 2025-08-15 00:21:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99c11d24-7021-363b-b099-3d0d5b4563c6 | -9.8172 | -47.749298 | 2025-08-15 00:21:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 397b525a-3ce4-310e-bbd5-7f879a2b1589 | -9.0382 | -40.519798 | 2025-08-15 00:21:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| fd5ab2b1-319b-351e-9ed7-0e5695d9afed | -13.3247 | -45.229301 | 2025-08-15 00:21:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 523e1de1-3ae5-32a9-85ac-ac564174aa6a | -13.3851 | -44.310699 | 2025-08-15 00:21:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e2aaccfa-7bbb-3d5d-80a2-edc1bac53bfb | -2.3903 | -47.652401 | 2025-08-15 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7f7e866-a31d-3b27-b2aa-e14448766958 | -5.6012 | -45.373501 | 2025-08-15 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38dedaf2-0fcf-3094-8d65-5b4754ac835a | -3.4328 | -49.0378 | 2025-08-15 00:21:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e33da55b-0305-3a79-a5d1-0fbdd7846181 | -4.3956 | -41.906399 | 2025-08-15 00:21:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 512e557a-a606-3a68-a49e-ced9b80c3ebe | -6.2216 | -43.339001 | 2025-08-15 00:21:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3e16048-eb94-32d6-8a2f-8f0107a7d21f | -12.427 | -48.689999 | 2025-08-15 00:21:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 060adba2-0dc8-3141-a046-34ca7d30ed40 | -10.5377 | -42.551102 | 2025-08-15 00:21:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 78faa196-02ff-3a8a-bfbe-a6c9d3e95e98 | -11.913 | -43.449902 | 2025-08-15 00:21:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 408aba73-f188-3deb-b121-eeb8720c6115 | -13.3345 | -45.2272 | 2025-08-15 00:21:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3673ce50-a64e-3b0e-a146-81d878796e49 | -13.4695 | -43.750702 | 2025-08-15 00:21:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7bbd8457-7bda-30f3-85b0-c7b38782fed7 | -5.7668 | -46.6619 | 2025-08-15 00:21:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8985cc53-7206-3eae-88cd-21cfc96affa8 | -8.6097 | -45.626499 | 2025-08-15 00:21:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 072252eb-b8af-37fb-8b74-25eecb4b562a | -19.377399 | -42.9291 | 2025-08-15 00:21:00 | METOP-C | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5681585c-7e9c-30cf-b5c6-ad9e39a4c83d | -11.9244 | -43.455002 | 2025-08-15 00:21:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d2da347-8bc3-3144-a829-e673ef622583 | -2.4865 | -47.577099 | 2025-08-15 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6beceb5e-114d-3bef-a12d-f141f19544cf | -3.3763 | -47.5998 | 2025-08-15 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0379f14-8d78-3e1b-9096-a1799bbba40b | -5.1771 | -37.606499 | 2025-08-15 00:21:00 | METOP-C | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 876d1f0d-440e-3f56-97b9-1e29fd90b9cb | -5.8184 | -47.865002 | 2025-08-15 00:21:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 105f26d7-3097-374e-a8b3-f5003b0bad88 | -7.011 | -43.8629 | 2025-08-15 00:21:00 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd8b48a-0aeb-36be-8f3e-d477a2ef5a19 | -6.9498 | -44.548801 | 2025-08-15 00:21:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c30944a-f8ff-3e37-8ac9-20eae1bab469 | -6.9699 | -42.868 | 2025-08-15 00:21:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 319cdb32-678b-30b0-9712-0811f8e5cd5d | -7.0199 | -47.452801 | 2025-08-15 00:21:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7241c2ec-6d2c-3d64-a0a6-ea4cdd378613 | -9.1901 | -45.322899 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f7436b39-596c-328b-9200-ff7e11fd7ce9 | -11.9228 | -43.447701 | 2025-08-15 00:21:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1b12eb2-b08a-37f9-8d72-2370fb7c2e9b | -6.59 | -44.6437 | 2025-08-15 00:21:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 675a43bf-3e12-375d-aa51-a4feb3796808 | -12.4921 | -47.0154 | 2025-08-15 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79f26d30-9607-3264-8004-5fdce6b17f95 | -15.3933 | -46.5951 | 2025-08-15 00:21:00 | METOP-C | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1ae2d315-689b-3a13-8f67-7121c533b1f2 | -22.616301 | -42.098301 | 2025-08-15 00:21:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f6a8ef78-0fae-32db-a257-72154bd8d0a5 | -12.5787 | -46.940701 | 2025-08-15 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16eab092-8f55-38a4-a80b-39df5718d3de | -7.5709 | -47.066101 | 2025-08-15 00:21:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a92ea679-c549-33d4-bada-0bb113be7e30 | -4.1842 | -42.420399 | 2025-08-15 00:21:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aa520bd5-ec85-3400-ab01-27c2396111bb | -2.4924 | -47.557899 | 2025-08-15 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc6b10a6-78c8-3985-bd2d-62af10cecdd1 | -3.8282 | -47.734901 | 2025-08-15 00:21:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65df5ea8-5e57-3797-aa77-cb5ce1f28a4a | -15.4009 | -46.581799 | 2025-08-15 00:21:00 | METOP-C | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1f84061e-e55f-3c87-8361-c7e7f74cc87a | -9.0301 | -40.529499 | 2025-08-15 00:21:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| d99c2b90-af2a-3ae3-8566-1852dd323ef8 | -8.3381 | -40.971699 | 2025-08-15 00:21:00 | METOP-C | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0090745f-a023-335d-9278-c64996fa048a | -16.6026 | -47.055901 | 2025-08-15 00:21:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4ddbe787-44c1-3b26-aaa9-7acaf10586f8 | -12.4255 | -43.488499 | 2025-08-15 00:21:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea6dd8a-17b2-379b-aad7-6f4fbf6b8f30 | -16.695499 | -41.014599 | 2025-08-15 00:21:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3e75611-44c1-315e-a3a7-fe30d7a322ea | -11.931 | -43.438202 | 2025-08-15 00:21:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69cf4cf1-1c23-3468-87d6-1e475d4f0a66 | -8.3189 | -45.009499 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2e773f6f-0674-3164-a96d-2355284d752f | -14.2404 | -44.570499 | 2025-08-15 00:21:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b6d9352-e516-30d4-92c3-c4a172c7ba00 | -8.3074 | -45.0042 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a488d76-6dca-36d9-848a-5dde658ad1eb | -4.6084 | -43.320999 | 2025-08-15 00:21:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18a836a7-ed57-3030-9c02-59a6a49bb98c | -9.0284 | -40.522099 | 2025-08-15 00:21:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| a9d2660a-cba1-317c-98cb-d8aa964ba08b | -7.8557 | -48.234001 | 2025-08-15 00:21:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5688da3a-7dde-3c1c-944f-6d4912badfa3 | -9.8074 | -47.751301 | 2025-08-15 00:21:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d5a0195-32bb-3e3e-8df9-33979b079e50 | -5.5505 | -45.376999 | 2025-08-15 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cccf382-5cfd-3ff1-9543-3c22752c5d13 | -9.0462 | -40.509998 | 2025-08-15 00:21:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| cef6be70-b959-3879-b361-a960a4a42fbc | -4.2267 | -47.2216 | 2025-08-15 00:21:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06bc7ff4-a386-3808-b7ba-d39816c91074 | -7.4384 | -49.2383 | 2025-08-15 00:21:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 21f06bb4-4d83-3ea4-9957-061aae80aee2 | -20.9797 | -47.424702 | 2025-08-15 00:21:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 68130609-d55e-38b4-a0b0-c24ac6798204 | -5.5472 | -45.362301 | 2025-08-15 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7f242c2-17ca-3f0c-b26d-43239de1b69e | -2.9163 | -48.294701 | 2025-08-15 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d5d1538-b585-3fd1-977e-566593cb964c | -4.5888 | -43.325401 | 2025-08-15 00:21:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad5d61a7-d207-30c5-8182-da53c8065b06 | -7.292 | -43.829201 | 2025-08-15 00:21:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db8a462d-a091-37ae-9df8-90411052a745 | -9.1803 | -45.325001 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 69456d45-1a8a-3de3-ba73-b2ac07ade182 | -5.757 | -46.664001 | 2025-08-15 00:21:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed9f7ad6-2dab-35b8-9ffd-54209b4e498b | -5.228 | -43.188999 | 2025-08-15 00:21:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7d125a7-a31e-3638-a60c-6673fbb21a86 | -15.3911 | -46.583801 | 2025-08-15 00:21:00 | METOP-C | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4e34b038-38e2-3419-be8a-136688f1b7b9 | -7.8631 | -48.220798 | 2025-08-15 00:21:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce60e17-5bef-30a6-9bca-c021eb1d0c4b | -9.0266 | -40.514599 | 2025-08-15 00:21:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 86402db2-0c6c-382f-9153-f7c03da061c0 | -7.3843 | -44.878899 | 2025-08-15 00:21:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b11dd214-b56f-3dd4-b934-117f40cce1b3 | -3.4454 | -48.956799 | 2025-08-15 00:21:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d4d3d19-78b5-363a-9bb7-742b011eebd2 | -7.3908 | -44.862 | 2025-08-15 00:21:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c53b796e-6d27-3c08-b49d-bb369ff60844 | -8.5203 | -43.291401 | 2025-08-15 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 98dfbcc3-8626-3ec5-889e-cf8c6a4ebc11 | -6.4921 | -42.853401 | 2025-08-15 00:21:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 02b93cb9-ed75-3776-8b69-c693f93373d3 | -10.9586 | -49.563301 | 2025-08-15 00:21:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d37c8242-8815-3d84-8953-fd9cd07a1797 | -4.665 | -48.860699 | 2025-08-15 00:21:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b06cd140-3f66-362d-9fc2-2e50204031a3 | -14.0631 | -46.319199 | 2025-08-15 00:21:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a3cf2e00-8744-3ab4-b22c-934b570626e2 | -8.5167 | -43.321201 | 2025-08-15 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f1b42619-930b-3158-9bd0-11d4d71e61e1 | -11.814 | -44.262501 | 2025-08-15 00:21:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1ed8706-ed77-34a1-96a5-97c478a124bd | -14.2422 | -44.578899 | 2025-08-15 00:21:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 304121e2-109e-3d08-90e8-b699b0ce33c7 | -9.7229 | -48.027302 | 2025-08-15 00:21:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 452f13ed-a7e8-366d-bf80-194b2829c39d | -11.9212 | -43.440399 | 2025-08-15 00:21:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bff84bdb-e7a6-3cf7-bfbc-132715d1d33b | -6.5089 | -42.792 | 2025-08-15 00:21:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README4.md)
