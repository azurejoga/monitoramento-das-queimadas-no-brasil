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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17c7d4a0-1896-33c9-99b5-e1a5c0d0a06b | -7.3958 | -39.6595 | 2025-08-28 03:40:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 54.6 |
| bac1811a-e220-3961-9a34-cab1d91c5a88 | -6.8774 | -43.5919 | 2025-08-28 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| f22daea5-d8f1-38a6-becb-08e011ee5979 | -9.1154 | -65.7886 | 2025-08-28 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 288.0 |
| 6fd660b3-cd75-3bf5-a905-33ebc03b1581 | -10.4736 | -57.9563 | 2025-08-28 03:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 9af96803-6153-3db3-af89-a7d7ff584247 | -8.433 | -41.4559 | 2025-08-28 03:40:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 140.3 |
| df52210b-ed0c-35a3-8e1c-c0fe001938c2 | -9.1339 | -65.788 | 2025-08-28 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 218.2 |
| e680854b-2726-32d7-a10f-d2e3132f306f | -9.406 | -60.5711 | 2025-08-28 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 26c03801-12e9-3aba-b860-76d19ca056b3 | -6.8772 | -43.6152 | 2025-08-28 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 3eb4801e-a7fd-3d0c-a964-3d1375a79c4f | -8.9479 | -65.9616 | 2025-08-28 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 53478820-bccb-3b8d-89de-374cbbc9e497 | -10.4738 | -57.9366 | 2025-08-28 03:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| f3773c2f-cbdc-38de-9825-0cab5d902664 | -6.07855 | -43.99665 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a531c6b-c01e-344e-ab95-28cded137b6c | -6.22442 | -43.37386 | 2025-08-28 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7fdff07-31d5-3176-b9f9-e8f0b9977292 | -6.88312 | -43.61566 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cf93445a-41a8-3fb5-aee3-326f74977e37 | -6.28186 | -44.47456 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaa0b1a2-d49e-3e3c-8524-945fccc06ba9 | -3.78956 | -45.03953 | 2025-08-28 03:45:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1d53131-e634-3c48-a7a4-be98a3d9374b | -8.44269 | -41.45435 | 2025-08-28 03:45:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 8f815394-9bc7-3c27-b5bb-2ccd35499762 | -6.32703 | -42.87834 | 2025-08-28 03:45:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48301d13-ab4e-3b0e-b724-3760471b7599 | -6.16264 | -47.28279 | 2025-08-28 03:45:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 63ee13f0-78eb-3bf2-b10e-eefe1a711234 | -7.56002 | -42.00779 | 2025-08-28 03:45:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec5442fa-1eb2-3962-afae-ef7c1c232c62 | -7.17546 | -43.84463 | 2025-08-28 03:45:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 523f7d3f-6625-37f5-bb79-a596e540aca0 | -7.54668 | -36.75851 | 2025-08-28 03:45:00 | NPP-375D | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2102378a-7a37-3f94-8aa3-27dacee5563b | -8.44483 | -41.44212 | 2025-08-28 03:45:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f75d21d5-3b57-3d4b-92e5-c01fdd6197ff | -4.79999 | -47.26353 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3b8d82e9-409e-3291-9c37-09fa15cfd39f | -6.87509 | -43.60189 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3b1a3135-66d1-3b1a-88ca-6b1b3cedf968 | -3.78884 | -45.04374 | 2025-08-28 03:45:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebd4eb58-3b7c-35a0-9fe7-49e4df8d422f | -3.23253 | -43.44042 | 2025-08-28 03:45:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2cd9aa05-9c78-3150-8a76-04121f6f0073 | -3.23197 | -43.44371 | 2025-08-28 03:45:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cba4d3bf-6e41-3efe-99f6-aaf64f817a62 | -3.23786 | -43.4414 | 2025-08-28 03:45:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1546726c-a450-39ab-9a07-6a0458fd3cae | -4.79432 | -47.25711 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0218fb47-1ee1-37a4-8cb2-bd943dcc8634 | -6.8611 | -43.62137 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39b1b65e-1bf1-309f-b35b-790d34cad553 | -8.24423 | -45.06805 | 2025-08-28 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c57b1525-e529-39a6-894e-817d248b3993 | -5.64577 | -45.26239 | 2025-08-28 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bfc192c-702f-3aa1-806d-c8681e6b60af | -7.43753 | -42.04052 | 2025-08-28 03:45:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 784ac1e6-43a2-3c29-88c7-89f65774aa3b | -6.43296 | -44.58045 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 21df27fe-1403-3f0e-aee1-48a7f7ce780e | -6.81256 | -44.3493 | 2025-08-28 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f721bd2-99f4-334d-970d-edd21202898d | -6.16783 | -44.07019 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c9a4f1b-3df3-374d-8f61-46cb86d337d3 | -8.47184 | -43.65206 | 2025-08-28 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d6f0543-efe9-3aca-9c06-916e3d4a2bdb | -6.4336 | -44.57684 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 430f4d98-4988-3029-8e75-a0f8129f4a39 | -6.15789 | -44.18868 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d515f65d-c3d7-3ac0-a78f-b0549cdd3ab1 | -7.18326 | -44.87449 | 2025-08-28 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b9964ff-1c98-3596-88da-b9f8bc7eb18e | -9.19489 | -44.43348 | 2025-08-28 03:45:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30d2a4af-046d-3895-935a-0a8898b82647 | -6.13194 | -45.07074 | 2025-08-28 03:45:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 735b1a3e-29c5-3392-8ee3-b7133e88b3f3 | -6.71373 | -43.09138 | 2025-08-28 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0634a285-febf-3e73-9b50-546239b6a28e | -7.67976 | -45.00037 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49f700c5-30ee-3dc2-8248-3ccd3b51d93e | -4.16079 | -43.88152 | 2025-08-28 03:45:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea2db1fc-4312-3729-a8d5-39a4d08da53e | -7.3889 | -39.68863 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 74c25f70-4535-30a9-9c45-e058d9958801 | -7.43522 | -42.054 | 2025-08-28 03:45:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b3c60792-fada-35b9-823b-f625c786c832 | -6.87076 | -43.62607 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 72d495e9-af8c-3b2a-86a1-b771568c1b0f | -6.17744 | -44.1715 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a354862-551f-34de-8585-20093e42157d | -4.66478 | -41.02203 | 2025-08-28 03:45:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ff0ebaae-e3d7-37fe-a55d-d64cfda45e37 | -6.1282 | -44.42028 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 068048fe-3938-365e-a51c-390c68061ba8 | -6.86308 | -43.62417 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c858c293-99f4-3667-bd0f-af6e50303c63 | -9.64987 | -40.5988 | 2025-08-28 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dc58d8b1-4293-38c4-b504-5edf1a726d9f | -6.18993 | -44.16304 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8848c53-ca1e-3562-aaf9-65b3cc412962 | -7.54726 | -36.75491 | 2025-08-28 03:45:00 | NPP-375D | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6e7488ba-c314-3713-9aa0-e9f181bc5901 | -8.44997 | -43.65992 | 2025-08-28 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 170a1a01-f374-3a20-80d9-edd5f2e1dcc8 | -6.30066 | -42.50137 | 2025-08-28 03:45:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0e700b7a-2428-3587-b56b-22e4b7848866 | -7.2398 | -45.43641 | 2025-08-28 03:45:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 041a3f08-e889-33fd-871d-188199025818 | -5.74587 | -40.44336 | 2025-08-28 03:45:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90533de7-6c03-38a5-8ebd-9b2d519d7cb2 | -7.39892 | -39.70035 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 7ec2c67a-bacc-3d74-bb7e-b254658eea2e | -8.4565 | -43.6515 | 2025-08-28 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8989a7a-0fca-3d07-8012-8ce81028e8b1 | -6.86219 | -43.61533 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f163f2f-c192-3706-bd7f-2ee4af9700de | -9.13218 | -40.55725 | 2025-08-28 03:45:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6fbfa93-8110-3287-b74b-b2c3ee57d8aa | -9.18919 | -44.4355 | 2025-08-28 03:45:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30f4b115-0644-36f3-a0b2-7f427b98ecce | -7.39828 | -39.68018 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 23353ec8-2944-3d40-82a0-d608c37e521b | -4.16017 | -43.88512 | 2025-08-28 03:45:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2c26ced-92bd-3313-9d38-0729ef0054ba | -6.36498 | -44.04794 | 2025-08-28 03:45:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdf3a5ae-1421-35b0-9307-6a4c473330e3 | -6.17902 | -44.06879 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f089db45-3f9e-35d5-8659-7e975b4a0d21 | -6.86412 | -43.61811 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23f85f45-7a9e-3a2d-8258-1febfb2ec2da | -7.20074 | -44.06432 | 2025-08-28 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be32de28-68c6-35da-aa18-4c9456397b53 | -6.08286 | -44.00315 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 219d1ece-555c-327b-8a58-61869e54730c | -6.36906 | -44.0556 | 2025-08-28 03:45:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88fb3c0b-0f80-3a0d-9e43-e6e5eae6728e | -5.18489 | -37.01891 | 2025-08-28 03:45:00 | NPP-375D | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 56b5e117-07d2-3b1c-8467-eb4944e0555f | -7.76561 | -44.06512 | 2025-08-28 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| accba138-d613-3a86-9462-3e766ab2c7a6 | -5.68917 | -40.97512 | 2025-08-28 03:45:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2af4a53c-6367-3176-bb4b-c3cec755ca6c | -6.1656 | -44.39847 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c15937b-6bba-31d8-9984-69c107c0842a | -6.24461 | -43.37766 | 2025-08-28 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2ddd9d6-fccb-3a29-9014-3de42a84e720 | -8.45051 | -43.65622 | 2025-08-28 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30994e2a-78d0-34a7-9837-f9e38ce9a257 | -7.42993 | -42.05767 | 2025-08-28 03:45:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a88522e2-34ae-3315-856a-8c24b0de3304 | -6.85851 | -43.62027 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a945114-cd7e-340e-8e6d-c73e07ddc1a5 | -6.28127 | -44.478 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3305df9c-e0e4-30e3-919b-916a1829ea06 | -4.79666 | -47.26366 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fc79716d-e9e4-3afc-ab72-dbd38e9f8ebe | -6.86892 | -43.60706 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55d8e13b-bffb-3cf5-b5c8-59387636c000 | -4.79894 | -47.26926 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 906c054a-3466-3024-877b-c15a32b4d9b8 | -8.43486 | -41.4487 | 2025-08-28 03:45:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 120.4 |
| 10096e94-81e3-32b6-946b-2c5771653408 | -7.06018 | -44.36528 | 2025-08-28 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0513ecc1-2d4b-32e1-b085-d22f38534f79 | -4.7871 | -47.27901 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc238231-0cdb-3c7f-a588-073e1ca2cc35 | -6.16253 | -44.06922 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d62ac6e-3c75-33ce-bb1c-eb8a6e6914d8 | -6.44643 | -44.56794 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3358aff9-953f-3c2e-89e1-aa707f5a4acc | -6.87857 | -43.61179 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7440cc84-6c11-3d08-b798-1d1ca134197d | -8.43559 | -41.44456 | 2025-08-28 03:45:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| eae88c9a-82d3-305f-8c0a-645d9b7b6f43 | -6.16002 | -44.05254 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8aebb31f-9c9b-3704-bba5-47cde417cf7e | -7.13592 | -44.82161 | 2025-08-28 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb4a1325-597f-3a77-910e-ba9029e3c199 | -4.40194 | -40.49825 | 2025-08-28 03:45:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 92fefc18-3b84-3adb-af5b-b92e9c4e3c18 | -6.18017 | -44.06223 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7c15fa7-c881-389f-9115-467574d3c026 | -6.19647 | -44.15705 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61f78364-0bb2-3ce4-a51f-5ea012056a42 | -6.17369 | -44.06797 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db269c36-83c6-32ef-9165-8c7fcdaedc8f | -5.20771 | -44.3224 | 2025-08-28 03:45:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 308fe6e9-1548-3520-8fb6-fb07e1bfc000 | -7.2349 | -45.43094 | 2025-08-28 03:45:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef8e4820-73f4-3361-adab-88e284b654ed | -7.78718 | -43.18263 | 2025-08-28 03:45:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |


[Clique aqui para ver as próximas entradas](README20.md)
