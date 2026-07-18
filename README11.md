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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a10ce02b-b7f5-392a-bc8c-6224581b6a94 | -12.79667 | -46.56667 | 2026-07-18 04:38:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5741cc55-c527-31b3-bb67-2d43999bd863 | -9.09282 | -50.6139 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca1ba5be-564d-3e09-929d-eaf6bd425217 | -10.48045 | -42.48093 | 2026-07-18 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7257f741-9660-3805-8295-82363785dc79 | -12.50547 | -48.25599 | 2026-07-18 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c00ca33-82f5-3de1-8c34-e12301e37a23 | -7.47945 | -46.66537 | 2026-07-18 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46d5ec6a-6a17-3469-aeab-4789b59be82e | -9.9552 | -50.55474 | 2026-07-18 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c9b26d0-89de-336e-911b-052df728a10b | -5.93345 | -43.6398 | 2026-07-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d86e92e6-ae89-3ea1-a76b-9a84d4b8f19f | -11.07692 | -40.21423 | 2026-07-18 04:38:00 | NOAA-20 | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 28af527a-22ce-3e97-bca6-db134c3b13b0 | -6.93107 | -51.93627 | 2026-07-18 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4750f7d6-9b58-3f6d-8bd1-b47375df4703 | -7.85199 | -48.39193 | 2026-07-18 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ef1edcf-ea51-3719-99c3-e4798dcfb0e8 | -12.80083 | -46.56309 | 2026-07-18 04:38:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c0d3a14-bf27-3963-bd62-afb6f2911751 | -9.52466 | -47.11872 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e6a2359-7c31-3ccc-a3a8-d939d612645c | -5.89622 | -46.20486 | 2026-07-18 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e32a69c3-aadf-3bb5-89aa-9abaee689912 | -11.79586 | -45.94471 | 2026-07-18 04:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46796a7d-4ead-3a75-bf00-3fc315a65e92 | -7.85474 | -48.39592 | 2026-07-18 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86f63c60-4594-39cd-9804-3d121ababee3 | -6.91839 | -51.94346 | 2026-07-18 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f4bbca7-56b2-3634-88d7-57eac8891284 | -8.9397 | -47.60958 | 2026-07-18 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 743ba9d0-90c2-3e39-a08a-161be6a0ef88 | -8.12498 | -46.45052 | 2026-07-18 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dec8979f-3079-3b87-b80c-1902d3c9c538 | -9.69912 | -47.69952 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c32a9dfd-1c41-3ad3-b098-3528a03a0ae1 | -9.16361 | -50.8901 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50868135-48b9-399a-9be9-fc2e2f4fe265 | -11.55113 | -48.25977 | 2026-07-18 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4cc2899-4dfe-37d4-b334-91af423067cf | -11.07761 | -40.21474 | 2026-07-18 04:38:00 | NOAA-20 | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f4377dcb-8452-3d0c-9bb8-13270a7aa973 | -5.89565 | -46.20854 | 2026-07-18 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfad2b3d-4080-38dc-b092-6b5016ed11b9 | -5.59722 | -45.33841 | 2026-07-18 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6e5377c-4ce4-3b12-8c01-1da22b8bd194 | -8.1238 | -47.87318 | 2026-07-18 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4db6fc32-e619-3e5f-88ea-b1c8cc4e6b3f | -8.71562 | -49.60286 | 2026-07-18 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8452932a-61e9-36f4-a76c-113af57cc8ff | -10.80526 | -46.54974 | 2026-07-18 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 875a1c95-43eb-3a53-9c83-94ad1e3fc965 | -9.09625 | -50.61448 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0162cd6c-7219-310c-93ce-bc6de6f90574 | -6.73853 | -47.13218 | 2026-07-18 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e5703ef-6a53-3c49-94a0-4e2eabca2f58 | -11.65685 | -49.76355 | 2026-07-18 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18b099c9-d7ac-377d-992c-75fac89146f3 | -9.16078 | -50.88561 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2032d399-7a56-3d8c-819f-fa5c6f70ab05 | -9.479 | -57.32545 | 2026-07-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 845bc4d6-eeaa-3225-ba80-1c0521c8f653 | -5.35611 | -49.16322 | 2026-07-18 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 208c3d87-4744-369e-98bc-7f6b2cd1fdbe | -5.5287 | -45.27211 | 2026-07-18 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 891c8be7-52c8-3d9d-b6c3-799775ff0822 | -6.85431 | -47.82518 | 2026-07-18 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 755e7ba5-e90a-3217-ba02-f84851a68325 | -11.79351 | -45.93566 | 2026-07-18 04:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 108a0b0c-16ce-3d5d-992d-e7b4be1730d4 | -8.71228 | -49.60231 | 2026-07-18 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df48602e-1279-3f71-a854-d54b6a1e0344 | -8.72798 | -47.83215 | 2026-07-18 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 29d014e3-9771-346d-a615-046f72fb2b16 | -11.7965 | -45.94046 | 2026-07-18 04:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 368731a8-95c9-3856-aba2-bde599a823ff | -12.22379 | -44.00546 | 2026-07-18 04:38:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aac1b7c5-ee20-3578-99f2-053892e321ff | -6.11023 | -46.18151 | 2026-07-18 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a342eabe-ad7f-3633-81e7-94349c69b82e | -8.36493 | -46.80394 | 2026-07-18 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5217e282-5817-38a6-b823-d31ed7380c55 | -10.53141 | -48.15704 | 2026-07-18 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b5d3433c-cd16-3f58-96fc-398e90107e04 | -9.08193 | -50.61596 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a118d8f-0310-308b-a7df-dc7117e6962e | -10.47662 | -42.47591 | 2026-07-18 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eeb0bb7d-bd68-3658-a327-e8e852a98053 | -9.48922 | -46.66585 | 2026-07-18 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 506bfb88-5f2f-34c8-a651-f916ac5c5083 | -11.40919 | -47.52751 | 2026-07-18 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d1a6f45c-4ed2-36db-a8ce-1225d0a9d24e | -9.53143 | -47.11978 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7745580-705c-3367-adca-9364d9671720 | -8.94248 | -47.61364 | 2026-07-18 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b87c3ed7-5589-3af8-ba00-1941d7131fb7 | -9.68427 | -56.1017 | 2026-07-18 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2537a4f-e9ea-3249-9b4b-ef57d9e8f051 | -5.74499 | -43.26909 | 2026-07-18 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52a32c17-751d-3196-998c-a5b6829f1a62 | -9.49037 | -46.65832 | 2026-07-18 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 974f4514-f07c-3284-9759-079da7f74d45 | -10.84779 | -44.98558 | 2026-07-18 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8480685e-4e30-3e90-99e6-98fc44b1e98b | -10.64917 | -47.23347 | 2026-07-18 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c993b766-6a38-391a-8f8b-7ecc80b164bf | -6.67399 | -47.52309 | 2026-07-18 04:38:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 343dd92b-9729-3f2a-8307-6a3a1723bb91 | -6.8408 | -45.5118 | 2026-07-18 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3d239c2-fa52-39fb-a98d-07166b7d1104 | -11.79287 | -45.93992 | 2026-07-18 04:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40146592-fb43-3eb4-9d6b-344628f594e5 | -9.11304 | -47.36327 | 2026-07-18 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfe7248c-8166-34d0-b7e3-74fda49c0b64 | -9.51902 | -47.13285 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 912851ce-b658-3652-9f10-0deff9bc5beb | -11.54724 | -48.2628 | 2026-07-18 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d9386e3-2b2c-3db4-89b3-025b443e3f69 | -9.13894 | -49.8399 | 2026-07-18 04:38:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e861403a-a7ac-34fd-a86d-5340d63e7ee8 | -9.48153 | -57.32528 | 2026-07-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b955c43f-1ffc-3dc5-b8c2-5b272550ef88 | -11.41201 | -47.53173 | 2026-07-18 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc923be8-fb64-3820-9630-83b26291d73b | -5.89904 | -46.20905 | 2026-07-18 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f4d8e50-ded3-366f-9ede-188b1aa98273 | -5.92578 | -43.63865 | 2026-07-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b8b3a42c-2687-30ab-af04-f981a37023a9 | -7.91411 | -48.25622 | 2026-07-18 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fea1ae8e-78c9-3759-9175-2d4d4a0a33f2 | -12.45563 | -46.50777 | 2026-07-18 04:38:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97d009a5-e977-3c56-86fd-8e8fef79e9f2 | -8.7406 | -49.44697 | 2026-07-18 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9920479d-8e80-3cd8-b958-f1a033c1237a | -11.20517 | -49.80546 | 2026-07-18 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef2fbd00-15a4-36c4-a2c0-4a88cee45295 | -8.57856 | -48.52257 | 2026-07-18 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 65b3de54-5d3e-3738-9215-14fad62f5b25 | -9.53199 | -47.11611 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 324d283b-f393-3f88-af51-b273d4f90e7f | -9.48751 | -46.65403 | 2026-07-18 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0005f3da-6ace-3110-99f6-3a0f8b0863e0 | -10.364 | -46.38573 | 2026-07-18 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1745a1d3-56c5-3f79-88a5-3b03e8c049f7 | -5.93129 | -43.65403 | 2026-07-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8861cff2-132f-31d4-aba0-7d42314e4bec | -9.5241 | -47.12239 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf7c02dc-f933-35d7-ba48-87798e5b9247 | -7.91026 | -48.25916 | 2026-07-18 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef3cd964-6bfe-34f7-9e0d-19483af02541 | -6.7424 | -47.12918 | 2026-07-18 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efd054f6-761f-3ab0-91db-5fce7fa68d0f | -8.94621 | -47.60685 | 2026-07-18 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3bfe95b-128f-32e0-a1fb-a4cbcb114a7f | -9.16424 | -50.88622 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22185e4c-9182-3cf2-a4a4-615a072c0607 | -12.95062 | -44.72847 | 2026-07-18 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96453dc6-4b84-3cc1-8434-c6dadd529aa9 | -9.09686 | -50.61073 | 2026-07-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f21007c-7908-3ffb-ae5a-565563dd7e49 | -11.5478 | -48.25924 | 2026-07-18 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8471cf8-e8d3-315b-94e9-f55b2f1b4773 | -11.79681 | -45.9432 | 2026-07-18 04:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cea7eb5-d99b-33e7-a357-887295c223b5 | -9.67563 | -47.89555 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49f39655-e24b-3fee-b8cc-77eee62cd48a | -9.91312 | -53.3186 | 2026-07-18 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ab57882a-9cff-3246-ae84-bc9288824eeb | -11.39225 | -47.52497 | 2026-07-18 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ed44be3-bdea-391f-adbd-86aaf729b8e4 | -10.46384 | -49.14776 | 2026-07-18 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c8a8c52-5e24-3b11-99c1-1c455b52c554 | -11.07649 | -40.21744 | 2026-07-18 04:38:00 | NOAA-20 | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2796a478-52e0-3f9a-b19b-936184a197b5 | -6.67454 | -47.51961 | 2026-07-18 04:38:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 178b5526-26ca-3dd8-b8d4-7d21f2fae8a0 | -8.94511 | -47.61392 | 2026-07-18 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0973acb-0289-3905-8587-609dc3b67a5b | -12.30101 | -50.09153 | 2026-07-18 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5787e912-c1cd-350c-8de7-72172a6ce642 | -9.51114 | -47.13908 | 2026-07-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 840a4241-0581-34c7-8355-85951ec2a19b | -7.91302 | -48.26315 | 2026-07-18 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9266562b-1fc7-34e5-8616-e651ac2c2caa | -10.83805 | -46.47469 | 2026-07-18 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc3b8957-c17d-3e7f-ad24-c58d13182db6 | -10.52863 | -48.15297 | 2026-07-18 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ac3a26a-a592-3749-86e9-e0ecc15c77b2 | -7.28973 | -46.25694 | 2026-07-18 04:38:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fdfdc16b-d8e5-345f-b596-532e3ce0a5d7 | -8.94566 | -47.61038 | 2026-07-18 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5771fc33-c416-371d-acbc-79709ff490dc | -5.52579 | -45.26765 | 2026-07-18 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b68c355-ce7b-3d7d-8fe2-4bcb01c7e079 | -12.01611 | -50.57107 | 2026-07-18 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9f7fb56-7523-3048-b72b-853fe944ae4d | -7.75686 | -45.88302 | 2026-07-18 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
