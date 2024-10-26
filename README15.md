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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5616ea55-973a-3bfd-9f35-45c295b097bb | -4.58 | -48.0132 | 2024-10-26 01:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 303.9 |
| de9369fc-5cc1-3840-9464-dcf9a3fe899f | -6.0931 | -47.225 | 2024-10-26 01:25:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 7bd7b764-f29d-3ec7-bc1f-e6cbcbb8559c | -7.6474 | -63.4584 | 2024-10-26 01:25:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| e2050e18-0868-3aca-8b65-3ca89bdc2a68 | -20.3088 | -55.367199 | 2024-10-26 01:26:09 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 31c68618-17cd-3525-9193-ba70429b2e25 | -20.2974 | -55.362301 | 2024-10-26 01:26:09 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c2ae0733-3938-3781-bcaf-31066492c887 | -20.299 | -55.369598 | 2024-10-26 01:26:09 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0ddeefe9-44f7-3050-bb8b-1384824b3c74 | -20.300699 | -55.3769 | 2024-10-26 01:26:09 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8501afcf-7bbb-3589-b74d-0e7a21880152 | -19.640301 | -56.633801 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6f78e221-ad6c-3cbe-a9de-bbc3229c8a9e | -19.649799 | -56.677799 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b4313645-5ee2-3988-a7cb-0e3f863f1e8c | -19.6514 | -56.685101 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0c5dc2c8-9632-31dc-aafd-b3fa73d81ae4 | -19.630501 | -56.636101 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f0f79c3e-278a-38ac-bff0-6ca381fa8cb7 | -19.632099 | -56.643501 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5a1b3ed0-a6e7-3161-bac3-754001df1cb9 | -19.633699 | -56.650799 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f0a90088-610d-3094-8fd4-e1e66258406a | -19.6353 | -56.6581 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b78c12b5-dbcb-39a0-bd43-641fd71eaac3 | -19.6416 | -56.687401 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0514d532-9a29-3f5f-a7ce-21652390d142 | -19.6432 | -56.694698 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9b10b855-2503-39db-aba7-7b77aef13add | -19.6448 | -56.702099 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 47f4c44a-8def-32ed-92be-052136f28c55 | -19.620701 | -56.6385 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6d1b6568-fe51-389a-bb2e-3f359871defd | -19.622299 | -56.645901 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3ee8cfcf-189b-3d10-986e-97f63b4f078f | -19.623899 | -56.653198 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 06696201-4e3b-39d1-92ff-6d7e3feefdf2 | -19.6255 | -56.6605 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 08d83970-30fb-30d7-b2ec-033ae4fa91bb | -19.627001 | -56.667801 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 239b030a-91e6-35af-8f2b-92e3f0de4f56 | -19.628599 | -56.675098 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b6fdb191-bbc0-3078-8648-52611e2ce7a1 | -19.630199 | -56.682499 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8cfea59d-4071-3209-a8e8-db6f7322f0c6 | -19.6318 | -56.6898 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1336ad10-5ca9-31af-9072-125c1c183439 | -19.635 | -56.704498 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 77a87f4c-d19e-3960-b15b-37a012eea88f | -19.6366 | -56.7118 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ef8d014a-f56a-3eb9-a5e7-a4646fcedada | -19.638201 | -56.719101 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0a3ccd64-0547-30e3-85f5-e02f46d7865e | -19.612499 | -56.648201 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 79bdff9f-1e7e-3984-9ba9-0e614bf3b228 | -19.6141 | -56.655499 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d6779a5c-c5d5-3d30-9d6a-b2aab1e16ed2 | -19.6157 | -56.6628 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 855c95e5-d96a-3a86-903b-1196861a3a62 | -19.6173 | -56.670101 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f77274e5-2515-3075-b9ef-d72f8c060f79 | -19.6189 | -56.677399 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 88f6c1ea-7943-3b69-a7e0-e9ddcd86e556 | -19.620501 | -56.684799 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f507687e-417e-3fba-b22a-6de9e70d6545 | -19.622101 | -56.692101 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0a6d3819-8c6c-32de-ab8d-4b35c9c5a57f | -19.623699 | -56.699402 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b781c246-1b18-35cc-a5e6-6a8371db7262 | -19.6059 | -56.6651 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8f57cd02-6393-389c-9df2-a9649f08d5eb | -19.6075 | -56.672401 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e65e1b50-1c73-32fb-b1aa-02eb2714f169 | -19.6091 | -56.679699 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7f5a003b-94bf-3999-a14c-8d70a27f6f44 | -19.610701 | -56.687099 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e002bc88-67fa-36c6-a3c2-06b38774bf7b | -19.612301 | -56.694401 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 168b7154-5838-3801-9020-9071cfedd2e4 | -19.613899 | -56.701698 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ea740a6f-f59e-35c3-b401-46ab378f0d8d | -19.615499 | -56.709099 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| def724ab-cabe-3634-bccb-3be737275eae | -19.621799 | -56.7384 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0e6e5e78-8e0e-3249-808a-7f3381b87f27 | -19.6234 | -56.745701 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c64b9907-0284-38cf-b774-80cf9dfc1136 | -19.625 | -56.753101 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 209191d5-2a31-39ff-a0a4-67fbc2b8a1d4 | -19.650499 | -56.8708 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0b2e45c9-dd86-3471-9ae8-331a364028a0 | -19.6521 | -56.878201 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a35d09c8-9d48-3d4c-aae0-94214b34225b | -19.5977 | -56.674801 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f82e44f2-e0f9-3480-9561-bbb02f30bc78 | -19.5993 | -56.682098 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 04cc4291-fea2-3eec-80bd-0bb5264ddb0e | -19.600901 | -56.6894 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0d59a7c8-b8fb-3d70-b13c-7b42baa8d49d | -19.602501 | -56.696701 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f3be59e2-e6c8-3c8a-be1a-9f60045f5d16 | -19.604099 | -56.704102 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b59735d9-fcf4-3b99-970c-047dd10de476 | -19.612101 | -56.7407 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f87bec7c-7868-36cf-872f-d9f15c370478 | -19.6136 | -56.7481 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f54bfecc-6225-31dc-96a7-b894cf82ae4f | -19.6152 | -56.755402 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2d332872-af4d-32c3-bbf6-2034478c78be | -19.640699 | -56.8731 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 47cf2f54-8fc0-3d9b-a57a-95850d5a2c8a | -19.6423 | -56.880501 | 2024-10-26 01:26:25 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 79678b45-a8e8-3047-a403-4b513d73ed4b | -19.5895 | -56.684399 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1e0cb900-9272-3f10-b515-a478e5c9f8f0 | -19.591101 | -56.6917 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e5b5984f-743a-3d34-8cb2-4bd5effd11da | -19.592699 | -56.699001 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4c80d04f-22b0-356e-91d5-d12888596095 | -19.594299 | -56.706402 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4196d591-9afa-3efb-9a79-ef09715afb95 | -19.630899 | -56.875401 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7614eddf-d593-3051-8b49-b2b849304bd7 | -19.6325 | -56.882801 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| edd43cf2-a270-3910-aee2-87efe28b5f20 | -19.581301 | -56.694099 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f0e38f67-e141-396a-8559-9079ae71920d | -19.582899 | -56.701401 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f96ab9e1-4763-3156-9b0c-3264afd69b95 | -19.584499 | -56.708698 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bfc2d38f-2e4d-341b-a591-70c222737f2f | -19.5716 | -56.6964 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 51ae5866-839c-347d-ae95-83016de88536 | -19.614599 | -56.894901 | 2024-10-26 01:26:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e531125f-7a13-3ae7-bcf4-7a36e00179e7 | -19.616199 | -56.902199 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1b343e5c-b93d-393e-aeaf-3f8ea6cb984e | -19.604799 | -56.897202 | 2024-10-26 01:26:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dc314083-a1eb-3930-bea8-92404239fb91 | -19.6064 | -56.904499 | 2024-10-26 01:26:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 080c936c-95d7-3641-9cca-cd9fa2b28b9c | -19.552 | -56.701 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 09972a1b-50c5-3dea-a548-f5a813a7b21b | -19.5536 | -56.708302 | 2024-10-26 01:26:26 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 605cfd4a-23c1-3f99-826f-6e7d48d2fb73 | -19.5375 | -56.6814 | 2024-10-26 01:26:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9ca63811-b662-3427-a893-bb1ed14471b1 | -19.5406 | -56.695999 | 2024-10-26 01:26:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| da83c79e-9ded-3783-9919-b2bc3dce1344 | -19.5422 | -56.7034 | 2024-10-26 01:26:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fe38f7ae-6d00-354f-87ad-8a604484a598 | -19.5438 | -56.710701 | 2024-10-26 01:26:26 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 01ae7d3e-3872-3b54-beee-00cbfa8b0e43 | -19.5277 | -56.683701 | 2024-10-26 01:26:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e974b7a4-d3f4-3635-9bd2-5f5b941038e6 | -19.5292 | -56.691002 | 2024-10-26 01:26:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 66b8ed0a-a42e-308c-8b67-e5fe85772230 | -19.5308 | -56.698299 | 2024-10-26 01:26:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9db4aef3-50e4-35ce-98ca-422bc205038f | -19.5324 | -56.7057 | 2024-10-26 01:26:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bd6a4a5b-c651-3444-b5e3-d1523b17efff | -19.534 | -56.713001 | 2024-10-26 01:26:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a65b88d2-7231-3693-996b-42951bf599ad | -19.521 | -56.700699 | 2024-10-26 01:26:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 488d2324-cd03-3064-91ed-fa45027cc9b0 | -19.4872 | -56.6395 | 2024-10-26 01:26:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 226ca79b-32ea-3588-99b0-bd48a41dfda9 | -19.4888 | -56.646801 | 2024-10-26 01:26:27 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1797c138-4e28-3d35-81f8-6f91ff6e593c | -16.9204 | -57.5291 | 2024-10-26 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| cd579f32-763e-3c50-b4dd-c20ffa3cc530 | -16.9207 | -57.5086 | 2024-10-26 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 0e6c3439-38f4-314b-aac3-eb6df10cf5d7 | -16.94 | -57.5268 | 2024-10-26 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.6 |
| 1b9b89aa-4ed9-3897-b71d-83bf8619d747 | -17.0499 | -53.452 | 2024-10-26 01:26:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 8531b73f-b6f9-3f8d-a2ae-6fd4fad80dba | -17.2186 | -57.2485 | 2024-10-26 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.9 |
| a2579b37-50af-3626-9b19-089649b602d3 | -17.219 | -57.228 | 2024-10-26 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| 9db56a85-c6bf-3873-83c4-93d1d2646a73 | -17.2537 | -57.5108 | 2024-10-26 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.5 |
| d3a9ab21-ee0a-3af1-9b82-c4f859fe2355 | -17.254 | -57.4903 | 2024-10-26 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 469ca1a8-b1a2-3467-8c9d-24ee83ccb7c5 | -18.2722 | -55.987499 | 2024-10-26 01:26:44 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7fd9c84a-9400-3f64-a37f-ca630470371d | -18.2738 | -55.994701 | 2024-10-26 01:26:44 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a7557910-54e5-3bd0-b44c-8bf1d525ff17 | -18.275499 | -56.0019 | 2024-10-26 01:26:44 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a4545fe-8d59-3992-b67d-b95b1773b053 | -17.7868 | -57.3649 | 2024-10-26 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| b866fca1-a67a-3bcd-a882-5b36d4271dd4 | -17.7872 | -57.3443 | 2024-10-26 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 5f1ca0cf-0c46-3959-8df4-2b540e1bb989 | -17.8069 | -57.3419 | 2024-10-26 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.2 |


[Clique aqui para ver as próximas entradas](README16.md)
