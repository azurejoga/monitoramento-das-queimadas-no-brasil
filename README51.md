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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79898f61-a974-3c2b-a84c-6809265f952f | -1.20857 | -49.28624 | 2026-10-01 04:32:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 08894932-6ba8-3fec-a3c6-e2095b516f5e | -4.28082 | -50.7634 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 9679090e-717c-3e9a-867b-bf6d8b18f41b | -4.26759 | -50.75426 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e930afa4-0ccf-3654-a052-1d0e6acb1ddf | -3.41935 | -48.33656 | 2026-10-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af489749-a0c9-39e5-919c-037ecb7b5aac | -3.00819 | -51.07176 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b3ab84e1-6f37-38af-bf25-19ea777d1dd4 | -4.25897 | -50.73193 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a0d76eb-0e44-3b9c-967f-84684015fa61 | -3.43115 | -50.43554 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4ed5a94-b511-3363-a724-efa8d7f3a773 | -3.09877 | -50.30357 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e745129-7f8c-3b88-9d10-0dd5960090da | -4.12428 | -51.02675 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fc6e347-1315-32b7-9704-29df7f92d24b | -5.73771 | -45.1614 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de92b418-7a4c-37b2-a69c-5c5f1340f823 | -1.41901 | -48.89852 | 2026-10-01 04:32:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30829eb7-4ff2-3d15-abe9-1af6b3d2bc0f | -4.26237 | -50.77624 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2c4d69df-7e60-3a58-9267-d9207c3b49cf | -3.00951 | -53.8777 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aae14339-f74e-3c7e-a9d1-11b5976571b7 | -2.26735 | -48.74729 | 2026-10-01 04:32:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f406d1b4-5dd5-3c66-befe-32a1aba75314 | -2.97175 | -51.03539 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2b8535f-15bb-338b-b4a7-92176181ea3c | -2.9847 | -51.0337 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 76548d66-6cf8-39aa-b32b-fcfc3fb826cd | -2.89457 | -54.13681 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62f2ab43-1264-31e5-b401-e71f0924654f | -4.24379 | -50.75039 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f5d6c29d-d958-3c5d-9956-5bb3ddf97f9c | -2.03471 | -54.06034 | 2026-10-01 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 19908e90-992f-39ab-8047-dffbe9ec793e | -3.87289 | -50.43618 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d6c9f6b-b984-3490-aea6-4ac205c751f5 | -3.00466 | -51.06737 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 846bdbec-3a23-3e35-bb23-93aed618d753 | -4.31085 | -50.77887 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2b782f3-821a-3af2-ad96-1ab5ce2444fc | -4.26808 | -50.76648 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| aac80ab0-682c-387e-98eb-49a3fc36fffb | -4.26609 | -50.73827 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47db668d-8058-3790-919a-09cf660e7fe2 | -4.26211 | -50.73769 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28a53876-b48b-38c3-915c-980e056f6224 | -5.73977 | -45.05988 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ca5d743-8eed-316e-a790-88911dddf961 | -4.25337 | -50.74144 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a0f5de8b-76b6-3fd8-995e-5ef794cc37fc | -3.10296 | -51.27074 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd45eb4b-3e5e-35e0-9e8a-caf7f81f3b4b | -4.25403 | -50.76261 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3f93e4b4-7654-30ee-8aa5-b2506e8357c2 | -4.27155 | -50.75496 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| fc3202fa-4035-378f-9ae0-24fadf17da8d | -5.42927 | -43.45235 | 2026-10-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b8630f46-f667-3268-a7ef-1f91e1ee9fcc | -3.21564 | -48.81467 | 2026-10-01 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff7afa62-7f4f-3ce3-85be-148ab9feef3b | -5.27301 | -46.1514 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d71c72f9-cc18-332f-806d-97a2bbbe0cba | -4.25172 | -50.75165 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 4961e128-2a59-3133-935b-8a481f8ba041 | -3.54537 | -41.57194 | 2026-10-01 04:32:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5645a03e-c7ff-3c1f-b525-2f123885e6cd | -4.28706 | -50.77489 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 909.5 |
| 6f2d31f6-ce1c-39cd-8237-cda9e651c812 | -4.29355 | -50.76035 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 264862f2-c682-36c6-9b22-9da8e7282f60 | -4.31482 | -50.77954 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d5b6d416-694a-3a63-ae11-bab642c203d3 | -3.09656 | -50.26759 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9b0a1eb-62c5-33fb-bf80-ebf78db234f3 | -3.57041 | -51.48246 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 27ebcdf9-fc13-33d0-adb8-12fba65436dd | -4.25718 | -50.76836 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9f015ab7-9701-32dd-80ca-8083c292bbcd | -3.16645 | -54.10279 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ed7c7aec-286d-3007-a1f4-0616d281a603 | -3.48472 | -54.73097 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c697ad50-9b6c-3c9c-a1cf-7c56cea47d3b | -4.2643 | -50.77473 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| f302c17d-f6e1-34d9-845d-0f6a82083736 | -5.74051 | -45.16545 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| be6a25a2-13c5-35b1-8739-f3c375f134c4 | -2.89356 | -54.14286 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5873f258-178b-3b77-94f3-487e039ac597 | -6.69761 | -45.62509 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc695330-d077-39dd-ab88-7e5b501a507c | -1.20784 | -49.29085 | 2026-10-01 04:32:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2b0e9566-f653-3425-9b55-1c69cf891089 | -5.42603 | -43.45292 | 2026-10-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a13b65dd-0bc5-3163-89a8-a429d0837248 | -1.12116 | -48.86548 | 2026-10-01 04:32:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af04d4bf-e6ac-305b-9357-0f03d5390e59 | -3.8029 | -51.02633 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06e414fd-d6c4-3ae6-891f-1520d04b41f1 | -4.30124 | -50.78771 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 850300d7-bb8a-37e2-9f20-6d75398b98eb | -4.28857 | -48.56144 | 2026-10-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cd87a06-e0a3-39d0-a77a-b9ef7086559c | 1.78924 | -55.6536 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf0768bf-e9ad-3da3-bcc1-8a018aeea275 | -4.28847 | -50.79092 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b0211464-892c-3ebf-86c3-5e6323f4f191 | -4.27402 | -50.73951 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9072a7ee-9752-37ca-9c45-4854811bebc9 | -4.27033 | -50.7774 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 77ca744d-356c-3f4e-9f65-8c2e8a62c3d5 | -2.5552 | -49.10269 | 2026-10-01 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22d1ec85-b849-3e7a-8997-5d428081ff61 | -3.41908 | -54.54331 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3cf7d75-9e42-3fb2-b952-d75c85154cf5 | -4.25615 | -50.76472 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 722694f9-ec8e-3ee2-9659-5383503293b0 | -4.28874 | -50.76479 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| c6b6b934-c586-3117-9b81-e744c4951f9e | -3.24862 | -50.81954 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6403ea59-802e-32f9-9af1-221f24818b91 | -5.10972 | -56.0142 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8315aa9-adf3-3df6-a3d8-c6681fea4f59 | -3.18208 | -54.10269 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 162dd4e1-5498-3897-9522-1d220daf2eb7 | 1.78854 | -55.64907 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 85a32997-bbea-3f1a-8286-2e51fd47d9b0 | -4.28729 | -54.79608 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b05ad8a6-15e6-3830-a8fd-274d85ebed35 | -4.26379 | -50.79209 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0536c60a-b744-3008-aacc-c0b8e67da113 | -6.82783 | -45.18005 | 2026-10-01 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 200eb6fe-c131-35b8-b3a5-3f5054758e6c | -3.11612 | -50.27077 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c56a311d-2733-38a3-a6fc-dcb699f401f7 | -3.16213 | -51.35528 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 02f2409d-6cde-397a-bf32-0b69baf79a46 | -5.75501 | -45.16043 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7ab2dfb6-748e-3b2d-b721-a02871466fc9 | -6.73201 | -45.53671 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 074b8eec-0995-358a-8146-17463eaa3248 | -5.74831 | -45.15941 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 21e89d35-36d6-3fb7-a981-7e6d13240b2f | -2.96 | -51.02969 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41b6211d-3044-3550-8012-0b3a9979a8ef | -4.25959 | -50.74427 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 23a367f7-1876-35ed-b899-d9fc0dbd1e19 | -3.95389 | -48.12672 | 2026-10-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 061ed7a1-93c8-3edf-8372-e24dbca7fe7b | -4.28818 | -50.74365 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b20ba78d-2719-36e5-9a86-e3a0fb59268f | -3.00305 | -54.22818 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e43fcad-0d7f-365c-a356-939597c075f2 | 1.04046 | -50.02195 | 2026-10-01 04:32:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaf81493-7b95-3e45-9958-04af2e36dac0 | -4.26347 | -50.77994 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 31be4acb-2e6f-3015-805b-63459d78367a | -3.99137 | -49.04011 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42602469-8b17-30c7-9da1-4f3004e395da | -1.48679 | -48.90039 | 2026-10-01 04:32:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26a518ea-c4a8-3c7a-abd0-c02fa9c37752 | -2.96351 | -51.03404 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88f86f7b-fbe7-3026-b649-dd287b27fee8 | -3.06063 | -51.34048 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 087e17a9-79d4-3a03-bf19-75c5908e4c34 | -3.48547 | -54.72823 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f87d062-bf94-3a12-a32d-f67e17a8e2e4 | -2.96592 | -51.01929 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6e464c6-ffba-3a74-a7b4-d80ab6cd528b | -3.18611 | -48.02422 | 2026-10-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cadd5e61-daf2-346c-ad9a-0b36d1f8a34c | -3.16944 | -54.08525 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cfaf768e-b860-3fa5-83c1-6081b89efc8f | -3.37734 | -50.84834 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcc5c821-5c3f-3d02-81b0-1a86cf792553 | -3.84888 | -55.81211 | 2026-10-01 04:32:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bed252b-9310-3d8d-8199-be56a46d5bbe | -2.91303 | -51.31644 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 330ee99c-4c37-3744-b8df-2f00bcfdec61 | -4.53919 | -50.78419 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23ccbbc6-f0d9-3f18-842b-68fa7f06ab21 | -2.902 | -54.09199 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db4aeda7-9467-3b6f-b716-30de28987ede | -3.11373 | -50.28563 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fe236486-6e13-39df-9d6a-68659bcf255c | -3.15793 | -54.09969 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 101e8e15-3ee2-3d29-a4f5-722942a8033b | 1.71004 | -55.91019 | 2026-10-01 04:32:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 577c8662-04f1-3af3-abd3-024bb7f57b79 | -3.16854 | -54.09848 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 50766196-ecc6-3c48-9626-a12cb1b5e56e | -4.28111 | -50.73726 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 42fcaf46-c66d-3328-a0a1-ec88f6c7a264 | -2.29674 | -48.58624 | 2026-10-01 04:32:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bba078a-a330-307e-aeb5-7035f96db731 | -4.26185 | -50.75502 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |


[Clique aqui para ver as próximas entradas](README52.md)
