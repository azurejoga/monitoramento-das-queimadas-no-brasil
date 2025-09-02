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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 983acc95-ca33-30c5-b5b4-9c70ab26b0b6 | -6.85775 | -52.80808 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 768ea286-8d9b-397b-9f00-249c7e1c0b71 | -9.83301 | -48.31524 | 2025-09-02 04:14:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54d57e89-4d3d-30eb-87eb-830999fea669 | -12.92486 | -48.10438 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7e8bf81-6c87-3dec-b443-10941c52dc30 | -13.71696 | -46.93412 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f65cb31-c037-3029-a3c7-6b70053aae4f | -7.62003 | -42.65108 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b46f4665-c923-34a7-a827-96b344fb4ce9 | -11.37755 | -43.56696 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5500ccaa-5cac-32fa-b80f-dc5eca668b81 | -11.66833 | -52.1975 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 2284c49a-38cb-3e16-88a7-e420ee8a0ac9 | -6.92491 | -44.72176 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0210e4eb-858f-322e-b263-3085c5546504 | -7.9156 | -46.44717 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8652ca5d-fb48-3265-a897-d8b6a54a4e0d | -6.93937 | -44.35386 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cb520e7-d5ee-3ad1-802d-292d36d0cfbd | -12.38387 | -46.46606 | 2025-09-02 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 479af35f-77d1-3141-8e3d-064202b3d5da | -9.49975 | -48.87487 | 2025-09-02 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0370348a-651c-3af2-91b2-386250913e6c | -10.65309 | -47.07679 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e06b946-3bf8-3ad9-9d69-6be24e2f922f | -12.7589 | -44.6961 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3cd2c1c-adda-39ab-8cc3-ad4a28025b6d | -10.04602 | -48.11027 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ad58ddf-ff02-366f-acb9-4890c12566f8 | -13.40739 | -47.06733 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf896079-6375-3d7c-b4c6-f87b618c30ce | -11.66522 | -52.21387 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 160b46b0-5612-3c4d-9535-2aadf9bae99b | -6.80934 | -52.82356 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a02dd36-ef7f-3238-a401-bf2c77b753ab | -10.97137 | -50.77822 | 2025-09-02 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d13465c-b34f-3b61-ba59-e4707138e0c8 | -7.63457 | -46.55344 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 193b61e3-9642-3782-aba1-e3f4f253686b | -11.09214 | -44.62612 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4e3d341-8760-3bbb-9e13-0e4086f98947 | -6.87875 | -45.8556 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f1de614a-5751-3386-b447-16129c83a352 | -6.79608 | -52.8028 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c1fe9a0-7cbc-35fe-82b7-a819fe29d6ad | -11.8402 | -51.54026 | 2025-09-02 04:14:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2728110-bf72-3147-a329-f7e38326564f | -10.45483 | -49.05573 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4e218045-0921-3df7-b2ad-89142f5e1770 | -11.43079 | -55.18771 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d6f32d2-43c4-3f30-a677-2134acb19f30 | -10.25885 | -47.52304 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14834985-c1fb-363a-a331-9061e50986cf | -10.44549 | -54.77689 | 2025-09-02 04:14:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 013c56a5-746c-39e3-8cba-113e77c75049 | -12.98206 | -48.0989 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2313c774-82ee-3e9f-9e94-0c98d60bd2ad | -14.04814 | -44.55134 | 2025-09-02 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f0e6520-989c-3699-b605-613b39a56fa9 | -9.50156 | -48.86437 | 2025-09-02 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8bbb6c2-5864-36a5-a2ea-ddb5f113f6b4 | -6.98141 | -43.10661 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0be7449-8276-3a29-884b-545f7ce877fa | -7.09511 | -44.55413 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f023a3fa-618e-32d1-8910-e588450ac8f7 | -11.06148 | -45.38984 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9130b0d3-98f9-3e26-b316-2b4e2421a722 | -8.83116 | -45.79529 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa0b74d5-aa02-32c8-8c69-0d90c7853946 | -12.64178 | -48.24403 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa58e899-fccc-3177-947d-7182db5411dc | -6.98292 | -44.33891 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9651be7a-2723-35cc-bd6f-48a41a904e06 | -10.57952 | -44.85721 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dd8980a-d0fd-355a-bf64-61e385855049 | -6.85362 | -52.79971 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5784122f-ac81-3bf4-a9b2-cf17f8aab8be | -10.83008 | -47.44942 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f90472a-feaa-3a13-8860-7565bb8244e9 | -11.09545 | -44.62666 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| d134939c-7e5f-3923-89b6-bae0709c9b41 | -11.67568 | -52.19191 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| dfc847cf-e3ad-3252-8e6c-3e98c50d12a9 | -6.85036 | -52.81785 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b4594df-8175-3e9c-8ac6-6df57a9141ec | -6.87109 | -45.85834 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ef3d482-fd05-3d82-93dc-f287d8b47e64 | -11.84801 | -51.47218 | 2025-09-02 04:14:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63995a51-f97b-3133-a792-2d2fdb39f976 | -13.59087 | -48.13631 | 2025-09-02 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1bc6d32-bd23-3fd1-8f49-b20e8dc1a053 | -14.04257 | -44.60868 | 2025-09-02 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8b38d52-acaf-35c9-b38a-e05f3b623845 | -11.82728 | -44.70319 | 2025-09-02 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0a1afe8-46f8-3720-98c2-453a5ba0d2cc | -7.98137 | -46.47103 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8aaba532-882f-34ed-8bdf-7490c6564976 | -12.98284 | -48.09438 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bbbeebaa-efae-31df-84c8-c0832190ecb9 | -12.80743 | -48.06723 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| efb00ad5-f274-37ef-a832-d92344442496 | -12.06685 | -45.8114 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ec90ddb8-c33a-3e8a-955c-4e39dd1b6e12 | -10.28743 | -47.51006 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ecdb2da-fa71-38b9-8153-b28acbbc0536 | -6.76384 | -45.71606 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33a95eb8-1795-35b5-ada6-ec5607f6ea82 | -12.76165 | -44.70017 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1834b367-01f2-3545-9517-5e13f34c8645 | -11.35867 | -43.5349 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ee116ce-fa3c-36d1-a403-3dc25c12072e | -10.83442 | -47.44579 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7fbedea-1828-3a17-b4d5-46383b4e256b | -11.89381 | -46.75243 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6799cc9-0c3f-3a5a-9c94-990ed7f81fdf | -11.6601 | -52.22265 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f300b7f8-4893-3448-b478-8a5047624684 | -9.75162 | -46.9218 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83a4b98c-01ad-335f-a375-c24705bde3ce | -13.65446 | -46.9327 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| effbec92-a536-3970-9c67-c6c2855b5b79 | -10.76519 | -49.57518 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97d3d9e4-058b-3abb-aa90-e0aa2e1b4e67 | -11.09702 | -44.68102 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a7702c0-9da7-3c1a-97e2-68009b3462f3 | -11.37145 | -43.56236 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e668660-6bd5-3b14-ab1b-6d81cea0e6dc | -7.70056 | -50.26864 | 2025-09-02 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a0410565-dcfd-31f0-b5e6-edac1f991f4c | -8.12919 | -45.03702 | 2025-09-02 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ca7cf3c-6151-3170-ad51-38f9c7e39f8a | -8.1644 | -42.3115 | 2025-09-02 04:14:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 61776797-7377-3ba0-a215-43ef58ab33e0 | -10.06104 | -48.13683 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2ecba4e-53fa-3f85-9290-a473f2b9c63d | -9.70609 | -48.30618 | 2025-09-02 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cf4c88d-668f-3287-8d30-d689d4afe52d | -11.10483 | -44.63179 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 84af2a83-76e2-33e6-8fb1-d1b83a7ca4cd | -7.63166 | -46.54867 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e601517b-7d45-3726-ac92-671a8892c23d | -11.09378 | -44.63721 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 67ac3e49-ae97-3190-9a86-ea10fd02c17f | -6.98739 | -44.33242 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf6b4897-eaa1-3f1e-99e5-59b8b9cc3a24 | -6.84487 | -52.81708 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5b78a75-36c5-3c98-98c5-2026b3d89f22 | -10.04441 | -48.11965 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ec34ec0-1fdf-3efe-b4db-6fa01d801585 | -6.63321 | -43.955 | 2025-09-02 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29f8742d-e12a-34e2-96da-f0c7942a386f | -11.7909 | -46.403 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9eb3adea-d565-3097-b899-878175c26e19 | -12.61345 | -48.18825 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 798f974b-e0a0-33ee-b4b1-5a66dc7480ad | -12.87052 | -48.04866 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7a1d3602-e713-3e86-b129-4c51baa53af2 | -7.88183 | -45.18075 | 2025-09-02 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b4da4a0-1908-3f3e-9156-5cabdb126bfc | -12.99223 | -48.1053 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 702b3efa-8e7a-3ab9-bcb3-530fdc309861 | -11.67458 | -52.22539 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dcdf6097-9023-36a0-8c17-fb769a59a0c3 | -13.5451 | -46.97847 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbb7e240-064b-39b8-a8ab-ef87f67aa80d | -12.61808 | -48.19108 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| f87ba085-c974-3f0a-8952-10a789671dc0 | -7.98672 | -44.05308 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efe234c2-8668-370a-a725-3d0318caf684 | -7.55642 | -45.69832 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0495cc06-f7ad-3471-a108-c8721450f205 | -10.83987 | -47.28136 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bb06262-55d5-3377-a883-4c5c7026add2 | -7.11969 | -44.57276 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 899f22e9-f2a1-3c86-b09f-10f797306cb1 | -7.98205 | -46.46687 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9bdb1333-2028-3819-93a5-2df3982021e0 | -11.66423 | -52.17281 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ef492852-52d5-33ed-9dba-21fa7eacd765 | -9.72795 | -48.9558 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c1cbb95-fede-3ab5-b96e-07ef319c7b63 | -6.88641 | -45.85282 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7de20987-bd91-3e7a-b957-126e1dc16bf9 | -13.70354 | -46.8877 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea3fb4a9-846e-385c-a5f4-8d9916845b34 | -11.47234 | -50.48134 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 953e2e65-1f80-3961-a119-9ad9aeef1e66 | -11.66903 | -52.17377 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a3005046-321f-3cc7-b5c7-71fa7eb90b86 | -11.37587 | -43.5558 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cde8fb69-54c4-3ba8-8d77-41fe8213a736 | -6.95079 | -45.5644 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54daf4c6-c9df-3399-863b-7e8c88f1bcdc | -10.47299 | -51.62431 | 2025-09-02 04:14:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 99936ab5-88e9-31cc-bf3f-66f36014892b | -7.11303 | -44.54971 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad4f3728-2d1c-3548-95d0-ba854d3cb4bc | -12.96749 | -48.0962 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README43.md)
