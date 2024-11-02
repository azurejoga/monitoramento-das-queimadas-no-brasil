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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfc2932b-01bb-3b69-b89e-5b951e28a8ba | -5.11438 | -43.96198 | 2024-11-02 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c1533c6-f061-38b1-9c6f-abcae78e2de7 | -5.11104 | -43.96144 | 2024-11-02 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d48c96bc-0bf4-30fb-b703-e7d23f0147ae | -5.25606 | -43.34748 | 2024-11-02 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40ea0b10-3627-3b5a-850d-8e8abfd6072d | -8.71779 | -44.01979 | 2024-11-02 04:12:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2df4b476-678f-325a-935e-6952794ca74e | -7.79219 | -45.24389 | 2024-11-02 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b696416c-d928-3c7e-95b3-a8e1dfda9046 | -7.7916 | -45.24757 | 2024-11-02 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 194e6296-35b6-33a0-8a08-b6291ca8e613 | -5.67091 | -43.38878 | 2024-11-02 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2e9315f-c642-3550-935c-cfe6f1e07687 | -6.69469 | -43.0591 | 2024-11-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad8cb765-289b-3281-898f-b50c7b799e90 | -6.698 | -43.05962 | 2024-11-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4373457d-c33c-327e-84f3-047064f863e3 | -6.10988 | -43.96491 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc25109d-bae9-38df-b996-449b3d690728 | -6.10655 | -43.96438 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c4f8542-4b8f-330c-a32d-f153414c9817 | -6.10322 | -43.96386 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81534fd1-86f9-3efb-b8bd-2d01d1dc2f71 | -5.72001 | -43.78794 | 2024-11-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18812562-fd13-3900-9f21-ca1139bf461f | -5.56551 | -43.88224 | 2024-11-02 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9d8e61ee-0db4-3475-a9b2-dfe57d74569c | -5.53545 | -43.94225 | 2024-11-02 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26dfc48a-c9ad-33f2-a90e-68ceb81d24f0 | -6.12596 | -43.97106 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fcedfcd4-b50c-3767-a0a2-3370d4a15904 | -6.12429 | -43.98158 | 2024-11-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fc221bb-9be2-322f-a268-c22cf83f5094 | -5.31663 | -43.07059 | 2024-11-02 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 295d5400-282e-3c76-80c8-3fc692acc567 | -5.31387 | -43.06663 | 2024-11-02 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ce9e786-9642-3dfb-b6c1-10a2f8fe4e8c | -5.31333 | -43.07007 | 2024-11-02 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 934b3e5d-931d-35fe-90a2-cd8f1eb7f367 | -5.31224 | -43.07697 | 2024-11-02 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bcd9b9e-d21f-3bee-9a62-b5067a33cb26 | -5.30948 | -43.073 | 2024-11-02 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b150085b-5896-369d-82a4-094457954f65 | -5.4492 | -43.22253 | 2024-11-02 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04944a1b-a765-3f93-920c-3302d68fc6d0 | -5.43714 | -43.25601 | 2024-11-02 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1203fa85-774f-38f2-89f8-e8cc69536b74 | -5.31609 | -43.07404 | 2024-11-02 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d23f4dda-540b-358c-aabc-c41a69983c77 | -5.29268 | -43.33236 | 2024-11-02 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7e9c613-2edb-38ff-82e2-3506d9c1c525 | -5.50723 | -43.86597 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f6f37ee-7e71-3630-8375-a66b486885e7 | -5.5017 | -43.79315 | 2024-11-02 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0bf7cee-36e2-3274-9866-1b5b1dff091e | -5.44693 | -43.5805 | 2024-11-02 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 699465f9-e5a7-3551-ad77-84c84630eb56 | -5.28911 | -43.33141 | 2024-11-02 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ead7f0fa-0d8b-370f-ada6-2559d31bcfa1 | -5.28857 | -43.33486 | 2024-11-02 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c494f138-1166-3e9b-bc90-43dac92192a1 | -4.44526 | -43.6408 | 2024-11-02 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58877c6f-5650-3fc8-9acd-b5b819dd11c5 | -4.42321 | -40.73885 | 2024-11-02 04:12:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7cbac168-65fa-361d-b2f9-bba9a0ae08aa | -6.31924 | -41.5704 | 2024-11-02 04:12:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 13c6412e-0898-3c7b-9841-0c53caa03331 | -6.31867 | -41.57403 | 2024-11-02 04:12:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8637192d-558e-320c-a0c7-b981173e6f22 | -6.31473 | -41.57713 | 2024-11-02 04:12:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2ee8567a-c4f7-3561-a8b3-e897c5f0d708 | -5.47726 | -40.39729 | 2024-11-02 04:12:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c55d54e1-b87b-3c68-9b3d-69117e339cda | -5.26619 | -41.24432 | 2024-11-02 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1383a036-3216-3833-8b51-684e20d6982d | -6.31811 | -41.57766 | 2024-11-02 04:12:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0cd19930-39ec-37cc-a933-f67a832f9a92 | -5.99883 | -41.836 | 2024-11-02 04:12:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c5a69f78-fecb-351c-9071-395fc5e9befb | -5.27295 | -41.24538 | 2024-11-02 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7799d556-f03d-3daf-980b-3d4ec5bc775f | -5.26957 | -41.24485 | 2024-11-02 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d8a292c9-2ad8-36c7-b1eb-2e4cef157bd1 | -5.26674 | -41.24073 | 2024-11-02 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 50b6b980-085d-3e5b-99dd-229f28dfcb00 | -6.33222 | -41.9201 | 2024-11-02 04:12:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2c0238fa-dc6f-3d17-8ae9-6ad44f150053 | -6.1865 | -41.87232 | 2024-11-02 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 47cea841-3219-3db7-bebf-a16c3d8856a5 | -6.01988 | -41.21959 | 2024-11-02 04:12:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf32e823-1764-369c-831e-36bb680606ec | -6.00607 | -41.8335 | 2024-11-02 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e416c494-2c1f-37b8-a69a-07dffb336581 | -6.00217 | -41.83652 | 2024-11-02 04:12:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| af5f9d7f-6ab0-34e0-a32c-a1bf6eb9076d | -6.33557 | -41.92063 | 2024-11-02 04:12:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 869d563d-fd0a-3709-8a3b-66fe03b2eea5 | -6.00552 | -41.83705 | 2024-11-02 04:12:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a5de0680-b154-32af-baae-38a00bcc925c | -6.60298 | -41.37026 | 2024-11-02 04:12:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a56c678-8cd8-357f-9215-919ce0dc7393 | -6.59958 | -41.36975 | 2024-11-02 04:12:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2799d274-a460-3aea-b054-59d60d1506f2 | -4.72095 | -42.12624 | 2024-11-02 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ab5140f1-20bc-3c44-bcff-20897a329248 | -4.58198 | -42.47238 | 2024-11-02 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 87c81479-4031-30ca-9e3c-455141aaca4d | -4.57867 | -42.47187 | 2024-11-02 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 87b7fdaa-0871-38dc-bfb9-c1e739f4c1dd | -4.57813 | -42.47531 | 2024-11-02 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8762676a-208f-3861-abee-a9a1503d6e4d | -4.55448 | -43.09924 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 809faf81-010f-3139-adaf-427e92389ea9 | -4.55394 | -43.1027 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e55c8c65-f30a-3e78-970c-269bb5976046 | -4.5534 | -43.10614 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58e6ef06-c2e5-3dec-b6c6-826bb660f455 | -7.11068 | -35.26223 | 2024-11-02 04:12:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a15f0c3d-b011-3fcf-a6c3-b0a455f3c213 | -4.44637 | -43.63379 | 2024-11-02 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 03cab501-9593-3aaa-873b-cc463a72ad53 | -5.22811 | -43.48156 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52a95454-8416-3a63-a7fa-68c520022d3b | -6.47227 | -35.49513 | 2024-11-02 04:12:00 | NOAA-20 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fe279fb9-a7a7-3782-ac26-8c448cc2a593 | -6.47145 | -35.49732 | 2024-11-02 04:12:00 | NOAA-20 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7dea5805-a9ed-3dc4-86c3-0341ff5eed61 | -5.9314 | -38.3465 | 2024-11-02 04:12:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 53776ec9-0bd3-31da-a744-684ed091bd01 | -7.44302 | -38.14143 | 2024-11-02 04:12:00 | NOAA-20 | BOA VENTURA | PARAÍBA | Brasil | 2502102 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1572a43-5215-3167-99a7-7a76b297bfee | -6.91653 | -38.56407 | 2024-11-02 04:12:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 012a5928-7283-3639-ad44-cd37bd59125f | -6.86692 | -38.35681 | 2024-11-02 04:12:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 31b5fc58-dad2-3cc3-af92-2dc16665c400 | -6.77413 | -37.54285 | 2024-11-02 04:12:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e861eaa-4570-3039-838c-1618951ca36f | -6.68174 | -37.46645 | 2024-11-02 04:12:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1aad75d3-4a05-31c0-8601-873d3d294428 | -6.67814 | -37.4616 | 2024-11-02 04:12:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 29b9b303-865a-3814-ad6f-9fe7e89f6529 | -6.50641 | -39.35397 | 2024-11-02 04:12:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6aaf0cbd-a68b-333c-bf10-0cd9e6e834c8 | -7.23104 | -40.20409 | 2024-11-02 04:12:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a6730ce5-3010-3756-9d9f-ea9abd1e51ff | -7.23042 | -40.20822 | 2024-11-02 04:12:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5e782813-e55e-31ca-b38f-3ffc11a00e6d | -6.68519 | -39.45464 | 2024-11-02 04:12:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d94528c9-9aa3-3a1a-9403-d65d57172393 | -6.62265 | -39.74938 | 2024-11-02 04:12:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1de94985-92d7-34a3-b0f8-d0c469278538 | -6.619 | -39.74882 | 2024-11-02 04:12:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a6b08135-f02b-3674-be0a-9b54fb63114e | -8.60953 | -40.50723 | 2024-11-02 04:12:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5c6a3ae4-705a-3f08-b6f4-04a0f0c84228 | -8.73458 | -40.56693 | 2024-11-02 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| eafcf39d-1886-3944-b779-2e3b7986252c | -8.731 | -40.56639 | 2024-11-02 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 354ea946-9f65-3cc7-9135-1c36a44ad427 | -8.74286 | -40.58504 | 2024-11-02 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2ee08d65-26bd-38ab-ad8a-621f0773815c | -8.8567 | -40.45176 | 2024-11-02 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 29afaca4-8bb1-3d7a-b387-03088b48d2f8 | -8.73928 | -40.58448 | 2024-11-02 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b49067ca-659c-3362-be24-120c61b18cca | -8.73866 | -40.58861 | 2024-11-02 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 57446b91-4b56-31eb-92c5-acafc9b37724 | -4.23278 | -40.40346 | 2024-11-02 04:12:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 467fc289-9a68-3874-8b59-123d7736e401 | -3.8652 | -41.03653 | 2024-11-02 04:12:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a6346b60-262a-340a-9f84-1e218ddfcc5f | -4.63609 | -40.72111 | 2024-11-02 04:12:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eff64d1c-7c2b-37f8-9ca1-abffcae4455e | -4.55172 | -43.09528 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a06d519-81ed-3af4-87fd-a350827b2549 | -4.55117 | -43.09872 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e17c2046-456d-33bd-9842-562c97442d0d | -4.55063 | -43.10218 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f07e6b0-5a11-38f4-95e6-026da7f64f34 | -4.54895 | -43.09131 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63346ec1-fc53-388d-ad45-88873ccf015a | -4.54841 | -43.09476 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 307351ea-307c-32a3-87d0-36278fe42154 | -4.5451 | -43.09424 | 2024-11-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 408f14a8-1a84-364c-aff8-f83e420275b3 | -6.11963 | -42.67467 | 2024-11-02 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e1e55120-5154-3527-b674-995877611e78 | -7.29933 | -42.21055 | 2024-11-02 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c6817d53-0420-3e4a-ac96-cef33ce0bfdf | -7.29878 | -42.21408 | 2024-11-02 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fa7ea97e-4e69-37a8-b244-128764aec3d0 | -6.77603 | -42.36405 | 2024-11-02 04:12:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ba02e3d4-6d6e-35b0-9b62-b70a4034c19b | -7.91457 | -43.79129 | 2024-11-02 04:12:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 77e116ed-f3b6-3985-9452-bd27a3514439 | -3.49258 | -44.20855 | 2024-11-02 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e19d6307-e711-3eb5-824e-8357cd5069e5 | -3.38562 | -44.24101 | 2024-11-02 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README37.md)
