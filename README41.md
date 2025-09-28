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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e253b6b-ce06-383d-a36d-b305074366ea | -15.97414 | -42.0084 | 2025-09-28 04:06:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b8e7ab3-e912-3478-9467-e86af96f2ed5 | -12.00005 | -47.06846 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7f8c667-30eb-3ae2-b60e-66b82cb74b33 | -11.44689 | -45.00457 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bd1c62cd-44b3-3d7c-b03b-04a106c949eb | -10.2986 | -45.39498 | 2025-09-28 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 868bf9d8-79ef-3c89-b6e3-314e54a75381 | -15.28043 | -49.48059 | 2025-09-28 04:06:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a600da0-abbb-3cad-8fdf-063c573949b1 | -14.54295 | -48.40351 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bec6de66-cf3c-3bbd-a01e-2dca9d79a38b | -10.90967 | -45.73957 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5b316be-3299-3da6-891f-1fdb9fb9b8ad | -10.9273 | -44.31904 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1110d5e-2203-3934-b835-23843c066270 | -10.96308 | -49.57229 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da696c35-d9ac-398a-8fe5-f0e523ef5aed | -14.43423 | -44.87848 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4215af9-4ac4-3bba-9f9a-83ffbf146f70 | -11.4947 | -43.52683 | 2025-09-28 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0a1fc28-1594-3ea3-bf15-02b79889093d | -10.28311 | -45.2041 | 2025-09-28 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10d975dc-ea07-3ca2-9148-e2c50bc86b07 | -15.44362 | -48.22968 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80cfdca3-ac75-33a9-a0d4-e7a2599ed373 | -11.60105 | -44.35504 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 561260dc-b6d9-3dd0-b2ea-83444282b25e | -12.02271 | -47.91874 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65e0e795-ef99-3bd1-b2bb-412a3bdec221 | -11.38838 | -46.97952 | 2025-09-28 04:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 815cef15-6625-3a86-ba12-4c23bf8002e7 | -13.75789 | -47.86705 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52145bb1-f5ff-3314-a93b-f05881b6e16a | -10.45495 | -48.20629 | 2025-09-28 04:06:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e80cbd26-ee39-3899-aec1-0c479325d2a0 | -14.53858 | -48.409 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b5ef21f-876f-367b-9218-f70cd753a0f2 | -11.44016 | -44.9986 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d80ae1e0-d9c3-3f57-8e05-8ff18b4c5b87 | -11.37188 | -44.96822 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca496661-0bbf-38a3-9edb-d32a3a3675db | -11.44545 | -44.99022 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ce196d63-f542-3fa4-be5e-cd2e76667bb3 | -11.21022 | -47.74104 | 2025-09-28 04:06:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad2d115c-dbac-3446-92d5-b0e9870b4bc0 | -13.40096 | -48.16191 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 025e823f-a65b-3e59-b22a-8fa12f1ea7b9 | -11.37075 | -45.01939 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bc1cfa66-0667-3a82-88ea-1c68b3bcb48e | -11.9972 | -47.88087 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2807376-2da9-38c3-be3b-73511f5fde41 | -13.61422 | -48.08326 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69f82b47-2fe5-33d7-bafb-c2bae293a0c8 | -15.62123 | -48.35962 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 136018b5-6ccf-3ed9-9df8-a4d14e4e9c8b | -11.41097 | -46.95095 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31f146a6-54e0-3421-b779-3a11379e16ce | -11.58465 | -45.4919 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cf3ee9e-ee49-39d4-8d73-e77d7ae565fe | -13.77113 | -47.86796 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 831c0baa-b6c8-34f3-9c92-77a452f43406 | -10.85236 | -47.79316 | 2025-09-28 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e418969e-d645-3eef-b6a0-fed00dff196a | -13.58806 | -47.31783 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7df18088-93af-3861-ad6c-05e752272686 | -11.98944 | -47.07882 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e85462f9-6a6b-3e44-8dec-e05ca0ec9e68 | -13.40013 | -48.16636 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2adc6692-94ae-3c54-a430-2dde3e99c6c2 | -13.02378 | -49.45732 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e39d66a4-3eba-3878-a43a-6bca44a165ba | -12.68316 | -46.88454 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e5dcb290-70a6-3ea2-8c19-9090d4bedf9f | -10.90672 | -45.74722 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc321cae-91bf-38f8-915b-101385196f62 | -13.62754 | -47.31461 | 2025-09-28 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15fcaadb-fba8-356d-9a61-7867b8f7ba55 | -11.98844 | -48.00631 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0137cc4d-6c4f-34ad-928b-d46d7a7505e4 | -11.64946 | -52.8709 | 2025-09-28 04:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2773877d-dea5-3a78-aadc-42c46e74435b | -12.00506 | -47.04068 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 862a05aa-8b85-3039-8be7-54d4479aee93 | -15.33424 | -47.89185 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cbb76eae-94c1-3f16-aba2-47326944a5ee | -11.9566 | -47.97686 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bf5e89f6-aac2-3915-b819-c581465bacfb | -12.32162 | -51.51942 | 2025-09-28 04:06:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37f24703-033f-313e-bc56-6836546b9946 | -13.01287 | -49.46174 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0674801a-6cc8-3e98-b2e4-e667d84fffed | -11.5816 | -45.48654 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d51a3610-d4c8-30eb-a61f-d54f145d2421 | -14.33327 | -44.50063 | 2025-09-28 04:06:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9ce0f8b4-e6b5-3051-abe5-25075cf8d38b | -11.92888 | -38.32978 | 2025-09-28 04:06:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c10dffc0-f765-3530-889f-8dd2a5fb78f4 | -15.43338 | -48.23667 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3948e4d-38af-392d-bcc5-c2821a0cf62d | -10.5963 | -46.27526 | 2025-09-28 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe1f3bf5-04c1-3897-84e0-65e23f74261c | -12.694 | -46.87165 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d498bc48-3339-3f17-9cdc-5f08ab57a166 | -15.08549 | -48.3309 | 2025-09-28 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 851137f9-9f47-3a1f-a492-5a3e809dffbd | -11.49546 | -43.52616 | 2025-09-28 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0819887e-a8c4-3026-be51-ef5d08df9e22 | -9.54265 | -50.77952 | 2025-09-28 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c6ae10d-e8cd-3f03-a654-cc1af082bb20 | -13.5896 | -47.30932 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffab03d5-d80f-373c-8bb8-58293090829f | -11.99095 | -47.04631 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5236251-804e-3a8b-b84c-2f80dd2eb0cb | -11.98928 | -48.00167 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33724d78-37df-3b8b-acac-5d5136a7a1a8 | -15.03275 | -46.96297 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d43fd36-96c1-3cff-bcd4-7652534f9335 | -13.60097 | -47.2943 | 2025-09-28 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0160a229-fcc2-3eac-895a-ccbac402a834 | -11.7908 | -44.86923 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9e80268-4e2e-32db-8904-eb289f323d2c | -11.09565 | -54.28576 | 2025-09-28 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be71c111-6f3b-309a-a3fa-e78465a80aff | -11.62317 | -52.85493 | 2025-09-28 04:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e91f5cf0-1db2-3f41-aa48-d9386d51fc0c | -13.39837 | -48.16288 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36c9c821-d6d5-3708-9b2c-b7d9c8392380 | -15.62551 | -46.26073 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ed13cce-66a9-3bdf-928d-86822742a747 | -13.78109 | -47.89296 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb68a51b-e1f6-332f-b0e2-3a1c6267aabf | -11.79596 | -44.90671 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab37c6e5-8164-3109-a3cb-d29896ac54b3 | -10.94408 | -44.26306 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 571ccc7c-ce53-3696-b04d-74c456a2eb53 | -14.77194 | -45.67278 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 582047ed-5255-323b-9278-40aef97138e4 | -14.45553 | -41.67347 | 2025-09-28 04:06:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 66bd05cc-0e19-3679-81e2-7a589032d383 | -13.01772 | -49.46278 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f104791f-e0a0-34ae-ad1d-bad79bea9d21 | -13.61928 | -47.31247 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5b46b2ad-fdca-3e65-9a79-2ffb66755a3f | -13.52464 | -47.40309 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da10bc23-28c1-399e-95f2-e7ad70d5f314 | -13.77485 | -47.87208 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c24acb16-e76a-324f-8314-0d3dca030555 | -14.32538 | -47.09322 | 2025-09-28 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4be82d7-ee4b-33f0-96af-136f11b31ba8 | -13.58712 | -47.29919 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dab3a624-c437-37ba-9ab2-51b7dce4797f | -13.4054 | -48.16272 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 39192be9-e4f2-3fab-bc03-35e103e7c5ad | -13.53916 | -43.49973 | 2025-09-28 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d4c6292a-d029-31d4-bfe5-bcb57a2d8e6e | -10.92727 | -44.31739 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e6b4502-e417-36be-8782-ee3109433884 | -11.77721 | -43.76369 | 2025-09-28 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e88f763-b5ea-34cd-a3a4-05f64471086e | -13.60089 | -47.31857 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78cce5dd-6536-3264-bd44-ca1f1da5010f | -13.56211 | -44.10205 | 2025-09-28 04:06:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fb304d7-6d22-3a3e-9b5d-3fc7b6ce9883 | -14.32107 | -52.92855 | 2025-09-28 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b20906a-d2e8-331a-a653-7defa6d49d2e | -13.64844 | -48.07053 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a34666d-fe9c-3bfe-b5fb-5423e87002fa | -12.74214 | -46.81634 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 067c8bbb-525f-3be4-8ae1-2db1bbce52fd | -10.41775 | -46.15596 | 2025-09-28 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14d0f727-7030-33d6-9bb8-16bcc1bef4d0 | -13.77547 | -47.86869 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9dde72af-2e55-30bc-9d00-e8f0b0efe9b3 | -15.29462 | -49.48251 | 2025-09-28 04:06:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1066419a-4b35-398b-a26b-d30a988f32aa | -13.59084 | -47.32633 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d58fb25b-3f09-3c26-8565-e5c526ce35c3 | -13.71426 | -48.34845 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb4f8e62-5a60-36c0-803e-2f903d6a4a42 | -11.50989 | -46.95254 | 2025-09-28 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9f553a58-b87e-385c-98b8-8c64fba431fc | -11.98801 | -46.60145 | 2025-09-28 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0c1fb5c-ec3e-3b4b-a293-fb83acf412b2 | -15.52097 | -42.20179 | 2025-09-28 04:06:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ca6a0a1-36e1-3bb2-bfc5-428a7cc97ef0 | -13.59684 | -47.29324 | 2025-09-28 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7250874-07e2-3fe1-8404-c2230fc8d3c1 | -12.02315 | -47.92746 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e10063a8-ae3e-306c-8634-dea6fedbe79c | -11.52404 | -54.31726 | 2025-09-28 04:06:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2591bdf-eace-3756-83d1-6cada20184c2 | -13.29998 | -44.15756 | 2025-09-28 04:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da6ed3b1-e1ec-39ea-a2a6-7c89e294de14 | -11.69025 | -44.42208 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93cfc791-4fcc-3595-afe8-279bb6f1ac6d | -13.60606 | -48.0844 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| afda1a80-ec8d-3960-a0c3-72f0cda6968a | -11.41736 | -44.9059 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README42.md)
