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
| 551ca60e-04be-3525-a696-521c070d4f69 | -2.0325 | -46.3726 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d63833c7-a736-36cb-8001-37270926b33c | -2.77978 | -48.57613 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 942a654c-0840-3456-a363-8ce8fbaa582a | -7.06441 | -38.58204 | 2024-11-16 04:01:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 28be1228-047b-3710-a51b-4a4da2711923 | -3.03331 | -45.13708 | 2024-11-16 04:01:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b829357e-20eb-3965-b853-56c939553a2e | -5.00427 | -44.32828 | 2024-11-16 04:01:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee01ac59-ba15-38d8-a274-9477f542faf7 | -2.66789 | -46.19076 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b83be42c-95a0-3008-bd92-4d6f96b23eb7 | -6.30383 | -39.48019 | 2024-11-16 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 32f58cdf-b7f9-3d98-947b-a3569a590e7d | -7.55186 | -39.21031 | 2024-11-16 04:01:00 | NOAA-21 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f09ec49-825e-3615-8fbb-71051f190651 | -2.49702 | -46.22942 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5170882-2c3a-3ea6-a695-adff57ed7926 | -3.50208 | -42.00875 | 2024-11-16 04:01:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0f111fbf-bcca-3221-8b0c-1928c21eeff8 | -4.03323 | -44.10695 | 2024-11-16 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46e46d6d-833e-3afd-82f6-33a1928cf8e8 | -2.89215 | -40.02583 | 2024-11-16 04:01:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4bb59ff5-c57b-35fa-8c04-724d23233551 | -5.23025 | -43.73159 | 2024-11-16 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4183c0ce-ba44-309e-ac5d-d540473d9a71 | -3.87904 | -45.02702 | 2024-11-16 04:01:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d5a91f4-e1fc-32ea-a166-3b1da810a20d | 0.15357 | -51.13744 | 2024-11-16 04:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dd62f85-ba88-3287-85c0-8d52a3f79c05 | -3.18265 | -42.07659 | 2024-11-16 04:01:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03694034-4663-36e1-8526-0fc9ea0d2695 | -4.90938 | -44.02883 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4102d149-843f-3c84-958a-975d0e728382 | -4.37686 | -48.57183 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64954d6a-c648-3ce0-8e13-a15ec848a04a | -2.63817 | -45.97507 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 812c4ff3-7251-37f7-8888-453cd8761eac | -4.98954 | -44.32085 | 2024-11-16 04:01:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 998179bb-0cf8-3f4c-bc2e-3ef1bdb72a20 | -3.52338 | -44.71739 | 2024-11-16 04:01:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5b60cb9-3258-361a-8992-0580fb90e6b7 | -2.07592 | -46.47761 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a88d87ca-550d-3085-af68-23d8beff5bcf | -3.73727 | -45.66562 | 2024-11-16 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fe545e14-1d7f-3961-b844-aff156bd068c | -3.45037 | -40.97162 | 2024-11-16 04:01:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e2781644-7c4b-3c7d-affa-9b759a54a386 | -7.62346 | -35.09826 | 2024-11-16 04:01:00 | NOAA-21 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dadc2f96-142e-3301-b536-8abb93705370 | -3.07645 | -48.01623 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0ee88c8-d44c-3af6-acf1-016dbb73ffd1 | -6.86093 | -38.88457 | 2024-11-16 04:01:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e3082ba5-818b-399d-8847-b6ce44e4f716 | -7.39854 | -40.40103 | 2024-11-16 04:01:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b6c6e5aa-07fd-34ee-9747-e0f5a23c8e20 | -3.07422 | -48.01213 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4ca295d-1584-3f76-9798-7064f21f0f80 | -2.39334 | -46.31559 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cf396dc-4919-3962-8428-c1530abf90d1 | -5.82011 | -40.53306 | 2024-11-16 04:01:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 111bf6aa-bfeb-3e66-89e8-88ff2841ae1b | -2.95284 | -44.29551 | 2024-11-16 04:01:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8e0c9b6-e686-31aa-a3f3-629028f90909 | -4.15612 | -45.43699 | 2024-11-16 04:01:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cdd1896b-823c-3ee6-9b97-4a67cd7d545f | -4.23107 | -50.67418 | 2024-11-16 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffca0a6e-0551-31dc-9281-fe25e10a49ee | -7.18154 | -39.12355 | 2024-11-16 04:01:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 300f4835-e185-3221-a0be-be183de6b330 | -6.16606 | -41.16441 | 2024-11-16 04:01:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e41f8038-fdc5-3927-bdcb-35d89213453a | -5.58883 | -37.38209 | 2024-11-16 04:01:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a839b31f-5db9-3e38-b974-a9c593438ecd | -3.76208 | -50.78794 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e57d6a9-ca7d-3fad-8233-29747a3ec380 | -3.91426 | -45.85522 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd342954-3c1e-3b21-a306-4dd8bb95c2ca | -2.77086 | -48.57804 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0277c27c-2070-330e-b6bf-7a06bc3bf201 | -3.56204 | -50.24506 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5860537d-8688-34d9-8992-9fa6cac961f8 | -3.78725 | -43.91386 | 2024-11-16 04:01:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7ce4a4db-aabb-3fc0-8b46-6ed43f018445 | -3.18329 | -42.07263 | 2024-11-16 04:01:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cc709b8-fe1e-3e0d-a3ec-e4931cc817fd | -7.06697 | -35.2408 | 2024-11-16 04:01:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 638e7eac-7b0d-3cbb-b5b7-1ac212fe6862 | -3.88377 | -45.02395 | 2024-11-16 04:01:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b466c6ce-bcce-3934-a184-2b7377217703 | -5.32979 | -40.90186 | 2024-11-16 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b8c7c9ac-35d0-37c9-86f9-a5dc30d952d3 | -2.51083 | -47.47466 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0a46074c-36a7-3267-b512-ff3edf991e0a | -3.12605 | -45.89627 | 2024-11-16 04:01:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b162ae9-7de1-3e7a-9f09-42cfd05e402e | -4.90637 | -44.03049 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e0e999b0-5da7-3804-be5c-7c9ba7b68349 | -4.61849 | -45.34636 | 2024-11-16 04:01:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fa620e2-b69d-3269-ac50-98f789d6586e | -2.19611 | -46.34336 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df45ae59-f15a-3794-ae95-ad31f3a18eaa | -4.37761 | -45.62093 | 2024-11-16 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac72f533-0bbf-30ba-82b1-d86943c27f4e | -2.79219 | -48.56778 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0fe464d7-d9d8-382f-8062-8fad46302a8f | -3.64155 | -43.61416 | 2024-11-16 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e39717e-1cb8-3197-91fa-7e5fcd0d7c02 | -4.28131 | -48.2104 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8397a3d-70e5-3268-b28c-327ecc69ab0c | -3.28061 | -45.50733 | 2024-11-16 04:01:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 6fd22ea1-8f69-3370-a949-adc7db18062f | -4.40686 | -40.6921 | 2024-11-16 04:01:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0bbfad08-16b4-3267-8c14-0408deaa1f33 | -4.54484 | -42.97834 | 2024-11-16 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5d64ddb-27c3-3460-8540-592824d2dc31 | -4.29942 | -48.1025 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9184cdad-e107-3e8d-b3e6-1768b173c145 | -3.5618 | -50.23475 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39f57a65-7608-320b-ab42-a4199ff0a6f6 | -5.90411 | -46.2294 | 2024-11-16 04:01:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 918eae5a-df1a-3eb9-a717-6a4713dcce89 | -3.87815 | -44.49179 | 2024-11-16 04:01:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 003d8470-a3c9-3d80-8926-4cbb856fca88 | -6.98516 | -38.87378 | 2024-11-16 04:01:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 49c8a17c-ef39-31c8-b987-8ff6972b763b | -3.79702 | -40.9985 | 2024-11-16 04:01:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d5c1e000-156c-3dc6-8664-b05ce8b0568d | -5.0059 | -44.31843 | 2024-11-16 04:01:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2ff5020-a4e6-36c3-b564-2eecab5d79ef | -2.22245 | -46.35751 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57f5a4bc-6937-3890-b695-6340931461f7 | -3.69016 | -40.77474 | 2024-11-16 04:01:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 66b68375-7800-3c52-bd90-3f88843990b3 | -2.81794 | -46.65947 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e7a2d38-98bc-3a1b-8e5e-ed00abbb995e | -3.57063 | -50.25403 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e260ad72-6aaf-3e20-aac5-25688c11fec3 | -2.55756 | -46.90173 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 93d7098a-ac18-3092-bcac-669c23a1ed61 | -2.74566 | -48.56355 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fbeb14a-8fe0-3c77-8afd-bb9b3bbb3915 | -2.56237 | -46.90247 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f952bb7d-a8e6-3e87-b8c4-09b6ed82c319 | -4.15039 | -50.77069 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 044c979b-4283-3a9f-bfbd-00a003888220 | -2.94712 | -48.01918 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ddcae8da-886d-3da1-9033-dbfa88782280 | -4.99423 | -44.31661 | 2024-11-16 04:01:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e9d6c62e-b7d0-3c0c-b4ee-1975dbfaa4f4 | -4.18695 | -46.37135 | 2024-11-16 04:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8370cf10-4316-3910-ae98-e3ad6f87bfa2 | -2.15232 | -46.55364 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d37ea26-19ba-307c-9b52-9fff700583b1 | -2.97459 | -47.99344 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7279aac3-80da-362e-a236-59c06c331c62 | -3.9972 | -46.49857 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 334b23c0-90a5-3784-b80d-cb07f15143c5 | -6.64149 | -39.71437 | 2024-11-16 04:01:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 89d699f8-20d9-386d-b9d5-13986ed21b8d | -3.56868 | -50.24164 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0328a4d-0e0d-3cf2-af03-1a1c6066a4da | -5.1556 | -44.09348 | 2024-11-16 04:01:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 28f8071b-3b8c-3ba8-ba8f-c9dcfbcc77a9 | -3.74426 | -45.6499 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0cdb84ac-c4fa-3f39-a2f4-09e2bf9a60fc | -2.64961 | -46.1593 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24086262-c5aa-352e-bf40-4a511bb4093d | -6.29997 | -39.48315 | 2024-11-16 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 32894cc8-f762-3960-aba9-10c7ac749064 | -2.63691 | -46.56011 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dce4fc0a-3147-33d9-8ff1-1669767e1931 | -3.49954 | -47.21319 | 2024-11-16 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cd7c25fa-e49b-31e8-a124-0b354f80be2c | -2.45121 | -48.02418 | 2024-11-16 04:01:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28a5d679-e8ed-30df-b9f5-8068441ce2bc | -1.71319 | -46.16049 | 2024-11-16 04:01:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ca9b95b-a3fe-3e2f-86f8-df95ddd14154 | -4.00564 | -44.33257 | 2024-11-16 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f41bc16-11c2-3cd2-97c4-20e813f0deea | -1.40506 | -51.09376 | 2024-11-16 04:01:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a058401-f691-3d3e-ab26-fdc2b3e7699d | -2.61715 | -46.18351 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80a78a82-55e2-3de5-bc7c-b48d6d7263f9 | -7.58314 | -39.04971 | 2024-11-16 04:01:00 | NOAA-21 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1ba4049-8102-37b1-afe0-d6710fcb2c27 | -2.51089 | -47.47606 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 65cd1919-d2f2-3893-9264-56cdf7974672 | -2.89551 | -45.34457 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 3c0bfb07-35e9-39f9-b588-1f5d12459376 | -2.28496 | -47.91718 | 2024-11-16 04:01:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f3c24a99-9a30-3ad4-a305-08fc066a586f | -5.66756 | -35.64901 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 15.8 |
| ac69b8ad-286f-367e-a89a-2ff832a39fe1 | -2.48055 | -46.36399 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09a21d71-8812-387a-8cf1-32472fcca70f | -5.29807 | -44.89742 | 2024-11-16 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6dd66fa-df75-3784-93b0-90efa7f60a8b | -6.9435 | -40.02428 | 2024-11-16 04:01:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |


[Clique aqui para ver as próximas entradas](README20.md)
