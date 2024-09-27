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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67256a62-2517-346d-b120-08267a2246c4 | -11.18279 | -46.00486 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 605adea5-6c86-3cca-a795-17d81b55cf38 | -11.17712 | -46.00648 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b37c19d-08f2-328d-b3ae-56fd9171030e | -10.82341 | -45.98791 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8ecea60-fe15-3024-ad89-bf4794a7108d | -10.82271 | -45.9928 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47e1d6de-5393-3b1a-979d-22d972858abb | -10.79661 | -45.89867 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58e12cb2-84ce-3514-a90e-d1dd247e0b6e | -10.79273 | -45.89815 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 717cb3f1-b374-323a-9755-6447c068c92a | -13.33828 | -46.3424 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 833e02cd-d570-3755-af03-c85d1b6d46eb | -13.33759 | -46.34743 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07d97c7d-8fe1-3bee-a6e4-38b2c5f0f16f | -13.33272 | -46.29573 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7b6c4dc-f2c9-35af-85b3-bf8b4080d6ee | -13.33046 | -46.34129 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0364fb5-7223-3c97-99e9-dd01ecb2111e | -13.3294 | -46.29087 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb44d7cb-e928-3dae-8985-47496d7becf1 | -13.28622 | -46.31483 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e39e9977-62b0-3f3e-8481-4a89626b6dbd | -13.28593 | -46.31366 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9850929a-338d-395a-be58-e24ed2b58b64 | -13.28559 | -46.31943 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 548ab6f1-550c-37e8-a30d-1686dcfedaca | -13.28494 | -46.32431 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7979e054-ceb2-3e39-8728-50ad10ab0dc3 | -13.28461 | -46.32304 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6961e306-22b7-3b39-8d14-b304b1a11888 | -13.28295 | -46.30951 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 754de958-7223-3907-b559-25a982a90ebe | -13.28269 | -46.30839 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ec28529-9e5f-302f-ad59-7e46e7756cf3 | -13.28206 | -46.31285 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c3ec05dc-c71d-3d49-8808-7fac4ef9e5cd | -13.27879 | -46.30769 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b688bfe-f889-37f5-a603-eaa63bb9115d | -13.27485 | -46.30735 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2503ebb1-b643-36de-9f49-b50843254087 | -13.27422 | -46.31181 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b5782a92-cb89-32fd-884e-98812a866a98 | -13.27028 | -46.31144 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eb7e12ae-a983-3c2d-a00d-0c5b0bcbe2d4 | -13.267 | -46.30639 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a801b31b-fcf4-36e3-99ef-b74590dd523c | -13.2631 | -46.30577 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f2e394b-9b53-35b6-a956-c7b6fa9f5206 | -13.25916 | -46.30539 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86169486-ade2-3563-8396-5b2c8d0158dd | -13.25591 | -46.30007 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1b78f19-8761-3c6c-a3a0-aaf0456fd678 | -13.25522 | -46.30505 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48d1446b-d682-3468-ad7d-5eed4ccb6622 | -13.22668 | -45.638 | 2024-09-27 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40b31001-4141-39db-9b85-881c5ed76345 | -13.22618 | -45.64171 | 2024-09-27 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 558c3acd-fe63-3c3a-9b3e-0bab221975ca | -13.22567 | -45.64542 | 2024-09-27 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9686efd5-fa41-341a-8c0a-3b68711d661e | -13.22517 | -45.64914 | 2024-09-27 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d55901b8-f24e-31b3-b618-0fcfb41ccd88 | -13.22466 | -45.65286 | 2024-09-27 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4f9add4-6315-3d3b-87de-5676889b6cb9 | -13.22109 | -45.64856 | 2024-09-27 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f706a21-2c81-3d5d-95f3-61cd3a655ed2 | -12.95732 | -45.39082 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46d16aec-7d61-348e-a019-45f813479ddb | -12.9568 | -45.39463 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37844a92-3b3f-35a1-8746-d2ce518f1bd0 | -12.94339 | -45.36935 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4ab4083-2091-301e-8c08-a76198fc19ac | -12.73275 | -45.5741 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76ec65ef-819a-388a-8100-c7e0e0f6e4c6 | -12.72868 | -45.57353 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23f0aac7-81fd-39eb-920d-8d20d0817c0d | -12.72564 | -45.56558 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59b7967a-454b-3d24-98e5-09d733c6b563 | -12.72513 | -45.56927 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d30d10e-0e9e-315f-aea3-1f63eef03c26 | -12.72208 | -45.56131 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55811fc4-593b-342c-9668-993fd4862e54 | -6.40965 | -45.99918 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07ea59c9-c88b-3884-9574-e008b8cd20fb | -6.39859 | -46.63459 | 2024-09-27 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 573d04da-47ae-370b-8fb4-7618f0d19d13 | -7.83012 | -45.49757 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19cd0bb9-676d-309d-bed5-ce9ee34f144c | -7.81865 | -45.49586 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5dc376a-eb97-3836-9998-b83a1674abdd | -7.90491 | -46.41206 | 2024-09-27 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08019efb-7d5f-3b7d-987f-b93b7fe7e440 | -7.8062 | -45.52788 | 2024-09-27 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d878bcf3-0535-3eed-a1bc-797875058035 | -7.76691 | -46.15725 | 2024-09-27 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4477854c-c7ad-3488-a4e2-0383483678fa | -7.76322 | -46.15677 | 2024-09-27 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42b71a7b-3d3c-3d77-9e3e-739a04127672 | -7.76259 | -46.16103 | 2024-09-27 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f326b40b-a406-3001-b742-5324f587d878 | -7.60211 | -46.35822 | 2024-09-27 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89c85d69-c8d2-3420-b8fb-d2077173899a | -7.60149 | -46.36236 | 2024-09-27 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28373fe4-9dae-337d-a972-fe3f65b6d195 | -7.60024 | -46.37075 | 2024-09-27 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b24758d-667f-371e-91b5-015385d9502a | -7.59787 | -46.36181 | 2024-09-27 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21999f98-1cb9-3b01-8432-8c4c1f7209dc | -7.55958 | -45.81158 | 2024-09-27 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9d9089a-6730-3c0c-b8bb-42c5bb1f81b1 | -7.36409 | -46.54701 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 844a38c7-9253-31d4-a166-0b52471c011b | -7.32886 | -46.05803 | 2024-09-27 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| edd823e9-e9c1-3579-8f1f-9103846dbfe5 | -7.27935 | -46.60737 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 899b7494-582d-314f-81c9-d7735ff4a741 | -7.27577 | -46.60685 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92eb2194-fc14-3c33-a763-7fb90736af6d | -7.27515 | -46.61096 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c98e2d4d-2503-35d5-b2eb-2f4696b43335 | -7.27157 | -46.61044 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2c4199c5-7775-3bb5-a8dd-8c1f43d7230e | -7.26739 | -46.61399 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ce930ba6-72c5-34ce-9222-e246d29bb760 | -7.25953 | -46.07135 | 2024-09-27 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23b0834e-2ac0-3fc7-8d8b-d9d9a5018f9b | -7.09952 | -46.44688 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cb583ad7-ea5e-3a8a-8e47-12872bfcfce2 | -7.09794 | -46.44403 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bf1e28ff-1e8f-3cd7-8b8e-c5922f7e4d14 | -7.09731 | -46.44815 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 08a90404-0c8d-3248-88f6-57b2ca18e646 | -7.09592 | -46.44638 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b5a6ab8c-2d09-3da0-91d2-56420b902272 | -7.09533 | -46.45044 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bbca52e7-d2ef-3bc9-b065-612a2af19743 | -7.09371 | -46.44763 | 2024-09-27 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 479c2d71-e3fd-34ab-b71b-2e1542c9bf14 | -7.01072 | -45.64811 | 2024-09-27 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 984367a8-5568-3b7f-95f9-3547767a0c0e | -6.96254 | -46.18026 | 2024-09-27 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a5c90ed-402c-372e-b6b6-71c8d62c88f0 | -6.84212 | -46.43218 | 2024-09-27 04:40:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd8c5c5c-bf14-3632-a8a7-f970ec6cf702 | -6.66508 | -46.33656 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2ebf369-3a3f-365c-b89a-cbe17dbfce7c | -6.66445 | -46.34066 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3550896-1e8f-392c-90f5-ef28b9475124 | -6.56303 | -45.71841 | 2024-09-27 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 201a9192-c9d2-39a2-be00-c36156f96832 | -6.56239 | -45.72277 | 2024-09-27 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 649e166f-310c-3f0f-b65e-1a0d5befd6fb | -8.08441 | -45.48189 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d38fc28-b079-32b5-bb34-a90db1aea7fa | -9.25302 | -45.74769 | 2024-09-27 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46d1ee63-3607-3b4f-b0fa-0ffcf8c3101d | -9.25139 | -45.74982 | 2024-09-27 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f373b83c-d8d6-37c0-9388-88c0adfbbcce | -9.01676 | -45.9604 | 2024-09-27 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6a1ea0b-9d6f-318f-b6ef-553061b81b06 | -9.01663 | -45.95846 | 2024-09-27 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb7c1efe-bf9c-36e7-b4df-b20285cd95d8 | -8.92718 | -47.08308 | 2024-09-27 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e91815ac-488a-357f-8ced-5be7758f01f8 | -8.92657 | -47.08713 | 2024-09-27 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5536612b-6dcf-315b-af36-3be378434781 | -8.88733 | -47.15561 | 2024-09-27 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0108bb98-fb46-34b5-8a6c-98e51c14b543 | -10.71591 | -47.36642 | 2024-09-27 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83e9e5d0-d697-3963-8c0a-1e2f19991dea | -10.68783 | -47.40854 | 2024-09-27 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e613a2c-0f7d-3adf-9080-8924328b83d4 | -9.79841 | -47.16341 | 2024-09-27 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a83dd682-c4d1-3e25-ba80-71510d4aadf0 | -9.55987 | -46.57921 | 2024-09-27 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d6e633c0-b973-3440-bb13-024596fac44e | -9.55709 | -46.31557 | 2024-09-27 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91de50f1-9e61-3451-b2d7-6d40512d07c6 | -9.55619 | -46.57871 | 2024-09-27 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1f5c5c59-f0d8-36c5-b5c7-463f8dd439bb | -9.55336 | -46.31504 | 2024-09-27 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51279261-962c-3c95-9c76-d85d0045d37c | -9.54823 | -46.58183 | 2024-09-27 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87730b2a-4363-34f5-9f11-0db95d930066 | -9.54648 | -46.56825 | 2024-09-27 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36c0c2c0-642f-3658-996b-5590ea818f25 | -9.54457 | -46.58122 | 2024-09-27 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e2f7847d-1a92-399f-99ff-c82a7ccc0260 | -9.4409 | -46.47276 | 2024-09-27 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48c0fbe3-eb7f-3659-9f36-b469d05555e8 | -10.86321 | -46.40868 | 2024-09-27 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fa1bb97e-4b88-32d8-931a-961c3a365d56 | -10.06746 | -46.05261 | 2024-09-27 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da90076c-41ea-3f6f-aa38-fa1b7308b1af | -11.33355 | -46.23221 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c820b41-18af-35e0-8337-b51fbf37cd38 | -11.33287 | -46.23698 | 2024-09-27 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README88.md)
