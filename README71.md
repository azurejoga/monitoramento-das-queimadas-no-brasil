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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f2ccfdf-4adc-3bee-a34e-8e68a6ad90f1 | -3.59042 | -49.98663 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24ec5792-b1e9-3d74-aa72-a9695e3b876b | -2.61313 | -49.2543 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c483dbf-0252-3811-bb2f-c8f27e0d9bc4 | -2.32413 | -49.07854 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db2d64eb-542f-3b79-815d-2b25ddda05a4 | -3.67631 | -54.44955 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 390b0249-a5d3-3e7e-816e-0f3175f25101 | -2.51794 | -48.18612 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bb3956c-681b-358a-8ed2-a105381574e6 | -4.07122 | -46.68336 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dad16722-57b3-3b34-99c9-7e614344a196 | -3.38689 | -50.1531 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d824bffd-d8a7-3c49-a8b8-377dabb0a46b | -2.09358 | -50.35435 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8353fc68-6c11-3959-b455-a21ddeb47cd5 | -3.81036 | -46.68838 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 272a32a4-ac49-3a58-8905-f21b0b726566 | -3.03729 | -50.98113 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 619dc472-0532-3b24-8d70-6ce53dfeb884 | -4.67637 | -46.3697 | 2024-11-30 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f5f7426f-b836-30c5-900a-4e87604d9e3f | -4.22894 | -46.05605 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75d89640-b93b-31c0-8c17-ee4a4859c28d | -3.33569 | -53.21823 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 394a303f-b779-3e16-ae1f-ebf4d005eaaf | -1.20108 | -51.75864 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eafdec3d-bf20-39da-b01f-82806a8601ac | -1.25718 | -54.54443 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36047fad-c66a-32d1-baa2-4eb131085883 | -1.32926 | -55.85217 | 2024-11-30 04:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2d1a9b65-6a91-3db2-99dd-929eac71a603 | -4.83725 | -41.29775 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 60fbd982-5776-3b17-8ed1-4b8cbe4c2875 | -4.08059 | -54.56319 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90226751-00a1-3f88-b2ca-bf1a8d5dc8a4 | -1.65668 | -52.72836 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17becd52-0143-37c2-a2e5-e94d870b84a9 | -3.02345 | -54.02411 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f6ae31c-ef2a-3fd4-bac1-43786ad6aad0 | -3.53024 | -51.47998 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d210d8c-faca-315e-92c8-d6f013bc3c85 | -2.44965 | -50.36493 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f28814be-bd94-3de0-aebd-a4fffa85bb4f | -3.37677 | -50.72025 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12b594ad-2907-3b1b-a474-d1d0637d61c9 | -2.71674 | -46.20734 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 902c78b6-1938-38ca-9332-5e140cc7b00a | -1.39145 | -51.59188 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 62fa8a70-8a5f-3ea2-877b-919b2fffbfd7 | -2.67223 | -46.61508 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30d63732-138f-35eb-ac63-ef30f4319179 | -2.90607 | -54.18296 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ead42004-0a76-3273-b7e9-b019b7779735 | -4.17792 | -48.62172 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9358c87f-a9aa-369a-b47f-dfa311ce3846 | -3.74622 | -53.39153 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51a10d6d-1747-3087-aa2b-94591838ab82 | -2.22556 | -46.40142 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e149b95f-4342-3f75-ac0c-f8b8f3b47592 | -2.66947 | -46.13675 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ecccac9-43aa-3987-8356-f96008fc7b0f | -2.76546 | -55.33797 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4821191-0518-3a7a-9d62-3b70125e246f | -2.67853 | -46.10153 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90642183-05cd-3c15-9fda-74f2d36eeb8c | -3.24615 | -50.77068 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e321c6e2-110c-31ba-aa00-4ef3f07682a5 | -2.26888 | -53.46634 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd85f9c7-5dc6-3b9d-a345-9c51ac1debe2 | -3.78191 | -50.1318 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4db9408-7b3e-3770-8717-10264e2ea057 | -4.04008 | -48.96059 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aee7029a-4b29-3d79-9255-9d1956e75650 | -4.14954 | -48.23284 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8dc34aa-4d2e-3aee-8504-c6bc03a55838 | -3.146 | -53.83722 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a8576289-1c99-38bb-b5fa-160641a20121 | -1.53102 | -51.62021 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfe97f6e-69d2-30c9-bc24-2483b01b8d24 | -2.62139 | -54.21769 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca5a2932-9dd0-3882-94b9-c9f44786f335 | -3.76003 | -49.94555 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49dc5e7c-15a7-3fec-b431-e8507d3daae3 | -2.58139 | -47.02427 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2318669c-5a61-3643-a810-7b61e893de76 | -2.76312 | -49.40537 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ade4e191-9d44-3c7a-9ea7-718efb88c2fa | -2.08826 | -48.32415 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cf68574-4324-322a-bec8-d5e89a062d64 | -3.33505 | -44.00255 | 2024-11-30 04:40:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18017a0a-d995-3c5d-8cd5-6c5c5f55223c | -1.35006 | -51.39075 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1eee3742-a722-3508-b773-a707f29c1018 | -3.22973 | -50.26966 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e327cbb-44fd-354b-8c6f-72ba195ae545 | -3.30893 | -51.10748 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 55431e48-3ab0-3270-8d63-1d1c092f666a | -2.90088 | -49.45859 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d70bbd7-1b76-3a69-8515-f0ae748d7def | -3.97455 | -46.72118 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f475259-1863-34e8-be09-837ac5084353 | -5.20985 | -47.19504 | 2024-11-30 04:40:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57588afe-e665-3370-a6ca-3b0b856ea727 | -3.68068 | -44.70724 | 2024-11-30 04:40:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a5beb55-90f2-377d-ba74-b9f5a42258ff | -2.31422 | -49.07701 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45b53a7c-07a4-3a0b-bd49-34246970f83f | -1.70029 | -52.47274 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a983605-cd78-373f-818f-4e1b49115517 | -1.59662 | -52.29366 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac49b674-9198-3df5-bc70-6a83f683da32 | -3.8226 | -46.60696 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77b12ada-7889-3398-a243-abbcb9fd18ce | -3.60762 | -49.98573 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dbed2cf6-92e4-3688-9aa5-661ad34a414f | -1.5838 | -53.83995 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6d217d1-7635-3944-a47a-9b9be3fb4ea4 | -2.32105 | -46.34914 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| acfbf0e6-9f85-3e2f-a3d0-785f2d3fe2d0 | -3.06996 | -54.40716 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46c6d350-3abf-35d9-93e6-b46922bdef80 | -2.01816 | -51.19668 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6f8c6ad-1115-36db-91e3-ecedc73eed94 | -3.96202 | -48.82857 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b205ac7c-7f7c-35b8-a592-338c992b7077 | -5.50456 | -47.16766 | 2024-11-30 04:40:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc6cc028-30ad-3a3b-aced-b94042717734 | -2.93462 | -48.63271 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8b3f055-9e28-351f-97b5-9db4fc4a6bbe | -1.0821 | -53.63444 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cab888a0-8f3a-32ab-a727-c9a84d4eeea3 | -2.58017 | -55.99488 | 2024-11-30 04:40:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99fe452f-69cb-398d-869b-e7352c144288 | -2.74921 | -48.62103 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0da8570-aada-3658-904f-43cc6a198acf | -1.88909 | -48.0528 | 2024-11-30 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba7f5f05-f996-358d-8ba9-b84b4f8aec48 | -2.62754 | -54.07198 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4de1c3c5-b14c-3a5f-9e14-fa409283d48b | -6.07867 | -48.04764 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7929b4c-f8c6-37b5-b2f0-cbae5d7747b3 | -5.66524 | -46.82072 | 2024-11-30 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaf927b9-c22d-35e9-bd75-9a5156755ec0 | -3.4639 | -50.23015 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e121c8ee-f410-311f-9564-b8e234a35d3b | -1.25592 | -54.55248 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cce036ea-2761-3c43-addb-267faf3977a8 | -1.34343 | -52.5481 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79265e0e-41a4-3e1f-b12b-dd1e402180a5 | -3.02616 | -49.52757 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a507e297-6340-33d5-a8b0-1afaba444607 | -2.46085 | -46.55265 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40a6cb4c-541c-3fc1-88a4-7a50548ca794 | -3.25413 | -51.14138 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 384c165c-9770-395e-9aa7-556a9db5ef36 | -4.66728 | -44.06462 | 2024-11-30 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2adf8bc-cc25-395b-8c8e-3de56b984fb5 | -3.11828 | -53.98193 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6c722e0-9017-3be3-92a3-659fae56172e | -4.6367 | -45.08812 | 2024-11-30 04:40:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d0f3b0a-7ba6-316e-95e7-c439d711983a | -3.86162 | -50.53643 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ddc3ad7-cb09-3c33-b840-5f7ae298ec54 | -1.20373 | -51.74194 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8f267a3f-dded-3782-8d95-29d40bfd248d | -1.85791 | -50.80516 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e50573c2-8734-3b13-b04b-8b7e2a16a66c | -0.24437 | -53.76155 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d30214f-5ec7-36d6-9004-aa6eb693838d | -2.2388 | -47.99017 | 2024-11-30 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3540db7-6900-3b9a-8301-6b179e99ad8e | -2.67627 | -46.27836 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f258c644-5dfc-3454-84dd-905ad8150906 | -1.07044 | -53.62916 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1f86e3cd-808f-3bbe-a8f1-eac34d2efd70 | -2.21071 | -48.91323 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfacf5b0-d301-3874-80d3-1e95f178e5c4 | -1.19317 | -51.76171 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f07b66d-464b-3861-a952-f18cfd8a8e4e | -1.9996 | -51.17794 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3905bd1-62d5-35f3-96eb-f738eaf2ce5b | -2.91453 | -48.32616 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0735bf63-2fd0-3c11-9f13-35eb0c908cdd | -3.03387 | -49.52167 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca5d7b4c-ec15-30a9-948b-e0cf8757ce9e | -3.61727 | -50.09502 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abc63f26-f5db-3582-8ff4-e1043470610a | -3.13544 | -53.68252 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e12119a-156b-3ad8-bbd0-19089614ae49 | -3.40003 | -50.6605 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4c96104e-f38a-311e-ae2d-9043d5dfd39d | -3.48536 | -53.80468 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ca03935f-d656-3ca8-b9ee-cf98c46af7c0 | -1.36489 | -51.38893 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df8a1604-3af6-3ce3-ad53-8bfe9e2c7401 | -1.6829 | -45.79053 | 2024-11-30 04:40:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ce0a4b21-6910-3b46-a838-1e16879db7d0 | -2.13813 | -46.41535 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README72.md)
