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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5be08040-3374-3359-8113-34987df1a397 | -3.28449 | -53.84923 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b44fb697-2eb6-396d-baa0-3dcd2451995c | -4.66556 | -46.53864 | 2024-11-21 04:31:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0becd422-c05a-32d5-a700-ae94039c130c | -3.46033 | -52.72532 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c9e3292-b0c5-3411-99dc-f4069bc8fb36 | -5.19827 | -44.2232 | 2024-11-21 04:31:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56877b32-8a62-3fe8-a354-a9c22676dc3d | -3.42289 | -53.28949 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b23d3879-8c90-3d6f-9fad-11723558d97e | -4.07615 | -50.03784 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26f6e0c2-7e3d-35a3-aa13-1f427a645b40 | -4.79204 | -45.79793 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 676b4da8-258f-3f7c-b5a6-0ab69ce59480 | -3.28108 | -53.83597 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 39fecb8a-0414-3141-8753-846a730164a3 | -3.29548 | -53.86215 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb464eb2-7cd7-36aa-9155-3bac3645c8c8 | -3.29246 | -53.8521 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 47a29772-d95c-30f3-80e0-27d38cc69dd9 | -6.31749 | -49.67776 | 2024-11-21 04:31:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bbb58e8e-6595-38d6-af11-2a7b3797981f | -5.10191 | -43.17194 | 2024-11-21 04:31:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef4ad6b4-4d19-37e3-8d20-5a3f50a19d0a | -4.38893 | -47.77641 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80cc39d7-0d6e-3cf1-b29f-f76df7e7ba6c | -3.35866 | -53.40304 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d3eeb08-62ec-33fd-969b-c1f4ca72425a | -6.60619 | -42.38284 | 2024-11-21 04:31:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9b8b5496-e418-3008-8c82-0f6886cac212 | -4.34965 | -45.88196 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d98c0908-4e48-36ec-9d62-444631ac9d1b | -3.91943 | -50.10962 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca65e451-8473-3d72-b27e-c8879cd07b96 | -4.07134 | -50.90456 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54ab1fef-fe0a-3ec2-86e6-22ea8147eaf6 | -5.87928 | -43.87815 | 2024-11-21 04:31:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33d56191-1eba-3f50-bb9a-edd4a189e8e4 | -6.95339 | -47.84797 | 2024-11-21 04:31:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 755b5c8b-44ae-3bf9-bfa1-e7e9b2c597e9 | -3.76181 | -52.41201 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 179c5f6a-34fb-3fbb-a84b-38a7c4e90ed8 | -4.88728 | -45.83514 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2be87cf-594c-3b7d-b6d2-a55b109b4ea1 | -3.28632 | -53.86066 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07c58637-73e3-3720-b4a5-3b23d0981122 | -3.66509 | -51.57106 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d87db21f-7761-36ad-8558-803b6ff6fdf0 | -3.28365 | -53.82531 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8cf8777e-406a-3b5b-853b-afab0dbc1f2c | -3.22656 | -53.62577 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 187e25e4-2046-30ba-b309-814973e0f387 | -4.60864 | -45.74396 | 2024-11-21 04:31:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 389d32ae-f793-3633-9dbf-9aea0cf711f9 | -4.41413 | -45.96163 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75581003-b8cf-3cff-9fe1-18b80fef5697 | -4.24768 | -49.18727 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1df23053-2fb8-3093-a2a7-03f34e0768ad | -5.00166 | -44.80082 | 2024-11-21 04:31:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 973e041d-aef8-300e-bcb9-7455eb0cc86a | -5.45104 | -43.23656 | 2024-11-21 04:31:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7da59979-f966-374e-b599-ae2f9e466110 | -3.72878 | -52.31619 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ced700c-327b-3b4b-b33f-b78baa354ed1 | -3.10157 | -53.99206 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef845a95-71fc-34a1-80a0-760a81654010 | -4.65969 | -46.40136 | 2024-11-21 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cc39b40-6922-3ae4-ab8b-0ff66feacb9d | -7.50423 | -45.92414 | 2024-11-21 04:31:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c4d7b46-ddb9-380e-8c0a-226a11e07d0f | -5.46219 | -43.26722 | 2024-11-21 04:31:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7413cc32-c411-3c44-a989-c23145f743b9 | -5.45464 | -46.48465 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c829bbb7-fa08-311d-bc0a-a7cd42287355 | -3.27403 | -53.02088 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dc08629-2d9b-3917-8c28-c68fd66e07e2 | -3.56845 | -51.34891 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7b4f277-43bd-33be-8f27-2fbc5a5ada6e | -3.27757 | -53.83386 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1dfba010-2fab-32f9-bfa9-577f6ee3bc72 | -3.2829 | -53.82994 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d551c10c-baac-3255-8207-7bead335c302 | -7.02991 | -47.61825 | 2024-11-21 04:31:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b98e9ba-0074-3a3c-9ab3-e800e96f58aa | -4.53892 | -46.43658 | 2024-11-21 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8876066c-2ad7-3fbd-b049-f36c3f39cbfa | -3.3193 | -54.09063 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ae471d2-f0c0-3272-966b-3c3097023780 | -4.96659 | -49.84413 | 2024-11-21 04:31:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1182f7af-f732-38d9-99a1-47f0f503be97 | -7.49316 | -47.16802 | 2024-11-21 04:31:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97109828-1493-34aa-825d-ebeb7bbc4c27 | -3.38241 | -52.45821 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 011a3f5b-5acf-384b-b04a-45b187ce8d58 | -5.94735 | -44.24312 | 2024-11-21 04:31:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a0f3bfdd-6f8a-37f8-aa0e-e9eaaeda58cd | -3.10052 | -53.74227 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 65ae80ac-f602-3039-aba8-5be5811ada07 | -3.47024 | -54.54237 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae1ee750-f889-3dc8-9cba-d7d0ff689069 | -4.05999 | -49.28501 | 2024-11-21 04:31:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d30c02f-3d7a-3d3d-b582-294f767040ed | -3.28945 | -53.84204 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb24a207-f156-375d-af94-2711ab7453e8 | -4.56324 | -48.02191 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3efd34b8-ecb2-38ea-839a-84d78c951657 | -4.3606 | -47.22631 | 2024-11-21 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cfe0c1c-6836-343e-9904-7ead59261ffb | -3.28066 | -53.84384 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e228bd45-8062-3d3d-8fe8-695b9ff76544 | -4.08359 | -49.29263 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12f2024b-3d3a-335e-94e5-268d323d751a | -5.9424 | -46.19431 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 675f78b7-c0ba-3479-9a43-e0b372ba3aad | -3.91877 | -50.1137 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19c43eb0-0e6b-3320-b761-9ac10a610736 | -3.61731 | -51.09171 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 555fac6b-4456-3b53-b696-43299a88965c | -3.51192 | -53.80038 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd05950e-09d3-312a-a3bd-f0c342436884 | -6.82663 | -46.77222 | 2024-11-21 04:31:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ffa1e911-77be-3634-927f-bb0c09ab5317 | -7.17719 | -45.04129 | 2024-11-21 04:31:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8bfa766-50c2-3eea-aa70-101b4af5dc86 | -4.55065 | -48.01988 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7a6c851-4565-37c3-9954-ad5a0766b6ad | -3.2909 | -53.86141 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8499b0e9-87b1-38ff-8a99-98acd259c43e | -4.64138 | -45.66719 | 2024-11-21 04:31:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ac31569-2480-3d96-844d-1a5eb169b46f | -4.58737 | -44.82513 | 2024-11-21 04:31:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42c0604f-ada0-3b38-b066-c2da859599ca | -3.83467 | -50.28815 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 317a989d-c4c4-3d4a-a760-9f5fe6be46c2 | -3.2871 | -53.85602 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e53fc25-cad5-39cf-8f36-868d01b6441e | -5.58719 | -46.37068 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc81e6c5-8b5b-3ccd-b72a-4ebf214cb100 | -5.2194 | -44.90857 | 2024-11-21 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06bc5f5b-f87f-30ee-8ae6-0f92bede6dcd | -3.75994 | -55.57315 | 2024-11-21 04:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11cd8ee6-2a2e-3ca0-81d5-daa07323939d | -4.38891 | -47.75506 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11bc164b-cb90-32a4-8051-81e558f384b5 | -3.51422 | -54.69023 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eb531a0a-cba0-37ba-b5c3-bf015c87c8ea | -3.69632 | -51.27447 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c797c18-3170-3c49-892b-0a06bbcc01de | -6.81883 | -46.77825 | 2024-11-21 04:31:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 21cc1867-d8de-314e-8ff8-581b391a92be | -6.14212 | -42.77319 | 2024-11-21 04:31:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| cf02e1f9-47a4-3534-9072-6e8b1de257a8 | -4.57769 | -48.01701 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 1026508c-dea1-38e9-8fdc-235a6c8ee04f | -3.73161 | -50.44008 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fee45f9a-b688-32cd-a883-9f7f245461d6 | -3.81499 | -52.34501 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a0274118-c70c-375b-b53b-340842eefbfc | -10.70318 | -48.80693 | 2024-11-21 04:31:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9041b724-3296-366f-95ca-af58d3a5b243 | -3.86265 | -52.33073 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ce81adf-fd66-34a7-b19e-08fc13d36521 | -3.92769 | -51.17691 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b655fe2-73c4-3869-968c-b9229bf45905 | -3.5074 | -53.79947 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c64f5159-54ea-3e7f-8589-9c3fba6b94e7 | -4.79254 | -46.46172 | 2024-11-21 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 987ccac5-4ced-38e8-8e4e-466e7585e9fd | -3.68556 | -50.21887 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b6480868-d541-337d-a385-49c2e9eab352 | -4.18096 | -53.57703 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8eb92034-255c-3064-aed1-5727dd1929e1 | -5.19043 | -47.73972 | 2024-11-21 04:31:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e475cdc9-b343-391c-bcf6-1870de77968c | -3.93729 | -49.95467 | 2024-11-21 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a27e7442-c83a-395e-a65e-b2f7c7b9333e | -3.71435 | -51.18583 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27b8c72c-8600-3443-bf62-0a8632b32efe | -4.36945 | -46.09335 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86dd9e1d-f936-3d4c-b2ed-64d2551a0ef8 | -3.60335 | -51.55593 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 430f87d8-d540-34c4-b45a-46aa9c39fd78 | -3.81236 | -51.27069 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88f8552a-8483-3122-a8fc-7468d0d20b55 | -6.21281 | -46.15851 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5fce2ff-af26-3996-9945-e0995e4740bf | -3.10605 | -53.73685 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3021a142-2e6a-3427-8690-e18b1855c4b4 | -6.99117 | -46.3166 | 2024-11-21 04:31:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae92fd8f-e51b-3b48-9de4-74ae021204b5 | -3.56505 | -54.68293 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41e7adaf-38e3-3fa3-91e7-e324e12d5ca8 | -7.39169 | -42.77896 | 2024-11-21 04:31:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 08956626-1678-3905-9a8d-0c8e4556561e | -4.63897 | -49.54869 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3b94b9b-8b3d-30fa-9e6f-5a5f367ac0b0 | -3.3902 | -54.54995 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ca94caf-c057-3ea3-bcec-fbb562ec8e4c | -3.27469 | -53.01677 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README45.md)
