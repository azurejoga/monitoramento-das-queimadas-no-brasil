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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3818d7e-b88e-36c8-b49a-2605c672130d | -1.98423 | -52.08075 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c30ce9c8-b829-3d0f-8585-87b5abef35df | -1.98009 | -52.08414 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b4f0811-2331-3129-930e-563e97e5dbe6 | -1.97656 | -52.0836 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ac3a921-67e2-3b7e-995e-7ca9f177fe1b | -1.92636 | -52.12809 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bedfe880-1def-31e6-bff5-184b854a7c42 | -1.92284 | -52.12754 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a43ce08-f1d1-3cc7-b562-f0d54a6e142f | -1.92224 | -52.13145 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a21e2da-3f78-3a86-9888-b742ff8fc590 | -1.92064 | -52.0519 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c05b6fd-b636-3f4f-855f-e16a2ece682c | -1.91931 | -52.12699 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e880ab8-4a86-3f2d-8e94-1549e397887f | -1.91711 | -52.05137 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82759bf6-601f-3b2b-a2f6-5d980d7ff8cf | -1.83845 | -52.11561 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f85779d-3683-30ac-a30e-4653249cac36 | -1.82771 | -52.02258 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2151f99c-2efa-39f6-b5c2-2b8d25905418 | -1.82767 | -52.02148 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6ed8562-77cf-3165-809b-3be348954a68 | -1.75909 | -52.06825 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80d3b835-d4e0-38cb-9db2-fa3f0fd423b7 | -1.75556 | -52.0677 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 18270d34-7688-3507-a5ee-d92e160f4526 | -1.75459 | -52.02744 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4b91e52-134e-35fb-9b9b-019a6bf8a212 | -1.08444 | -53.16747 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9f32dda-69a7-31a0-8dd6-0a7799ce91b7 | -1.07769 | -53.16644 | 2024-10-29 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92cd9d89-c007-3b41-b0e8-deac40ab7dba | -3.30104 | -53.37177 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78ac24ef-567d-3924-bdad-36bd1bde36a3 | -3.22499 | -52.60826 | 2024-10-29 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35d1c00b-1cb1-30b7-bb89-787605f83e99 | -3.22467 | -52.19005 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bafbad23-e8da-3ac4-87d7-44383a224a2f | -3.22149 | -52.60773 | 2024-10-29 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a2151a3-1ab4-301d-804a-480a2cb28f0f | -3.21817 | -53.36707 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2a052c7-607c-3b29-9363-a9e149977a16 | -3.21477 | -53.36657 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b7fc8c9-b0a1-37cc-b98c-d5f0e0bee53b | -3.2125 | -53.35881 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82e79896-61ca-3594-89d8-81543553b076 | -3.2122 | -52.45971 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f397c4c4-03a8-3a1b-93a1-425a1872fe6c | -3.20967 | -53.39912 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 287eb259-fcc8-3c1a-a33e-ac5f44c281f9 | -3.2091 | -53.40275 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7823b12-1454-32a4-a2bc-d92b08b22aa9 | -3.20854 | -53.3619 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c821d055-4f0e-3d39-a4b0-17cfd81e2400 | -3.20627 | -53.3986 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f61f28d9-8a44-3930-9bca-2c341b8fe74b | -3.20571 | -53.40223 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f23185f-db21-32e2-b750-cb7d135f3e57 | -3.20457 | -53.365 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a12cd89-b386-3550-bad1-f6627296d6e8 | -3.204 | -53.36862 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48f893f8-9650-336b-b365-4ec9f26686d0 | -3.20231 | -53.40171 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 587cb9d5-39df-369a-b14b-11c9906e3000 | -3.18566 | -52.88243 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f31e6b83-44dc-3c51-aefc-0440fdcef784 | -3.1822 | -52.88189 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9287ec84-584e-3e91-a640-46045caafd1f | -3.18011 | -53.16283 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37e18b27-0b03-3ff9-accf-06348219b17a | -3.10613 | -53.05363 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1653f2b5-2f11-3aa4-9b6a-5bedff18fb9b | -3.10556 | -53.05732 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a49b576-4bbc-3378-84a3-707a45c0d22f | -3.1027 | -53.05308 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78dcdd49-967b-3bb2-bc35-bf2547eba624 | -3.10213 | -53.05677 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7cf1886-47d3-3516-96fd-cd96c1f633c9 | -3.05775 | -53.25324 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72348f66-7b7b-306f-b8ac-6fcf9b8ea3fd | -3.05491 | -53.24903 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48881353-93d2-3923-860c-429b71b1ea08 | -3.05435 | -53.25271 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0f10bd4-0bfe-3bb1-8c73-41530e5d4d7c | -3.05378 | -53.25636 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41700b10-4628-3ba0-b105-065b5477f39b | -3.05151 | -53.2485 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e16b2f1-5f69-332c-a49a-a4d1ac4b0432 | -3.04925 | -53.26308 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c64ed42-ac68-31ee-b58d-343f5c5ffcd2 | -3.04293 | -53.03709 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4d48dd9-1711-37ea-a747-262f7af97b09 | -3.03951 | -53.03654 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07ca0dab-05cc-32db-af08-c5fd28cf52cd | -3.03752 | -52.35423 | 2024-10-29 05:01:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 371aa617-b301-3cad-a0dc-e2fb27722dd8 | -2.32087 | -52.71895 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a377090-9606-30d5-a211-977b7391a242 | -2.26833 | -53.48333 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f6545bd-b224-36c2-a76e-2786584f83a0 | -2.2644 | -53.48637 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75824a95-bec2-3e09-aace-c0a4538d246b | -2.15263 | -52.83492 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06325f8a-f8ad-30de-918a-fff9f5f80432 | -2.12819 | -53.26062 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e9ab638-0dfb-32ac-bba3-28e7a20fff8a | -2.1248 | -53.26009 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 717d305e-badc-353d-b39f-5158136d3c08 | -3.00721 | -53.4427 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0bec7918-373c-3c42-bd43-04536267f415 | -3.00155 | -53.43452 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e1f2982c-f47e-32d3-9b00-e2b3c0c8b522 | -3.00099 | -53.4381 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3dc54da5-e607-31f7-881e-e5aa3b42aff1 | -2.99816 | -53.43401 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39df2d6b-9581-351d-af6f-48a2f6351dec | -2.9976 | -53.4376 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 55bd5bdc-2980-3446-bb56-975e042eab76 | -2.99704 | -53.44117 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bed5c944-299a-36fc-93fd-7579857d2f15 | -2.99421 | -53.43708 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67e3b715-2c77-32e7-8960-d82eb1530935 | -2.99265 | -52.90722 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cead3c97-c531-3449-a706-b402ccb57d98 | -2.99208 | -52.91095 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a5df6f5-4fa8-3fa2-85aa-e17b6084fd01 | -2.98863 | -52.91043 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2e4501e-ccbe-3cb3-879e-0e835b217a0f | -2.98294 | -53.26457 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1f041b1-d50a-3a78-a31a-af1907fbca60 | -2.98237 | -53.2682 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb6e037d-f18c-3fbd-ad88-98ea524b7178 | -2.97953 | -53.26406 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dbdba33-d42d-31d6-aa2a-172fc659a846 | -2.97896 | -53.26769 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8741bdc0-a24b-34f9-ae29-753d96a7d1c3 | -2.97499 | -53.27081 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43e1bd5b-f868-30ab-9b2d-bc9cf2ab2caa | -2.97385 | -53.3452 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fddd482e-dd31-391f-9c9f-0ca21b3be005 | -2.97215 | -53.26667 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7bef7ab-a26b-3e5c-a7d2-7e65ebb6cc6e | -2.97159 | -53.2703 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b89f2db-010c-330d-ab69-0e34f502fe53 | -2.96874 | -53.26617 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fba65c3-b87d-32c8-9013-cde759a9f927 | -2.94719 | -52.56688 | 2024-10-29 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c5fd2e2-7882-3d13-8e30-b2df2cb09ec2 | -2.9437 | -52.56633 | 2024-10-29 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fa7f068-a292-3cd6-9e2d-9b437d4d5033 | -2.8879 | -53.04311 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e3f124c-73b7-36ec-bc37-1f54d264cd06 | -2.86913 | -53.34349 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 688d9a6e-812c-39db-9569-647cd8d282ac | -2.86801 | -53.35067 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 69efca62-9b1a-394c-b609-8dc6f91b176e | -2.86799 | -53.32848 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cfab313-5a07-38fb-9034-ed0f7e887031 | -2.86745 | -53.35424 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 74a7b7b6-6460-3c82-b65f-f37b74ecf693 | -2.86743 | -53.3321 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1046fd1c-16e0-33ff-9aa4-b2ad0d01c6b5 | -2.86686 | -53.33574 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5408b0e8-c67d-3d47-9579-33b1aee6223f | -2.86629 | -53.33937 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d209e47-ac02-3ca6-a693-b2d5fa818181 | -2.86573 | -53.343 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0f72ebc-d30d-3d03-b606-d3529f09227f | -2.86516 | -53.34661 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72d6d40f-ea58-36d1-96eb-201d220024a9 | -2.86461 | -53.35018 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1e134b5e-ffa0-3ed5-a7ce-708787feccef | -2.86405 | -53.35374 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e371cc94-0002-3352-bedf-b2a2249cc72c | -2.86403 | -53.33162 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be770bd0-517c-3638-b4a9-80c60d2b629f | -2.86346 | -53.33526 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 352e892a-2392-3474-900e-700e7d1d0062 | -2.86289 | -53.33889 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31bc8341-55ac-3dea-a5bd-c12af6b0c780 | -2.86233 | -53.34251 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0647b713-84d5-3aaa-b5f0-d99117733741 | -2.86177 | -53.34612 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87722730-6c33-3e11-abee-cf715a7775cf | -2.86121 | -53.34968 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8329733e-a1cd-3026-bd8e-24a6d46a1d75 | -2.86066 | -53.35323 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48e2905f-ec00-3b98-ab19-edd69f01f526 | -2.86063 | -53.33112 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2bbd9b9-ad43-3f04-9bc2-a59c549bc7de | -2.86006 | -53.33475 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0f2d473-fb6b-370c-ba39-05bb56cf3b23 | -2.85837 | -53.34561 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c836046-78e6-3fe7-ba61-33e9d97ea6e2 | -2.85782 | -53.34917 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8eb8094e-50b3-3213-8bbd-94eac9d52d07 | -2.85667 | -53.33423 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README81.md)
