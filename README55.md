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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 616548ec-5299-313f-9ccc-1405382aae0d | -2.53031 | -48.24378 | 2025-10-28 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84c7030b-221e-378f-acbb-8846b7a94b91 | -7.89339 | -45.70294 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3406f306-c2d3-3ed1-90ea-680d213d28bc | -7.89409 | -45.6982 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afb64cb5-eb69-3eca-9c7a-9d59650843f6 | -3.57142 | -43.61468 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c7142a1-ca47-38f2-b139-9d902c87a1e1 | -6.0323 | -44.29851 | 2025-10-28 04:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb47ca66-06ee-3df0-ab6a-a1f599252bd6 | -3.11796 | -49.11115 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43397b7e-c6e5-3c04-b4b0-b94c6500cccc | -5.70253 | -49.19943 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b83c1e6f-a7ec-3be5-82f8-4ecbbefd3b22 | -5.62035 | -45.98358 | 2025-10-28 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1178a1b9-4d0e-32dc-b4cb-70aec9452192 | -7.95528 | -45.49641 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d9a9009c-38fe-3bde-876a-02a873ed3374 | -7.26752 | -44.96431 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 699e823f-47b2-35ae-8d00-9b1aafa66b84 | -3.6188 | -50.14495 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04933d6b-4305-3fe6-9e0e-9f9f05190d89 | -3.22485 | -48.77396 | 2025-10-28 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bc00c1c-5af2-3098-aea7-54d41b2d9237 | -5.70308 | -49.19597 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e8690cec-8bd1-30f7-85ff-f89893f22019 | -4.22464 | -43.19661 | 2025-10-28 04:42:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdaf90b0-71f1-35f6-94ee-d72e5f9c0f3e | -7.96868 | -45.4595 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4afc6c0-9db7-3a59-8b15-bcef0c03b692 | -7.81747 | -46.47039 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a65d34e8-8229-3f06-bd0a-2eda6cfbe0bd | -8.08228 | -45.96317 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fb8bc0c-07f7-31d1-9ce8-d1a147a61b2d | -4.51455 | -44.03788 | 2025-10-28 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8712cb1d-fcd2-3e15-ad5d-a239ea026ff7 | -7.97778 | -46.7157 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b600f4b8-029e-3adc-af7b-aa23dc23e95e | -3.43084 | -54.53658 | 2025-10-28 04:42:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0308cf72-8aa3-3367-8c1a-0fec108a76bf | -7.81766 | -46.44431 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c60df8a-eff7-3507-ac4c-38125be7407f | -5.0141 | -41.03924 | 2025-10-28 04:42:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1f27f6ee-0df4-396d-beb9-f580afbf0c69 | -7.96119 | -45.53661 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2a4217e2-8f80-3755-b685-9e3744d26dcc | -5.64647 | -46.32776 | 2025-10-28 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecd38a38-6102-34ea-a4d7-de1a7e6e4784 | -7.59722 | -43.59082 | 2025-10-28 04:42:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1604b3e-d60e-3180-b4f1-ec60bc530d1a | -2.80813 | -49.14021 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d464ec08-5f51-3dbd-8b41-51e020ca187c | -7.81659 | -46.4265 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3229b7a3-b1f4-38e2-8d41-dfc88eb0cd23 | -5.36707 | -50.56664 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d617711-1e8a-3e78-b650-5f50efef5792 | -1.50725 | -53.15651 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c05c1209-c10e-3842-b49a-f6ca6197d762 | -7.36722 | -47.79747 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aebb9645-5e1e-30cb-820f-ee1f1ff0eb0d | -5.79582 | -35.60268 | 2025-10-28 04:42:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 2b57ee20-214a-3cea-a476-7a1e43ae7f9a | -4.341 | -41.82542 | 2025-10-28 04:42:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f24b6bb2-de3d-3eb2-a2c1-15a5d9733a19 | -3.58617 | -43.62828 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd359a5d-025b-3ac3-9053-eeb59708e033 | -6.12952 | -41.70934 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 311e27b8-3598-3c74-abae-6a0fb7770c05 | -6.08084 | -46.99714 | 2025-10-28 04:42:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 149ec2cc-a70b-3eb2-a147-e209ef2957fe | -6.74866 | -46.35075 | 2025-10-28 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 695b0680-a613-31a9-8935-4a8ccc975028 | -2.19427 | -56.97525 | 2025-10-28 04:42:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a920d77b-fbe0-35dd-a62f-861464ec934c | -6.11339 | -41.71791 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc103dc9-f26c-3054-b03b-c49c5aa234dd | -6.24094 | -44.65195 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eabe8631-5caf-3f0e-99f7-ba1da18e933f | -2.74864 | -45.40475 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 17620f37-296c-3559-af84-b0011852d70b | -2.42168 | -48.43918 | 2025-10-28 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eed739a0-081f-32ed-a2f1-9dccd3b882eb | -4.10007 | -48.02891 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc263f0a-2650-3949-a83b-959634816cb3 | -5.7669 | -48.63955 | 2025-10-28 04:42:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0eab351e-63e9-3015-a1a8-c8ef7c85d81a | -3.09724 | -54.61865 | 2025-10-28 04:42:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 835f0c7f-6e90-308c-bf9d-d8517381e522 | -5.9767 | -42.73516 | 2025-10-28 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c6b5b62d-dea7-3464-b5b6-285499a5d0bc | -4.46218 | -43.23769 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9ef6c7fc-c17e-3167-95c6-3c3f386a99fc | -3.25136 | -50.03668 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f9134f6-76cb-39af-92d4-3488e0694231 | -8.16026 | -47.01124 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0a2f721-45b7-3d49-bfcc-0bfd5ea270c2 | -4.96702 | -56.27268 | 2025-10-28 04:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 089192ac-2598-3b2a-bc3a-92a11bd14eb1 | -3.29827 | -51.5949 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae3f54d6-9562-3d5a-a33c-b8295a025d8e | -8.00036 | -46.19775 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8f75aea8-aa43-3690-bed9-45e7a5443f92 | -7.27673 | -46.89893 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64dbc863-f9a1-3afa-a425-be9afd9dfc00 | -4.21168 | -48.35427 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb3002ad-d6f1-3c89-9a68-00a5a214d08f | -6.58998 | -48.58411 | 2025-10-28 04:42:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e11d73d9-903e-35a0-8760-42a8eb8fcbfd | -2.43888 | -49.37465 | 2025-10-28 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1a35264-5fc6-334f-8570-b605a7119813 | -6.96238 | -46.24127 | 2025-10-28 04:42:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8288b34a-7d4a-3951-931d-4e5216820637 | -3.17232 | -45.65236 | 2025-10-28 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 048a1bce-8888-32d2-97d8-4e719b3bfa64 | -7.95559 | -45.52101 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3e6ff471-6f36-368b-a9c0-6ac2247c1eaf | -3.24466 | -50.64923 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c859169-01e4-3e5c-9b4b-2fbfa21945f0 | -4.88268 | -45.74404 | 2025-10-28 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 298c18bf-8da7-3413-8da1-e7ffa32a304c | -4.58907 | -48.53455 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 915a4cca-d39e-3784-a25f-4ea441947aa6 | -4.90334 | -47.42053 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46bd394f-b1b2-38e4-a99e-8bc070976ef3 | -6.78039 | -46.45861 | 2025-10-28 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 016c3eb2-67b9-34f4-bcbc-a5f80696cd7c | -7.94154 | -45.50895 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db6bd084-0606-3b94-9f3a-2b83011509c4 | -7.06623 | -44.47929 | 2025-10-28 04:42:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b939e9f1-ce8b-3356-810b-79d76e1732fa | -6.13862 | -41.71513 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7c2eafcc-af61-3e7d-86d1-ba3b06409ff0 | -6.23535 | -43.32211 | 2025-10-28 04:42:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2bed95d8-4cfc-386d-9fde-456d255f0472 | -4.73395 | -48.3032 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cbb5ed08-0919-3029-9eaa-e2a8a7379e1a | -4.23672 | -47.58005 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffbb543d-7198-3400-8baf-e7d72ca46ea4 | -2.42114 | -48.44263 | 2025-10-28 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2e1f7155-9d1e-3519-9908-5d80388f6846 | -2.83511 | -49.4008 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 94247f48-67e1-3740-a87a-82451b00ab11 | -4.22595 | -48.36715 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 502ae9f2-977f-34ce-86fc-5517a1f7e77a | -4.34866 | -46.31384 | 2025-10-28 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f337634f-cb9c-3b16-ad74-77be12d57cb4 | -6.97321 | -47.33709 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6eaea8c-921c-303e-9d68-e87468c0818b | -7.77661 | -45.38143 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86a6fcc4-7e9c-3a53-bc75-27a630b77dcb | -7.85852 | -46.39754 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfbed9b7-8925-3985-968e-5b97ba4cb0b0 | -2.9791 | -51.33963 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5267e5c-af32-3565-9a51-6274bcf4b75d | -3.59619 | -48.9917 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e0b08d0-0dc8-343f-b2c1-2cd998370951 | -4.90732 | -47.41738 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73b67c81-5db5-3750-b905-bf3e4a83b454 | -4.22262 | -48.36663 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16a14c44-f559-3ac4-9b19-342b88497aa4 | -7.99844 | -46.19539 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e5662b0-0435-3749-9c75-5e5f847e77fe | -6.09034 | -42.14915 | 2025-10-28 04:42:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3af149aa-0348-33cd-8ef7-0cb7ac1486b1 | -6.87386 | -43.58664 | 2025-10-28 04:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bcb78d3-9130-3ca4-b5e2-58a262032313 | -3.2378 | -50.64814 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b28d04a-92da-33f5-a119-ae072b5e08bc | -7.98364 | -44.79445 | 2025-10-28 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5745e413-7610-3348-af99-000debe6047e | -7.95275 | -45.54021 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f15ec2be-6f43-3239-846e-f478c38ca0c2 | -7.42522 | -41.87147 | 2025-10-28 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2884a733-0a76-315d-bb5c-841673fba68f | -3.33423 | -50.74265 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfdf1124-26ad-3ee4-a5e1-d6be37c66ac7 | -7.36794 | -42.44559 | 2025-10-28 04:42:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b7fbd3b-850a-346b-bf90-a12894ef654c | -7.96016 | -45.51686 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6520fab-4d59-30f6-9370-539eb98f4833 | -3.69519 | -43.22198 | 2025-10-28 04:42:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bd33bf5-edb2-3d93-8f99-f8fbf8349412 | -7.77272 | -45.38087 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d89507d1-0f4f-34ff-b32a-125770f05c07 | -7.9556 | -45.4674 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cec80888-2473-39cd-b77d-fbd3cc9f532a | -3.04661 | -53.02179 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee4717d7-1f2c-3837-a969-ab812b04656b | -3.24004 | -50.6561 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f17d5640-816d-3c4a-b33c-0cc199091ebb | -2.83178 | -49.40028 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a1950344-cb5e-31ca-ab8c-213ee1d22a2b | -6.5849 | -44.62368 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 935c3beb-a637-3695-bf7f-913e35cce549 | -5.20359 | -46.14967 | 2025-10-28 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 069780bf-cdb2-3854-a784-db643326eedf | -4.80806 | -46.60559 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97d42423-cadb-3fee-86e6-19fa9a14c589 | -5.24946 | -50.45298 | 2025-10-28 04:42:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README56.md)
