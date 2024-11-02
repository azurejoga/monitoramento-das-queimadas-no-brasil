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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a34629f3-ddfa-319d-8870-f4448ced89fa | -3.22469 | -44.41673 | 2024-11-02 04:10:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f5cf55a-b705-3e1f-894b-ada3bde9b582 | -3.2241 | -44.42046 | 2024-11-02 04:10:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7bcb1857-dcf0-3321-b7e7-162d03cf785c | -3.22127 | -44.41618 | 2024-11-02 04:10:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc9a656c-44a1-3352-8b23-2cedf5bcc438 | -3.22067 | -44.41991 | 2024-11-02 04:10:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5931ca11-711f-3b9a-91dc-42ce935ed9b5 | -3.1426 | -44.97854 | 2024-11-02 04:10:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ff8dd24-956d-39f9-b46f-6df26126bb8e | -3.1091 | -45.09837 | 2024-11-02 04:10:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a77cb2f-da70-3819-89cd-055bfed66dd6 | -3.07448 | -45.13352 | 2024-11-02 04:10:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 35.7 |
| f8071470-0ad4-3e21-85b9-9b01a7878347 | -3.07385 | -45.13749 | 2024-11-02 04:10:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1793ab81-f94a-3904-a79f-7774d90a35bb | -2.98269 | -44.39439 | 2024-11-02 04:10:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fdce6b1-ea3b-3fdd-af5a-50f83b7f4f53 | -2.98016 | -45.40931 | 2024-11-02 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7278d260-006b-3c4f-80d4-5eed71f5f99d | -2.64468 | -45.77676 | 2024-11-02 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33907765-a763-367d-84bf-1a5f4e0f579b | -2.6417 | -45.77188 | 2024-11-02 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee22ee22-e832-35b3-acf3-abfa29bd9732 | -2.64101 | -45.77617 | 2024-11-02 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64acc00b-1673-3841-bca5-a6c3b52a1324 | -2.61499 | -45.40201 | 2024-11-02 04:10:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c50a584e-3c83-321a-9e81-9b0932ff0b72 | -2.61139 | -45.40143 | 2024-11-02 04:10:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6eb4907-fcd2-3597-97ba-06b65e36deed | -2.40497 | -45.12796 | 2024-11-02 04:10:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4748f93a-4dc4-3617-99da-a6c43a9ade24 | -1.80094 | -45.90566 | 2024-11-02 04:10:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb4ca312-5447-3d07-bad0-c949e6edca73 | -2.07923 | -47.13127 | 2024-11-02 04:10:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94df72f2-a3a2-3e33-b5dd-96964c0f7fa5 | -2.07866 | -47.13477 | 2024-11-02 04:10:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 869a3f68-6e1d-30cb-ac8e-25dc0d40bd92 | -2.07738 | -47.13422 | 2024-11-02 04:10:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd141ea2-c9e0-386d-a637-1fe6c92ec5af | -1.94318 | -47.0378 | 2024-11-02 04:10:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33603654-9249-351a-8afa-dbd6c56f25fa | -2.15876 | -46.38745 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fcbc78c0-ac37-3261-b267-918664449de0 | -2.15802 | -46.39215 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78399f74-b1d5-305a-a6d1-3de119c2c321 | -2.15494 | -46.38684 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffc2c2c5-0e52-353f-a846-b9d35b1cc3b9 | -2.13083 | -46.66438 | 2024-11-02 04:10:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaaab5a8-0b5c-3193-a8db-f45a8c542f75 | -2.12693 | -46.66377 | 2024-11-02 04:10:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4fe5d7c-ce9d-3e22-8d21-38b1b45492ae | -2.08153 | -46.33909 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0781f919-6823-3e05-ad20-5fe69172cd33 | -2.07664 | -46.50601 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c53e610d-1f47-3497-ab33-94b247378a80 | -2.01504 | -46.83467 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0093028-3073-3430-9212-cae273c504e7 | -2.0122 | -46.83241 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7e7089ad-96ba-3df2-937e-ad3480cef8a7 | -2.01193 | -46.82898 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68e36cbd-fb84-3553-9286-c4b0cdf9abb0 | -2.0111 | -46.83404 | 2024-11-02 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87653231-83cb-374b-b0a8-b6d998d5905c | -2.01053 | -46.4396 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fee68619-0576-3963-b8ff-acb50e697ba2 | -2.00989 | -46.89102 | 2024-11-02 04:10:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa1e92e3-576a-3df3-a8e1-d012902230fc | -2.00744 | -46.88885 | 2024-11-02 04:10:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2f65237-331b-3f13-b467-fda5a0fd8966 | -2.00594 | -46.59233 | 2024-11-02 04:10:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7e2e96a-c4dc-3dd2-bcf7-0822b463864e | -2.00584 | -46.89909 | 2024-11-02 04:10:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fddfd972-5c82-303a-9f6b-eb667093cb45 | -2.00426 | -46.9006 | 2024-11-02 04:10:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38ee1e8c-f60a-3b42-be68-349b276b1d3a | -2.00205 | -46.59173 | 2024-11-02 04:10:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c61e04c9-a1c9-382b-8ee7-8dbf3d6ea3bd | -1.99284 | -46.40256 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 548c9723-1873-3d96-bcd3-fb8d0177e4cd | -1.97729 | -46.43745 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a4ad164-da6a-3890-aa54-5c0e8db7e9a7 | -1.97125 | -46.43832 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97ecd396-3923-37c4-99b8-14b9a8b7986e | -1.96959 | -46.43621 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c487eb76-ddd0-36aa-a605-55f4f6e85b7f | -1.96818 | -46.43292 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34e79181-7c64-3ca2-a8ce-01841edcb110 | -1.9674 | -46.4377 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85b61aa7-0ab5-397f-9b74-2bfb694ccb23 | -1.96649 | -46.4308 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69f3bd4a-971d-317d-8aa7-26f3386e9add | -1.96574 | -46.43559 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5f41c18-c575-3871-8163-1158bd5fcf9c | -1.96512 | -46.42752 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 357916df-beca-33d1-b25f-2f8410145e17 | -1.96433 | -46.43231 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 513baee0-f788-3b39-8ab9-2965bd4affa8 | -1.96264 | -46.43018 | 2024-11-02 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80144296-e970-3980-b0d1-1bb8c0edb73c | -1.46679 | -46.72501 | 2024-11-02 04:10:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| f9fd64ed-3148-3846-9610-a927d9849b51 | -1.46364 | -46.71932 | 2024-11-02 04:10:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 04ee5133-5f64-3b7a-8eaa-1faa97ee712a | -1.46284 | -46.72437 | 2024-11-02 04:10:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 3edcb6cd-ed05-3b72-93cf-605bf44e011f | -1.45969 | -46.71867 | 2024-11-02 04:10:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3b5e7599-c2e2-38a0-8da3-d4abc73ee462 | -1.4589 | -46.72372 | 2024-11-02 04:10:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 86c009cf-5a41-35de-9e6c-347d8bbfa43c | -1.21836 | -46.51797 | 2024-11-02 04:10:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edc68c6a-dab7-342e-9eb9-2b3f65f19b54 | -1.21756 | -46.52291 | 2024-11-02 04:10:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 040cbff3-3c1d-3e1c-9941-e7e85f77828d | -2.85947 | -46.65783 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f65317e0-ccff-38c8-baab-c3ab0bc2d505 | -2.82177 | -46.62228 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 45f02b0d-49f4-3818-a7f7-a56387a7aa32 | -2.82099 | -46.62705 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 819bff47-8303-388f-856a-c6bff3160f81 | -2.81792 | -46.62165 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5583c6e5-3a4e-34bc-8fa3-066870c29159 | -2.80017 | -46.63358 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 976162eb-04ca-337e-8af9-3b24cd18554e | -2.71536 | -46.68139 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82380952-da86-36fa-883a-ae6b318ed0d3 | -2.71149 | -46.68077 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05731dd1-682c-3802-9c39-5ade97d5340e | -2.70834 | -46.70011 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b15d8085-44fc-3661-8fdd-4a9c195a9c28 | -2.70755 | -46.70497 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afb3c4ed-9925-3202-827b-37f15b617526 | -2.68603 | -46.75933 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 967fe28a-48b7-3b72-9c21-6f1d132719a7 | -2.6841 | -46.75104 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00030464-2134-3f6e-b53d-cd89edc2a003 | -2.6833 | -46.75593 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf6c6c05-ca1f-3b5b-a8e0-fefc8be92f22 | -2.68291 | -46.75378 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3ef87b59-b83f-3a2d-bd8a-a8706e4c797c | -2.68214 | -46.75867 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ca83620-d0d8-3425-a8b7-2c2a65bba3cb | -2.68022 | -46.75039 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a51afd3a-dd96-3d37-bfe5-7b45ad5c8b78 | -2.67979 | -46.74822 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80e37e36-864c-30d2-9a23-b93eef901d3b | -2.67942 | -46.75528 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57523b22-5469-3bc5-bc5c-2bef22d75cfd | -2.67902 | -46.75313 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b64eea53-79c5-3782-acf3-8d3ca46414a1 | -2.67795 | -46.73997 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c440cca5-85bd-3270-9070-6256dc134932 | -2.67745 | -46.7378 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9863a870-0742-342e-836e-8fbc0b576e15 | -2.67714 | -46.74487 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 27d1547e-eaba-3cff-a70c-886faa59e0e9 | -2.67668 | -46.74269 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c0a06a6-7095-30fc-99cb-217a2f909e37 | -2.67634 | -46.74977 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 87f295e8-253b-34fa-b0e9-90f5dd5ab522 | -2.67591 | -46.7476 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c04a13f0-55a0-321a-add1-df5d5e258d66 | -2.67513 | -46.75251 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 912b0933-9f52-3c79-9a59-d1ddcd7e4827 | -2.67509 | -46.7275 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31ce269d-96b6-3741-a6ee-388930bb882b | -2.67486 | -46.73452 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebb1cded-784b-39a2-a9e3-d4f8045e3fe1 | -2.67432 | -46.73235 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59921338-d71e-35db-966b-f5ecfa7dba8b | -2.67406 | -46.73938 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 731b14f4-cc67-32ad-bbfb-8495e68a44d0 | -2.67356 | -46.73721 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36f2d632-a1f0-3452-af92-8a0a01a9a24e | -2.67326 | -46.74426 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cff28e59-c5f4-3622-ac93-bfec100960a6 | -2.67279 | -46.74209 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27999ecf-7968-3b13-9d26-8140b98bc7eb | -2.67044 | -46.73174 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 731a0225-bfc6-358a-80fb-57aeb1d16d60 | -2.6627 | -46.75554 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 101c266b-906a-309b-93ec-398c784c81d4 | -2.65881 | -46.75492 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39429ee5-2b0e-34d5-bda9-127069ece249 | -2.57137 | -47.30699 | 2024-11-02 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8e8b4c67-91f5-39ce-b0a6-c9b69abf1331 | -2.57081 | -47.31052 | 2024-11-02 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7754db4f-e26d-37c4-894f-97941f0d5d93 | -2.5679 | -47.30281 | 2024-11-02 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6874c58e-e0ca-3d7a-a324-dbea01178c49 | -2.56734 | -47.30636 | 2024-11-02 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6a3ab86-458c-3473-a525-b79ea1f38566 | -2.56677 | -47.30991 | 2024-11-02 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2970ddb0-4fda-3696-b1e3-12072cd5970f | -2.5338 | -46.93569 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb80081d-5e27-3bb0-81c7-efe214273005 | -2.52986 | -46.93503 | 2024-11-02 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c4ce311-9c43-3d38-a62e-095f9303102b | -2.52697 | -47.30003 | 2024-11-02 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README30.md)
