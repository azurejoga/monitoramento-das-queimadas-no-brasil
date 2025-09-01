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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7a8cdd9-f5cb-310e-baba-49881364f3ea | -7.9351 | -46.4559 | 2025-09-01 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 282b3b35-cd69-341d-8cff-f9cc6c54f384 | -8.1945 | -46.7657 | 2025-09-01 12:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| d5cc1d11-32fc-3fe8-8631-6ceaf28ce08e | -7.0948 | -44.3358 | 2025-09-01 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 3b2c5375-3d2b-3cd4-9a73-7ed35132f292 | -11.3705 | -43.5868 | 2025-09-01 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 296.4 |
| 58f73b58-7607-38cf-b217-6544958714ae | -6.7438 | -43.7898 | 2025-09-01 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 0b65c555-291c-3264-a91a-370ee7ced762 | -14.6483 | -43.9461 | 2025-09-01 12:30:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 6a29e14f-b2e6-35c5-af86-0fd3cd42b67e | -12.8428 | -48.0795 | 2025-09-01 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 9e14d1d8-07f9-33b7-959c-5e8bdc0c42eb | -11.0572 | -45.123 | 2025-09-01 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 91655093-87dc-376e-904b-dba47721251c | -11.3709 | -43.5631 | 2025-09-01 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| d3694103-484d-3a68-a3f7-0bf69baf3782 | -11.0845 | -44.6343 | 2025-09-01 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0ebbbc79-246d-33ff-9b24-07edf1f4a76a | -12.9575 | -48.1076 | 2025-09-01 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 4ae0d7ce-daad-34fd-b9e4-2bfc4406bb7c | -14.6478 | -43.97 | 2025-09-01 12:30:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 138dcd10-03e0-3fca-b697-329eeb5ccafa | -7.9539 | -46.4542 | 2025-09-01 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 3c5141b2-4e74-3ac9-86cf-b6b085638673 | -11.0568 | -45.146 | 2025-09-01 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 9f79215b-8d32-3200-b9da-fdb89ff762de | -12.5764 | -44.8047 | 2025-09-01 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 30f584dc-5a42-3a8a-a3d9-be87d8c7f443 | -7.076 | -44.3376 | 2025-09-01 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| ea96df39-35f6-38cc-99e1-94aecff38b9d | -12.793 | -47.6415 | 2025-09-01 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4d05cf60-ed75-347d-9c8f-acb29a9e8615 | -6.824 | -43.3168 | 2025-09-01 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 9c3f268c-30cd-35ce-81a0-474193145e27 | -7.0572 | -44.3393 | 2025-09-01 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| f2ad04bb-3517-317a-b1ba-69bfb5ccfa8e | -7.0946 | -44.3589 | 2025-09-01 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 87f6313f-76dd-3007-88bc-0a2f034413b6 | -12.5769 | -44.7814 | 2025-09-01 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 86776142-9d44-3036-a068-37958e2ef466 | -11.0377 | -45.1487 | 2025-09-01 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| e7ed75c4-bb1f-363a-91cc-e0bd03bd34bd | -9.6505 | -47.8128 | 2025-09-01 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| a2153d70-f527-3445-99c2-66fbb8cd0169 | -8.8437 | -47.5217 | 2025-09-01 12:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 05f5edc4-006f-3a72-8ec6-77cc8d71310f | -6.7992 | -45.6815 | 2025-09-01 12:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 227.1 |
| a66f57c6-d33e-3974-a629-ee37aea77530 | -6.7626 | -43.7881 | 2025-09-01 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 18fab334-9344-3aaa-b604-c7f251cfd5d5 | -12.9575 | -48.1076 | 2025-09-01 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| a8e13bc4-f3b5-313e-bf0c-61b652d1fdfe | -7.3992 | -47.4333 | 2025-09-01 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 652babee-1d27-322f-b402-c7898dfd8e39 | -11.9623 | -45.8428 | 2025-09-01 12:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 36273539-365a-3b74-9c79-ea9d3a418966 | -7.0757 | -44.3606 | 2025-09-01 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 184b5ff3-bdd9-3ae6-8a49-14698dee4a1c | -6.7438 | -43.7898 | 2025-09-01 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 295.5 |
| 13e70534-5364-3976-ac43-ec3dfb50f04f | -15.7116 | -48.8809 | 2025-09-01 12:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 36647a82-12ab-3adb-8a63-9c0bebd404dd | -11.0377 | -45.1487 | 2025-09-01 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 104528d5-78ac-32c5-a3ef-7cc183ad39f0 | -6.8426 | -43.3385 | 2025-09-01 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| e845900d-994c-327a-a866-4bf5301190c3 | -7.0946 | -44.3589 | 2025-09-01 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 021318d8-635c-384d-801a-e6522b7f7cd2 | -6.824 | -43.3168 | 2025-09-01 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| b18199d8-5c9b-38b2-9976-a9e998faf949 | -11.3709 | -43.5631 | 2025-09-01 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| aafee06b-c293-3bc8-af38-6e7cc3d0bf75 | -9.6505 | -47.8128 | 2025-09-01 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 9708f0d0-b37e-3360-8c36-3818d21d6204 | -8.8401 | -47.8079 | 2025-09-01 12:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a8b3d7d8-78be-393d-8290-21d2d991a8a3 | -15.5862 | -48.3435 | 2025-09-01 12:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 06882f73-f541-3e1d-b5db-a9741fb75c11 | -6.8237 | -43.3402 | 2025-09-01 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 31cbf412-a40f-3679-b413-30087738cd54 | -6.8428 | -43.3151 | 2025-09-01 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| c204035e-f5f2-3645-893c-a1a7b2d30314 | -11.3705 | -43.5868 | 2025-09-01 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 310.4 |
| 85617ab8-936a-31bb-bc1f-136f4df689c1 | -6.7992 | -45.6815 | 2025-09-01 12:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 2543c6b3-85c0-3e9f-b44a-f7c79e88170c | -6.7229 | -42.2409 | 2025-09-01 12:40:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 7c17ebeb-1b91-386d-81a0-032e4b1bc441 | -11.3701 | -43.6104 | 2025-09-01 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 3e3c7e57-2b34-35d4-824a-ee2799d84402 | -7.076 | -44.3376 | 2025-09-01 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 183.0 |
| bdf5015d-1d11-3ec5-bac5-066ca11d6843 | -14.6483 | -43.9461 | 2025-09-01 12:40:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 165.8 |
| 47fa9476-9e6a-391e-b811-f97e4d5bef26 | -6.744 | -43.7666 | 2025-09-01 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 233.3 |
| 0fe366ef-f0d8-3b37-9c5f-ca359e6f6493 | -11.0381 | -45.1256 | 2025-09-01 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 4667b5f8-2031-38ad-b51b-67e56860b3f6 | -8.8936 | -45.1168 | 2025-09-01 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| feed810d-8ceb-33b4-9844-3b6f615dbea9 | -9.2258 | -47.1066 | 2025-09-01 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 75da5c37-97ff-309a-8aee-7a76ed9e48b9 | -11.0662 | -46.9145 | 2025-09-01 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 6ceb19d5-ebf8-376e-bfda-c3a51a1200b2 | -7.0572 | -44.3393 | 2025-09-01 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 12f7afd8-1c66-36f9-875e-263aedaf4983 | -6.704 | -42.2427 | 2025-09-01 12:40:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 8060af0b-708c-3990-ae26-e4633fe0b95b | -12.9764 | -48.1272 | 2025-09-01 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 66ceb452-6011-3457-8e1c-e061be00fec7 | -6.7626 | -43.7881 | 2025-09-01 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 175.9 |
| bd429e19-fdf5-3755-b041-e9f09995af0f | -7.0948 | -44.3358 | 2025-09-01 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 66683887-ad6e-37bc-8fc0-272f96b1ed20 | -6.7226 | -42.2648 | 2025-09-01 12:40:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 115.3 |
| fe8b81db-ff03-3ef8-95cd-b85a4adb5dfe | -7.9539 | -46.4542 | 2025-09-01 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| fbed56d0-2946-314d-82b1-67dc23635686 | -8.8437 | -47.5217 | 2025-09-01 12:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| f21c491c-152b-3dc5-af04-b6aae989b6fb | -6.7628 | -43.7649 | 2025-09-01 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 409ad110-7e31-30cd-b86a-8835814bc660 | -12.9768 | -48.1049 | 2025-09-01 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 581d1976-9f64-37f8-89ec-0397772204e2 | -11.0568 | -45.146 | 2025-09-01 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 273db51b-d1e7-3c2d-b9cc-afa0f4e8747e | -11.0845 | -44.6343 | 2025-09-01 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| dacdf7e9-aba5-3ac6-af3c-f869f99415e3 | -10.8935 | -45.8084 | 2025-09-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 4d996f3b-ecb3-3e84-a6e9-c6d4963e03ee | -11.0568 | -45.146 | 2025-09-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| c48be31a-bca6-3993-86ee-2ef548c1da6e | -11.9685 | -51.3554 | 2025-09-01 12:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 032159b0-7b73-3235-8a56-d5c8be14d71c | -7.9348 | -46.4783 | 2025-09-01 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| f5cea7ff-d46e-349a-ba03-688dc964cab5 | -12.9764 | -48.1272 | 2025-09-01 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 6ea825b3-06c5-3e0d-a4ca-deaca8ac3e99 | -11.3709 | -43.5631 | 2025-09-01 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 17443c7c-4aef-3ff0-8fac-66bc0caed941 | -11.3705 | -43.5868 | 2025-09-01 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.6 |
| e29621ab-5223-3238-b121-49611ee99ea0 | -11.0841 | -44.6575 | 2025-09-01 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 348.8 |
| d7096440-4052-37f2-a8fa-bec5e11f3598 | -15.7116 | -48.8809 | 2025-09-01 12:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c95cbe0b-7071-3e77-a7a3-fc88430c28cc | -7.0946 | -44.3589 | 2025-09-01 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| e3e795c6-a123-3d75-9ada-7ced1e6f78d5 | -6.8281 | -52.8143 | 2025-09-01 12:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 16e1e7a7-d9b4-3b42-b53d-ba0384dcc1af | -7.9539 | -46.4542 | 2025-09-01 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 8a7d7a32-27dc-3027-b1d0-6ed11ec0aaae | -12.9768 | -48.1049 | 2025-09-01 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 36427f90-b918-3813-a3f2-5b3c823217a8 | -7.076 | -44.3376 | 2025-09-01 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 8d11c87d-1e56-30b8-9a92-6c51c5f5ba80 | -8.8437 | -47.5217 | 2025-09-01 12:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 241.2 |
| 44b423d4-72d7-3b92-bac4-ae3c12676dd3 | -6.8428 | -43.3151 | 2025-09-01 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| f7e08298-3719-39cc-bd7a-b95ca32fd5c6 | -15.5862 | -48.3435 | 2025-09-01 12:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| cb4d3f13-28af-3a28-be46-1e139521d0d1 | -11.0662 | -46.9145 | 2025-09-01 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5123b083-efe4-3556-8476-73f1db97afa8 | -6.8466 | -52.8132 | 2025-09-01 12:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 012067cd-246a-3b44-9818-fdac338281b0 | -12.9575 | -48.1076 | 2025-09-01 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 608de20f-ecf7-34e0-b5de-4719ba0b6776 | -9.2258 | -47.1066 | 2025-09-01 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 9105a3f6-f212-3d6b-a3f4-5534e087d9e7 | -11.0849 | -44.611 | 2025-09-01 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 252b0960-b06c-3436-b2b9-e718e1e8e4cd | -6.8426 | -43.3385 | 2025-09-01 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| ca992d1c-7774-3917-b432-78d1fcde6f6f | -7.0757 | -44.3606 | 2025-09-01 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 8a33f575-984b-3fb4-aa1e-f2597e4bb2fe | -7.0572 | -44.3393 | 2025-09-01 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| dfb88d82-60ae-39d6-921b-6a16a1a63f52 | -11.0654 | -44.637 | 2025-09-01 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 9ed1bd4d-602d-3101-b456-0937a698760e | -11.0377 | -45.1487 | 2025-09-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 87e7da1e-40b3-3d51-acbc-eaccd2cac77a | -7.0948 | -44.3358 | 2025-09-01 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 9d70a3f5-fb81-304e-ab9d-f8fc4f9e699d | -8.8625 | -47.5198 | 2025-09-01 12:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| d5a33c6d-6c12-3ce2-9535-ce9b921957e2 | -7.3992 | -47.4333 | 2025-09-01 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| f1fa1220-c2c0-35fc-8a2a-2751f64c3b77 | -6.824 | -43.3168 | 2025-09-01 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 54c31e10-1731-35fb-840a-95c5948fb1c0 | -11.0845 | -44.6343 | 2025-09-01 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 541.7 |
| 266dba8a-c49f-399c-b279-4fb209eb2ebe | -13.3439 | -46.9757 | 2025-09-01 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 2b395e66-7d50-38cd-a93e-a3ac77c4f784 | -7.9536 | -46.4765 | 2025-09-01 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 929c0967-15e8-30af-9b0d-7631f9f8d5d9 | -9.2825 | -47.1007 | 2025-09-01 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |


[Clique aqui para ver as próximas entradas](README106.md)
