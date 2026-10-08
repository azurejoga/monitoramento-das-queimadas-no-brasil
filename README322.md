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

## Dados Diários - Página 322

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf65301e-29ee-3ce0-b3d1-9d0eb4a8b702 | -11.76253 | -45.48968 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| adf115b3-fa76-3224-862c-337fde9c9f97 | -11.85083 | -45.28676 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 922ec027-3ccd-38a3-99ee-ffd6384844cc | -6.68881 | -41.7637 | 2026-10-08 16:37:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| adfed08b-a2aa-37d9-8228-4128231a0611 | -7.21946 | -44.28035 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| efa90863-2101-31b3-9aba-7cb9a2a60306 | -10.58906 | -47.3045 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c453e587-03d5-3f8f-9abc-1999baa695b5 | -5.9922 | -40.93537 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| a18b74db-c1ad-3d8f-879f-07b13b5b9cc5 | -13.34912 | -43.96477 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b55cced1-b692-30a5-871d-227b0ed74073 | -10.48053 | -39.32753 | 2026-10-08 16:37:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 35d5d5f9-5d10-3596-aa32-2107af168325 | -8.18263 | -54.72437 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 307397fa-a217-370b-83b1-65c81425504d | -13.76903 | -49.3192 | 2026-10-08 16:37:00 | NOAA-20 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9f86715-5811-34d0-8998-a6d3ff3304df | -6.94431 | -43.06702 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 24a257c5-a9b3-38fd-9677-ab9202560df3 | -9.35933 | -45.94692 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 269.0 |
| dc1e2a8f-dfd4-31f9-8646-c8bda92cc05c | -6.54045 | -45.3959 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 41a7e366-75fe-335d-9de2-461962085a8f | -10.52196 | -57.75906 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7ff5f3ad-2087-351d-b441-be7bd864ef7e | -7.26768 | -39.18752 | 2026-10-08 16:37:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0af07677-ee08-3384-b4e0-80ec7cfc451d | -10.76247 | -51.66307 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9064984f-7839-38e4-b72b-0326107bc5cc | -12.18821 | -44.64811 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a51e4a10-c156-3999-9175-0820b6a48f10 | -9.89682 | -44.79787 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 4d8d0406-9f6a-3ae9-a385-2aa60ea62e0b | -6.31486 | -43.34402 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 419ffe40-913b-3a7f-a755-e3f3a86ba99e | -7.74821 | -43.80953 | 2026-10-08 16:37:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 93057548-73b6-37de-bff6-2bff8fb5d580 | -7.22377 | -39.24378 | 2026-10-08 16:37:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 50975189-3527-32de-9a24-eab8de1081df | -9.12843 | -45.83315 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 2fdaad72-b125-3676-b503-52d6862f92b0 | -5.971 | -40.90989 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 0ac30dd7-1ac8-3cd2-a2a8-9c6789bd581e | -7.63849 | -44.37881 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 82b00d3c-037b-331f-a491-3e25ea18cb79 | -9.44959 | -44.60507 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f695382e-47d2-3952-8f93-1e39a1969de9 | -11.24751 | -45.17753 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3facda25-1f13-3749-92ab-4e34aa0750df | -10.10599 | -39.55273 | 2026-10-08 16:37:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 400ac330-925f-3661-9585-c88139baec7a | -11.77669 | -47.73602 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c4d2df00-5828-30a1-a224-ac318eb1c039 | -9.89218 | -44.85585 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b1afa7c2-43b9-3c82-bf99-37fc049c2bf8 | -6.82378 | -39.55225 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4f07a5e2-74aa-3649-9289-7684e6884557 | -6.37181 | -42.52899 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| e7153f1e-7f55-36b1-a709-04ce408f0aaf | -11.32332 | -46.65761 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5a16025d-ad8f-3be8-a1fe-88038d3f0de8 | -6.93079 | -43.07323 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 1e2cad57-37e7-3478-a629-2b0e34a4514b | -8.61296 | -44.88026 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| df1c9540-f48d-3532-9c69-a5bb487e2950 | -13.17542 | -54.33052 | 2026-10-08 16:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 71ba4462-35e7-3e48-be5e-f7a5869ab907 | -9.87728 | -44.86959 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 7ab19ac2-4a98-30fa-bf0b-7f3f435033e3 | -6.93722 | -43.66565 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 2f756410-8aec-3e4c-9c64-0e394b218961 | -8.96281 | -45.14588 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 13066c1f-acbc-3fbb-82a7-fbea4ae914fc | -9.10298 | -40.31805 | 2026-10-08 16:37:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 23.4 |
| c9295cee-6e04-3c52-a05b-f3b8e3c345e1 | -12.04324 | -47.38117 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e7f3042-deb6-3f92-a768-9bb9038622ab | -11.64277 | -43.70792 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| eed48c63-16c2-3356-acb5-1c3eec15ec87 | -6.65267 | -44.75991 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ae092059-780b-3b9f-9126-9b94a2c5ca97 | -18.25012 | -41.63962 | 2026-10-08 16:37:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| ca232d4c-3769-35d5-a5cb-4b8e2f87d48e | -10.67416 | -47.82294 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8060802b-9cdc-326b-bd7e-69c9e95c1325 | -12.18583 | -44.81048 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a5086f5a-f292-3f88-8bd9-6df68eba0548 | -10.50728 | -47.29245 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 90856d87-aeb5-3c45-9c9a-7507204d0397 | -12.23575 | -44.7378 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 54104593-54e6-3655-8f18-c4628d033b07 | -8.29791 | -45.72563 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 3ee4136d-a26c-3d9d-82d4-22ae3a9f3b34 | -9.08901 | -47.57981 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2c081551-429a-3e37-88e7-a79127b88f7e | -4.98344 | -36.87952 | 2026-10-08 16:37:00 | NOAA-20 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ae5bc01f-efd0-3dfb-9c66-03b0e0564154 | -6.62039 | -44.9213 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e5cc2fa7-5fdc-3a66-a933-f978d9e4e36a | -8.28467 | -45.72765 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 69f936bd-ab8c-3161-9ac8-dc92ce7f2501 | -9.89325 | -44.86284 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 149.3 |
| b178c6b3-5936-3472-a9ec-f02b913cc242 | -6.31776 | -43.33957 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0aa1496e-4342-390e-abf8-6c39d7b7fd24 | -6.79018 | -45.05595 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 64d12fa3-8bc0-34f7-a702-1ebde4c2f7bf | -11.2591 | -41.90696 | 2026-10-08 16:37:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 75964ed2-500e-3c30-b2cb-908aefeb3f6e | -11.22747 | -45.24652 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 2a9ada1a-d7fa-3d77-9f95-bd3666ad7228 | -13.66085 | -49.08947 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4d3c57e7-e0fa-3555-82dc-d8b42e88e741 | -7.31044 | -44.01178 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 766279b7-2d56-3532-8d36-fadbd081a242 | -9.36372 | -45.95344 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 5cd1d4d1-8313-38cb-9725-dc0d467748a7 | -8.78525 | -47.37328 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d8e7c2a2-d709-30f5-b3ea-452653402f2e | -7.57105 | -46.68596 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2ac8a4f3-9f8b-3c0a-84a6-68caead0b2d9 | -12.13573 | -54.39164 | 2026-10-08 16:37:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9941bfff-6921-3e24-a4c6-7b6d844813e0 | -18.75278 | -43.65432 | 2026-10-08 16:37:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c06031c0-dca4-3d14-852c-3459fd3ee508 | -11.63943 | -43.70847 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 38a10f7b-a882-34be-a894-24e034552588 | -6.95264 | -44.41526 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a9909d4f-932c-344b-af0c-796b65cee7e4 | -11.59204 | -43.66821 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 95bf455f-b7a2-3890-b98c-144c961ae0a9 | -6.69151 | -45.29678 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 5de2edb0-bed5-3d6e-9e59-d147833933e6 | -11.79317 | -46.78442 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e1fc548-19b2-340a-b2fc-2bc63abe89d4 | -6.50451 | -42.03481 | 2026-10-08 16:37:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 43b53af5-b434-3b7c-a8f0-1969785acec3 | -11.07191 | -45.76661 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 024d840c-5a33-387e-a323-83fe8c03a178 | -11.07473 | -44.03137 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| c9f579e4-878d-32a3-af78-b21f7eafb220 | -11.22297 | -45.26161 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 597fe532-94c5-3e6b-b59a-b2be002dfd92 | -9.55652 | -45.63615 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e6d49f16-80ed-3217-a81e-be668a79479b | -5.77849 | -42.0553 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 8252af18-2717-3da1-997d-eaf42b84c96f | -5.74366 | -42.05604 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| da7e0ec7-e48e-3950-b916-574be81812a3 | -6.99644 | -44.13299 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91409c92-1f15-3c0b-8351-7c78be2c4598 | -19.0648 | -48.64313 | 2026-10-08 16:37:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 56.1 |
| b5576b83-9aef-3c7a-9f9f-eb1473eb2e95 | -7.74879 | -43.81325 | 2026-10-08 16:37:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| cee5b2b2-ad50-3c9d-b00d-de377c19f7ee | -8.32003 | -50.37871 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c57e678e-a125-3919-86d6-57701d0e3257 | -8.95299 | -45.126 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 396abfe4-041e-322c-b8c8-134edced0706 | -11.09027 | -44.02162 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 876af865-381b-303a-91c3-125bd5829c8a | -12.1587 | -44.72112 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b490a77b-9b6f-3e92-bfa2-51deb3477abc | -5.99071 | -40.92918 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 30.5 |
| 4696b192-0a9f-33f5-8ba1-85b23cbdd6e2 | -9.82682 | -45.76449 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| fab3dbb7-3fa8-310e-8a08-27af6e927796 | -10.33579 | -46.24337 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 459083d7-7413-3845-b483-9182cf4237f7 | -9.36318 | -45.94992 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 269.0 |
| 5b073784-1ed2-3797-b830-75b0a88e68e0 | -7.48841 | -42.8216 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| a43163c9-40f0-3714-ab21-eefb48e643f0 | -5.70724 | -41.73838 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 0c2f3e8a-b00f-3f42-bd94-116592ce3150 | -12.61983 | -47.89407 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 54476293-18a0-3c7c-a9ed-12741a5e73e9 | -8.95897 | -45.14291 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 2542b0c0-8bd5-302b-aec0-5a2be9fac247 | -7.01921 | -44.3231 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82b2e181-9a56-340e-b08d-c6f0f31c3531 | -8.25717 | -54.72911 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0e166941-c91f-3746-bc26-22903f7b14c2 | -19.49923 | -43.68435 | 2026-10-08 16:37:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 344f41c6-8e96-32a1-bd1a-ab6b254b6169 | -5.71934 | -41.64214 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 36508702-4cbe-3f4a-b980-65ca91cd1b6c | -11.21231 | -41.58144 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| e06c7737-87d6-3b2a-b480-9026c4c12c45 | -13.9865 | -46.36684 | 2026-10-08 16:37:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f204f03a-605a-3afa-a7dc-83f68d437c90 | -7.00332 | -43.43998 | 2026-10-08 16:37:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 10a3ae75-3ce2-3008-a2ee-33e9e83947b7 | -7.04173 | -44.33451 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bc108c5d-30a1-3368-8b82-09f6025acd71 | -6.75208 | -41.53717 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |


[Clique aqui para ver as próximas entradas](README323.md)
