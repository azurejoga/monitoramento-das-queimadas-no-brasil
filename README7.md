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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d3ec0f5-7df9-37bc-bd0c-115c5776e938 | -7.60416 | -45.55946 | 2025-06-20 03:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b76058ba-8d11-38cf-860b-fb83b5bef276 | -9.30922 | -44.83456 | 2025-06-20 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d8bca7e-e3ae-3818-b0b7-0581970875d9 | -7.02075 | -44.59318 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d064e0cc-45d9-32b2-a19c-661178fba3fa | -8.72441 | -47.98833 | 2025-06-20 03:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 630ff016-a593-37a5-bfd4-8d244609b103 | -6.67599 | -44.25024 | 2025-06-20 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 71dc3647-0d7d-31fa-a42d-0b52ad62b669 | -9.29946 | -44.72689 | 2025-06-20 03:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c80a3b7-f261-346f-82a7-c76d1cae20cc | -7.01917 | -44.60203 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 594c32a1-ffed-3a26-ab6f-119f584cdb20 | -7.26546 | -45.35948 | 2025-06-20 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5182f385-9a11-346a-b6b1-64c2636eafca | -10.49766 | -47.00808 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bcc8988-7df4-3c72-ba8e-dac7af9b1806 | -10.42831 | -47.12148 | 2025-06-20 03:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7526ea87-b000-34ea-8a42-5fda66b61066 | -7.39441 | -45.40176 | 2025-06-20 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b49e510f-3e4a-3f60-ad61-267598569d11 | -4.81924 | -44.35686 | 2025-06-20 03:38:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e541677-48f1-3340-9859-1e1d90ba0da9 | -10.49434 | -47.02428 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5a0092dc-a8d2-3f8f-a61a-b94739afd7f5 | -10.42236 | -47.08345 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57dce45c-7571-37aa-96cf-0a8023193016 | -9.83917 | -44.71039 | 2025-06-20 03:38:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02a19b05-a20c-3d06-ae30-c9362b89c70e | -5.12772 | -45.03472 | 2025-06-20 03:38:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae5a4d30-189e-3282-8a2f-5ff22e2c2cdb | -7.21302 | -43.06775 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e7ab7ab7-6c36-3dd4-8141-5076fe6fac69 | -7.02005 | -44.60828 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf194559-b356-390b-bc5a-5915f6035ed0 | -9.84635 | -44.7037 | 2025-06-20 03:38:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4f5ba8d-9dfe-39d7-9a87-9012086ac13f | -7.22194 | -43.07972 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 604bfef5-af62-3399-9293-a0303f5badfe | -6.84849 | -42.79564 | 2025-06-20 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a37b9cdc-e8d0-34fd-b267-b448fefaed29 | -7.21363 | -43.06435 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 289b034d-2a52-3ca7-b9c6-4158ba7dd5ad | -4.77803 | -47.25188 | 2025-06-20 03:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b3a0f1a-14e1-3979-b80b-7d6e1c5870be | -9.30343 | -44.83341 | 2025-06-20 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ad9e56d-e16a-3a4d-93cb-f33ac4634ef3 | -8.95405 | -47.97743 | 2025-06-20 03:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d0c7dc1-09d4-391b-9ffa-62fcd8afc76d | -10.48338 | -47.04477 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6714b873-2324-3965-aa0a-f22a19f34c3e | -10.52532 | -47.58761 | 2025-06-20 03:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d589f467-8c7c-3c08-99c5-4466f48bf3e9 | -7.27074 | -45.36565 | 2025-06-20 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81b5e1cd-790f-3246-a49d-a6f89099235c | -9.84862 | -44.69171 | 2025-06-20 03:38:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0d25ea8-5c17-3ca4-a8d2-b2301c375a66 | -7.21241 | -43.07114 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 56e7724b-1f6f-3f75-bb0c-e8c5f94add7f | -5.15632 | -38.00191 | 2025-06-20 03:38:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8cb55558-2ff9-3fc3-a8a1-a2876a6058e9 | -8.26493 | -44.95906 | 2025-06-20 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04035f6c-dc35-383f-a227-8a33a3aaf9c0 | -7.02248 | -44.5952 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48a3932b-5887-343e-ad92-8712c572a1fe | -10.4954 | -47.02289 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1bb1b217-22e8-39d2-8a43-aa6580030208 | -8.25898 | -44.95789 | 2025-06-20 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c594342-1a4e-3d74-883e-ceec13750d95 | -7.02166 | -44.5996 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30755587-e361-3bfe-8ca2-1b792599a2c5 | -10.49433 | -47.02832 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 036af7dc-1912-3ad3-b8e4-4ac2566d42a2 | -10.4846 | -47.04332 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ca09b09e-406c-35c5-81a7-2ebbd6a6f7de | -10.49215 | -47.03933 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d17c02b-03fc-3dd4-8a32-cbf020309138 | -7.60779 | -45.55487 | 2025-06-20 03:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0dcb82f-9b48-39ae-83b6-43b43a348dc2 | -7.02579 | -44.59938 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a3aac53-0ae9-306b-874b-d6b06d555f9f | -10.97693 | -42.17957 | 2025-06-20 03:38:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c8f295f3-911c-3467-9d7b-f69ec3eedecc | -6.67516 | -44.25481 | 2025-06-20 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8cef082a-5594-31b6-9a82-c7bf9155a167 | -10.49323 | -47.02971 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbd3c083-8447-37ff-a61a-fe3c4c0d688e | -7.7552 | -47.61768 | 2025-06-20 03:38:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fa7218a-90f1-31e8-98cf-21fc5f95310e | -9.33241 | -47.83087 | 2025-06-20 03:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50e3b4a3-8bf8-3f36-b0cf-12495ad56bcb | -7.06866 | -43.39602 | 2025-06-20 03:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e2dd9ae5-8bc5-39ef-bdc9-8f3ea451c39f | -8.27087 | -44.96021 | 2025-06-20 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 654a7ef2-f8b4-356b-830d-3ae2ab1c3298 | -8.9611 | -47.97872 | 2025-06-20 03:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae3fe99f-cf3e-3a44-ae56-a6a3e5cfa64f | -9.83991 | -44.70648 | 2025-06-20 03:38:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73f24b28-df07-3626-ae3a-284a2cc1197f | -11.31457 | -45.20876 | 2025-06-20 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8cafc8f2-0110-3bf5-a98f-4d56c7477ee1 | -4.81818 | -44.3591 | 2025-06-20 03:38:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88607f6e-4b0e-3b1a-a6fc-be537ed90581 | -10.48235 | -47.0547 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74efcf52-bc13-33c1-bf3b-15d80a4c6e72 | -9.30596 | -44.72406 | 2025-06-20 03:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62ee73ec-8140-3d57-882e-21db2cdc6486 | -8.12315 | -43.12468 | 2025-06-20 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc3fa5ea-6171-3c8f-8a2b-59afa49eb214 | -7.2184 | -43.06865 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 5ca743b1-485f-3529-80f4-536969bee990 | -7.02084 | -44.604 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f9ff162-6b2d-3154-a5fb-753c62c3f72e | -7.21718 | -43.07541 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| cbbea535-9831-3925-ba3c-27e91cb1a7ba | -6.84262 | -42.79786 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| de00aa2b-6ded-31ba-8e20-9132c3608919 | -8.27007 | -44.9645 | 2025-06-20 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0be7b83-38f7-3886-8f32-12762359d8d1 | -7.26985 | -45.37048 | 2025-06-20 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8b30831-5ecb-3d2c-9754-61152eeffe76 | -10.47359 | -47.06469 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9dc86128-8f01-351a-aa28-d019c8377249 | -9.31502 | -44.8357 | 2025-06-20 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a6aed7d-c214-32de-88e2-5990f012a1c0 | -9.95095 | -46.63271 | 2025-06-20 03:38:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16157270-aa31-3576-9cb3-c6a14e2715ad | -7.15029 | -44.06462 | 2025-06-20 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5947ab9-8595-3a60-978c-76ad900a5922 | -9.31143 | -47.79176 | 2025-06-20 03:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42e08024-0b2d-37f5-aae3-793f2d318d1f | -8.17031 | -43.15382 | 2025-06-20 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 56c6e577-6be0-329c-bd31-d6473fb3452c | -10.52273 | -46.64957 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 62fd35bc-adda-349b-bc97-c0e6a7f52f41 | -7.22317 | -43.07293 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 766d4263-5c23-3c73-b6b0-bb76cb1316e6 | -8.72114 | -47.98911 | 2025-06-20 03:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ca60a02-f825-394e-b9d6-f0a6acef6d87 | -8.25224 | -44.96094 | 2025-06-20 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36bbc586-cb4e-3b15-9071-0a3d083586d8 | -10.47703 | -47.04735 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 55572794-2d1f-3227-9319-c8c409f6c71e | -6.24384 | -44.65622 | 2025-06-20 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ff6264b-3e0c-36f4-a938-3022d87c9213 | -7.01734 | -44.58981 | 2025-06-20 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbfc747e-c3df-399c-91ef-ef92a6747f6f | -6.66435 | -44.24788 | 2025-06-20 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc39acad-114e-3345-a85f-11b8d92b9431 | -11.8852 | -40.95636 | 2025-06-20 03:38:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ebf82415-7794-315c-b0c7-b6b0f886b220 | -6.24472 | -44.65145 | 2025-06-20 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f27f7ff0-b531-3d75-bea0-b93ab86a41d7 | -9.84785 | -44.69577 | 2025-06-20 03:38:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0769ccc9-e00e-3d37-8f96-9cbef1c98a7d | -10.52658 | -47.58123 | 2025-06-20 03:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ab51ae5-cfac-3474-9b3d-4439499a78da | -5.7869 | -43.46098 | 2025-06-20 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acc978de-229f-33d1-a727-09301dbdd2f7 | -7.11403 | -43.14304 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5c01bcba-99b8-31d1-9c91-fab2a83cbad3 | -8.12841 | -43.12589 | 2025-06-20 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 82ccf1e3-abf4-306d-aafa-ce48cdfd0061 | -7.06316 | -43.39501 | 2025-06-20 03:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 71d62b3c-b571-30e1-9a11-64b55a0bc829 | -7.22255 | -43.07634 | 2025-06-20 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e5765991-621b-3c51-8c96-2c136f6fc40c | -7.60691 | -45.55972 | 2025-06-20 03:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4e73aae-5753-3bea-b3d9-dec3c33ba682 | -10.52099 | -47.5831 | 2025-06-20 03:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3462a1f-702e-3da1-9190-3d81b0d722c3 | -5.78128 | -43.45985 | 2025-06-20 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8989b1f-3692-31b6-9d6b-1e300cb61dbd | -10.48123 | -47.06032 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf2113a9-297b-3ad9-9289-82967dbe8379 | -6.67098 | -44.24463 | 2025-06-20 03:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d9e316b3-60c8-3e38-9409-00767abbfb2f | -10.4868 | -47.02808 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c112ca1-6e45-3bf9-bf97-276a199c7ac9 | -10.49655 | -47.0135 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d495d91d-ec51-30cc-8301-334e058e57cd | -10.4879 | -47.02666 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 118e66aa-a6b0-32bb-8787-0580901d1276 | -7.38722 | -45.40575 | 2025-06-20 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 42c0b32b-78b2-3b8d-899c-b20d2c1f6932 | -5.12488 | -45.03115 | 2025-06-20 03:38:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f733dff6-3b6d-3fdb-8ec8-e09c982d2d67 | -7.06252 | -43.39857 | 2025-06-20 03:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b416f72-916d-3731-b17f-e97c43d28409 | -7.27163 | -45.3608 | 2025-06-20 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c36497d1-f7aa-306f-ac5d-1672f7eed3b0 | -11.32108 | -45.20599 | 2025-06-20 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a547d9b4-7652-3284-8c97-d6f5006b602c | -10.48572 | -47.03763 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb1bfeae-ef77-3925-a020-4591311a4e38 | -5.48473 | -42.14488 | 2025-06-20 03:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8574e522-be45-3039-8b0e-03a998a454b1 | -10.49753 | -47.0121 | 2025-06-20 03:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README8.md)
