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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bef97029-cc70-33c3-bdc4-19d1d2d2fae6 | -11.4637 | -50.7955 | 2025-09-14 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| e9f0425b-dc43-3443-b9a8-7db73dd808d9 | -11.483 | -50.772 | 2025-09-14 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 8dafd859-dd61-34d1-98f7-4ea17813d6ca | -14.4779 | -47.3368 | 2025-09-14 00:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 87677d1e-52bd-391b-b9a8-aeae6322e4bc | -12.4541 | -57.7872 | 2025-09-14 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 30fce5a3-f64c-3269-94cc-a3e37e92447e | -11.3491 | -50.8507 | 2025-09-14 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 45f3127e-a7d5-301f-b4ef-df2f7d36471c | -18.7282 | -51.7816 | 2025-09-14 00:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| afa6ecef-781c-353f-ac1a-876bf552a2fb | -12.9294 | -54.7333 | 2025-09-14 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 43d59dad-1b6a-387e-9595-c6d954b39a38 | -3.5995 | -47.5142 | 2025-09-14 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 233.0 |
| 668ef142-4f8a-39fd-8472-8b17ece3fe2d | -3.581 | -47.5149 | 2025-09-14 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| d2b14bba-568c-372d-819f-2227b8024f16 | -3.5908 | -58.5963 | 2025-09-14 00:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 71e2591c-e83a-3470-8f8f-e6b31606ea13 | -18.7082 | -51.7851 | 2025-09-14 00:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 5b3650d7-d2ff-36ba-b726-0d7cd481a9c2 | -12.6636 | -54.6782 | 2025-09-14 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 219.0 |
| d65524d2-a5c4-3f96-a28f-23ce96e21b80 | -11.445 | -50.7762 | 2025-09-14 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 80938f92-2c3a-3074-ac81-a7c080299031 | -11.3304 | -50.8314 | 2025-09-14 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| ca7e231e-95ca-30f5-a1f6-7793e02f2b09 | -8.9554 | -46.1525 | 2025-09-14 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 1818acd7-5717-3a8d-893d-668d38d2e305 | -11.4447 | -50.7976 | 2025-09-14 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| dd0fff83-c09c-31be-ad7e-eddd5846bf0a | -3.6181 | -47.5134 | 2025-09-14 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| fee1da5f-4f36-3acf-967d-3175c1d517d9 | -12.7867 | -47.9986 | 2025-09-14 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| c103438b-bf1d-39ba-b663-e82827948a38 | -12.6826 | -54.6763 | 2025-09-14 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 207.1 |
| 336d5e68-1c1d-3d1c-adb6-0eb4ff7464f0 | -12.6633 | -54.6988 | 2025-09-14 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 3a86e5c5-7b6e-3955-a25e-4c3b370ed01a | -11.7011 | -59.3061 | 2025-09-14 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 32acad27-7a62-38c8-89cb-ccf81b75628a | -11.4827 | -50.7934 | 2025-09-14 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 6bafc5b4-f4d9-3ce4-88be-190b41dd09cd | -12.6824 | -54.6968 | 2025-09-14 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 98b40057-d134-3ea8-a665-dcdedad57059 | -17.3119 | -46.0954 | 2025-09-14 00:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b50ef6a8-7b9d-32ee-9f05-68b134e5157a | -11.464 | -50.7741 | 2025-09-14 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 88a500b9-f578-307c-943f-6e68a30d115f | -12.6824 | -54.6968 | 2025-09-14 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 2d2e6b9c-a8a7-36bb-aa26-c25590d14225 | -3.5995 | -47.5142 | 2025-09-14 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 191.6 |
| 55ad6ed2-2ea3-3865-83e4-43ce45d2483e | -12.7867 | -47.9986 | 2025-09-14 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 13bf7ed3-37cb-38dd-a9ff-deca66078b0a | -12.6636 | -54.6782 | 2025-09-14 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 164.5 |
| db455ed4-6c8d-3742-9a2a-76ed0f2c2e17 | -11.4447 | -50.7976 | 2025-09-14 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| ada38c3a-1a01-380f-a0c1-a1b13772d975 | -11.7011 | -59.3061 | 2025-09-14 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 50cdebe1-c10d-3ef8-8874-2b3cefc805c8 | -12.4541 | -57.7872 | 2025-09-14 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 276f725b-ba22-3e25-8a5b-85776e282e39 | -3.5994 | -47.5359 | 2025-09-14 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 4a8b92cf-0472-3eb8-83a3-8626b60987c7 | -10.7579 | -44.7721 | 2025-09-14 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 4ef14bb1-1fbc-3359-b07c-e2837be2bc3e | -3.5996 | -47.4923 | 2025-09-14 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| bb640c81-684e-3fc5-a047-7a12e076fec2 | -11.464 | -50.7741 | 2025-09-14 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 4ce7b233-9865-3226-b39c-dd8ae3420b5e | -18.7082 | -51.7851 | 2025-09-14 01:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 770d9492-9f03-3734-b743-22f75ed5f4f6 | -11.3301 | -50.8528 | 2025-09-14 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 61df35d9-24f1-39f8-9189-9586f52e187b | -17.3119 | -46.0954 | 2025-09-14 01:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| d0be4a3b-4f39-3a41-8222-94f12c49d638 | -12.6633 | -54.6988 | 2025-09-14 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 56fd7bef-f5c6-3709-b2ce-25ad02e6cf2e | -12.7863 | -48.0209 | 2025-09-14 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| d3803421-a521-3696-8612-c551d71bea67 | -18.7282 | -51.7816 | 2025-09-14 01:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d9a12584-04ee-386f-b079-1a5bfad33e27 | -12.9294 | -54.7333 | 2025-09-14 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| f089573c-d324-30db-a45c-e545fa6779c5 | -10.9163 | -45.5775 | 2025-09-14 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 75dd68fe-6cc6-3438-83c7-83ac92433dc2 | -11.4637 | -50.7955 | 2025-09-14 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 1779a7ef-fe1a-38fc-8796-aa5224640f58 | -17.3125 | -46.0719 | 2025-09-14 01:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 497eddae-8ab1-3531-a1a9-5011ce4e26b7 | -11.3491 | -50.8507 | 2025-09-14 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 58df1c5c-c7a6-3dd0-9bba-5bea3bec1654 | -11.445 | -50.7762 | 2025-09-14 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| d4bfb85e-d866-34b0-a7d1-92f59636f868 | -15.8018 | -52.2043 | 2025-09-14 01:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 97a32656-f4b6-352f-a944-72755f4f3473 | -14.6394 | -52.1094 | 2025-09-14 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 4bcbe652-4e4b-38b7-abb1-a49b6fc3888b | -12.6826 | -54.6763 | 2025-09-14 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 351e0fb1-9dc1-34c8-9c08-716a918d1c45 | -3.581 | -47.5149 | 2025-09-14 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 8782f42e-6f4f-3cf0-a859-10ee7dc3845f | -12.6633 | -54.6988 | 2025-09-14 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 5fc0269e-e893-3c21-b29e-88295c152b2e | -18.7282 | -51.7816 | 2025-09-14 01:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 2f9617f4-4ee5-3b3b-a3e0-1bfea6789f31 | -12.9294 | -54.7333 | 2025-09-14 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| a84a4521-151d-3c42-803e-53a6c695727f | -3.5994 | -47.5359 | 2025-09-14 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| bea264d3-7b8d-35b7-a20f-2c126e0e1f78 | -17.3119 | -46.0954 | 2025-09-14 01:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0884b9e6-852a-3154-8965-20df61ab4bdb | -21.6026 | -50.9594 | 2025-09-14 01:10:00 | GOES-19 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| 3a62abe7-024c-304c-ab0b-ede6b9039bc1 | -10.7579 | -44.7721 | 2025-09-14 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 98c47de6-11ee-334f-baf1-7437509d8273 | -12.6826 | -54.6763 | 2025-09-14 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 1b0d2f29-aca9-3395-ac82-6610f9924c18 | -12.7867 | -47.9986 | 2025-09-14 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 7e6384ad-1a79-357b-861d-ad09973d3715 | -12.6824 | -54.6968 | 2025-09-14 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 85d014da-0a75-3932-a738-95c9d3369681 | -14.6394 | -52.1094 | 2025-09-14 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| cf7c4da7-4a8e-3042-b2ca-5b633bfecf5b | -13.9283 | -44.8341 | 2025-09-14 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 935a52e3-da37-36c0-a606-53c7e0e9f404 | -10.9163 | -45.5775 | 2025-09-14 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 168531a4-fb5e-322f-9755-d8639d0533db | -3.5995 | -47.5142 | 2025-09-14 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 235.2 |
| e2fb3dbb-145a-37ba-adfa-7f3aa576b8c3 | -17.3319 | -46.0912 | 2025-09-14 01:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 2e287dec-e071-3f80-870f-ed063d8abb1d | -12.6636 | -54.6782 | 2025-09-14 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 83646559-aa63-35a4-9799-ecd96e9b7dfb | -3.581 | -47.5149 | 2025-09-14 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 2d03b89e-e26c-3c93-882a-c891ccd95ff3 | -13.9478 | -44.8306 | 2025-09-14 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 81bc8e43-c690-383e-bd05-fee96b4ef85c | -10.7576 | -44.7953 | 2025-09-14 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 07dcc932-b0d8-3eb2-ba58-d2dc0496951d | -12.7863 | -48.0209 | 2025-09-14 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 7be80fe1-29b0-359b-8f37-7f55169049ae | -11.3491 | -50.8507 | 2025-09-14 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 58d12b12-1ace-3ac8-b821-26c02acb860a | -12.7867 | -47.9986 | 2025-09-14 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 3a47f93c-a845-3885-b7a7-fab0496ff816 | -12.7863 | -48.0209 | 2025-09-14 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| a2f4999f-51d8-3c30-a0ea-4c2404c1a8af | -17.3319 | -46.0912 | 2025-09-14 01:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 77.3 |
| bb3a1b26-917d-3dee-aa55-015b47da95b2 | -12.6636 | -54.6782 | 2025-09-14 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| d59857cc-a6f9-34b7-84d3-94688a12e331 | -13.9283 | -44.8341 | 2025-09-14 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 0b8782be-3146-374b-b508-8fdb011fd5f0 | -13.9278 | -44.8576 | 2025-09-14 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 104a091c-9d82-3131-81f5-9ea9705a8264 | -3.5996 | -47.4923 | 2025-09-14 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 070978dd-f82a-31e0-be5f-798b91822fce | -17.3119 | -46.0954 | 2025-09-14 01:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| b9b89b8b-ff1a-3c3c-b83c-9bee5e5718f6 | -18.0059 | -46.9732 | 2025-09-14 01:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 57c012eb-f4ec-39a7-b435-79aeb999368c | -18.0065 | -46.9499 | 2025-09-14 01:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 95c0844a-84e0-3733-a747-7e24bc2bf9ee | -10.7579 | -44.7721 | 2025-09-14 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 133.6 |
| e80c9294-a793-38c5-bb54-387c51e76a65 | -12.9294 | -54.7333 | 2025-09-14 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 62f2f9d3-5cc6-39f4-b832-21ff45507edd | -12.6824 | -54.6968 | 2025-09-14 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 04e28004-df79-3433-a8d5-f0f7b729fd97 | -22.7282 | -49.8866 | 2025-09-14 01:20:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 54.7 |
| f6285746-12da-350f-ae9f-5933a4d803fc | -13.9473 | -44.8541 | 2025-09-14 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a702bfc9-a0b3-39a3-ae0c-f63aa227766c | -11.3301 | -50.8528 | 2025-09-14 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 35875832-10df-3977-8066-4efbcf32dee2 | -3.5995 | -47.5142 | 2025-09-14 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 179.6 |
| e883674f-bee0-3631-97ec-fa9d5ccd931d | -12.6826 | -54.6763 | 2025-09-14 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 78ea9fb0-e42c-315d-ae83-1fc639afc5c8 | -3.5994 | -47.5359 | 2025-09-14 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d03fcd3e-365e-3341-8353-ae0879e2589d | -3.581 | -47.5149 | 2025-09-14 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 1b3c51fb-bb31-3c26-810e-1f361fa33e81 | -12.7859 | -48.0432 | 2025-09-14 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4911f2d6-55f3-3d72-9381-96cd05812d56 | -12.6633 | -54.6988 | 2025-09-14 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| ec01f445-a531-309f-9160-b67e1d18c865 | -13.9478 | -44.8306 | 2025-09-14 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 12af0679-6913-30c8-9a09-3b36e99f69fd | -20.90481 | -55.18456 | 2025-09-14 01:26:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ff49400d-3895-3d4a-9e5e-648b95770768 | -21.64409 | -50.21688 | 2025-09-14 01:26:00 | TERRA_M-M | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| 8ad1adee-60b1-30ad-87f6-65bbcec5567a | -18.72184 | -51.80006 | 2025-09-14 01:26:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 8896e084-1202-352b-99cb-59582a0826d2 | -21.65973 | -50.21302 | 2025-09-14 01:26:00 | TERRA_M-M | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 41.3 |


[Clique aqui para ver as próximas entradas](README4.md)
