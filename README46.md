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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ccb86b2-724b-3f59-a305-c2ec3c968cc6 | -5.87151 | -43.88912 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24f00a80-d134-3ba2-be79-ce0d6c304cff | -4.91925 | -48.17027 | 2025-10-16 04:38:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1282ebac-dbb6-341c-be3a-b6720d4a54e6 | -6.14869 | -41.78618 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8101ffa7-0876-30a2-981d-8598d7482e77 | -5.57289 | -41.3285 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b2929e3a-12a2-3559-ac3f-5f6b4db3c0a2 | -7.94022 | -44.12971 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2bfc9bf5-b4fb-32df-8a5a-95ca69873148 | -7.07643 | -45.44849 | 2025-10-16 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f42d526-fc4d-31bf-9c7e-e8aa8924b06f | -6.71142 | -44.38174 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d499f82-0ade-399b-8aca-e8de61be18a9 | -7.8517 | -45.40872 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 998ad1a1-cd0c-3661-aaaa-649c744a0e0b | -7.94712 | -43.26891 | 2025-10-16 04:38:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 395a6c6e-840a-3bb1-a62d-4283181aa499 | -7.04445 | -42.73652 | 2025-10-16 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e6ef63b9-c5c7-38a9-9d40-847cb2f4a1fc | -3.07207 | -49.38327 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f4eb584-353e-3bbd-ac81-e439ea9c518e | -4.83284 | -41.4717 | 2025-10-16 04:38:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 721b9ef6-b391-3dde-94cb-c780eeddc631 | -4.65979 | -44.10726 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9a246c1-0dc3-3b4f-b50a-f2a8bda7615c | -5.46552 | -44.64788 | 2025-10-16 04:38:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f7d8b94-38b4-33e8-bbc0-98c94bcdf6ff | -8.24322 | -44.03173 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d09d1b8e-7de8-3671-b0ee-fe0f4399649a | -7.11279 | -44.71561 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e8c3c1e-7771-3b97-82ce-cd798ce9094b | -3.68257 | -47.63395 | 2025-10-16 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 025692c4-a86f-313b-9579-0662c07babec | -2.26001 | -47.85522 | 2025-10-16 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a88d41d0-8542-3277-8786-6144bafb2ab4 | -6.2507 | -44.02613 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c831d424-8d1e-3589-afee-b3b88b5874be | -5.40675 | -40.9129 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| efbe5814-39b3-30eb-b24b-881330ec90a6 | -5.13745 | -46.1059 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97cd0029-f19d-35c0-8b33-07e496ec5260 | -4.92439 | -45.88626 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe39835a-a33e-3c48-89a4-6b805d671355 | -8.24228 | -43.40878 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 445d7fd2-076b-3ed8-b946-f746fd2ad0a3 | -7.16981 | -42.51347 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8082ee2a-57c7-3792-9287-f6da1f1fe768 | -6.90854 | -41.84602 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7ca494e2-a30b-3b0e-b844-b5a114364375 | -6.80555 | -44.53677 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a55220d-50a6-35da-8869-11f1baed72e5 | -5.87737 | -43.87806 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a749cab7-98a5-343b-b01a-47c89cb2e4c6 | -5.85779 | -42.87888 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 86e037d8-69da-3685-8ae8-2665fe772333 | 0.09313 | -51.03828 | 2025-10-16 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 004fda70-a1c1-3328-845a-b751cf304a1f | -7.53707 | -44.28159 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18e0077d-ee48-31dc-b47d-96012859bd7d | -3.99522 | -48.33543 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14081705-cb66-316b-a9ce-7bce8306e9dc | -6.66994 | -45.02866 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbf76ba5-1b7c-3592-ab48-470f8e56c155 | -2.70487 | -49.85934 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44294212-bbae-39ba-bcb8-a4b57f607957 | -6.00843 | -43.11869 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cef51bfb-77db-3659-844c-f4c6f844427a | -4.44129 | -44.14474 | 2025-10-16 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b273a4d-6f37-34d9-878f-15359e8bdc2d | -4.38311 | -43.39103 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| d16e579c-24f5-398a-befe-ffe509402a74 | -2.8799 | -50.73883 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2458046-80ae-36ea-b246-ad7539899307 | -4.62166 | -49.55377 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b12a1c1-1461-3a1b-944a-e6c6f95bc49a | -7.48339 | -42.7543 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7da5cc40-1d3f-33ee-a7ae-406ad15f675c | -8.2249 | -44.00883 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6078708-968b-320a-a9ee-3df2f070d94d | -4.24546 | -46.22499 | 2025-10-16 04:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24532e9a-407a-3d57-bd0e-cbcb85050bd5 | -7.20814 | -43.8358 | 2025-10-16 04:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4ab033e-ed59-3b9a-8624-fe3d9ed42f90 | -7.3418 | -43.86739 | 2025-10-16 04:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7a844623-47dc-33d9-a6b8-a9f8df609850 | -6.02671 | -43.39246 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9865e3e7-bdd1-39ab-b80a-eb7e96b5f240 | -5.87506 | -43.89364 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c34abd2-c599-3b8e-97a4-85545e0c1e4c | -5.76527 | -47.91053 | 2025-10-16 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85ac7140-86ec-3725-9155-3c735a1de711 | -6.45665 | -41.82393 | 2025-10-16 04:38:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d7937b74-4a84-315e-bebf-4888659f1756 | -6.94822 | -47.74211 | 2025-10-16 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ef2f4d6-462b-3116-b4ca-d83c238ff50f | -4.37839 | -43.39415 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 56c38134-0c6f-3f12-81f2-295fe9732e28 | -6.06139 | -44.52766 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| edb357b5-8987-3821-a81a-e846cc74c456 | -5.87602 | -43.85865 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34f34fdd-63bb-317f-9e2a-48987506dcbf | -7.95278 | -44.13147 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49913e07-9486-335f-95e7-ddb24b4ac0a1 | -6.05836 | -41.93666 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b9a106d8-d81c-3f99-ae79-0bf5f9930235 | -2.7073 | -49.86036 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bb350c5e-5ae6-35f8-a7cc-3e31b091b3c8 | -8.17734 | -44.00908 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f39bede6-568b-37c0-8197-67b715965e90 | -7.20297 | -45.48181 | 2025-10-16 04:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 965f71d6-da9a-3c86-952c-f8de73dc3de3 | -5.61571 | -42.68822 | 2025-10-16 04:38:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9568915e-57d1-3919-ba51-2ee492a193f0 | -5.33326 | -45.03106 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2f9507b-cb9f-33e3-90c9-edfb18426c4a | -6.3363 | -44.00836 | 2025-10-16 04:38:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3c5a1da-f569-35a4-837c-52ce04977690 | -3.33259 | -50.10375 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4eed1516-e5e8-37ab-8904-018605286ab3 | -3.92811 | -47.69348 | 2025-10-16 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9ed6196-f866-32b3-b56c-0708b8139148 | -4.66084 | -44.1003 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 561a1b20-4131-3df3-a1de-116f689fcc3d | -4.67385 | -44.09534 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 13312690-9e5d-3f44-9950-49681526e68d | -5.45196 | -41.02954 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c41828fe-28a8-3162-a13c-60ccffb17f41 | -6.30307 | -44.12386 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ced8013f-d2ab-38e0-8193-d2fdedacf5c7 | -3.27616 | -45.8363 | 2025-10-16 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 16922dc1-16f6-381d-b436-7eb60f075177 | -5.88674 | -43.87173 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffa7aa83-f566-33a2-8293-705679b751d1 | -7.04993 | -43.97018 | 2025-10-16 04:38:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 672bbdf1-c68a-3012-96e9-835d49556869 | -5.65738 | -51.29931 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55c60425-5114-335c-bf95-6ae8a551aae5 | -8.2365 | -43.41943 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| afc7e92c-c473-32e7-bad6-8c231264e2fa | -4.38896 | -43.38025 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f8b4302-ff65-3f82-b7d8-98117c2e1736 | -5.62914 | -43.92211 | 2025-10-16 04:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cb48990-ceb0-3ae2-bb19-dc0693074fdc | -2.81543 | -54.38137 | 2025-10-16 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c45e09c-d78b-37c8-be63-aa898cdb53fd | -4.91712 | -45.98191 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60c1cb19-c15c-3825-ae83-892e7e863c16 | -5.10227 | -44.94614 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4c5ec00-a0db-3521-bcaf-c1e3a5c20706 | -5.98365 | -44.56639 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f671d34c-edbc-377b-b05e-94fdd9e48582 | -8.27484 | -43.36854 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a6ac1353-0aa7-3d0f-9d3f-0cfcba778ccf | -6.6692 | -45.03363 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a57b04d4-56e0-3370-a44d-7fadebc73d26 | -6.20448 | -42.60649 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ff518c9a-1f19-3b95-9e80-e4406725aae6 | -4.66692 | -44.08712 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dd77614-a409-3dc5-a8a1-e88601b82109 | -6.22478 | -41.55234 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7241833a-426c-3bca-a518-2190a6dd2b62 | -6.21791 | -46.0256 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6013a6a2-7ccc-3903-b5b6-66f6a5a40a80 | -4.84436 | -42.79046 | 2025-10-16 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| c3a97a2c-0bfb-3d7b-8d9e-779e599ae08a | -4.65003 | -47.95317 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea15927b-4292-3490-92b1-a710eab0c460 | -2.79017 | -49.59587 | 2025-10-16 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| baed7ee6-8afd-35fa-936b-e5df6a22ae8e | -5.86193 | -42.81796 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ebf4c640-d0fd-3d06-9159-fa01e34d9252 | -7.90368 | -44.98935 | 2025-10-16 04:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95a54cbe-831c-37a5-bc94-98b75edd6f0f | -6.52991 | -42.20446 | 2025-10-16 04:38:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 04b9140c-7bec-3fff-b20b-cb898b482523 | -3.68202 | -47.63747 | 2025-10-16 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 95d6eb99-e084-34cc-9d16-7b7217ea6f16 | -6.22334 | -44.59737 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bfac551-53e2-39b0-a7c8-3b8942f4357b | -3.16707 | -49.53718 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 509fa365-507a-3608-92cc-49b5b9af8226 | -2.29632 | -47.99136 | 2025-10-16 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61636f43-ec18-3dc5-9493-3445ada9729f | -5.53794 | -41.32821 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2bd02bdd-74e7-3557-b7ec-49999c2c8c84 | -6.2477 | -44.01782 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb27d6e3-69a3-3f31-be1d-c0be71352805 | -3.67578 | -48.31021 | 2025-10-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6d14a22-057d-3835-afd4-b3a5c1b02539 | -7.04754 | -47.36745 | 2025-10-16 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa805a99-a5a0-376d-9218-e9891e6fdf5f | -6.37005 | -41.49405 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 819e907e-6e4b-394a-a256-dfb6fadeb4f1 | -4.25152 | -42.99161 | 2025-10-16 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e82fb81a-3e36-3b84-a157-38f3934609a3 | -6.17799 | -44.29979 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c798e34-e451-3473-aad0-9049c1e46493 | -3.68183 | -52.06361 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README47.md)
