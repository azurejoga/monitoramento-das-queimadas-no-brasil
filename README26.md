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
| cb4120d8-5c41-3adc-92a9-66da91528f25 | -6.01946 | -57.82545 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bbf7d2b-9887-398d-93cf-ebfe4b788839 | -6.36786 | -51.74035 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac2cbb35-b9d2-37ec-a2b4-a6e68923f443 | -6.60158 | -59.0013 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a8151dd2-e6aa-30a8-93da-66620f463ab1 | -6.95136 | -59.29701 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1661b3a8-5003-3d1c-9e9d-365f5f33df2e | -6.99738 | -44.82809 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06c74f79-fd4d-3cc7-a8d7-a9619c8ecd2d | -9.13986 | -46.39562 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb998b13-583b-3342-a237-eb8291b67147 | -6.83415 | -56.41805 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 695814df-b737-3071-8f47-3337af34d876 | -6.34274 | -44.0685 | 2026-08-15 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5aa9c8c1-5999-349a-9afa-a1696e646820 | -6.85474 | -56.42133 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23706bcb-1b2c-3596-a8f2-7be975c3c4d2 | -6.5357 | -55.17893 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39a56803-cdcf-330e-8ba2-ff557b1a6cb7 | -6.78801 | -55.84556 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bec19239-bb95-334c-b637-51be778797e1 | -6.95365 | -59.28322 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9eb5da92-39dc-30f3-ab17-b7658cfa5809 | -6.78831 | -55.69083 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f789729-a5e3-303c-9738-a13c13454524 | -6.92319 | -43.63583 | 2026-08-15 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 259f96df-8f02-3875-9673-322919dfb9f0 | -6.84951 | -56.43198 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76005380-4510-3860-a401-a8b027db8ef6 | -6.93795 | -52.78966 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24d855e7-64eb-395a-bafe-0db760a9bda8 | -6.12218 | -44.03464 | 2026-08-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 753b2c70-27a5-3020-bf2d-6393fc4ef8fe | -6.85877 | -56.41814 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74a13bc9-f97a-3f71-bd44-b758873d267b | -2.73829 | -58.18792 | 2026-08-15 04:57:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f64bf222-c117-39c6-ac07-6f1479010d96 | -2.86115 | -46.79966 | 2026-08-15 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abb8a82e-cfe3-3399-b487-beb27a8c87d1 | -6.85131 | -56.42078 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c9559d2-1e83-3b3f-8ce2-b01d14829d34 | -6.58722 | -56.3601 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54a968bb-903b-3375-b29d-b28a3fd59a44 | -6.98989 | -45.89738 | 2026-08-15 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da251d55-a0ad-32c1-a86f-37b592ff210a | -8.52389 | -46.53219 | 2026-08-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ee45cbf-f898-3643-84b2-a11ef56b6d1b | -6.8628 | -56.41496 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 257b9a2f-7a4a-3891-b30b-f2d5d388773b | -5.49349 | -45.12035 | 2026-08-15 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4b05469-3885-3aef-8809-7fed76c32ca1 | -6.58437 | -56.35588 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cce61623-d28c-389d-b265-9f707b214d1e | -3.51578 | -58.95256 | 2026-08-15 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0244c828-74a6-3087-b0c8-e7aec22c36df | -6.7253 | -58.93675 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8edec81-57b4-3408-8c0f-b4b0cf1dd371 | -9.12296 | -46.40557 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b135949c-1343-3969-82bc-7968266be31a | -6.62113 | -59.0773 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| febeba24-b105-3a27-97c6-9ae63b72ca71 | -8.79909 | -47.92846 | 2026-08-15 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e88065a-8339-3ef2-b41b-cc03f051ce83 | -6.88211 | -41.95762 | 2026-08-15 04:57:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 703595bd-0309-3c7f-ae5c-893f2b34b162 | -6.83131 | -56.4138 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22204033-f17e-3fdf-8629-fa9ec0baccfb | -8.52003 | -46.52276 | 2026-08-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| aba5ef33-61ee-37ae-bab8-325bf0846451 | -6.70962 | -58.95727 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 17fbc120-2daa-3b17-878e-922902a5a6a0 | -9.58611 | -45.36905 | 2026-08-15 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a43d673-fcf0-3725-8e5c-20a72df22118 | -8.16591 | -47.4029 | 2026-08-15 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b3ebe0b-194f-38a1-b6d3-f3aa6ecf6df8 | -6.60441 | -56.36266 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f32f6da6-4010-3241-b105-260a102be135 | -6.85011 | -56.42824 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80f379b6-cee9-3322-9a6a-9645f52572e7 | -7.72497 | -46.24376 | 2026-08-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a46e49b-00a9-3060-acf1-b17dec209aad | -1.22273 | -54.20404 | 2026-08-15 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 270c9964-81bc-3934-936e-52d7fd8ea2e3 | -1.59016 | -50.43926 | 2026-08-15 04:57:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 872e67ee-33cf-3791-84af-d20ead7599ae | -6.62539 | -59.05188 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aebefd3b-0ea4-38b5-ae7b-25d456fc7cbe | -4.10305 | -42.50599 | 2026-08-15 04:57:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2c76545d-cefb-36bf-98ae-b3a4692bc9c2 | -6.96355 | -52.81234 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2d324b2-2a2f-3b10-ab6d-e803e1cc6a3a | -6.57956 | -56.53633 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e6a5a18-836e-331f-ba3f-ca1e45d67ab4 | -6.61815 | -58.99879 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6f6a701-d959-3732-85b3-d48978920be8 | -2.81131 | -48.59371 | 2026-08-15 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bb83b9d-17df-32b5-834c-fe264a79df56 | -4.0157 | -54.87152 | 2026-08-15 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59080ea7-5927-363b-9cfe-eeef13944249 | -6.99749 | -44.83166 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03f144ac-e61e-3a76-b0fa-8fd5a2d0c171 | -6.78915 | -55.83834 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7c0bb7b-2a6e-3c92-8613-9d812f1bf6ae | -3.10559 | -51.28001 | 2026-08-15 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6afeda18-26c5-3d54-bb4b-45dae0d484be | -6.92854 | -43.64097 | 2026-08-15 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 94cf6703-a9e3-360e-a829-4dac674ccef4 | -3.5984 | -58.62073 | 2026-08-15 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb080f19-f4c0-363b-ba04-8966c5fec53f | -6.85191 | -56.41705 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 352caf1b-0df0-3f4c-8a1a-a6d314925305 | -6.79139 | -55.84609 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac32cf69-bdf8-3200-a72e-3ec0f29e13a5 | -6.9599 | -59.29488 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 101a1706-47af-36a5-ad57-af2dbe255fa5 | -6.27531 | -43.2776 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c933afbd-948e-382c-ac1d-882458c226ba | -6.798 | -55.83651 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 774e79a9-29cb-389b-a4a3-eef00cd71e10 | -5.50212 | -60.15137 | 2026-08-15 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee19065d-d826-3425-8795-fcc1111125cc | -6.78927 | -58.74603 | 2026-08-15 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2daa7a2f-68c1-3279-bf1f-b6187d1eb3e0 | -7.01573 | -41.44154 | 2026-08-15 04:57:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1a671f94-d6d1-3dec-8fcc-c9d90cf38c93 | -7.28187 | -44.68014 | 2026-08-15 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 599cd0e3-27a3-385d-ac62-1f60143b689e | -7.82439 | -44.11465 | 2026-08-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c07500f-8049-3b9e-8d36-2942d99c0241 | -8.02862 | -55.13787 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b96d1475-60ca-3f7b-94f0-a2ea461917a5 | -8.71726 | -49.60885 | 2026-08-15 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37d72b3b-0680-33f5-9d56-4ab2d104cc36 | -9.11443 | -49.25984 | 2026-08-15 04:57:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8a023a0-d8a6-33e2-9c05-601c95eb0611 | -3.97529 | -49.45992 | 2026-08-15 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1813ebe0-41fa-3068-9913-d51ac81d112d | -9.56827 | -45.3773 | 2026-08-15 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38b57b4c-f7d3-324c-af9e-310b5a3ddac2 | -6.95648 | -59.29079 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e01eb6f9-99e0-3e2b-b587-694b9fa0b5fe | -6.96161 | -59.28453 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91bcb416-ebdb-390f-a368-b89ea12b70c9 | -8.55882 | -54.59587 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18c3e46d-e413-3a8c-97f4-620c43b20b14 | -6.95534 | -59.29769 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79d8a6f0-ee18-3f55-88af-1ad7eac05110 | -6.85354 | -56.42877 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef1b1dc9-4ea8-37b1-95e1-f549752cb9f1 | -6.85071 | -56.42451 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed6a2f7b-124d-36e9-9e78-6b0c61cf4d38 | -3.97144 | -49.45934 | 2026-08-15 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ad9880c8-93bd-3654-8183-83a3ca9004f4 | -6.14237 | -57.90243 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afa85c53-6a89-34bf-8b07-f839f9196692 | -2.66074 | -54.64165 | 2026-08-15 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61c4a33e-5ee1-3eba-8846-28d8455f6ac6 | -6.85534 | -56.41759 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e49254c-78eb-3426-8e5f-1825291f3936 | -6.6103 | -58.99749 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d078c9c5-a869-3c0a-9a2a-0b2da11a57a8 | -6.33702 | -44.06768 | 2026-08-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f25d427-f77c-3a8f-a809-77a10ef7ace7 | -6.62198 | -59.07224 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab2c1e5a-9f06-3cd8-8496-767ba4a14ff2 | -6.12339 | -44.02588 | 2026-08-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b7464bcf-225b-3b89-b444-6d940815667f | -6.25206 | -47.71278 | 2026-08-15 04:57:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bc00c3fd-4407-3769-b4f0-8eadafd82258 | -2.95015 | -50.31295 | 2026-08-15 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5558e8a4-d2ad-3879-93d7-6cf7fcbdf6f8 | -6.27471 | -43.2819 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad4b994c-365c-3698-ae27-2551c76c73a8 | -6.92376 | -43.63161 | 2026-08-15 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4718d6b7-f9b8-322f-b260-24b575e0aeba | -3.52976 | -59.02281 | 2026-08-15 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f42fc60-6ea2-3e2c-9b00-5cb23b844ec3 | -6.91727 | -43.63489 | 2026-08-15 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7259da68-6f03-3a1c-abb9-c1d8be4c7ee3 | -6.69873 | -58.95015 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98332032-3544-359c-86fe-390b418d56c1 | -6.59754 | -56.3616 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c13c6b85-b899-356c-8eb8-c7dc5c41071c | -8.17059 | -47.40365 | 2026-08-15 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d2c3361-5147-3bc2-a83b-b4ecf3220d39 | -6.81455 | -56.43031 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbcc0b69-2bfb-3399-8ca4-7715b7463840 | -7.45869 | -55.30082 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| fa2903e0-36fa-34a9-bbcd-2d3161ea7fb6 | -6.65728 | -59.10389 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bf29d9a3-caba-374f-bcdd-cbe2c9e7f790 | -7.03939 | -55.50119 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3f6f8aa-79d1-31d1-9f53-6cacadc99a36 | -6.20837 | -57.76862 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 9b93e6fa-15cc-30cb-8c41-bf568d4345f8 | -3.97323 | -49.45796 | 2026-08-15 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b22e56d1-43ee-37a5-8fe9-059f1df5af2c | -6.60704 | -58.99399 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |


[Clique aqui para ver as próximas entradas](README27.md)
