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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43948129-17e6-364f-be9d-a499a229cccd | -12.78127 | -44.43893 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20085113-0161-3ba4-b1c9-1864e9361d6d | -12.84086 | -44.35798 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| a69cc67b-82b0-3d5a-86cb-bfa31bc4caf4 | -9.18128 | -58.058 | 2026-06-24 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08f1ceee-ec6b-33f8-8158-26b604943766 | -11.64166 | -52.86148 | 2026-06-24 05:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14336620-183d-37cf-9f98-ab6994e7b5a3 | -12.84958 | -44.37244 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 4147e848-a350-3698-add0-babf9f4ec243 | -11.55021 | -48.26348 | 2026-06-24 05:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c3c4154-f2cd-3ebd-ac72-2c319eb1b941 | -16.84562 | -45.42973 | 2026-06-24 05:10:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f97bb490-1f2e-3646-94bd-4fd13fc2ef8e | -9.38106 | -58.20445 | 2026-06-24 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d129049c-85c1-3bd3-95c1-e9b4d84a49c8 | -12.51431 | -48.276 | 2026-06-24 05:10:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44e486f5-17a7-3c48-b42b-5d48122d6308 | -13.18373 | -43.40401 | 2026-06-24 05:10:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ee2e663-fd51-3b31-9629-4cb2bae1201d | -11.3043 | -54.72013 | 2026-06-24 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eced0e48-5827-399e-adf2-d2cc72d1c1ff | -10.38391 | -56.72509 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2766743e-ee41-3833-a1d3-4d3ba6a58d05 | -12.78017 | -44.44862 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 415f6eca-900f-30ed-ba38-8215ca254fac | -13.07073 | -53.35806 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7915e8ab-83cf-3a8b-a131-12ad43545068 | -10.90305 | -54.13417 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7603a2cb-8f52-3dcd-bcf3-7b9b446c7de8 | -11.29177 | -43.31997 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6eb5f1f5-12e3-3b6b-8327-f78a8e55986a | -10.27878 | -60.54431 | 2026-06-24 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8f8d78c-b405-3cf1-8467-6a5aa748d94c | -9.17769 | -58.0574 | 2026-06-24 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eab3793a-670c-3382-8373-5daeb0c40115 | -11.51221 | -56.12294 | 2026-06-24 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ae13748-6b22-3982-8533-fa20f7572a7c | -11.54881 | -48.26738 | 2026-06-24 05:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 752bc3fb-259c-37ef-ba17-44dacdf6a555 | -10.16368 | -56.61812 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aec17add-aa2a-374a-a783-01fcbdb5fe89 | -10.53945 | -53.73335 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 720cc6bf-fb86-3e01-8a63-a34aadebfc54 | -10.54266 | -53.73315 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bee189a-caf2-31bf-a313-80294b4dd93f | -11.2927 | -43.31963 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 111cd58e-cc88-3756-b99e-d86373055377 | -11.2416 | -43.36158 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d8be75e7-ac50-3380-886d-6683c656597f | -9.18643 | -58.0716 | 2026-06-24 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ca9ef39-7291-377a-9108-8daeb2da91a3 | -12.51087 | -48.26476 | 2026-06-24 05:10:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2aada1fe-d5db-325b-9871-762e24711ad2 | -10.81903 | -58.01942 | 2026-06-24 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb34e5e8-071d-35fb-b95b-07ecff5f3840 | -11.23512 | -43.36072 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 17635b6c-528d-309f-9b4f-3a65b9c7d1fc | -12.77477 | -44.4468 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 14d066e1-87bd-3121-8967-ad2ef5c8a816 | -11.27547 | -55.78711 | 2026-06-24 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9b8201f-4ef0-37f7-8426-eab3ab54fcb0 | -10.80431 | -48.56698 | 2026-06-24 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 339d58c2-bfa4-35ca-b980-57119f22213e | -10.90362 | -54.13054 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 252d2996-4ab9-3ae5-8a20-e345c80cebde | -12.83297 | -44.37163 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| bfacd9fe-df43-3859-9e85-1f0e502aadf8 | -13.06015 | -53.3564 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 28252783-71e7-31d7-a06f-b8634d10e5d2 | -10.79 | -56.7432 | 2026-06-24 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09443245-d438-3e97-a7f0-ddf599fb7894 | -11.29212 | -43.32446 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e06742b2-426f-350a-af93-84c78acb51ae | -10.53869 | -53.7363 | 2026-06-24 05:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c7d3755-5a65-32ce-8efb-a9cdc79cc934 | -13.11689 | -53.53191 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73a269a3-1f67-3978-a218-9a6982de8089 | -11.78774 | -57.35303 | 2026-06-24 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ec79ec3-8cd1-32fb-b644-ceb5f79014b0 | -12.85271 | -44.36438 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| dc5600c9-2ec4-30c2-9814-35f74ff8f268 | -12.84594 | -44.36847 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| a1e4be6e-9fa6-3eef-a2b1-4d61f531a372 | -12.77593 | -44.43717 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2b3df45-dafc-3674-96b8-bdab4a83bbf0 | -9.18352 | -58.06684 | 2026-06-24 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19620f0c-e860-3a1b-9485-0cce21209eee | -13.1163 | -53.53586 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3c11e6e-ccdd-3fe9-bd70-e2371ab54277 | -11.19221 | -48.58636 | 2026-06-24 05:10:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b261fd3-5c56-324c-a31d-82cd32acbaf6 | -14.62294 | -48.33817 | 2026-06-24 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f0503d7-0e9c-30e3-ae0d-7da22eb2fdc8 | -14.52589 | -49.10928 | 2026-06-24 05:10:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0756e01-ac30-3468-ac1d-cd633f89447d | -11.30954 | -51.41136 | 2026-06-24 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6d94b09-48f0-3bfd-a7d8-20611905eb2f | -12.85011 | -44.36761 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| dce84b3f-5ca6-3416-aaae-ed67f1cb8d7a | -11.30821 | -54.71709 | 2026-06-24 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b71ba9e5-bf9c-3239-9eca-794a352ecf71 | -13.0678 | -53.35351 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6fe121ae-d3d6-3ded-82f8-35b812db16a0 | -13.17991 | -43.40408 | 2026-06-24 05:10:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7686bc54-c965-3e35-b118-c9073308c7e7 | -11.27824 | -55.79118 | 2026-06-24 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf9026aa-34c8-3375-b303-9d570d087aea | -10.16132 | -56.63266 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36fe9b71-c236-30cd-aa8e-3273fb24e0ec | -11.50887 | -56.12239 | 2026-06-24 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6ada526-f6fa-3ef3-81bb-974487488087 | -13.06367 | -53.35696 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 369a07c4-79ab-3622-8d22-62822bff8168 | -12.83466 | -44.35713 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 6204d1e0-ee32-3a1e-ac5c-19b84ce51139 | -13.54313 | -52.96204 | 2026-06-24 05:10:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1cbae5a-5470-3f67-8f03-4f0a9f72949a | -13.54015 | -52.95723 | 2026-06-24 05:10:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75836155-fe4b-36b1-8955-b110c53c8baf | -10.1282 | -52.11491 | 2026-06-24 05:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5ea9921-4a37-3153-894d-02cb3925e760 | -11.88817 | -55.1371 | 2026-06-24 05:10:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 202a931d-278c-328b-800a-d0d50deefc60 | -11.6381 | -52.86095 | 2026-06-24 05:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7bfe3e7-28c1-3e11-be70-0762e336915a | -11.54449 | -52.77998 | 2026-06-24 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fb4bc7e-7c96-3774-9bdb-0693110afe44 | -12.84537 | -44.37327 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| c3b9311b-ed04-3336-86c2-8164749d22c1 | -10.39126 | -56.72261 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 794b54f0-5618-379c-a23e-5c1d9ecfba6c | -10.77917 | -54.10015 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a60192d-fb00-33aa-9612-573f5961da3f | -11.29776 | -43.32518 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 41ad7352-fafd-3c93-b158-8eebd099b5b3 | -13.06427 | -53.35296 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 273d058c-cb11-36c0-8785-ea90109460a4 | -10.38729 | -56.72567 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 615bac86-19b9-3f7c-8a55-aa82dfcd73d8 | -17.28631 | -47.04063 | 2026-06-24 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f76dde0d-cdc1-301d-b229-427038f3229c | -10.57739 | -57.31939 | 2026-06-24 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20990e62-9ae2-3443-9f48-59109f2bf026 | -13.06487 | -53.34895 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fcaba60-1cb9-3fff-b4ac-4adb7552dc09 | -9.1806 | -58.06211 | 2026-06-24 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15e039d4-bed9-37a5-92af-e0f38d8fe1f5 | -11.96685 | -49.23461 | 2026-06-24 05:10:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31e1054c-7f47-38fb-8eec-934356dbff7b | -15.36421 | -47.36331 | 2026-06-24 05:10:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 844d050a-2866-38ae-bb9c-fb1de6f0a286 | -10.7786 | -54.1038 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06b28c89-afe0-3fc5-b9a3-8c434635ccfc | -12.77535 | -44.44199 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65d85878-3bc1-332a-a515-5242cb835275 | -12.54671 | -54.60229 | 2026-06-24 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8eeeffa-6d18-3b11-a735-8cdd98649155 | -13.06308 | -53.36095 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 23faa4f8-2a6a-378b-a436-832bc650b29c | -11.64032 | -52.86411 | 2026-06-24 05:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9259339-cd53-390f-862d-69771f322b6a | -17.28588 | -47.04444 | 2026-06-24 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 769bffa3-0811-3b3e-9e78-2843dda4cbdb | -13.84697 | -47.04105 | 2026-06-24 05:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a42e0e73-f1db-3a58-89d5-400d24c1b488 | -12.85328 | -44.35953 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| f1e00863-4b65-312c-92e0-6d7a2d95d838 | -12.51498 | -48.27073 | 2026-06-24 05:10:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0e8490b-5e6b-3c9c-8b2b-06cab8ac5c30 | -10.16309 | -56.62175 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47db9336-d945-3f7a-9253-3058d61dc41a | -10.39214 | -56.72245 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68fabecb-e224-33be-a23b-933e4cbf24cd | -11.29121 | -43.32481 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5a7d3f3c-30db-36fe-a3dd-5b69ff73d7fd | -11.48291 | -46.74353 | 2026-06-24 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9d7eab7-9b1c-3113-ab04-9a8d838351d5 | -11.54484 | -48.2678 | 2026-06-24 05:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48e2a774-12fa-3462-8167-8012304bd82b | -11.30721 | -51.41401 | 2026-06-24 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2106a68-5d2d-3c1d-ad9e-ffc1490fa7b6 | -10.38906 | -56.71469 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c0cbaf2-2868-333e-9846-7727c00ab4ea | -13.0672 | -53.35751 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 617d38af-5a63-3a36-895a-f36f31a79640 | -10.38848 | -56.71835 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c905eaab-8b0f-3f82-ae54-45bf9bafcd12 | -11.281 | -55.79524 | 2026-06-24 05:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77927cfd-9a99-3d79-950a-2df1fb0e97ec | -12.84142 | -44.35312 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d744bf02-f484-30b1-bbd8-b27999072cbd | -16.84499 | -45.42874 | 2026-06-24 05:10:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ab43dc0-d5b9-3379-af47-6e8dd36fdf65 | -12.78691 | -44.44444 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 797bf370-358e-3a38-99da-11e4b90330d9 | -14.52401 | -49.11057 | 2026-06-24 05:10:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe513c74-ee6f-3102-a1da-64f24588c1fd | -12.66077 | -47.67819 | 2026-06-24 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README18.md)
