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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c5b03f6-d101-3dbb-a2ae-f50c783bbeb0 | -4.58215 | -43.01983 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8efdbb8b-3eb1-39d5-9b3f-142167bfed4e | -6.65441 | -51.49105 | 2026-09-18 00:01:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| acddcfe1-31ab-365b-88d3-08493dc578dd | -10.12516 | -45.65398 | 2026-09-18 00:01:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9257a931-69a1-39cf-bed3-aba340a92b12 | -4.56133 | -42.97581 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| a7b53a76-9adc-3f8c-b98e-42ac1a867b08 | -4.56519 | -42.95796 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1559.9 |
| d5fcc348-7242-3f86-b493-4ba8a9f8cf8b | -7.00124 | -43.87581 | 2026-09-18 00:01:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 41.0 |
| dfab0644-01a3-3086-a971-7d501e27a57c | -11.05616 | -48.30413 | 2026-09-18 00:01:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c371474a-30d5-3578-a2ca-abb5e2907e28 | -11.06501 | -48.30293 | 2026-09-18 00:01:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c7b73235-2d26-3f60-9ba6-c7551cfabc49 | -6.0332 | -51.80456 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 48965082-7388-32d6-a5a3-fdbd2174d710 | -7.80303 | -44.89398 | 2026-09-18 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 64e2a921-4355-393c-a49f-08833701807b | -4.35654 | -47.78394 | 2026-09-18 00:01:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 585dc412-6413-3dd7-83db-c6618c5c7093 | -5.22306 | -49.30633 | 2026-09-18 00:01:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 47eae7cf-9325-3310-87a8-f1db291ab355 | -7.94159 | -49.56482 | 2026-09-18 00:01:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| eb45ab5a-ec34-348c-b563-d2023fe913fa | -9.91153 | -46.55763 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6e10e4a8-fb2b-31c3-bf32-75ed097f09d2 | -5.76214 | -45.79719 | 2026-09-18 00:01:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e726d353-e2df-3a2d-bb86-ba4b2af7381b | -5.79483 | -51.66993 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 01d573b3-3b87-3c71-8285-055af3641e7a | -7.66851 | -46.08381 | 2026-09-18 00:01:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e7118b52-80ce-3762-80fe-7cf7d1e3be14 | -10.12134 | -45.56304 | 2026-09-18 00:01:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 979f561c-b33e-32cb-80c3-86d9ea3bd5cd | -11.07505 | -48.29532 | 2026-09-18 00:01:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 379022e6-5945-3525-a72e-d70707d44094 | -6.66893 | -50.91364 | 2026-09-18 00:01:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 72aac489-5e0c-32a7-acad-1cd39b7cbd51 | -7.00704 | -43.86224 | 2026-09-18 00:01:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 640b94ab-878e-3688-9707-a4f0e16d4e19 | -8.94339 | -51.47286 | 2026-09-18 00:01:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 1a32263c-e333-3b27-988b-d2d5c403962b | -6.9644 | -46.95058 | 2026-09-18 00:01:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0332a321-cc08-3c9b-94d8-6864b1faf777 | -5.86598 | -52.0546 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ed42c3c3-c5ab-303a-8d73-2fd67eebc371 | -6.46981 | -48.00886 | 2026-09-18 00:01:00 | TERRA_M-M | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 30.8 |
| bb7ad56c-a28d-3a3d-8353-f59bef99de91 | -4.4994 | -45.90465 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| ac3640ea-9d2b-3d53-bad2-40f8a4106aed | -8.88012 | -45.89357 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7cc396bf-3406-3ad5-a694-be882719fbe0 | -7.05353 | -46.22041 | 2026-09-18 00:01:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 57742626-5bc2-39e5-ad0a-75a6419ca8eb | -6.34549 | -43.38288 | 2026-09-18 00:01:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b728a1ef-be31-3c73-a661-424dff5f3349 | -10.64897 | -50.24266 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 53c47da2-fbfa-3032-ae6a-49c7a4af8b17 | -7.68039 | -46.0943 | 2026-09-18 00:01:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 8e881ede-e8bb-341f-981e-8af32ab1af3e | -4.01696 | -49.18884 | 2026-09-18 00:01:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f6085fa-038f-3d19-8b5e-cb17e10e5cc0 | -9.16067 | -49.99923 | 2026-09-18 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| fca91541-9c0c-3ea2-9cd6-8f37affeb573 | -8.93772 | -44.39549 | 2026-09-18 00:01:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3cbca3c2-2205-3701-b430-c9ab1351e24d | -11.07377 | -48.28621 | 2026-09-18 00:01:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| e2687fbb-5d35-37b5-a94f-ad3cb04ceddb | -5.76408 | -45.81033 | 2026-09-18 00:01:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 89faab15-e6d0-309f-b496-82240575c079 | -9.94767 | -46.60525 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bb6e7c9a-59c7-30db-a73e-bc692cf04e47 | -5.83147 | -52.07975 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 839383ff-47b4-3b61-b96b-fa6297c95b59 | -8.55399 | -44.89712 | 2026-09-18 00:01:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 21385c2b-fdb9-3c43-bf76-aae408a2f7f8 | -10.54814 | -44.84555 | 2026-09-18 00:01:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 58477e4a-8370-3542-95ff-727cd7c7c9f5 | -10.66047 | -50.26006 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 54226e17-c0bc-3bc5-a653-b1ad7e17689e | -4.50138 | -45.91831 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f9ed30f5-2682-3f77-ab6d-acf907094a33 | -7.63861 | -46.16134 | 2026-09-18 00:01:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 04212791-713d-3e82-8193-1168766b5ca8 | -10.99547 | -49.73249 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bc62166d-3eeb-345d-b1ce-e280b655d59e | -9.74248 | -46.53041 | 2026-09-18 00:01:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 29a87999-3c12-3092-a470-a472c2ea3137 | -10.12314 | -45.56947 | 2026-09-18 00:01:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 297d66f0-e2d2-3d88-9df2-c969854b8286 | -8.93274 | -51.46408 | 2026-09-18 00:01:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 56f11201-2bf0-36a6-b0db-7d9590f7a083 | -6.36343 | -58.28773 | 2026-09-18 00:01:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 573972ac-33b2-3abb-90a7-65481e6d35ab | -7.79195 | -44.89555 | 2026-09-18 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 54229e2e-f9f8-3522-b487-ffbadafd510f | -11.46614 | -51.48502 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f011964f-39a5-3913-8b4e-4d78a49ae126 | -9.71936 | -54.82641 | 2026-09-18 00:01:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2b7fb0a3-a386-331f-832a-8cc30be1a7eb | -10.09046 | -48.1846 | 2026-09-18 00:01:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9d9043c9-f38b-33aa-af70-1ee784c8904d | -11.3257 | -46.76301 | 2026-09-18 00:01:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 631772e7-8738-3100-8a5d-a394983a597f | -6.3007 | -41.7869 | 2026-09-18 00:01:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 76108ef1-9347-39fa-b2f9-ab4d8bcccd86 | -5.72737 | -51.71414 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b17817b9-c75e-37de-8a98-b966e648ae6b | -5.6389 | -44.80743 | 2026-09-18 00:01:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 29c8fc34-7cbf-3116-9a45-daf4ee35f361 | -8.84509 | -50.45596 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6b4e3238-bc0d-3989-9f0e-b2a9b7cf94a9 | -11.53813 | -46.88956 | 2026-09-18 00:01:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b635d02-2d7c-3c34-bf02-4d44bda44627 | -6.51934 | -49.88142 | 2026-09-18 00:01:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a2df7707-5fe6-3603-8cbc-85018437559d | -4.01137 | -49.95708 | 2026-09-18 00:01:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 10995a29-26f7-3108-b78a-943cc5fd6060 | -9.77553 | -45.04382 | 2026-09-18 00:01:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| e9b67ab3-1717-3e3b-a16c-c75a956f4c38 | -5.50228 | -45.51212 | 2026-09-18 00:01:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5e2725c0-9415-3176-8748-4aaa1ece38e6 | -6.01192 | -51.77428 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| bb65563d-1bd1-37b2-942d-a6b845e812b7 | -10.65563 | -50.50056 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2675d568-164d-32a2-9e5d-8e45d9628ff4 | -11.13216 | -49.04972 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a40fe6a5-903b-3d37-bf43-20b35a5abb3c | -9.90633 | -48.38014 | 2026-09-18 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9c35ef82-115a-386e-b1c5-184b88061bde | -10.09173 | -48.19366 | 2026-09-18 00:01:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0efc09f8-06b4-326c-91af-792094d0d345 | -9.71709 | -48.15199 | 2026-09-18 00:01:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6e068eba-36ac-37f2-9e7b-633362174287 | -3.03594 | -51.36764 | 2026-09-18 00:03:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 9e8d4cc9-c07c-3f67-862e-18e7fca5bf7e | -4.38714 | -55.03244 | 2026-09-18 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bd35ee44-52a3-3334-827a-5f541680ac70 | -3.46802 | -54.70227 | 2026-09-18 00:03:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 710838af-66fa-3441-9c01-4fb75ad431f0 | -2.90347 | -54.17395 | 2026-09-18 00:03:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a27dd8d0-2fd5-3eb2-9816-93f3a5786022 | -1.22304 | -49.25235 | 2026-09-18 00:03:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 71350f35-f068-3607-ae6a-2c7958e14fcd | -3.42718 | -50.66253 | 2026-09-18 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ad00972-68bb-3923-ba59-2aa17e644ec7 | -2.9662 | -52.14234 | 2026-09-18 00:03:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 93d7cbd0-07e1-3c65-85ee-d8ea7f0accdc | -4.53581 | -54.94022 | 2026-09-18 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7277fd94-1e8b-34ab-a71d-19e8165ffb64 | -1.78591 | -47.84205 | 2026-09-18 00:03:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| d5c73a33-3dc3-3a7f-b407-d631a3645a98 | -3.37191 | -50.45608 | 2026-09-18 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a4b1dcdf-2974-38bd-8ff5-dcd5ff777f14 | -1.18767 | -48.80758 | 2026-09-18 00:03:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95acde15-6f65-39d7-a929-829db38c9ee9 | -1.38535 | -49.36114 | 2026-09-18 00:03:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b84ea8c-991e-37b5-a616-7bec0ff39226 | -1.44645 | -49.33661 | 2026-09-18 00:03:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 76cf1817-735a-3168-8883-ae804f99d5b1 | -2.86979 | -49.62371 | 2026-09-18 00:03:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c18f8730-e359-31e7-9abd-7e991b0d1876 | -4.44096 | -55.52652 | 2026-09-18 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| ba2cfddd-3268-3a2c-bff0-2af266269f29 | 1.25899 | -50.77741 | 2026-09-18 00:03:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a09be281-be10-3fe4-bb68-3711bc0974b2 | -2.89324 | -54.17539 | 2026-09-18 00:03:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 08803dcb-787b-39c1-b712-9df33063b3a0 | -2.48879 | -49.40602 | 2026-09-18 00:03:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| da50559e-cd4a-39a3-90f8-c257cab805e6 | -3.37071 | -50.44733 | 2026-09-18 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 18c41e55-f13e-39ff-a698-294ebb5d32bb | -1.03219 | -53.74108 | 2026-09-18 00:03:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2ed9ea2d-9b10-3628-bcde-8ff91e631dca | -3.452 | -58.22044 | 2026-09-18 00:03:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6c5d6271-1992-34b4-a90d-e396f6a65336 | 1.26142 | -50.75971 | 2026-09-18 00:03:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b128ef2f-a75f-33b3-97d2-fae621ed28a0 | -3.21005 | -53.94995 | 2026-09-18 00:03:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1ddde50c-d410-34e7-bbef-426fada48f22 | -1.78727 | -47.83558 | 2026-09-18 00:03:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 44674634-16b9-38fe-9976-465f8b6b6c6b | -4.49316 | -55.49656 | 2026-09-18 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 863a2b10-11ba-3b0f-8abd-20a4ef2bc8e6 | -4.50606 | -54.97978 | 2026-09-18 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 06c28313-392a-3245-a363-febead16b758 | -4.50614 | -54.97406 | 2026-09-18 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 021d2b5c-1e8a-3560-b413-9f54ea674969 | -3.3807 | -50.45485 | 2026-09-18 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 433a061c-b068-34fa-9147-8424d429b4b3 | -3.96698 | -52.18897 | 2026-09-18 00:03:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8adb15be-70da-38e8-97cf-c7ffec75d6ff | -4.42936 | -55.52865 | 2026-09-18 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| b4cc3322-67f0-3ea6-9273-92aa1135576f | -3.04481 | -51.3664 | 2026-09-18 00:03:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3a152702-5d09-325f-a012-7984a833fe7e | 2.09452 | -50.86737 | 2026-09-18 00:03:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README5.md)
