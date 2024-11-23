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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4fb15e6-c90b-3df4-834c-d6dfd0696cd9 | -3.27843 | -53.83464 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67cf54b7-4ff5-3adc-a452-967beafa2063 | -3.25365 | -54.22938 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eaf961e7-acef-3f54-8ba5-2e9100793d66 | -3.22311 | -54.24073 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79e6ad65-4157-3a31-ae9a-f0d1d8cd5920 | -6.15021 | -46.67812 | 2024-11-23 05:12:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29e3d49f-6ec6-33b7-be90-66c177f0ee85 | -2.86222 | -53.96962 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3c42b1a-3276-3af4-be0c-7a6f184d44b1 | -4.37102 | -47.82498 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25f15179-b87c-3140-93a8-1cb2da9fee03 | -3.08619 | -53.25879 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73a2237e-526a-30ee-ad50-886d220108b2 | -3.22838 | -54.25351 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 613873a8-d0ea-3fb5-963c-644f9afff8f4 | -3.67305 | -51.73663 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73b13746-a6cd-37aa-9ae0-ab7f767510c1 | -4.02833 | -48.86887 | 2024-11-23 05:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0aba5ea6-308c-3124-8574-2fb3e65a9eb8 | -3.33798 | -53.32868 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abfe3d51-7bcd-3cc6-82c4-e6b416b99e9e | -3.26759 | -54.11368 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d93854db-d71a-35c2-918f-800498a9c3ef | -3.25717 | -54.22993 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db817d48-646c-3465-8d3d-580bda372475 | -6.0578 | -44.04302 | 2024-11-23 05:12:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 50681423-5586-3268-946f-e546c84bfe59 | -3.42676 | -50.98408 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e2537e5-978a-3d1f-a886-0581cbdacdbd | -3.10743 | -54.00108 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f829fa9-3b66-380d-af1f-8457c86d21de | -3.51564 | -53.81199 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c680ac3d-9f63-3386-818a-cf198bfdf939 | -3.22253 | -54.24461 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2949daf9-506f-3285-9da2-b4a22408df18 | -3.74926 | -50.00579 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68f7ae7f-35bf-3c13-8645-552b00cd0e72 | -3.55889 | -54.41339 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5d88772-8c77-3343-a400-e752c4897414 | -3.759 | -49.93514 | 2024-11-23 05:12:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a69692fa-6d04-3c3d-85b5-28f3e8a1090f | -3.11567 | -53.11432 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4934c043-f7fc-3c22-8cd1-5959ca4fec8f | -3.25657 | -54.23389 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e44ae97-0960-35fc-88a9-2ebf1d26e043 | -3.71035 | -51.79319 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b7dc143-d24b-33ad-8a72-fbca11854ba2 | -4.02332 | -48.8681 | 2024-11-23 05:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7f0b172-f375-3dea-9a3b-a356870a4505 | -4.54469 | -45.88276 | 2024-11-23 05:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5d5a0c08-df2f-3cbf-80dd-ffac30820bda | -3.21842 | -54.24797 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 435fc5bc-ef2f-378f-a308-486a700303ba | -3.63415 | -54.44407 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12e0590e-46cd-382f-a51c-5da28db1bac0 | -3.2192 | -53.93365 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e806559e-6c10-3597-97e5-a71785a852b9 | -4.69309 | -44.40273 | 2024-11-23 05:12:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31739266-b0b7-3acc-8d75-4eddbcd716f7 | -3.81363 | -51.99481 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d200429f-0521-3c61-9852-49daeb0fb241 | -2.84135 | -54.01142 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44b640d3-e140-3a3a-85f8-93ea23916dc2 | -3.28459 | -53.85587 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd6007f1-e4f4-310e-b8d8-288daa3d9d91 | -3.28035 | -53.82225 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abff9381-5556-3796-bf70-dfe4320711f8 | -4.33221 | -50.76555 | 2024-11-23 05:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6344af6e-9252-36e8-a002-2239657e2fda | -3.23074 | -54.23792 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3e182c8-cbf0-3398-8243-343a40047d58 | -4.25969 | -48.69158 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2efb7a0c-ff83-3291-a28f-8b6455884526 | -3.42261 | -53.28675 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4ab81fe-0fac-3e47-a59c-278eb2e79c4f | -3.24923 | -53.27293 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92ea72e8-c814-30a3-9ad1-d21f22d51480 | -4.74869 | -49.09557 | 2024-11-23 05:12:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13c5ccb2-0224-3289-ad86-f1bee94f516a | -3.29535 | -53.85754 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8af8cee5-5a6c-3931-b9c2-3a919d0b4d11 | -3.22897 | -54.2496 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| daaea463-e51d-3994-a3c7-6415dd81815e | -4.69313 | -45.84961 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b73d15c3-7aba-3d9f-8177-9c8d47dc7fdd | -3.98152 | -49.01259 | 2024-11-23 05:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0f91fa3-0a5e-31c0-8cbd-6319f8880622 | -3.23897 | -54.23115 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 297edaf5-69b5-3ea3-a6b1-93dc588f3a1d | -3.94259 | -47.96802 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 815842ca-3f78-39fe-bbc0-4bf4dff17a68 | -3.57784 | -54.68456 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d61df6db-3b0c-39dd-8476-515067cad714 | -3.22605 | -54.24516 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc84b14c-c58f-3a1d-88ad-b5f18c3b70d2 | -3.75262 | -50.01252 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff9fe648-7ed1-35c1-a2b9-c14819361b82 | -4.05642 | -48.32534 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a75e8b6e-2e37-3f33-8388-78b12361db3a | -5.12862 | -47.03225 | 2024-11-23 05:12:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4f372c37-9161-3c5a-939b-1df88e50583f | -2.80541 | -54.08035 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48ef0293-9e6a-301d-9e66-b7faca099b00 | -4.61058 | -46.48925 | 2024-11-23 05:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d2d6170f-ed80-3b22-8705-b2d614c8cc13 | -3.07288 | -53.2969 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d095f1d-c86b-32bc-bab7-80d4eafdc84b | -4.25795 | -48.70336 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 17f71580-2470-357d-95e0-dcb3c9211a03 | -4.35627 | -48.69442 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31e52b08-479d-35f2-a71b-d6721bd4fac0 | -3.28624 | -53.83168 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29ae28ca-d984-3a06-86b0-7ede82e9893a | -4.99714 | -49.76238 | 2024-11-23 05:12:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8be1764b-1d10-355d-9862-d252191c67b1 | -4.61579 | -46.49522 | 2024-11-23 05:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 6799e101-57b1-3455-8fd4-7c6e08b33e11 | -3.64815 | -50.8887 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 933a2fc2-da19-35a7-bb2b-318897912b18 | -3.26896 | -53.82463 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 19c57973-07e1-3d2c-b923-5897044aea53 | -3.25126 | -54.24515 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4a288799-562d-33a4-9bb0-6407dbc692b2 | -3.34134 | -53.30685 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8857293-39ec-3ab4-aec3-9574ac08ff88 | -4.029 | -49.9201 | 2024-11-23 05:12:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c9cba976-af96-3a83-ad95-1325f2090747 | -3.32206 | -54.08952 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 457e59fb-f1b3-349d-9ebb-849e2b9f4770 | -3.57899 | -54.5159 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35380d5b-a028-3d70-a245-f279f6372da6 | -3.67695 | -54.58536 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e4178fb-c233-3630-8e10-7d350457def5 | -3.22956 | -54.24571 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88174617-facb-3f09-bbf5-d05e4ecab8db | -3.25656 | -53.26723 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| addaa721-9cef-325a-81ee-8a7181fb2c08 | -2.84965 | -54.00452 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60f929b3-4c9d-3de9-9c1a-7b3f11563ac8 | -6.14361 | -46.68173 | 2024-11-23 05:12:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d59f1795-11f6-330a-ab5b-a92226b3a365 | -3.27741 | -53.81751 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 932529b1-c938-348a-a63a-2cb8a4791ca2 | -3.4867 | -54.47832 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 863ab814-1b39-3773-8fce-a97af67224bb | -5.5708 | -46.293 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0bca5cb-70a9-3625-bc9f-064a19a8ab4c | -4.09037 | -47.02682 | 2024-11-23 05:12:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53cefa33-77fb-317d-8a27-995b3aa6ae1d | -3.23778 | -54.23902 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 921348e3-b51d-3bdc-a16d-31cc9e49c1fe | -6.49578 | -47.04646 | 2024-11-23 05:12:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 90cf8e08-b04d-373a-b566-9de41e187205 | -4.25704 | -48.69734 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 0419dfae-0e14-3dc1-8561-2e28a8753743 | -3.46128 | -49.68956 | 2024-11-23 05:12:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3db64fb-c476-3a0c-aae8-dd29aae7319a | -3.24833 | -54.24067 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9388269c-da49-36d5-ae85-eae8c163f4d9 | -3.25192 | -54.21702 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2aa3819-cf3d-3650-a192-0e1289eb5e73 | -3.10994 | -53.17714 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6166da83-5868-3fea-bc44-24f51ebce340 | -2.83367 | -54.01432 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31c239bf-4551-3ec2-8274-957c318b365e | -3.28408 | -53.83479 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 717890a5-cea4-30a6-9feb-c6feafdb2d26 | -3.50779 | -53.81516 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40413a10-d101-393b-ad63-698698f0855f | -4.02789 | -54.63304 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54018474-7c78-3b53-ab97-97cf497fcd9f | -4.95076 | -47.80114 | 2024-11-23 05:12:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3427115-b7f7-345d-90a3-22eed0432917 | -3.01839 | -54.06246 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff3ff22e-237f-3bdd-b630-6b3b23b5d374 | -3.25305 | -54.23335 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 66ad0ade-3b5a-366e-baa8-46405f61cf4c | -3.12446 | -53.10664 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66ac5652-242c-33c3-9cd5-87d6efde791e | -3.76363 | -49.93589 | 2024-11-23 05:12:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be2daf4d-003f-33f7-84e8-b385e38c073d | -4.60402 | -46.49296 | 2024-11-23 05:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 24f55748-8d12-3e09-b58d-de06d6801954 | -4.369 | -48.50011 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b37b7615-8826-36f7-b791-3b24cc638eaf | -3.83539 | -52.25756 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5861cadb-26cc-3918-a94f-9459c26cbe60 | -3.24661 | -54.22829 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd7bda2a-a46f-394b-87f6-06bddfb34c8c | -4.39789 | -49.77304 | 2024-11-23 05:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35ee50c0-216e-3f78-8543-17a9b288df00 | -4.48323 | -48.11775 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd55bc69-96bd-3b5b-aefa-b04b3076aebb | -3.25418 | -54.24961 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca311eb7-e223-3621-9315-089e79bd6286 | -3.70503 | -54.54212 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd63ee6a-6fa2-338d-8f6c-d1eba0253e62 | -3.1799 | -54.3305 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README58.md)
