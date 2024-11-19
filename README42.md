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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e12c4848-0882-3ae8-bbc7-03553e3d11d3 | -3.10555 | -53.74698 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce61f5ed-c65f-3b06-82f8-8347266f73e9 | -4.54186 | -48.0161 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 616d2852-8f90-3e3b-af50-b2158dccb261 | -3.22905 | -59.33405 | 2024-11-19 05:08:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a139f1e-e64d-3200-be23-fb5af16db9b8 | -2.70496 | -51.69121 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9d809d7-67e5-3cd9-8aa5-e4f0842dc3ca | -3.08532 | -54.66588 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74936046-3826-3fb5-adda-7b7474642d78 | -2.00338 | -44.8002 | 2024-11-19 05:08:00 | NPP-375D | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 50855933-f5f3-3fcc-a6a8-055f207aacbc | -3.52665 | -54.67954 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8944c4d4-24b7-3f01-8031-7bc8c2780ff6 | -2.99458 | -51.45789 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a85476d6-de4c-3290-a0e1-4f9e16edb3ad | -2.83744 | -54.01273 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2258eaef-1226-310f-8b73-15a180ba1588 | -2.4361 | -54.61981 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d886ebea-1ac2-382e-a21c-093aff55e677 | -3.77767 | -52.4084 | 2024-11-19 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2bebb18-d085-32f9-a461-996ea28bf0ea | -1.38702 | -52.00225 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 053829c1-6e2f-38d4-a703-f6d2b0ca650f | -0.84996 | -48.7509 | 2024-11-19 05:08:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e2d43102-dee4-33b2-a9ce-6a0dc9d6d27a | -3.04276 | -54.40462 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 767263e7-b1fd-3b1c-8899-d7f06ffcef4f | -4.54851 | -48.00738 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f5e6454-8cf0-3b2d-99fb-05cf3a85294d | -1.86739 | -53.19854 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2880b3fa-488f-37a3-a5b4-8c07271a41b0 | -3.10848 | -53.75151 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6ae6e6b-6199-3e59-aac8-91bd19343027 | -1.27545 | -52.75931 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5ee2836-d708-3b2d-b9e6-5baaa29e9aa2 | -2.22274 | -50.51865 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a29910b7-1f0d-39aa-9050-cccb933d2d78 | -4.54281 | -48.00971 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a8df1fa-4e2d-31d9-8e7f-ae479706d1da | -3.58573 | -50.67306 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 058470a7-b09d-3e11-ba54-32a26d3a5a9c | -4.57284 | -48.02391 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e123b49b-d2a5-309b-a4bb-8f62d860f581 | -2.28775 | -53.62947 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 94f65440-60c6-3fcf-9885-36bbbae8127b | -1.59317 | -53.80625 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 56d857d4-8802-328b-8221-3facaef675a7 | -4.55142 | -48.02394 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 65654391-8e62-317b-9ef8-53c3823ab207 | -2.76968 | -54.05046 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a3cc684-4856-3eff-b287-c54b30fd0c1d | -4.54803 | -48.01059 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 953da165-17a4-3355-a00c-f035b0b8ef8e | -4.57949 | -48.01527 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4481841-133b-30f8-bf92-523fb36d7e65 | -2.84563 | -54.00609 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af3371a5-b49a-3637-90d5-65a27f34c77b | -4.54756 | -48.01377 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56c98535-f304-3a1a-87cb-22b333532054 | -1.19754 | -51.98303 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2df4e710-3f98-3ccc-a0ae-9d924b6d3703 | -0.95714 | -51.72163 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22fafc73-5af1-3d8d-a613-cfe54c620d20 | -0.09285 | -51.393 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4548709d-e0b8-30c8-bf17-0e7e3197667d | -3.69239 | -50.11542 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 684417e8-aaf2-3e7f-a819-6d81d7415e64 | -1.92115 | -53.34822 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7603f1b-7a63-33a3-b81b-e14afd98b4a3 | -1.9522 | -54.45754 | 2024-11-19 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 58f77aee-58ee-37ea-ac8b-db0133b8deaa | -3.18595 | -53.24834 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18041fd0-43d3-3e5c-9936-5b066dd1b84c | -2.5804 | -51.72218 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a454aa73-dcde-347c-9b8e-c0c23b08054e | -4.05061 | -54.37528 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1cbe63a-97d0-35d3-bc79-3a8446826345 | -3.0531 | -54.40626 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e50e1e0a-7e13-34b6-854f-7ba5b5c9c0cd | -1.98788 | -53.13968 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f96acbf-1638-3813-be6c-93a5fea21fd2 | -3.36492 | -54.09749 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2a1df40-750e-343c-bd8e-b46bf399cb70 | -3.98388 | -49.91743 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43a1a4e2-1657-3eb6-9fdf-c480b1beaa0e | -2.40877 | -50.30554 | 2024-11-19 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a6b51b3-c584-350c-8a4e-f81711e20b11 | -3.03849 | -49.46613 | 2024-11-19 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7930dc01-66ba-388b-a3d5-4033dfb3c1b5 | -3.10068 | -53.09789 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 111f0379-1a3c-3d96-991a-1ae2790fa1d5 | -2.28691 | -53.75011 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67bfcd74-545e-3b2a-aecf-4c0bcd96e478 | -3.08647 | -54.6585 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70750c26-5b19-331c-b173-5e5452c67ab0 | -2.54173 | -47.10268 | 2024-11-19 05:08:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3691543a-2649-3a96-8537-87c0c458614d | -0.0458 | -53.2544 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8b1e912-166b-37aa-8edf-cb92fcc9789d | -2.32499 | -45.64735 | 2024-11-19 05:08:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7505e9b7-3c71-356e-90a7-ee08cb5830ce | -1.13896 | -51.68589 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 057e8615-8ce4-355d-9ca6-39ecba6d4b74 | -4.57807 | -48.02471 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78f7ce7d-c69d-388f-810b-7c13ba965f0d | -2.58908 | -51.71836 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c552e9bc-8320-3fb5-b681-7694aa03a629 | -4.0646 | -50.0063 | 2024-11-19 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b2fd582-d18c-372e-861c-bcf44bf98008 | -4.54663 | -48.02008 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 371dacbb-e50d-3f42-8e67-463ac2b7744b | -1.20862 | -51.78226 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0efdadb-9467-3957-92d8-78155305eb1b | -0.88013 | -51.7275 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 972aae0a-b2bf-3dc3-ac77-d7038ce6bd14 | -1.86676 | -53.20263 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a81c987-6dd6-3a7b-a415-29c2bf47292d | -1.21562 | -51.78823 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49ae9bc5-e6d7-3634-9c6a-7f02bc697072 | -1.14135 | -51.69614 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97134700-84af-3b4f-aa55-ef710a4dff56 | -3.1866 | -53.2441 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54ae54f7-9846-395d-bb31-8980e6bc20b8 | -2.77542 | -52.60247 | 2024-11-19 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 48230e4a-dc9c-3a88-8491-957b127fde7a | -1.20048 | -51.77407 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21afabe4-1f25-308f-944b-46810e5e46d2 | -1.51613 | -52.09151 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46b0505a-a5f3-3245-b10f-a4fbc41fb83c | -2.24274 | -53.66296 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b38783a-ed51-33fa-891b-b82fd0d8e274 | -4.57287 | -48.0238 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9075bf27-5593-3d3e-9892-a0606d952f91 | -1.06325 | -52.39915 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec4c3ac7-d57f-38ec-a457-364597eb2760 | -2.9646 | -54.16486 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fead2b9f-e535-363e-a3aa-02e865410312 | -1.20622 | -51.7721 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa5bc1d3-8bf7-399a-afdb-7a49d7143bcc | -2.77933 | -48.58131 | 2024-11-19 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7a660ac-7ff4-386e-b41c-dcda2095b874 | -1.58969 | -53.80571 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c35c4475-9492-3916-ac36-5c46f29d7e5d | -2.26313 | -51.88469 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fbeea94-5a5f-3d97-beec-62ba92464791 | -0.92963 | -51.64371 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d129a67-a450-350e-a54d-1c754b89d150 | -1.24608 | -51.61485 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f1693b8-1809-31f1-8762-b4cbc41f77df | -3.54397 | -50.41183 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 567e0ca7-8d30-3847-a522-7b28e42c36a3 | -4.56283 | -48.01918 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 987869ba-f434-3d10-9202-d9fe414cc55d | -4.0593 | -50.00357 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e083294-e909-3f8e-95b7-b8d713e9af65 | -3.34284 | -45.35908 | 2024-11-19 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6f1a159f-9312-3518-ad3f-4e96be52fb44 | -4.06072 | -50.0011 | 2024-11-19 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7feb3f80-3bdf-31bd-be11-5b42fbd49bdf | -0.88399 | -51.72809 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f3a4782-047b-3fd9-8814-7e87743fb79f | -2.53887 | -47.33556 | 2024-11-19 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6c8a8ee-15bc-3516-92ab-eb46683e777e | -3.99892 | -49.91013 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c9f66d7-2539-3aa3-9576-726ea5f20d6e | -1.79486 | -46.80657 | 2024-11-19 05:08:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 369456fa-a534-3d6e-ad80-d253416a2680 | -2.61331 | -54.53869 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a63326d1-a282-39a0-a582-99e6a22252e0 | -2.87543 | -51.47541 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34074778-696c-3e9c-9fc3-819c1f5ff4aa | -2.68781 | -51.80173 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96bd0790-932b-3d3b-abd6-cfb43009147b | -2.22638 | -51.99254 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bde92f0-411a-3c54-a4a9-e95627ceddaa | -2.57146 | -48.03674 | 2024-11-19 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6b97228-d7be-3c30-9aba-1403173cc56f | -1.92778 | -54.05835 | 2024-11-19 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0b251d0e-4066-39aa-81ca-3a258408d02e | -1.30178 | -52.23105 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 040be071-67ab-31b1-aadb-92d1de19975f | -3.05596 | -54.41058 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12a165ae-e4f5-3044-94da-0609f1767f58 | -4.56237 | -48.02225 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efc23ee0-b319-3b2a-9c35-d5ec6e6c5b6d | -2.83454 | -54.00834 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ac5b086-da80-33db-8dab-ff3f25faecfa | -3.09508 | -51.0414 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16398557-899f-3a46-af21-14e137e77076 | -4.11519 | -51.04501 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 349cba8c-e898-329f-be70-f3f3ccac27e9 | -2.59142 | -47.47966 | 2024-11-19 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd512601-41d8-306e-b420-dfb4167bb985 | -4.57421 | -48.01435 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cf2dea19-42b3-3bef-ae78-9ec77d8cee9e | -3.47932 | -53.86909 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7211ae1f-fb53-3da8-98bd-c176c35340f7 | -2.96126 | -51.45555 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README43.md)
