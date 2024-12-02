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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c8e20cb-0ea5-3522-b098-327b3d000680 | -3.35486 | -49.50515 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f209324-80a3-35de-8385-0aac95ab756d | -1.25773 | -53.37694 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ca00ee4-9037-32c2-9791-a065eff86e00 | -1.42086 | -52.25652 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e55f3f7-97a9-3c93-89e1-335f537a9edd | -4.35966 | -50.86767 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2911532d-17eb-300b-b0d0-ea8b7f5f9b31 | -1.8178 | -46.64206 | 2024-12-02 04:48:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f8e538d-71d5-3890-a02f-04cf916a78db | -1.67808 | -52.80107 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf9f882d-1269-3222-8474-d7a51b14104a | 0.86275 | -59.68607 | 2024-12-02 04:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ac73154-7bb5-3936-b9cc-914bc8e75138 | -3.74989 | -54.51731 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f0b1ecd6-a2bf-379f-be11-338e346f6da5 | -1.07285 | -53.39464 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62d89af9-2a52-3ba5-aae8-c232b7619b0f | -3.25904 | -53.86622 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29c014fa-f597-3bb6-bf4e-5146f2b74f28 | -1.22802 | -53.3648 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6b02a68-0588-32a6-8bdd-bc9b05148c83 | -2.74017 | -51.75248 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c285395-d973-3645-8381-6f1aafb4407a | -4.76871 | -46.43064 | 2024-12-02 04:48:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7724cd6e-618f-3f9b-b735-fcdfbf05ac88 | -2.36564 | -53.86144 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 834ba122-f873-36c4-994b-f31412fec53e | -2.57853 | -53.97896 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3f54083-3af2-341c-8689-c6d788ef8413 | -1.26666 | -55.7046 | 2024-12-02 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f8c2834-d47c-33df-b427-cae65420f492 | -2.44189 | -53.99847 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c3ed0b1-b485-37ac-afe1-56abfdb8cdda | -4.06071 | -51.06705 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bd24ea9-9370-3603-a474-ffc4cc484296 | -2.11874 | -50.34199 | 2024-12-02 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 433bc537-dc3e-3f0b-b9f5-ab4bc0ce23e3 | -3.2495 | -53.618 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8df57bcf-e9a9-3792-9a0b-6cfc6c0dbf87 | -4.0732 | -46.68084 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 184f0af5-297e-3b73-9fdc-ed1e9961f507 | -2.00888 | -51.19792 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31f7146e-a507-3ee3-9ba1-815a9c7b6ea4 | -3.33356 | -53.37413 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16317f2c-a222-3955-a99a-f28088276f6b | -1.29117 | -51.37416 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 628c71c5-8239-3a4a-a1c0-8c24d6177025 | -2.19138 | -50.57298 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2900bfe9-7866-3601-b6ee-56e8675367b8 | -3.4581 | -51.42108 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bab302ac-a8a2-3754-9f14-67dd1be75121 | -1.78424 | -52.7523 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee44e760-8f9f-3772-b9ae-3bdcdd5662bb | -2.58106 | -54.0304 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba89c201-5f47-3c31-8077-3864c043ea78 | -1.7027 | -52.645 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65d6e12e-afdc-3a29-b396-be5506e837d1 | -1.43294 | -51.12174 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b95bfd9f-0283-3782-9f84-69f851bc0f15 | -3.28951 | -50.4417 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9370c53-3019-3a22-afbe-c9594e581151 | -3.27431 | -46.45688 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 30.8 |
| a2f0b02f-563b-32e3-a872-74a3276b0eb4 | -3.5954 | -50.37116 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbbf44c4-3d8e-3e20-80e4-1cd4d8916961 | -1.98294 | -52.07427 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30bbfc96-d665-39e0-b5cd-efdc8a91e366 | -1.14632 | -53.66428 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcba6e14-d6af-3e1d-8c57-8121b384cc26 | -3.46793 | -50.27044 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a851cd04-8554-3304-aca5-b0e33ceef7aa | -3.59377 | -54.7467 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c99a9ae-a7a1-37f6-9c46-f0ee4af74ab7 | -2.4376 | -54.02533 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a97eef94-e3f7-3ccb-9703-cfd116c2ac80 | -2.54583 | -53.41244 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20bef7f6-7f27-3cd0-a049-1f20328d45ec | -2.7062 | -54.15995 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5becacbf-4d86-3589-a14e-ceb4890fdbfd | -0.5887 | -51.69336 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e162ed8-a5e0-3a51-9906-c40408b23683 | -4.03454 | -46.93279 | 2024-12-02 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdc4d8ee-741f-3021-88d3-a6af3cacc78a | -3.17806 | -54.33106 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f25a864-bb2a-3d9f-b1ba-9d668fd7ba83 | -4.24846 | -49.19457 | 2024-12-02 04:48:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 700b47ff-de6d-3686-99a3-61d3f5f4bf0b | -2.73364 | -54.1007 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 414be9dd-e229-34a0-b27f-3f55ce91af0a | -3.26092 | -53.83216 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85df8a05-05d6-3453-a3b7-e8f5ca54bd13 | -3.05567 | -51.06376 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 482b7792-c029-3fca-9dfe-98f042248631 | -3.90485 | -47.72377 | 2024-12-02 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 354c4b7e-a76d-3179-b7b5-7e2653885a88 | -2.65754 | -46.12325 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a5bace6-b7ac-3755-9909-50b6ce9194d3 | -3.74566 | -51.29947 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08c66bd3-3758-3145-ba84-1c85e277e035 | -1.69935 | -52.64447 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d6bc73c-52c9-3659-aa47-ded640000dc2 | -3.76046 | -52.67325 | 2024-12-02 04:48:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed04616e-de19-3d23-ac02-3d9a5615c6ae | -2.0535 | -51.19427 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c24de43-7f69-3400-b4ae-112841899bb3 | -2.31132 | -53.90047 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86955d73-1561-353e-8be0-16eac60e8b96 | -3.06075 | -53.65763 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f6f858d-bde6-3b4f-8003-e89ebc5b73a5 | -1.474 | -54.43208 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e4a7efe-165c-3107-a10e-b57d55c8d3ec | -1.51548 | -51.20149 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98031ef0-9b09-3ef0-8450-bfe5b328d2e6 | -3.17229 | -53.64021 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee52d9ad-f2f2-3edb-9d66-b00a8664e7cf | -1.09675 | -53.61782 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 151a7bf8-137c-324e-8180-5ae0382951e5 | -3.71062 | -47.67977 | 2024-12-02 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fefa40c3-c422-377e-ade5-0871c0e9bda1 | -2.97485 | -53.93074 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf653d63-5441-336e-91a8-73cfcaf7f2d6 | -2.03905 | -54.6632 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27ada728-84d5-3168-8c0e-081068485522 | -2.56457 | -53.40418 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b65ba444-83b2-37b9-9b45-fee799e53f8e | -4.14254 | -48.24126 | 2024-12-02 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| faeb0a7d-56ae-34a8-80c4-efcfd83a56f6 | -1.81382 | -46.64145 | 2024-12-02 04:48:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6340bb40-6efe-3f2f-8f69-6a3e9b709ce8 | -3.33645 | -51.5256 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ec27a0f-b7c1-37b0-8050-98d429268771 | -3.50178 | -53.83907 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98aaaece-4e24-3d03-bc22-a3b991c2acb5 | -4.61935 | -48.03445 | 2024-12-02 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab51ef66-3c82-30bb-a592-2a81cc57c639 | -3.54364 | -50.18554 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e980298-125a-3553-aa49-5088d7f1fe1b | -2.26057 | -53.61799 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5c0fbdb-b869-3339-b50a-cbe2bdc96073 | -2.84682 | -54.05134 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a6c1cff-2926-31ea-94d3-0719041148c9 | -2.46912 | -46.58139 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe8f0fe9-4068-361f-bd82-369a58ce4106 | -2.82331 | -54.07547 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 453d2e53-0a3a-3953-8612-7612bf1ac2d4 | -1.4225 | -54.51226 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5834d1b5-4d64-301f-b9ff-dc54f3c4ee5c | -4.05668 | -48.9652 | 2024-12-02 04:48:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 47f02f05-2a58-3696-a7ef-31a59fb38d82 | -3.96 | -49.98823 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccfe4f8b-9e18-39fb-8289-545f8e12d609 | -1.23873 | -48.32689 | 2024-12-02 04:48:00 | NOAA-20 | SANTA BÁRBARA DO PARÁ | PARÁ | Brasil | 1506351 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de926cee-1743-3b9d-b7fa-6d8e4ac05253 | -3.93382 | -46.71985 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 768019ea-2045-33f9-90c0-ccfd8252180c | -2.89146 | -53.97243 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b06c048-8831-325b-86f7-bba5d72d7599 | -2.84866 | -54.03987 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5208b2d-7185-3f74-b588-8143abecbd6b | -2.22418 | -53.62778 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 407c57fc-f554-340b-a0b5-6aec507f4dba | -4.06921 | -47.09129 | 2024-12-02 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51609446-1abd-34bf-80b2-3495c8996dbc | -1.25222 | -54.55196 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56624f64-0555-34c9-b027-1d81702ede82 | -5.1179 | -43.20859 | 2024-12-02 04:48:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 21aaea6d-6c55-355f-bf5c-2d84713f8b35 | -3.2586 | -49.902 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81f4d798-d571-38e3-bc1a-bcd9764a91d5 | -2.95743 | -47.89527 | 2024-12-02 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3230fcc7-23e4-33c5-a782-d7d1a0b51206 | -2.44641 | -54.01488 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2ccd5df-59ed-37c0-b029-28c5d5236496 | -2.80033 | -54.04039 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3655e2a-ec21-378f-96e9-1a520114843f | -3.74308 | -52.26597 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08ba807e-c3fd-33a4-8e58-fe222fe94e8f | -1.90603 | -51.00869 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5862b07-fbeb-34a3-a375-e2ca4cd1775c | -2.61511 | -51.81383 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64fb3321-c2a7-3025-b685-c3ad8dfc8fb8 | -3.53856 | -50.17358 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| babed374-6ca2-3929-b25c-96f32a0a44f5 | -1.62627 | -53.86283 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b74af13c-8e5d-3288-9b9d-45caf9981703 | -3.26139 | -53.63108 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc55b21b-2c75-3e45-a5fe-fec283b54c3b | -3.8134 | -50.95321 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25731d6c-8d2b-3f9e-8223-b131b62e286a | -3.56695 | -52.50036 | 2024-12-02 04:48:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c626cf05-1732-3505-a7d9-87402c46682c | -2.89172 | -54.01535 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb5fec86-6d3f-33f0-bbbd-f759fbbd37cb | -3.43481 | -54.5389 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9e823ca-e7a0-39b0-a985-c418437011fb | -2.82846 | -54.08808 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92873d6b-d4f5-3c71-ab6f-dec000110557 | -3.37792 | -50.69519 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README65.md)
