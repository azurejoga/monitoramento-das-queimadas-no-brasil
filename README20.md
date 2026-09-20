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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef950daf-6b99-3d30-b1b6-65cc463107b4 | -12.75875 | -46.12688 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b3d2038a-2db4-361b-b681-750a7650c071 | -10.47112 | -45.0917 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d039b7a4-ebf2-30c2-a056-70e40d0beef5 | -9.79082 | -45.0741 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26d5ce7a-fdec-3ea5-8eed-c6d441c1ddcf | -7.28254 | -45.54895 | 2026-09-20 03:45:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3035bb48-d336-3d97-81a1-d579f3d6baef | -11.45261 | -45.72175 | 2026-09-20 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69c2d982-6b57-3e25-926e-d2f67907f853 | -10.85397 | -50.17091 | 2026-09-20 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5795fff-8335-3604-832d-f9cba66a4c41 | -10.60402 | -46.52975 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7af557d3-5ec1-30bc-ad04-a7b624294e47 | -6.56173 | -45.58726 | 2026-09-20 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e73c34c3-6e0d-3b2c-899c-ef3c200ce543 | -7.88265 | -44.85801 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67d82094-c1ca-3c9e-9ed6-807274b02d8e | -7.59185 | -46.97769 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41410af0-8e7e-31a7-a336-7087248d09fe | -10.29948 | -45.42789 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f34cba34-044c-3cb2-abc5-5270efe221e1 | -7.7502 | -46.76847 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 177281d8-0313-30d5-803e-881cc5c05f33 | -11.44622 | -45.32436 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04beb62e-dff9-323d-847c-3423119cf0cc | -7.53628 | -45.43348 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| edf4ac34-f6b7-36ed-beec-7d0e9af3b92b | -10.23814 | -45.35141 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd9ff6b0-fda6-3178-b2ae-b2d9684f2846 | -7.54735 | -45.43541 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 081cd9fc-4f40-3822-bd17-fd03744d65de | -9.72895 | -46.09281 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dda77b1a-2ea2-3003-aecc-9a0db3cb31b2 | -11.32436 | -47.28741 | 2026-09-20 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4731bb3e-f3c1-344f-afa8-6a25fb747ff2 | -8.78443 | -48.71022 | 2026-09-20 03:45:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 179f292f-2beb-3af1-b7a3-be4a834a0eae | -11.03166 | -48.30695 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89151c1e-6c1e-3837-8f13-96d944dd4df7 | -10.30557 | -50.26201 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 15c5db44-a852-3420-8ae6-20e80e19dc16 | -6.31196 | -47.63409 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0cab2c74-01b7-3e95-9496-66b1fbab22a3 | -6.29736 | -47.60527 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 37119d39-3806-3954-9b58-c3ac792ff9a2 | -10.56369 | -46.55769 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38e9cad8-0515-3512-b18e-e5ab39da54dc | -10.30433 | -45.43111 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61b948d2-d068-3660-86f7-84c236927979 | -9.79256 | -45.06446 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fae6b8f-b37c-3359-a9d8-4b41ae670121 | -8.04726 | -46.25331 | 2026-09-20 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 933ce211-3670-316a-9a7c-9f0ab898670f | -9.26473 | -46.19631 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c031e9f-e0cd-3e26-a25e-6c76dfc81264 | -7.43339 | -44.73804 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18caa5e2-1bb0-36ec-b8f6-0929819da02a | -8.50079 | -47.43534 | 2026-09-20 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| de76cfe1-54ee-3ab9-9642-3b78b83898b2 | -12.29003 | -47.11091 | 2026-09-20 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db279a5f-f0cb-333e-843b-f907059353de | -12.11529 | -47.01745 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b858984d-bd41-39ec-8ba3-13339bd35f02 | -10.78241 | -46.33316 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0cb05cd9-032e-3844-a7d3-b2db48350700 | -10.77619 | -46.33563 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bbc2a21-742a-3af8-8c4a-7ac5f6680ef6 | -8.77158 | -44.25698 | 2026-09-20 03:45:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea70a184-781c-3150-a2a9-81c7097e6a5b | -6.30275 | -47.61217 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c65ee9be-499a-31ab-a6f5-084376f8cabb | -7.55226 | -45.43991 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a95958e-9d0b-325d-b1d7-e05f6643fbff | -10.77831 | -46.32468 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 271b7c5e-e030-344a-bb19-92ce11e06874 | -9.61609 | -45.8771 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26b9a78c-255a-33ea-ab1b-ba6e51d7bf3a | -10.13531 | -45.5595 | 2026-09-20 03:45:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73b4eb45-1ebf-3ffc-9b02-2128aeb5de66 | -12.12018 | -47.02248 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0c38ba2-8183-3fd8-9e27-3f2e9fc0f928 | -10.29956 | -50.27132 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| ad8d04b9-6853-39a9-88cd-e0e05719c447 | -12.312 | -50.73308 | 2026-09-20 03:45:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a5eb596d-9667-3268-8019-4c4b059098c7 | -10.4039 | -48.36275 | 2026-09-20 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e738da3b-6842-3dbd-b2ed-4352572391de | -13.03115 | -46.90784 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b6015a8e-7dc5-38cc-8e11-bb985d56b37c | -11.44384 | -45.33707 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 324ae04f-09cc-3698-86bd-dc96f7a81c7f | -11.06308 | -44.68697 | 2026-09-20 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec23f56b-4ac7-366f-8073-ea60177695e6 | -12.12623 | -47.03479 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dbf32542-c18e-3b24-9e81-73a62a5b0e6f | -10.2369 | -45.35806 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7edab55e-5f99-32df-bb29-50fe9ab1b2ef | -7.88324 | -44.85468 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae5f377e-1909-3edd-be4a-22f2a0f01175 | -9.9047 | -45.10214 | 2026-09-20 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f45a383-20c4-38f6-99ca-c02ec3bf8bad | -8.65589 | -45.44063 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ef9a4a5-4284-3ec5-86e3-e86f8294175a | -6.30291 | -47.61018 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 817e654c-f60b-3a02-9c46-67af5741a561 | -7.76347 | -44.88945 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3309848-8da4-3fb6-8622-1987458ccb8b | -11.45633 | -45.70226 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7e8288c-ae48-311c-9c31-6e7e4ab700b2 | -11.45509 | -45.70875 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af466892-94cb-3cf6-900c-3081899aa18c | -11.48254 | -47.78899 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69508555-0956-3960-9782-ec270461bccf | -9.73142 | -46.08578 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b17782de-b1a7-3fa4-826a-e07a28813de1 | -6.30373 | -47.60691 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| db128354-591e-33fc-b912-1c5897172e8a | -12.15419 | -47.02881 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 177190a0-5d02-3ade-ae58-f09c95861038 | -10.30009 | -45.42466 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87671ac4-6159-304a-b279-d212d697f3f7 | -7.53562 | -45.43716 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| d3ded83c-1498-3939-82ca-e02545ef92ba | -13.02799 | -46.92709 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f76b7d10-7e3d-3700-bd58-545534238520 | -7.75263 | -46.76731 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5ce940f-8a24-363d-a3c5-0b8652df4308 | -8.49866 | -47.44018 | 2026-09-20 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 3fae81a1-803f-3ec7-8973-8e1cb764245a | -11.4494 | -45.39283 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9386a63d-3b23-3354-88f2-7d9bf31926e5 | -11.83612 | -46.85889 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a43f1f78-6806-347b-8db7-2209cfa3f566 | -9.82514 | -46.43128 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f646af9d-1ea0-343f-a267-6b5ba41c26e6 | -10.30238 | -50.29385 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4238c4ef-5e78-390f-8ccd-6d5dff770a71 | -7.41083 | -46.62077 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 241136c0-751b-3dd0-972f-e0449f715711 | -8.71087 | -45.44677 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d02fed2a-730b-34a5-9548-d671b929e7fa | -8.38124 | -47.19284 | 2026-09-20 03:45:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f63a435-b461-3d7a-a716-4b1330317915 | -7.5342 | -45.88102 | 2026-09-20 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| baeffbfb-03b2-3f0e-a7ac-40e50a9c018b | -6.56533 | -45.58081 | 2026-09-20 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08802569-7fa5-39ea-825d-1d1933ab47d8 | -7.76623 | -44.05165 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae458bda-f9dd-3aa6-8ed9-f59b41cec301 | -11.48349 | -47.78418 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fcd5cd29-c5a3-3068-bce9-b09484a0ed63 | -9.73536 | -47.26371 | 2026-09-20 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddf991f4-aa51-355a-b9a0-e436425f3d96 | -11.45571 | -45.3876 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 141f8b87-ddb9-3c37-b65c-84feac948fe6 | -8.39348 | -45.62839 | 2026-09-20 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 906340c2-3252-319f-ba0f-435a24735022 | -8.65456 | -45.44011 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00b52fe0-ebcc-3749-92c8-1e36085b562a | -7.53496 | -45.44083 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 3a853107-3aad-3783-82f2-89dbb3131b37 | -13.95238 | -47.85797 | 2026-09-20 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73a20408-b4fc-3740-98ff-715ab9398d69 | -15.48052 | -48.42313 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae9c0900-547a-3313-b9f3-27208d7f2aae | -14.69251 | -46.69614 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b1c2e98c-4584-3194-8189-7f13af48ef68 | -14.79423 | -48.53303 | 2026-09-20 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a10951d9-1c6c-3547-b81c-0e38504d6524 | -14.92433 | -49.91741 | 2026-09-20 03:47:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f0994d9-2d38-3d01-bda1-83595cc73230 | -20.77729 | -47.16503 | 2026-09-20 03:47:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95241dea-a6d9-32ba-9a48-421dc431be62 | -17.03802 | -47.28561 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f1a2a45-6a1c-353d-a349-c3ee22ea9657 | -17.02167 | -47.15279 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7766ab37-0b39-3982-9b35-70ac65422fb3 | -15.17266 | -48.16545 | 2026-09-20 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e20cb63-c0b0-3e30-abad-5a77e142b682 | -15.32272 | -49.56504 | 2026-09-20 03:47:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eb6a6314-9199-3ae0-8b39-25d0308db90e | -17.0387 | -47.28232 | 2026-09-20 03:47:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d4da930-7b10-3c75-afe6-f0f84e907c63 | -14.91832 | -49.91848 | 2026-09-20 03:47:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7607bc81-825e-390d-ab91-09d34e7a42da | -14.612 | -48.10735 | 2026-09-20 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a14e7cb7-c303-3292-a303-010aa5ca6cc9 | -13.73522 | -48.78261 | 2026-09-20 03:47:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7757154d-30e3-31cc-9665-f15a64e0fd5f | -14.92591 | -49.91438 | 2026-09-20 03:47:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efb906b3-67a6-3f81-b2aa-d0dcc99ffc23 | -14.69461 | -46.69242 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 321e3c8e-e98d-3bc3-bce5-5caaa7836457 | -16.59126 | -45.33339 | 2026-09-20 03:47:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 156c389a-f6d8-3af7-af0d-ba475fe3000c | -14.68337 | -46.69366 | 2026-09-20 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 88bc65ef-6ee1-3f2b-b5ef-3a3ee3d3710e | -16.58266 | -51.6293 | 2026-09-20 03:47:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README21.md)
