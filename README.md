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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2949d9c1-b2f3-3388-add3-b99ebf9011b6 | -10.4527 | -47.2801 | 2026-10-08 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 57dfac33-e076-36cd-bb59-882647a50cdd | -3.5515 | -59.4807 | 2026-10-08 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 8bc07091-1a4f-391c-8f30-f808d752933b | -3.8383 | -55.9774 | 2026-10-08 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 78c801d4-dc32-3e8c-b232-98eeffe1b601 | -3.6049 | -54.5736 | 2026-10-08 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 71127c2e-f01a-39c8-aa88-5e0ddb421fa8 | -3.1114 | -53.7839 | 2026-10-08 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 82a1f5de-cbcd-34ef-9f9f-86f63948ec7a | -1.4569 | -54.7761 | 2026-10-08 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6a83090a-a852-3991-a925-3731bd27d12e | -10.4337 | -47.2824 | 2026-10-08 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 347ee43d-4e6b-30c9-b9fb-ab92d67cf303 | -4.3473 | -43.779 | 2026-10-08 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 4fb927ba-1171-3341-bab1-bf30b7bd5bbc | -3.1298 | -53.7834 | 2026-10-08 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| aa605781-01f5-3b06-b7cc-cf2f2881d421 | -8.7231 | -45.1583 | 2026-10-08 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| b05acb5e-cff1-3ce8-8be6-5b98e971eab7 | -3.1297 | -53.8036 | 2026-10-08 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 57417249-e381-3e1a-bd11-6c531990c039 | -5.7189 | -45.1547 | 2026-10-08 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 36e60a77-3688-3c6c-85b9-8feb005c4eea | -3.1697 | -58.6437 | 2026-10-08 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c4c679b3-d3f8-3877-b7ec-fb7273c9f849 | -2.8575 | -59.1107 | 2026-10-08 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a1e44883-aa17-3868-a2a8-49a170f55ec5 | -3.11 | -54.1862 | 2026-10-08 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| d2c9db98-f39b-323a-b424-999bc1632e08 | -6.6319 | -43.7068 | 2026-10-08 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 5c1871c5-27b3-3952-8826-c258783a918f | -6.8952 | -43.6833 | 2026-10-08 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 3ced77eb-129b-378c-8a85-b4c8bec1aede | -3.1097 | -54.2865 | 2026-10-08 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 03450d98-81ae-33e3-9c1a-03569d971d03 | -6.2158 | -52.849 | 2026-10-08 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| ccc3d87d-9da1-3633-bd87-ad537138b89c | -6.6317 | -43.73 | 2026-10-08 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 348.4 |
| 1c64e116-c00e-3ea9-97f0-ba850ca04321 | -3.1114 | -53.8041 | 2026-10-08 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d796bf80-9902-38b9-9bd8-4c82632011e9 | -3.1697 | -58.6244 | 2026-10-08 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 467d0832-9a2d-31dc-8bf0-4773e89d0821 | -3.8567 | -55.9769 | 2026-10-08 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 3dcdccbd-70bd-3a48-be1f-722fa4397802 | -3.1786 | -50.6016 | 2026-10-08 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9385a24b-8c14-396e-8286-885d9f9e5c55 | -9.475 | -64.3525 | 2026-10-08 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 89a7fba3-51a0-3fe3-b25c-6b7f7326c0ce | -3.5698 | -59.4803 | 2026-10-08 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 268dc731-f85b-3c73-beda-aebef20aae0b | -6.2343 | -52.848 | 2026-10-08 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 176.7 |
| 9d52dc1d-e7f6-3808-8835-72f951f97c6d | -6.6129 | -43.7317 | 2026-10-08 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 98effa16-845d-34e4-aab1-b608f53f86e1 | -9.0407 | -65.9215 | 2026-10-08 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| dff68ada-e0ec-3fd4-b71c-db4b44e1503e | -6.998 | -71.6456 | 2026-10-08 00:00:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b0d49c0e-c769-3c5f-ac3f-e2883fd66313 | -6.2529 | -52.847 | 2026-10-08 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| ee53dc10-5ad0-3730-9ad0-d0fca218bd6e | -3.1101 | -54.1661 | 2026-10-08 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 8591cfc1-edb8-3180-9331-4b48e8e302b0 | -9.0591 | -65.9396 | 2026-10-08 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ef1185eb-b5e4-351d-a714-cfff36d89d47 | -6.15 | -39.4409 | 2026-10-08 00:00:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 66.3 |
| aaf7b48d-85ae-3892-bebf-881d08d822bd | -2.7796 | -54.0937 | 2026-10-08 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 895d706a-445a-3769-9449-ade426aba94b | -8.7225 | -45.204 | 2026-10-08 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 2cef6765-1c34-3fc9-9393-046ee0a1960f | -16.8948 | -40.8938 | 2026-10-08 00:00:00 | GOES-19 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.1 |
| e0f6d4ea-201a-31d5-9896-bb9921ba681c | -9.5351 | -35.8148 | 2026-10-08 00:00:00 | GOES-19 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| fea4238e-fd46-3553-bd26-5940ad9c1ac1 | -3.1973 | -50.5382 | 2026-10-08 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3c81d319-1be0-36a5-814e-4753f769f657 | -3.3134 | -53.8592 | 2026-10-08 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c020b5b5-bb10-349e-be64-214ba52a4554 | -3.1792 | -50.4551 | 2026-10-08 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 04daa0b8-9f51-35fe-b587-ed683b3ca449 | -3.1972 | -50.5592 | 2026-10-08 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.5 |
| c9e94e2d-115a-3b02-9998-9fbe35254205 | -7.2185 | -55.1016 | 2026-10-08 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 19c3562a-2199-3846-b5b4-65d02c706ed2 | -5.9586 | -55.3648 | 2026-10-08 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| db510a9f-8c78-381e-8fcb-be48395366a3 | -7.1964 | -45.354 | 2026-10-08 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 3520a31a-90b8-3af8-9b0a-5d003cc8622a | -9.0406 | -65.9401 | 2026-10-08 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c79665f1-2ae2-39bf-a0f2-93a16eda841b | -2.7612 | -54.1142 | 2026-10-08 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| faf0a9d8-474b-387a-bb4a-f7551f0f74e2 | -1.4569 | -54.7562 | 2026-10-08 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a0c6bdc6-cd7c-3067-a127-ab45ffe643ad | -3.0913 | -54.287 | 2026-10-08 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b390215b-6c63-36e7-80d8-5c1e3b3fe982 | -7.4443 | -63.5401 | 2026-10-08 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 047a113e-c116-37e3-ae3c-66ffcdd9d689 | -4.0628 | -59.8328 | 2026-10-08 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 1c6cc555-8211-3e8b-8cea-8551e010a0ea | -2.1629 | -59.2361 | 2026-10-08 00:00:00 | GOES-19 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 94a30611-834a-3d88-a71d-12fa180b10ba | -3.073 | -54.2874 | 2026-10-08 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| e2737873-dced-3149-98e4-234f8be83849 | -9.0592 | -65.9209 | 2026-10-08 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 2bc97109-a590-33bf-a55e-dfda3c081774 | -4.366 | -43.778 | 2026-10-08 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| c73ab53b-1e81-387a-81e6-453ccf79dabe | -3.9663 | -56.1119 | 2026-10-08 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| e473a62b-e9d1-31ac-b214-bfdcdacbf09e | -3.1607 | -50.4556 | 2026-10-08 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c9f6e1a5-b401-3180-948a-5ec099315990 | -2.7981 | -54.0732 | 2026-10-08 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 1984298b-218d-39f1-bb45-1e1627ccd87b | -2.8896 | -54.1715 | 2026-10-08 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| c3fbefa2-5888-3349-aa79-dea94a33fc43 | -3.1115 | -53.7637 | 2026-10-08 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 1982427f-3241-3b0a-a658-d9e4a166fc78 | -1.5302 | -54.8151 | 2026-10-08 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 46bca873-9323-300b-b123-f1077348eaf7 | -3.5866 | -54.5542 | 2026-10-08 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 791b9bd8-b229-3b72-a424-d2832766d298 | -5.9587 | -55.3448 | 2026-10-08 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4257ddf8-6644-3a22-879c-c2ae1693a83b | -6.2157 | -52.8695 | 2026-10-08 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 63765932-84c1-317f-975c-bff7ad6d128c | -9.4935 | -64.3706 | 2026-10-08 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| b5dc7213-a3f2-3870-8366-4a67a41f51a5 | -2.8895 | -54.1915 | 2026-10-08 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 3f0e9182-b0ad-3f06-af04-bcc4c124112b | -2.1446 | -59.2364 | 2026-10-08 00:00:00 | GOES-19 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 7dd6b882-329b-3e94-907e-2192fa27edca | -9.4936 | -64.3518 | 2026-10-08 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.4 |
| ded209cd-15cf-3823-bd25-b6149510d0d7 | -1.5306 | -54.5558 | 2026-10-08 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| e49e14e3-5b50-39f4-9713-df3ee805ae5a | -3.8566 | -55.9967 | 2026-10-08 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| f7d9eaf9-38ba-319d-94f8-5cef8e27134d | -4.3471 | -43.8021 | 2026-10-08 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 685ae80a-e2b5-351a-9571-aaaec57d0262 | -2.7797 | -54.0736 | 2026-10-08 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| d3201ff4-afcc-3d61-ac02-2bf6ac333c87 | -10.453 | -47.2578 | 2026-10-08 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 8f73b9bd-8c07-3048-8484-4b4bc85eae0a | -6.8764 | -43.685 | 2026-10-08 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 04496cf4-f2d4-37c2-8a71-df70e43314ee | -2.798 | -54.0933 | 2026-10-08 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 575a52eb-8fe0-3001-b322-b9f78e4273cd | -7.4442 | -63.5589 | 2026-10-08 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 9abeb553-a344-3afd-9dff-ac7260a14815 | -10.434 | -47.2601 | 2026-10-08 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1b180a44-564b-3cb5-b46d-d9a26e77b575 | -1.5301 | -54.835 | 2026-10-08 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 41e46e6c-0cc7-3469-84b1-2b8fe26aa60a | -4.1176 | -59.8888 | 2026-10-08 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 6abd328e-bc32-3413-8219-8dc502f0aa59 | -2.572 | -56.1646 | 2026-10-08 00:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 47d374f2-9208-34b3-9aa5-2d94327bd720 | -2.5903 | -56.1839 | 2026-10-08 00:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 6a7d77e1-d1bf-3330-964c-781afb95c2e5 | -6.3353 | -43.3365 | 2026-10-08 00:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| a7b0b1b7-845d-3fc2-a578-74d9c04de1d4 | -6.9797 | -71.6457 | 2026-10-08 00:00:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 82f8bd9b-4096-38a3-9c3f-84e4a2e3b5b1 | -4.3658 | -43.8011 | 2026-10-08 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 1464e27f-d2cf-39b0-9d12-4799ece81980 | -8.3882 | -46.3006 | 2026-10-08 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| efcf456c-4ef4-3a3e-a314-5074871365f8 | -3.1879 | -58.6433 | 2026-10-08 00:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| ae52970a-e212-3e27-ab17-df7b31cd244b | -3.1285 | -54.1657 | 2026-10-08 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| be00ca2f-a54d-380d-9a4e-124d53c23cd0 | -8.7039 | -45.1832 | 2026-10-08 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 1647bee7-c982-3da8-91c7-5f3287880bee | -1.5118 | -54.8352 | 2026-10-08 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 9859bc16-c983-3802-b990-4c8134f9297c | -3.1601 | -50.6021 | 2026-10-08 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 08635d57-bf64-3060-bb8b-c45cdd3f523a | -3.2157 | -50.5586 | 2026-10-08 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 041f87b6-fb6e-359e-82e5-350afbbc59ba | -7.7579 | -54.9499 | 2026-10-08 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 3f98593b-e3ad-3ed4-8c71-fb92b37f4467 | -9.8261 | -44.7781 | 2026-10-08 00:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 5001514e-b3bf-3c2f-a89f-1d55d95e0239 | -3.2313 | -46.9596 | 2026-10-08 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 587f7848-b8aa-36be-87a8-113d40f4968e | -16.8634 | -40.5966 | 2026-10-08 00:00:00 | GOES-19 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.6 |
| 43ba4e87-78a1-3776-ae64-2951928a8470 | -6.0935 | -49.411 | 2026-10-08 00:00:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 992f9f16-082f-3035-a659-100c6001a5fe | -9.4749 | -64.3713 | 2026-10-08 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.4 |
| d92fda42-97a1-3aee-982a-e495e4e0b903 | -5.6932 | -53.487 | 2026-10-08 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| ea86325b-b868-3e9c-88a4-49208a5c64bf | -3.073 | -54.2674 | 2026-10-08 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 21d70a62-58fc-384f-a479-849a5b820a71 | -6.8762 | -43.7083 | 2026-10-08 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |


[Clique aqui para ver as próximas entradas](README2.md)
