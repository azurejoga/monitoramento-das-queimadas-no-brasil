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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 300274a2-735f-39c1-bd68-a99533b9aeff | -12.15074 | -47.91666 | 2025-10-10 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43cfeceb-c77a-392a-906a-af8956baee3a | -8.19211 | -43.32398 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 080a30b3-f672-3bf2-8e6b-7307faa83493 | -8.5229 | -46.13122 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 470178b6-2f9e-3735-9ad2-a19127517d73 | -6.19956 | -49.04176 | 2025-10-10 04:51:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1259d642-72d7-3d74-938c-2c8786228a97 | -11.68692 | -47.52085 | 2025-10-10 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a44aeaf5-dbba-3965-bc6f-398cf6724d45 | -8.51111 | -46.11504 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70051dec-1efd-393c-8796-bea269db5ce4 | -8.37611 | -47.76156 | 2025-10-10 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc5da457-247f-326b-9d16-712be2d0c7d3 | -7.55671 | -44.29245 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efca2cd3-d241-38d2-a742-bac516cfaaa2 | -6.58599 | -44.62139 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 516c8e2b-4ea7-39c9-ba3d-190115807664 | -7.78175 | -44.05395 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab8d192a-2fa2-3a5f-acaa-6988d2b6d5be | -10.16857 | -44.55198 | 2025-10-10 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbfd180e-85f6-3e89-a44c-5d1edc9bb892 | -7.5347 | -46.77114 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fe3f331-9f09-3e04-a0b9-f673093c3861 | -8.04677 | -43.91318 | 2025-10-10 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2cadd055-c639-35cd-b120-035b70f57705 | -7.62315 | -46.65477 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5130e934-54a4-324c-abed-7bfcbce2c06e | -8.16445 | -43.32032 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9862c6c7-c3e5-3127-9b37-9ed292ab0219 | -7.24197 | -49.40486 | 2025-10-10 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 689fc0c1-a5d9-321a-a7c9-66172a9eb53f | -12.61345 | -45.06136 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d19278df-a694-3ee1-b42b-9be498659cb4 | -8.49605 | -46.12252 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67981835-005e-3e6b-9d00-40a3d2fb0add | -7.42276 | -42.97463 | 2025-10-10 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 192b167e-4091-39ce-a15b-e8f9abcb14f4 | -8.20064 | -43.34394 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 07174395-717b-3e49-a141-640c5174e5a0 | -8.19664 | -43.33206 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 41a2eba8-7735-3693-9271-2095ed7c9e15 | -7.42228 | -42.97828 | 2025-10-10 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b7962ef9-0d85-38d8-9d94-242fb9e54519 | -12.62954 | -45.06027 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 892d02e6-66d4-32d1-b142-81cf761db62b | -6.58623 | -44.21381 | 2025-10-10 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 189d16a6-e539-352c-a6e4-3b77c22be057 | -8.16395 | -43.32408 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ecc59cc6-6423-357d-aa64-8a275716d199 | -7.20216 | -45.49177 | 2025-10-10 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2547a2c3-092a-36d5-afd0-527d15b58f9b | -8.51046 | -46.11979 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2423ecb2-c172-3d2a-944e-e47d0ec8e71c | -7.26281 | -44.91294 | 2025-10-10 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fac5c844-a2f4-3d56-a20e-0a6851fbbab7 | -6.82273 | -42.7952 | 2025-10-10 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 90f7007c-1890-3ed3-8cc1-6672b55b7401 | -5.85036 | -50.07556 | 2025-10-10 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adb6473a-0ea9-3d3d-b975-cdbf17329404 | -8.4967 | -46.11779 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a5bd49c-5b02-3d6b-9e1d-156c36bd0865 | -5.37471 | -50.90152 | 2025-10-10 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76394dc6-3a6b-3eed-a5fe-220ee66b8506 | -7.67713 | -42.39494 | 2025-10-10 04:51:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3803cb7c-a4c4-3ceb-96e2-191a265c2886 | -11.97488 | -45.20537 | 2025-10-10 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6720dcf4-fb60-3b35-a3a0-83e346f14e4f | -7.54091 | -44.2933 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08b8d2b2-f0da-3dc3-97ac-b2deeb20f138 | -8.17603 | -43.31796 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9b9ee0ee-ccb9-358f-b324-6d1eb446205e | -8.20055 | -43.34599 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fe67a6f6-fd54-3d1f-bb75-63ee468580f6 | -10.16133 | -44.60669 | 2025-10-10 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f1037d19-bff0-34e1-b314-05141f538b10 | -8.18106 | -43.32237 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5538fd57-b2e3-398f-bc0e-91d47ebbae2d | -7.55151 | -44.59672 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d98eb482-7f5f-3346-bcef-0bb2592eea76 | -12.63712 | -45.04185 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 045cd2a0-f185-3ca4-a855-3fec5d1b0ae0 | -7.20286 | -45.48676 | 2025-10-10 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a0f45859-fefc-3dc2-85fb-2c2744c026b9 | -7.79517 | -44.19247 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77d10f90-793a-33f9-ba4a-acaa760a3ac2 | -5.85383 | -50.0761 | 2025-10-10 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72bab9e7-5ed8-301f-9726-fe30bb39e9fe | -10.48924 | -51.86802 | 2025-10-10 04:51:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1619b6d-6393-3b27-878e-37c8fe29e060 | -8.20166 | -43.33652 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 449f90b6-bf9d-398b-bab7-89d949804e7e | -6.58436 | -44.63295 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bc02823c-f505-3d1b-8a18-9c37d90aae26 | -12.64118 | -45.05212 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9d3fb324-b124-3ff8-9493-53b839f8806e | -6.5 | -44.43201 | 2025-10-10 04:51:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 752d12d9-9ff1-3ccd-a71c-b2332480e50f | -7.89728 | -45.49474 | 2025-10-10 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 194772ee-b940-3352-a4f0-a4de0c36526b | -12.63594 | -45.05147 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ea5f5899-a844-3966-9b2a-5409c77038a9 | -8.53012 | -46.11291 | 2025-10-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 401c3412-c192-3ed7-866d-5f8729cf5c09 | -8.13842 | -47.39067 | 2025-10-10 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43c5a049-fabd-3ec4-9b94-7f53d7fe2291 | -8.5157 | -46.1157 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4a1e4767-847f-3fcc-bb8f-72fb9306a582 | -13.39131 | -44.23478 | 2025-10-10 04:51:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2da34a65-d718-31cc-81cd-1cd6c86cc60e | -8.19161 | -43.32763 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 48c4e188-bfa4-3417-a1d7-62df6d935301 | -6.58517 | -44.6272 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 640698d7-6d18-3e5e-a26e-1c5873326ad3 | -7.54645 | -44.29102 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7ba9b4d-acb7-3072-86f5-6fca17fe8f9f | -6.66722 | -47.74974 | 2025-10-10 04:51:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02323efd-2650-3b71-8905-50ec69218058 | -7.0982 | -43.25193 | 2025-10-10 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 80192109-1b8f-3130-8683-6648e3ce99ed | -6.99781 | -46.99291 | 2025-10-10 04:51:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ab0cc08-b299-3dbd-a0da-352b65a8d629 | -8.51373 | -46.12991 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ac32a851-959d-3659-9f2d-545e6cc1361f | -7.78118 | -44.05443 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffa9d2b7-d5da-37f1-8a89-29b5d533be86 | -5.64741 | -45.96695 | 2025-10-10 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c14490cf-b1a5-3903-9d91-f3576840eaf7 | -7.54051 | -44.29629 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ca837a7-5112-382a-a376-ade20a73b3a0 | -8.89427 | -46.0123 | 2025-10-10 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0bd3aca8-2345-3212-b733-5d0f7c57e92f | -11.64476 | -47.53703 | 2025-10-10 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7a84c99-dca2-3f4f-9fda-f0fe275870eb | -8.15841 | -43.32338 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 58ec1e77-73c8-30bb-86b0-1ac51f64b52c | -8.22546 | -44.14054 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 537112e8-fcc8-3ac9-bc3f-9a7a481e2b87 | -11.64039 | -47.53651 | 2025-10-10 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52fb53d6-a241-33cf-89ad-35f4533f0d7a | -11.21348 | -48.04476 | 2025-10-10 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76e03d96-32cb-36c1-bd9d-a03e853b7906 | -9.33078 | -46.10819 | 2025-10-10 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abbcf889-a8a0-3633-9a04-297773266f86 | -7.80033 | -44.19334 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 59601e73-3bc4-322e-8acd-8a3327a88dd0 | -8.52487 | -46.117 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0acf115f-c507-3e31-85a2-26eaa4d2488d | -12.63554 | -45.05466 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b2c92c1a-365e-373c-9df9-d394b006b011 | -6.50917 | -44.14399 | 2025-10-10 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00f9f1e0-9121-32e3-be9a-8e1ee2485455 | -12.7172 | -45.83562 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 207d4f98-e044-3d7c-b1de-fabcd721c80f | -7.77599 | -44.05344 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 291f9adc-1658-318b-bbbc-23fdcc048ccf | -7.78655 | -44.05798 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b04dad20-57ed-33dd-9d8f-6d9b3b03183d | -12.63672 | -45.0451 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6fba916e-bfc8-30a9-b2e8-4bd76bf599e8 | -8.5085 | -46.13396 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4cef52bb-b4e2-3f97-aa3e-4d5bd3af22d9 | -8.20103 | -43.34225 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 4216c4a1-c87a-3479-824b-ca3445a04093 | -7.53158 | -44.30429 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 270fdf61-3afc-3421-a5e7-0bed3c8874dc | -7.54012 | -44.29924 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db10f811-7db1-3482-b92f-e8f5e3c371db | -8.49999 | -46.12791 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c417cb47-58c2-3d31-a48d-3d875d9c11f2 | -8.90102 | -46.00691 | 2025-10-10 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e25bdca-e2ee-3c72-a66e-7e571d32a0e8 | -11.96897 | -45.21086 | 2025-10-10 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eaa0ef3b-f93f-3b7a-81ac-3bd38569ca95 | -7.55191 | -44.59381 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 740fbb52-cff4-3a83-bf09-fba6c049e6df | -12.92414 | -45.05616 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 099ea029-eeda-3cf1-8493-e9dc0c7c78c5 | -11.96819 | -45.21704 | 2025-10-10 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8bb1104-9f0c-3862-9fbd-c72c0198471f | -7.54569 | -44.60178 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39b90eee-4caa-3255-8876-b17a71466ff6 | -8.20724 | -43.38102 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e2e66f05-e250-3a2d-8100-bdb6efb896eb | -12.36861 | -47.22304 | 2025-10-10 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a29601c6-e95a-38bf-8df8-78d910548374 | -8.50722 | -46.14326 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 19db5d7a-d107-3b9e-93d7-01640e19c17c | -7.42735 | -42.983 | 2025-10-10 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 721051e5-db49-3d3c-a319-5febe3ba2914 | -12.77512 | -45.77737 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 707b0498-f404-38f0-aa68-c49b2722c1de | -12.63999 | -45.06171 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3510e672-f806-3de6-8977-2b06e7d80528 | -8.51897 | -46.12583 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d2c7a3f9-bdd8-3214-a6fe-3e7517561e42 | -8.21061 | -43.35509 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 669ec1c0-71ce-36cf-b049-60c78c253888 | -7.28759 | -41.96772 | 2025-10-10 04:51:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README36.md)
