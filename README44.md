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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f60957d-ed0d-3efc-9ba6-1e322fce41c9 | -4.25018 | -51.04741 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c97994a6-9777-3d18-91c2-de8f15d9aeba | -2.96004 | -51.04917 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2a0ed9c-eb10-34a1-9974-30bc1a475fa1 | -7.46512 | -47.59924 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35e9e62a-faf6-34ca-893a-f596d33a6003 | -3.50318 | -51.68848 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91a581e6-ed6f-3cb4-9c23-d1fd070816b9 | -2.96729 | -54.13315 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74f09baf-fd9a-3c60-a206-1a37a3b0fcc9 | -4.1308 | -46.83731 | 2026-10-07 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06d2348a-5d40-3009-aee3-61bea5d5570d | -5.97662 | -40.91355 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bc963353-8b0b-3060-aab6-60ae61af5205 | -3.2818 | -54.06128 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 081ae797-3eeb-39d5-ba14-5d1962e32e02 | -5.74937 | -43.26962 | 2026-10-07 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fbc114ae-d3d3-3ebb-afc4-657673ccac73 | -3.50783 | -54.66594 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 10edc422-7f35-315a-9a15-cbd17eec0d88 | -8.20707 | -46.348 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22533953-bffe-3dad-9c33-9f9855e9e411 | -4.25105 | -51.0443 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6100715-5375-3889-b675-29eafd460532 | -3.27132 | -50.39788 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8daefbb4-fe72-3461-9758-2fef5081c116 | -5.24411 | -47.93602 | 2026-10-07 04:19:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9899288f-aa73-3e2d-81bc-aab1c050b6b6 | -3.07189 | -54.18446 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df7c2552-9527-343c-9dd0-5f23dc2497dc | -5.41582 | -45.73106 | 2026-10-07 04:19:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5e10622-5d70-3b2f-bc43-a4e4860f4b3e | -2.98114 | -54.05357 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40189ab7-dd2b-352c-a3dc-1ea142e909c1 | -3.09649 | -54.15417 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9c3142c-00ae-337f-91ad-0db41cb3de19 | -5.98191 | -37.83007 | 2026-10-07 04:19:00 | NOAA-20 | UMARIZAL | RIO GRANDE DO NORTE | Brasil | 2414506 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3378b1b3-b0e3-348b-ba1c-e2192f31f07c | -5.17783 | -46.27533 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 755947ac-b664-3366-9d34-44fd239e8092 | -3.58165 | -54.30756 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35d6232f-9038-358c-8a18-8dbabd0db6fc | -6.02631 | -42.26472 | 2026-10-07 04:19:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 050e8121-f529-3db2-bc30-906d61442129 | -2.60806 | -45.51012 | 2026-10-07 04:19:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e5c29a2-82ff-3144-bf8a-ea66e89b422b | -5.97721 | -40.90974 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b567e335-9938-3d17-97d7-153349803045 | -3.98748 | -56.25021 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79f6ab2b-9ec6-3a24-b669-8f4568150fb3 | -2.87034 | -54.15056 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ecb0f8bb-5828-3e47-a642-ba8dae8c802b | -3.17775 | -50.55054 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a2be740a-1b2e-3f01-b3be-a402124f1114 | -3.09238 | -53.73875 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7954e2d7-b5db-3cd8-a93b-67105fc317bf | -2.76898 | -54.09674 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 1d1265f5-6a8f-34ee-9e3f-0920149687f5 | -3.28831 | -54.06938 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 37c4bf61-5078-3079-a7b0-6f956d77f2d3 | -6.88218 | -43.68771 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4c4961f-bd91-33e0-b63f-78ebc5c821c0 | -5.02997 | -44.70929 | 2026-10-07 04:19:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8511c7e-695a-3a2a-8e41-21e247c7a7f9 | -7.20215 | -44.3034 | 2026-10-07 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0254da51-3bb2-3abb-ac1b-d65b8d553c83 | -4.9219 | -55.8691 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43ddb914-daf4-3398-a7ba-a5aff846da20 | -7.18436 | -52.62449 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da135aa1-32a9-388b-8253-3cebc8457407 | -2.77524 | -54.09787 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9dec709c-b91d-330b-a846-d6243422371a | -3.70138 | -50.98468 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33e2134e-0347-36d3-a4bc-1e68be5d666f | -7.75092 | -49.20784 | 2026-10-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7799e8fe-dcf2-323a-a807-61647e9b311f | -6.33324 | -43.82759 | 2026-10-07 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0addb99a-6e72-3dc6-9bef-8e7312ac8a2c | -3.29842 | -54.03941 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 565a2f5e-d177-3e57-82a1-46beccd79a97 | -6.84599 | -41.76971 | 2026-10-07 04:19:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1d94568-dade-3cc2-9cc5-afd3d32dc297 | -3.2838 | -54.05826 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 17fc8236-7a41-307a-aaa8-d401629706f3 | -3.20737 | -53.8782 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2a4232fd-2ec5-3dc5-becb-db1d6e226dcf | -3.29081 | -54.05453 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 998b8446-160b-3257-bed6-10620501fa06 | -4.99577 | -56.048 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 755e3c08-1f8a-3ca2-b35a-6bb3ed64e5c8 | -7.10766 | -42.53793 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e0b9c2bb-f102-3c6b-b96d-910e26d2e466 | -3.12301 | -53.70588 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 669196dc-7129-3bc5-a763-40e36a8cc21d | -2.57043 | -50.68252 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5b9bca4-b712-388f-a7cc-05e59d86cfd8 | -3.81063 | -51.03794 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d6e4731-9419-3fcc-be9e-afdaf74e8418 | -3.2727 | -50.40292 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| accb5d6a-1629-3bea-9744-817ee2616a71 | -3.01121 | -54.14005 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7740aea-2c6c-30c6-a1bc-bc0cd2177a1d | -1.29259 | -54.56004 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e984106-8e26-3907-8d3e-286ba92a8a9e | -6.15291 | -51.73528 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7b8c2e4-34a1-3848-a863-2ab8ce25fc01 | -5.97996 | -40.93758 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| f3991698-fecb-3008-a501-17e796d14189 | -3.24004 | -50.17845 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27866765-93c0-32b5-9660-444a3d0124bc | -3.29925 | -54.03463 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39b9f11a-ef2b-3b02-9afa-c1b8b87836c6 | -3.09688 | -53.74923 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78d63031-1e68-37f5-be03-f425ae05bb4c | -3.09476 | -53.72479 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32d772d8-2f0c-3a58-b439-0a24a44bda86 | -4.92861 | -55.87049 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2c80cf4-5a00-31bb-8431-273bf59b2f5f | -6.99801 | -48.65355 | 2026-10-07 04:19:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a0d9e36-c416-3c9c-8892-9a3b089fb2ef | -6.37989 | -42.54596 | 2026-10-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dd9bab50-69a6-3da3-9755-0497fb2373d1 | -3.29324 | -54.04014 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9057f6f6-db42-3634-9751-2e886f95090e | -3.54382 | -50.0965 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec36d46c-eadc-38f2-96be-a29cb2feb6aa | -3.34619 | -54.17012 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5d55a3c1-f4a4-3155-8781-c55b587c9ea9 | -3.12909 | -53.70696 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c31aca6-d6cd-36c8-bd89-0a57b2a155be | -3.09489 | -54.16343 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f71190eb-120f-37a3-82ae-b31efd7a5916 | -3.49767 | -54.64811 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ac99d13-a2a3-3e4c-8441-ac20987915dc | -6.93719 | -43.06144 | 2026-10-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75104822-022c-3264-9990-c7fcdee4632f | -3.13305 | -54.37145 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2d50c0b-bcd4-395b-a8d2-7dda83927a79 | -3.00582 | -54.1339 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2d07653d-6574-387a-af36-e4340313a73d | -3.98352 | -56.22308 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2dc73aad-28ea-3d4c-916e-b306c5160753 | -8.38715 | -46.28791 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0970c19f-118d-3d3a-9858-15db13f6c7cc | -4.076 | -54.89395 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b8a2a5a-bc5c-3b2d-bf5a-e91777d2561d | -3.80705 | -47.48914 | 2026-10-07 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3df7e423-e3ba-3320-a89d-6d275ad4a910 | -6.72959 | -45.80605 | 2026-10-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ba9febf-6c54-3ae3-8173-1d0398d1b12c | -6.20268 | -49.38061 | 2026-10-07 04:19:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 634fa020-00a0-3b5a-b538-c5e204c7db49 | -3.29868 | -54.07436 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5606f8dd-16da-3074-b887-d389e59d2333 | -3.97012 | -56.06305 | 2026-10-07 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bab0c753-d17b-302a-a1be-27edc527a481 | -3.09554 | -53.72018 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eac4d61a-c7a6-37a8-8bd7-48286e61b987 | -3.49352 | -50.10129 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f74fb3fd-d44c-3f94-a3f8-fe4e8910e729 | -3.52609 | -54.64278 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d6e3084e-c09e-3860-8836-ddbb3b3a9c85 | -7.86059 | -44.17968 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd5151cd-5fef-333e-ba14-9f87208e377d | -5.68022 | -53.49131 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce01b9db-a4d3-324a-8ce2-784cc1c46e77 | -3.27592 | -54.06706 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 097ae92f-d1ee-3f2a-b60f-50d9e2f31ed4 | -3.53787 | -54.65088 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e299edd1-2d6d-3c33-ba93-58b94661e600 | -3.01744 | -54.14132 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29968a43-3bb1-3957-99d6-17d82739eb8c | -3.50116 | -54.67166 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8aeebc31-5597-3d05-a184-da8fd7af9bdf | -3.29689 | -53.86863 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0d16523b-6bd2-3421-ae11-a6379b5d1fa4 | -3.04421 | -53.91005 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d7b4ed9b-62bb-371a-9a42-15a2fd98e96c | -3.80552 | -51.03748 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c6613b5-24c5-360d-8303-31d99cc57fb1 | -3.12831 | -53.71161 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eba8bc04-170f-3dea-b01f-7c342bb07742 | -3.28087 | -54.03783 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e1de4712-093d-3bde-9f34-cc9e328e3624 | -1.27947 | -54.55754 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ad352f4-ce66-32e1-88a9-8d17bb8be372 | -5.72541 | -45.16059 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 00e99ddc-b618-3ac5-991f-9ada09acdc84 | -3.09981 | -53.76906 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82fd8efb-e364-31a8-8579-483452967460 | -3.08032 | -54.24777 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06a109da-ce0b-3108-8ccc-5c5714e6ee5e | -3.28544 | -54.04855 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b7c77b7f-5e62-377e-a29e-10437bd7aa2a | -3.97825 | -56.22055 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42f77124-0187-327a-bb5a-997faa7c0658 | -2.79898 | -54.09307 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 774bc3b9-fd69-3a3b-8e35-dd51b4638f8e | -3.11045 | -53.7805 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README45.md)
