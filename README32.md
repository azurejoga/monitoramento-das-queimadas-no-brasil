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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79390a7a-5f3e-3340-a09d-4673424e180b | -8.769 | -48.67334 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1aa47feb-2d72-38c4-8342-3430ab66419b | -7.2928 | -44.52593 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba6ef8e1-a038-311f-b6ea-d5d1f37626ef | -8.37735 | -47.2087 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3990701c-4345-3fb7-b9ce-11143a4dca4e | -7.35808 | -44.62947 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8872abde-bce5-3b8d-bb0d-c1db5dcf722e | -8.46684 | -44.50333 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c43ffecc-6904-3a94-ab59-4b01772af78d | -8.38339 | -47.20053 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4521c34-6a9b-3d07-b84d-cb1f1cf1e8a1 | -7.68542 | -46.11623 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37dae517-ed20-33cc-9a22-ef68c64e6136 | -8.12772 | -44.83236 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f31d82e-23d7-3bae-8b1f-0bff790726e8 | -9.55881 | -46.5779 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daf9ad7c-c8b8-325d-8aec-11a0fa23a56a | -9.80333 | -48.33498 | 2026-09-19 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f581261b-866e-3ad0-a1c8-14d0ac18a994 | -4.98852 | -45.16317 | 2026-09-19 04:02:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9b3f8e9-a847-3516-a183-d3765798fc4e | -6.99245 | -45.67967 | 2026-09-19 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1268cd6-d56b-3251-a07a-01d10d812b40 | -8.66343 | -45.45531 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 479f3a72-b0f1-3780-b165-44a5dae85265 | -7.85926 | -44.86348 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 84244658-4ce6-380e-b257-fda814f2b067 | -9.75185 | -45.07196 | 2026-09-19 04:02:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4253b661-32a6-3159-a19a-300dfe22833c | -7.00563 | -49.76046 | 2026-09-19 04:02:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5d634fc-490b-3a1d-afce-09e36cb5e916 | -10.02393 | -44.34807 | 2026-09-19 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dafa4fc8-a155-3bec-a73c-be00d813684e | -7.20086 | -44.09784 | 2026-09-19 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98db8c9e-a988-3c88-a5d2-68320e056abf | -9.93809 | -45.28121 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17b6df14-8772-3b6f-b5bd-5655e97da287 | -10.20733 | -46.59453 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fa73d96-ca51-3aa7-b46d-6549c63332cd | -6.26653 | -41.67233 | 2026-09-19 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c815c4e9-b09a-3fbc-b4c8-0da8f3ae5797 | -8.75868 | -46.9206 | 2026-09-19 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4296f99e-3224-3202-8baf-7883b04c3cdd | -10.17081 | -48.4638 | 2026-09-19 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 830a5202-507d-3856-a3da-65344ad230fe | -10.52199 | -46.71241 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df58826f-cb63-3bd5-a7cc-bc0447f73cc6 | -9.92554 | -46.59393 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5a1ddc64-2198-38f4-b5ce-df6aa684531b | -9.68201 | -48.32476 | 2026-09-19 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 650ceb7f-ef92-3cfd-a948-bb8dd0138ae3 | -8.35616 | -47.541 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6ef8b8c3-995b-30b1-9c88-fe0adb315a9d | -6.28237 | -41.65993 | 2026-09-19 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a7c034be-6a31-3557-bb32-5445c4142fce | -8.37052 | -47.22129 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 151cf699-62af-30a8-bd52-5f12c78bb353 | -6.22593 | -43.7546 | 2026-09-19 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 40b304ad-acd9-3dd8-be77-743eb247ef92 | -8.77319 | -46.91449 | 2026-09-19 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5d53cdd4-2da2-3c2b-9f36-ca77184acf18 | -7.85312 | -45.16625 | 2026-09-19 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbb0e944-ff17-3cf0-a3b3-e54efdb3cdf8 | -7.22627 | -49.64083 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44eee8c5-6448-31d6-a3c0-8926e41451f0 | -6.58549 | -44.15207 | 2026-09-19 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09bd0802-0cf8-39bc-8edf-6afb20ee31dd | -9.2537 | -45.93141 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9cd02f7-a62b-3009-a96e-321330ba33be | -9.20923 | -46.76523 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac2a0b8f-4504-3790-af05-46a3f486e643 | -7.58421 | -43.44764 | 2026-09-19 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 367f2b00-db0b-39b3-9542-b80687e55671 | -8.29415 | -46.85538 | 2026-09-19 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7375a461-dbb5-3f52-aabe-94514d4e29ab | -6.00277 | -51.79618 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61723e5b-8ec7-3553-9399-aa8e37dc57cf | -7.64823 | -46.10149 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 97db4dfe-5a5b-304b-a024-6b27af473417 | -9.89002 | -46.55155 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1f08023-23b9-3db8-adf1-7cf249680f0c | -9.90398 | -46.56977 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3140eff-8bec-3795-a730-db1aa22ed77f | -10.13149 | -45.56528 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e59daddd-0006-372a-aadb-999dc474282f | -9.8929 | -46.55152 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24526bbd-f9a7-363f-a1e8-01f0788e1e27 | -3.3584 | -50.45571 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8201ba6b-2d8a-3955-bab9-a98cffd7412a | -6.98842 | -42.18618 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7c68566b-24b9-3f42-99f1-9304794fee48 | -6.9563 | -42.56464 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b77bf645-2d40-3bbc-be33-4d0deaf7b25b | -7.69082 | -46.08513 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f8d5ac4-199f-369f-92d3-b7b9ffadad31 | -3.24017 | -46.95012 | 2026-09-19 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 422596cf-65d5-30e4-89bc-cea599df9e83 | -8.55034 | -44.56278 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22c7c53d-5f03-3ee2-8d9c-d48e45d761c5 | -3.36579 | -50.45978 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7da5941b-2441-3c3a-86dc-db263ed4d9d5 | -10.13929 | -45.5666 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e16a196-fe78-3a2b-bfc2-d38b4418e8ef | -7.66884 | -46.1331 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be955dc1-0d19-30c5-a3bc-a2e8381c70c9 | -6.94231 | -43.10634 | 2026-09-19 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b7b9e4c-e9a9-3265-a1b3-7746100a811f | -2.8271 | -50.4716 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 44ceb554-627a-3362-afba-e55140747050 | -9.60616 | -45.38294 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 267bc226-2e0d-3278-aef0-3fa1a0fafbfe | -10.77064 | -46.3084 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fddad5e-0926-3c80-8240-c421efa7df54 | -4.18421 | -49.40807 | 2026-09-19 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14b57029-099a-3cea-af6b-44e5034d1589 | -7.83256 | -45.26275 | 2026-09-19 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ff45de6-2f87-3b72-8a57-866ee7db6012 | -6.99705 | -42.17603 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8b789bd-f13c-331c-bc99-a05cc6e7b5a1 | -10.10094 | -48.42005 | 2026-09-19 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9383e515-fe28-30e9-9fc1-600a9b70160c | -6.20349 | -45.34335 | 2026-09-19 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fa40c36-03df-3496-96bb-5ea57565887b | -6.94968 | -46.96787 | 2026-09-19 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c1c6d7b-ee26-3f53-b968-f82da7b43fbc | -9.65616 | -49.14376 | 2026-09-19 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b0e9f45-8756-38a9-9459-ea68533e7f19 | -6.73808 | -45.4718 | 2026-09-19 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32816916-ee60-3c94-b00b-78eeff6b7936 | -10.13979 | -47.68805 | 2026-09-19 04:02:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11403137-246d-3c6c-bafa-23628eeeffdf | -3.46503 | -50.61453 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b9e6c61-1b17-3d52-8a10-56017d6f8247 | -10.23571 | -48.84586 | 2026-09-19 04:02:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 12eade0f-f4f7-33a3-988c-d5de5bf0fae1 | -8.24607 | -45.60738 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b98a98e-3e78-305e-a024-e80298257556 | -4.2831 | -48.58937 | 2026-09-19 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8efbb33d-af89-36c9-b553-7f95ade49c54 | -7.77671 | -44.89792 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d361f0c6-65f1-38ab-821a-8c8430ad35bb | -10.24053 | -48.84682 | 2026-09-19 04:02:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3557f60a-36b0-3152-8b42-3f6e9a54f683 | -8.76067 | -44.22467 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32846814-5d38-322d-8470-2a3d8f72a25a | -10.53727 | -44.84661 | 2026-09-19 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c6e3769-f81f-365b-9ce3-5402b1a0aa26 | -7.7633 | -46.70471 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 814e028d-0157-31b0-a47a-7b11a239c926 | -7.09209 | -42.08802 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2877a0a3-5a4e-3264-9420-338682667e8c | -10.58291 | -46.54445 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 652043e2-ee37-3933-97ca-51971bf97546 | -6.70972 | -43.54655 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eaa2062f-1c07-33db-bd61-95f27915a7d2 | -3.3726 | -50.45624 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60144dfc-d910-3afa-bc34-f2477780ee9f | -6.57571 | -44.16463 | 2026-09-19 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 72a3c59d-7d31-3f1d-86ae-e3f4777ca9c2 | -4.57738 | -42.94774 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d3ec1467-1b4d-389d-9811-69222ff29d23 | -3.52184 | -50.79603 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| da0cb9cd-682d-318a-9d88-c771145dd06f | -9.15213 | -49.9973 | 2026-09-19 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c6a4154-80ce-39f6-b658-3a254bbba100 | -7.85316 | -45.16841 | 2026-09-19 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c351ad96-8050-3bff-b2de-d4514e863ab5 | -2.95749 | -52.14407 | 2026-09-19 04:02:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 068b080d-3ac4-3b25-8310-38f5d6d5da15 | -4.8612 | -48.30191 | 2026-09-19 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 554d5b80-6933-36dc-bd88-64de2842bac2 | -3.02096 | -51.19323 | 2026-09-19 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28170c9b-9149-3247-8186-2fc4b004be42 | -6.93876 | -43.10577 | 2026-09-19 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baf6236d-9181-3f5a-9f4a-8103ac840d73 | -7.65883 | -46.11547 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5417cd7d-70a1-3e79-989e-223538420c4f | -5.73509 | -43.28316 | 2026-09-19 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 429ef33c-1dad-30ca-bc81-56d1a8a0445f | -8.84298 | -50.44783 | 2026-09-19 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0149b607-5646-3583-9dcd-12ad42077f19 | -10.58759 | -46.5419 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2588a603-24c6-391e-952e-08f4d5fcf870 | -7.02437 | -44.65012 | 2026-09-19 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9036d79f-3a21-3734-83ed-8c387505d5b0 | -3.36133 | -50.44984 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 05a48e38-ef44-38c3-b386-05a536f98d85 | -10.53583 | -46.73907 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1d0ad6bd-840c-32af-a20c-932ee0e40bc6 | -10.50815 | -46.71799 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0a40597-e595-3fc7-9956-23f9e86fdbb5 | -5.1371 | -38.10651 | 2026-09-19 04:02:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3f57c2a1-7406-3554-9542-b53e80e3c2f7 | -6.20761 | -45.3438 | 2026-09-19 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a0dfac3-3811-39e3-80e6-1435c9fdc7cf | -7.79328 | -44.84506 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5cd9d1c-daff-3a26-a6e8-f0d06b858480 | -6.98679 | -42.17444 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README33.md)
