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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da54e086-ee53-32b8-8004-be214be2bf10 | -4.88352 | -49.94714 | 2025-10-17 04:49:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4ec69d0-3046-3164-8d12-84848f5757f2 | -2.69105 | -51.84476 | 2025-10-17 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21cfd271-eb13-3b9c-b6d9-a8870f21de3b | -4.58109 | -46.30363 | 2025-10-17 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c10a1262-ffa6-3c60-b82b-62afa2319ba7 | -5.48704 | -45.40355 | 2025-10-17 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 449b56a3-b904-3397-8fbd-dbf82e935894 | -4.60551 | -50.91297 | 2025-10-17 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a7b4a11-bca2-37dd-88cf-806bbaa8d5f1 | -5.86051 | -47.58441 | 2025-10-17 04:49:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| feafa7b4-22a7-3809-955b-9c71c2febf52 | -8.21624 | -43.98136 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9e90df9-42bf-33e6-b0fe-337c342302bf | -3.50774 | -52.48556 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 4c99d5d0-74b2-3f52-9245-32621951bdd5 | -4.43569 | -50.5531 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 493c63fa-2b2b-37dc-95fe-4fd999bfd488 | -4.71486 | -46.44889 | 2025-10-17 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1c8cd14-25e6-3b5d-a009-ff2ed35ea772 | -2.87519 | -50.72941 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57e89dc5-0367-301c-ab7b-bbb4f355885b | -3.47106 | -51.66384 | 2025-10-17 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63087f11-61bf-34ad-873a-9c8be7857a68 | -6.13989 | -41.73039 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4e1d0179-af3a-3e05-a0e6-93e525e5b79c | -5.64401 | -46.58836 | 2025-10-17 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e45e093e-9157-3a7e-a38f-ec0bd41a1bd8 | -8.19852 | -43.96818 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10a7e37f-a0eb-34ce-8859-431664b475f1 | -5.88539 | -43.90427 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7369fdf5-3e25-3e94-8cbf-451bdf502c56 | -5.71262 | -44.51974 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d815465e-c175-38c6-b771-ec1710fb748c | -5.51959 | -43.30878 | 2025-10-17 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6c7ac94-a7ad-34db-bfff-96c12cc9ea00 | -3.51145 | -50.21679 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b96c96db-b859-344d-9516-a6278853a8b8 | -2.59831 | -51.34877 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cef3429-285e-3d57-a935-4500ae689502 | -4.39484 | -43.41083 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8d6f9f3-8f27-3cc5-a8cf-e83f3ba0ea50 | -3.97368 | -42.4877 | 2025-10-17 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 58323838-2e34-3402-92ed-86565fd360ea | -7.52604 | -46.84056 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 801a1fee-a306-388b-b286-6833ab5e1474 | -5.85567 | -43.87978 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b41f53b3-047e-3667-8abe-683749b7dd32 | -3.76334 | -48.92512 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9c11fd0-b25e-3168-b2ff-dac461901739 | -7.28047 | -42.31146 | 2025-10-17 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e3b85eb1-a525-3a42-810b-05f0dff1f069 | -2.70904 | -49.8569 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 163fc45f-362e-321e-a366-40c678b0d753 | -5.29267 | -47.93169 | 2025-10-17 04:49:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4cc65524-9bfb-3f84-93ec-cbacec2bb2b4 | -5.2454 | -50.9539 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94b1fb20-fc00-362d-8dec-227dbd0fc155 | -7.46028 | -42.66408 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5db56c56-9e4f-3c09-b25d-cfb003a450b5 | -6.58485 | -47.07433 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6744fa8f-7b97-37d6-b66c-b45b7ca5a3be | -7.62283 | -47.8341 | 2025-10-17 04:49:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ccf614d-574f-31aa-9c15-7cb337a6ce2f | -7.11746 | -44.73519 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08489d26-f18f-31a5-90bb-588637a8d10c | -8.22697 | -44.00931 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d6b5058-6c60-32fc-8a7c-ece45c56b839 | -3.10505 | -47.5123 | 2025-10-17 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e714a615-2461-3a27-9595-ab65a1c54927 | -5.28255 | -47.92598 | 2025-10-17 04:49:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e378443-0213-365b-89d5-435713dec2bd | -2.98065 | -49.22331 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 145643fe-ce1f-3cb0-9ee9-476196edc730 | -6.74301 | -42.52696 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e0642446-9b44-381f-8f09-dd5788828927 | -7.10786 | -44.73839 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3673eb53-77ef-3b40-a656-cd13c51bce99 | -6.40387 | -41.48398 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e43f33d-8fbb-3c88-a815-2bb841abc076 | -7.60382 | -46.87875 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75fb27aa-6ab2-399e-a633-ca78110ed458 | -5.87728 | -44.83811 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0bc8df41-ee7d-343c-b66c-67c44aa91e8e | -7.11933 | -44.72207 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1d0a534-ec18-3f1b-ae28-e9f0aa73e020 | -2.51643 | -51.9336 | 2025-10-17 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 864a9872-2d6c-3bac-83a5-89a2731b2e2a | -6.95654 | -47.72019 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc2c3001-1b88-325f-9e1a-152f14faa763 | -3.15899 | -49.74971 | 2025-10-17 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 542db97c-7aae-336f-9ac6-eab1df4b4a38 | -7.18015 | -42.18621 | 2025-10-17 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 205677cc-9c86-34a0-a90f-923a3771a3eb | -5.32951 | -44.8438 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6f4bea1-8b26-350e-9061-9171052f4ada | -3.62396 | -42.77127 | 2025-10-17 04:49:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77f241b6-369e-3bd5-bc39-59c9b2527823 | -5.90519 | -44.73798 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7731a778-dd7b-3172-865c-9b1c14e6e26c | -4.42281 | -47.75481 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6608dc8d-2f55-3778-b751-5de1d53c6f56 | -7.12382 | -44.72268 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2c80687-a20e-3240-951c-a4785574ae86 | -6.75333 | -42.38062 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 14dd730e-4284-38e9-8df8-6ca0f7b9628d | -5.56912 | -47.61441 | 2025-10-17 04:49:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85910582-f834-39c8-8044-960a5ade19da | -4.22019 | -48.36747 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03d440b6-0879-3080-81ce-8cb5b3b75c2c | -6.31979 | -40.94559 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4f9e4be2-3f41-3116-b553-5a2c06cfd7c9 | -6.98894 | -39.22667 | 2025-10-17 04:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1724d093-8b45-3769-8284-11e9ab166e83 | -5.29379 | -43.55393 | 2025-10-17 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c8667735-dc49-3d6f-aebe-e1affecdfb89 | -2.74764 | -48.30581 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ccb0454-f123-39f6-a9b9-8ce71913e48c | -4.67301 | -49.33706 | 2025-10-17 04:49:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14396121-7aff-3972-b421-ae165a62f680 | -6.22777 | -47.03759 | 2025-10-17 04:49:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6aaa9725-8c65-3cb3-932c-8f268b0c02d1 | -5.8345 | -42.23819 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 374436bb-f90a-3bef-9fbf-6e697906d8b3 | -6.5884 | -43.93652 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34208b16-255a-370d-af7b-ea9d6a5bef2e | -7.17528 | -42.18208 | 2025-10-17 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c1cfbf96-d3e9-382e-b072-a097445deb54 | -5.83363 | -42.24444 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7ac776a5-fb7b-3eee-944e-f31cc824656e | -8.20286 | -43.31396 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 3d0adfb8-ca77-3a48-a17a-544456c3cb38 | -6.78618 | -47.0387 | 2025-10-17 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59e71356-7939-3fea-8576-7ae365ee0fdc | -6.20073 | -52.73771 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7b6bb49-14e6-3946-8fda-74be03091827 | -7.0441 | -42.73577 | 2025-10-17 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 503388e6-418d-39bb-9af7-48fb26611966 | -6.31906 | -40.93949 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2b42e20-f7f7-3331-8446-96816fdbeb1c | -6.26214 | -43.90211 | 2025-10-17 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 303eaab6-eae8-3df2-bbde-572c2ae81806 | -3.23516 | -42.07301 | 2025-10-17 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b566cd65-92c6-300f-9dcc-c3b00c1c2a81 | -7.21954 | -43.80643 | 2025-10-17 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0c3e4d7-f8f1-341b-bbad-254fac44ba76 | -7.04553 | -46.37983 | 2025-10-17 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e235ea56-1b4e-31fc-b750-240707f1b02e | -3.35244 | -49.25135 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84f25c10-e29f-3e44-a742-342c9a7675de | -7.52996 | -46.84109 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a7ff859-490e-3ca0-acbf-230915fca1fe | -7.95224 | -44.13188 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ada1c77-dff6-38be-9409-e6cc62043067 | -6.58366 | -43.93618 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 004d8aea-92f5-3931-a384-c5c442a1eaf5 | -2.70795 | -49.86382 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69c8e6ed-23f3-3602-b9d7-ec91cdfcf6f0 | -3.8854 | -52.28093 | 2025-10-17 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc7aa2ce-7e2f-3dae-95ca-78fba373db32 | -6.37413 | -44.71263 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17af8de5-2e55-3c3a-b046-708bbf40e1ad | -5.25409 | -44.20357 | 2025-10-17 04:49:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6de4c35-8082-32c3-b05d-49216a4879a1 | -5.55113 | -45.20063 | 2025-10-17 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a9e96bc-627d-3036-8ef8-714746d53647 | -6.15253 | -40.91392 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 77bcf832-7c20-3514-845d-7f4036359fbf | -8.25944 | -43.34074 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b347c16a-3e82-37ee-8687-543be2cff277 | -4.4166 | -43.39368 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e37722b9-35a2-3ac8-b70e-fc25b4f3d86b | -4.24752 | -48.56786 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f88004ef-7c7b-38fc-ae0e-a0522b727417 | -4.25904 | -48.56193 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 035c5f35-46c7-358e-8524-d278ee0ae17c | -5.91365 | -46.51928 | 2025-10-17 04:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0389b8b-e4cf-3dab-9fc4-6a5d9d24dadb | -4.9237 | -46.7261 | 2025-10-17 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 213582db-fee5-3d58-904f-4e839875f9d0 | -2.8813 | -50.73391 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0d79185-57f6-3f26-afc5-49967f01b5e3 | -5.6924 | -42.67807 | 2025-10-17 04:49:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bfae81b9-375b-3d94-82b3-d6f73d5e8f31 | -5.89839 | -44.75417 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fd3fb56-3114-3ccd-a690-af6d458c8c39 | -7.17227 | -46.93292 | 2025-10-17 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7a3aa40-f3b2-3e45-8b83-8eea8d33f246 | -7.18197 | -41.68492 | 2025-10-17 04:49:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d894c7ef-b3d9-31e2-9d26-a6c17956723d | -3.78118 | -49.42997 | 2025-10-17 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 071ee075-13db-33e6-b8fb-6ac5c420f1e9 | -2.95738 | -52.50209 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b65aef29-c08e-3fa2-8e1f-100c0c7951ec | -3.16658 | -51.81863 | 2025-10-17 04:49:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d67726b0-8d03-3dd4-9ca5-4b0071cbce02 | -7.66529 | -42.57052 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d6e80a9-db9e-3c42-9e2f-fedfc5b499cf | -6.7586 | -42.3811 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README80.md)
