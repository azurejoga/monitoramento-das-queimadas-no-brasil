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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bbcd522-5a3e-3e91-b1ca-b628e435a521 | -1.09174 | -53.64477 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bab463a-28df-3ce1-aef2-71512332e5c5 | -4.69515 | -42.39923 | 2024-12-01 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d5c7eb78-3c4a-3394-8e9d-bc97dbf7d575 | -2.81958 | -46.84704 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52d5b3f7-064f-3220-b01e-0b2a7f282495 | -2.74647 | -51.75661 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f45643d3-4a28-3978-b5b8-d0738cf24c80 | -3.88751 | -47.06388 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54483638-bc8e-3370-95b1-3094e6add92e | -1.09674 | -53.64944 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54e5d5bc-e9ab-35eb-9f78-b9629e7848ef | -2.60155 | -46.57371 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afa83a38-cda5-3fe2-a195-8f298b2f0be6 | -3.26014 | -50.05424 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3afd9330-f2bc-3154-a0d1-65c57f22e5f9 | -3.409 | -51.97444 | 2024-12-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f277635-75e1-3d5d-930b-fdb06404673a | -2.4482 | -53.6229 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b39e54b9-a6e3-312d-8e74-df9ffd73fdbd | -1.21234 | -51.73847 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f374a45-070a-3966-b91e-9ed2816b584f | -3.13647 | -45.98476 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efb47159-d206-3f8c-a266-c14c372c22ed | -2.03491 | -48.73467 | 2024-12-01 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f8a5c9e-790a-334f-8f57-a9937119f609 | -4.53683 | -45.70523 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b93c9467-111b-3922-9b6d-745c1f7baf7f | -3.14271 | -45.98947 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26a8a97a-4b38-34ac-9b8d-6c259b5c5e76 | -2.45371 | -53.62371 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56783d7b-c3ae-322a-b336-7266e721bcd5 | 1.14127 | -51.14909 | 2024-12-01 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9275f95a-6c3d-37d1-8ed4-5092af7c8838 | -2.12307 | -46.41772 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e7ce89a-bc13-3fc8-86ec-ff713bd99a33 | -4.05283 | -46.8244 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31fbd27d-4786-3069-9383-b090d6f4e5e4 | -2.54856 | -45.6147 | 2024-12-01 04:21:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3deab75a-b8f9-3571-aead-9ab40c8e73c6 | -4.16952 | -46.55817 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ffb989a-f4c9-3784-8d68-1d494625255c | -2.2077 | -45.66204 | 2024-12-01 04:21:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aca1a0b3-b852-384f-90a5-56b613f812be | -0.8479 | -48.53616 | 2024-12-01 04:21:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cd31317-7974-38df-a11e-ecc0ae78cf9e | -2.89853 | -51.57624 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d3cb57e-d546-3057-b4a2-be85b0e2b6df | -3.16718 | -46.54863 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d42ef177-e0cf-3e89-896d-0caab3e2aa73 | -1.70296 | -46.1514 | 2024-12-01 04:21:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 895d626d-2a6e-35b1-8f59-4063017bc7ad | -2.6524 | -46.5771 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49fba437-29a0-3107-808d-ae6b1e53e875 | -2.68754 | -51.72792 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ffcb1146-5222-3aeb-88b9-33d41acc974e | -2.59426 | -46.93956 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ffa6b05-d41a-35af-a689-98eb21a0f75f | -0.26402 | -51.49899 | 2024-12-01 04:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76c7b755-7b7c-3fa7-8a18-d46be6c0915a | -3.21365 | -53.12386 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 26319286-8c8a-3736-a0fc-cf46ddcca5ce | -3.26483 | -50.20729 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff4a44da-d34a-3bcc-a732-b35d620625db | -3.33866 | -40.47973 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 762a364a-abd2-3db3-bb3e-d1f35840540f | -3.20891 | -53.11984 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5706c4a6-5f9e-31d9-9bc2-45978e732ad4 | -3.91039 | -42.41654 | 2024-12-01 04:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 78089dfc-b474-377c-b63a-040cbb801944 | -1.25542 | -54.54907 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88f8d55c-8943-3ee8-b8da-5258589c3277 | -3.95218 | -48.17241 | 2024-12-01 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba75b94f-d93a-3ab3-b4cf-aa0ddcdc2f54 | -4.54915 | -43.29819 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| e554c9d4-e45d-3899-9973-1dea111db35a | -3.61917 | -50.19162 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecd8a402-9546-3426-a1b5-c18430f83726 | -4.54805 | -43.30528 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6a73e27f-2846-3208-bd63-5c867f54613b | -4.04463 | -46.83101 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63b20a83-29a0-3715-8528-c784582d6e08 | 0.97611 | -50.12666 | 2024-12-01 04:21:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18207174-ad9d-3a49-ab20-022472002e6a | -3.60288 | -50.37161 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1a4eba6-99dd-3f6c-8d5b-f9f5e93dd6a5 | -2.98309 | -45.57534 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45789531-adee-3d9e-9f29-00071013aa39 | -4.55195 | -43.30225 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 89799258-d8fa-3e58-89ba-e4fc1e0b43d6 | -3.31955 | -50.14151 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a394fa8f-5899-31e1-a87b-61d85bf7eca4 | -4.04309 | -46.9301 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88e343df-0504-3056-a05d-52e3437e85ff | -1.82581 | -47.21507 | 2024-12-01 04:21:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 172ac3bf-d41d-32e5-b112-4d4ae8d1c1f8 | -2.60505 | -46.57425 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a67eb55-3af1-364b-90b1-aa3c0674f070 | -3.26786 | -48.7721 | 2024-12-01 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a2900da-3620-3a12-96df-892072ab8456 | -1.52568 | -45.91586 | 2024-12-01 04:21:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2c83822-28b9-3f5d-84c1-f0757db5a36d | -3.20786 | -53.12634 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7077011f-4fe1-3ae8-94ec-81199a78bd24 | -4.0919 | -46.1364 | 2024-12-01 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04d4d355-1add-31d6-9d34-93cc74a671dd | -3.21238 | -50.27002 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6c8ea7b-574d-3c94-b27f-ad28d417405e | -2.83991 | -49.88903 | 2024-12-01 04:21:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fb7b9b39-8883-3b34-9c68-81be354f8d43 | -2.92678 | -54.26703 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f1a11a9-59b5-3e89-92d9-11c0a4a448e3 | -4.54074 | -45.70223 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 64b09d15-96f9-3100-992c-3ffe3c3d076b | -3.26979 | -50.20391 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad97eda3-cd49-355c-95fd-46b4ad5d191c | -2.54518 | -45.61418 | 2024-12-01 04:21:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bad747d-983a-3c0f-90df-958496c4f2b0 | -3.02928 | -51.53515 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cdc821de-029f-384b-a268-828ceafa399b | -0.01266 | -51.16658 | 2024-12-01 04:21:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 12a5783c-50ab-3916-8b2d-f8e62599be9a | -4.89906 | -41.32156 | 2024-12-01 04:21:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 23d4a170-57b5-3a03-bc14-124fe518d793 | -1.18791 | -54.03756 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aabb111-c900-3551-ac0f-80173fea576d | -2.83533 | -46.86168 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 301e5300-ffdb-3a94-a53c-c8ef97d2a9ed | -3.42081 | -50.18548 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff3f6f32-583f-3254-ac23-806caac107ae | -2.80691 | -53.04131 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b0512a0-6fdf-3b77-9140-822032265be9 | -1.97961 | -52.8944 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f895ae02-0ef9-3636-ac38-af62c0c34e89 | -3.12228 | -45.98631 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c1b2003-2069-3274-94a3-a8aa8a08d435 | -3.39537 | -50.31464 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5fc4d03-c433-3f2e-83e3-7730401b2733 | -2.75096 | -46.11427 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3867f225-0075-3b87-8e56-c464875b7364 | -3.14328 | -45.98581 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93b9b925-ab64-30c1-b758-23500e30ee5c | -3.62617 | -49.85288 | 2024-12-01 04:21:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab7e7699-7300-326b-ae9d-2f807c8f1f53 | -3.93283 | -46.71575 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 377dd287-c6de-33fe-9e19-eba8c29d29cb | -3.4685 | -50.27187 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 06b30d3b-6f20-38a6-a0f6-00cf56cf399f | -2.11883 | -45.96047 | 2024-12-01 04:21:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3e3ea14-547e-3e67-b2bc-3d47cb04a6be | -1.82168 | -47.28832 | 2024-12-01 04:21:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5629417e-2299-375b-9e96-ec34fc0016b7 | -3.08917 | -51.40738 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63c0ac1e-ae4d-34ff-a93e-9ebfd5d43a4a | -2.47883 | -46.57075 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 404e43b8-1128-32ed-bf63-4785da4ae415 | -2.45314 | -53.62719 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cae8591e-e316-36eb-8376-837bfa94d466 | -3.41617 | -50.16017 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2d86d1b-a3f5-3d19-8f47-a69e672e9efc | -3.70385 | -47.14636 | 2024-12-01 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3e8edaa-5ee8-3d71-826f-2d8f12fe2d85 | -3.4264 | -49.99137 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9317a069-8734-3a2f-a7a8-17010609156d | -2.6261 | -54.22015 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbdd5c7b-c2fc-3176-82e0-5d3645746c97 | -3.54189 | -50.40839 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49217714-51b2-3ef0-bba0-b5c8c24770fc | -3.4229 | -42.50848 | 2024-12-01 04:21:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e713d5cf-923a-3436-8519-fcd6c86774b6 | -1.25554 | -51.78511 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73342914-9d35-3316-9f03-5d2c9cdaafc0 | -2.79192 | -51.89721 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2787027-aabd-340a-a5f1-cde1916572b8 | -4.05345 | -46.82053 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82cb4fa0-ae3f-33e5-bb42-c0288e51c78b | -2.63285 | -46.19569 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29859c53-adab-3000-ac5a-9e2592383c66 | -2.12175 | -46.56066 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 604ed1a0-7c1c-3127-a00b-f1d5dc3683f6 | -1.26572 | -51.75248 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6a77fb21-b4b6-3e7a-8623-9f43c36df0f6 | -2.87779 | -46.79943 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a9ce4a9-b95e-3c4a-b800-88c6047a5356 | -3.4659 | -44.01034 | 2024-12-01 04:21:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bb9567a-0968-302d-b2c5-7dd6da2b8452 | -3.26917 | -50.56223 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8964e4f-8491-3422-a302-d7a9174c0d38 | -4.85829 | -41.31411 | 2024-12-01 04:21:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 97a17df6-6c0d-326f-b5f6-a35a57e4ec05 | -2.51852 | -51.83002 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ca3db36-b62a-393d-93b1-0647c3a3b173 | -2.0711 | -51.19337 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d70281ac-3784-388c-a062-2aa383067a3e | -3.16249 | -53.23856 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0da6a2a-a68e-326e-b882-65999963ebe2 | -1.25887 | -54.55008 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aba8a06a-7eea-35f7-85c7-f9841f93d3ae | -2.1141 | -46.5635 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README29.md)
