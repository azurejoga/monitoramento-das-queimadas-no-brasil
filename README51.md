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
| 71ac56c3-8568-3674-a8cc-917865302354 | -3.59877 | -49.9987 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7ca5cb0-4f1d-37e5-b397-83bc5ea5846e | -3.09444 | -50.35098 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8afb8b08-48ee-3260-8891-0b7338bfa4f8 | -1.14574 | -51.67879 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 060621ed-0fb4-3974-b367-79d396a2ebb1 | -3.59767 | -50.37065 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4053653b-9330-3643-a428-c5297fe4357c | -2.68375 | -48.62854 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf72c25f-c81e-3a9b-9a43-45d9048816bf | -2.22889 | -47.77096 | 2024-11-30 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb730f44-73bb-3a1b-bf7d-966edf02cb05 | -1.39442 | -53.6372 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8a212cd8-e2fa-325b-9c6b-6a201f365ffb | -3.08134 | -49.50143 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec93d7b6-c2e2-3899-82ff-922a79a1cbd3 | -1.00125 | -53.69778 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e798b21-cfe1-366f-bcaa-3607b78b327f | -2.9724 | -48.04013 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f259e6f-4a69-3ba1-a290-9689e2481ffe | -3.77838 | -49.98056 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ad96c86-4200-30d2-809d-31949c2d0f08 | -3.5132 | -53.78317 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96c96f8e-71a4-37ee-bbae-63d7af072ebd | -2.58707 | -47.03267 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b31b96db-edfd-3f94-a597-98d72645c87d | -2.3845 | -47.88477 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f24f46c-5079-30a9-9323-c07d4216531b | -2.7111 | -46.12568 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 832411d4-985c-349c-a8e0-58dcfd84a355 | -3.71592 | -47.14939 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 567a5d39-b8bb-3398-8741-492c0421fb5f | -6.4134 | -52.43432 | 2024-11-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b2f71dd-3012-3265-a06a-fa36c19825af | -1.86156 | -48.00969 | 2024-11-30 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbc3ca32-1d5b-3f6b-a5ad-d7af4259e3e6 | -1.54976 | -52.27741 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a5f9fa6f-8757-3b9e-b434-7cce8ec24da7 | -1.50126 | -54.94571 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 636000cb-43f9-3e2f-9b90-d45821dac49f | -3.25214 | -53.63123 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8d155db4-ba94-35bc-a9ca-b15970e997d1 | -1.16405 | -53.77773 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c6d202a-7c57-3c8a-8c09-f0d52ffeaae8 | -4.97886 | -47.23809 | 2024-11-30 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42352380-e993-336f-b276-ce83ac6a6c18 | -3.59118 | -51.32062 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 351fe128-d042-3076-9c8e-42ad620c9f92 | -2.84673 | -46.68739 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89692045-802f-3dec-b054-8d7255467c25 | -3.11135 | -53.99898 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b82f15b-c65e-39dd-9332-5fe713cec56f | -3.38178 | -50.31554 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2d06a77-5557-385d-842c-8b53aa19f070 | -3.24032 | -50.24593 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6949038f-88e7-37b1-969e-352cdecee34c | -5.42186 | -44.85371 | 2024-11-30 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a6e6d78-913d-3666-95c6-01489959de8e | -2.47576 | -50.40583 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9260237-ec90-38a1-bea9-165179844894 | -3.02757 | -51.53549 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15db8c8d-07d3-32e5-9214-7f401e275b6c | -2.62788 | -46.88073 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9f51e16-82e4-35e1-bb29-22b1f6fdbd64 | -3.11819 | -53.10376 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77b0d9df-8100-36d0-8951-b8c485316b1f | -2.98568 | -53.28036 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e6b6801-022d-397b-9da5-a8eacabb1d0a | -1.72506 | -52.49313 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2383edc-8264-3a7a-84ca-15d68fbc2981 | -2.19447 | -48.34065 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 313a2a1a-bed8-3308-9726-d1bc53888910 | -3.69827 | -47.12762 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bfd581c-0531-3b1f-beee-73072f236c28 | -1.26819 | -54.5587 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| da3dab43-9aac-3c14-b1ab-5a3e7e77ffd8 | -2.95476 | -53.87982 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 69daf0b4-6f41-37e9-b240-da2f4809da09 | -5.12288 | -45.15619 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc76ec9c-5c11-34e3-8654-a1ddbd54ff5d | -2.37011 | -48.63223 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eab161bc-fc54-3d75-a058-a347d0808f45 | -2.24212 | -47.99068 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ba5bbbf-013a-37a7-93ba-57ae0993c52d | -4.43435 | -46.58009 | 2024-11-30 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af280125-8b17-3368-b4fb-3c7d50826889 | -3.16456 | -49.53554 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26c5bf21-759b-315a-9880-c91752477d4d | -8.38213 | -44.47624 | 2024-11-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b28e562-aead-36f9-aac4-d251e2afa96e | -1.16155 | -53.68641 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bd4856a-81e3-3652-bd3b-70eaf37a6706 | -1.80505 | -52.08743 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c41001c1-8152-38ef-8b22-37ecf47ddcb4 | -1.72024 | -51.18332 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33d88342-bff1-3587-965d-f0b95692405a | -3.26919 | -50.55815 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d8fe25d-3eb3-3366-a3ab-0a4807ac111b | -2.38301 | -54.32793 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 18515472-41e8-35e3-a8a0-50969e167e43 | -3.11713 | -53.98895 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a3b30560-3a4c-3306-a54f-78310d9e9e0c | -2.78761 | -53.20906 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb100724-471d-33ff-95f0-0ec2e8c9e24d | -3.58873 | -50.36198 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d8e4ac3-7a56-3e1c-9ca8-b9e4b1b9ea20 | -1.13443 | -53.38919 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abb306ed-06d0-3571-9754-2581c14135d7 | -4.09687 | -50.35829 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98952a12-8249-3f09-97ee-810d19824629 | -2.11379 | -46.5513 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1229b903-f8c9-311d-baa3-59d29bf8409a | -2.34748 | -53.81113 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c7f6b73-87ce-32de-90cb-b2f49e35a618 | -4.01133 | -46.52773 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d4c5b4d-8d41-3682-bfc2-7ebbb823ff4b | -2.88139 | -53.9437 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8150053-2673-35c7-85dc-ee0e1f9ce808 | -3.03865 | -51.03879 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a8967d8-41a9-319b-9ba3-2e03832aeda1 | -3.80087 | -46.69189 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10a431af-1f36-3b93-9e20-03fdf44dab1c | -1.55347 | -52.27798 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 11f771ce-2e7a-3bb4-bdb8-26de521a4a06 | -2.27612 | -46.4324 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d06554c4-e599-3555-b578-1a8d902758b5 | -2.03557 | -46.51313 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e16f98d7-422a-319d-83ea-659e126e82d9 | -1.3448 | -52.12798 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91e7320e-8e7d-3658-a9a4-dc12ab508460 | -3.96883 | -47.23971 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a4b14dc-24df-389c-874a-65b0d422a02f | -2.715 | -48.60168 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6a7dda5-53d1-3fa2-a2f7-ec8d7b5878ea | -3.28908 | -50.27883 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dda48e3-d08e-3c51-bf7c-f12020be6fcc | -3.25086 | -53.86015 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a98af8a-e91e-318d-a9ac-629694804b13 | -4.18124 | -48.62223 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6066bc1-461b-36d9-b7c5-3c7986d5f824 | -3.5826 | -50.33555 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7653f05-7026-36d4-9550-aa2bfad41cf5 | -3.08919 | -51.03128 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5301072a-38b4-3bb7-bdac-85fe66be8482 | -3.5797 | -50.41897 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c630fbd5-49e7-3743-8b9c-4eb647085b8a | -3.86698 | -50.15232 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a382db60-ce22-32c2-8577-142a197a945c | -2.22685 | -46.56855 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1edbc69b-2107-3d25-ac4b-baac1e8d00c5 | -3.97185 | -46.90055 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9bfef1d-c682-3370-bef6-72f3b9d8f1e8 | -2.6145 | -51.76283 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72315c12-60c0-3273-b52f-058e6a83d16d | -2.94862 | -47.9967 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f4b4f33-af30-3121-a728-9215065e5d82 | -2.37835 | -49.14686 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98f9ab58-cf27-3c8c-9eec-de3c901a99cd | -2.53748 | -47.33291 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13e9c09e-abbb-3efe-9885-19d247bb8b2d | -3.54341 | -50.1772 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c6e9c93b-527a-314c-9d6d-b075d059b612 | -6.9425 | -42.78487 | 2024-11-30 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7e94bfe4-b794-35c2-9a7d-d336580737ba | -2.8454 | -54.04012 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7d4834b5-b047-3c46-b371-14b5fae7c9d4 | -1.25287 | -54.54375 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| feb5f2a3-0ae6-30e5-a433-c1a9b83340d3 | -1.14908 | -51.70482 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 693fd8a9-a33b-380b-bab7-56358de9b61c | -3.06023 | -50.32741 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aab1b1f-039f-31a9-bbca-a8e58b5f1425 | -1.66337 | -52.19979 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7d38d29-f813-3735-94b6-4eaed217bade | -3.94189 | -46.88818 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6094dc5b-e629-38b6-9432-4e39e08e56cf | -1.0043 | -51.72166 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 421dd7ff-cc2a-3c9b-bba0-113e81d3e0cc | -4.17892 | -46.57085 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6815ceb9-475b-3567-b6d6-98c2dee607d2 | -3.19499 | -48.57851 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89ebd9f2-97ac-3d61-9420-2f58e91e0e4c | -1.19523 | -53.86798 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bda9817b-3d45-3687-98b7-144398903352 | -3.9554 | -46.72989 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf23c9cf-7ea3-30a3-b436-d64d89d716f2 | -3.94768 | -40.97458 | 2024-11-30 04:40:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0433d408-b797-3247-886b-0a3f641fe849 | -1.88448 | -52.66 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46ce60ea-4622-30b5-9afb-2c62837cf70a | -3.79332 | -46.69466 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35e3c520-4a43-38a5-8a6c-de40e32a17e0 | -3.1388 | -55.0039 | 2024-11-30 04:40:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fc6fff8-90da-3c05-99ee-eb4d4fd236bd | -3.39409 | -50.30288 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b91a26b-e6d7-3206-94fd-be15d91a6b2d | -2.46374 | -46.8975 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb4a3c6e-1c0b-3a4f-8293-c5b1926b065e | -3.79071 | -58.97213 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README52.md)
