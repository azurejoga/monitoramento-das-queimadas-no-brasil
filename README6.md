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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 503e46e1-289f-3075-834a-64216d27a438 | -6.5927 | -44.683399 | 2024-10-27 00:13:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 538803d5-6c19-3541-93b4-2de207fb04c0 | -6.8516 | -45.858101 | 2024-10-27 00:13:36 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d99e8ab4-3bd9-3ab4-8597-1c9d85535e0b | -6.8533 | -45.8661 | 2024-10-27 00:13:36 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66837ed0-6030-3626-97f0-3aecca9857be | -6.855 | -45.874001 | 2024-10-27 00:13:36 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dddf5a8a-ddc3-35b6-8955-843cc382790e | -6.8603 | -45.897999 | 2024-10-27 00:13:36 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7dbf32a-5c75-3c09-a601-3c1f939c2ad8 | -6.8418 | -45.860298 | 2024-10-27 00:13:36 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 421c5e9c-1740-3310-b734-1b3c39950ef3 | -6.8435 | -45.868198 | 2024-10-27 00:13:36 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dbea11f-a95b-3e2e-a47b-2b7189b32775 | -6.8452 | -45.876202 | 2024-10-27 00:13:36 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c965a2c5-42e1-3d34-8d9f-4e1630158134 | -6.3687 | -44.000401 | 2024-10-27 00:13:37 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71fd2728-723f-352c-88c2-f2cd17299adc | -6.3702 | -44.007401 | 2024-10-27 00:13:37 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26a6034f-7a54-34bf-8587-01c8934cb40a | -6.3589 | -44.002499 | 2024-10-27 00:13:37 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33047284-f3bc-3e9e-bf10-3a45ec55c3a4 | -6.3604 | -44.009499 | 2024-10-27 00:13:37 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59de9b0c-ea21-3884-9d00-2454f7dfab39 | -6.8198 | -46.135502 | 2024-10-27 00:13:37 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40bd8791-b09e-3ece-b041-0afcd1faec2a | -5.6902 | -41.634499 | 2024-10-27 00:13:39 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4cc434eb-87d7-3efd-8ea1-88d08788dc06 | -5.6919 | -41.6418 | 2024-10-27 00:13:39 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61cdc5bc-2386-3428-8b6e-4aba12832034 | -5.6804 | -41.636799 | 2024-10-27 00:13:39 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b0fb66cf-7076-37bb-a33f-6bd26c32d776 | -5.8794 | -42.557301 | 2024-10-27 00:13:39 | METOP-B | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ecaf84c3-6df6-330e-9afd-b116803ed1a2 | -5.6497 | -41.818199 | 2024-10-27 00:13:40 | METOP-B | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ddae5853-227a-3eb0-8d70-0f26e95b2c88 | -5.6513 | -41.825401 | 2024-10-27 00:13:40 | METOP-B | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f4dd6a17-cafa-33e4-a3cd-058f4a357e3e | -5.6529 | -41.8326 | 2024-10-27 00:13:40 | METOP-B | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cfcc1780-8a0e-3913-a8df-a868596c9200 | -5.9767 | -43.537701 | 2024-10-27 00:13:41 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73843ce6-3f04-3a25-a012-2f0ba255bf58 | -6.0998 | -43.856701 | 2024-10-27 00:13:41 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 106fb21f-8914-32f3-9104-e0e551cf8d78 | -5.6087 | -41.729099 | 2024-10-27 00:13:41 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f6c01653-5087-3d7c-b35e-063e8ade735a | -5.5989 | -41.7313 | 2024-10-27 00:13:41 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0b28c819-8f64-3ab4-917b-d2629768c5af | -5.6006 | -41.738499 | 2024-10-27 00:13:41 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d2744f7f-8cee-3764-90e2-0878a7c82780 | -5.5891 | -41.733501 | 2024-10-27 00:13:41 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| abcb0488-f3e4-3f06-8395-ac8c55efaf57 | -5.4384 | -41.615101 | 2024-10-27 00:13:43 | METOP-B | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| faa0ed35-5c56-301e-bbea-da27b2f04fbf | -5.4401 | -41.622398 | 2024-10-27 00:13:43 | METOP-B | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b770bdb9-911c-3814-9da2-3b04913c3db6 | -5.4683 | -41.926998 | 2024-10-27 00:13:44 | METOP-B | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a76002dd-6855-3565-82e1-bd0a70d1a196 | -5.4699 | -41.934101 | 2024-10-27 00:13:44 | METOP-B | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 29743a82-d447-3088-a1c9-5c6c0382ee6e | -5.4649 | -41.957699 | 2024-10-27 00:13:44 | METOP-B | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 049b3ce1-638e-31fe-84e9-04f6dbb97472 | -5.5244 | -42.219601 | 2024-10-27 00:13:44 | METOP-B | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0d3c66bb-af55-32a9-95d6-9b7ccc4b42aa | -5.526 | -42.226601 | 2024-10-27 00:13:44 | METOP-B | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08390e14-8d48-3173-b43c-62e252e15330 | -5.6262 | -42.7593 | 2024-10-27 00:13:44 | METOP-B | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb4c6637-933a-30f5-bb7f-f0b2859ed866 | -5.6325 | -42.7868 | 2024-10-27 00:13:44 | METOP-B | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 93989981-c44c-335e-b7a4-f28f2a0c28cb | -5.2634 | -41.210499 | 2024-10-27 00:13:44 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e3fabef6-5c23-3f9d-9eb3-22acb1553cf8 | -5.2652 | -41.217999 | 2024-10-27 00:13:44 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 023f0932-553a-3258-9e21-dcaa755c01ab | -5.2669 | -41.225601 | 2024-10-27 00:13:44 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ad8aaea2-3a26-34d6-8c99-a49863bf85a7 | -5.8256 | -43.8741 | 2024-10-27 00:13:45 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5b26e5c-66f8-34c0-88b8-7ddaee2dab00 | -5.8938 | -44.317501 | 2024-10-27 00:13:46 | METOP-B | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9681a4b7-cec7-3100-9bf6-7807267eb2a6 | -5.8954 | -44.324402 | 2024-10-27 00:13:46 | METOP-B | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc622cf5-58a8-31b1-9ba9-f2a396c5131c | -5.8064 | -44.110401 | 2024-10-27 00:13:46 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77ba3b4c-6db1-3e52-b420-5ad736038508 | -5.8079 | -44.117298 | 2024-10-27 00:13:46 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe9ea7b-0219-3b11-81c2-e952f1d1b79a | -5.8095 | -44.124298 | 2024-10-27 00:13:46 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f520d8ee-1b13-3104-9e49-89cc47b65802 | -5.811 | -44.131199 | 2024-10-27 00:13:46 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6071426-c650-3785-b842-a76531405607 | -5.52 | -42.927601 | 2024-10-27 00:13:47 | METOP-B | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d23ace9e-4003-343f-b510-1be9ceda0b83 | -5.7121 | -43.827099 | 2024-10-27 00:13:47 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6eec75d5-87a3-3f6b-bb5a-ccf247ae57b7 | -5.7136 | -43.834 | 2024-10-27 00:13:47 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1593b0b7-daf9-39c2-8524-087c1d23b0e9 | -5.7152 | -43.840801 | 2024-10-27 00:13:47 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96e4a7f6-f889-316b-b387-1295c352ceed | -5.698 | -43.902401 | 2024-10-27 00:13:47 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c428186-f743-3c0d-adde-22cb347a1b55 | -5.6996 | -43.909302 | 2024-10-27 00:13:47 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fade3a2e-74ee-355d-b5b4-8b453929344d | -5.9198 | -44.711399 | 2024-10-27 00:13:47 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2b3d806-51b0-3c2a-85a7-dbaa55371fef | -5.9214 | -44.718498 | 2024-10-27 00:13:47 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5123bc45-62d1-35a8-91bd-7d03551939f5 | -5.4358 | -42.874199 | 2024-10-27 00:13:48 | METOP-B | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db3be405-7107-3433-9585-f3d057bd43f6 | -5.4373 | -42.8811 | 2024-10-27 00:13:48 | METOP-B | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 83829a0c-e65a-321d-ba75-f20f4bf9a0fd | -5.4774 | -43.332802 | 2024-10-27 00:13:49 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27292533-dde8-31b3-97c3-437214fc06aa | -5.8273 | -44.897099 | 2024-10-27 00:13:49 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc6192ef-93ad-368b-a075-de93b3fe8214 | -6.0998 | -46.130402 | 2024-10-27 00:13:49 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f66d7ab2-b050-32fb-8043-4bf717eb2b68 | -6.1015 | -46.138401 | 2024-10-27 00:13:49 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af308f44-6903-3af7-8cab-35c2ba548f38 | -5.2786 | -42.771999 | 2024-10-27 00:13:50 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f2df2e94-90ee-3177-8127-3cab4fde57de | -5.2948 | -42.9347 | 2024-10-27 00:13:50 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 282644e9-da51-34cb-88d5-6e98d377ec7c | -5.2964 | -42.941502 | 2024-10-27 00:13:50 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 115a28ef-ddc6-3659-8bb0-16e03c61d9d9 | -5.4118 | -43.361801 | 2024-10-27 00:13:50 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9479561-dece-38f8-ac70-2d9350bb3e02 | -5.4133 | -43.368599 | 2024-10-27 00:13:50 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 163c6c04-553b-30cd-bcae-6f39c3a87953 | -5.4148 | -43.375401 | 2024-10-27 00:13:50 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80f5ab08-ee7c-3517-84a1-0f621b802b2d | -5.4481 | -43.569099 | 2024-10-27 00:13:50 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48539ba5-ea0a-3b9f-8b92-e41c902da7a0 | -5.2932 | -42.927799 | 2024-10-27 00:13:50 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3299ac2-17c9-3028-aefd-5012dcc0d3f0 | -5.1561 | -42.412998 | 2024-10-27 00:13:51 | METOP-B | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0bf1dfc6-d29d-3376-8f9a-fa29a553f5b6 | -5.0123 | -41.871399 | 2024-10-27 00:13:51 | METOP-B | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 73981f96-18f4-344c-8dcb-6b7120a06c85 | -5.5575 | -44.333099 | 2024-10-27 00:13:51 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7cb4aa5-9218-360b-9325-00bac3e6610a | -4.3298 | -39.129398 | 2024-10-27 00:13:52 | METOP-B | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ab33cddd-cbac-36a2-afe3-7097b476251e | -5.6236 | -44.813999 | 2024-10-27 00:13:52 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 050f3fb5-07b6-33ee-bc97-bb5576356593 | -5.6252 | -44.821098 | 2024-10-27 00:13:52 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b0f7e14-65c1-368c-af79-7023574e237f | -5.6138 | -44.8162 | 2024-10-27 00:13:52 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa51528b-22ae-3d6d-9571-2bc278e938ac | -5.6154 | -44.823299 | 2024-10-27 00:13:52 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fc00112-ac45-3198-a5f1-e111ad6edcd7 | -5.0981 | -42.8848 | 2024-10-27 00:13:53 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4add20a3-9216-35cb-92ca-207044ab1e83 | -5.0997 | -42.891701 | 2024-10-27 00:13:53 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b2e5684-4f33-3102-8f5f-ad608a679a90 | -5.0882 | -42.887001 | 2024-10-27 00:13:53 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d988d509-7393-335c-acee-d40d6b735566 | -5.0898 | -42.893902 | 2024-10-27 00:13:53 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d694325f-d166-3ee9-9506-a94aa5c51c76 | -5.0784 | -42.889198 | 2024-10-27 00:13:54 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77af051b-83e5-3edb-aa9d-58cc4dd7f8f7 | -4.5557 | -40.641701 | 2024-10-27 00:13:54 | METOP-B | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0351a8cb-7bac-3e1d-a2c8-96989a7d8c26 | -4.5575 | -40.649799 | 2024-10-27 00:13:54 | METOP-B | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b9fad8ca-f36d-3e18-9da9-599c9719cd22 | -5.0449 | -42.968899 | 2024-10-27 00:13:54 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79069d35-186d-3f79-8f24-624b6ab2184b | -5.3276 | -44.18 | 2024-10-27 00:13:54 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09091c72-c9c4-342f-90a2-f6df167c9d1f | -5.3292 | -44.187 | 2024-10-27 00:13:54 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 047fc652-93e0-31fe-9451-31226d1bc3fb | -5.3235 | -44.253601 | 2024-10-27 00:13:55 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e3b87a7-ab8f-3b79-991c-2bd0b33558ab | -5.2689 | -44.055401 | 2024-10-27 00:13:55 | METOP-B | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f511010f-4e4b-3ee5-8b4a-cfed0d39ba79 | -5.2704 | -44.062302 | 2024-10-27 00:13:55 | METOP-B | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5306ea94-8068-371e-ae31-1f4d1370ba22 | -4.8473 | -42.460201 | 2024-10-27 00:13:56 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c826747e-b746-31f6-a2ff-18abe26d33ff | -4.8488 | -42.467201 | 2024-10-27 00:13:56 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e8bb7406-405d-31c2-85ba-091aae57b30c | -5.2773 | -44.460999 | 2024-10-27 00:13:56 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c77920f-47bc-32a1-9bcb-5b0991bd8af3 | -5.2788 | -44.467999 | 2024-10-27 00:13:56 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3205204d-e427-3eaf-87ea-4520837253e1 | -4.843 | -42.941898 | 2024-10-27 00:13:58 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e381263-efc9-3b41-bef2-375aa5f692c1 | -4.2865 | -40.591801 | 2024-10-27 00:13:58 | METOP-B | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fc4cb367-0d8c-33a5-9df1-f14c5cf22028 | -5.024 | -44.2038 | 2024-10-27 00:13:59 | METOP-B | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9efd3ada-a211-31d8-93e6-21250ff592a4 | -5.1312 | -44.728901 | 2024-10-27 00:13:59 | METOP-B | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b4d5a55-ad5c-379f-b459-48838cf7fc9a | -4.7367 | -43.246601 | 2024-10-27 00:14:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd85669-fe8b-3697-8695-3062cb524b01 | -4.7583 | -43.3423 | 2024-10-27 00:14:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4e58a54-a239-3a71-b388-f48600d06faf | -4.7598 | -43.349098 | 2024-10-27 00:14:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9867c692-13ad-3006-ab0d-89bc15ce8b6a | -4.7613 | -43.355999 | 2024-10-27 00:14:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
