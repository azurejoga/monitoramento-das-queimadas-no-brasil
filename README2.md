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
| 0b1c0cf8-7a05-31bb-bed5-8f988a3cdd09 | -5.32609 | -44.69352 | 2026-05-29 03:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc88ddea-b7e6-3600-8446-034a468f44a7 | -6.99685 | -43.866 | 2026-05-29 03:32:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feebe0e7-d1cf-3f65-9648-ad3b289767c8 | -7.0031 | -43.86724 | 2026-05-29 03:32:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49be34de-1387-3fa6-bc59-a5c6345cb11c | -6.75947 | -45.0263 | 2026-05-29 03:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d5c07d7-03f2-3485-89f6-f877b47e752c | -6.39366 | -44.1684 | 2026-05-29 03:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1bb6b2c0-5376-32ab-bf43-121cff1bc827 | -6.6403 | -43.91695 | 2026-05-29 03:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc528e5e-5b88-3be2-a82d-a16a17ced3f6 | -5.3193 | -44.69249 | 2026-05-29 03:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 918683f3-ac86-32a5-ab1c-6fc3f554ac8a | -6.99594 | -43.87103 | 2026-05-29 03:32:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31a10e47-7608-33ef-9152-1665f5d6ea16 | -6.38693 | -44.17096 | 2026-05-29 03:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92f0f3d7-f90c-39ed-9db8-78b7713dd9ff | -6.39338 | -44.1721 | 2026-05-29 03:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8b0ac1a7-d37b-31e7-aa06-3b815b51d841 | -6.08245 | -44.00396 | 2026-05-29 03:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 22323e94-03dc-3037-9015-10a148d68b3e | -5.95368 | -43.49488 | 2026-05-29 03:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c90860ae-d98e-3e98-badc-6e7a6e258fe8 | -7.00029 | -43.86731 | 2026-05-29 03:32:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c7157b4-4cd4-32fc-925f-6a0bac721d0b | -6.39269 | -44.17375 | 2026-05-29 03:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0fc70f22-6c12-3e57-9d94-7ba61e42d622 | -5.94835 | -43.48878 | 2026-05-29 03:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 348bc7b6-a8cf-304e-8202-7c8b7915cafa | -5.93332 | -43.46526 | 2026-05-29 03:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e6f86f4-94ac-3181-be36-2b7264d6cba3 | -6.75699 | -45.02663 | 2026-05-29 03:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e89c2cdd-14aa-329b-b8ae-bbbcc7dfdd36 | -5.93949 | -43.46666 | 2026-05-29 03:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 144b4708-dc32-38e4-b873-6178b86aa4d4 | -6.99404 | -43.86612 | 2026-05-29 03:32:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff3d63a8-7f65-3ee1-bf1a-22e822c1d118 | -6.64245 | -43.91893 | 2026-05-29 03:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bff7517d-0092-3956-955f-cc7b0d51a91b | -6.76061 | -45.02037 | 2026-05-29 03:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a9dce14-eab6-3802-b1a2-12da094e0fac | -6.03663 | -44.0009 | 2026-05-29 03:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc49d981-fe14-3427-a4f1-8d27f018424e | -6.63937 | -43.92206 | 2026-05-29 03:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b84dd63a-0d4a-3614-99da-5cabe4c11968 | -6.7638 | -45.02752 | 2026-05-29 03:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 226f0939-6a61-3eb2-b4d4-edfa98182098 | -10.81837 | -46.89563 | 2026-05-29 03:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa10f158-0a86-3379-a823-99d0f56ac119 | -9.23509 | -40.55912 | 2026-05-29 03:34:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 983b40e8-76ae-3588-bb66-c9e3c15b5488 | -11.94565 | -43.40681 | 2026-05-29 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f710833-acdb-334a-ac5c-33bf633fa04e | -12.00024 | -45.14419 | 2026-05-29 03:34:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0288374-890a-39e2-afc7-43a08489b553 | -12.00818 | -45.35823 | 2026-05-29 03:34:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7db2da2b-402a-3954-ade6-6a2bb65c6edc | -10.82539 | -46.89703 | 2026-05-29 03:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b199dcb-b071-3454-84ef-153a536e4fb9 | -9.16899 | -40.91817 | 2026-05-29 03:34:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 83152b9b-5ed0-369e-847b-41fcd1a9aa97 | -9.34378 | -40.20652 | 2026-05-29 03:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b888bd12-25e8-3cf6-9d88-f3df994b48cf | -9.16953 | -40.91526 | 2026-05-29 03:34:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 28dd4aba-00be-3404-9481-e13623a4a863 | -11.594 | -47.44385 | 2026-05-29 03:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 27f159ae-eb51-3873-9381-1c1ae3cf6389 | -14.41821 | -44.58733 | 2026-05-29 03:34:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2ada435-df73-386c-ab5a-4a8fdbb5ec04 | -10.97816 | -45.0951 | 2026-05-29 03:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 025ef268-e189-3a79-a9b4-91b203e2161c | -11.94368 | -43.39958 | 2026-05-29 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cdef370-bf89-38cc-91b6-5a31e74594b6 | -11.94004 | -43.40574 | 2026-05-29 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f6ef242-9e27-351b-bb02-dec13c4cc64d | -10.8229 | -46.89587 | 2026-05-29 03:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 585714c4-49b4-3167-8a9d-decfa1dd658c | -9.74346 | -37.16744 | 2026-05-29 03:34:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e7c143ee-a3a1-3201-b426-cb9f4355fde9 | -11.59549 | -47.43681 | 2026-05-29 03:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3e7d1890-14e4-3822-8e81-62c9be20e5f6 | -10.98448 | -45.0963 | 2026-05-29 03:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36d0eafa-618d-3882-a79b-5d4c9d4b62b1 | -11.94295 | -43.40342 | 2026-05-29 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37bc8b54-0241-3ec9-a406-aadaa4469547 | -11.5925 | -47.45092 | 2026-05-29 03:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 348d5ad9-7d51-359f-a7bb-1083f38037e0 | -11.58689 | -47.44226 | 2026-05-29 03:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 93e98977-443b-3246-86ef-d758ff28670a | -9.34853 | -40.20739 | 2026-05-29 03:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 678e4b9c-343a-3713-a539-8f47cd110f4d | -12.0019 | -45.35687 | 2026-05-29 03:34:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2727c5f6-6888-365f-a66e-befe1fd5fea8 | -11.94157 | -43.39809 | 2026-05-29 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f2a6b33-eaa3-3416-a8c5-2280113952fc | -11.94081 | -43.40191 | 2026-05-29 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b8d9fcb-cc9d-3e9d-8536-d0adc1f60f1a | -11.94221 | -43.40725 | 2026-05-29 03:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f050ca30-ddd9-32e3-93ec-30e675533a5a | -9.23995 | -40.56005 | 2026-05-29 03:34:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c0f02844-75f3-323c-8750-6a0c61705fbe | -11.60106 | -47.44571 | 2026-05-29 03:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 31cd5958-0aba-35a2-9ac8-f4ce4e8f2dc5 | -12.70133 | -44.79197 | 2026-05-29 03:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17b6a058-527c-354c-ba48-3d3768501bb9 | -11.5854 | -47.44928 | 2026-05-29 03:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cf43c02e-3c19-307d-b01e-9a4b956031f4 | -11.99617 | -45.14438 | 2026-05-29 03:34:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8314af46-dfe7-353e-a556-d1eb9e1ddcab | -14.41247 | -44.586 | 2026-05-29 03:34:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aea4ff4f-b32e-3b59-95f5-342720c54b82 | -12.00237 | -45.14575 | 2026-05-29 03:34:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0650915-3cb9-3a86-80c3-b37fce0e8138 | -17.7017 | -42.27293 | 2026-05-29 03:36:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e8e3033-cd9b-3618-bbab-afe81d69f5d8 | -19.17175 | -47.35635 | 2026-05-29 03:36:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 907d6d18-a115-30af-913e-ed1a8c8bdcd7 | -23.20687 | -49.41014 | 2026-05-29 03:38:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1fbdc32d-6ba5-3a4f-ae97-938f0df92b0f | -21.39547 | -48.70989 | 2026-05-29 03:38:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d73c5a18-ace0-3ec1-8c6a-a470d42cabb5 | -21.39408 | -48.71554 | 2026-05-29 03:38:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 584726ed-102e-3ac0-8356-ba52eb52a89b | -11.591 | -47.4496 | 2026-05-29 03:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 7398a390-c088-38e0-8c35-41f1693085b6 | -11.5914 | -47.4273 | 2026-05-29 03:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 359f5667-dd33-31ab-bfa7-697178301c99 | -11.591 | -47.4496 | 2026-05-29 03:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e6af359a-781d-354b-8e3b-99e7413e84d6 | -11.591 | -47.4496 | 2026-05-29 04:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 551b7e50-6273-3f7a-9089-ef83db1887fa | -11.591 | -47.4496 | 2026-05-29 04:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| bd681298-b2a8-3a52-b0a5-f38d3b0c8937 | -8.11403 | -44.16047 | 2026-05-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7982991e-4704-3af2-a6e7-c0d70cbb2b19 | -8.11627 | -44.168 | 2026-05-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1efe7dbe-afe9-3469-ad78-2dbb6fc2fcf8 | -6.24556 | -48.57529 | 2026-05-29 04:19:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1788e1ac-f843-3be0-90c8-f53b5d8e2eb2 | -6.25012 | -48.57103 | 2026-05-29 04:19:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f1c231a-fdbb-3782-ab17-5c50408f807e | -5.79067 | -45.12003 | 2026-05-29 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ed1aeeb-add4-3a9a-89fd-c3ff5e07542a | -8.11681 | -44.16449 | 2026-05-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73af7854-c474-32c5-b3e7-c52144517eee | -7.00333 | -45.00406 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 05e8e462-6318-344f-b2ba-3ecebe0630b8 | -7.00993 | -45.0051 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77b64303-0584-3b34-afa7-4aa76632d201 | -6.39456 | -44.17265 | 2026-05-29 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3868416e-1486-3548-80a4-b71aae308de7 | -8.11349 | -44.16398 | 2026-05-29 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2faea4db-dd33-3fd6-b31b-b926d3834b80 | -6.08072 | -44.00308 | 2026-05-29 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c527a7c-a03e-3f84-8617-cc15c462e6e4 | -6.05214 | -44.01284 | 2026-05-29 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7288801-7fad-3a18-bc7b-9d4430d20554 | -7.35296 | -46.21495 | 2026-05-29 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 38126fb7-202c-30c8-8c6a-6ae3424bca84 | -5.95579 | -43.49102 | 2026-05-29 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf52c0ba-7214-3927-880e-c5ea06ebfaea | -5.94968 | -43.48648 | 2026-05-29 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b94b1404-a336-35f6-b6ee-287bc6c6845d | -6.76294 | -45.0188 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bf25b70-2550-3916-9c31-dec4c7cdcf46 | -7.33865 | -49.86401 | 2026-05-29 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67169e08-96ec-3193-8052-a512bfd0a341 | -7.00278 | -45.00752 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61506f5a-83d3-3d4c-a50b-fac29a176a03 | -6.76516 | -45.02622 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bf40f5a-9490-3e71-85d4-7cc12f4098ba | -6.08403 | -44.00359 | 2026-05-29 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a3ecf0c-09b0-3aa1-9d45-045e2b5306b8 | -5.92358 | -43.47889 | 2026-05-29 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acec793c-d519-39ea-ba28-23b09979f5a2 | -7.33923 | -49.8605 | 2026-05-29 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4dc1e1e-b88d-3913-9f74-25b0579a92c0 | -7.56532 | -42.64478 | 2026-05-29 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cb337eb3-9e03-3919-b1a2-ba19145683f4 | -7.60861 | -43.15015 | 2026-05-29 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2f54a4e1-efdb-3976-8732-f3774a62c2da | -4.47807 | -37.80919 | 2026-05-29 04:19:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 79d1e63c-fa91-3ded-8b42-978d316e4aa1 | -7.55729 | -42.65135 | 2026-05-29 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3f2c903b-f49b-305f-9edc-6e14ee75bb22 | -6.99727 | -44.99957 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9979c507-7250-36d9-8772-668199d8edbf | -3.86075 | -42.96307 | 2026-05-29 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| baf476c2-f972-3383-89eb-4610cf9cc638 | -7.69489 | -46.14104 | 2026-05-29 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69244f83-78a0-3daf-9c06-a2b745d5b739 | -7.33521 | -49.85985 | 2026-05-29 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f3d7706-50aa-3882-9ec1-b60c0b35bb4a | -2.96518 | -39.9245 | 2026-05-29 04:19:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 526045de-7b4d-35d1-9076-a657a877e48d | -7.00387 | -45.00061 | 2026-05-29 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0db01ee2-9a20-305f-9704-0cfe8e624cba | -6.24475 | -48.58025 | 2026-05-29 04:19:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README3.md)
