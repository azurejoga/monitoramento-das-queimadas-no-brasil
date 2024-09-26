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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d668b8e-096f-39b4-a4c7-8f332318d94d | -10.43868 | -53.68219 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1afe528-22d6-3ee8-bce3-72b47f97686e | -10.50579 | -52.2273 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fddbbb38-58ff-3110-9d3c-89cfbacee5ad | -10.44612 | -53.22125 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb449d32-fa0c-309f-9721-07be39c429a6 | -10.42194 | -52.9372 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1774201f-e4d7-34f7-9cab-2a440deaf851 | -10.4185 | -52.93667 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5963ccff-443c-33ae-8756-b0b584e6ba31 | -10.41563 | -52.93232 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f6e3e28-b319-310c-8435-d68252b9f9be | -10.41506 | -52.93613 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73a6aae4-abb3-3c01-b97b-2613fa4d4925 | -10.41219 | -52.93179 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da20d6d3-3d97-3a68-89cf-94cfd21e38a6 | -10.41162 | -52.9356 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2236cc6-2905-345f-9473-39bb29ec4910 | -10.40531 | -52.93073 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb562e49-d58e-3a94-b009-5fdcaa4f1d48 | -10.40187 | -52.9302 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6d33521-da58-31df-ae90-71ec14858ced | -10.35993 | -52.93156 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12344329-a77e-380c-9038-8b449f015d19 | -10.30272 | -53.008 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20d47976-dafb-37a7-bb0c-8a8737a2b9b5 | -10.30101 | -53.01934 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c858624e-7e69-33f1-aa97-2765c4c0df2d | -10.29878 | -53.08066 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00be74dd-bdcf-33a5-be1d-5ff1ac7ff038 | -10.29759 | -53.01881 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8c52a6c-06fc-3da2-b10d-2c19a447f927 | -10.29479 | -53.08388 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f700a0aa-4996-3ee4-8231-0b901c52fed0 | -10.29076 | -53.04094 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3db89132-ac5a-3949-8fd5-66373768d259 | -10.28733 | -53.04042 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65c44bc0-7c28-3410-9341-467e2e11b24f | -10.28391 | -53.03989 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a71339b-43ea-3ae3-8c75-af56f1cf6398 | -10.28335 | -53.04365 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b1c1558-5033-34c2-8775-a5ce09beb6fe | -10.28278 | -53.04742 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b59e931f-dbe1-36e6-bf5b-9b29c3d19a71 | -10.28222 | -53.05117 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64725944-be4f-3ad6-8692-b8873ea56334 | -10.28166 | -53.05494 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfd299d9-318a-356f-88fb-3ec8a7629a04 | -10.27993 | -53.04312 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e527b4cc-11db-3dd4-9494-3e158012da07 | -10.2788 | -53.05064 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec746e97-8d95-3666-bfc1-81a3d78140a1 | -10.27824 | -53.0544 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6c96140-e799-3d87-9212-9a59a4cbc8ab | -10.45711 | -53.31031 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9371ced6-14ba-3fd4-af64-cfb8d0cd59b4 | -10.45483 | -53.30237 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e6e4faf-0e47-3687-a160-856024f49977 | -10.45427 | -53.30609 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c92aa445-393a-34d2-9dc2-f4fa7081209e | -10.45371 | -53.3098 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aeb5577b-c05c-30ae-bf43-8866a1fa78f6 | -10.45316 | -53.3135 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b8b9ad49-af88-3804-961b-d6bd17b3dad8 | -10.45143 | -53.30186 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d293f720-67ec-34c1-b550-e3b313af309e | -10.45087 | -53.30558 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4133d77b-60a1-384b-ad9f-c54091871e30 | -10.45032 | -53.30929 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| be47056e-c511-3480-9d2d-16c7b2afe4dc | -10.44976 | -53.31299 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 224744dc-f3ed-3dce-a207-4e0cf277ceda | -10.04856 | -53.34308 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 745ccab0-06ed-3db0-a28c-145bc25590b6 | -10.04573 | -53.33892 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95d42282-b588-3f05-ab83-52ca5e149e52 | -10.04518 | -53.34256 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a61c9f3-cacd-3a10-90b4-3943402257cb | -10.06557 | -53.45791 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdec5c6e-2069-3e11-ad8f-cf45a974bfaa | -10.06556 | -53.43551 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 478bee06-df2e-3ae5-a660-3b3ab50566fb | -10.06501 | -53.46156 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4eac8f5-ab4e-33db-bbe8-d7504b26f814 | -10.065 | -53.43916 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c3c15c7-4b7a-39d3-8a23-701444f671dc | -10.06275 | -53.43133 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc616911-62f6-32cb-a43b-f5e62947bab1 | -10.0622 | -53.45738 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f881ae70-7ee4-39b8-8707-4ee79c4237a1 | -10.06218 | -53.43499 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccb7e4ce-cb10-3a2b-89b7-e06249f81a11 | -10.06164 | -53.46104 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be14aba1-96ca-3f7a-a47c-e2c3f3591a20 | -10.06162 | -53.43864 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d21e49a-08a8-3de8-b579-0caf29832670 | -10.06108 | -53.46469 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 388539dd-4ccf-39d1-9d47-db3cd677cb83 | -10.06107 | -53.44229 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9882110-29ac-39e8-ae86-ec25d59e3cce | -10.06051 | -53.44592 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3480eadc-d10d-3204-a776-3d705050711e | -10.05995 | -53.44957 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96f5817e-68ba-3146-9239-6d1480a26014 | -10.05939 | -53.45321 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c91ba993-bbfe-311c-9698-9b3892344d1a | -10.05937 | -53.4308 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a9a4ed3-2c6d-3347-b4d0-5c9bc0966e75 | -10.05883 | -53.45686 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93cf5528-3a0b-3d5e-9c00-cc33479086e3 | -10.05881 | -53.43446 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0b156e1-eb0b-3e3f-9512-b72eea2c4907 | -10.05827 | -53.46051 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faa28642-d384-3c82-87d7-6e6bef29ba85 | -10.05825 | -53.43811 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df696eaa-182f-37e7-aeef-d8e5661f76b7 | -10.05771 | -53.46417 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa3e65b3-bced-3a2f-a1ca-199c01a30b5b | -10.05769 | -53.44176 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acb44343-bbd2-3d48-9c30-7983b2f07a2f | -10.05713 | -53.44541 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c070725-b2e9-3fa2-9abf-c5d2bfc5b7fc | -10.05658 | -53.44905 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4cda29ec-61fc-39c5-9fe5-729748ad90bc | -10.05602 | -53.45269 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a67a927-5bab-304a-a298-196439c1c11a | -10.056 | -53.43027 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08a19767-b63f-3925-afa0-774e34c46d62 | -10.05546 | -53.45634 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ec38419d-0ac3-3eca-a435-87197023fb62 | -10.05544 | -53.43393 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8f6cef7-38c3-3600-920b-88ebb8add5b4 | -10.0549 | -53.45999 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| beeaae40-f9d6-3196-a54a-8e0e23f04ffb | -10.05488 | -53.43758 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 203d76d7-0ce0-3535-9b7f-33188a16ce8d | -10.05434 | -53.46365 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a4f0cd1-1b27-32cf-b3e2-3783bc68d130 | -10.05432 | -53.44124 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0448a0e-3768-3cf1-91ea-01ed903b4453 | -10.05376 | -53.44489 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32d8962d-4971-398e-bab5-55bf81213c76 | -10.0532 | -53.44853 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6d555b8-507f-3f22-bb84-52347f653758 | -10.05265 | -53.45217 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 38fc7203-7e06-302c-a99f-d2965462d0be | -10.05209 | -53.45581 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e6a15a5-4ffa-3e55-a13c-632503488860 | -10.05207 | -53.43341 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd544bfd-8fec-3b4f-8aae-eecfbe1ca93e | -10.05153 | -53.45947 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 414d8555-6e5b-33a4-b43f-05fe3878b2e7 | -10.0515 | -53.43707 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d53b9646-952b-3dc8-8168-4cd1c791e9fc | -10.05097 | -53.46312 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c8e545ed-a9ce-34e4-871c-8703ec67c459 | -10.05095 | -53.44072 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26ae8433-9877-372f-9808-a052e4197128 | -10.05039 | -53.44437 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8d11606c-29b7-3a35-8c2b-9425443dc9d2 | -10.04983 | -53.44801 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a67a4d8d-4869-3532-9b09-931dda1551dd | -10.04927 | -53.45165 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 682d7e4d-8f94-3469-a798-188cc69534fd | -10.04872 | -53.4553 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 214d755b-da96-348e-a991-d45caf2dc8e2 | -10.04816 | -53.45895 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7cf51761-0d3b-3e35-9170-69e9727babc3 | -10.0476 | -53.4626 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| de373d6b-8ab4-3f0c-986c-6f0988e61d0b | -10.04701 | -53.44386 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3ac3cc24-432d-3844-89cc-17eb61266a37 | -10.04646 | -53.44749 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 57181712-c578-3aa3-8fd2-2b14ac083be2 | -10.0459 | -53.45114 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e45c08c2-2dc0-3770-a922-e99404d74ef9 | -10.04534 | -53.45477 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8448b033-e3ad-3242-bb8a-bcc39c149a98 | -10.04479 | -53.45843 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 633bae10-7545-3203-82af-7c35b437acf4 | -10.04423 | -53.46207 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 92c1e94b-62a1-3513-afc9-93914fd0007c | -10.04364 | -53.44334 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cdd20af3-e76f-3f72-94fb-266b2910e2a6 | -10.04308 | -53.44698 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a233fbd3-15a5-3775-9337-e2e10adea91c | -10.04253 | -53.45062 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 40125db2-1073-37eb-bc9f-680b4fd1457f | -10.04197 | -53.45427 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 438bed78-0499-3568-8026-d7527f7c61da | -10.04141 | -53.45791 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 70ba46a1-1b25-3002-96ba-3bebe331f8fe | -10.04086 | -53.46156 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 3dc4531a-ac1f-3ff1-9ba6-aec436c8530c | -10.03971 | -53.44646 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8200aba3-4d7b-3a00-840a-c541fb92b36f | -10.03915 | -53.45011 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4bcb82b8-4827-3f0f-a860-bb8922614bdc | -10.0386 | -53.45375 | 2024-09-26 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README123.md)
