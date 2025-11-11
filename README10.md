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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41d44f2a-949d-3831-8f16-039d41b84994 | -6.08947 | -41.56307 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 230fcd88-308e-3c09-8553-0aa4942904c0 | -5.3029 | -40.9139 | 2025-11-11 03:40:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eda6f627-969a-3cbb-a74f-a0ec2210207d | -9.67243 | -43.90395 | 2025-11-11 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b964a3f9-1c12-39a6-b1af-6af296be7c53 | -4.59709 | -45.48643 | 2025-11-11 03:40:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20a11856-fb92-38b1-bb4c-ab05944b1764 | -5.65176 | -41.05613 | 2025-11-11 03:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3ba2da92-1468-3889-845c-60ae7c2991f6 | -6.55224 | -44.46857 | 2025-11-11 03:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 121534d7-0316-30b1-8d0d-6b58140f898a | -9.98311 | -44.45478 | 2025-11-11 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7ecd22dd-4fdb-3007-b058-b7390c85c55c | -11.0448 | -45.4016 | 2025-11-11 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 64b40f9a-f9e0-3960-afaa-9f92e77ad56f | -5.42518 | -44.64365 | 2025-11-11 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7e276b9b-5948-3aa9-8f23-c24f38cd4873 | -4.71999 | -46.45935 | 2025-11-11 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 4e73ae5b-aba8-3764-b70c-4ae46a93e63b | -6.08846 | -41.56874 | 2025-11-11 03:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0364c8f3-957c-33dc-98e4-fdfa18af6c31 | -10.49673 | -44.93225 | 2025-11-11 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e8d5e5b-6e71-398d-abdd-dd673655c218 | -12.33012 | -43.65685 | 2025-11-11 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a6524e0-fe0e-3284-991a-b1806ce8a27e | -12.3358 | -43.65483 | 2025-11-11 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 543e873f-2164-37b0-a845-4c25c1c77192 | -12.56705 | -43.90999 | 2025-11-11 03:42:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 522f0c7d-0f56-3378-ad55-1978b0242301 | -12.34031 | -43.65894 | 2025-11-11 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73c2a91e-1df9-3548-80ce-2bc502ffc4cb | -12.3307 | -43.6538 | 2025-11-11 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45a556c4-c922-3bee-ad09-0f20b60adb8e | -12.3409 | -43.65587 | 2025-11-11 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 035d63ca-ea10-3ad6-8b20-7a7b68dcf2cd | -15.85469 | -44.54319 | 2025-11-11 03:42:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 730e5f0e-710d-3cca-9535-82ccdf417069 | -11.57623 | -44.8532 | 2025-11-11 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1296f5c-f5fa-31ff-be55-eccdd7f9da93 | -12.01702 | -43.85473 | 2025-11-11 03:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb0a0429-44d7-3524-86c1-d64c5da71c06 | -11.90946 | -43.82315 | 2025-11-11 03:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6d1f934-c21e-341f-bc72-cd9d2c695d75 | -16.1916 | -44.27779 | 2025-11-11 03:42:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd8f2473-5adb-363e-9e82-bb33e2fd814b | -12.93406 | -43.59972 | 2025-11-11 03:42:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 867ff2d1-de0f-334d-877c-824f9ed4406a | -12.56764 | -43.90685 | 2025-11-11 03:42:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3436f6fd-0b60-3101-99d5-a1d2e38344dd | -12.01243 | -43.85051 | 2025-11-11 03:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecc8a013-074f-3d58-910c-2726da81d029 | -11.90825 | -43.82957 | 2025-11-11 03:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b408778d-2a6b-3589-bebf-105b53e6c199 | -13.46222 | -44.03332 | 2025-11-11 03:42:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dcc330b-77a6-35b5-8f5c-7322a1e713ae | -12.33521 | -43.65789 | 2025-11-11 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bcc4bb5-e9c1-3335-8421-66fb92263fa9 | -12.93908 | -43.60074 | 2025-11-11 03:42:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2a7a1c35-a94f-3e93-9a1d-36d08ecbfd68 | -12.01763 | -43.85152 | 2025-11-11 03:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b687b4e-7356-32e5-b816-37842ae8aff9 | -15.85406 | -44.54634 | 2025-11-11 03:42:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 248b5d35-b2f7-3678-be2a-48dbfef39d8f | -23.02717 | -47.48963 | 2025-11-11 03:44:00 | NPP-375D | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 30ab5376-e872-3122-850e-c417297ede92 | -18.18815 | -46.92585 | 2025-11-11 03:44:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1eceda22-c3c1-3288-8f9f-a0ea7a4afd4d | -20.74869 | -49.77286 | 2025-11-11 03:44:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 27c924f3-0a6f-3b5d-b52d-90eb59090830 | -22.97972 | -47.24088 | 2025-11-11 03:44:00 | NPP-375D | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 06e2d7cd-0b59-33f6-81ea-d143507530de | -22.98491 | -47.24224 | 2025-11-11 03:44:00 | NPP-375D | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 17221c12-ca17-3e71-ab2d-02f9e84607d0 | -21.58411 | -48.35444 | 2025-11-11 03:44:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04e12129-8b85-32a9-9fed-956ca16e86b3 | -20.79409 | -48.35366 | 2025-11-11 03:44:00 | NPP-375D | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59759be4-178c-3501-bfd5-e8b19e7d38c9 | -21.58471 | -48.35283 | 2025-11-11 03:44:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5e08d15-ea44-3cd3-9247-9514ee24d3ff | -18.19386 | -46.92671 | 2025-11-11 03:44:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86877362-a02c-34b8-866c-d02447bb9dad | -17.87185 | -45.54628 | 2025-11-11 03:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c585fff1-9bfa-3dd2-be92-c7fd9bf71107 | -21.58511 | -48.35003 | 2025-11-11 03:44:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6bef29d-68dc-3ad8-bb37-00ae4dfd0a44 | -18.0341 | -46.78476 | 2025-11-11 03:44:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7dcb2bc-230e-384e-8ee0-4b7f81c5f690 | -20.74356 | -49.77167 | 2025-11-11 03:44:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e9982446-64d1-348a-b84e-b9a049587518 | -21.58573 | -48.34845 | 2025-11-11 03:44:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc43a638-a741-33ac-99e6-5062f99da18b | -22.38816 | -46.81345 | 2025-11-11 03:44:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bae14dcc-8ad6-3ce3-bc5e-80908d967873 | -20.74241 | -49.77118 | 2025-11-11 03:44:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 03404a94-109c-3d3d-8abd-ff84e8597921 | -22.67891 | -50.44255 | 2025-11-11 03:44:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07830537-033a-3eba-a1a4-826bdd999701 | -23.02639 | -47.49311 | 2025-11-11 03:44:00 | NPP-375D | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5dce646d-0e5c-38c3-9b8e-7b729046ca86 | -20.79311 | -48.35796 | 2025-11-11 03:44:00 | NPP-375D | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4d4f528-0285-3c43-a785-0fff5496221d | -18.03736 | -46.78234 | 2025-11-11 03:44:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9017ee71-a1c5-30c2-824d-b71749fcc2e5 | -22.38741 | -46.81682 | 2025-11-11 03:44:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef5b9942-26e0-37c9-b9fa-ec84572b12ea | -18.03091 | -46.78513 | 2025-11-11 03:44:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f737e667-2427-37c6-8bb0-963c1925475d | -18.035 | -46.78064 | 2025-11-11 03:44:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b3494f1-0fa5-3fd6-bae7-cfa7e83026b8 | -18.03178 | -46.78103 | 2025-11-11 03:44:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22b5444a-ecf9-390e-929a-72e0d1ffbb15 | -17.87193 | -45.54582 | 2025-11-11 03:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfebd3f8-f545-3d67-8dc0-189412b05d37 | -22.6775 | -50.44829 | 2025-11-11 03:44:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1bafa618-0c18-3f9f-857d-eb0ae707b145 | -18.18725 | -46.93001 | 2025-11-11 03:44:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5fc910a-3ff2-3f7b-82c9-1449d8d396ef | -18.03823 | -46.77823 | 2025-11-11 03:44:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77da1329-efb8-365c-a9b0-1c330807bf6b | -26.69651 | -52.47068 | 2025-11-11 03:46:00 | NPP-375D | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9f3d56a5-b4e3-3dba-8c69-b76283d766a9 | -26.69794 | -52.47012 | 2025-11-11 03:46:00 | NPP-375D | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b067ecbe-831a-385d-9c84-1fbfda688c53 | -26.69811 | -52.46468 | 2025-11-11 03:46:00 | NPP-375D | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 42606667-608f-31a7-ba53-8ad29af4e277 | -26.60946 | -53.16761 | 2025-11-11 03:46:00 | NPP-375D | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c28d524c-79ba-30d1-af35-30eb97e6b985 | -26.69135 | -52.46885 | 2025-11-11 03:46:00 | NPP-375D | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5b4d0a5e-c365-3b48-b44d-2160d67be977 | -4.7668 | -42.6572 | 2025-11-11 03:50:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 51656a6b-8178-3903-9ccf-20d844e8f277 | -5.4241 | -44.6524 | 2025-11-11 03:50:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| be747b37-7ecf-3cff-8233-98ee7d92c8d6 | -4.748 | -42.6584 | 2025-11-11 03:50:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 9dbde53c-239d-3b08-b1f2-f0ead42dd6be | -18.3827 | -54.9942 | 2025-11-11 03:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 60fc9d25-abd9-32ec-9e42-e5efb28e5bc5 | -4.7204 | -46.4497 | 2025-11-11 03:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 99dac102-537f-3ded-80f1-cfbaba9aba79 | 2.96137 | -51.42976 | 2025-11-11 03:57:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1ee4daa-5b32-3070-babd-d59d3415d87e | 2.96845 | -51.42871 | 2025-11-11 03:57:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2e33c8a-60da-3492-83dd-da01f0583882 | -6.09753 | -41.62983 | 2025-11-11 03:59:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a6c6ca07-2c00-3681-a70e-564a01cd514e | -5.12182 | -45.47564 | 2025-11-11 03:59:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1485109-d8b9-3e43-ac8f-e34c664b3fae | -5.39017 | -46.00989 | 2025-11-11 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaf1feba-1a98-3b30-b259-fbb65119da30 | -4.90376 | -44.33274 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c0f41fd0-fcd6-3ba0-a505-191cbe32e6e2 | -7.13477 | -41.26167 | 2025-11-11 03:59:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 65d4ab98-2e76-3706-8ed5-466e2c5ec194 | -5.40281 | -45.24182 | 2025-11-11 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f74d8ba-d394-3eb0-ac76-0e227daefb96 | -7.1359 | -41.25454 | 2025-11-11 03:59:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7e529c9f-67a9-3586-ab9c-10a124aca2e2 | -6.02944 | -46.15522 | 2025-11-11 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 692e878d-9305-3428-b226-cc4cf9ce96f6 | -2.44009 | -46.30802 | 2025-11-11 03:59:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9f14367-532e-3aab-9eee-0878f14a8ea7 | -4.88838 | -40.44876 | 2025-11-11 03:59:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea8306e1-f213-31e3-9446-edb3f5d9c9c3 | -4.72351 | -46.46228 | 2025-11-11 03:59:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f32911b-f789-3916-a5ab-858d407fc45c | -5.12843 | -44.72543 | 2025-11-11 03:59:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db53adaa-f78f-3875-aa7b-ecab8365edcb | -5.10509 | -40.73187 | 2025-11-11 03:59:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 85517485-3328-3cfd-9b1a-8d96ffb7f0ab | -3.85372 | -41.57824 | 2025-11-11 03:59:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 51e3fbe2-937c-309b-9d07-ee81fa5010f1 | -6.09168 | -41.55737 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 26f2308c-565b-300b-a1d5-c525764fd13a | -4.68066 | -43.24365 | 2025-11-11 03:59:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb8201b9-1c48-38c4-bf5c-a8a2574880cf | -4.25389 | -48.58201 | 2025-11-11 03:59:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07dab9ab-9f31-3ee6-b989-68f7044f4f6f | -4.90409 | -44.32465 | 2025-11-11 03:59:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b52c988-1ea7-3b5f-938a-5cf8c9446631 | -4.59787 | -45.49093 | 2025-11-11 03:59:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa6766e4-0691-3436-8f42-7ebb69a9e6fe | -4.9328 | -45.46696 | 2025-11-11 03:59:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86b227e8-f75d-3743-817d-249b44e0b9a4 | -5.40023 | -45.24122 | 2025-11-11 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de281e34-5590-3929-88a1-1b24b93ca87a | -5.33112 | -35.55313 | 2025-11-11 03:59:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a40c28a7-88ac-32b4-8f05-7617a8af45d8 | -7.13313 | -41.25044 | 2025-11-11 03:59:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2387fe2d-cc8f-32a8-bd10-3fafd328aac8 | -3.7328 | -47.65062 | 2025-11-11 03:59:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d16ea1ae-a37b-30a8-a3d1-45d294a53a7c | -6.26127 | -43.68311 | 2025-11-11 03:59:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9ed6366c-1568-3d6b-a90a-8468d4d82ffa | -3.76968 | -44.01655 | 2025-11-11 03:59:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1532a1e-594b-3409-86f5-897aac453e37 | -4.45841 | -38.39067 | 2025-11-11 03:59:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 651489ce-37a8-3a24-ae97-28f7f074c8ca | -7.07258 | -41.58648 | 2025-11-11 03:59:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README11.md)
