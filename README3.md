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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce708e4d-b762-3d5e-887e-e5333f0b05ad | 3.94017 | -60.96399 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c16a88f-a225-3fae-b417-17ca60e1a021 | 0.64317 | -59.99922 | 2026-03-23 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ff7da3e8-377e-3d87-94bf-56440be91b78 | 3.54458 | -61.81341 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67b2611d-9305-3162-9daf-6bd1698948f0 | 3.54179 | -61.81749 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f85573d9-26ad-374a-8f48-087b992a4c8c | 3.57206 | -61.71819 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac6fc9ee-09f1-314a-be2b-f9b89ae11ca1 | 3.23681 | -61.19825 | 2026-03-23 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab50e95f-051d-30ef-b68d-2f2aedeed800 | 3.4997 | -61.37877 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be3ba08a-89db-345a-8bf6-38086f849915 | 1.13488 | -60.08566 | 2026-03-23 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fafa7d2d-50da-3065-bc25-bb6d5941aa10 | 2.65215 | -61.30375 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f169346b-f881-3223-ae09-657e9dd1aa03 | 0.73552 | -59.60645 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c275c46-0827-3d05-847e-5855727ff63a | 3.5119 | -61.38846 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f574fde-de15-35d3-97ee-f395ba4b3818 | 2.64633 | -61.28944 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d0ebe2e-17a5-337a-b965-c53fc45f9e00 | 0.59105 | -60.21122 | 2026-03-23 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc6fc3d1-abc7-34f8-bd37-638bc1bd778c | 3.93956 | -60.96024 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7d5ee06-b2dc-3ef9-88cb-34ae4e4f1f8b | 2.65319 | -61.28833 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b1b77bf-0fec-355a-bb45-8fa55eddcebd | 0.98112 | -59.37916 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b6d6f3a-ad0c-3174-a1d8-8fd25fa35eb2 | 1.89687 | -60.62847 | 2026-03-23 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7780868a-5800-3de9-aefe-d04592bc4abb | 0.57901 | -59.90928 | 2026-03-23 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8dc406fa-6cf3-3f56-a6f6-1603485fe7eb | 2.33198 | -60.39114 | 2026-03-23 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf76fa2e-965b-3a83-984c-f897ec797443 | 0.73439 | -59.60448 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab1f997a-c9ad-3659-be4d-dd9b98e699e0 | 2.64187 | -61.30537 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b29dc82-0605-30d1-9d81-32af8603980a | 3.92326 | -60.92456 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b57fef52-db15-3f66-ad5d-65cdaaaac27d | 0.77349 | -59.86857 | 2026-03-23 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c1a2e77-cf21-3ca6-9823-f7bda1f43e0f | 2.64873 | -61.30429 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 757a4762-29c3-35e6-9534-013c2b943ede | 1.13856 | -60.08509 | 2026-03-23 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c0040fe-65f6-3fa7-84b8-b5cd588329f6 | 0.72289 | -60.28891 | 2026-03-23 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81f3ded8-ef3b-3a81-9fa1-b1efb78ce2ca | 4.37715 | -60.76733 | 2026-03-23 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d3d111d3-df7d-3d8c-9887-d2e1a375462f | 0.85012 | -59.98826 | 2026-03-23 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75299198-4557-3b9e-b5ec-d3b8f4d2192c | 2.0612 | -60.21366 | 2026-03-23 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9277d38-746d-3c29-9a31-86da39ea35b6 | 3.53843 | -61.81802 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fc09a4d-369a-380c-a026-3ef6eeeb578d | 4.3755 | -60.77905 | 2026-03-23 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 562e1191-4802-3b13-b9ab-6d2e34736019 | 1.1374 | -60.08723 | 2026-03-23 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8dd8c0b0-8841-3ddd-afa6-0554a8862152 | 2.6441 | -61.29741 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4591058-f128-3f2b-b2a0-99ce2638215d | 3.12009 | -59.99837 | 2026-03-23 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd058d5b-2587-3b93-8404-c6a7ba0acde2 | 2.43175 | -60.4055 | 2026-03-23 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e9c2117-4c1a-33ad-8268-87be9def0e54 | 2.94839 | -60.74715 | 2026-03-23 05:46:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daf1f120-c982-34bb-a760-de570405b0fb | 2.12263 | -61.22389 | 2026-03-23 05:46:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f26dca91-911f-339d-9b0f-c65e6126e282 | 0.57408 | -59.90788 | 2026-03-23 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f53ea10-1906-3260-aebe-0c681693357d | 2.65036 | -61.2926 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e1f3f95-3a23-31dc-b3ed-407c55e118bd | 0.82879 | -59.40029 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b807e597-0de4-3c8f-9329-22856ab5e3d1 | 2.65155 | -61.30002 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d33d96b1-6141-3439-a6ac-4384af37c6ca | 2.64813 | -61.30058 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f07833f0-f149-3a8f-878b-fd038829053f | 3.23339 | -61.19879 | 2026-03-23 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93173a01-236d-3c32-9664-8e4bd0f16f3e | 2.23776 | -60.29287 | 2026-03-23 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6612a332-01fa-3527-9de2-ba58a349cc30 | 0.98262 | -59.38863 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a7d1610c-baa6-3aa3-b515-1606111e21e2 | 0.98496 | -59.37855 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1aab91d-d0b0-3a9e-9d98-4cbd1a605b49 | 0.61377 | -59.76513 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f0ba4f7-6bdc-315b-b278-1968ad9fa65c | 4.65972 | -60.65578 | 2026-03-23 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1ff8db6-1bb3-31e6-b9d7-8bab7689eb17 | 0.57526 | -59.90988 | 2026-03-23 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f26a5ca8-f788-3e5d-835e-bb26f1bd5c3f | 1.08713 | -59.24296 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8352a0c-b616-3032-9e93-2da7e92f87d9 | 0.6145 | -59.86697 | 2026-03-23 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea2483cc-f4d3-3813-bca9-c90603147c04 | 0.98187 | -59.3839 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a03a45e-fa08-399e-b635-b02e2c752d8b | 0.98571 | -59.3833 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36707a68-97a5-3408-b428-431e99bb928c | 0.98955 | -59.38269 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f77bf3b-0095-37fc-845e-a9bf262fddeb | 3.5153 | -61.38792 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 720d7898-78a4-373d-96f6-e5a8e50c4c38 | 2.65378 | -61.29203 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa7adaba-147d-39b9-8344-0929676e44a9 | 2.6453 | -61.30483 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f156af8-626b-33a0-afe8-3646a20c8809 | 2.65095 | -61.2963 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 981a4d9a-6264-3bd7-9a77-3bcca2130c3c | 3.51104 | -61.38442 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8e022ab-48b8-377d-8f60-8f8971c6bee0 | 3.23398 | -61.20249 | 2026-03-23 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ee384ae-cf8b-3e9e-9ce1-a818669c5b88 | 0.9888 | -59.37793 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8934e6c0-b39a-36b7-821b-bbf775a7844c | 0.95913 | -60.23051 | 2026-03-23 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a5c463b-0588-3c43-a0c0-770b8fa08c88 | 0.98646 | -59.38803 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c94ad87-3205-3917-b1b9-ddfe524a6270 | 1.13671 | -60.08293 | 2026-03-23 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c5e8b81-45a3-3e35-a230-f05940a76f68 | 4.66016 | -60.50347 | 2026-03-23 05:46:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b1449b1-2903-3ed1-a085-1e481acc3d70 | 2.63784 | -61.30219 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 370efca5-b876-393a-a5a7-da1e587a31a4 | 3.51131 | -61.38482 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a19dada-7083-3f51-ab79-6216d3949c0a | 3.943 | -60.9597 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf548b89-710c-31c6-b0f2-d1f0f011ed43 | 3.93493 | -60.95333 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f68f045a-bdbf-310e-ad9e-69086131bb93 | 1.13372 | -60.08779 | 2026-03-23 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f08a1b0a-b2c8-3a37-b11c-16b70f0de20a | 3.51162 | -61.38806 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e46037e4-1a96-3fd3-b471-6cac1cc3883c | 4.3749 | -60.77531 | 2026-03-23 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9627a640-9b54-34e8-b984-3d6a679b7507 | 0.54938 | -60.25746 | 2026-03-23 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b5dcbb3-27d0-3450-956a-4b48e52b9625 | 2.96921 | -61.64701 | 2026-03-23 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ead3ef1-569e-3ed2-b019-a417f446e79f | 0.77667 | -59.87037 | 2026-03-23 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d73dca36-bbf0-369a-b341-739da44ad9a0 | 4.92424 | -60.54563 | 2026-03-23 05:46:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44592033-4b45-3e01-a13e-53621e00cf2c | 0.77723 | -59.868 | 2026-03-23 05:46:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb1ba62c-886e-399b-b64e-c1117110a23a | 2.64127 | -61.30166 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9845125a-2761-3195-893c-9fb7289efbb2 | 0.74987 | -60.55528 | 2026-03-23 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce0e5528-36e2-35aa-9e01-8e160f833515 | 0.69414 | -60.08126 | 2026-03-23 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b777792c-36bf-3d3f-86b1-55c890f71bc9 | 3.1924 | -60.24236 | 2026-03-23 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 557644c0-8b15-344e-8591-b64807e96a44 | 2.64753 | -61.29687 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 038fe760-72fc-3a21-a07f-5da85bdd5e3d | 1.97514 | -60.57104 | 2026-03-23 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72e2ab75-cf53-3c9f-a1bc-b408ce1d0e8e | 3.50309 | -61.37823 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b13fba7-ec77-3dd1-9ef3-bdec535bc777 | 3.9406 | -60.94477 | 2026-03-23 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f9e555f-5459-38c1-b2b6-f6d97c7ecc42 | 3.1237 | -59.99778 | 2026-03-23 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01ad1e03-fc3a-3ba5-92a8-e51acafa82cf | 0.59474 | -60.2107 | 2026-03-23 05:46:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28b7627e-efe2-3100-877b-f7d3865ce111 | 1.3551 | -60.0251 | 2026-03-23 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20292aae-4679-3a34-b168-5599736a144d | 1.27298 | -60.51339 | 2026-03-23 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.7 |
| aa242af9-835c-30c8-91e6-a39168623b80 | 1.27658 | -60.51281 | 2026-03-23 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8532d71b-334a-3085-ba94-b280db27110b | 2.94777 | -60.74331 | 2026-03-23 05:46:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 161dc6d2-ada7-3aed-a8f4-a99656717b97 | 1.94832 | -60.96969 | 2026-03-23 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d191fd0-bcae-3523-8cb6-15b117ed07b7 | 0.61755 | -59.76455 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c44fdeca-a31c-3328-b932-309433bb1ff3 | 2.11917 | -61.22443 | 2026-03-23 05:46:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c935a9a-a545-332e-9caf-2306ef64f52b | 3.24347 | -60.29305 | 2026-03-23 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c37a325b-e1dd-33e6-a860-fddf411f7b67 | 2.6447 | -61.30112 | 2026-03-23 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc3954ae-a508-3000-86a4-bfe629f6e073 | 0.9903 | -59.38743 | 2026-03-23 05:46:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ce4edaa-602d-3de8-a8e8-9e1d95f4f1c7 | 1.9738 | -60.5683 | 2026-03-23 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 109f0b74-b1b6-3dd8-a742-bf693dc408f4 | 2.3167 | -60.54573 | 2026-03-23 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c328bee1-2d67-37ca-82f7-7cf1cda4d0d2 | 4.37775 | -60.7711 | 2026-03-23 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README4.md)
