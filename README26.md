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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0e0606a-6bb1-3918-a124-6df49771dde6 | -11.36329 | -45.18604 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6dbd970-05cf-3ea1-b472-a36d83e44b84 | -7.22115 | -42.76735 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 70dd89da-0172-31c1-8330-89bff761320d | -7.1212 | -42.75459 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c04b7092-0b74-3322-a2b0-5c72baa08384 | -11.22811 | -45.09743 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 321df4e5-3637-3224-9454-6d8ee31a76c6 | -6.3927 | -45.4999 | 2026-08-31 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 629e720d-4a3d-3c75-8033-767749def6b6 | -7.1173 | -42.75756 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4a2a5f1d-2556-38e4-ab83-2904c819724f | -7.90887 | -44.28104 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70c88fcc-27d4-3e0a-a6bf-ef0a314d095c | -11.21698 | -45.14344 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12bb69e2-195a-33ff-920d-7fb2375a247e | -11.79047 | -47.67207 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c794463-e57a-3737-82c9-0b11cb3a6c9a | -10.14135 | -45.70753 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aab21988-7b27-3bec-b752-cebba9ba6680 | -11.16531 | -45.04707 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4641ae39-453a-341f-97c0-da96c41dd619 | -10.4013 | -45.08171 | 2026-08-31 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70c4aacb-6ac1-33b7-b8bc-3cedd6066ac2 | -10.75419 | -44.88096 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7dc98d1f-e4a7-3b79-8d7a-ae2299f3e812 | -11.79135 | -47.66694 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc57cab6-0039-34b4-91aa-8b5a2532b4b3 | -8.74802 | -46.44852 | 2026-08-31 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c45ea357-5472-38c3-8dab-3de1b253ea23 | -7.92827 | -44.24946 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac2cc60e-251e-311b-a81c-be51dab95de7 | -11.22748 | -45.10122 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| defff613-6d5d-3297-8e5b-5e4cd60fec64 | -10.73757 | -47.96661 | 2026-08-31 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 489f2317-24de-3fe6-9f0b-395e867d8d46 | -7.34569 | -55.18145 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 258818c6-5c17-3099-86be-90d5832ea8f0 | -12.10858 | -45.03393 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8bccee1e-d7bb-39de-b7a3-342f259483c8 | -10.80455 | -50.65732 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d9ba9bc2-4009-349b-9dab-4b680052a52f | -11.68088 | -47.60708 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 26e3cb33-e483-3808-9fde-6f9b85d342a0 | -8.08408 | -45.47833 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97f6252a-4bba-3654-9137-32c75eef4db0 | -11.21362 | -45.09892 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 711de544-abbb-3762-843c-3fd06e6c9bb7 | -11.83294 | -46.75793 | 2026-08-31 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2d0712e-af30-3847-a6a5-a567031b8757 | -11.36918 | -45.21485 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2094e5c0-9ca6-368e-8437-600a53ddd960 | -11.34182 | -45.18642 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90ad9a82-66e0-3c05-9db5-90bbc5d4d66d | -6.86498 | -41.65206 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 97bfa197-6169-3c78-b758-ac7ef874377a | -8.74338 | -46.45265 | 2026-08-31 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 577e1d90-4066-37d7-8dfb-d1ee15f2f93e | -11.35618 | -45.22855 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f3a832f4-7132-3727-9ece-c459d725d68b | -5.59277 | -42.32716 | 2026-08-31 04:14:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 83950dd3-d7fe-3615-b998-d3916fc5d215 | -10.73685 | -54.04978 | 2026-08-31 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 512738d5-ff5f-37af-82b0-c6e9da41b9a9 | -8.14854 | -45.47382 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bceb528-479f-384d-a633-82e587ac5810 | -10.14949 | -45.75591 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80302d71-69cf-3f9e-a57a-ea0cf61b619c | -5.60069 | -44.00595 | 2026-08-31 04:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7607835-cca0-3780-ac80-9c2fd9ba328a | -11.32544 | -45.18807 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65bc7296-0bbb-37fe-acb8-da57d4769d57 | -10.74641 | -44.86384 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 195c00fa-81cd-3fbd-98d2-396113c97c29 | -6.84902 | -41.66723 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a278d7cf-c92e-3e28-9e3d-bc7a40ced0e7 | -12.11199 | -45.03465 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 778b2fb7-9f89-3c48-9e24-476273c69fdb | -10.14348 | -45.69467 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 151e69e5-ac19-3d08-b0c8-4968765e8ab1 | -11.20614 | -45.05806 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7807ee44-8f56-3fe1-bca6-3b2c5e52f3c4 | -6.91647 | -41.64989 | 2026-08-31 04:14:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c70531fd-a63a-32a2-9615-72f84ddaa954 | -8.08116 | -45.47331 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1df3c22-96f5-3979-accb-2d003e6b4c3e | -9.43275 | -45.66552 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67bdaa38-f1d8-3255-ba0a-b2345841f595 | -7.60855 | -44.84536 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0832527e-382c-3c00-bf88-d2ea12d4e1f3 | -8.13026 | -45.49329 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36497820-6791-3917-b34d-c9292bcbee7c | -11.91364 | -45.06344 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30c54095-c41a-3311-9634-d128833a1163 | -7.78693 | -43.95641 | 2026-08-31 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45fc5930-26c4-383f-ac2c-b7cab38abe23 | -11.6763 | -47.6083 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36f22397-d5fc-35bc-89c5-30091015131b | -7.92482 | -44.24889 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6abfdfe3-83cb-353d-9e76-b25a3a391d4c | -8.12934 | -45.4993 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41e71249-dc7a-31ca-9270-c44e7288975b | -10.76097 | -50.85019 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81ab0242-274f-3dc9-b695-a9cb637da4c1 | -6.39346 | -45.49544 | 2026-08-31 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0331f477-8ab1-3b8b-807e-ff818e32319c | -11.91584 | -45.07144 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99780ef1-1e72-3991-ad60-383d5aef13e8 | -10.06677 | -48.70502 | 2026-08-31 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c6f3c99-1d66-388a-8960-f95bf1a04896 | -11.24235 | -45.13018 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 717e7b50-dc52-3596-94b3-6f180b5d82f4 | -10.15596 | -45.73097 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f8b33d2b-0fa3-31cb-93c9-4d40cabd94be | -10.82166 | -50.6896 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 486fe03a-cbb4-305f-8ed4-63e9c328bea0 | -11.92619 | -45.07299 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 050624ce-1b64-3ad9-b07f-4ec4c2db679d | -12.3869 | -46.45126 | 2026-08-31 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bd4aad4-1df8-3ed3-bbd6-e949eaf1d9e6 | -7.2857 | -52.54565 | 2026-08-31 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 508bfcd2-ab18-3f98-9426-2ef07c9b8cf0 | -7.18973 | -46.56874 | 2026-08-31 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 805b784f-dde8-3765-a8ac-570b355e57c1 | -7.18115 | -43.71199 | 2026-08-31 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7b8d564-7478-3694-9b3c-05feae4fef69 | -7.21176 | -42.74063 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 69290ed1-80c0-327f-a352-4703956df344 | -11.34052 | -45.19416 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73918807-1604-3d1e-bc6f-99249b2e589e | -11.2274 | -45.14513 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7f6114b-9a42-36c5-a237-4c4e3a552a60 | -5.60768 | -44.00707 | 2026-08-31 04:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1ecefc77-e347-386a-a31f-3d5815df995a | -12.08465 | -44.98669 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dcb83630-f180-3eca-bfac-eb7b112d3889 | -11.81573 | -46.76915 | 2026-08-31 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e61ad16f-f788-3d17-9e9a-a1b7a98d4ade | -7.54826 | -47.32333 | 2026-08-31 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dac74f98-fdc1-3f35-a085-b0411059360a | -7.76986 | -44.06124 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee5b427d-9ce8-32c5-ba1b-1bd2c01e93b7 | -7.63859 | -46.72001 | 2026-08-31 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 424bd5c1-0068-3241-9de9-3fd901c5c5ab | -5.31199 | -44.55702 | 2026-08-31 04:14:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dffdef09-c7fb-3e8a-bf02-a73730dc5ede | -10.85889 | -50.49055 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ca42278-20fc-33e9-baa5-5babea983475 | -10.73432 | -44.87868 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02256ae3-f6c3-3c68-996c-55b60ec786a2 | -8.41238 | -44.98495 | 2026-08-31 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 591659a0-eba9-3099-91a7-3170047a63bc | -7.93809 | -44.2977 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24506304-1abc-3e46-b0e0-d56100d38abe | -10.77431 | -50.8522 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb6c86a1-af06-3b08-a392-9b154a6d0de9 | -8.60512 | -54.77115 | 2026-08-31 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aec41342-d03c-38cf-bc52-937103f0c0f0 | -10.75956 | -50.84932 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e65c7480-db4c-32f8-8045-b0740dee5d02 | -9.42053 | -45.67172 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 987c76c3-6f00-37ab-b322-5c9fbc2bea06 | -11.20205 | -45.06131 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdf6675a-3541-32e4-aac0-0a160bae5a6b | -7.10336 | -42.78059 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd4fd0d0-a41f-351d-9bcc-26172d5f51b9 | -5.59333 | -42.32366 | 2026-08-31 04:14:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 57ba0860-f684-37e8-ad9b-5c5035a72a44 | -11.21552 | -45.08742 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 06a6c6a9-81da-3078-b57b-30262a9e764e | -11.36135 | -45.19763 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 303d8239-1f26-3568-90fd-b691627b199d | -9.67193 | -47.93607 | 2026-08-31 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95e8b9e8-9afb-3fde-b617-d89de8d9113a | -7.60893 | -44.88705 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7561a2f0-d301-3cd2-95d6-969a9207598b | -11.22244 | -45.08859 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b967108-821c-3953-8a4f-35355ead2067 | -10.12859 | -45.73975 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73266cfb-0143-308a-a71a-06d76b10c0df | -7.9311 | -44.25384 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f96d83a9-258e-3e9d-ad3d-2447c5b1dc85 | -11.36765 | -45.20268 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39a63031-f85d-3d00-8815-b3694ab6e759 | -7.93864 | -44.25113 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df8ff50c-6802-3137-bf8b-e60aefa770c3 | -11.69253 | -47.60984 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c6976b4-3ce7-3b43-87cd-9b4bf312c593 | -12.12287 | -45.03276 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7a76d39-9fb7-3739-b2f8-52cf67d44061 | -6.41985 | -43.51887 | 2026-08-31 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b794ca2-7de8-35c7-b0fa-3c748fcc038e | -11.21415 | -45.13899 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42e22057-aadc-321e-8114-995e9d14467d | -8.38553 | -44.99316 | 2026-08-31 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae051f4f-e417-3d52-8643-b32e31ee5db5 | -7.97328 | -44.29969 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6dc4cc1e-1a08-3e0d-bcd2-c77ff6ebc569 | -10.99277 | -49.68729 | 2026-08-31 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README27.md)
