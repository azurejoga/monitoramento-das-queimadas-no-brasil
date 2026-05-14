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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f35c4630-1549-38c9-9267-e6f06903f024 | -17.3622 | -42.7029 | 2026-05-14 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 5e99231e-b168-3417-851b-292e986f9937 | -17.383 | -42.6732 | 2026-05-14 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 18f06042-945f-3313-9678-1c24b42bdc4a | -17.3629 | -42.6781 | 2026-05-14 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 116.8 |
| ef75e948-b465-3c78-988c-2fa342ce76f2 | -8.1133 | -44.1668 | 2026-05-14 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 60d17caa-d39e-3c3c-8cc1-b01a958635d6 | -19.2091 | -52.636 | 2026-05-14 00:00:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 09670cf4-f0fb-3632-b489-c314ed86c6aa | -17.3823 | -42.698 | 2026-05-14 00:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 205.0 |
| d8d020b0-4479-331b-91e6-10193cbfefda | -17.3622 | -42.7029 | 2026-05-14 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 194.9 |
| dc0dec12-b4f9-313c-bbb9-afc4b282a67f | -19.2091 | -52.636 | 2026-05-14 00:10:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 7da3fc0c-e9f9-38a2-9e6b-00babcce52f0 | -17.3629 | -42.6781 | 2026-05-14 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 1e535bc8-ebef-3ef7-9b18-aa764edae1a8 | -17.3823 | -42.698 | 2026-05-14 00:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 173.4 |
| a7521b08-c86a-37a0-9dfc-4b0f8fb10633 | -17.383 | -42.6732 | 2026-05-14 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 46f8a785-2827-3e1b-9434-8ce52a7420a9 | -19.2096 | -52.6142 | 2026-05-14 00:10:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 51.1 |
| b38e8637-c61f-3d33-ab5d-da9ce859634b | -17.3629 | -42.6781 | 2026-05-14 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| d748ba10-93de-3b1c-b695-c4e91b78417f | -17.3823 | -42.698 | 2026-05-14 00:20:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 3cad947b-7c8b-3fa6-a7d2-a04bc69af7d9 | -8.113 | -44.19 | 2026-05-14 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 815a8a8b-7d16-3a8d-9edc-c5ffb20f9e4e | -19.2091 | -52.636 | 2026-05-14 00:20:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 914f776f-ca4f-3d59-8639-76c62c00943c | -17.3622 | -42.7029 | 2026-05-14 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 97d70b1a-4105-3cb2-973b-af94614d7ec8 | -17.383 | -42.6732 | 2026-05-14 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 77fa73a4-b039-37ff-b32e-27cc0c1e9aaa | -19.2091 | -52.636 | 2026-05-14 00:30:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c3e34bae-99e4-34e2-b079-421ed834cc0e | -8.113 | -44.19 | 2026-05-14 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 7b399028-dfa0-3f02-aec7-f2fc8f9f8968 | -17.3622 | -42.7029 | 2026-05-14 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 150.5 |
| afc3e321-8cb8-3b2e-9068-339a194eb407 | -17.383 | -42.6732 | 2026-05-14 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a3141534-9649-3aa9-aae9-713fe1e2616f | -17.3629 | -42.6781 | 2026-05-14 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 123642c4-1e2b-345b-bbb2-90f18e5a6fdd | -17.3823 | -42.698 | 2026-05-14 00:30:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 832e6622-2fa0-3f3a-885e-f57590ff7ac6 | -17.3823 | -42.698 | 2026-05-14 00:40:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 2a38ffcd-f899-39d2-9a93-7dafd7e67cdf | -17.3622 | -42.7029 | 2026-05-14 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 68a2eefb-58d1-3770-a5b7-5f95907a79d0 | -17.3629 | -42.6781 | 2026-05-14 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 210ee7d0-7bfa-3ae8-b2a8-fdc055ef7638 | -17.383 | -42.6732 | 2026-05-14 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 2ac3bc06-7668-3bdd-acda-d709d669d1de | -10.3643 | -46.8448 | 2026-05-14 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 619219fa-d01f-3fc9-87d5-34b030d5c0ce | -17.3622 | -42.7029 | 2026-05-14 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a4fa467d-a64f-34e6-b2cd-4c3ab62b55bd | -17.383 | -42.6732 | 2026-05-14 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| d6f43a74-6f30-3984-94aa-b50ee6c8fda9 | -17.3823 | -42.698 | 2026-05-14 00:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 10465a45-c316-3abe-80d7-0033910d33c1 | -17.3629 | -42.6781 | 2026-05-14 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 075a3025-9d71-3100-8479-95fe0b319365 | -17.3629 | -42.6781 | 2026-05-14 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 5d5224d3-f542-30c0-82d9-e1f6fabd6274 | -17.383 | -42.6732 | 2026-05-14 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| ddc823e4-5d37-3952-9fbf-7988e4b62de4 | -17.3622 | -42.7029 | 2026-05-14 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 115.9 |
| f86bf4ad-00c7-35fb-8231-6b542d8494de | -10.3643 | -46.8448 | 2026-05-14 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| c9d81feb-56a4-3d11-915b-59aa4efccb68 | -10.364 | -46.8672 | 2026-05-14 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b324b44b-2a6e-32d8-abb8-e65f5e4beba0 | -17.3823 | -42.698 | 2026-05-14 01:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 103.0 |
| c82e2c5c-2d49-3c63-9b89-a0e9bace6258 | -11.7987 | -57.354401 | 2026-05-14 01:01:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4813849-f6b0-3fe6-b606-2452c219491b | -17.3823 | -42.698 | 2026-05-14 01:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| a114f1b4-cc8c-3eda-8ef6-22fa268f1637 | -17.3629 | -42.6781 | 2026-05-14 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 57726731-3813-327d-9648-0b3951ee3117 | -17.383 | -42.6732 | 2026-05-14 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d84b488a-51bd-3b60-89c1-9a800cffe0cf | -17.3622 | -42.7029 | 2026-05-14 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 4906c554-7ae9-3913-9746-63c0c172f07b | -17.3629 | -42.6781 | 2026-05-14 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c19858d3-099b-3984-9a7e-a7d18b5fb03b | -17.383 | -42.6732 | 2026-05-14 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c2103c61-1797-3546-bb51-7ba574c213f4 | -17.3823 | -42.698 | 2026-05-14 01:20:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| d8a2cf5c-2202-3f87-abc5-6e8c9dd8a71f | -17.3622 | -42.7029 | 2026-05-14 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 071959da-ace3-3f57-b793-5d8f8e1ec8c3 | -17.3823 | -42.698 | 2026-05-14 01:30:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 801205f0-69c4-37e9-b05e-80e1634d1aaf | -17.383 | -42.6732 | 2026-05-14 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 4007e6b2-4b15-3b1e-8eee-16d293320e9b | -17.3622 | -42.7029 | 2026-05-14 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 96cb975f-cd6c-339b-a459-eb7b9e9111c3 | -17.3629 | -42.6781 | 2026-05-14 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| ae891dce-b32c-374f-a290-0aa12ce23991 | -19.2096 | -52.626801 | 2026-05-14 01:31:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ef6d3449-34f9-3637-96f0-111699dc0d51 | -19.212601 | -52.638901 | 2026-05-14 01:31:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6d18fece-d635-3eb4-befb-59191a03211e | -19.219299 | -52.6241 | 2026-05-14 01:31:00 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9ea648b2-3daa-382c-87bd-6d7cda6d9989 | -17.3823 | -42.698 | 2026-05-14 01:40:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 7b740a30-07f4-3790-8e25-e0b538c5e455 | -17.3622 | -42.7029 | 2026-05-14 01:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 33a45cfd-325d-3b5b-a622-d7685e225852 | -17.3629 | -42.6781 | 2026-05-14 01:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 53.6 |
| a5186a71-ec24-39d0-813c-94edb549f11d | -17.3823 | -42.698 | 2026-05-14 01:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2b5a792a-504b-3f91-bbb5-376a24d32889 | -17.3622 | -42.7029 | 2026-05-14 01:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a10ee95e-6df2-30ff-b965-cb2f31e778dd | -17.383 | -42.6732 | 2026-05-14 01:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 60.8 |
| c9b79383-58e0-388d-abca-5eb15b6bba43 | -17.3629 | -42.6781 | 2026-05-14 01:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5d2da2b6-ec53-3335-88bb-61ba47c01b60 | -17.3622 | -42.7029 | 2026-05-14 02:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 1580233c-c1a2-3c9c-a858-ccaa3ba9437f | -17.3823 | -42.698 | 2026-05-14 02:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 216d8c47-a0f9-3d84-95e0-ea546050a95b | -17.3823 | -42.698 | 2026-05-14 02:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 63a6067c-b6bd-3940-9c26-909d9d12f84a | -17.3622 | -42.7029 | 2026-05-14 02:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 487f0bac-c43f-3fc1-9c3a-0d5876252cc3 | -17.3823 | -42.698 | 2026-05-14 02:20:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| edf9f985-f0a2-3cb1-8b68-2769d2b5ef9a | -17.3622 | -42.7029 | 2026-05-14 02:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e3640b9b-27ee-3a55-86b8-5d11cc3ba2e5 | -17.3622 | -42.7029 | 2026-05-14 02:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b1caa255-e8df-3eaa-8cc7-a59c490aff9f | -9.4578 | -40.3392 | 2026-05-14 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.7 |
| e4414455-8da1-385d-9925-c223ccce34cf | -17.3622 | -42.7029 | 2026-05-14 02:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 2ce815a7-cbc9-3d25-a8b0-3f9c6e6b83c2 | -9.4578 | -40.3392 | 2026-05-14 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.9 |
| fd08cac0-c14d-3fb7-9e79-6b9b09ed5e64 | -5.4436 | -36.79174 | 2026-05-14 03:13:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9d429e5-9531-3fff-80c5-3b35d1899e2f | -9.46632 | -40.34198 | 2026-05-14 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 15014de4-06c7-3a5d-bc2a-843de11d112b | -9.45874 | -40.34621 | 2026-05-14 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 8511b8b2-7048-3f54-b9d7-a0f451dd71bd | -9.45982 | -40.34066 | 2026-05-14 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 681aeb94-25db-30c5-9497-2ee1561aaf5d | -9.4609 | -40.33513 | 2026-05-14 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| f0d551eb-9e14-3dcf-92f7-486d7b577b55 | -9.46524 | -40.34753 | 2026-05-14 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 859617ff-720b-3b51-bdb7-0f8ac4c6f223 | -17.37095 | -42.6974 | 2026-05-14 03:17:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| dcba22ec-d815-39b8-88fa-fb7685b05d4d | -17.36443 | -42.69607 | 2026-05-14 03:17:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2a72b478-bb3b-3f31-b1b1-4971f8061e13 | -17.35668 | -42.70013 | 2026-05-14 03:17:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88171d5a-79b8-3bf3-a5d7-324ada4be1e6 | -17.36316 | -42.70167 | 2026-05-14 03:17:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| cbdb0f41-0124-30ff-be6c-f43404c96fe3 | -22.05893 | -41.52441 | 2026-05-14 03:19:00 | NOAA-20 | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 633e8eb3-1814-3c96-9d1e-a32d45e25f2e | -9.4578 | -40.3392 | 2026-05-14 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 148.7 |
| ab83787b-c78b-3871-b805-9d92551e985c | -9.4769 | -40.3365 | 2026-05-14 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 102.7 |
| e14bef83-14cb-380f-950e-139e20dfaca0 | -9.4574 | -40.3641 | 2026-05-14 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 3b10ef21-808a-34d3-90a1-fd07227b06fa | -9.4769 | -40.3365 | 2026-05-14 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 122.0 |
| dbcb4bb0-0a90-372f-8b23-c4f5ac7e5975 | -9.4578 | -40.3392 | 2026-05-14 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 240.1 |
| 427c4ed5-473d-3b8c-8999-20602887e4ab | -9.4578 | -40.3392 | 2026-05-14 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 580.1 |
| 29f35afa-f15e-3c6b-8181-c2474853e6c1 | -9.4574 | -40.3641 | 2026-05-14 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 62ce01e8-0f4a-3780-9110-542eb9afe948 | -9.4582 | -40.3143 | 2026-05-14 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 157.9 |
| 49cfcec3-7565-3138-b13c-e63c2d5f5078 | -9.4769 | -40.3365 | 2026-05-14 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 248.4 |
| d42c38a1-cb08-31bf-8cd1-c5cb3faf666c | -9.4773 | -40.3116 | 2026-05-14 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.5 |
| b183d024-7e91-3f97-b8c6-39cc3b9261f5 | -9.4582 | -40.3143 | 2026-05-14 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 45d30b25-dd1e-3cb1-b81c-a9293c4ef871 | -9.4578 | -40.3392 | 2026-05-14 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 350.2 |
| d747789b-0074-32f2-b900-6adfe8ad1df9 | -9.4773 | -40.3116 | 2026-05-14 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.8 |
| c370837b-b589-352a-bdff-f61d6cd4ecbd | -9.4769 | -40.3365 | 2026-05-14 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 221.8 |
| 9e2ce8aa-fae4-32f4-a760-64e61d57935e | -9.4574 | -40.3641 | 2026-05-14 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 67b6ff83-a62e-3ef8-b365-32781f91f6d8 | -9.4578 | -40.3392 | 2026-05-14 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 190.9 |
| b393da4b-c0d0-306f-b0cc-c8a816d5b3ef | -9.4582 | -40.3143 | 2026-05-14 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.5 |


[Clique aqui para ver as próximas entradas](README2.md)
