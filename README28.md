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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63ac78bb-c003-3f3f-b882-33a27114ba64 | 0.38708 | -50.93707 | 2025-10-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb5c3142-ba12-3478-9cd1-f673e70a39cb | 1.55998 | -56.02446 | 2025-10-23 04:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba0637f6-ae1b-3367-85ad-b5efce4865fa | 0.38089 | -50.94172 | 2025-10-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68602148-bd04-3612-9188-e908fa293687 | 0.98391 | -51.29256 | 2025-10-23 04:53:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62c7192e-b473-3244-99fa-671a81095181 | 0.98246 | -50.06539 | 2025-10-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 040990e8-703a-32a2-9d6a-91a31240ba04 | 0.397 | -51.10818 | 2025-10-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf13977f-7d2e-31cf-aa26-3d340c4d466a | 1.65629 | -55.75522 | 2025-10-23 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac167943-8095-3b82-9131-5c0b2a9db4d6 | 0.98336 | -51.28904 | 2025-10-23 04:53:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2c7d3b17-71d9-3347-a833-5ac181a30593 | 1.29039 | -50.97378 | 2025-10-23 04:53:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9078c759-a5c0-387f-b581-cc653912a1f3 | 1.55928 | -56.01999 | 2025-10-23 04:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f330d3bd-020b-3076-a7ad-8f84cf982471 | 0.98246 | -50.06538 | 2025-10-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55c959a9-6892-3002-ad5a-6968429e3e83 | 0.38427 | -50.94119 | 2025-10-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4663ace5-8503-327b-8b1b-0de34e2d8a4e | 0.98391 | -51.29255 | 2025-10-23 04:53:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ca844a2-7aea-3bb5-a59f-70c99744b520 | -3.84438 | -51.67442 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 827c1d94-0139-3ac3-bea5-4414327d70e8 | -3.73635 | -51.37746 | 2025-10-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44a038a0-508d-38fc-8fa5-57cfa2f7f50c | -3.47314 | -50.07243 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39261255-031f-3545-8916-b2aa31f2b2aa | -3.15645 | -49.17551 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26856cc5-b761-3e8f-8ee5-57bbf5fd8be1 | -3.81599 | -51.70006 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a16b34b8-5aed-36b0-b1dd-055461171952 | -6.60566 | -44.21779 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d057ae6-a1e0-36d3-8b3b-29105bdc4a24 | -5.63358 | -50.0315 | 2025-10-23 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd2f9526-6ef0-3952-bffe-024f41654a92 | -3.33698 | -50.75164 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8afcbb1a-0a9c-31b3-9748-309cb81f09fa | -2.80544 | -51.34834 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8efd77a5-46f4-3d2f-ae84-1ebca52e0464 | -3.16364 | -48.61018 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3571fcfc-22a2-39b9-90a1-2e10afc652bc | -3.05175 | -48.71371 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a59500e9-2a15-3ef2-a8a9-2d7144dce9ab | -6.85433 | -46.29485 | 2025-10-23 04:55:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 33ec39be-3206-303e-9f8f-c56ae441e538 | -3.02329 | -49.48006 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f57c735b-bb15-39b8-9ed6-999c5550abbb | -3.22014 | -49.36264 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26ca3e70-eff4-326b-a9e5-342ed7497b33 | -7.08063 | -46.19964 | 2025-10-23 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15ae43da-5c05-3c68-b4f5-0e9890992ee9 | -3.41898 | -50.36737 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8085d2df-0043-35f4-a10d-0ca201f9227a | -2.42929 | -49.2708 | 2025-10-23 04:55:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 683c7368-ff43-301d-a053-a0955e1230bc | -6.1122 | -41.79416 | 2025-10-23 04:55:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c1d9dcf9-08f4-3a8c-b731-7967f4d40155 | -3.04783 | -48.71309 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b6ad930-26c8-36aa-bec6-434fc9b934f7 | -7.1791 | -44.78423 | 2025-10-23 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65d6136a-3c71-378a-89c4-c536933ec83b | -6.60399 | -44.21758 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 787e254e-b826-3627-95db-07c8effe2bf2 | -2.73865 | -48.43179 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87414329-840f-3dfe-ae87-58e657f12c5e | -2.86111 | -50.74175 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 573cd8bb-cdb1-3595-8072-3b17d9672efe | -2.80927 | -50.27949 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf5a5fd2-9e98-3ff5-9e59-6d78ab317573 | -3.46889 | -50.07325 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b680a96-a56d-3cfa-b0d0-563b7f479b24 | -6.94186 | -44.46162 | 2025-10-23 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1883382-5235-3089-9254-b42c05dd45e3 | -2.23774 | -51.99786 | 2025-10-23 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9066f651-0b30-388a-8233-a19812d3ac70 | -3.04188 | -49.51784 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8a8225a-4393-3983-8d94-823c09c415d4 | -2.90066 | -49.39989 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6ea9224-a26f-367b-8d47-41b01211230d | -3.15234 | -50.16519 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3517162c-e808-3029-aab8-1905783c634a | -4.63735 | -49.53801 | 2025-10-23 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b171ad23-de92-3e49-a146-b63f0d3535c5 | -5.69056 | -45.9783 | 2025-10-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08d7f7ae-5c29-39e8-8e67-4a42ff33477b | -3.47252 | -50.07383 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3379ff8-413c-328a-b7c6-1b5b2c2ed90f | -2.80486 | -51.35203 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6027f7f2-77ae-3b08-accf-ad653eccf9d4 | -5.69331 | -45.97509 | 2025-10-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f0bbe41-8491-308e-8250-983eb09c4e8c | -2.98203 | -54.0011 | 2025-10-23 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65701e49-e53c-3b36-b5f3-27549af71816 | -7.08142 | -46.19425 | 2025-10-23 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44ba1fc6-a002-3101-8f30-37ca8412be4f | -4.15023 | -40.91595 | 2025-10-23 04:55:00 | NOAA-20 | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 235264f1-58cf-39fc-9ef6-cde686579727 | -2.73467 | -48.43121 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7b08392-43f7-3aa4-ae87-c45819d6db75 | -7.93659 | -47.18457 | 2025-10-23 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bff4d694-a9a9-3112-8058-a67c65afa1d7 | -3.94822 | -46.97224 | 2025-10-23 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e435e1ac-5bba-31db-851a-5ff7480f2ec4 | -3.47186 | -50.07806 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94d4177d-326a-37a8-b1e6-35f005272042 | -2.80144 | -51.35151 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dfb9945-d77b-3dc6-a48c-aee28072fad2 | -3.48276 | -50.08264 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1e3d7e42-3052-39a9-9917-96e78ebcd951 | -1.79049 | -54.85018 | 2025-10-23 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17f2c3b5-46f8-3411-8fb8-ca62de18cc55 | -4.67736 | -42.72786 | 2025-10-23 04:55:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c76dfb50-a202-3b01-9083-002b802c930b | -3.01981 | -49.48701 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 283f55ae-eb9e-300a-a629-e1bafde0407b | -3.84791 | -52.27897 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e09c173d-4791-3312-a704-f0176bd70562 | -3.96229 | -49.0254 | 2025-10-23 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df2e8193-228f-3667-9f07-397e5ab3f3ce | -6.60444 | -44.21427 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b8ae908-f963-3dd5-9a67-6f82f8b3bd41 | -2.85821 | -50.73732 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9004a65c-8cca-39bb-b1e3-25ccec505e12 | -3.11446 | -51.20853 | 2025-10-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d6a2310-7820-3bdd-b961-87ebabffbb96 | -6.30545 | -41.88283 | 2025-10-23 04:55:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 680cf097-f355-31bb-81a3-3028feab4d7b | -2.80827 | -51.35256 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18eed446-9172-3b11-8fef-a5eac70068df | -2.87583 | -50.71616 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8317436a-429e-3d57-9f24-a35b8c971c9b | -2.56205 | -50.63859 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfd59916-e4ca-3766-9a71-912ff28dcb23 | -3.11898 | -45.23633 | 2025-10-23 04:55:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3f7386a-747e-37a4-92b7-8b5b523c507a | -3.33347 | -50.75111 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 793f9228-5672-3c1f-8dcb-58f6ae3232e3 | -3.1116 | -51.20424 | 2025-10-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a0e40e7-6f83-3845-a714-f61e69303f7c | -4.19243 | -50.11197 | 2025-10-23 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09f4c5ad-70e1-33c0-95ed-289a1f80fde4 | -0.84336 | -48.73523 | 2025-10-23 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1500d7cf-0996-3809-a2ae-28de1c5f29be | -2.25324 | -51.92082 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be2b84ee-536f-35ce-9f05-74b392281094 | -7.62734 | -42.19287 | 2025-10-23 04:55:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa520004-3fa6-3869-8284-cbd2ee92206b | -2.86822 | -50.71897 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d104ab5-62f6-3ffa-9f5d-5b0c423f2b06 | -2.86231 | -50.73397 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a1059e3-b5f1-3921-8954-7615113414cc | -5.69218 | -45.96729 | 2025-10-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ea9b335a-50f8-3b5a-b9d2-b76643237f60 | -2.80908 | -54.38213 | 2025-10-23 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dccf5b6a-6506-3704-adfa-bbeb3b0a0176 | -3.39294 | -50.27523 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cdad9e7-d9d9-306e-9ba6-60d469b66282 | -5.69137 | -45.97279 | 2025-10-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 47d25188-5357-3de7-86fe-69447a04aa1d | -3.14811 | -50.16876 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83f62abb-8ab9-38fa-8ed1-165b39b936fe | -3.22392 | -49.3632 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f74191fe-ec9e-3cb0-a364-873408056489 | -6.45519 | -52.82598 | 2025-10-23 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b923f54-6ce9-377e-b961-7e1f1317abda | -2.86171 | -50.73786 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f28cdad3-f4fc-3c49-99cc-df6817defd53 | -3.25758 | -49.12099 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc7c77b2-d4b1-3ca4-9861-889ba5c45c7d | -1.59934 | -55.75498 | 2025-10-23 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16060800-1952-3e6f-a414-adeaecf3cc25 | -3.80292 | -51.76163 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6796d1df-4e70-3896-bb92-d0d0c4ce2bee | -2.73601 | -48.29159 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d354dc65-931c-3e23-83c4-765ab1c16b5a | -2.84262 | -51.35745 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f61b1c59-b06a-3a5d-b6c3-a199a8e8b4ef | -3.04561 | -49.51841 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9065d006-3a53-345a-aaf0-556f544daf00 | -4.27612 | -50.54659 | 2025-10-23 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9d28d94-6cf2-366d-9f38-83ad3ac47052 | -5.68839 | -45.97439 | 2025-10-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a06ed9da-97cb-34c8-9488-d84f2a33ba0f | -3.84736 | -52.2825 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5afaf2c-df97-3245-9a44-9ed2c3794d03 | -7.5182 | -46.88555 | 2025-10-23 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c9c6405-85fc-319b-80d2-69b34283c964 | -6.94133 | -44.46542 | 2025-10-23 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab92a16c-d598-3b6f-a6da-68a5ff63b453 | -4.19921 | -48.35956 | 2025-10-23 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd30fcd4-5cc0-3a7f-97e4-10674f54e00a | -3.22605 | -49.34943 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bc457d5-9942-3b54-a8f5-d995ec5e6059 | -3.83803 | -51.3314 | 2025-10-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README29.md)
