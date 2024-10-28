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
| bc287043-c958-3b6c-aba5-bac05592c2f2 | -5.4166 | -46.348499 | 2024-10-28 00:49:08 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6b43941-3883-3c82-95bd-89feee5e164a | -4.3504 | -48.6092 | 2024-10-28 00:49:08 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccad025c-d2e7-34fb-aa51-5ec9cef68cde | -4.3437 | -48.625 | 2024-10-28 00:49:08 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f45c8225-cbd7-3023-ae8e-5ea23fb72cf2 | -4.3453 | -48.631901 | 2024-10-28 00:49:08 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c42d5fb1-a5ea-3604-80b9-675f828dcc11 | -4.3469 | -48.638699 | 2024-10-28 00:49:08 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfa5b140-1f7c-3e81-802f-e98d9a27b1a9 | -3.8362 | -46.4743 | 2024-10-28 00:49:08 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3c6ecff-010e-33ab-8797-c50c9c8870a4 | -4.3355 | -48.634102 | 2024-10-28 00:49:08 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49c382df-d8db-34c7-8e34-76025a373bd9 | -3.8264 | -46.476501 | 2024-10-28 00:49:08 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 539be305-2fd3-3492-9ecd-6d6172d93f04 | -5.405 | -46.342999 | 2024-10-28 00:49:09 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8375e31-1d91-3ea1-b06f-2c6a2993dea5 | -3.6778 | -45.927601 | 2024-10-28 00:49:09 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 927d8d7e-90c0-3415-a414-ebd676496e33 | -4.2983 | -48.606499 | 2024-10-28 00:49:09 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b346c49-1a72-3ea6-a301-65de84bf3ac1 | -4.2998 | -48.6133 | 2024-10-28 00:49:09 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aed7bd89-05d5-3d8f-b576-71b697d2238b | -3.668 | -45.929798 | 2024-10-28 00:49:09 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb4eb9c8-275c-31bf-b2a8-32c458cf0a88 | -4.2947 | -48.636101 | 2024-10-28 00:49:09 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44f2485e-d0a6-322d-a436-3111c1691563 | -4.2963 | -48.642899 | 2024-10-28 00:49:09 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a594b88d-c47c-38cf-8b2e-7c475c6506be | -4.4927 | -42.8755 | 2024-10-28 00:49:10 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0207d8fd-a3cf-3c8c-ad10-96bca434c7f4 | -4.5453 | -42.965801 | 2024-10-28 00:49:10 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e069bdac-5351-3822-8210-1db7c69099be | -4.5482 | -42.977901 | 2024-10-28 00:49:10 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9a73b7d-1de0-3d73-a22e-33e91ce91bca | -4.4956 | -42.887699 | 2024-10-28 00:49:10 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7127ea6f-01b5-35a4-8470-0f49708f44e7 | -4.483 | -42.8778 | 2024-10-28 00:49:10 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05af2e31-1ccd-3591-8103-398e550a0a2a | -4.4859 | -42.889999 | 2024-10-28 00:49:10 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f49c2aa9-883d-3d56-aa76-1a992230f1ba | -4.7509 | -50.818199 | 2024-10-28 00:49:10 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ba0e974-6308-3f16-89be-cb4b5355c9e2 | -4.7525 | -50.8255 | 2024-10-28 00:49:10 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c60e578-1ead-3af1-bc98-30c9de645899 | -3.8179 | -46.928101 | 2024-10-28 00:49:10 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b08c5e6a-044f-3e95-a7c6-09d33ca2fa67 | -4.7497 | -44.084099 | 2024-10-28 00:49:11 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94d63411-5f6c-3b69-a5de-33682a597f21 | -4.7522 | -44.0942 | 2024-10-28 00:49:11 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9a90111-1e45-3032-a16d-aff7796ee783 | -4.0988 | -48.232498 | 2024-10-28 00:49:11 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fc36d9b-c41d-33ba-a54a-bb1aa49dffa6 | -4.0706 | -48.2896 | 2024-10-28 00:49:11 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d4e8bfa-2885-3ab5-82be-9667ea56a9b2 | -4.1082 | -48.498001 | 2024-10-28 00:49:11 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c82f0ea-e24f-3707-b879-034e7693d42d | -4.1098 | -48.504799 | 2024-10-28 00:49:11 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34cf71e0-82d6-38a1-8669-a360cef35452 | -4.8186 | -44.7239 | 2024-10-28 00:49:12 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89112c97-ebcb-3764-a4be-64f41a236a55 | -5.1237 | -46.022499 | 2024-10-28 00:49:12 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d80455d-c1bc-338a-96f2-72053e8a33fb | -5.1256 | -46.030399 | 2024-10-28 00:49:12 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c057703b-06b7-3288-b30f-66c6df21ed99 | -5.0614 | -45.800201 | 2024-10-28 00:49:12 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6de08b56-feb7-3983-8bbd-77815a63fd1b | -5.0633 | -45.8083 | 2024-10-28 00:49:12 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f008f38d-9465-3c32-8943-2f8168dba4d6 | -4.8467 | -44.930099 | 2024-10-28 00:49:12 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2e0be98-e65c-3e06-b47f-57cb89749a2a | -5.2446 | -46.673801 | 2024-10-28 00:49:12 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 494af1eb-32d6-3a32-9253-484886997440 | -5.2481 | -46.688702 | 2024-10-28 00:49:12 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d605d650-0e0f-380e-9179-701e023720f5 | -5.2498 | -46.696098 | 2024-10-28 00:49:12 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ccd84515-a7de-380f-866c-47d2af3c7d59 | -4.0984 | -48.500198 | 2024-10-28 00:49:12 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df0de672-bbfd-3830-a8a9-a920706e6a41 | -4.1 | -48.507 | 2024-10-28 00:49:12 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f829a33-7254-34a7-86fd-057f8718b1f4 | -3.077 | -44.331299 | 2024-10-28 00:49:12 | METOP-C | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 55c4d8e3-696c-3b1c-985d-4edb91c79246 | -4.1365 | -42.1618 | 2024-10-28 00:49:13 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a06c27f9-38bd-36ff-974a-a6f387159b4c | -3.1734 | -45.0051 | 2024-10-28 00:49:13 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 696dacb3-bbd9-3140-8bea-79f15e08d14c | -3.1756 | -45.0144 | 2024-10-28 00:49:13 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b65a5cfa-3ccf-31b0-8871-eabce20715b5 | -4.6597 | -44.662102 | 2024-10-28 00:49:14 | METOP-C | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 947599c7-6e22-355f-a2c7-dbb552463874 | -3.9365 | -48.334301 | 2024-10-28 00:49:14 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb1c5dec-eddf-36be-b401-89aeb1987f63 | -3.9381 | -48.341202 | 2024-10-28 00:49:14 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55242379-bb71-3034-a1fb-f3eb60790124 | -3.9397 | -48.348099 | 2024-10-28 00:49:14 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b34344-1224-3ece-9b1f-59fd82ecbeee | -3.9413 | -48.355 | 2024-10-28 00:49:14 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b427229-c5db-3a11-8ac9-06391355c16b | -4.3778 | -50.444901 | 2024-10-28 00:49:14 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6711738f-5c9b-384a-805a-51348d4e5798 | -5.0122 | -46.473202 | 2024-10-28 00:49:15 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c340a41a-be3b-3e2b-9d2f-8aaa129c0391 | -5.014 | -46.4809 | 2024-10-28 00:49:15 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3189ee00-b9ab-3b01-9840-f7afc2ba2d76 | -3.5889 | -47.2756 | 2024-10-28 00:49:15 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6c931ed-a56c-3c24-b565-da22737c473e | -4.981 | -46.472301 | 2024-10-28 00:49:16 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71ef165f-c174-36b4-a5dc-f185ffba9a59 | -5.3823 | -48.341099 | 2024-10-28 00:49:16 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7c5e2744-0340-3be6-8941-85b0042d8772 | -5.3839 | -48.3479 | 2024-10-28 00:49:16 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e069c442-8364-3061-bc83-bfc51aa63122 | -5.421 | -48.734901 | 2024-10-28 00:49:17 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 256975b8-0cfb-3552-8854-97e42fa23fec | -5.4226 | -48.741798 | 2024-10-28 00:49:17 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bde6897-cfb0-360a-be1f-18a7877589f0 | -5.2301 | -47.9482 | 2024-10-28 00:49:17 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e36e5623-17b7-3255-94a3-b6c96cdb36e3 | -3.2415 | -46.267799 | 2024-10-28 00:49:17 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1b46a23-3283-3552-b1c1-fa0819397b00 | -3.2433 | -46.275902 | 2024-10-28 00:49:17 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db162a99-1b98-3b92-a955-ca865078eb84 | -3.1992 | -46.175098 | 2024-10-28 00:49:17 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4553b851-3d52-33eb-ad2c-58ccff46f899 | -4.7173 | -45.784698 | 2024-10-28 00:49:18 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12f574d3-7444-3f77-87bb-697201e8a48e | -4.7089 | -45.881199 | 2024-10-28 00:49:18 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d9cde765-b60b-3ecf-a097-ab34f89ff3e4 | -4.6973 | -45.875301 | 2024-10-28 00:49:18 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0573c169-6d8b-3634-a4f0-796a2131e7b5 | -4.6992 | -45.883499 | 2024-10-28 00:49:18 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ae9d763-1db1-382b-8d36-1b106dd94fca | -4.7011 | -45.891602 | 2024-10-28 00:49:18 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8a2ab50b-1115-3a27-852d-c61c94ec135f | -4.0745 | -50.0173 | 2024-10-28 00:49:18 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f48fa6d5-221f-3767-adeb-9566028d1395 | -4.0761 | -50.0242 | 2024-10-28 00:49:18 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faae8b5e-3ec0-3172-913d-98380a2176b9 | -4.0631 | -50.012501 | 2024-10-28 00:49:18 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56b83a9e-e7f5-3101-884e-03ca5be911c6 | -4.0647 | -50.019501 | 2024-10-28 00:49:18 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5cc1215-e18c-3366-b83b-8ad6bbebe423 | -4.0663 | -50.026402 | 2024-10-28 00:49:18 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53f54e59-8e0e-33d3-a77e-459421c1e640 | -4.0679 | -50.033401 | 2024-10-28 00:49:18 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60b4c392-73e6-30e9-ad27-30eb66e3ea74 | -3.5695 | -41.384102 | 2024-10-28 00:49:19 | METOP-C | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 816e08e3-6ba9-37ed-8b8a-dc4e6a6a123f | -3.5734 | -41.400101 | 2024-10-28 00:49:19 | METOP-C | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d9a78bba-0125-3ff5-9b87-cac90a582b6e | -3.5598 | -41.386398 | 2024-10-28 00:49:19 | METOP-C | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db3dbcb8-be09-3e2f-934b-4df5a5ccc1dc | -3.5637 | -41.402401 | 2024-10-28 00:49:19 | METOP-C | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88e965ff-d6c3-3fec-9395-08ffeed07d30 | -4.9045 | -46.853001 | 2024-10-28 00:49:19 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f57cadc-590d-35ab-b4be-6aadbc6a9702 | -4.9062 | -46.860401 | 2024-10-28 00:49:19 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 805ec3a7-7b7c-366f-9b4a-b382adeed7c5 | -4.7726 | -46.374699 | 2024-10-28 00:49:19 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 199fcdd1-8b0e-3b89-a130-a80e7caf2e9e | -4.7744 | -46.382401 | 2024-10-28 00:49:19 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b144c8cf-837e-326f-b0a0-660e45605183 | -4.7762 | -46.390099 | 2024-10-28 00:49:19 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf6dd9ba-621f-3cdf-8100-a77aeeaec09c | -4.778 | -46.3978 | 2024-10-28 00:49:19 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e597dc1-6429-340b-8ef9-2662c0005a76 | -4.7646 | -46.384701 | 2024-10-28 00:49:19 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7668095f-9969-3a57-89c1-232941b9f1ba | -4.7664 | -46.392399 | 2024-10-28 00:49:19 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b26e34d2-81c9-3ba2-9a4f-18e63a577728 | -4.7682 | -46.400101 | 2024-10-28 00:49:19 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b253035-ebf6-3606-ba27-2e3bc5082e21 | -4.859 | -46.879002 | 2024-10-28 00:49:19 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c1c4f137-9813-3a6a-a994-e3091c75f2f2 | -3.94 | -49.879799 | 2024-10-28 00:49:19 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6aedc0b6-965f-3af5-9e20-a010e31fdbac | -3.9416 | -49.8867 | 2024-10-28 00:49:19 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f936488-94ff-357c-9c43-af8db10baab4 | -3.9432 | -49.8936 | 2024-10-28 00:49:19 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2df7e84f-3f7a-3fbb-a3cd-da63cd70f0d9 | -3.1725 | -46.5924 | 2024-10-28 00:49:19 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b115501-a6b8-3e23-98ae-19b2fb6f0e78 | -3.1744 | -46.600201 | 2024-10-28 00:49:19 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8451df8d-578b-374a-a9d2-c0aa4bfd1f8f | -3.1762 | -46.608002 | 2024-10-28 00:49:19 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 668345f7-589b-3913-b980-ad3a32b72115 | -3.9318 | -49.888901 | 2024-10-28 00:49:19 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac29d27-0544-3693-bc6c-520907c2d90e | -4.176 | -44.098801 | 2024-10-28 00:49:20 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec9e1342-1fab-3ef9-a4b6-593572050e79 | -4.1785 | -44.1091 | 2024-10-28 00:49:20 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 414c2bae-5ffe-3b3b-b347-d984addeb10e | -4.1809 | -44.1194 | 2024-10-28 00:49:20 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c06f0dd6-cf2c-3138-b15a-7991d160882d | -4.5764 | -45.799801 | 2024-10-28 00:49:20 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3655a21e-3191-338f-a7b1-a61b9824d673 | -4.1663 | -44.101101 | 2024-10-28 00:49:20 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
