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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bb25a14-21f7-3434-bb71-e628427257db | -10.66845 | -45.97862 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| d160cf78-2d29-34dc-90f0-58a644c550c1 | -10.66716 | -45.95298 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 247.0 |
| be3f480e-2702-39a6-a84d-43741eb2a2b3 | -10.66605 | -45.95966 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.4 |
| a48ac6ca-7682-3a7a-bd8a-d710e26dccae | -10.66484 | -45.93354 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 709adf75-f3e6-39fc-855b-b308f894f860 | -10.66359 | -45.94023 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.1 |
| 36c381b2-b1fe-387c-bdc6-fba33e8362d2 | -10.65684 | -45.97376 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 04109c9e-3d9c-3137-86be-5596a0af8d07 | -10.6559 | -45.85852 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 61e68da8-faa9-3b0d-9863-06f42cd5d866 | -10.65456 | -45.95445 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9ac74372-ce26-39c3-b675-918e4f58f726 | -10.65404 | -45.86487 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c8a5e996-bcf9-3e05-a6ca-6dfe66db6952 | -10.65345 | -45.96112 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 8818b505-516f-3707-a555-ff9b055b3f55 | -10.65172 | -45.84657 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| e64b259c-fb5d-38ce-a18e-9b52a14bb569 | -10.64017 | -46.06075 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 98563a4d-f9e6-3d80-912f-0ec885773076 | -10.63771 | -46.04086 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 7e028579-8443-36f9-9b1d-196797bb6940 | -10.62988 | -46.08199 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9f1b11ac-d680-3660-afc0-29d1caf1fb2a | -10.62747 | -46.06229 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 43dc3872-2472-36cc-9845-71287689e9e6 | -10.61713 | -46.08331 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| df5efaa7-e17f-3870-a309-54f122ea0969 | -10.61475 | -46.06362 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| af4599a4-849f-3c8b-b1c5-8f22d244466b | -10.58473 | -46.02775 | 2024-09-28 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 383057bb-1b17-3482-a961-6f8824cb9aa9 | -10.28288 | -43.57243 | 2024-09-28 00:24:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 35aa39be-a9da-3753-85f9-026da960387e | -10.2725 | -43.57375 | 2024-09-28 00:24:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| e576cb57-7691-38fa-a87b-c8bd54092c1c | -10.26607 | -43.58033 | 2024-09-28 00:24:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 3978ec51-8a38-3d1a-82e2-c1ae307d2f56 | -10.26369 | -43.58746 | 2024-09-28 00:24:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2721d3c8-255d-391e-8953-77ea622fdb16 | -10.26213 | -43.57508 | 2024-09-28 00:24:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 6606adbc-3820-3e79-95f3-0f398a60042e | -12.17179 | -47.98426 | 2024-09-28 00:24:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 15918334-b1b3-38ff-a57e-96b53a2f1d87 | -10.95773 | -50.15338 | 2024-09-28 00:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| c24f03b4-c6c0-31b8-89f2-f6a4de6cd9e7 | -10.95336 | -50.11204 | 2024-09-28 00:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 43319e14-78a0-3812-84fb-906fae6c709f | -10.95209 | -50.11895 | 2024-09-28 00:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 87d99203-404b-381a-a894-caab7b975154 | -10.89451 | -46.43004 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| be4f6e18-4494-3548-a43f-6d5423fd011a | -10.89188 | -46.40877 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 20a88fc8-88de-3bea-9eea-4979b7a4dea3 | -10.89183 | -46.42392 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4c806677-5aaf-3c25-b1bd-e3bd004bc724 | -10.88935 | -46.40255 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 8c4fa13f-525c-3445-bed0-646dfab98f05 | -10.88135 | -46.43141 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| c77d8b86-3c63-37a7-96fc-18fbdda8818d | -10.87879 | -46.4105 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| f7220af6-49bd-3721-8705-b85994f3e3d4 | -10.87868 | -46.42539 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2a5154d5-b215-32e9-a6cb-d035b3a63a9f | -10.58703 | -46.04703 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| e82b3d16-6325-380a-bf25-158e065be14b | -10.58657 | -46.0526 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 3d9dae74-2189-3faa-a0a8-0821189af1c1 | -10.58413 | -46.0333 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| d99e5b63-8eb7-3b6c-a1f9-8dd4cca2d29c | -10.58134 | -46.11342 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 5ab25f03-18c6-3f44-b41b-0a04e2847d62 | -10.58134 | -46.10793 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 564e96ad-a99d-39dd-9b8f-b110227a6f0d | -10.57904 | -46.08831 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 91e4335b-93ab-38fb-9204-8ba331073c66 | -10.57889 | -46.09387 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 1bf6e52e-3309-3e2c-b658-304f52ac7334 | -10.57436 | -46.04861 | 2024-09-28 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| b68b867c-5f60-357b-95ea-7edf4f70538c | -7.89407 | -44.62987 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| d9f20e14-1fff-37fd-8934-e6df6446c50e | -7.89228 | -44.61632 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| bf6aed85-0036-3776-88f7-a019e058cfee | -9.12841 | -43.15882 | 2024-09-28 00:26:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| bb6cac33-d34e-39dd-95b2-59d218c97b73 | -9.12696 | -43.14767 | 2024-09-28 00:26:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 77e1b1ba-049b-3ce6-86b4-3c56284e9964 | -8.8363 | -45.09005 | 2024-09-28 00:26:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5db4941a-c533-36af-978d-e875718ba44d | -8.39901 | -40.87199 | 2024-09-28 00:26:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 6d0dc0af-6eef-3c74-8047-1d4126fc1eaa | -8.07574 | -42.91211 | 2024-09-28 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 187a07a9-585a-388c-a5fb-63386980d3a0 | -8.07155 | -42.88026 | 2024-09-28 00:26:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 52585d1a-98ee-3d65-bebb-5434a4136e10 | -7.9827 | -43.91266 | 2024-09-28 00:26:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 67b5e2c4-0460-3243-866a-e8eea7224da1 | -7.89897 | -42.67316 | 2024-09-28 00:26:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e0871cb3-9c58-3342-8d42-547494f26bf8 | -7.89052 | -44.60292 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 85f1ee47-2301-38f2-8555-3bf1c12be76a | -7.88148 | -44.61776 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 6a695283-d022-3d48-817b-d5ad5a383a68 | -7.87972 | -44.6043 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 869f008c-5916-3fc2-a704-dc88d173bebe | -7.87068 | -44.61921 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 70d80475-74a9-33aa-8261-2810c1729c91 | -7.86892 | -44.60568 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 372.4 |
| 39cf7f05-e5ef-31d0-9162-67201ba5dd4d | -7.86721 | -44.59249 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9663e0f7-2c6b-30c8-8c62-d7c0999ce73b | -7.85814 | -44.60715 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f268731e-28a5-3432-ab19-4a777dd05503 | -7.8047 | -44.90342 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e362df45-6be1-3fcf-921a-3649f2b3fed2 | -7.79748 | -44.67647 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 68c048ed-c635-3072-8b7d-019f5cc44daf | -7.78665 | -44.67799 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 57fe2cab-56cd-3a62-9e58-60e7e9208e92 | -7.78487 | -44.66432 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ca9cd56a-4a9c-30eb-8a1f-4cf0a26a4b54 | -7.77406 | -44.66587 | 2024-09-28 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| b50d4353-dc7c-31c8-9c2f-20ba77f50af4 | -7.387 | -44.10928 | 2024-09-28 00:26:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 462a67b4-72dd-3f25-87e8-dae16d698ad3 | -7.18852 | -41.77902 | 2024-09-28 00:26:00 | TERRA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| fea430dd-c701-3778-8f87-244afaf9a21b | -7.37341 | -44.08625 | 2024-09-28 00:26:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 09f71e2f-a2f3-36fa-85d0-d81d5ebf0725 | -7.14336 | -42.52826 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| afe2bc0b-eaef-3e2b-a34d-63e54b46d3f3 | -7.13136 | -42.50971 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d7d963f7-0722-3180-a6ec-9d0269ee1f6d | -7.12772 | -38.78168 | 2024-09-28 00:26:00 | TERRA_M-M | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| fb15b7a1-a073-3006-96f9-28c89dcbdbe1 | -7.06448 | -42.0853 | 2024-09-28 00:26:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| eecd9a3d-3638-36c7-8ada-d423691a97c0 | -6.943 | -39.41943 | 2024-09-28 00:26:00 | TERRA_M-M | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 3941509b-d3a2-3684-9448-cd86f9fa726f | -6.7208 | -43.55997 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 57d0d749-f041-3c23-9c26-9618848fb825 | -6.64166 | -42.08804 | 2024-09-28 00:26:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d55b54cb-1f4b-357d-8982-1c2118459ffc | -6.63749 | -43.85416 | 2024-09-28 00:26:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6b7aea70-013b-3936-a6b7-84713bd87603 | -6.62871 | -42.06123 | 2024-09-28 00:26:00 | TERRA_M-M | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| ad5bf2e2-9867-3f5a-8040-2e7c894e65b1 | -6.62829 | -43.86119 | 2024-09-28 00:26:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 77fab357-39d7-3cc6-8314-4dc3a8566d43 | -6.62747 | -43.85559 | 2024-09-28 00:26:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2c92d584-efe9-3f14-b144-7a58ebacfabb | -6.62742 | -42.05184 | 2024-09-28 00:26:00 | TERRA_M-M | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 504c955a-0b1e-3dc4-b1a7-02a3bcb671f7 | -6.62674 | -43.84982 | 2024-09-28 00:26:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b7ea21d1-d3e1-3a7a-b0a1-40b3390a161f | -6.61737 | -39.59358 | 2024-09-28 00:26:00 | TERRA_M-M | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 236d0819-e1ac-32c8-a9dd-4d21e6ba0836 | -6.55562 | -43.16014 | 2024-09-28 00:26:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 671ba12b-9e29-3792-99ef-264da4e53979 | -6.55422 | -43.14966 | 2024-09-28 00:26:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3a20217a-f0aa-3f55-8ebd-57820699c0fa | -6.40679 | -42.91997 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 086b7922-a6d0-3829-8f1a-f4002f5ea816 | -6.32946 | -42.4962 | 2024-09-28 00:26:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 390616b2-5861-3ffa-9aaa-f24748a824b3 | -6.32568 | -42.60631 | 2024-09-28 00:26:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| c437ebc6-c4af-3707-a6b7-bb1f7039ba28 | -6.32434 | -42.59653 | 2024-09-28 00:26:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 41a79cc1-8351-3def-a26a-f5604e46cfdd | -6.31547 | -43.42744 | 2024-09-28 00:26:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 44b7180c-a597-3fa6-9741-51b049efd3b3 | -6.31406 | -43.4168 | 2024-09-28 00:26:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 2149e668-4aa3-3133-8bbf-d273f8efcf7e | -6.3097 | -42.48917 | 2024-09-28 00:26:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 84b021b6-242f-38b7-9755-12bef4dcd036 | -6.30047 | -42.49046 | 2024-09-28 00:26:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| dad34a2f-546a-3221-9d62-bee5da9dda68 | -6.28198 | -42.56249 | 2024-09-28 00:26:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 662e182b-2478-3b46-a6b5-7e1e41cd9f25 | -6.28065 | -42.55254 | 2024-09-28 00:26:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 7007cf10-0f5d-32a0-bfb8-251de7aabf79 | -6.20334 | -43.27612 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 49865d1b-2302-361d-b6f7-7ce5b3d434cd | -6.1753 | -43.45856 | 2024-09-28 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7f22fee7-6b22-3816-818f-cc8352e329b9 | -6.1738 | -43.44755 | 2024-09-28 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| e4a607c5-1cfe-347a-9878-83b74de8ad78 | -6.17236 | -43.43695 | 2024-09-28 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 61cbeb05-b6b0-3175-879d-7caa88b4d0a4 | -6.16414 | -43.44914 | 2024-09-28 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c924dd69-7f27-33cd-b13e-f9c6427f0ce6 | -6.16268 | -43.43834 | 2024-09-28 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6076af0a-b2e2-3ea5-b9a8-e53f355f9df7 | -6.01368 | -42.34354 | 2024-09-28 00:26:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |


[Clique aqui para ver as próximas entradas](README14.md)
