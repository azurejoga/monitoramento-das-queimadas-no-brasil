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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bec0db0b-5b5d-384b-b839-07cb4e2825d3 | -2.7271 | -45.62518 | 2024-12-28 04:38:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f229971c-e3ba-3740-a76e-7117342cf272 | -4.29719 | -46.54227 | 2024-12-28 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f63612b8-272f-3f9c-8532-8b9d946139b3 | -3.37695 | -46.22333 | 2024-12-28 04:38:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee213512-ba2e-3c23-8cea-f82708df689a | -3.74193 | -47.1895 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 741cbbc8-b498-37a6-a2c5-5a00cccbb5ec | -3.91333 | -47.02485 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23d62fc2-642d-321f-8b54-5d053e93ecbf | -3.80695 | -46.72816 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39524f16-7d97-3561-ac8d-b4cf2749d4d0 | -4.07828 | -47.09233 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ecba575f-4eb1-3722-9790-b571e8ae068f | -3.81631 | -46.71393 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25b2d720-9fed-3386-af2c-6fa532fd5dff | -3.97335 | -46.88817 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 557edcb8-1e29-3f29-9b41-b62347621279 | -4.08292 | -46.8114 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f38e669-223c-3831-b82c-fbe01896e7d0 | -3.99355 | -46.68833 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10f0ca36-ae3f-3f4e-aded-cafbc207b312 | -2.3896 | -51.91282 | 2024-12-28 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 510cd815-206a-3b0c-9ce6-82c394c5996a | -3.76053 | -47.22584 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08e8de79-6077-33d4-92f3-5813de6abf26 | -4.01272 | -46.70306 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d43b1e37-7c39-3df5-9ac3-8dee03f86a92 | -4.83431 | -46.72728 | 2024-12-28 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 861679e0-25e7-3b7a-9b65-be1dfc62b959 | -4.34109 | -46.49141 | 2024-12-28 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cfa052b-24fd-31bd-ac93-07676c5fe4ec | -3.88101 | -46.9478 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1db4e2a4-b629-335b-8361-b61cf7fa3a8a | -4.01442 | -46.71515 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2bc5415-aaaa-3593-9d7b-ccacfdfe1a01 | -2.84057 | -48.10621 | 2024-12-28 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76d6e604-be1d-3fb0-8909-9aedde748d81 | -3.88141 | -47.01306 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bd1d991-5aa0-3949-bdef-997c6c64fa30 | -4.01562 | -46.70745 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46680524-9521-3ff2-a499-34210713f505 | -1.36786 | -46.61335 | 2024-12-28 04:38:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eabd2dde-3397-342c-88a4-dcf33b420271 | -4.0485 | -47.03419 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 891419c3-3f25-35fc-b9cc-3e62d76995ee | -4.07315 | -47.08004 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e13ec511-e31b-3d6b-abe8-290767fb95f4 | -3.98372 | -46.91271 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 860f360a-d67c-35c0-abcf-f41c99c55333 | -4.00395 | -46.71355 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92f36650-ae5f-3491-9bd2-31affe5c845e | -3.8952 | -47.0152 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57e1ca5a-390b-3438-8eb2-6da1eb6997b2 | -4.10262 | -46.82218 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86d252f2-0441-33f9-bd26-9f2e5c84b160 | -3.34367 | -50.38571 | 2024-12-28 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c8fdbcb-24e5-3657-8fa4-50dc8f1c5915 | -1.93077 | -46.43496 | 2024-12-28 04:38:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b29ecd11-2085-3ecb-95ae-c25b6f3397ec | -3.79652 | -46.72646 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14499067-355b-31bf-abe9-dee42f4db0ef | -5.90707 | -43.48754 | 2024-12-28 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d9858ae-52cc-3dc0-92b2-e2af6cffdb37 | -3.74308 | -47.18219 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44095de7-fcf7-3152-a508-cb74326e0b67 | -3.85896 | -46.67648 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 347678b1-91e0-3276-b890-de5514eeb9d2 | -4.0777 | -47.09607 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57a7cf0b-6abd-3752-8589-f7850681adf6 | -4.11865 | -46.71881 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16bbe777-e961-3ef5-9842-cff6e50cde52 | -3.9975 | -46.93805 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54f39098-da60-3f9b-836a-d3883bb3fcbe | -2.26185 | -53.88305 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f74aa1a1-0d16-3bbe-b1ec-624fce18e22f | -4.1176 | -46.6794 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f73f3346-4b3d-3c30-88b3-4a6823f34b86 | -2.28843 | -45.57175 | 2024-12-28 04:38:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a3ac624-d047-3158-8fc9-85bb5a1fc968 | -3.97335 | -46.58635 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5526f8a0-8155-327b-9b37-ec3fb66a0a6f | -3.9088 | -46.90598 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03e51851-e680-35c6-87bb-1dea27ef74d9 | -3.96738 | -46.67241 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a5e6481-04f6-36c6-9002-fd3666902810 | -3.80347 | -46.72762 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a34c2816-0243-3d12-95d5-8a1e568910c5 | -2.52546 | -44.99809 | 2024-12-28 04:38:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c28ecdc9-d881-3a21-927a-410169c78424 | -4.03028 | -46.68214 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce0d1979-8c78-34c6-a509-6fac5d410549 | -3.86363 | -46.66938 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c7b0e4c-2758-35b9-b026-38e18e3da62f | -3.90424 | -46.8898 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b849e90-3ab9-3d59-85eb-ca81057e513a | -4.00804 | -46.71024 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 652e4220-551b-3cc7-886d-f1f0da57df4c | -3.99691 | -46.73597 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c37e59e8-160f-3951-9026-942af2d53124 | -3.9013 | -47.08017 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 271682e8-6fdf-30aa-8a57-212bcbf6a080 | -1.37071 | -46.5949 | 2024-12-28 04:38:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29d0324b-0d41-3cd1-b023-a1b244f0a8a7 | -4.55759 | -44.12537 | 2024-12-28 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b31dc6e-c5c2-3a17-94f5-6e88ead6ef9b | -2.22006 | -53.64751 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58b6a2f9-5583-314c-8fb8-b18246b19213 | -3.74251 | -47.18584 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81f3d301-1a8f-36ff-8ef7-3c351da36201 | -4.11515 | -46.71831 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd495986-17e6-37fc-b4fe-37db907fae7b | -3.80419 | -46.85961 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca4aead6-6483-3bb3-9463-29049e13b9f5 | -3.19601 | -45.99241 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab9a060d-6d79-37b7-8c50-606734edf901 | -3.74196 | -47.3465 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0818a432-2cbe-3632-9e86-71ab6e5fdda5 | -3.76964 | -47.21217 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11a90b42-1714-3b06-b7e0-d9763dd21628 | -3.19414 | -45.99351 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed1816a2-8a24-3567-bedb-87961dfad7c1 | -5.31514 | -46.06242 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c005d7b-c04a-31eb-a426-a2ad90096f63 | -3.84461 | -47.04546 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83713dd7-d370-3fc6-987a-1deed07ffa3d | -3.8705 | -47.01514 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54f45306-d47a-3fb8-8255-840dc971f6ef | -3.90642 | -46.9211 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9ca9891-0498-340a-93a7-4cebaa41f0ab | -4.48756 | -45.67907 | 2024-12-28 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96bef52c-0bcd-3aa5-a35a-225a156dccd7 | -3.84403 | -47.04918 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81db275d-1166-3ebb-8594-acab652047a7 | -3.1912 | -45.99997 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0fcdb7d-ad43-3a88-a272-e69f0528d34c | -3.72767 | -47.19106 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b22ac1dc-44f0-358f-8db9-0986b9afd260 | -2.5747 | -53.99115 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09776473-5b38-396a-abe2-418f2dfac02e | -4.07712 | -47.09979 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eec4daa5-fce8-389b-ac5e-646d362c5a98 | -3.89233 | -47.01094 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0e8ec2c-9fe4-3e4f-9291-a2a919570ce2 | -3.86304 | -46.67321 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b3c122d-e089-34c2-bc9a-819ca8d03108 | -5.23365 | -41.39988 | 2024-12-28 04:38:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| cfa56c78-156b-3ea8-96dd-fc3860dc8f0e | -3.71409 | -41.69668 | 2024-12-28 04:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 02d0228c-cfb0-3f81-b286-3d2267275da3 | -3.77709 | -46.85142 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96c9a091-81d0-3191-974f-4eaff900f410 | -3.34424 | -50.38209 | 2024-12-28 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7df50f24-81aa-3bb1-9472-257be3cfc639 | -3.34027 | -50.38517 | 2024-12-28 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2ee2f35-236f-3d39-9f46-3ee35aa974f5 | -3.19958 | -45.99296 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d6a1736-9a1c-38fe-b348-b71b84607c32 | -3.95922 | -46.67896 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74fc0704-307c-3338-95ee-7e7c3fd8c3b6 | -2.22168 | -50.45948 | 2024-12-28 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1114459b-81a6-3d52-99bb-f9ff2c06f701 | -3.76395 | -47.22637 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18feee6b-315c-3478-b510-237921bcbd03 | -3.74536 | -47.34702 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 898c7183-de2a-302e-b88c-27359d9798a3 | -1.35264 | -53.52079 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 128f0b89-96c9-3356-879b-e92535510050 | -3.7271 | -47.19474 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 026e059a-0385-3932-bba1-58656976f0dc | -3.96969 | -46.68067 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ac074d5-b113-3f82-91f2-2d21b9ba9a0e | -3.02382 | -53.89259 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b48705a3-566b-3ab6-b328-eb9202e790a4 | -4.01264 | -46.56438 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e79e7377-7667-3eca-905e-47030e3283f0 | -4.00684 | -46.71792 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b400bc1-5634-38a5-8c38-a3b4fb9c9ef7 | -6.44532 | -44.37959 | 2024-12-28 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdc7ce4c-740b-3e0e-91f2-f5084ae6d60a | -3.80755 | -46.72434 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24dae4a5-5014-32eb-8a5d-25b6be3e85bb | -6.3909 | -38.90884 | 2024-12-28 04:38:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8bd702ae-1500-3b23-b531-58e1b36b3c18 | -3.91273 | -46.98281 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f1090e5-d298-3132-ab55-c762f7e7f899 | -3.79439 | -46.85421 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dab232e-02b6-3d3f-b3bd-7dc2c9e58e14 | -3.19896 | -45.99701 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f108389c-3080-32dd-96a9-470a0d97a608 | -3.44254 | -53.29436 | 2024-12-28 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ab4e8d6-78a7-37b8-821d-3cf6aa70949a | -1.15358 | -48.84867 | 2024-12-28 04:38:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d14fef2c-2569-3fbf-a5e0-1a1f47a5d217 | -3.95177 | -49.44323 | 2024-12-28 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a737a5f-75b6-3d02-ad32-9dc51fe84443 | -4.0284 | -46.91179 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4137486-f2df-3a78-a18f-a58652cb3728 | -3.74593 | -47.18638 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README15.md)
