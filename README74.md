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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40a0fd67-ab88-3dab-bf4a-c70934cf28d0 | -1.25549 | -54.22594 | 2026-09-23 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 363e22d0-1413-3ae8-8a79-62746ddb7f5c | 0.78136 | -59.20415 | 2026-09-23 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c74f6e35-904d-3020-b7c3-f0d804c479a9 | 2.13478 | -50.73077 | 2026-09-23 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a188a765-687a-3c58-98a1-62660cd2850d | -1.2985 | -55.83855 | 2026-09-23 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 005389c0-12bb-38bc-90fb-683f35f5ccf5 | 2.78112 | -60.2271 | 2026-09-23 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e556601f-1053-302b-bdfe-5cc72ce9bc5d | -1.41592 | -49.30067 | 2026-09-23 05:01:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c9d5151-e5d7-3670-bcf8-f02261570204 | -3.20556 | -50.9173 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c97dbe5-a893-306a-80d9-ebb87ddfb8b8 | -1.82921 | -55.71598 | 2026-09-23 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6219310-5702-3dce-94b8-a4019a36a555 | -3.82259 | -52.40166 | 2026-09-23 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdac5874-ed3e-3083-a0ec-2d7a5c8f741e | -3.22229 | -46.94357 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7f5b29a5-93c6-3a16-a710-f9a32106713c | -3.5901 | -50.03011 | 2026-09-23 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcc39ef6-0077-3fba-9b85-914d320f59c3 | -2.23857 | -48.74895 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b151cb7-8215-36af-b387-67e3d8bc665f | -2.45326 | -49.21881 | 2026-09-23 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 5903d708-7388-31cb-a4a1-e8f4fd6587f8 | 2.33323 | -50.76631 | 2026-09-23 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5a80bde9-98e6-3e49-8615-a4515c622b82 | -3.44646 | -50.609 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f70e733-8eb2-3be4-b43e-5162a4a2044a | -2.94149 | -50.49115 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a386dff-93cb-3814-8a14-42bb006c6d0a | -3.01443 | -54.18655 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70f0895e-3086-35bc-8c20-d7897bc68893 | -2.9803 | -54.15358 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a19b7cbc-800a-37a4-9b84-8893a4e6889f | -3.44196 | -50.61561 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 494d5c01-3d96-33ca-bc95-c7f6736269e7 | 0.79145 | -59.20249 | 2026-09-23 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7034940-bbaf-3ab4-877a-dffbf4482579 | -3.88013 | -51.95344 | 2026-09-23 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a00a264-1441-3318-b467-7e008322fa70 | -3.03207 | -54.41246 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb099ee6-b01c-3d93-979c-f297288e5268 | -1.11957 | -54.12434 | 2026-09-23 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c324baa-41e6-35c9-a141-c09a40e90463 | -2.95178 | -54.0789 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e66288b-2225-38d8-a853-87f67d050f00 | -2.46222 | -57.91499 | 2026-09-23 05:01:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21f3bec8-87c0-35ec-96f5-ccf74b5377ad | -4.19201 | -49.2969 | 2026-09-23 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d2bb0fc-4afa-3d84-a699-6208571395a7 | -2.72878 | -51.55578 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 762475be-0851-3cbc-89be-bf3962bcbd95 | -2.95946 | -54.08344 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e94740d-e82b-35c6-801d-4483cd40006d | 2.33655 | -50.76579 | 2026-09-23 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 41cc1b97-4516-3bdc-8d51-018a7d94d465 | -4.45874 | -47.92122 | 2026-09-23 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| fc949a2f-18e3-39f1-a119-761a2081aa78 | 1.04095 | -50.01832 | 2026-09-23 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5698a82-c13f-3c6f-a8b0-9d66bf303432 | 1.77276 | -60.23553 | 2026-09-23 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 479383ec-e560-301a-a316-4f0a010873d3 | -3.04745 | -54.4069 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8d33b3a-ecbe-31a4-b6f2-729d1e1325ce | -3.23916 | -53.95634 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e89dfd74-b47c-3ca8-8b3c-232d700af684 | -3.04972 | -54.41526 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94b52bd3-583c-3dc8-8519-8e27c77b00e1 | -2.41688 | -58.27284 | 2026-09-23 05:01:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 04ff66cb-0c77-3595-bc10-b083d844dba1 | -1.3806 | -49.04829 | 2026-09-23 05:01:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 804c3b76-fc23-3d0b-8e03-bbe9c0c5bb4b | -3.36233 | -50.7643 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cadbfee4-0089-3a40-b682-2c1e72d0adc3 | 1.91005 | -60.5809 | 2026-09-23 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3733be8a-95e3-343d-a84a-3108ccc7def7 | -3.24667 | -53.95371 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7df3634a-c150-3997-9cd9-8fbf0a75c7e3 | -2.94873 | -51.04225 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fa8f02a-4761-3b2c-855d-1f831af9c923 | -1.33397 | -54.66964 | 2026-09-23 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04ef57c7-0250-306b-8791-35acc6ae612e | 0.3683 | -51.0504 | 2026-09-23 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eace21e-f514-3502-9320-4aebdbb60188 | -3.23976 | -53.9526 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5f713e9-e0a2-36f7-bb6c-64b604afab84 | -2.62767 | -51.70262 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 090b1ff7-a7ab-3451-9301-d27e9f47fd3b | -3.22878 | -53.9547 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4b88446-2aab-3233-84ee-47c6aaa45096 | -3.25525 | -53.96658 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 162b23a0-da82-3c0d-85ca-7bb323f4b24e | -4.46259 | -47.92181 | 2026-09-23 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 477e5672-17cf-3174-ae19-a76aee6fda8a | 0.60258 | -50.79837 | 2026-09-23 05:01:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 614d199b-f001-3dbe-a50e-88887be0171a | -2.82497 | -49.23727 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20bfdb96-302e-38d8-abf1-8a0832425391 | -2.83164 | -50.47792 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9c12284-eb38-3883-8e88-47c49ba50165 | -3.44252 | -50.61204 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41906a65-cbdb-3455-b542-7c4edc3cf5ba | -2.74372 | -51.5475 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3f28728-d368-33ee-9ee4-f6cba49e4a78 | -1.82536 | -55.71541 | 2026-09-23 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 659421cb-0d5a-371e-ad36-5de39b9a49bd | -2.88102 | -50.23109 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b97c2e9a-46dd-38ac-8d6a-32f37273a413 | -3.00455 | -54.1811 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a55b36c-b440-38e9-b6cb-8acef2d6c504 | -3.66892 | -49.18506 | 2026-09-23 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b2e14f9-b020-357a-82b6-295f7270f02e | -3.15142 | -48.06881 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4752c742-2bab-348a-9bc0-44fdf3b67ed3 | -3.52156 | -51.6346 | 2026-09-23 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a047d1f1-256d-3114-af85-7affb83bf38e | -2.97743 | -54.14923 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da0b587b-b534-3a06-82c7-0a4eebf99153 | -2.82021 | -49.24456 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea456355-4ff9-36df-8a2f-18889e3c4b42 | -4.2998 | -49.12969 | 2026-09-23 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| deba8636-cff2-39cc-ac08-608f5c8a439b | -2.93811 | -50.4906 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b92263e-772b-3d53-9e4f-392fae3bb350 | -3.3613 | -50.46387 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad73519a-1b50-38b6-902d-a6ff0a502435 | -2.9675 | -50.39233 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56172426-5003-3b23-8004-4ca6aebf54d0 | -3.2363 | -53.95206 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbeed00a-b880-3769-81be-e594cdce01c8 | -2.82435 | -49.24119 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e3e18e1-7758-3ca5-b550-4b1f0ccba0ab | -2.95057 | -54.08654 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 204da686-c551-32bd-9ed6-ac925fb6922e | 2.08895 | -50.95707 | 2026-09-23 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93bac8d2-a9b5-3cbf-9901-cebc388b4ca1 | -3.04519 | -54.39851 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a08fa2dd-cd19-3117-94a6-c92455a1d2e7 | -4.22291 | -48.61585 | 2026-09-23 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6ef6945f-3b4f-382d-a312-5b1027b514fa | -3.58322 | -50.02901 | 2026-09-23 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb041306-6f34-3302-919a-1803c1ec2297 | -3.23224 | -53.95524 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 534700e7-6e44-3630-9b50-1a9fe87d23f6 | -3.44984 | -50.60952 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1d1e606-86a3-3924-9a6d-249494ed6e8d | -1.91774 | -58.26156 | 2026-09-23 05:01:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3f25ef6f-ac33-38c1-80f2-ab78180ed0d4 | -2.95598 | -54.08288 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48818032-6f0f-3421-b5f5-abad18861d59 | -1.4292 | -49.30662 | 2026-09-23 05:01:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf60881e-bceb-3ebf-a5e4-e2276156a276 | -3.45322 | -50.61004 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2759de01-6eed-3a52-8940-fcda0e22f241 | -3.2258 | -46.94762 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 69fdaf3e-954f-329c-8532-4ec26e69f8c3 | -3.88291 | -51.95742 | 2026-09-23 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0b67648-a08a-3dbf-8583-8dc3447d611d | 0.17505 | -60.48817 | 2026-09-23 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d30d28e1-dcf8-3843-8899-224e2e4db3c6 | -3.77225 | -51.35344 | 2026-09-23 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07eb8184-36b0-32cb-831d-7111fce4af7e | 1.43908 | -50.82578 | 2026-09-23 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87b630ac-0f9a-3807-8761-ded5b29b0595 | -2.97766 | -50.39391 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0fe4a7f5-8a8e-39b3-97e6-3f8de055c033 | -3.0167 | -54.19481 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e194c905-ee72-38d1-9d4c-a25574135a36 | -3.58951 | -50.03382 | 2026-09-23 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3bad209-89ac-316a-8b4f-b78b3587de7c | -2.51078 | -56.60939 | 2026-09-23 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 851c0bfd-2aaf-3934-8fb7-4d7290d85f07 | 2.46799 | -50.97499 | 2026-09-23 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eeac5147-d241-36d1-857a-bc7c5e3d84c4 | -2.88377 | -54.07984 | 2026-09-23 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38db17a1-127b-3b20-816b-4a3361e02169 | -1.71955 | -49.98294 | 2026-09-23 05:01:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6daefa9-07fd-3450-aeac-10a28a63dead | 0.60557 | -55.98521 | 2026-09-23 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d0df995-aa54-3e17-9283-39d935b18d15 | -1.63402 | -55.12171 | 2026-09-23 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed1d741b-921a-3abd-85c3-ded736e96568 | -2.92508 | -48.74231 | 2026-09-23 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f0a35bb-b81a-3dc5-83db-33b77f0f1a21 | -2.54768 | -49.10093 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43f35e74-e4d5-39d9-ab1e-30b9f97f80a3 | -2.48538 | -49.05894 | 2026-09-23 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29afbabd-055f-3c3e-ae5f-9e93e4497b67 | -3.20806 | -53.95124 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea09e2ae-d629-3b52-8ddc-0bf59a342f0e | -3.08581 | -51.28547 | 2026-09-23 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4c38c5d-4a50-3d62-ab4a-ce1a5b19d2d3 | -3.93704 | -49.98984 | 2026-09-23 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7a84aa77-b094-3885-af3e-ff1ff8469b41 | -3.62318 | -49.99266 | 2026-09-23 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4213b61d-73ed-3a75-b3fe-64e144018c3a | -3.88623 | -51.95794 | 2026-09-23 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README75.md)
