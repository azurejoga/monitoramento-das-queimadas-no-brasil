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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 891bc030-7f7d-3650-872e-df8141f95382 | -14.7961 | -48.032001 | 2024-10-04 00:42:17 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| abbba470-e1ca-3fba-8639-e2a024da3120 | -14.7978 | -48.039902 | 2024-10-04 00:42:17 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cb75622a-2dfb-3d04-8f47-0befd63acb2a | -14.7995 | -48.047699 | 2024-10-04 00:42:17 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25e1f2e5-7039-3741-bb31-7c6658115f68 | -14.783 | -48.0186 | 2024-10-04 00:42:17 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5b458307-2c43-3090-938f-a59e328b65af | -14.7847 | -48.026402 | 2024-10-04 00:42:17 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ab989dd2-691f-39ea-bd3c-75eb3e4d402f | -14.7863 | -48.034199 | 2024-10-04 00:42:17 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5d89f038-1e0c-3898-b366-82f99eb26b89 | -14.788 | -48.042099 | 2024-10-04 00:42:17 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 065ead8b-a259-39fd-890c-0a10ef6a1ff6 | -14.7897 | -48.0499 | 2024-10-04 00:42:17 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ba9f12c9-77b8-3a23-a455-322921c56608 | -14.7981 | -48.089199 | 2024-10-04 00:42:17 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d61077b-99d0-31c3-99b5-f2d28b98f7f2 | -14.7998 | -48.097 | 2024-10-04 00:42:17 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 39b4f671-ad5c-30fb-b59c-3416fe405ac3 | -13.8942 | -44.274601 | 2024-10-04 00:42:18 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8566b35-6eba-354f-93e1-6b972943c359 | -14.7799 | -48.052101 | 2024-10-04 00:42:18 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d2fef9de-8841-306c-9df1-800ac5a03755 | -14.7816 | -48.059898 | 2024-10-04 00:42:18 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac9e463a-6f3c-38a8-9c91-1b570563ba7b | -13.6627 | -43.726002 | 2024-10-04 00:42:20 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 768ae38c-c863-3fd3-9ae7-ffa63936bb16 | -13.3036 | -42.305401 | 2024-10-04 00:42:20 | METOP-C | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cdbcfd57-8a38-3278-bd12-08800a599b14 | -13.2916 | -42.298801 | 2024-10-04 00:42:20 | METOP-C | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1e2d5b58-6bd2-3665-a37e-199a9b7c718e | -13.2938 | -42.3078 | 2024-10-04 00:42:20 | METOP-C | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5f2ef5f0-ab6c-37c8-b576-38032d9b0724 | -13.2959 | -42.3167 | 2024-10-04 00:42:20 | METOP-C | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 022ab94a-8895-3c9d-ab75-777f6b573ac4 | -14.8064 | -48.8022 | 2024-10-04 00:42:20 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0a7c922c-0968-3945-8b41-db0ee787cec3 | -14.7966 | -48.804298 | 2024-10-04 00:42:20 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d4e592a8-603c-3068-ad09-6600ca96ebfd | -14.7868 | -48.806499 | 2024-10-04 00:42:20 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd80d445-fa9c-3f90-a056-5fa3ad5183fb | -12.7148 | -40.207401 | 2024-10-04 00:42:21 | METOP-C | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1677904d-6b24-331f-814e-5265389c7882 | -14.196 | -46.462101 | 2024-10-04 00:42:21 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e2afdebf-8566-3910-923d-e67f8c616110 | -14.1976 | -46.4692 | 2024-10-04 00:42:21 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 81242a22-6373-35ef-b877-b497476b4a66 | -14.1878 | -46.4715 | 2024-10-04 00:42:22 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 549b9413-0295-380a-8cb1-7601746b137f | -14.1894 | -46.4786 | 2024-10-04 00:42:22 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9987d57a-6dc6-3dcb-ae4c-cfdc0c336c44 | -13.4097 | -43.441299 | 2024-10-04 00:42:23 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c56d7180-5d03-392d-bb6a-1b70f5e0a43e | -13.4752 | -43.7635 | 2024-10-04 00:42:23 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| afe905d0-203d-342b-ac29-08285db11785 | -13.4771 | -43.771198 | 2024-10-04 00:42:23 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c33f08c4-c00b-31af-96dd-1cf3fb20ccd9 | -13.4789 | -43.778801 | 2024-10-04 00:42:23 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f2bb10a-5d1f-3866-97a4-de04baf050ca | -14.5178 | -49.278999 | 2024-10-04 00:42:26 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2cc672a2-4120-373d-9895-f3e9a2fbd19b | -14.5196 | -49.2878 | 2024-10-04 00:42:26 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 59525755-3fd6-36b5-8f92-246247680c50 | -14.5081 | -49.281101 | 2024-10-04 00:42:26 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 47a2cd7e-8ffd-323b-b919-344532948890 | -13.0179 | -43.7519 | 2024-10-04 00:42:30 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d08f7bf-7cd4-3f2a-bdd0-d5f757b34e6e | -12.1414 | -40.895302 | 2024-10-04 00:42:33 | METOP-C | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6c7d7150-0758-3a4d-becf-7907ad8d6e91 | -12.1359 | -40.873001 | 2024-10-04 00:42:33 | METOP-C | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0344d6ad-650e-301c-8811-7421cbe20a37 | -12.1387 | -40.884201 | 2024-10-04 00:42:33 | METOP-C | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f7054a5a-8338-37f5-aef4-5d1ee52383a8 | -12.6809 | -43.114399 | 2024-10-04 00:42:33 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2ad331e9-05ee-31d2-9d20-6137b91d44cb | -12.129 | -40.8866 | 2024-10-04 00:42:34 | METOP-C | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 455dd9f2-fba3-348b-b7f9-615cd4753a18 | -13.169 | -45.4263 | 2024-10-04 00:42:34 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 646ed92a-c85b-3861-b7d5-d8bf166a6e40 | -13.1706 | -45.433399 | 2024-10-04 00:42:34 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d5e5fa3-7bb0-30be-8e94-2ad2b29db637 | -13.1543 | -46.316601 | 2024-10-04 00:42:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 69da58f0-380f-3f74-b317-70c23a98288b | -13.1559 | -46.323601 | 2024-10-04 00:42:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5262399d-a4a3-387b-b4b8-0f1aa6b33a6b | -13.1398 | -46.297798 | 2024-10-04 00:42:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f135b8a1-5351-3f47-b847-70950efa6dbe | -13.1414 | -46.304798 | 2024-10-04 00:42:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3078822f-bdca-3b90-a0c2-ac05af217277 | -13.1284 | -46.292999 | 2024-10-04 00:42:38 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aafdf3f7-6621-3c26-95b0-5048d18204c4 | -13.13 | -46.300098 | 2024-10-04 00:42:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 92532458-bc95-37c8-bb8b-6bfdfdf57ede | -13.1316 | -46.307098 | 2024-10-04 00:42:38 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0d729b71-5063-3071-b727-8cc85789c2c3 | -13.1202 | -46.302299 | 2024-10-04 00:42:38 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b81edb6-1342-3538-ae0a-01ed928fec7c | -13.1218 | -46.309299 | 2024-10-04 00:42:38 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 766f2177-1bc7-3579-9fdd-064b8b8f3336 | -13.5141 | -48.605701 | 2024-10-04 00:42:40 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f65d9811-54e0-3720-9fd6-2c22256c317a | -13.5043 | -48.607899 | 2024-10-04 00:42:40 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d11cd109-ec24-388b-a5f2-450003f7592b | -13.506 | -48.615898 | 2024-10-04 00:42:40 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f4974e3-ed4a-35b7-9d69-914fc7724907 | -13.4979 | -48.625999 | 2024-10-04 00:42:40 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1f5372dd-93b8-3fb7-8fa8-27d0bb035353 | -13.4996 | -48.633999 | 2024-10-04 00:42:40 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 81b910f5-18d4-3368-83d2-e84edd105fc9 | -13.6967 | -49.8508 | 2024-10-04 00:42:41 | METOP-C | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3095e723-40d3-31a7-b7b9-96f61fcdc00e | -13.6986 | -49.860001 | 2024-10-04 00:42:41 | METOP-C | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 03522c08-3084-39bc-ade4-0e0dfd6827b4 | -13.4898 | -48.636101 | 2024-10-04 00:42:41 | METOP-C | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b29aa554-2283-393d-a8c9-e972b9d9f25c | -13.2074 | -48.515701 | 2024-10-04 00:42:45 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 781274cc-2c84-3a34-abc9-fc423ccdc55e | -13.2232 | -48.636501 | 2024-10-04 00:42:45 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 314829ce-fbbf-399f-9433-4575e430cbab | -13.2249 | -48.644402 | 2024-10-04 00:42:45 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7b4b9699-0d3d-3951-a4d3-d96454418b0b | -13.2134 | -48.638599 | 2024-10-04 00:42:45 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5cbded48-f33c-3b84-9b35-3475868b868d | -13.2151 | -48.646599 | 2024-10-04 00:42:45 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 35f88f9d-14ab-3678-acf2-67f90e37d2ca | -13.2053 | -48.648701 | 2024-10-04 00:42:45 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3febeeb5-8319-324d-b7da-8da209f50085 | -13.1789 | -48.6213 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93039812-7290-3026-9671-a951fcbd5e91 | -13.1806 | -48.6292 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4748fd64-b2ff-3f22-ad67-35a127303c4e | -13.1892 | -48.668999 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f94ee2b7-b3c6-3505-b36d-6a1229eea0bd | -13.1909 | -48.676998 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 080bacc7-0406-3005-90a7-dcffcbea6ec4 | -13.1692 | -48.623402 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f98b746b-ce25-313f-8c30-32e61890b66c | -13.1709 | -48.631302 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f6739d4f-e4c2-38b9-96b3-6296c1ab2a53 | -13.1726 | -48.639301 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6dafffff-12be-3f62-a425-6c29de56cdf9 | -13.1795 | -48.671101 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 519c887d-4123-3dd9-94d5-20e1e5f5ad45 | -13.1812 | -48.6791 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 28e2a4c6-275d-36a4-bf61-14a2f864e6dc | -13.1829 | -48.687 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 65ee97c4-6b57-30b5-bb11-47e1f26ca873 | -13.3188 | -49.321701 | 2024-10-04 00:42:46 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 64fc3278-190e-338e-a433-f09db72fd4c2 | -13.1577 | -48.617699 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 49a14f87-cc25-3967-a320-acc511cff48e | -13.1594 | -48.625599 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8e6062-df18-35c3-b3d9-a51efade89c8 | -13.1611 | -48.633499 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5b905aa5-3798-3337-b2b0-7e9530c03614 | -13.1628 | -48.641499 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 840866fb-1590-3dab-b103-00d2b1e342d1 | -13.1645 | -48.649399 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7b0ee8fb-9124-3da7-b748-fe729d8c0734 | -13.168 | -48.665298 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e2d9fad9-f97f-31dc-87d0-396d90ff6ae5 | -13.1697 | -48.673302 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d5aa4a47-395a-3820-b2c0-a3cbaf890b34 | -13.1714 | -48.681301 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 421271b9-c210-327a-9b75-2e6073088635 | -13.1731 | -48.689201 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 633b23c9-f722-35b3-a8d0-09feba66b99b | -13.3053 | -49.3069 | 2024-10-04 00:42:46 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e5c21d05-2c1d-3f1d-9a28-f44440c62904 | -13.3072 | -49.315399 | 2024-10-04 00:42:46 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aea138e5-5571-3d56-a432-2e93131b8c74 | -13.1582 | -48.6675 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4e60a023-581b-36e4-bb26-99249dcdf0c4 | -13.1599 | -48.6754 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83477769-1e47-3ea5-a826-cc378cff85e4 | -13.1484 | -48.669601 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 262e1085-f879-3c88-8a02-c19b83e8d17d | -13.1501 | -48.677601 | 2024-10-04 00:42:46 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 98c2b5d6-3379-3fdb-be32-14274f775615 | -13.6153 | -51.182098 | 2024-10-04 00:42:47 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 890eea3d-caa5-34c1-b980-50eefa30d895 | -13.6175 | -51.193001 | 2024-10-04 00:42:47 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 34280c49-d6f1-3c0d-94a0-51845ee98177 | -13.6198 | -51.203999 | 2024-10-04 00:42:47 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c721e55f-c248-31fe-8888-c57ed884cbf1 | -13.6077 | -51.195099 | 2024-10-04 00:42:47 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a77597f-744c-3d42-97e4-5d24a183c873 | -13.61 | -51.2061 | 2024-10-04 00:42:47 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0473fcff-7971-358b-9aed-bc62b9bb9ce2 | -13.6122 | -51.217098 | 2024-10-04 00:42:47 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7dfc0dd4-2133-3de1-98a2-9e0234a1065b | -12.7981 | -47.442001 | 2024-10-04 00:42:48 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d229bd4-6f50-307c-a85d-24e22e28f5db | -13.6002 | -51.208099 | 2024-10-04 00:42:48 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 977aab8b-521d-33f4-8df1-7a1691c59613 | -13.6025 | -51.219101 | 2024-10-04 00:42:48 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9008a6d7-f49e-35a1-b827-5da6097b713b | -12.7883 | -47.444199 | 2024-10-04 00:42:48 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
