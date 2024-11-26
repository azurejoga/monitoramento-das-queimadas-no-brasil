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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01306014-ca1d-3959-b4c2-a014694e0f3b | -2.98356 | -53.89028 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99af4eb6-b5c6-365f-8684-dcaf489e9ff8 | -4.50482 | -45.20314 | 2024-11-26 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcea2c07-c56a-31c6-8dc1-765bea9e551a | -1.55794 | -53.79503 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0a2d2682-5090-3457-812d-e9b3e030987f | -3.59541 | -50.38962 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e76f5b6-f238-3179-b265-e53d0968aeca | -3.94589 | -48.15601 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5611ab7c-5e6e-33cc-a9b4-d53972012534 | -1.72394 | -53.59087 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccfb6887-73f8-3d06-bd78-220c399b00a7 | -2.91592 | -48.72436 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eea8504-773f-3a63-95a1-b57fab179f29 | -3.94201 | -48.15896 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7869b08-34e7-376e-b2ae-915a1941cbf9 | -4.66526 | -47.94881 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60f23cc6-014f-3581-ba60-3b73b55891db | -3.23015 | -51.60687 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 861c8c01-3c94-3ea5-8bb1-a34089615704 | -3.97397 | -48.08549 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 322f252c-63cb-356f-a497-7df2f7989724 | -3.28984 | -50.26801 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b1dcae9-2d9a-35ec-8bdc-cccb2059bacf | -3.17886 | -48.43026 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67782c47-ee5b-307f-8254-bc426da43177 | -3.42836 | -49.9939 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb7b2a7c-ab43-34b8-a2c8-6cfb800ccc9e | -2.69328 | -46.87094 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 073b27da-6ef2-3783-9ac4-a6337fffa729 | -3.59066 | -44.92747 | 2024-11-26 04:38:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e23ec23-dbd2-3c16-bfef-e6a2fbfb3472 | -4.38461 | -47.77516 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6919c0a7-add6-3db8-93a1-22603dbf861f | -3.99064 | -48.08808 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b77946d-81cc-3dd4-a8c2-c1f5f6724296 | -3.4514 | -50.00122 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13e57262-4aac-3473-a249-85f3e4418f6a | -2.25099 | -53.61735 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2b853ed-2f81-3fbd-8ab5-6a9acb5625ef | -3.06251 | -50.24743 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f13ae230-ec0a-32b7-9406-85f8254b2fad | -3.91051 | -42.42133 | 2024-11-26 04:38:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| bb793bc7-4473-34a1-9ce6-fab534e69bc4 | -3.39327 | -50.32124 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2239887-0cce-30ef-a82a-14a64a58e5fe | -3.97762 | -48.19303 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbf48fde-b1f4-38bb-99d3-f11fce0543b2 | -2.64761 | -51.77187 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| def1f38b-2cce-3be5-a332-eb400e38e17f | -3.98391 | -48.06556 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| b3083529-9776-329f-bf02-d6cf1ca3267e | -2.80978 | -53.03023 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d038c92d-82bd-396a-a59d-1d133bec5557 | -3.24459 | -50.2236 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 310bc03b-f8e4-3285-b7bc-d869abfe6071 | -3.84422 | -49.96355 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dac0f83f-4289-3b27-9991-815b58106469 | -4.29551 | -48.23549 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c10ac4ff-1b51-3c2b-9d4c-4f6eba4fbdce | -3.95395 | -46.91076 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bef2e36-2a94-3a8d-985a-b4979724ef53 | -3.38534 | -50.10505 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ae9b032-d9f4-3c86-8631-6d438a1a85e5 | -1.35572 | -54.6339 | 2024-11-26 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c12397fd-b3dc-30bd-b2b3-f509da321558 | -2.89586 | -51.5737 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1daa6fc-4c28-3939-95f5-a28278bf77ac | -3.98064 | -48.08654 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 221ef301-4ef8-3b58-b2c2-b61b51cd80ee | -3.45026 | -50.00837 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4fe0fed-6c0a-3e66-a2b4-14cf00b49bd4 | -2.69922 | -51.98462 | 2024-11-26 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d62e8ea5-9233-3f46-aaea-aa8ab279e649 | -3.69056 | -50.22975 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3b3a092-2bb4-3892-bd60-73f6228f0c03 | -3.17669 | -48.44407 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d61b692f-c543-3b62-9df5-95f57be048b6 | -3.28585 | -50.27114 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f57a2dd1-035a-3be4-bcc5-525c553b956c | -3.25273 | -50.41199 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1af589ce-f775-3724-b2e6-98195d01812d | -3.96615 | -48.06996 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f35ca60-90aa-3d0d-b10d-0c3e4f374ef5 | -3.34592 | -50.50982 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c45a607-5a9f-3deb-bf04-8bf3479c5744 | -4.09499 | -48.48104 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86740427-f05a-3eef-a3dc-8af142410bfb | -4.94911 | -47.8037 | 2024-11-26 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dd1ff6a-0e5e-3410-938d-6bc7c74522e5 | -3.15398 | -50.61677 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c1d8a5b-0912-3135-80da-e950863a5a94 | -1.74008 | -52.73812 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cde21f93-0b31-3a6a-907c-a9cfe917d932 | -2.4893 | -49.0293 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c27dab5-e19f-3740-b1ef-c5f4ce1a7e5f | -3.06257 | -50.24799 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 171f562b-3a7e-3845-bab7-9cea3477bcf3 | -3.84407 | -47.05605 | 2024-11-26 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca8a88df-bcc8-3016-9d72-c5b6ac350815 | -3.15053 | -50.61623 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e858df9d-a7ce-3f00-bfd6-215a73fdaf90 | -3.9639 | -48.06246 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| d1288c75-9650-3a61-aada-e0c5308feb5e | -3.98112 | -48.06155 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| df78458e-0323-35f0-9ef0-ad20ec1710b2 | -3.93966 | -46.8896 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ce951a4-ad0d-399d-ae15-1cf10fd07bad | -3.32341 | -50.05841 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bd74e54-bc02-313c-b6bd-33e94047d680 | -3.58918 | -50.38488 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34311f8b-9ea7-3358-9647-6b20b674e631 | -4.1776 | -48.79164 | 2024-11-26 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe492d2e-62c6-3960-bccf-29fd995fc64c | -3.94309 | -46.89015 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36040517-bc5b-3893-aa8d-b3ee17b67896 | -3.9884 | -48.08056 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ba2181a-f177-3b1d-8153-d9f9f045aae9 | -3.08479 | -51.02676 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 814772e4-eb04-364f-b494-e0653fe5338a | -4.24085 | -48.6706 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f33dade5-22cc-34d8-b76b-9b696d2e61b8 | -3.47269 | -50.3487 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4a912bf-ff45-363a-a9c5-651dd2cbf7b3 | -8.26189 | -49.54441 | 2024-11-26 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8685ffd-cf01-3c95-9281-fc45f7a47711 | -1.92836 | -53.35033 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a255f48-d633-36d4-a246-444532ac0ba5 | -3.75775 | -49.93567 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50339a23-26fe-37a5-bf0a-50c61169e3fe | -4.05021 | -48.31085 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfb1963c-9c1f-3931-9b98-9cc32e851961 | -2.69853 | -51.98893 | 2024-11-26 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d973d918-0a35-3eec-8cca-5a64c95f6418 | -4.36401 | -48.08177 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 07f795e2-67d2-300a-8d05-4bcaf9a7f4c1 | -4.2983 | -48.23947 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7409f2b3-2ffc-3a21-9ff3-47bc4aabdb1c | -6.11099 | -46.92301 | 2024-11-26 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f45e951-5d0b-3e7d-a4d8-7cffb80b771b | -2.40762 | -53.67987 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd2f4cee-8287-35b9-bc8a-c6cb38cd996b | -3.68831 | -50.222 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3512aa7-e1d4-3a90-85f2-72163aabaa5e | -5.47918 | -51.17156 | 2024-11-26 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ea8f741c-324f-3c55-868b-2207c25530ff | -3.16687 | -51.09911 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22f6ada1-27ef-3a1c-85f8-784eaae855a1 | -4.2519 | -48.66524 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5f9ec44-6993-3f39-aedc-c6cc43fcc0df | -1.78064 | -52.73457 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78dbaa43-827e-37cf-9451-70b80d77cacb | -3.0883 | -51.02732 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b286332-7410-364d-9c7d-71df516099d0 | -3.08523 | -51.41106 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 366b134a-8a5e-3c8d-9e91-d6696b7072ce | -2.71271 | -46.29215 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d2fc1a4-7721-3e5e-932f-d99eae8c7ad5 | -2.27095 | -51.90959 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae19ebaa-43ae-3d8b-994e-9b8a985338de | -3.98337 | -48.06906 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| e7569b91-daaa-3ede-8306-e7e90a684260 | -3.42712 | -49.99389 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ca86211-05ba-31b6-a4ff-15735736fc44 | -2.93234 | -48.01974 | 2024-11-26 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a358f59d-144a-3130-a3d0-0b94c5af3217 | -4.66191 | -47.94829 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10c5d3e8-06b0-34e1-afc8-8d3e67214568 | -3.55137 | -50.20436 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 328865e5-866c-3b04-82d3-773e7e386d6f | -4.13055 | -48.51196 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1607fbbc-a40e-3141-82c8-a4b87f320387 | -3.98616 | -48.07306 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 38ecdee7-68c2-3301-9474-e26d31dbc4b3 | -2.71222 | -46.2617 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 899c89ce-6918-387c-8f9c-6aa9d4e404cb | -2.47673 | -49.10917 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64457ce7-af8a-37cc-93fb-7905eb8bc5ee | -3.18827 | -48.43526 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 33e11fc9-3ddf-3b56-8584-022472b82dcc | -3.1855 | -48.43129 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 488a9f23-09dd-3501-81b2-cfb92a431511 | -1.57338 | -54.39375 | 2024-11-26 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4df6097f-ce16-3a68-a6a0-28fa7684eda7 | -3.9752 | -49.93011 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04e12cb9-e6f1-31f1-bbf6-2af1ac5db48e | -3.04496 | -48.50789 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86318d5c-4c13-3596-a71d-d154add15e81 | -3.49849 | -53.8116 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3531969e-668e-3936-8af7-8cc40cf9219f | -4.02914 | -45.54641 | 2024-11-26 04:38:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31a60a14-b5c2-3716-8c54-c66bf45b785d | -3.18163 | -48.43423 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 4dc5da00-9d46-37d5-8233-5c932738f876 | -6.07359 | -48.02681 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 849131d3-1807-3521-85c3-f48ccd8b728f | -2.45512 | -46.56103 | 2024-11-26 04:38:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cf3795e-a2f3-3837-8a1c-1b3358d2d8c6 | -1.9916 | -53.29203 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README26.md)
