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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b015156-ed45-35da-9813-c6481a932fcc | -20.39051 | -42.55565 | 2026-09-22 03:47:00 | NPP-375D | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3a3f1480-e856-3bde-b3f0-eb7a7b9bbc06 | -18.80775 | -47.55583 | 2026-09-22 03:47:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6efefc7b-88f6-371f-a22e-a3fe2f53c734 | -18.75756 | -44.98867 | 2026-09-22 03:47:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1292bba8-8840-38db-a684-ddb126fce53f | -11.4404 | -47.3355 | 2026-09-22 03:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| cb711cef-ee4c-325c-919c-dc48bc2826c6 | -10.5906 | -53.9918 | 2026-09-22 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8176a4ac-1a96-3d8e-9cc4-5b6f1981e4a7 | -10.6097 | -53.9697 | 2026-09-22 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b2ceb000-faec-36e5-8a42-6974a5bb4c1b | -11.3255 | -54.0487 | 2026-09-22 03:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 545153e0-7f23-3281-8845-d4d65f48153a | -3.2395 | -53.9618 | 2026-09-22 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 67fadb45-6697-3179-8052-b01274e1cd14 | -18.7472 | -46.93 | 2026-09-22 03:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 71.7 |
| d8bcc9c5-ed53-3053-9cc4-c5f65990ee6d | -11.3066 | -54.0505 | 2026-09-22 03:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 1c2e4518-f4d7-3433-aa3a-6b46f955cf0c | -12.574 | -45.9576 | 2026-09-22 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 7e04c516-6f0a-3cab-844c-623c3bde7a6a | -3.2211 | -53.9623 | 2026-09-22 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e50b6510-12f8-3e2f-8bd6-5f51835a153d | -10.6094 | -53.9902 | 2026-09-22 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.8 |
| ade5aae4-b4c3-3d0f-8c78-a33554b8e1ea | -7.5889 | -57.6757 | 2026-09-22 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a494d2a8-4582-3e02-bd39-16a606cbccfe | -7.5889 | -57.6757 | 2026-09-22 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 4d1786f3-68d7-3fe0-a8e6-5da8ab4f3399 | -18.7472 | -46.93 | 2026-09-22 04:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| abfa1752-89a4-3611-8b77-f3fb1cdf2fbe | -11.1557 | -51.1263 | 2026-09-22 04:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 85bdaeae-34cd-31b1-958c-10d5965485cc | -10.6097 | -53.9697 | 2026-09-22 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 53b95e00-5457-3cb7-ad59-3bd8a999cb1f | -11.156 | -51.1051 | 2026-09-22 04:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 243df5df-760c-3c60-bb0e-ba9c960aebde | -2.8608 | -57.7994 | 2026-09-22 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| a54a0980-aef2-346c-be7c-283d53e05b8c | -10.6094 | -53.9902 | 2026-09-22 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 243.8 |
| fcf1ed51-7e7e-32c4-a818-15784581c341 | -10.5906 | -53.9918 | 2026-09-22 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 2a95c767-e178-3f82-8a80-18e1b2bde7d3 | -11.3255 | -54.0487 | 2026-09-22 04:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3465c100-77b6-322c-a959-ebc182542638 | -10.5908 | -53.9713 | 2026-09-22 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 47ef67fa-2bf0-3db2-abbb-7ecff5d320f2 | -2.16691 | -47.88333 | 2026-09-22 04:00:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c24d476f-9b25-3d43-887f-b2bd8a7a0493 | -2.02672 | -48.78206 | 2026-09-22 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38ddd630-acc1-3160-b288-a16e833f406b | -3.78229 | -40.15659 | 2026-09-22 04:00:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fd802b95-1790-3695-8be1-3d7c8b8d50f6 | -3.3415 | -42.7894 | 2026-09-22 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adf6f9e4-aa85-3c71-ab45-160a0807b9a9 | -3.45159 | -50.61746 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aed512ce-a9ac-3a33-891a-43b8b7c1f167 | -3.34724 | -42.77961 | 2026-09-22 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 983d7989-0954-331a-9e08-e3c048812d6e | -1.38648 | -49.32981 | 2026-09-22 04:00:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 72f4c55f-b42f-321f-81c0-e22b2c312d26 | -3.69272 | -42.95779 | 2026-09-22 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd63ddd9-bdca-3d6e-becf-f3997d8f3ce6 | -4.49273 | -43.78903 | 2026-09-22 04:00:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9da57a7a-8ce8-3e23-a6b5-9148ccc2aa59 | -4.17947 | -49.41158 | 2026-09-22 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3e78598-5492-3469-92ff-a392b91c26d3 | -2.02061 | -48.78099 | 2026-09-22 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a77a8c67-3cfb-33fd-a020-ac498133ae63 | -3.34208 | -42.78592 | 2026-09-22 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6136e047-307f-3284-bdec-032b8259f15c | -3.06109 | -40.10802 | 2026-09-22 04:00:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0a855c4e-71aa-31b1-88a2-270bf44cd817 | -2.17165 | -48.3237 | 2026-09-22 04:00:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d3ea088b-5792-3aa3-ad42-cc2f1842d4b1 | -3.38268 | -50.44204 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4bbb9fb-4aa4-388a-91f4-f558afe6d082 | -4.6555 | -42.09616 | 2026-09-22 04:00:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d51953dc-1501-3553-ad12-82f94232763d | -1.38439 | -49.33176 | 2026-09-22 04:00:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb4e53a7-d4e7-366f-9db0-d09e7d7a8acb | -3.45466 | -50.59998 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f521288e-46b3-3b54-a011-915ea722df2f | -3.68869 | -42.95714 | 2026-09-22 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 97621d43-39ee-3019-8c34-1a84d46bcfe2 | -3.12329 | -51.61024 | 2026-09-22 04:00:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b2594e02-9a4a-3728-9a3c-f5d10e5cfd49 | -3.68408 | -42.96001 | 2026-09-22 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 404ac991-9f37-38cb-83d9-208ea3b59c54 | -3.43928 | -50.60907 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b1423e8-c026-3f80-8cbf-3a8ad6fe62b4 | -4.22319 | -48.61988 | 2026-09-22 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4ff594bb-6024-31c4-b777-49bcaf7704a0 | -5.01108 | -38.02324 | 2026-09-22 04:00:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 587b99d4-b18c-3d2b-a05b-28724a4fe39d | -3.36071 | -50.7673 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04bb5f13-80b5-3616-bb9a-0b3759a122f8 | -2.43837 | -46.01896 | 2026-09-22 04:00:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb1d3d64-8404-32f3-b274-730b3b7370a5 | -4.68222 | -40.14509 | 2026-09-22 04:00:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0189fabf-1347-3e73-a809-08885c8860d5 | -1.77864 | -47.10838 | 2026-09-22 04:00:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43ef358a-dbb9-3720-9035-f346602374e5 | -3.44208 | -50.61541 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f059d4b-303b-30dc-958b-9fd24d3b157a | -2.02107 | -48.77809 | 2026-09-22 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a6abbe8-20be-39d7-b336-060e3059801b | -3.83228 | -40.1103 | 2026-09-22 04:00:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 17312959-573c-35ff-99a0-f9593c9efdc9 | -3.68523 | -42.95297 | 2026-09-22 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 753f18f5-31aa-326e-b844-cc55403d0eea | -2.82511 | -46.70784 | 2026-09-22 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e62eee3-c7d5-3148-83a2-0617b6b92098 | -1.74585 | -47.13622 | 2026-09-22 04:00:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fcb9ca2b-ab54-342d-b530-27f2339e4657 | -4.30382 | -49.12717 | 2026-09-22 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b52de8e-e18c-309a-b5ef-df5a17d27363 | -4.10874 | -39.50437 | 2026-09-22 04:00:00 | NOAA-20 | GENERAL SAMPAIO | CEARÁ | Brasil | 2304608 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ce7c55f-fa39-328b-b708-3a9f610fd054 | -4.95721 | -45.15816 | 2026-09-22 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8633858e-a3fe-3dee-b8bb-3f6a2ddaecdf | -3.97627 | -40.89986 | 2026-09-22 04:00:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a5e59cb3-13dd-3dcb-b063-fc3553a8126b | -3.44702 | -50.60427 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e28bd73-1664-38fe-9488-9398dcef6eab | -3.44106 | -50.62149 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9b86397f-f1cf-3454-a566-47e246b548b3 | -3.84748 | -40.60135 | 2026-09-22 04:00:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73b3de1f-3325-3986-a4e9-89eb6221209b | -4.68159 | -40.14899 | 2026-09-22 04:00:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c87ca0c-9268-3541-a78b-9a04264cf38a | -5.2078 | -39.41098 | 2026-09-22 04:00:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f291fda4-660a-3c6a-b695-49e14de8975f | -3.69214 | -42.96132 | 2026-09-22 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e884547f-b935-30db-af73-b75ada95679a | -3.44492 | -50.61623 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a6c8c83-00f6-3331-9f41-06dd3ac68d1e | -3.35965 | -50.77342 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0628765c-4712-347b-98d8-1b579168fe5f | -5.62961 | -40.87421 | 2026-09-22 04:00:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43d35313-197b-3ed4-9f27-bead529704d8 | -3.15881 | -48.08292 | 2026-09-22 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3542a53-e04c-3401-b977-662b84a72bfd | -2.16631 | -47.88995 | 2026-09-22 04:00:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4336d4a7-61b4-30a5-b3cb-7dddde57e7a0 | -5.21114 | -39.41151 | 2026-09-22 04:00:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b045fcd5-92a0-3d71-93e0-d30b40ea73d6 | -4.65325 | -42.08642 | 2026-09-22 04:00:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 301ce035-4d6a-3c2f-9cb6-c8a9d94b53f7 | -3.446 | -50.61006 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2f2cc1b-1f04-3d90-91ad-eca172d54780 | -3.1595 | -48.07888 | 2026-09-22 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46d26390-2484-3d39-8bb1-14e150185f30 | -5.42279 | -36.75965 | 2026-09-22 04:00:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b467771f-4f6f-37e4-97c8-d487f5be9bd0 | -4.66079 | -42.08763 | 2026-09-22 04:00:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2683d7bf-c07e-346f-972e-8ab04d953f32 | -1.74526 | -47.13985 | 2026-09-22 04:00:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f43e7e63-e17c-3fad-be5d-7e2b135bd4f3 | -2.17236 | -48.31937 | 2026-09-22 04:00:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 78f49ebd-82c7-3378-b858-67d8cf77c496 | -2.53804 | -48.16127 | 2026-09-22 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5d96ffb-d7e0-38f4-a1bb-303444cb821d | -3.37719 | -50.40886 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6f90d4f-7bc3-30f9-9a3a-3d88558b83ba | -4.95801 | -45.15337 | 2026-09-22 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4792b05d-615a-3652-b833-29f7b6c6adf4 | -2.82457 | -46.71106 | 2026-09-22 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c0bb6f6-3e52-3c64-ac26-07cb3649bbf3 | -3.86794 | -51.19599 | 2026-09-22 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e4ea2ea-1c96-3c36-ab54-2d9e0c4b3966 | -4.68504 | -40.14942 | 2026-09-22 04:00:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a7243175-2928-3cd6-b5e4-25243b757f96 | -2.16559 | -47.89142 | 2026-09-22 04:00:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed74da7b-bdc4-3dec-a103-14e4c39b19ca | -3.85766 | -44.69928 | 2026-09-22 04:00:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 243ec695-ac92-374e-8622-334238a5f978 | -5.31073 | -39.11008 | 2026-09-22 04:00:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1bb614ca-1d43-3d89-9a15-83cff44bfd70 | -4.002 | -38.98537 | 2026-09-22 04:00:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d22fa919-ef7d-3bd7-910a-7e5b75fe487e | -4.83648 | -45.99174 | 2026-09-22 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b31f940-161c-3e30-ace1-6c741369ae0d | -0.93506 | -47.5554 | 2026-09-22 04:00:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 095144c3-320d-3900-ba46-e50578460f06 | -1.38524 | -49.32654 | 2026-09-22 04:00:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fa36ad0-2290-3bed-b5a6-d85d42c0daa1 | -4.22393 | -48.61566 | 2026-09-22 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c8159298-db97-3be0-ac1d-d3226ff6e99f | -3.34008 | -42.78872 | 2026-09-22 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c41018ba-595a-36dd-a6a2-e774e64d8e15 | -4.64949 | -42.08581 | 2026-09-22 04:00:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6bea7443-ea0c-3c1a-bfeb-9643c020ecd5 | -4.18561 | -49.41274 | 2026-09-22 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 844d5993-8ded-3794-9dcb-d1c1266efdc6 | -2.167 | -47.88591 | 2026-09-22 04:00:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09bf399a-00c5-3d8e-b5f5-c00e98118747 | -1.7785 | -47.10889 | 2026-09-22 04:00:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
