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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8e8e726-d6b5-373c-8804-d98a00b66339 | -6.94434 | -42.89378 | 2025-06-13 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9629c4e7-696d-3660-835d-edfb46b604f3 | -3.0938 | -40.0922 | 2025-06-13 04:08:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6fc62e02-0948-35af-a1bb-7bc204943f64 | -5.6407 | -43.60308 | 2025-06-13 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bd9c6c3-03e2-3e17-b1ef-f9975ee4d5d3 | -5.49956 | -35.58549 | 2025-06-13 04:08:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff9b3c4c-5c33-32fd-bbc4-550c047d35e9 | -6.94491 | -42.8902 | 2025-06-13 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d85ef37e-fc14-3439-b32d-dc737e206a84 | -4.19344 | -38.37213 | 2025-06-13 04:08:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a728da3d-99bc-3fe3-b786-33485a93f0b4 | -6.15766 | -47.27074 | 2025-06-13 04:08:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 196beee0-d85c-3757-9ecc-d36f2fd023e0 | -5.64417 | -43.60364 | 2025-06-13 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6718400-4901-3f5a-b88f-b905d19ab6bc | -5.64478 | -43.60666 | 2025-06-13 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf059446-a583-3ce9-a937-9b2b795744ba | -5.50014 | -35.58152 | 2025-06-13 04:08:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9025485a-0b08-365a-a5f8-22f34718a878 | -5.64765 | -43.60421 | 2025-06-13 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f74bb0c-5f34-310c-8a57-350c43876947 | -6.94885 | -42.88716 | 2025-06-13 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8f09d7af-2033-3ade-b6ac-3d9eda8158a1 | -5.64356 | -43.60746 | 2025-06-13 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59d2a8f3-7c92-3d55-9052-01b1d5f83d46 | -6.94771 | -42.89431 | 2025-06-13 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| bb4e596d-6a51-32e5-93bc-bcf37524fcaf | -5.90437 | -43.45292 | 2025-06-13 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71309fe0-77e9-3784-8af3-0a8572b3428d | -6.94994 | -42.90203 | 2025-06-13 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 3770839f-b4a1-3916-89dd-2cbc0d7a4f9b | -13.8867 | -54.6312 | 2025-06-13 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 2c0c3e46-3625-3d22-b6c1-83390f116e82 | -13.9059 | -54.6291 | 2025-06-13 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 06370a26-dde6-3d60-a91d-307ac475ca7c | -10.6492 | -49.4267 | 2025-06-13 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a58afc21-1e7f-39f2-a0d2-36a4c45a2bca | -10.9167 | -56.8336 | 2025-06-13 04:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 2fef81a2-b4d2-3cc2-bbf7-7c661abffbab | -10.9355 | -56.8322 | 2025-06-13 04:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 56eeb5c9-760f-3987-a80b-20537dc5305a | -10.13847 | -47.43972 | 2025-06-13 04:10:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9149897-12ad-3393-9376-7bb9b0bf15e5 | -8.07539 | -43.11866 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 974d2c48-cdc8-3288-97f3-053e411a2b12 | -12.2907 | -50.10786 | 2025-06-13 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea37a9a8-489c-31bf-a11b-d6f462340623 | -8.1042 | -45.90343 | 2025-06-13 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 874d326b-9bc4-378c-be56-e73a818caece | -10.65311 | -49.41856 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0a7ec099-763d-3c6f-907c-79b0eb70b09c | -13.11589 | -44.07714 | 2025-06-13 04:10:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13cff847-773f-34cd-a130-e0eb71737525 | -7.72304 | -46.61964 | 2025-06-13 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 208aaa0b-4a8a-3b1a-be0a-ebd6479e0db4 | -9.40254 | -48.42484 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f86c577-a0bb-3a3f-8613-6d848f7d6d50 | -8.8127 | -46.69099 | 2025-06-13 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4da8daa-a8c8-3ae0-944b-8bc17a29686a | -9.41197 | -48.42225 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60970321-3247-3815-93f0-12c958e1dbf8 | -11.74238 | -54.72051 | 2025-06-13 04:10:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff836e2d-06d7-3bc8-9cc4-139da348fdc4 | -10.91689 | -56.83307 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 19d8b329-7c28-3217-be3f-41a9241464c3 | -10.13445 | -47.439 | 2025-06-13 04:10:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea44aaf3-3730-3539-9899-68716533c135 | -7.64326 | -43.63194 | 2025-06-13 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75513408-ef3b-3e52-92ac-574c1a8d73d6 | -9.84225 | -44.69096 | 2025-06-13 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce3c16ae-01e0-36c9-9d56-85fba7761544 | -10.35201 | -51.98977 | 2025-06-13 04:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ec37860-12ea-3035-aa2f-83371bc9d56b | -9.40114 | -48.40756 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0949a70-7b73-3b55-bb00-bd3441f56b20 | -11.00353 | -50.75771 | 2025-06-13 04:10:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48ac2bb8-8039-3b76-bb64-77aaabaf68f3 | -11.13797 | -53.94999 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4eac35a3-4590-3cf2-908a-ea47cfced6cc | -10.69516 | -49.49921 | 2025-06-13 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 870f5abc-5e73-3bf7-80da-8057782933fd | -12.05484 | -48.07515 | 2025-06-13 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b8a363b-9954-3e1c-9f4a-9b9328ad70e4 | -9.38875 | -48.42677 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 001c2a08-c8d8-3a76-b9c8-7c1e6c12bb01 | -10.69973 | -49.50005 | 2025-06-13 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4d02d772-529f-3c15-b028-ff39e15558db | -7.69562 | -45.78144 | 2025-06-13 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5009c0d6-9a98-3b49-b7a0-cfc046392289 | -9.4018 | -48.42904 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 187719d9-c509-3687-a6c7-1555ac323e57 | -9.39099 | -48.4117 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7085e7cd-ad9f-3f1d-9c62-922c88ced0de | -11.81073 | -54.50662 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 66e23054-7b11-3e8b-a943-92ddf4f6dd01 | -13.22413 | -47.20693 | 2025-06-13 04:10:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91ae5c47-1f38-382d-8f0b-509622ce3cdb | -10.29485 | -52.84416 | 2025-06-13 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c875d978-f643-3223-b3ed-ce8ec3cd8f29 | -11.17772 | -46.88378 | 2025-06-13 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cb48ced0-c18a-345a-ac48-53a32d82b0f5 | -7.4617 | -45.51605 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce3535ff-feaf-3bc1-98bc-611508859e64 | -10.73679 | -47.61477 | 2025-06-13 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bda5a5c3-07f9-3d40-b315-67500e7d5892 | -12.28145 | -50.10607 | 2025-06-13 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a29d82da-6812-39b3-a20d-067f9e454680 | -13.87672 | -47.30532 | 2025-06-13 04:10:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5f035b3-3aca-3a41-89cb-7259c96e9fe2 | -12.42947 | -54.87611 | 2025-06-13 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84faf785-3385-3e62-a1de-6b51c79cf106 | -12.00103 | -45.13608 | 2025-06-13 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 70c5d3fa-7df9-3a6f-a551-33675f706c74 | -9.84666 | -44.70767 | 2025-06-13 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2612e2a6-d81f-374e-99c6-8186143d5ce3 | -10.9333 | -56.83649 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 18738ede-f3c3-3005-9700-7091cc1a6bd2 | -7.20407 | -45.3501 | 2025-06-13 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fb1b7c7-ac4c-3b84-b6f8-9230454e2359 | -13.09626 | -52.28616 | 2025-06-13 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb3b26ec-74da-3b51-9f8b-8fd0ed78b2ec | -11.79719 | -43.78882 | 2025-06-13 04:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2556bbff-5361-3e58-a2cb-3dba89d2848e | -9.88688 | -47.81334 | 2025-06-13 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82d79c87-83a2-3417-8544-ee2612bb7024 | -10.92053 | -56.8261 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3181194b-ac9c-3b2b-9ede-8fa24d1f04fe | -8.96862 | -47.9702 | 2025-06-13 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b4594c4-6411-3857-9a78-411fa4678169 | -11.81787 | -54.50303 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7d40199-7ae5-3bc6-ab2d-5754179a2201 | -10.69683 | -49.48979 | 2025-06-13 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4345c676-6ff8-3fae-b065-aa833951923f | -13.08944 | -52.28683 | 2025-06-13 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6b05478-32a1-323c-baea-adc19121b1ab | -12.00443 | -45.12965 | 2025-06-13 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b13e9ca-c037-3359-8f1e-910e38f42270 | -9.84923 | -44.6921 | 2025-06-13 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0c18d5a-f3a5-3b50-b861-6bcddb0ecaba | -12.09718 | -49.48734 | 2025-06-13 04:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97a0fd3c-4afe-3934-8674-4132e4e20e79 | -9.67122 | -48.76407 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 62d79dda-9915-3c20-a51e-705a9e2c1a9e | -11.37674 | -55.10881 | 2025-06-13 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5ff6458-a3c2-319f-ae8e-c8fc36208a0a | -7.64386 | -43.62823 | 2025-06-13 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac88ccf4-59dd-38ea-a2f8-789d9e191685 | -8.81615 | -46.68892 | 2025-06-13 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c520aefc-a65f-3452-966a-0f0b5309614d | -8.95487 | -47.27871 | 2025-06-13 04:10:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c57e0ebb-6110-3b8b-aa20-ff10f0891a49 | -11.56322 | -54.57695 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7b63c767-278e-3538-953b-453ac3426941 | -10.35135 | -51.99336 | 2025-06-13 04:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c60d743c-c11e-34a8-bfa8-fc708d653211 | -7.69485 | -45.78603 | 2025-06-13 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf03352d-aa82-3749-a03a-2344b388a245 | -11.80958 | -54.50327 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e67f2dba-d47e-32bc-b584-da61530f00fc | -12.10255 | -48.87605 | 2025-06-13 04:10:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e08054b-9a21-3a1c-aa9c-0d1d5559c537 | -10.69941 | -49.4982 | 2025-06-13 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9573692c-d812-3641-b599-8024db2ceba0 | -9.88754 | -47.80952 | 2025-06-13 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a97bebb-dc81-3c55-87b3-c5b7d8a21ca3 | -10.92461 | -56.84227 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0fcb87cf-8c9c-3037-9255-722054f0f0df | -7.44975 | -45.51873 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9f309e55-23c9-3155-8798-1bad4eba9f58 | -10.64856 | -49.41774 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d91312e0-9d99-32e0-a3a4-d8ad0303b317 | -10.18732 | -49.49813 | 2025-06-13 04:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c48b0f5f-8563-3c48-8aff-92fa7cab439c | -10.6415 | -49.43074 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ed6c00c0-bcbe-3c08-9864-fcc029396153 | -9.01576 | -48.16575 | 2025-06-13 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c61d6890-3cf0-3854-b589-87ec816d9bbb | -7.45349 | -45.51934 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9434acc9-0fd8-35a5-a65e-f00ea05e12a3 | -12.00582 | -45.12892 | 2025-06-13 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5975b5f0-e1b1-36c6-8b5d-2e577b77088a | -10.81029 | -54.0421 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4325f68f-35ca-3fde-bf2e-27f498145bab | -10.80417 | -54.04087 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f6a9a8d2-d154-3cb4-b7f3-bb8a77eccb12 | -11.56421 | -54.57196 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c3a06494-bec6-340b-b295-32dcfb9eb5e0 | -11.126 | -53.94608 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa713ee9-8db5-3633-929a-c01662ba9377 | -9.64775 | -48.56647 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bef7641d-3a85-3414-8402-50ef929f69a2 | -9.39173 | -48.41011 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f74375b-9060-3b63-ac0b-596e7849dde4 | -10.29565 | -52.84008 | 2025-06-13 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd9bdc7e-4de8-35db-be8a-2417b19f65df | -10.86393 | -54.30504 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fd6df66-dfda-3c46-8171-c1a9ce62e6ea | -11.18239 | -46.87967 | 2025-06-13 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README10.md)
