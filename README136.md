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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3abc526c-0121-3abb-aed6-cca53f9e480d | -13.10403 | -46.36057 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24779579-727f-3707-9109-6c75aaeba6c0 | -10.8984 | -44.79963 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44437dcd-4ad8-354a-a937-eb68154b45b0 | -11.77414 | -45.50721 | 2026-10-10 05:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ccddc8dd-055f-3932-9631-093e1dadc0aa | -11.75979 | -45.46177 | 2026-10-10 05:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fefe3f7b-3815-349b-9dd9-409beeb016e1 | -12.77579 | -44.88664 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ae11f5b-087b-3182-a676-2403bd6f6acd | -7.91731 | -54.72052 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 643cd084-1b58-30a2-ad7e-172989ed19f1 | -8.49806 | -54.61426 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc102800-f4d0-3567-9336-1671e2b890b6 | -10.60191 | -60.48212 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 3787937e-cd6a-3c8c-b490-e7a9f49813ea | -9.93772 | -44.87872 | 2026-10-10 05:06:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2c606cfd-0aae-343d-a3dd-1ac0b330fe34 | -14.45182 | -43.9465 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80ea92bc-b158-3264-9da6-c448ccc30ca1 | -11.59453 | -43.72659 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad1a84ae-f2bc-3419-a2b8-c467451a2283 | -9.92593 | -44.78611 | 2026-10-10 05:06:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82662040-dcf9-3f77-bb34-f2479f50ad1f | -9.62883 | -48.8846 | 2026-10-10 05:06:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 368c2f94-47fd-374e-a247-552f6fd15fe7 | -10.90119 | -44.82531 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae1ccba4-fa1a-3a59-b080-95ae5ba8a40e | -11.32165 | -51.10676 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c54cb9cc-c4d3-3844-b85b-0ef5f9585cc6 | -11.37309 | -54.02763 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1a23eac-c8fa-30b7-bb05-f127e6bd5982 | -10.59851 | -60.47783 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4432b383-90f9-3283-88e4-97eb1d438ce5 | -11.79432 | -46.72344 | 2026-10-10 05:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 036ca7f7-7aee-3d5c-8523-88d7a2edf514 | -14.45947 | -43.94299 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e60434e-f331-3298-9b36-02bff7220aee | -10.04233 | -50.93178 | 2026-10-10 05:06:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90864386-8051-39a9-8b0d-0d76a6ad25aa | -9.25561 | -62.30391 | 2026-10-10 05:06:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d6b13b0-142f-339f-94ef-5d7b797a5768 | -13.10446 | -46.35708 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2944c984-2649-3191-9cb0-6c169888812f | -7.92459 | -63.70548 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a79a76f3-29cc-3561-bbd5-c0dc13dc5ee0 | -14.44769 | -43.93057 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c49de3c-61a1-31ee-89b3-c3c5410d9ce9 | -7.90298 | -54.72534 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c9ecdeea-48a3-31de-ab04-e6a40fe2a20d | -13.76806 | -48.13502 | 2026-10-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0170d97-1c72-35ee-a9eb-bb7751a360e5 | -13.35483 | -43.92006 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| afd3407d-845d-303e-bf0b-b5b96c347261 | -7.69997 | -61.36305 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7240c273-b1f5-315e-9421-40220abffaa6 | -10.52254 | -49.45954 | 2026-10-10 05:06:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2af82ef9-9182-3064-a09b-c84dbdec01de | -15.10313 | -43.63913 | 2026-10-10 05:06:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fc84a0b0-c307-37aa-972e-0672ba13f9b7 | -12.37847 | -46.57164 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fef2048-11b2-3f92-ba6a-7e08a45cc64e | -9.71383 | -50.15571 | 2026-10-10 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ced2563-126a-3e6a-8906-8d11b5a2696f | -10.60595 | -60.48282 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 6b25f3db-7e5f-305c-9adb-56f75a760935 | -11.37028 | -54.02342 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17a641b3-cf2d-32eb-9a38-b07495ad0d26 | -13.69205 | -49.07962 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4797957d-1a62-37ec-a6b2-184f118cef0d | -7.43834 | -63.55686 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 889e61ae-9265-3c3f-bcaf-b187a1ec460f | -9.7572 | -53.87793 | 2026-10-10 05:06:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83ca3c6b-5fb2-3be0-800b-fdf8cfed2e31 | -13.77165 | -48.1234 | 2026-10-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| baa0f2ff-db21-3e62-8a56-82c790be4faa | -9.49602 | -57.25084 | 2026-10-10 05:06:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29108119-3083-3449-b85d-0d0765dc532f | -16.56259 | -46.8012 | 2026-10-10 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f450a805-d2fe-3f52-89d3-8f01d9dd3f5d | -15.45582 | -48.06087 | 2026-10-10 05:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8ed0a5bf-cc79-370d-969b-b0cee04ad4ec | -18.91431 | -47.91681 | 2026-10-10 05:08:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a3cdfeb0-0053-3642-b0bc-83552c5e07d3 | -15.66047 | -48.13464 | 2026-10-10 05:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cf99fdc-d56e-38de-9fc7-6f289dd50224 | -15.24488 | -48.58403 | 2026-10-10 05:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80034731-b352-3882-a43f-9b5ba437100b | -15.9845 | -52.48814 | 2026-10-10 05:08:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd2f9558-400e-35f8-8e1d-1b89feadde6f | -14.8684 | -50.30836 | 2026-10-10 05:08:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81b68b92-9071-3b6a-96fc-bca93c53c9f4 | -18.91997 | -47.91395 | 2026-10-10 05:08:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d6b495b-d575-32f6-9fc0-7210529f96fd | -18.91466 | -47.91347 | 2026-10-10 05:08:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bea65be4-85be-3e06-8db5-c13af60b72dd | -18.91537 | -47.91707 | 2026-10-10 05:08:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6585197c-b4a5-3b2c-8fd3-33495e8b7b7c | -16.76078 | -47.07421 | 2026-10-10 05:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c43f744-94de-349a-a9b4-5d0fdf5d8c31 | -14.87323 | -50.30487 | 2026-10-10 05:08:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 846bea0f-04f5-35d2-9c19-ef2bd3eeb669 | -16.12234 | -43.74995 | 2026-10-10 05:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52ababeb-14d6-3b35-b4dc-5d823a46b308 | -19.5502 | -43.58859 | 2026-10-10 05:08:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b40d3a13-ff50-3d08-a88b-2ddae9d9e857 | -19.08095 | -48.14948 | 2026-10-10 05:08:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c80fd2bf-aefe-38f8-80f0-96d2b1dd89ab | -14.33325 | -55.02713 | 2026-10-10 05:08:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2950d9fb-1a87-3b75-a607-11edacc51274 | -14.97375 | -50.38316 | 2026-10-10 05:08:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fc1bbac-4157-3aa1-a10a-39c32cb20150 | -17.9871 | -47.21347 | 2026-10-10 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1446fa87-6fa1-366f-b900-5007e8b200fd | -15.5827 | -48.18503 | 2026-10-10 05:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85f45ad7-9454-3e54-8adc-fd61a203e7e2 | -15.65545 | -48.13411 | 2026-10-10 05:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b12fe4b-de5a-363d-b9ab-edd0c1275b53 | -14.40219 | -52.88419 | 2026-10-10 05:08:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a990ce9b-66d5-3893-b55e-b112fc638eb1 | -19.54957 | -43.58832 | 2026-10-10 05:08:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81dcff99-106c-3824-b8a7-be88d6d9ac92 | -18.91612 | -47.91033 | 2026-10-10 05:08:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c79ef8bb-38a4-3978-b5d2-27f2ba532b03 | -16.76214 | -47.07673 | 2026-10-10 05:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f17b8c7f-53f5-3fa1-b3e8-c01e7c9008a4 | -16.9386 | -49.38077 | 2026-10-10 05:08:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 661fe780-4102-3a5a-8a9e-8a0e0505d2a5 | -17.98669 | -47.21719 | 2026-10-10 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 788bfd7f-f675-37d5-933b-f4f7e9752e82 | -16.58345 | -46.76555 | 2026-10-10 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 162c5867-4515-354e-8987-f80ca03075b7 | -14.87268 | -50.30894 | 2026-10-10 05:08:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a32517f6-3844-3651-a460-ba470904fa3f | -14.87236 | -50.30289 | 2026-10-10 05:08:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c3041a3-e0d9-354d-82c2-cdbdbc499032 | -18.78933 | -46.47174 | 2026-10-10 05:08:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8b922df-9361-3d3b-b845-f00b74371c9a | -17.99219 | -47.21766 | 2026-10-10 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84e972c2-2824-3303-a307-cd648de03d9a | -19.54921 | -43.59273 | 2026-10-10 05:08:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab11cd66-89f9-37e2-9a68-b57d309f66fb | -15.08714 | -46.94544 | 2026-10-10 05:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2fd69dcf-38c1-34e2-85db-eb494c8b4321 | -16.59343 | -46.77386 | 2026-10-10 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96582d4b-de3b-384f-a30a-93941ef17586 | -16.76254 | -47.07299 | 2026-10-10 05:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24143bd7-feac-3195-84f4-cafbf44c81c5 | -15.58333 | -48.1868 | 2026-10-10 05:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03045fe6-d244-386e-8071-22d2279d28d2 | -17.46225 | -45.0846 | 2026-10-10 05:08:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad874840-e801-3b42-99d9-af2543d4aad6 | -18.78357 | -46.47079 | 2026-10-10 05:08:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7779a7d4-ea1b-3b8c-b667-c94997861c6f | -16.56812 | -46.8018 | 2026-10-10 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14205959-3fda-3fe6-9321-4a3f9b0726bc | -16.12805 | -46.88414 | 2026-10-10 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f163d5fe-25d1-3264-b106-5f60d2d0e44a | -17.34591 | -42.67143 | 2026-10-10 05:08:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08b96cba-de96-33b6-8aea-4266fb57b552 | -17.45559 | -45.08832 | 2026-10-10 05:08:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 775d8081-7ff2-3aea-8828-8735e8614fe2 | -16.75673 | -47.07579 | 2026-10-10 05:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5014eb93-fb1a-3088-9842-408b2144f507 | -18.91397 | -47.92012 | 2026-10-10 05:08:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4105cd63-eea8-3a6f-a287-bf0f8bebfa70 | -15.98504 | -52.48606 | 2026-10-10 05:08:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1904b443-f0e4-30bd-96be-48356b3cddad | -14.33994 | -55.00577 | 2026-10-10 05:08:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 90ef68bb-f793-33af-a30e-c060692545bd | -15.24557 | -48.57846 | 2026-10-10 05:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17b490e3-a23f-3e53-b447-161c4b213215 | -16.59303 | -46.77768 | 2026-10-10 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33f20c1e-5e06-3509-8cd7-f6e6ad22d9cd | -16.12193 | -43.75416 | 2026-10-10 05:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a61ddd02-ee1f-3c15-bee3-850432a1f77d | -18.91502 | -47.91006 | 2026-10-10 05:08:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 014fd0e5-ba3f-3a67-8698-87a90a2adb27 | -18.91574 | -47.91375 | 2026-10-10 05:08:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 93d81411-6f0f-36b4-a2c1-a7d6c3be6840 | -16.58303 | -46.76923 | 2026-10-10 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67c4158f-f903-3400-a8f9-dcb2e263b97c | -15.83239 | -47.45735 | 2026-10-10 05:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dfcf236-d55c-36ee-8521-038dfb6c65a9 | -16.11533 | -43.75298 | 2026-10-10 05:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6adb79a4-003d-34db-9299-79f95e94a165 | -16.58272 | -46.76914 | 2026-10-10 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34326fbb-764b-3309-86da-87fcd443a098 | -15.98515 | -52.48338 | 2026-10-10 05:08:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c99f721b-e7d8-316f-bf92-23cab5db63bc | -16.76121 | -47.07048 | 2026-10-10 05:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d74f9a93-ab41-3daf-8663-43b9b996d979 | -14.87183 | -50.30698 | 2026-10-10 05:08:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f420484b-2ce7-3947-80ea-47c6f822a71f | -17.46126 | -45.09452 | 2026-10-10 05:08:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57d7770f-4196-3a55-b721-8c68a83a9e7b | -19.54983 | -43.59298 | 2026-10-10 05:08:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c2d1ce8-c721-38de-886f-75718e87aa60 | -14.3433 | -55.00631 | 2026-10-10 05:08:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README137.md)
