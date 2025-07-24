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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aec82369-b97e-3acc-95a2-7165da2a4ec4 | -4.05106 | -42.51822 | 2025-07-24 00:07:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 8f9daefb-b497-3ceb-9da8-858509949121 | -3.93594 | -41.48842 | 2025-07-24 00:07:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6165096d-ad24-32e0-9b41-b569ebaf91ad | -8.04485 | -47.66253 | 2025-07-24 00:07:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 4739f1c6-f89c-36a5-9669-53241fd1640f | -4.78803 | -45.33276 | 2025-07-24 00:07:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| da04132b-906a-37d4-9ac0-510fe28b7c99 | -7.23848 | -43.07417 | 2025-07-24 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 21871d4a-223d-3ad7-a4ef-52f55d41dfc8 | -4.0612 | -42.52594 | 2025-07-24 00:07:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| c4b14f4a-c6fd-34e5-83d5-3ff93c92fd9e | -7.24914 | -43.08275 | 2025-07-24 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 9c6fe9b1-083a-3e30-99fe-edb9d63ea520 | -5.55044 | -44.25896 | 2025-07-24 00:07:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7fc0fbbb-685b-37c0-8715-41d72f09f93d | -10.71471 | -48.87831 | 2025-07-24 00:07:00 | TERRA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| a9b1e2ea-ac4e-3372-b9dd-d9d44e10983d | -11.24269 | -46.87068 | 2025-07-24 00:07:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 238.7 |
| c59af56c-7cd7-3d7f-99f3-61383602324b | -5.91079 | -43.45951 | 2025-07-24 00:07:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 56ac2dc6-fcfc-337b-b6c1-7e909111056c | -9.32405 | -44.84298 | 2025-07-24 00:07:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1a018e66-af69-394f-bef7-847e979f5e42 | -7.89244 | -45.541 | 2025-07-24 00:07:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 85ebffb8-8f2c-39fe-a916-7e163b54f147 | -9.47626 | -40.5335 | 2025-07-24 00:07:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| cdf39b39-d448-3329-babf-a735b5036530 | -9.05588 | -45.06434 | 2025-07-24 00:07:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 00e6982f-6235-3677-8a03-73bc613b4c97 | -6.4544 | -43.82782 | 2025-07-24 00:07:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c0349034-5e37-323d-a0d2-d8b30b782e30 | -9.58941 | -46.32661 | 2025-07-24 00:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 533488f1-de0a-33a8-9ae8-ac606144882f | -9.32583 | -44.85646 | 2025-07-24 00:07:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 8fbbf9f4-8e9f-3fdb-b7c3-4f2e7d5c5e8e | -10.96239 | -42.18314 | 2025-07-24 00:07:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| e3ab83ff-8620-3ad3-904b-55deccb57c3c | -7.88269 | -46.9025 | 2025-07-24 00:07:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| a8da3238-8373-3d07-aa47-28154f7d4747 | -4.05874 | -42.50801 | 2025-07-24 00:07:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 1db1a0c9-8ff9-34ce-8ec3-d2d5e6535be2 | -7.83991 | -44.50949 | 2025-07-24 00:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cacebb95-10b8-368d-9c04-76037b16a8be | -7.53223 | -44.48877 | 2025-07-24 00:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 1027e3d1-953e-3225-be0a-fcc272578abd | -8.49846 | -47.23477 | 2025-07-24 00:07:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b3e1503c-a7d7-3db3-b307-42852a83d9e2 | -3.93717 | -41.49725 | 2025-07-24 00:07:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 08566c3b-5515-3171-961e-89f4bc7acf7b | -8.92783 | -47.33688 | 2025-07-24 00:07:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e617d7d1-f34b-3e52-b9c0-c78ba04a2583 | -4.77935 | -45.34672 | 2025-07-24 00:07:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 782d30a5-aa1b-3ef8-85be-6084d12e026a | -11.73957 | -48.18121 | 2025-07-24 00:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 432d0793-b110-318c-a7b3-76be7d42b399 | -8.03164 | -47.66423 | 2025-07-24 00:07:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| db1de76d-7d0a-3b81-90f8-edf28d542377 | -11.24515 | -46.89175 | 2025-07-24 00:07:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 922b79bf-f1d5-3919-8c02-cb25e5829fb0 | -7.2505 | -43.09266 | 2025-07-24 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| b5c6d687-1fb0-3dfe-ad55-589bed39bcd7 | -4.04178 | -42.52539 | 2025-07-24 00:07:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 906e3408-fa52-355d-9f2d-b6ba98f01f91 | -6.57125 | -41.50302 | 2025-07-24 00:07:00 | TERRA_M-M | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 27b5c84a-6c03-38ea-b0a8-a53e1d075dba | -7.26408 | -43.0748 | 2025-07-24 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 218.3 |
| a3dfbf4a-5135-3797-9386-d7002da9fd71 | -5.56727 | -39.26814 | 2025-07-24 00:07:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 9b16a1f1-96c1-3102-bc56-a1e87df8bd64 | -7.15222 | -45.23741 | 2025-07-24 00:07:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2ab665a6-69fb-3509-8216-536a5de2cbbb | -7.46681 | -49.43022 | 2025-07-24 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| d521a928-25f8-30d4-a54e-36906e8b7924 | -11.25825 | -46.89045 | 2025-07-24 00:07:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| c8eaf64f-ad9d-3827-801d-d1f8bf8b237e | -6.4448 | -43.82919 | 2025-07-24 00:07:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 9c5884eb-f396-33a9-a6c0-83b6dadb401f | -7.53384 | -44.50071 | 2025-07-24 00:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 18648e19-8989-3653-a240-b7c546f5da02 | -5.14406 | -45.17223 | 2025-07-24 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 128d5105-2232-3cbb-82a8-19ecd4972596 | -5.56664 | -39.19653 | 2025-07-24 00:07:00 | TERRA_M-M | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dd777fbf-aa81-3cba-b7a0-6ae0cd6f0e8d | -8.48278 | -49.57165 | 2025-07-24 00:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b2c3b65e-a0bf-3c4a-b71a-9984877eaa5e | -4.91647 | -45.31581 | 2025-07-24 00:07:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c47d9ecc-83ea-328a-975f-efda09a7eb32 | -4.51434 | -42.07767 | 2025-07-24 00:07:00 | TERRA_M-M | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 48c5252e-8147-3491-a5e6-246bd1d6fec7 | -10.71148 | -48.84898 | 2025-07-24 00:07:00 | TERRA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| acd27ee9-3453-3e5f-a794-a47dccaa1934 | -5.14061 | -45.16695 | 2025-07-24 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4f432938-944d-3a82-9e83-e5be9e14ee98 | -9.31849 | -44.8516 | 2025-07-24 00:07:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| b5b7a236-991d-38be-b643-9bf21c4fc1ad | -11.77353 | -47.40388 | 2025-07-24 00:07:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 8a3ccfb5-8081-3e3d-95c1-93f50882a893 | -3.35259 | -47.17289 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 31df7c6e-15a1-3531-b518-23cc40ce477a | -3.36212 | -47.15515 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| d8def47c-1eaa-3f00-9e2d-015d102b29e6 | -3.04551 | -47.38278 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 654fef3c-f6ca-34d7-8491-4be10232f4de | -3.6002 | -44.79406 | 2025-07-24 00:09:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8b44dd65-7022-3822-9643-fc505e45f7c2 | -3.04897 | -47.37093 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 69a6d5ed-e769-35fe-868d-ff29812220ec | -3.17174 | -49.43312 | 2025-07-24 00:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 80068660-392c-3af2-bdb0-003ff8ffeeca | -3.36433 | -47.17135 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 16403890-933f-3ada-aac2-8fab91ebe971 | -3.17075 | -49.46367 | 2025-07-24 00:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 269.6 |
| 0b38bbc1-f4cd-3633-967c-c6339b9a77d3 | -3.23316 | -46.79833 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 23190b9c-82ba-33a1-badc-2a10af8c1a58 | -4.30154 | -48.10093 | 2025-07-24 00:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| c7a1dddb-5814-34c7-817b-7fea303a0acd | -3.21974 | -46.78488 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| a5e0f091-3ff0-31b1-b707-f6a748c3d785 | -3.2218 | -46.79988 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 7d98f803-fb99-330e-904a-4c11707ebb10 | -3.17497 | -49.45758 | 2025-07-24 00:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 728.6 |
| 2f2083fa-bf45-31e8-984d-11a176965f25 | -3.17825 | -49.48232 | 2025-07-24 00:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| ef32ed75-ad8d-3414-ba57-7cbaea3fc954 | -3.03943 | -47.38935 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8f38a9ce-f921-3551-a5df-e1b9e6a6f407 | -3.35041 | -47.15678 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 44048a18-ffb3-3184-8d70-11e03a3f1a10 | -3.05738 | -47.38112 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 3d4224fc-aaf4-32f8-b8c8-ccf3c915ad4a | -3.18909 | -49.45572 | 2025-07-24 00:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| dd7acc67-e041-3a77-abd5-d8cc769a6b15 | -3.05131 | -47.38772 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a5e3eac7-9ef5-3dd8-aace-ffd121aba0b7 | -3.23109 | -46.78334 | 2025-07-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| c34a977c-78c8-3bbe-930c-ab88595613ff | -3.16732 | -49.43911 | 2025-07-24 00:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 195.1 |
| 2c9a7184-37da-36db-854e-4c9c15870b67 | -7.4728 | -49.4004 | 2025-07-24 00:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 2db5489b-9fca-3cf1-9e23-48773e04d2a7 | -7.5256 | -44.4795 | 2025-07-24 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 46.7 |
| d5bcfcd3-4dbe-31d4-b37b-07123e201900 | -11.9518 | -58.7574 | 2025-07-24 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 989c6ea5-6a80-320e-9bb7-87529bbb1857 | -3.1833 | -49.4429 | 2025-07-24 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 303.6 |
| 68619367-1b89-3b2a-b83b-5a7708273fdc | -11.257 | -46.8899 | 2025-07-24 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 42453057-537a-3d0b-a4a7-52c92f96accc | -7.2594 | -43.0881 | 2025-07-24 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 327.8 |
| f52f02ce-1fa9-3e5d-8394-d0e8670315a2 | -8.4816 | -49.5534 | 2025-07-24 00:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c7454c9f-88e5-3654-8f2f-ea2a7bd5b22a | -3.1832 | -49.4642 | 2025-07-24 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 282.2 |
| 95d726a9-1a5b-3468-8df7-a472e35e6320 | -3.2321 | -46.7836 | 2025-07-24 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 340b0bcc-3ae8-336f-8d41-99aa2854e20e | -4.0569 | -42.5118 | 2025-07-24 00:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 155.3 |
| c60ba6ff-71ad-397f-a296-061f51124203 | -3.1649 | -49.4435 | 2025-07-24 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 257.4 |
| 76d97fe0-1c37-3a19-b163-03dd8e4bad45 | -7.4541 | -49.4018 | 2025-07-24 00:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 289a1914-08ef-3d2c-9a0c-f6bc618ba764 | -7.2408 | -43.0664 | 2025-07-24 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| 444b2811-259d-3b29-aaf3-9264fdbb5bc4 | -13.698 | -45.6634 | 2025-07-24 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 9e219a94-5c16-3346-80a8-f2e53b292164 | -13.6975 | -45.6865 | 2025-07-24 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2032f512-58a9-3dad-90b5-8e9d22ce2dcd | -7.2597 | -43.0645 | 2025-07-24 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 352.2 |
| beb2ca66-524d-3a36-b418-d57c38ca4adc | -3.1648 | -49.4648 | 2025-07-24 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 257.1 |
| 32990bd8-63c1-31e8-9648-4cceb881ca11 | -11.2383 | -46.8699 | 2025-07-24 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 4281b7ac-5f79-3ba6-852d-ff917825ed53 | -7.2405 | -43.0899 | 2025-07-24 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 120.1 |
| c1052973-0b44-3b03-9448-6aa9fa244fbc | -4.0567 | -42.5354 | 2025-07-24 00:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 0b2e85b0-dc7e-3439-9b22-32225518772d | -4.7842 | -45.3282 | 2025-07-24 00:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 64d900e2-dda5-3e22-a788-5f7dbf26a4a0 | -11.2574 | -46.8674 | 2025-07-24 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 12815532-3f25-3fae-983b-9bbaa10c131d | -13.7169 | -45.6833 | 2025-07-24 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 26813c96-d105-383d-b197-ce8b2732338a | -4.0569 | -42.5118 | 2025-07-24 00:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 170.7 |
| 7b48cead-620e-3d38-b8da-0e6d11a2bf74 | -3.1832 | -49.4642 | 2025-07-24 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 251.5 |
| 5e04a558-32c0-368a-b073-eb0e3e838adf | -4.7842 | -45.3282 | 2025-07-24 00:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| be9fd1ae-05be-3833-955b-73213e51d6ce | -3.1833 | -49.4429 | 2025-07-24 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 311.7 |
| ce4876a5-9dad-3cab-a23a-02b816b5d711 | -4.0567 | -42.5354 | 2025-07-24 00:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| e3637c18-d6c1-3362-abdf-35190b05c808 | -7.2594 | -43.0881 | 2025-07-24 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 289.5 |
| 58e33008-cffc-3c02-a19f-dc5240a532ce | -11.2574 | -46.8674 | 2025-07-24 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |


[Clique aqui para ver as próximas entradas](README3.md)
