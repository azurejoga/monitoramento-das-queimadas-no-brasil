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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07f2e1b8-4c51-3ef9-b96e-288fb2c8e01f | -10.78777 | -44.76574 | 2026-09-02 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d47b9330-2a43-378f-8ca4-6486876d2e2b | -11.52909 | -45.49294 | 2026-09-02 03:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 321e76e0-2225-3853-90c4-c71228d9f973 | -15.42909 | -41.80794 | 2026-09-02 03:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b79f46be-c7e2-3c56-8826-acbb2df828d5 | -13.40689 | -43.87326 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c57970a-8e9d-346d-bec1-d436b0d2c785 | -10.90693 | -45.37637 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e4434c2-5f12-3990-a27f-b4dac48863ae | -15.42444 | -41.8069 | 2026-09-02 03:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2c1a2985-6bf7-377c-a0f9-03969c7d6be9 | -11.34282 | -45.41427 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5cda1dd-5c75-36f6-88c3-7512333ea30b | -12.14003 | -47.0792 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 24990ecf-b1cf-35d0-b154-85aadda3ab51 | -11.3577 | -45.40546 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 316eb70f-a456-36f9-b5d5-dac3218fdf84 | -10.89757 | -45.35735 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1da6058a-8c17-35d7-a7b5-1893cffd3e2c | -15.36363 | -47.69811 | 2026-09-02 03:38:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78114690-cce1-340e-8dab-7efaf61367aa | -12.12966 | -47.06012 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 94867bec-38af-3221-a0db-2a95c7adaefa | -12.05732 | -45.01187 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 976f89fb-ccf0-30f6-a768-868848b046f2 | -12.12767 | -47.10368 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16e65a2d-ebfa-306c-baaf-e7737bd96798 | -12.12233 | -47.06173 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b03ef45d-b528-3972-a082-5b0b47061c6a | -12.12283 | -47.05867 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1afa2400-b4df-329a-b286-626205bf238c | -12.13309 | -47.11183 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4cbef4d-82e4-36cf-ba95-2ee0539cff8c | -12.12366 | -47.08892 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b99afe7d-4ffd-3b7e-bbf7-08c29567813b | -13.75144 | -43.82974 | 2026-09-02 03:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3907f397-46c2-3117-a151-674902cf4ba9 | -15.83576 | -47.70466 | 2026-09-02 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6a1e25d-b5d7-3513-aa4d-d3acbf3266fd | -11.53628 | -45.48988 | 2026-09-02 03:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ce404d1-520b-37ad-ae6e-dcdec0670518 | -15.8306 | -47.69646 | 2026-09-02 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 000aa988-aef4-3f6e-a459-bea5795d0987 | -17.79226 | -39.70667 | 2026-09-02 03:38:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 09c7ebef-d081-3988-937b-22d42ca072e7 | -13.41143 | -43.87333 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8b1e188c-c97b-3f5e-a793-497332543e62 | -13.75173 | -43.82834 | 2026-09-02 03:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c726c4e0-76d6-3280-9e30-5f5a259bb991 | -12.12369 | -47.05534 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0503a8b-bd2c-34c9-ab00-69a9c8d3f4c6 | -12.46659 | -41.31373 | 2026-09-02 03:38:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a752616e-58ec-364b-bfa3-53f6104a1455 | -13.41544 | -43.88192 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b8d7f698-c3b9-38b2-83bf-6d968997ef9c | -12.13864 | -47.08576 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 22c15b36-20d8-339a-9b12-12f618ceba5b | -16.22173 | -47.48551 | 2026-09-02 03:38:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4a1bdc56-fdb1-37b9-b3ab-98843865f466 | -12.34901 | -45.66509 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29b00dce-aa0e-31fc-8b1a-f1887b498c97 | -10.69555 | -46.21711 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 514a8fd6-dc78-3fd7-b59b-f1999bb5cab2 | -12.09173 | -47.10511 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ba2a2618-7180-305f-9c15-61b334320e9f | -12.12701 | -47.07294 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74c68791-b01e-3570-aab0-5b0f1cd43a51 | -13.37673 | -41.35049 | 2026-09-02 03:38:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c6eaad5-6516-3cd6-bdf3-2ddfdb13cf5a | -12.13927 | -47.08275 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 699171d3-662f-3f22-8975-37ec76bc54d9 | -10.77732 | -44.75597 | 2026-09-02 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f138cc00-2101-3580-9f69-951fd9a52cc2 | -10.90277 | -45.36426 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62f1cf9b-58e0-32e6-99bf-174683c658e1 | -17.65913 | -40.25257 | 2026-09-02 03:38:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 11e878c9-94a3-3177-b6df-6a182b47c886 | -11.35656 | -45.41114 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0caf63f9-63d4-378f-abc5-c6f531a4c841 | -10.90393 | -45.32573 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 0eafbc2f-d1e2-37be-a011-c8487f3b0e27 | -12.12151 | -47.06506 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f17811e-a1a5-3b6a-9271-51fc6f85276e | -12.13572 | -47.13314 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ceae409-14b5-3545-9088-ffe56ed1c166 | -14.97313 | -48.12699 | 2026-09-02 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0a60c01-7acd-3dd5-a59f-c70dc82131b2 | -12.12642 | -47.07599 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd237a51-a8aa-34c0-bd73-393f78b8b414 | -12.14197 | -47.06965 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 160c43bf-cade-3c12-9a42-64fe9286efe5 | -12.13154 | -47.15279 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0187c926-0c6f-3f24-854d-157dd5d77d58 | -12.1345 | -47.10522 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e048698-c89d-3f5f-b3ab-7bb356cfe161 | -10.8871 | -45.34396 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 735b5ba8-4a32-32d9-8830-3e999c0e63b5 | -12.14821 | -47.07434 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c390d69f-fc03-3afd-8478-43b44eadd2c9 | -12.1216 | -47.09909 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2411d3a3-9c7c-356b-a51a-9dd1ce52d5a0 | -17.67579 | -40.14022 | 2026-09-02 03:38:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 784c0093-f874-3475-acf4-ab9e69fe950d | -10.87964 | -45.34831 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73acadbc-7f4d-3194-9bbb-ad0f324aaf30 | -10.44087 | -46.7253 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7ffa5a1-ea22-311d-9b3b-98f9b54a21ee | -16.4359 | -42.40578 | 2026-09-02 03:38:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 231f9779-4da8-3ed3-9f6d-55984893611e | -12.07419 | -47.11907 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe60d366-63a4-3628-8143-0a966e606a37 | -10.70448 | -46.20751 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6f67458-7831-3d26-b825-ef7b3ee05ec8 | -15.37169 | -47.69347 | 2026-09-02 03:38:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed107882-0238-31ab-943b-ff682287bf68 | -16.2206 | -47.48485 | 2026-09-02 03:38:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8d17cc83-5f9c-3af6-94bc-c18041d1a11f | -14.96089 | -48.1169 | 2026-09-02 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 101b41f6-a830-3271-badd-a53ecd842131 | -10.9019 | -45.33581 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 70dfb550-3e00-3796-a508-a81604e7a1b2 | -13.70689 | -43.88151 | 2026-09-02 03:38:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34d26361-4ac9-3617-92cd-9e088303c219 | -12.13053 | -47.05676 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dd7ec2c1-1fbf-379b-ad49-4aea9078b5d5 | -10.89452 | -45.33978 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1a44bf71-3202-3833-853c-d6e7ffad60d1 | -10.43692 | -46.74477 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f59a7a72-f399-390d-a193-93ab1ed83740 | -11.91195 | -40.66209 | 2026-09-02 03:38:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9022f6e4-a7d9-324e-a922-6fe4c8e1bcf2 | -13.40616 | -43.877 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e0b657f8-99ea-33a7-9841-4ef83fc09176 | -10.77732 | -44.75437 | 2026-09-02 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2173ac81-c149-349b-9914-d873698ef1d7 | -12.87273 | -45.83354 | 2026-09-02 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aef039ac-fe58-3965-a3c5-bd6fbb6e3b9e | -12.18979 | -40.40918 | 2026-09-02 03:38:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5eb690a5-5a79-3901-b334-b9aaec1e2173 | -15.83357 | -47.69783 | 2026-09-02 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36977de0-3901-3fd8-8a3d-1767a3624297 | -11.53123 | -45.4824 | 2026-09-02 03:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c52131c9-1f96-3487-99f4-f92126623392 | -12.05645 | -45.01618 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c186c9b4-9f84-386c-8514-60fb9dc46bc0 | -12.1398 | -47.1477 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cae2e818-1508-3c1f-b1bf-f4595b30c02e | -10.89123 | -45.35613 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f93b201-7607-3fe1-85ae-f79685c7e8f7 | -12.14682 | -47.08087 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 53494f62-7844-3d82-80ee-94704a25bffa | -10.43744 | -46.73783 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65cfec5c-24cb-3575-a692-7eb37afaa6ad | -16.44797 | -42.41983 | 2026-09-02 03:38:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aea9328d-eb06-3231-af23-453d4041b770 | -13.06998 | -45.14722 | 2026-09-02 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9df3f0ad-9204-369a-94fd-a7b4ae517ca5 | -13.41095 | -43.8819 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d1d74423-02e2-3e53-a3d8-03a9185447ca | -10.70135 | -46.20706 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 682a99cf-db9a-3550-902b-b99cc97793d0 | -12.13711 | -47.12659 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f394299e-9785-3a82-a487-d391b154f77d | -10.89345 | -45.34513 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 127eb252-7511-3b1c-8f13-90e83b413052 | -12.07136 | -47.13216 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08fd5b45-5374-316a-b063-6d7e43e2c752 | -12.15083 | -47.12951 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 14d77399-3db7-3058-b7dc-a6791a08ae93 | -13.75075 | -43.83324 | 2026-09-02 03:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecd325bb-0c66-3b94-9a3e-056cfdb900c8 | -11.82964 | -46.06283 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 160ba7cf-aef6-3d02-80e5-43fa7b09bdb2 | -16.72641 | -47.07713 | 2026-09-02 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 878fbcc3-ec6d-351b-aa9c-0858e1bf29c5 | -12.05187 | -45.00751 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34c921ef-949e-3abf-b509-45fbece3be27 | -14.96784 | -48.1182 | 2026-09-02 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37edac19-c996-3d67-892c-cca82b048d04 | -11.83078 | -46.0573 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92215047-1f7e-3b13-a8f5-d6f8136a868d | -12.14676 | -47.11489 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ed37dd88-0309-3545-94bb-2935065a8e39 | -10.89643 | -45.36301 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2112c665-8f33-3534-a63d-45741a868dd5 | -12.0645 | -45.00759 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a0718de-0c76-3113-a824-3cef592b2f74 | -13.40542 | -43.88076 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| edfc6183-05c0-3e88-a0c4-25d6f864c4dc | -12.11346 | -47.10387 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 67dd62ee-fe8c-3428-b8b1-5ada7d13f660 | -15.43004 | -41.80293 | 2026-09-02 03:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3fae360d-d90d-3fd5-a804-980e5dfd5a5b | -16.21455 | -41.80641 | 2026-09-02 03:38:00 | NOAA-20 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| de36c927-bc8e-3ffd-9f82-278e345e4db6 | -12.1496 | -47.06782 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 47aaf3b1-ae6f-3d01-a9df-9ec41705f41f | -12.12225 | -47.09551 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README16.md)
