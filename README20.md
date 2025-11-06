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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cff7b4a-1514-3782-935a-4012484544fc | -1.14503 | -48.09863 | 2025-11-06 04:44:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44808ef8-e585-396d-bc61-6377fb8d4760 | -3.77389 | -51.71514 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5e6808c-1338-31a5-9177-84f0846b4eb1 | -4.59521 | -43.31727 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26a892fa-3c66-3606-b277-7d206ae50c14 | -1.96173 | -47.51509 | 2025-11-06 04:44:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6227e48a-4a69-3ce4-bfae-697fdc6ab10b | -3.07256 | -52.63199 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b860d06e-37a3-31a3-8fd7-52941320a329 | -3.89771 | -42.55082 | 2025-11-06 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 36591b92-a18c-3b6a-a481-6cbf4e454575 | -4.0939 | -50.9837 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53dfaa89-0bf7-33e4-a335-bdfce90c9c84 | -4.27397 | -50.51053 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44bb667a-4bf9-320d-bed7-ecc768a23502 | -5.46018 | -44.69086 | 2025-11-06 04:44:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7877324f-a40c-3ac9-805c-8b71c8b92bf7 | -4.71346 | -50.82996 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2257b59a-f9c2-39e7-a003-8b499fc4acbd | -1.33787 | -55.46133 | 2025-11-06 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 189d89ee-2497-3d2e-8ed5-7a824ecbba2e | -5.53118 | -46.50606 | 2025-11-06 04:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f05f9f98-b1a5-31e5-b159-9feff0d06062 | -4.77011 | -42.64817 | 2025-11-06 04:44:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| e7d3dd15-aca8-3693-b9a0-e3959236321c | -2.88254 | -52.61557 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 708e549a-a3f9-385e-aca0-04b4ac49da23 | -3.41712 | -52.67636 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dd526da-3edd-3e80-afb5-46ab081a7645 | -5.46601 | -44.68937 | 2025-11-06 04:44:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bbda060-e78b-3424-b5b2-015323ffa065 | -3.86038 | -47.40407 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f7cf186-4bdf-3faf-90d1-3dc2e238a744 | -5.46174 | -44.68864 | 2025-11-06 04:44:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b99d11b-9258-3110-942d-0239cdcee587 | -3.29744 | -52.10384 | 2025-11-06 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df05a761-b0aa-3c34-b989-7fd8e129746e | -2.79346 | -50.31535 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38893438-bce4-325f-9d85-f84bbad8f538 | -2.92919 | -51.30899 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71aaa94f-4aca-3993-906e-90ef40bf94e5 | -2.89489 | -53.12876 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bca4f6aa-b031-326c-80ae-8b9a4e2fd09c | -4.3641 | -50.88784 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1e66593b-a9f9-3f89-8202-943dd6350cca | -2.88187 | -49.83739 | 2025-11-06 04:44:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a70ce49a-f6e8-3b26-8a30-18e9350c4751 | -4.76524 | -42.64741 | 2025-11-06 04:44:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 676974fc-0870-3d17-ad0f-ecfb20ff8191 | -5.59008 | -45.85861 | 2025-11-06 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b28458a-17a7-35d5-8e86-3f9ce8346a14 | -6.12019 | -57.71402 | 2025-11-06 04:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b085f3cb-c16f-3edf-92d7-9fbc6ad82cb7 | -3.98844 | -48.00172 | 2025-11-06 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07198ae6-2365-340e-837a-69090b9ae4e7 | -3.57983 | -55.50919 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adc41d0f-ef12-3212-ad9d-5aca063440c8 | -4.76517 | -49.54088 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7314a0f2-3645-3519-8517-bc8931523a70 | -3.10953 | -51.03148 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 571fde4b-2df2-3312-a558-5cf434f5e346 | -3.22405 | -50.58436 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5b126f1-0a55-3076-888d-5848d1a513d4 | -6.28443 | -44.73744 | 2025-11-06 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f72653da-671a-3ba8-867c-5bf517d77b64 | -4.71677 | -46.43576 | 2025-11-06 04:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bb9a29b-00bf-3f19-929e-baa75365abb3 | -4.87784 | -47.54829 | 2025-11-06 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb74d703-78c4-3475-b0be-1daa2be54cf4 | -3.58803 | -50.49734 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 80b096db-a004-30a4-85a0-d49de5c9c7dd | -2.9331 | -51.30599 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dc10e8b-a4ba-397c-a944-7d6628f82d6a | -3.01459 | -51.39856 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d3f6f3c-000d-33b4-9a6a-26864b458299 | -4.00606 | -49.28296 | 2025-11-06 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebb27168-ca80-3e98-92bc-b8627dee9eca | -6.05331 | -44.16134 | 2025-11-06 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7991389-4914-37d9-9197-1ef83e0f6365 | -4.85458 | -40.62932 | 2025-11-06 04:44:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1dc794bb-2941-365a-b490-18b8267d3a14 | -3.92433 | -47.69237 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e3f89336-4771-31b6-80d1-0d2098d21620 | -4.07368 | -54.10606 | 2025-11-06 04:44:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d491931a-6e26-3edb-a18e-4e6effe5debc | -5.93372 | -41.36969 | 2025-11-06 04:44:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1060ec26-64ac-3696-a84c-f9a6779cfa33 | -6.23385 | -44.31062 | 2025-11-06 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01ae48d5-d984-3c7a-bce1-da7139ef2ff8 | -3.59648 | -49.44437 | 2025-11-06 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1025093f-b70b-3c4a-9d43-2adb0dbf1986 | -3.82739 | -51.35615 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f0a8fea-5347-3f1e-a0ab-e491466e506c | -3.8392 | -51.75089 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aba936d9-b92c-37df-964e-00fed10c9aef | -3.22639 | -44.64555 | 2025-11-06 04:44:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 287886d2-251c-3a20-96dd-0837c96de7e9 | -4.46728 | -49.42282 | 2025-11-06 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49250d1a-55b8-34e0-913e-a0b8e18c0fde | -5.35112 | -43.50673 | 2025-11-06 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8917a9d8-87da-39db-a5ea-8e92d531957b | -2.5906 | -51.34705 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55d4af36-7e34-38c5-a822-a0cb4054b741 | -3.0412 | -49.51406 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4656355d-f245-3d54-a9ad-43761ce56e07 | -3.7711 | -51.71102 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 076b1eac-47fa-3716-bc66-9c3dc9dba0e2 | -3.70213 | -49.90325 | 2025-11-06 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7983ecb2-3a56-395d-a564-8ddefcbe81b2 | -2.89736 | -52.59002 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e8ce9c0-4eaf-34ee-939e-73e7a00eac59 | -5.22408 | -46.87105 | 2025-11-06 04:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acad97d3-76bc-3926-ac19-a8e6fb2a0a50 | -7.83325 | -40.84115 | 2025-11-06 04:44:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0a3e723-b91c-3260-af13-bb5b18e806b2 | -4.41521 | -48.94395 | 2025-11-06 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7e8dba2-15fb-3987-aa47-a337e9026c83 | -3.90333 | -42.54627 | 2025-11-06 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| b40aca9e-1d52-376c-b44b-3204f6522081 | -3.01837 | -51.19989 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ae6ce4e-4513-3006-869f-6434fdf85d38 | -3.05112 | -49.51559 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77fbe514-98a2-3a8d-a4af-a9e13afa0f38 | -3.46013 | -49.83698 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c18ff53d-dc94-329e-8363-4221a04f220e | -3.73347 | -50.69975 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ecfd465-e50e-3867-b06a-4197be7e6a6c | -3.76952 | -43.98969 | 2025-11-06 04:44:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8a65a43-0ebf-3d3e-8ee4-d8a14f455203 | -5.46075 | -44.68682 | 2025-11-06 04:44:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5de1a3e-066a-3215-aad5-23ea493cf15b | -4.38969 | -49.68207 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9994b5b7-359f-34a6-87b5-8391fd9c21ad | -1.97272 | -52.10785 | 2025-11-06 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cad8bb0-772c-3c7c-a0e2-f38a5c6faee7 | -6.05843 | -44.15757 | 2025-11-06 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a54b12a0-a8ee-3141-bba5-931e41da9a7d | -4.29539 | -48.05874 | 2025-11-06 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18f57e05-708e-30bb-88cf-134152390a84 | -3.92773 | -47.70053 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fc56f01d-c4b9-3729-af40-3a103b64ce29 | -4.02428 | -51.01477 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af5d840a-84bf-327b-9879-587efae67db0 | -3.90413 | -42.54093 | 2025-11-06 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 12e55990-6703-3ab0-ab1b-6fbb521b59fc | -5.46444 | -44.69158 | 2025-11-06 04:44:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0244a2b-76c6-32cc-bb76-8c4c559f4680 | -4.99234 | -48.47404 | 2025-11-06 04:44:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a738f662-4d22-3609-a7ee-a014d657a54d | -2.87804 | -49.84031 | 2025-11-06 04:44:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be738d06-507f-3108-b5b8-4dea108c8519 | -3.87035 | -48.33278 | 2025-11-06 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4ec43639-38dc-32a5-b97b-7aaa7cbee2ef | -3.6201 | -43.53848 | 2025-11-06 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 02d679a1-8e21-33f5-9d64-9dc59a9eff10 | -3.36444 | -51.65871 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c9bbfa7-cde6-36f8-9c88-9d6e29dc02c2 | -3.76363 | -51.97647 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c44505ba-364d-38c5-9837-c9873f88a558 | -3.04451 | -49.51456 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bf9c218-4e89-368d-805c-a827e999b2e5 | -4.49518 | -45.92962 | 2025-11-06 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b2ebf0b-040f-3f0c-b7e8-7d82d4c516f0 | -3.59763 | -49.45875 | 2025-11-06 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54d5e29a-f5fc-3a72-a546-727cb383f609 | -4.21845 | -48.351 | 2025-11-06 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bb27c15-cd01-309b-a2f0-ef89579ba7af | -3.92423 | -47.69999 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88140a08-155b-393b-947c-87a0dd823ee8 | -5.15788 | -41.27651 | 2025-11-06 04:44:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b66f6be-c93d-3193-89c1-2b8eebab4c81 | -5.15443 | -41.26213 | 2025-11-06 04:44:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6e37ec1c-68fa-3751-87e1-f84468a7d902 | -3.58871 | -46.05347 | 2025-11-06 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 95144336-ef26-347c-be76-aba348c2f689 | -4.66641 | -50.7204 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95fd1c69-587a-37da-8920-b2f98b7363cc | -3.06906 | -52.63143 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af50224e-3095-3be3-b097-94dc5a7d6e39 | -4.60209 | -50.99638 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6b6cb6e-3712-3260-b014-83090c6ffc7f | -4.98891 | -48.4735 | 2025-11-06 04:44:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fefb1c70-6a56-3e9e-8b59-32a41218cc74 | -4.1071 | -48.0223 | 2025-11-06 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6c9f27db-8efb-3949-aa83-b8da7f2d5848 | -5.65095 | -43.0186 | 2025-11-06 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 860737ef-503a-39a8-a794-c82d36a69409 | -4.3159 | -50.39393 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 602f93a2-4a5a-3b2f-a864-36efe90a45ec | -3.14724 | -53.14151 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0476e7d6-6d8d-3c31-8875-13b1d55bf03f | -3.37753 | -44.10304 | 2025-11-06 04:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89a30302-cdd5-3e4e-9601-12f93e4c304c | -3.70747 | -53.37589 | 2025-11-06 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 999a564d-5b13-3078-91ca-ab5789b0d945 | -4.59638 | -43.34216 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c393fcf6-c8c2-33a1-b927-adb725f7b141 | -5.55072 | -45.19954 | 2025-11-06 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README21.md)
