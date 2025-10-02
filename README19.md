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
| 71e8f148-8932-3b3f-b128-e7178804285f | -3.694 | -49.56572 | 2025-10-02 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e98dcfa-cf6d-3745-8745-9f7e18a18b1a | -5.33328 | -43.76339 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 63bc8b5a-a363-3563-a7d4-3702d8ee0244 | -5.70029 | -42.68197 | 2025-10-02 04:00:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9bf90049-8535-3376-a0be-f126d9aceea3 | -5.82813 | -42.45397 | 2025-10-02 04:00:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cf83e39e-b9dc-30bb-bb69-ca7afe5d1e3a | -4.46281 | -43.62101 | 2025-10-02 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1be985ff-1e2a-3c16-9d2e-15f048818c29 | -4.15189 | -44.85707 | 2025-10-02 04:00:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1c5fc63-ff7e-3eb2-80bc-199cb9459c2d | -3.49736 | -50.26828 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b45a210b-9fad-3af2-887d-996b52dd9258 | -5.34157 | -43.75998 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fc4fbdf9-4f27-3077-91e7-59f262156713 | -3.78337 | -48.6298 | 2025-10-02 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c8a1332-2832-30a5-bfa5-556886e66821 | -5.27726 | -42.87717 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6a98cf03-45a4-38de-b4ac-ef7ffa30de67 | -3.824 | -49.10096 | 2025-10-02 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e6cb5e42-630e-3858-8d8b-4bc17d261f2d | -2.2453 | -47.88614 | 2025-10-02 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d3c27a6-b26a-388f-bc1b-99d94c46b6ff | -3.81421 | -47.57557 | 2025-10-02 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a3632ac-93ba-350a-981f-e326304c412a | -4.868 | -37.45076 | 2025-10-02 04:00:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5cc72c69-e5f7-330f-a2e0-b87e4c222d88 | -3.46885 | -50.08967 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51322e9f-d3a4-3749-b3af-ac8db5f2a1ba | -5.27952 | -42.88609 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 51fd2b52-6a1c-3894-9d4a-7d1e389083c2 | -3.46026 | -50.09154 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2d3449a-3e45-38e7-a33c-b0f4cf767b87 | -4.2617 | -41.77822 | 2025-10-02 04:00:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 631e5bfa-c904-3bf4-a1ae-0139daff894f | -5.40798 | -41.32743 | 2025-10-02 04:00:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1a2c1be6-e29f-3689-a799-2d25dc1c10bf | -3.95344 | -41.59523 | 2025-10-02 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6589fb48-7e15-346f-97e7-e2fdaf413681 | -4.43576 | -40.76092 | 2025-10-02 04:00:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 948e2d3b-9150-3a7a-a83c-a742175ba6be | -5.81921 | -42.8454 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| beb9edfe-8a72-33ff-8306-7d20684d692b | -5.89672 | -38.48454 | 2025-10-02 04:00:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 65b76884-64f4-312d-ac65-a4084bd32850 | -4.89961 | -41.74163 | 2025-10-02 04:00:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 40730d78-02f7-326e-a857-5ccd00a81767 | -3.82404 | -49.10115 | 2025-10-02 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3c3d44c1-a5ec-3320-a14f-30b7282e03fa | -5.8085 | -42.84378 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 10a24971-9aca-3c5c-bc2b-9e97d3beb899 | -3.81469 | -47.57272 | 2025-10-02 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf45020a-7a1e-3c83-807f-88e29ee9bd65 | -5.3363 | -43.76862 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9a1586ed-1649-31a7-a363-536c6111099f | -5.82803 | -42.81322 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 08749ab5-8a15-3e68-8c75-87e94ba57a8b | -4.05456 | -49.0807 | 2025-10-02 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5656d79f-0c7b-365a-b56b-a2d098b3242a | -5.48719 | -42.76572 | 2025-10-02 04:00:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4af037a3-3f7b-3fca-be99-f45f56a1209d | -3.34629 | -43.19635 | 2025-10-02 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 65b6eb98-60df-36de-beba-eb1c43660efb | -5.69832 | -42.69413 | 2025-10-02 04:00:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9180f2d3-bbd6-3d1d-bbe5-4169366eba67 | -3.81232 | -47.58689 | 2025-10-02 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04231e46-df43-340f-bcb4-39db0f015ae1 | -3.09217 | -47.01357 | 2025-10-02 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a480c3a8-c340-3ff0-90ad-44ae164e38d2 | -5.69551 | -42.64434 | 2025-10-02 04:00:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6578a04f-1ac4-3521-aaf5-803b9ce1bc71 | -3.46745 | -50.09816 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3032543-2acf-3bf3-b14c-2c17da761984 | -5.71359 | -42.82546 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bf03537a-b0ba-37ea-896a-f5afc1360e38 | -5.33403 | -43.75879 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 20c60a15-7300-3e77-8540-a486c06a214c | -3.48546 | -50.08655 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 438dc9fd-6223-3c5b-a61c-ad6175ff508e | -5.39462 | -37.70211 | 2025-10-02 04:00:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ca821070-ef3f-35bf-91a8-9caecb0bf2a2 | -5.7103 | -42.64261 | 2025-10-02 04:00:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7797c1d5-361f-3d96-a432-0483a80cb979 | -5.18202 | -42.83796 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d1069bc-ab22-3345-80cc-2fafaf951cf6 | -5.46256 | -42.85009 | 2025-10-02 04:00:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e6e18610-d192-3723-bfd7-d17a33e94a17 | -4.44623 | -43.23969 | 2025-10-02 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c06b1f41-ff6b-3d03-bf89-6df7c79c625a | -5.70772 | -42.65854 | 2025-10-02 04:00:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 79128e5f-eee3-35e1-8abc-bce9cf594192 | -0.90417 | -47.54499 | 2025-10-02 04:00:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 500a96d9-615c-3bdf-b321-1cf572026d71 | -5.33705 | -43.76399 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a6c0f5f1-ef7c-33b5-a0f7-83ac83e8e783 | -5.20565 | -43.04568 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 66eae5f7-8c58-3b11-8dba-a5bb8c2dca25 | -5.75812 | -42.92826 | 2025-10-02 04:00:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f55563a4-4731-31d7-906f-fed42348b256 | -5.40684 | -41.33462 | 2025-10-02 04:00:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2a92afbd-7345-3008-8b44-5e78d7310c28 | -4.40375 | -46.33352 | 2025-10-02 04:00:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8c3da21-35ed-3594-b26a-26230139bd3d | -5.26021 | -42.77739 | 2025-10-02 04:00:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee898899-ab8c-3596-9b0f-dda21be171a2 | -3.09627 | -47.01066 | 2025-10-02 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f38d1579-b095-3914-8674-590e266c6707 | -2.25051 | -47.887 | 2025-10-02 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a22fba0f-483e-3b3f-a730-9084242e08f4 | -4.15114 | -41.52245 | 2025-10-02 04:00:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b8ca74fb-3f17-3325-9ef9-790b69fe17e7 | -3.81729 | -47.58775 | 2025-10-02 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c29e608-7b7a-37aa-a9ae-f4868b4042c9 | -3.6277 | -42.77489 | 2025-10-02 04:00:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1f2b169-8ef9-324b-a7b7-12b0eeb959cc | -3.88972 | -42.52168 | 2025-10-02 04:00:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9160550b-f842-358d-a001-d4afb7f066b9 | -5.69964 | -42.68599 | 2025-10-02 04:00:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f83027c4-0f2d-3264-9733-0a70cb6c1f4c | -5.45806 | -42.83253 | 2025-10-02 04:00:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c9736bc1-3c8c-3217-94b4-0f1c8cfc9f07 | -5.32121 | -43.76623 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d1072c6-98ed-38d2-960b-b2456b6ed780 | -3.8933 | -42.52224 | 2025-10-02 04:00:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c39332f-4049-3758-87ad-39a1e0d6f7c2 | -3.38602 | -50.14746 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a095ce1-b2e4-3a86-8b7d-4e22c358af7c | -5.69197 | -42.6438 | 2025-10-02 04:00:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9881edf3-e320-3eed-a57d-f4344860c2ab | -3.87536 | -42.51944 | 2025-10-02 04:00:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4c6bba07-5744-3af0-80c1-3e2408976853 | -5.28085 | -42.87777 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c6f277e-7624-3c23-8700-141f5626c239 | -3.95403 | -41.5915 | 2025-10-02 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8633c840-2d2a-3974-baf9-5895ce08638b | -5.35423 | -41.15324 | 2025-10-02 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1bb0c8e4-47de-33bb-a931-8fb06a78ba14 | -3.35451 | -43.19301 | 2025-10-02 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ef6fd29-3a76-3e09-a54f-5f68b5f471cd | -3.86653 | -40.33315 | 2025-10-02 04:00:00 | NOAA-21 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bb41501a-163d-3e19-a8cb-c22e966f9fbb | -4.25877 | -48.55729 | 2025-10-02 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 713647f8-5274-3456-849e-f5f8688c61ef | -5.6446 | -42.78156 | 2025-10-02 04:00:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ca46bb32-4302-3f6a-bda5-b30e44f44105 | -5.81207 | -42.84433 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0c0c8bb6-1f9e-375b-aacd-d20573dfa673 | -5.40963 | -41.33883 | 2025-10-02 04:00:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f436935f-fda8-3d0a-b6a8-f99c8e75b039 | -5.70477 | -42.6992 | 2025-10-02 04:00:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 1d0e7bb8-12ee-3642-bce6-79dbfc726918 | -3.17093 | -42.95683 | 2025-10-02 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f62961ea-89e7-3248-8a81-ccb66555ffa8 | -4.62961 | -49.36678 | 2025-10-02 04:00:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 222818d1-8482-31f5-b759-7f11d32ca233 | -5.46322 | -42.84597 | 2025-10-02 04:00:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| da1f6398-8653-3586-8437-b1eb506ce896 | -0.90366 | -47.54818 | 2025-10-02 04:00:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5b6a99a2-3ae7-324d-b797-f9994a209ea8 | -5.2843 | -42.76442 | 2025-10-02 04:00:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3db657b0-6ac5-3c2f-af39-2d1ea7ad0b6a | -5.70121 | -42.6987 | 2025-10-02 04:00:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d05f41f6-a535-315d-bde7-d4e0388291fa | -4.25935 | -48.55395 | 2025-10-02 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce3964a5-6a79-3535-83e9-8a1ee39cc1d9 | -3.9295 | -41.56844 | 2025-10-02 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6588d8c7-fd8f-3448-87c1-d4662ce53f2c | -5.20202 | -43.04509 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 99972b96-58ff-35da-96da-4b9b1cb82a6a | -5.74672 | -42.86337 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6e574fd0-d240-3d8b-86b2-d536c9f71940 | -5.76885 | -41.73242 | 2025-10-02 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da6dcc50-c3c9-3513-9641-0886c3077164 | -3.49662 | -50.27269 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c82ac6d2-01b8-3f47-b07d-da32bc25ffb4 | -2.42451 | -47.14375 | 2025-10-02 04:00:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86d0fe38-0893-3136-97a7-3d9f1b159e07 | -4.8304 | -43.50946 | 2025-10-02 04:00:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 92f7590a-1fb6-3b05-8bb8-c82c7ea8e81d | -5.82214 | -42.84994 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6e6ccc15-afc6-392d-aa4b-124850d462ff | -5.32498 | -43.76682 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0ce8e9a-ea3a-30a9-af8d-f0167ed98480 | -4.52646 | -46.06782 | 2025-10-02 04:00:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f730d792-6f0f-3410-93e9-e0d77bb9efc4 | -5.70872 | -42.83303 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ed526edc-6334-3eec-bb73-1df1ee1fe32a | -5.10725 | -39.21198 | 2025-10-02 04:00:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd93840e-0a41-3260-a9a8-f65d9b23b6af | -2.26761 | -47.84792 | 2025-10-02 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 786930a3-7b47-3114-a005-dc3fedd51fd8 | -5.18767 | -37.65599 | 2025-10-02 04:00:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8f315522-b3ed-3d5d-b10c-a86ff911369d | -4.84579 | -40.79297 | 2025-10-02 04:00:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9582e462-ef3f-3b84-acc6-7fcc428f2a7b | -2.63505 | -48.04137 | 2025-10-02 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d98f3124-b6bc-33d9-bf8e-f833e80fbb7e | -3.78872 | -48.63068 | 2025-10-02 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README20.md)
