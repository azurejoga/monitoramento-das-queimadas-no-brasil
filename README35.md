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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fd5c1f6-49d0-3a05-9e89-b639d5afaf6c | -7.07732 | -44.8587 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65b4717c-34fd-3e7e-a790-c432ad0673aa | -9.08109 | -47.0569 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 36faf618-5f88-3ec2-89b0-f3ed6d3f46f8 | -7.25708 | -44.45592 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24ad8f6e-7a9c-34d4-9582-aa2c9932aa3f | -8.3358 | -44.83991 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b2c297e-4e91-3c22-a4f7-f47f1bcefb6c | -5.40311 | -43.43905 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 357a8671-ea53-3b7b-94b6-991131f80c5a | -7.88594 | -46.26802 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 809bdd3d-7ed7-3e47-bb2f-bb2a9cea5631 | -8.70707 | -47.8733 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| faa18b0f-3a5e-3ff0-9324-58668df63693 | -7.68732 | -44.76511 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f095e74-b411-3c16-a36c-221abc6a8c7d | -7.87639 | -46.03323 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4242be58-cd81-326a-8573-d07b6c9149cc | -4.97534 | -48.94302 | 2025-09-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e972e507-0e20-3f03-9fdf-ad86d78b67dc | -5.66918 | -43.347 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72f5df3b-30e7-3dc6-a159-c8d9833ea81c | -9.06405 | -45.7275 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69a115c9-1f15-3a80-89fa-9e3cb54ac322 | -6.19479 | -43.40182 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7230e38d-d119-3966-868e-9c2e0f30d6d3 | -4.86561 | -42.76506 | 2025-09-10 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0ba24c48-7a77-3571-85f7-bbf2ca0641df | -7.09999 | -50.75896 | 2025-09-10 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 594e5723-12db-37ab-9cd1-a2ef8d4739d6 | -5.58744 | -42.91405 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 14d73008-a549-3b1e-bd97-2953e5097ad5 | -9.04737 | -50.48225 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc7374c4-f02a-3fde-a081-a8ee7fcc1148 | -4.48985 | -42.92772 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b37a3a3e-d5b0-36a5-8c5d-86e4e492ba85 | -6.87376 | -47.88692 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efc1c805-3ef3-3914-b285-421ca7d72417 | -8.447 | -47.28006 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 325b0a83-9cec-3ff9-b675-8d85e24566aa | -6.85014 | -44.8959 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ed34b9c-a694-3aac-9934-cfff51d5114e | -6.68114 | -44.56745 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b70a0d8a-95e7-380b-8006-dbf5c3fca2ca | -4.94625 | -45.29533 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c6fbcbe1-a497-398b-aabb-0b71f0b42856 | -6.2592 | -43.40545 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 07208f08-cafb-30f5-8703-8c2b86db3e1b | -9.05114 | -50.48695 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c000f6a-4f85-38a0-bfcb-e70ad5d414ef | -5.50625 | -42.67193 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aafb7d3f-0c8f-37da-9e05-bfe2852586ae | -5.67908 | -43.34854 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35a0143f-e851-34ad-a3f3-32f1f2ea970b | -5.72622 | -43.89204 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3491136-6302-3e91-8fe6-6ae2ca79350b | -9.56664 | -48.0122 | 2025-09-10 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61d248a3-386b-3e38-a2e3-1865938b7d8d | -7.46569 | -44.93895 | 2025-09-10 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a66d800-3781-3c10-9b2a-e2c79471b0b2 | -8.84802 | -47.26067 | 2025-09-10 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7d7342f-8329-347d-9c14-4410eb9a3a5b | -7.55043 | -44.6662 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 575eb400-98fb-3751-ad37-f58fe68522ea | -6.24921 | -43.39975 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0770876c-73dc-3b5e-b526-c1b7a07cc38c | -9.21482 | -50.53956 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 803bf9d0-cf52-39e5-b045-d5a6649c9201 | -5.9644 | -45.80385 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5564156e-74f3-3341-9621-aa30b8c82284 | -7.87416 | -46.02495 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94adc18d-1c9f-3822-9c63-e94493ee5462 | -5.39211 | -43.44441 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 658ae74a-d9dd-3559-83ea-ec7f06c78a85 | -13.64623 | -46.98177 | 2025-09-10 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3172c02a-b102-3c0c-b999-a0f74bb3d8c9 | -14.53781 | -48.76735 | 2025-09-10 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c8d1c1b-7680-3042-a7d2-404d553ed714 | -13.18921 | -47.25624 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91fda517-89ed-3a2b-bb4a-5ecc8191272a | -12.18051 | -50.62737 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb86f6aa-d946-326d-88d8-6c9ced37d377 | -11.8196 | -46.75768 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a3bb574-7550-36c5-a2da-05265f4fc6ff | -20.94343 | -46.2734 | 2025-09-10 04:17:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0a61b1cc-33e9-3e20-a978-070044e877bb | -14.93305 | -55.93657 | 2025-09-10 04:17:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 206035fb-66e2-31d3-be2c-e5438b2481c3 | -20.45192 | -45.55236 | 2025-09-10 04:17:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 156587d5-1b29-3c7b-94ca-1f7f9b0eb55e | -12.08512 | -43.33167 | 2025-09-10 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ef379fe-0f83-33d4-97b9-d11702a3f182 | -11.81679 | -46.75321 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e3d8637-4a78-3320-881c-6de3608ee18a | -13.64894 | -46.98658 | 2025-09-10 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b1199db-4f2b-3b9f-84d1-cac4d88ca8a6 | -15.87584 | -52.20314 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 701492a7-c2d1-38ba-93aa-3e5bf26e01cf | -12.18386 | -53.87873 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bbe7385-46cf-395f-89f0-975c4df21a65 | -13.90549 | -47.97098 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2eec4e5-c65d-3523-b5b6-d6d646abdbc0 | -20.12649 | -47.68836 | 2025-09-10 04:17:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51861be4-2e08-3772-9670-496afae81b52 | -15.1494 | -44.02736 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba25d607-cfb8-31d1-bb65-5adb7c21b478 | -20.74691 | -43.48455 | 2025-09-10 04:17:00 | NOAA-21 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36c9e42c-ccfb-35a4-8af6-bde0e826f5d2 | -11.21274 | -54.98592 | 2025-09-10 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 093c0591-2568-317e-9d41-867075c306f9 | -15.48021 | -49.36507 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90e840ad-40ed-3a24-8049-e6ae9b577700 | -23.3912 | -45.9636 | 2025-09-10 04:17:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fc914358-17e8-3c21-9442-fd58363341ee | -16.88312 | -45.75013 | 2025-09-10 04:17:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff70e613-00a6-36ce-b87b-63f82015ed50 | -14.79268 | -42.72564 | 2025-09-10 04:17:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5f62709-66af-33e8-87f1-56627e237364 | -15.47564 | -49.36911 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f828dc5f-3176-3865-bfc9-9387837bce0f | -19.95158 | -49.27346 | 2025-09-10 04:17:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 46562c6e-2665-3336-bd9b-853904c08668 | -14.09613 | -42.09337 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ba5174f3-cb49-3bf3-8c6c-3761a1d5240f | -12.42096 | -47.80336 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33725c38-82f0-39b9-b4bb-129417d92b18 | -10.55014 | -51.50677 | 2025-09-10 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 989b00d7-e5d8-37c6-9ecd-da3bcdb69ce1 | -22.61666 | -47.42722 | 2025-09-10 04:17:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 342bcc69-8466-3f0d-a4b4-ec1d2351817f | -17.74633 | -44.4801 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbb52aef-c457-3582-9125-f0734ad73a91 | -20.54986 | -47.61816 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a664383-9c2b-3724-80f3-9b9bbe9e1848 | -11.21168 | -54.98928 | 2025-09-10 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e3ebb47-dd00-3a0a-a8f8-c670164029a2 | -13.64557 | -46.98571 | 2025-09-10 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9549855f-fcae-37bc-980a-5d62c001bc4c | -12.18119 | -53.86441 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ba72bc6-f624-3197-a22d-8b526e7a955b | -21.43211 | -48.91372 | 2025-09-10 04:17:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79a8707d-73df-35e4-a87a-fb8f64e30203 | -10.55656 | -51.49802 | 2025-09-10 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f0ce0fb-7a0f-31ea-9d3c-f9028562b212 | -9.99136 | -48.56676 | 2025-09-10 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91649b1c-e8c1-30c9-96e9-4d1e5df44db1 | -17.25617 | -46.76358 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f18fdcf8-42cd-3d12-bcf0-2699a5fbe503 | -13.97119 | -48.23929 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13ac4895-dfef-3b44-a9e3-d5a9fd2f726e | -10.00971 | -48.08313 | 2025-09-10 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| adad44d4-69b5-39ce-807d-2eedd26aa7e3 | -17.30738 | -46.76096 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa4e4a6d-820f-34ef-b287-11bf6049454c | -23.19745 | -47.34752 | 2025-09-10 04:17:00 | NOAA-21 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8911301d-2086-3744-9cd4-65f788df3cc1 | -11.9465 | -51.04473 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c12fe3a2-4ea6-35b5-97f8-c231b380a851 | -15.10004 | -50.08067 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 89ae514a-149c-3719-af79-9f70d7481309 | -20.52226 | -47.64009 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 146deaab-d7c3-3f89-997d-0f599ed20421 | -15.01213 | -48.02249 | 2025-09-10 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bd97ae1-19d9-314a-b504-1d61cb27e072 | -12.18581 | -53.86878 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e38b529-f797-3156-9f08-72f1d4ca95a1 | -13.96443 | -48.2262 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e938d7bd-948a-3cb7-9ffb-7de2eaf91f2e | -16.88474 | -45.76144 | 2025-09-10 04:17:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5769451-1c2c-3d34-b863-aa65f4216b10 | -10.01868 | -48.09877 | 2025-09-10 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 36a5e21f-8d20-38d2-90d5-a1981d1cbf75 | -11.44041 | -43.63626 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 819c189c-27de-36cb-8fbb-4be3709d9d92 | -11.67173 | -46.89367 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71713d1b-dee3-3bd6-9c13-225907988244 | -16.46535 | -50.67162 | 2025-09-10 04:17:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 125a341f-8e1e-32e8-a1da-e672f1b7b1d4 | -23.36059 | -47.19667 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 12ab5381-6424-3af6-a33f-a230739d123f | -14.90017 | -50.11486 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0b6c4688-b935-3d39-8368-70ef1be15f90 | -13.90333 | -47.97791 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 111f05a2-8fbf-3d81-b61f-cdf7dfc4df0c | -13.96625 | -48.22498 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 03f4f08a-eb59-39b4-b0f5-57a308e2607d | -11.89466 | -41.61938 | 2025-09-10 04:17:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 48966c50-c733-3777-a677-88455a4ed737 | -13.02367 | -48.01831 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01fd1ce2-6911-3380-a812-65ef1a1b7a8f | -13.20343 | -43.37491 | 2025-09-10 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 44780f1a-587c-3a36-93f3-700c9f89983d | -10.57961 | -52.04483 | 2025-09-10 04:17:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cc08f86-4359-3711-bf59-7b69232f9060 | -17.31152 | -46.73536 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c2023c0-becd-373b-96b1-96eca777f464 | -11.80181 | -46.76371 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1006ab0a-4d23-3b47-b916-2b976a9ffbba | -10.51929 | -49.80063 | 2025-09-10 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README36.md)
