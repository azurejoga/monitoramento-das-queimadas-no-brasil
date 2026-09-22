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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee4394c0-396b-3fa2-b9d9-d3548c6557c3 | -7.11529 | -43.73128 | 2026-09-22 11:45:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6c7a66d6-f1e7-3d79-bf8f-449136fa492f | -3.56414 | -43.46933 | 2026-09-22 11:45:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 904e4896-587f-3cf5-acc7-3ae96991d7c6 | -4.56456 | -44.0791 | 2026-09-22 11:45:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8ed0c269-b71b-32b9-ab7a-1a0b94a53995 | -7.47858 | -45.47243 | 2026-09-22 11:45:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9341e07a-de47-3c6d-b268-4c6a4b7d826b | -9.62168 | -43.93967 | 2026-09-22 11:45:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 960a475c-ee1f-3981-b5f5-5918dbf49773 | 1.54542 | -55.86527 | 2026-09-22 11:45:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 32004a5e-a23b-3e98-9bcf-0c69e50f5ceb | -7.53202 | -46.20699 | 2026-09-22 11:45:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 03dd7744-db13-3866-acbc-f29da2a4e908 | -6.5782 | -44.15514 | 2026-09-22 11:45:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 3aae4bf9-37dd-32d4-a56b-f65f075648b3 | -6.9717 | -47.49544 | 2026-09-22 11:45:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| e3aa43ce-dca5-3e9b-8ea2-1d83f92e8cdc | -9.59812 | -47.77386 | 2026-09-22 11:45:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| efc1d699-fbb7-3561-9b40-76014322d202 | -8.90663 | -45.92224 | 2026-09-22 11:45:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f3bf1dd6-4c3e-3ebf-9de6-6f8d8648fede | -2.96369 | -50.32591 | 2026-09-22 11:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 26f61913-9bb5-32b9-b630-3824e3334a49 | -7.3576 | -45.3374 | 2026-09-22 11:45:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0cb75e2f-ee2d-3423-8eaa-f1a3a678f2a3 | -6.94043 | -42.88761 | 2026-09-22 11:45:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 91e7dc57-4c52-310b-b8bb-f2177c587034 | -8.79826 | -44.2836 | 2026-09-22 11:45:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| da919df3-7f34-3aaa-93bf-fec0a1e0193a | -7.14202 | -48.42551 | 2026-09-22 11:45:00 | TERRA_M-M | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 566cc59b-f364-337f-bdbc-5bec606298df | -7.1383 | -42.07301 | 2026-09-22 11:45:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 317fe57b-75f0-354b-9918-757e270a49dd | -8.38567 | -44.83938 | 2026-09-22 11:45:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5f59a16c-6eb0-30a0-87ae-afdcce23e4c6 | -5.32687 | -49.23267 | 2026-09-22 11:45:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ab80bd95-d1cf-3b84-b439-2f96a2ef1652 | -8.40194 | -46.51156 | 2026-09-22 11:45:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| bb3d4de6-cbd9-3524-9369-f62d2099a715 | -8.25122 | -55.25331 | 2026-09-22 11:45:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 47f9a24c-66d5-38f1-82bb-e6a4b433cac0 | -8.81619 | -45.37164 | 2026-09-22 11:45:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| daf5cdab-db72-355a-a4ff-d86750da4448 | -3.56254 | -43.48087 | 2026-09-22 11:45:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 725d2d9e-b9d4-3cc2-a366-f2019da32e6d | -5.30842 | -43.41928 | 2026-09-22 11:45:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 44f44ecc-6ef3-3b8f-9b86-eb2c83f9254c | -7.55356 | -42.67392 | 2026-09-22 11:45:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 196e400d-01b9-35b5-8ece-fe043dc996d7 | -7.14072 | -48.43452 | 2026-09-22 11:45:00 | TERRA_M-M | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| b82cdbb1-3a74-3cef-97d8-b874f9b43ea3 | -5.33406 | -43.30799 | 2026-09-22 11:45:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bcecfda7-8a99-3927-b885-7aa56047bf9a | -8.31606 | -44.76309 | 2026-09-22 11:45:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| beb34a57-68b4-3996-811e-c1fe60326445 | -7.47718 | -45.48244 | 2026-09-22 11:45:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 1d625d7a-b8dc-3b12-8236-886923381fc0 | -7.41865 | -42.65074 | 2026-09-22 11:45:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 80950629-62b6-37ac-9e61-e0f6b28c116c | -9.6155 | -43.9454 | 2026-09-22 11:45:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| 8e3c091d-aa36-321f-92e4-d3d5f096e504 | -9.5678 | -46.54321 | 2026-09-22 11:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c052cbd2-341b-35c5-802e-b2a44f5a6f8e | -7.13442 | -48.41524 | 2026-09-22 11:45:00 | TERRA_M-M | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b233d3fa-2f9c-3770-baaf-a60f6666e2f6 | -9.27771 | -46.17683 | 2026-09-22 11:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 549af0b9-f1ce-3d1b-8d7e-c5228c5f7c33 | -10.01374 | -45.20898 | 2026-09-22 11:45:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8fc6aa65-9495-31e3-b950-f4947e91907c | -8.32751 | -50.84134 | 2026-09-22 11:45:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 41ada7c0-02ff-3e02-8c61-60563b639914 | -10.01518 | -45.19804 | 2026-09-22 11:45:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ba3d12c6-2e1c-3b5e-80c7-efd10662e6bf | -10.25097 | -45.50253 | 2026-09-22 11:45:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 98aa8c90-44cc-3bd5-97aa-b436df0c07c9 | -9.57688 | -46.54436 | 2026-09-22 11:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4b695562-7f2b-3725-8b10-9243d23933be | -8.35194 | -50.88023 | 2026-09-22 11:45:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 66da23d0-0207-379d-97c1-7eee289ca927 | -6.89991 | -41.69447 | 2026-09-22 11:45:00 | TERRA_M-M | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 94ba1d85-2a91-3fe1-b574-9fcf5ff32ce2 | -8.31753 | -44.75198 | 2026-09-22 11:45:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7498a051-0dbd-305b-a96b-73c60cf8c011 | -8.79668 | -44.29546 | 2026-09-22 11:45:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| f35a6975-83a8-306a-816b-2de02c25ddcb | -7.13942 | -48.44352 | 2026-09-22 11:45:00 | TERRA_M-M | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 723373f6-e924-3824-8ad4-5f3719ad6c6e | -6.29437 | -47.65331 | 2026-09-22 11:45:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 230a50a6-9600-3263-bfb2-99b7f31c4cd2 | -8.37989 | -45.61593 | 2026-09-22 11:45:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 1f7f8ebd-f600-349c-adb3-788abb75d0d2 | -10.10942 | -46.08601 | 2026-09-22 11:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8462c6a9-11fa-3ccc-8595-d5dca1933bdf | -10.47921 | -46.28245 | 2026-09-22 11:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d48f12d3-f680-3aa8-9441-9b133bffa8ec | -9.15247 | -50.00607 | 2026-09-22 11:45:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3e29fd86-c6d8-3a57-b296-e94f7c2724fb | -6.90915 | -42.95555 | 2026-09-22 11:45:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 43ee70d9-dd3e-3f26-85ec-db739ac67456 | -9.38881 | -47.75912 | 2026-09-22 11:45:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 7a9a928d-0363-333b-9ec3-0a34542fb774 | -7.2683 | -44.03849 | 2026-09-22 11:45:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| aacbfc2e-94b2-3e28-8bc6-f9dd022d9a57 | -10.25245 | -45.49126 | 2026-09-22 11:45:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e8e3d325-d025-37ef-bd07-8fa1705aa354 | -9.61384 | -43.95856 | 2026-09-22 11:45:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 8dc9a6b2-3bb3-375f-ad90-bed0c0958ab5 | -8.37061 | -45.61423 | 2026-09-22 11:45:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 47446b8b-3517-3052-8c62-b66ad9505445 | -7.89497 | -44.84414 | 2026-09-22 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 185b9d6a-c94d-3355-9b4a-aa0839db7103 | -1.17211 | -46.82011 | 2026-09-22 11:45:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b138f3c6-0d5a-311d-8fa8-f5de2fedd21e | -9.23179 | -46.17057 | 2026-09-22 11:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fa47a000-93c0-3963-9d6c-3e27d121ca30 | -5.27338 | -49.33669 | 2026-09-22 11:45:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fd18974a-606d-3843-bb71-ddffde9d38a5 | -6.93113 | -42.9585 | 2026-09-22 11:45:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.0 |
| 655bf388-45b7-3c41-8647-a0916f15abba | -8.60946 | -54.62104 | 2026-09-22 11:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 092ccf04-a21b-3988-93db-eefd2ac90875 | -7.54421 | -42.65711 | 2026-09-22 11:45:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| f113f2fe-9696-345c-bb8b-e82e5a0e4693 | -7.36398 | -47.58417 | 2026-09-22 11:45:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf055c9d-3830-3753-8f8f-483a528db5ed | -5.61156 | -44.11923 | 2026-09-22 11:45:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fd885252-4b87-32b7-b015-4e7d50f5a3aa | -8.37584 | -47.28864 | 2026-09-22 11:45:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ed15c3ba-777f-3129-b2d4-cc8b1f143e6a | -7.44878 | -44.74239 | 2026-09-22 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 88da481f-787d-3a3f-a4eb-2bec9cba6bed | -2.8253 | -49.23909 | 2026-09-22 11:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 375b03f1-fc2e-34c3-9e4f-5d80dcf31545 | -6.47329 | -42.78164 | 2026-09-22 11:45:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 20a9935b-fb14-35d0-8ddc-212df7bc27ab | -8.38469 | -47.28983 | 2026-09-22 11:45:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 29fe0712-f42b-3921-8b50-15cd03e25aad | -6.7838 | -48.67181 | 2026-09-22 11:45:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| af25fe4d-4200-3bce-9e1b-4a854432eb92 | -9.6199 | -43.95287 | 2026-09-22 11:45:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 128.2 |
| f91bd973-6165-38c2-b2a1-f4d7c9acecd4 | -8.09351 | -44.36021 | 2026-09-22 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| d6cb3df5-e779-38b1-8833-8e6a22310887 | -5.82336 | -44.13707 | 2026-09-22 11:45:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| b932348e-ca8f-33ea-a1fe-f1fb6a397fd3 | -7.12567 | -43.73267 | 2026-09-22 11:45:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f504b904-dd8b-316a-a793-5092c92a4cb6 | -7.55557 | -42.6587 | 2026-09-22 11:45:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| c1ec88d9-7475-31b8-8762-7892da1d541b | -8.31638 | -44.74604 | 2026-09-22 11:45:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f25ab33b-1886-3274-aa8f-a6ab6ca72e80 | -9.90129 | -48.48554 | 2026-09-22 11:45:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 5e44a69a-b09d-32f8-8342-151f76d7786f | -7.03005 | -44.65622 | 2026-09-22 11:45:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 542.6 |
| ccf326b8-b4ab-3e5f-a384-1e3e1fb38855 | -9.28555 | -46.18775 | 2026-09-22 11:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 135691a6-e041-39c3-be8a-6298ac72e221 | -6.97886 | -42.59359 | 2026-09-22 11:45:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 7ca272c2-5893-352f-ae6e-f72ec3a1367a | -8.10488 | -44.42706 | 2026-09-22 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dcf05bb3-a3fa-3959-9b61-ef677b999883 | -7.02855 | -44.66706 | 2026-09-22 11:45:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| cdc6e79f-4eb0-3fda-86bf-11081c3cfaa2 | -8.09394 | -44.35483 | 2026-09-22 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 574ad25f-0e2e-3aad-af9f-aba7eaf8166e | -5.34621 | -43.29685 | 2026-09-22 11:45:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 93f1316d-7f4c-3099-a3ac-8827f685e6c8 | -6.017 | -45.24599 | 2026-09-22 11:45:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3e83ce1a-c005-30da-a795-ad148a7112a8 | -3.45364 | -50.6106 | 2026-09-22 11:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 3b7c7a5a-856b-3fda-8938-6851fe3dd356 | -7.02183 | -44.64404 | 2026-09-22 11:45:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 70873188-700f-375f-aa36-91085aafba2e | -8.37459 | -47.29751 | 2026-09-22 11:45:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3a55c627-5ed9-3e52-99f5-7a4bb3544db3 | -3.10374 | -40.21924 | 2026-09-22 11:45:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 0ff497d6-cce1-343c-8bfe-ec4d2bad36d8 | -3.96954 | -43.12212 | 2026-09-22 11:45:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| cf02c210-2a7c-32f4-bbdf-c32f8d84ccdd | -9.24229 | -46.16209 | 2026-09-22 11:45:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3ea1b166-a3d0-35db-9dfd-ed1ac24e2967 | -8.08504 | -44.3472 | 2026-09-22 11:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 950f03cc-b14a-3914-9152-e6db69c8c0dc | -8.8023 | -48.75367 | 2026-09-22 11:45:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 10.9 |
| fd25622f-edca-3a22-b33b-0acc5fcd622e | -5.30677 | -43.43151 | 2026-09-22 11:45:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| ff3fad95-5aaa-34e8-880e-30a2c29ab404 | -6.92015 | -42.95697 | 2026-09-22 11:45:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| d887ff66-4899-3f1c-a0d5-6b0b1d8a14b4 | -8.77695 | -48.74073 | 2026-09-22 11:45:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6c5aaf70-6039-3141-9419-63179a3d9ba1 | -7.42382 | -49.83692 | 2026-09-22 11:45:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 93927e98-2fdc-3a1c-9b88-42d407aef6dd | -6.11909 | -44.68485 | 2026-09-22 11:45:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 51719a8d-9d77-3387-9380-fce68dcbd9ad | -5.98741 | -44.72949 | 2026-09-22 11:45:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a6c85ee9-ac55-3839-b117-7b328c84f680 | -8.38595 | -47.28093 | 2026-09-22 11:45:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README124.md)
