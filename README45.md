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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d440eaa-88ca-36be-8593-0be3670a35ed | -4.81509 | -49.39155 | 2024-10-16 04:29:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0bb46962-07bb-37a7-8ffb-f6d68beed3d1 | -4.44502 | -49.03248 | 2024-10-16 04:29:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b80dc2b8-1d60-35d4-b57e-26acba8c08eb | -4.44445 | -49.02961 | 2024-10-16 04:29:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eed5190a-e266-3bf8-81be-44026e305550 | -4.15828 | -49.00331 | 2024-10-16 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86041e2a-69dd-3c43-aac1-c1281fa61294 | -4.11733 | -49.23746 | 2024-10-16 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60b2fa8a-65d7-3b4f-ac4f-7df47fc147b6 | -4.57378 | -48.01412 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43cb7b40-989c-3117-9bd8-1fb1b7730a1a | -4.57323 | -48.01758 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7bb0f15-472e-38c0-84c7-f0e1fd044367 | -4.56992 | -48.01707 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 680c7a38-a0e9-3d59-bb26-048dafe6ffff | -4.56606 | -48.02001 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34b0c3c2-3a14-382e-b2b0-7ac801246263 | -4.56552 | -48.02348 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8aa7820-8129-3b37-acec-8f8fa8d6b292 | -4.46896 | -48.11821 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1874b090-b179-33b7-af2f-4e2396913162 | -4.46841 | -48.12169 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac42cfb2-b423-3287-8926-861516114ee1 | -4.36443 | -48.21962 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82a31f09-a40f-31da-a20d-99af7c7482c4 | -4.36208 | -48.49242 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68174d4f-4583-39f8-abc7-8f683f2a7d27 | -4.36166 | -48.21561 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7a18c5e-7777-3459-9113-af9a2c335990 | -4.35929 | -48.48837 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54f086a8-a3c8-3117-8d15-214e9aed4cfb | -4.35874 | -48.49189 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fbd2b2c-f914-3609-8a64-566fc1282fea | -4.35818 | -48.49541 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24c10f2b-bd88-3b97-adcd-7b528df2da7d | -4.35595 | -48.48784 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5a3fbd8-eaa9-3083-b327-791540f7f574 | -4.35539 | -48.49136 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7589ee2-49f0-318b-9aec-1b5fb1dd1c9d | -4.35484 | -48.49487 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d4c77f0-4df6-3f00-8df2-2f9b9c849431 | -4.35177 | -48.73074 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbbc208b-e228-3e47-9e98-25404da22353 | -4.33068 | -48.62521 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0994d670-71d1-32f2-a1f3-fe782a2d2bf6 | -4.32733 | -48.62468 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07f101b7-e7c2-39db-83fd-c4e2686eec8f | -4.32677 | -48.62824 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eae1d00-5e0e-3cc4-b689-e89ab0f55e3f | -4.3262 | -48.6318 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a031a13-9893-3619-b97e-0468b010729d | -4.32398 | -48.62416 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afc7cd9e-269a-3f73-aa37-bef060ac4c1d | -4.32341 | -48.62772 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5bfbcb9-4fb4-3dbf-bc79-bb46ea8dcf63 | -4.32285 | -48.63127 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09f97c99-4669-3d62-aa2b-f21e9db04efa | -4.31893 | -48.63432 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eade6889-3a18-3e5b-88a8-af63c6244731 | -4.31131 | -47.75982 | 2024-10-16 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e8e60bb6-68c8-3026-9400-112a5fa8f870 | -4.27893 | -48.22399 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05383bc4-7711-3881-a0c1-983e741bf5fd | -4.27561 | -48.22347 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e007b685-d490-3362-adf5-8d51d1e30643 | -4.27228 | -48.22295 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d608ff39-f2ff-30f6-96dc-0eaf4a603c94 | -4.08626 | -48.49962 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 81e5fe46-4ee3-3253-98df-4a314ed3a49f | -4.0857 | -48.50316 | 2024-10-16 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ed0cf0bb-8710-388c-92e5-e69d96b12bc9 | -3.80056 | -47.78923 | 2024-10-16 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca170eab-9ce2-3cf9-a364-719627a9feca | -3.80002 | -47.79268 | 2024-10-16 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89231d69-eb08-3737-8148-a8e60543e5bb | -3.79947 | -47.79613 | 2024-10-16 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c13cda8-f827-3d1f-82e1-e3738afd98d5 | -3.79671 | -47.79216 | 2024-10-16 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72d0884d-47c9-3f73-a009-247e2fb1ef6c | -3.86831 | -49.08192 | 2024-10-16 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2185de5-4184-3888-8ebb-1b964de637dd | -5.66735 | -48.68341 | 2024-10-16 04:29:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b37d7186-b4bc-3669-a222-c0dc15f00659 | -5.40433 | -49.19781 | 2024-10-16 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f014f54f-d150-3b45-8465-8b805e32af93 | -5.39013 | -48.39593 | 2024-10-16 04:29:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 235e126f-7cda-3874-8487-d4b9e8113af1 | -5.38388 | -48.94792 | 2024-10-16 04:29:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 69624e3e-877b-345d-b71f-ee11989d6750 | -5.25777 | -48.07218 | 2024-10-16 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa7aff47-f639-38b5-af1a-dfa93ed6242d | -5.25722 | -48.07564 | 2024-10-16 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2c7036e-7685-319b-be6e-ae47389f8077 | -5.22771 | -47.96114 | 2024-10-16 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b718461-3c32-33cf-8567-dfe3fd514dca | -5.2244 | -47.96061 | 2024-10-16 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 92c78c93-a2f0-333d-b0a0-bec343f4d402 | -5.22164 | -47.95664 | 2024-10-16 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ec58a1d5-f5e3-3b9e-85fa-477d721b3f67 | -5.2211 | -47.96009 | 2024-10-16 04:29:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e8b300a-1e1c-3798-ada0-2f6f9a235e53 | -0.77181 | -48.71021 | 2024-10-16 04:29:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43e430cc-fd2f-3575-849a-b89da421b7ac | -0.77123 | -48.71396 | 2024-10-16 04:29:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 360a2a9f-d099-32f1-90d3-2bde22eccf93 | -0.77013 | -48.69841 | 2024-10-16 04:29:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f56cb7b-99b5-321b-93ec-545a91d2dc3f | -0.76954 | -48.70216 | 2024-10-16 04:29:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61b77486-252d-39c8-8fd8-aaf073d632a5 | -0.76896 | -48.70591 | 2024-10-16 04:29:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cab0bb93-07ea-3d31-a444-bf36533c6884 | -0.76728 | -48.69411 | 2024-10-16 04:29:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2c13801-8a89-3fa4-bc0e-d7fd6efe8a62 | -0.7661 | -48.70162 | 2024-10-16 04:29:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8ebaa4c4-17cb-31fd-923c-9b7f9e0b5c6f | -0.75528 | -48.68071 | 2024-10-16 04:29:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43bf3c2c-be4f-388f-936b-2f45ba4ac1f1 | -0.75469 | -48.68446 | 2024-10-16 04:29:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df27387f-34db-38ea-80ba-612d80b2ac1e | -2.05355 | -49.49637 | 2024-10-16 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d06c8c2f-890d-3da4-a4e3-28e7dfef5104 | -1.14518 | -49.1932 | 2024-10-16 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4eba192-1afa-3137-a348-8d6808e316fc | -1.14228 | -49.18876 | 2024-10-16 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3d2b7de-d0bb-3a5b-a21b-b62af6b80c69 | -1.14167 | -49.19265 | 2024-10-16 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b374d1fa-c28f-3949-ab8f-9c9721b65411 | -1.13832 | -49.16823 | 2024-10-16 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f341557b-cc96-318f-b5a6-958820eda2e4 | -1.13771 | -49.17211 | 2024-10-16 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1affd784-77d5-346f-bfd3-8bc83d232b83 | -1.1371 | -49.17599 | 2024-10-16 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ed11446-90c3-3593-9c89-c67435e9ba69 | -1.13543 | -49.1638 | 2024-10-16 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 803df103-50da-3bf3-8403-68fdd8b03e70 | -1.05124 | -48.84889 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84fccefb-4647-3a61-a2f8-2cd2e66a5e70 | -0.86303 | -48.70849 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79dbffe8-98bf-3a63-8007-1e02655806cd | -0.86244 | -48.71224 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1ec649a-a778-3bc4-8cd3-4ccefe551afa | -0.86185 | -48.71599 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c03ee287-77b0-3d35-9dd7-b903a7db50b2 | -0.86126 | -48.71974 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 949ec31b-fdc8-3d9c-a24c-0b451c2d2a1c | -2.2065 | -48.86008 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56e2e8f8-edeb-3a59-89f8-166acbe018f0 | -3.37331 | -50.34434 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c5fa34e-c837-3d3f-a1ed-001206f8b01a | -3.3418 | -49.15128 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36599a88-20ef-32eb-959f-d3dd21bd6225 | -3.33509 | -50.13694 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a4cbf01-0c96-31a1-b39c-227820676604 | -3.30323 | -49.10834 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af1cf0e1-8c13-3052-b755-e9ed4edd5468 | -3.3004 | -49.10408 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60dea081-7656-3684-b4ec-4d9f621edf94 | -3.29931 | -49.08884 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0f11108-73df-3f4f-ae29-8284e3b2ef8d | -3.29756 | -49.09986 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a1962b0-d0f4-3103-9f10-bd3f0e87220e | -3.18995 | -50.31755 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bafd48b-e423-3092-9834-3817ff37faf4 | -3.16989 | -50.46527 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f993b53d-cad2-353a-8bd9-527a0062e955 | -3.16921 | -50.46951 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e88ec2c1-faeb-3524-b27e-7ac00dacbdc3 | -3.16557 | -50.46893 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 881fff0c-e832-3074-8751-f73efe421090 | -2.85532 | -49.37101 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1bdcb4-24fe-39d8-a49c-f0a78547fd51 | -2.85245 | -49.36665 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b8eb872-a570-3d8c-94d2-ad80d8b1618a | -2.85185 | -49.37046 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93c09b9c-ea7a-3b76-a293-8d3acd045aad | -2.83828 | -49.86873 | 2024-10-16 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5801f4d9-72d4-35db-b5c8-c22795fbfa0b | -2.83687 | -49.53389 | 2024-10-16 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fbdc9bb-5e9f-30a9-9683-9332ce3dfb85 | -2.83626 | -49.53778 | 2024-10-16 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17159d45-86c9-3759-964a-359ba0ef3467 | -2.83398 | -49.52946 | 2024-10-16 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c355033-27f3-3d84-bc1f-f8360a385715 | -2.83337 | -49.53335 | 2024-10-16 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46e48008-bd3a-385a-b0e1-9f2987186157 | -2.83276 | -49.53724 | 2024-10-16 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 420155c0-57d9-3cc0-b413-4f4f8a99effd | -2.82393 | -49.54778 | 2024-10-16 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed0f42bf-b217-3e94-b1f1-c22166b82d0a | -2.82332 | -49.55167 | 2024-10-16 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb36ae9e-eb75-399f-a3ac-3e83ea89c105 | -2.81279 | -49.8688 | 2024-10-16 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc6c52e5-5654-3bf9-a0d0-902f7195e7c4 | -2.76819 | -49.51511 | 2024-10-16 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fe61e92-c751-3416-8c7a-72cd86d651f4 | -2.63021 | -50.13497 | 2024-10-16 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f0dcc45-73f7-32ed-9a92-4cab3bf0dd5c | -2.60131 | -49.49067 | 2024-10-16 04:29:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README46.md)
