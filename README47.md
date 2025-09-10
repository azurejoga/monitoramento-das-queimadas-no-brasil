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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87f5b720-4311-3a9d-8ab3-6e05afd91695 | -11.45567 | -49.27465 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 960bd1d2-1f1e-3158-82a6-9e2eeafba6c2 | -12.05218 | -43.50313 | 2025-09-10 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 983b391c-4288-39bb-93e8-db0043f4acd3 | -13.79472 | -46.28976 | 2025-09-10 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b5a1ca2-187b-304d-997c-a9a6ec470f8b | -10.57445 | -52.04009 | 2025-09-10 04:17:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aadb84ce-64b7-3836-8cda-f911f97e99b5 | -11.2109 | -54.99337 | 2025-09-10 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 633e42ac-ff4b-3d6e-84e8-da430189571c | -20.10426 | -47.82417 | 2025-09-10 04:17:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f3b83452-43c4-3a91-827b-1a5c2fea0b78 | -13.02727 | -48.01899 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2d371505-d9a1-32ce-852d-0ec31afeee26 | -14.38229 | -47.31526 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 60e20968-a0af-39a0-a777-a5996374755a | -12.93452 | -54.79205 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 401124cf-0715-3a74-8e2b-381d33f69759 | -15.14996 | -44.0237 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf688d98-6a67-3521-a4f0-12735d3219c4 | -16.24476 | -41.87341 | 2025-09-10 04:17:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 27f4f361-db60-3526-aebb-ee0afa926ea8 | -16.65461 | -41.87725 | 2025-09-10 04:17:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 418f8b3f-f33f-317b-80b0-ac9b26370070 | -12.18653 | -53.87169 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9f03da36-e12e-3ecf-af38-320073061390 | -11.63433 | -46.62427 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d598fb7e-afb6-39b4-8e43-1d190bac8591 | -14.3905 | -43.64891 | 2025-09-10 04:17:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2f950c1c-72e3-31b9-89b2-9a28cfb90be9 | -11.14306 | -48.35205 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67cf8daa-3e68-3d32-bc8a-7ca29645bd05 | -16.62277 | -49.76017 | 2025-09-10 04:17:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01550a73-22f4-3865-82ab-b40913f94da4 | -16.57495 | -47.79076 | 2025-09-10 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f53d1c11-4443-3f5e-a554-c74eb79a2908 | -15.13444 | -52.40535 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6348893b-a824-3465-88d7-c36ce502c359 | -10.31036 | -48.80428 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 830d005a-738b-39a8-ba16-2256a1c8fda7 | -10.01608 | -51.69312 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e59854fc-0e96-3e0f-aea9-b906e68eefc4 | -20.52499 | -47.64442 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c4b0785-4d44-3efe-b1f2-29b4701be91e | -11.44709 | -43.61535 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0adc749e-5b98-30f7-90b9-b52fbfb647c0 | -12.82629 | -52.94086 | 2025-09-10 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01e0f339-de16-3b29-a772-f67a2c826294 | -12.96993 | -44.01365 | 2025-09-10 04:17:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f74407da-fab6-3bb0-b841-fa23b9f44f31 | -12.14325 | -44.84721 | 2025-09-10 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aa7e725-a54e-3565-b471-c8b50fcee1e5 | -15.47859 | -49.37433 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d93c90db-f961-3bfe-a2c8-fbbc49a19845 | -15.90631 | -50.18128 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2c90e2c-8519-35c0-83c4-6bd9f831f54f | -15.14885 | -44.03102 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 044551e5-f8d6-3473-b8a7-ffcc1622693d | -12.15392 | -43.70533 | 2025-09-10 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 088a418c-db22-3477-ae66-3b86fc5de844 | -22.06054 | -48.29389 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| debf11c6-47e6-34a1-a13c-aa62431c667f | -15.20492 | -46.24404 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79b1cd08-77de-3557-bc6f-1b806bbc7c5b | -14.25835 | -47.10904 | 2025-09-10 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ba1d7d7-8181-3636-b2d2-ec91241212ac | -17.30524 | -46.75304 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca1738d6-10da-3285-900d-f782b6fc97ab | -12.9919 | -48.02279 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e5b81f8-28dc-3f55-a05c-09b7aaca0a73 | -20.99957 | -47.98998 | 2025-09-10 04:17:00 | NOAA-21 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f77bab95-c8f2-3e2a-955d-fd9449121bf8 | -11.46844 | -49.27152 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04df48c4-ed9c-3123-8d5a-26c4902c92fa | -10.67956 | -47.09782 | 2025-09-10 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a08012f-a235-365c-a13a-23d65437f827 | -14.04182 | -42.14488 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f1e21713-ec9f-3548-8d10-e52a336511f8 | -11.54701 | -47.32081 | 2025-09-10 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b6cabd0-2788-332e-92b0-fd7bbf82b7dc | -13.01928 | -48.01431 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0042a7da-3a23-3b31-95c3-fb5e6d199bed | -11.46152 | -43.6321 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0c9183c5-e311-3ba6-9ae8-01b8defb2378 | -20.10823 | -47.82101 | 2025-09-10 04:17:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b3f128f4-bc17-3645-bbf7-87b16ced6fed | -11.43755 | -43.5887 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dca0ada1-f57b-3075-bac2-3ff914015728 | -14.38664 | -47.33168 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ac2bb4d-42dd-3873-9ba0-0caa047eed60 | -14.56349 | -43.72546 | 2025-09-10 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc23d23e-fdaf-3f39-8401-f17722cab741 | -16.45509 | -51.97386 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8044327-e01e-3268-8538-301358d30d8f | -13.97414 | -48.22217 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ecc0213e-9ef1-38b8-9a8f-a7017f1b21cd | -13.28223 | -51.72563 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d37b2270-c469-3222-8853-ed34a187cfad | -11.44933 | -43.62294 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| dfb9f0ce-d993-343b-a586-eb75a1272a0d | -12.06523 | -51.06512 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c606fc4-d9f0-3eee-a86d-bdc76874042b | -10.18922 | -46.22064 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f423e701-3c7b-3f95-9b70-765bb52f54b8 | -13.00515 | -45.20555 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ebb1172-93ea-3a43-8152-181e01fc6f72 | -12.68921 | -44.96567 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af698102-14ab-3c79-80c5-2f16f189aa25 | -15.90151 | -50.18568 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 897bd65b-8ca8-3d71-a77f-0791cb2caba3 | -11.28079 | -40.9758 | 2025-09-10 04:17:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 95b6a8ea-f60c-3e86-a098-05934767daa8 | -13.75583 | -47.17006 | 2025-09-10 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b85ac228-28a9-38f1-aca5-6606e1e7f09f | -15.03554 | -48.09864 | 2025-09-10 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e6f2133-a778-3823-8073-6fe1e19b6b77 | -20.52804 | -47.62573 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 584999d5-b163-3b88-b536-d6dd54129fb2 | -14.32665 | -47.31361 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81d3689a-0ae4-3f4f-8981-dc1749eb36a2 | -11.49316 | -50.4063 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13e0bb74-1184-3741-841f-01aee7ee40f4 | -14.61716 | -46.36078 | 2025-09-10 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81b7dbd2-75f6-3163-bb6c-d0228cd41b6e | -11.44075 | -49.26669 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d2ab95c-1b42-3530-962e-913e3bc756a6 | -10.30164 | -48.80816 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44b6463a-331e-3570-aec2-7fc246ae476c | -13.02648 | -48.01564 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e83096a-216c-3268-a1c4-cff6dbdeba2a | -13.01208 | -48.01306 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ca1f458-b8b3-3bbb-ad25-2bc53e9bd649 | -12.90761 | -47.98598 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05dd018b-921d-3b6b-ab74-05425cfc12cd | -15.11078 | -50.08866 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cfd73e04-2e29-3a2c-a055-3076d035ac3e | -20.53775 | -47.60828 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bdf5ae2d-5a37-35a2-94d9-9ce340668bcc | -11.27585 | -46.43269 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93e83482-a3e9-3af0-b7c3-6e85ff7aef24 | -14.79616 | -42.72618 | 2025-09-10 04:17:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62d0665b-79ec-3ee9-97c6-736d071b8ac3 | -11.34167 | -46.54473 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10b56d12-a285-3eb1-9014-1362a2d5c62e | -11.11737 | -48.36336 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdff3ee2-1dd5-3503-a5b1-95cfae6b87aa | -17.73461 | -44.48955 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa62d264-3d76-3331-a670-947b63373b48 | -13.89987 | -47.9827 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad7627ab-a365-33cd-8ee6-9dd2538e4cc8 | -13.86934 | -44.46395 | 2025-09-10 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 767b0360-f2a3-340d-9f52-95d6bee385aa | -15.52051 | -52.76876 | 2025-09-10 04:17:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 304948cf-a9f2-3c94-894c-66a97f201460 | -16.62196 | -49.76478 | 2025-09-10 04:17:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9e255798-62de-3451-a9c3-18823db90f51 | -16.39292 | -46.87522 | 2025-09-10 04:17:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1efda5e-cb9f-3f90-81a9-68483ef43366 | -11.11893 | -48.42463 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca5689b8-93ef-3345-84fa-b8e5e5717630 | -16.46996 | -50.66882 | 2025-09-10 04:17:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb7e3688-93da-3b80-8cc9-deb97405774c | -11.43823 | -43.65039 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e674037-5a3f-3038-9921-a96632f75581 | -15.8774 | -52.20093 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8eed64e9-0a7e-3aa8-bff1-5108538c59d7 | -11.66566 | -46.90892 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8311350-7223-37a3-bd5e-c5a3a3e17da4 | -22.05719 | -48.29327 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a50a065-65ce-3913-947e-88878ee537a3 | -10.14469 | -46.17063 | 2025-09-10 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8ec78b7-8029-3eba-8875-8f174e5d4874 | -15.84214 | -52.26691 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e76ba35a-3b6c-3ce8-bc29-7c84004253a7 | -12.18778 | -53.865 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4e48b575-b0bc-30d4-a60a-c49c8dc771c2 | -14.92567 | -50.10886 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a716ff81-6f0f-3746-921f-42ed4d2773aa | -17.30647 | -46.68192 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ec52cd8-6016-3a8d-a9dd-377ccdebade0 | -21.05285 | -41.84127 | 2025-09-10 04:17:00 | NOAA-21 | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c2e41c6a-00ce-39b9-9d61-a2d41605479b | -11.19229 | -48.40445 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6c6f39ee-43bb-3f18-bcda-458576b0c223 | -21.58506 | -43.97297 | 2025-09-10 04:17:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d90902f7-922f-3670-af5e-a5dccedc6aef | -16.46598 | -50.66806 | 2025-09-10 04:17:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c233831e-c4ae-3d67-b825-89eac7b1b9fc | -11.66285 | -46.90427 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cc54829-eefd-3758-973b-6c71bfa6ec17 | -20.99098 | -48.00011 | 2025-09-10 04:17:00 | NOAA-21 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f00a073e-0426-3e52-8c3b-bfb358c2dc96 | -12.2136 | -53.89509 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 719a8966-30a2-3fe4-8625-7e7fbd8c57f6 | -15.48527 | -49.38041 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b0894d3-0fb3-3fc0-b749-d079d33357c2 | -12.82737 | -52.93522 | 2025-09-10 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7ada543-1cf3-3847-a24c-1f0eca5252ce | -11.44236 | -43.69059 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README48.md)
