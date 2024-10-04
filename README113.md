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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc925df4-2da9-3730-8f56-2b48c7321bfe | -19.32532 | -42.57228 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b75efe37-3f50-3511-b21e-d91cfe45391c | -19.32484 | -42.59393 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 47525a7a-4eb2-3f37-a936-848eaefc64ac | -19.32448 | -42.57951 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0095a531-55fe-3a1f-97eb-354269483b00 | -19.32421 | -42.59981 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 29c2d9f1-5004-389e-aa14-07eeab9fe525 | -19.32366 | -42.58659 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| aa02f69d-aa8c-3b7d-8e25-f1382c5742dc | -19.3229 | -42.59313 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 1557d70a-00cf-37e7-a31e-be7830975d27 | -19.32222 | -42.59907 | 2024-10-04 04:34:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 7d602d30-9582-36ba-bec7-0fdc670c41fe | -19.32221 | -42.57203 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dc8b079a-b9cf-3023-88bc-ada3367a4d16 | -19.32158 | -42.60456 | 2024-10-04 04:34:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 208c563c-873a-3786-be89-0a2dea96f311 | -19.32144 | -42.57922 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 77ec7a81-aa24-31ae-b796-199f7d19c3f3 | -19.32063 | -42.58681 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d36f4ba7-d61d-3748-9918-b12b77df8c16 | -19.32048 | -42.57101 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 94aa6120-8e4f-30b6-9376-467e2915e86c | -19.31991 | -42.59353 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 8da400aa-e50c-3a16-8239-a49d99c47b0f | -19.31964 | -42.57829 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 665989f8-5c9d-3fe5-947c-45ff33f5443c | -19.31928 | -42.59933 | 2024-10-04 04:34:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 4fec9021-68b9-3c3e-937d-a4b9130dabaa | -19.31875 | -42.58599 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| a95d86ab-5854-3f05-a14f-8e39527d1859 | -19.31798 | -42.59266 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| e92ecf75-be2c-3e7f-8f52-5761a83e9563 | -19.3173 | -42.59851 | 2024-10-04 04:34:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b12fc281-1087-3a4a-a929-889d1138e489 | -19.31724 | -42.57197 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6b70c3f4-5298-3a26-a26e-22b1700dbc2e | -19.31669 | -42.60381 | 2024-10-04 04:34:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a51be830-4c59-3e7b-85df-f8c86d40066b | -19.31642 | -42.57965 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 50e2eb5a-6b11-320c-a539-c187e8a84c36 | -19.31566 | -42.58672 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 9291621c-3e36-3673-a735-bfcd38072927 | -19.31544 | -42.57142 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b2d76a3b-af9f-390e-9cce-3b99cd9cf711 | -19.31499 | -42.59301 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 45ef1a04-e530-3dc7-aba9-15995251634c | -19.31454 | -42.57927 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0d5f410f-3ec8-3abc-88ea-b54d9b8e5800 | -19.31375 | -42.5861 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 0f20ead7-9311-3a5c-ab57-0c79210fbadc | -19.31305 | -42.59218 | 2024-10-04 04:34:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 2f004c26-f07f-3a25-bb21-23654fbe0e7b | -19.31223 | -42.57225 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 28a12050-ccd4-3c35-a20f-88899db45622 | -19.3118 | -42.60306 | 2024-10-04 04:34:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8c232f63-812f-3066-97e5-5135d85d34be | -19.31141 | -42.57993 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 37b0b5dc-8105-3ba3-8b55-d29ff4f904d1 | -19.31073 | -42.58631 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| a55383fe-3dc9-3e75-a79e-5c400ee54d74 | -19.30961 | -42.57876 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 72e8a141-315a-37f9-90a3-9f7ae98896af | -19.309 | -42.40734 | 2024-10-04 04:34:00 | NPP-375D | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 21218ad4-8a82-3659-b5be-5faa84b9bd62 | -19.30887 | -42.58526 | 2024-10-04 04:34:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ac63da54-cc42-355a-b391-823176531254 | -19.30818 | -42.5913 | 2024-10-04 04:34:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 626dbb11-bd0b-3ea6-9aae-4420e75b9238 | -19.30332 | -42.59023 | 2024-10-04 04:34:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6ed560de-c522-3fb1-9f7a-af07c2b849ac | -19.2896 | -42.57947 | 2024-10-04 04:34:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 84de19df-e3dc-33e7-b620-c5f7a5f8b3ee | -19.28886 | -42.58598 | 2024-10-04 04:34:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1a34b92a-e853-3f7c-aa60-1459afc6c095 | -19.14013 | -42.5232 | 2024-10-04 04:34:00 | NPP-375D | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8e199d9d-ebf5-3f68-94eb-e19d0b6ba748 | -18.92251 | -42.02108 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a5988bcb-bdfc-3bc4-8c3f-9fc6e06d4dfa | -18.92186 | -42.027 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| cefcfeb6-b213-3e99-8a79-6fc36f893159 | -18.91742 | -42.02066 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 234e50d6-49c3-324d-bf4c-3c34333e4ec9 | -18.91677 | -42.02653 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2dd58481-9aab-362d-85aa-948b21d15bc7 | -18.91608 | -42.03272 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d3f699f8-c08a-3d64-a8bd-e693dec7aa81 | -18.91288 | -42.0152 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 85f76a17-dfd8-309b-b306-3ade6c3bb957 | -18.91233 | -42.02013 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e6fa3a3f-2f5c-3bc4-afbd-5a1aa4da78d1 | -18.91168 | -42.02599 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| aac707d8-30da-38aa-be3a-7b9dc0094da7 | -18.90777 | -42.01484 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f6dec3a0-f1f7-3961-954d-e9c5125c0e56 | -18.90726 | -42.01952 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 9b6240dd-0d82-3655-a059-7a2ab3a92a8a | -18.90661 | -42.02539 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| e862b793-0e14-3e62-ae90-e9c2d55a4931 | -18.90375 | -42.00457 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f3e5047-9dd0-364f-9c2b-f8e29361662f | -18.90339 | -42.00792 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b4504c94-840a-3dc7-a053-4cf715a196b3 | -18.90302 | -42.01124 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e3d926c2-f7d1-36fe-b135-0dba46bfa88c | -18.90268 | -42.0144 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 899f70dd-b8a5-34c3-bba6-c26b0f179c4b | -18.89712 | -42.01816 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 82bdb57b-781b-35c9-9e56-1432ae15f691 | -18.89206 | -42.01742 | 2024-10-04 04:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 86f22f0a-d0ae-3b76-9311-67975eb87224 | -18.61864 | -41.84824 | 2024-10-04 04:34:00 | NPP-375D | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ef35333b-b6d9-376b-8007-8a3eba146604 | -18.6183 | -41.85138 | 2024-10-04 04:34:00 | NPP-375D | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 173f40e9-8ab8-3f17-b9c4-3db7c3e770a4 | -18.55737 | -42.25998 | 2024-10-04 04:34:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c0c55847-2491-391a-92d5-c3ec91a875a3 | -18.55241 | -42.25927 | 2024-10-04 04:34:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c4ac0702-0740-30e2-95a7-56f8c7267eff | -18.54444 | -42.24029 | 2024-10-04 04:34:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6d34cf23-d721-389e-bebd-f8a4f2592faf | -18.5376 | -42.25648 | 2024-10-04 04:34:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 96c100bd-51f1-3235-8da2-244532bed011 | -18.53694 | -42.26244 | 2024-10-04 04:34:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0b4efd21-f1f0-3f68-baad-950494c3d521 | -18.52781 | -42.2538 | 2024-10-04 04:34:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 84ae490b-4afe-3232-832b-eb37618cb376 | -18.52711 | -42.25309 | 2024-10-04 04:34:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 85b48c72-f055-3040-ac18-90d438c0477c | -18.52642 | -42.25891 | 2024-10-04 04:34:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 189c6896-935f-3c38-a3f4-3b4dc50b718f | -18.5211 | -42.22301 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 500168d6-b4ef-3a63-ac4b-3b648bfa3084 | -18.52061 | -42.22235 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8aac34ba-2e89-376c-83cd-06019a809c7a | -18.45454 | -42.27088 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b22c4ec9-fdb6-3f2b-a6d4-fa5e27790e22 | -18.45386 | -42.27691 | 2024-10-04 04:34:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d2019ac8-9a2a-37e3-abac-849253e168b0 | -18.43563 | -42.21462 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 33182b13-e7c6-3f9a-93ac-cc392d397954 | -18.43126 | -42.20851 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 19533ea2-cded-32e1-8d09-25940a56fc02 | -18.43066 | -42.214 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 0d38883e-a9c6-366d-910b-8527226733db | -18.42656 | -42.20753 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 344dd76d-9ff5-3f49-b363-a70979497ad9 | -18.42628 | -42.20789 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 82b657bb-801f-3f29-b22c-d197e03dd197 | -18.42593 | -42.21288 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 9ea67c2b-d40d-342d-90f4-25e839e4da2d | -18.42569 | -42.21331 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| b74752b9-6ccf-3eff-ba51-62238b492692 | -18.42096 | -42.2122 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 95101a6e-0d9f-3bf7-9a45-96082f3f515f | -18.42071 | -42.2126 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 06718157-7852-3e6e-8836-e4b7e3053dba | -18.41029 | -42.21709 | 2024-10-04 04:34:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 80dd16e3-275c-3326-92f5-cf9179fc11ba | -18.40958 | -42.22318 | 2024-10-04 04:34:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 14e411d7-1065-35e5-ba57-17701090a79c | -19.43208 | -43.06652 | 2024-10-04 04:34:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d7294e1-0319-311b-a96c-97f19da6ea2c | -19.28448 | -42.88124 | 2024-10-04 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3cdc5a51-31c3-39d9-9d5e-55c22888c4f2 | -19.28426 | -42.87602 | 2024-10-04 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e1de1add-31a7-3552-8271-2076602c4a50 | -19.2836 | -42.8821 | 2024-10-04 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d08ebaa3-6e8f-3638-ba53-8b1bf2c85259 | -19.27964 | -42.88083 | 2024-10-04 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f6873c4d-5d4c-3f90-921b-b8a47910318b | -19.27943 | -42.87551 | 2024-10-04 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ba761b88-f478-382b-9de0-cfd8da004ec0 | -19.27877 | -42.88163 | 2024-10-04 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 02d219e8-7bd9-398d-8c23-de68f15528d2 | -19.2756 | -42.87357 | 2024-10-04 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 72efc302-166e-3eb3-b11a-6fb30fd00d65 | -19.26662 | -42.86671 | 2024-10-04 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 224bc5e0-c2ac-34a8-a271-09d16a677fc6 | -19.56684 | -42.73126 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2022a035-997f-3c50-ae92-3eef8de1026e | -19.56612 | -42.73774 | 2024-10-04 04:34:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ae79b3c0-a9a6-3549-80fb-ad418edbaa77 | -19.65546 | -42.38761 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ae215c96-3e25-374f-8184-47316f42cf92 | -19.65476 | -42.38771 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 60cf1d53-6cb5-370f-b56b-ab12d22d93c0 | -19.65107 | -42.38153 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 734af68e-2ab7-3342-b212-b7a9da8a6255 | -19.65046 | -42.38699 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e22a17c2-b81f-3521-ade9-a9c43f07fc99 | -19.65034 | -42.3816 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3ae80097-587e-32e5-883e-38a95747bd29 | -19.64976 | -42.38708 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 37598d24-6104-3bd2-97a4-712baf525cab | -19.64545 | -42.38643 | 2024-10-04 04:34:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ee38a1e0-a6a0-3439-a71b-9eb0e0697e79 | -19.62099 | -42.23895 | 2024-10-04 04:34:00 | NPP-375D | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README114.md)
