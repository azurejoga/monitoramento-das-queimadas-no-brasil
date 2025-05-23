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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| deef47fa-4626-392e-9f9c-7886afdb6b46 | -12.0621 | -47.3349 | 2025-05-23 00:07:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6dc66ec-0c6b-3c4c-b85d-981957fe7c2b | -15.4185 | -41.416401 | 2025-05-23 00:07:00 | METOP-B | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11e43899-a8bd-306d-a58c-9c32962bdaee | -6.9323 | -42.788101 | 2025-05-23 00:07:00 | METOP-B | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c6d20d35-6395-34a5-98d2-74e082844ea6 | -10.4885 | -42.4184 | 2025-05-23 00:07:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 79f831fb-26c9-39cc-be80-30f86bad6601 | -15.1357 | -43.959202 | 2025-05-23 00:07:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 25f32589-4e51-3fb7-a8f3-0fcfa3197577 | -23.120899 | -47.485298 | 2025-05-23 00:07:00 | METOP-B | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4281eb8c-eff3-3205-80af-35408fbdfc7e | -13.9748 | -55.951199 | 2025-05-23 00:07:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7cf34a72-0791-3812-b36b-0ef7b1ad0e73 | -14.6752 | -45.1049 | 2025-05-23 00:07:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7d1f405-2ab1-351d-ad09-ab0cf95001e3 | -11.9668 | -44.1581 | 2025-05-23 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03a5f4a4-0365-3377-9c46-4a765015b5ae | -7.9618 | -49.686298 | 2025-05-23 00:07:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 033010ed-fd04-3401-8399-b7597d93386d | -10.6463 | -49.464001 | 2025-05-23 00:07:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb7911d0-6288-3b56-9611-fd1a3527402b | -8.7767 | -49.041801 | 2025-05-23 00:07:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1908c419-a2df-377e-a7ea-72584d32f6db | -13.9706 | -55.9837 | 2025-05-23 00:07:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| feae48d3-a77b-3688-8d1f-65028841e4bf | -8.7787 | -49.0508 | 2025-05-23 00:07:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b99416e6-77e8-36de-9540-0e4d6320adc5 | -5.5662 | -45.205799 | 2025-05-23 00:07:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84bcc28b-f3f6-3ace-9ec9-b05f4523e78f | -6.2296 | -43.364101 | 2025-05-23 00:07:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 505a1810-bca3-30b2-a9df-88352888ce6a | -12.0719 | -47.332699 | 2025-05-23 00:07:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ce40ac1-ce83-3ec8-9548-b31cf0bc0edc | -9.0422 | -47.7486 | 2025-05-23 00:07:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 938b0894-1d0f-353b-a807-167b2ccba5a8 | -8.1202 | -46.4473 | 2025-05-23 00:07:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4db7e4e1-1cbb-36ed-8915-182608baeae9 | -12.2902 | -52.478802 | 2025-05-23 00:07:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00b44303-2f91-3c11-b147-e5ac78574254 | -7.1985 | -43.093201 | 2025-05-23 00:07:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c5f9e710-bd05-39d6-ba63-e58056264d00 | -11.5524 | -47.445202 | 2025-05-23 00:07:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81b4cb36-6242-3328-8ffb-1e264444ee7f | -11.7911 | -44.2938 | 2025-05-23 00:07:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3cd5c257-9177-3b53-b493-9075d9ad493a | -14.0373 | -53.345798 | 2025-05-23 00:07:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a688e22-26b6-3641-b41d-713fcf35b615 | -12.0604 | -47.326801 | 2025-05-23 00:07:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47747f30-351f-3f74-8691-7e4e2fd5edf2 | -7.1959 | -43.126499 | 2025-05-23 00:07:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6c309b6f-4f44-314b-a13c-2e6ee6e19163 | -12.8403 | -47.380501 | 2025-05-23 00:07:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98cb1dac-9afb-351c-af18-f3f4d3e18e65 | -10.706 | -48.820599 | 2025-05-23 00:07:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 301384ae-6efc-33ee-a920-57da0740ba60 | -7.0598 | -44.928799 | 2025-05-23 00:07:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 896c6d2d-a259-3be2-9f0e-7e3676ff461c | -7.708 | -45.658699 | 2025-05-23 00:07:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48545cfb-3408-3fea-b381-600a45d5eaf8 | -10.6365 | -49.466099 | 2025-05-23 00:07:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48a07e4a-dde6-39f3-bea7-cdf82e9461ee | -5.5647 | -45.198898 | 2025-05-23 00:07:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 994ceea4-9929-3c14-8c41-fbd57a12c10e | -13.9802 | -55.981998 | 2025-05-23 00:07:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a938132b-8761-30d5-9d1c-7ccbe1073c5f | -11.5507 | -47.437199 | 2025-05-23 00:07:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2ba31c3-ff31-3ef8-9fe8-05aba892a801 | -7.0695 | -44.9335 | 2025-05-23 00:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 0d54bf7e-2272-31de-b6c4-7e067d6e9d57 | -12.2943 | -52.4995 | 2025-05-23 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 028d9fa8-d716-39de-8731-10c3a47f1e87 | -20.8588 | -53.7605 | 2025-05-23 00:10:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 922c0561-1249-31f9-ac03-442f6565388a | -13.9818 | -56.0151 | 2025-05-23 00:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 286cd157-6001-35c8-a721-4e52449bcd6b | -9.9639 | -49.8002 | 2025-05-23 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| f1394c87-ecdb-338b-a0f7-9ee3ed22986a | -20.8593 | -53.7387 | 2025-05-23 00:10:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 44b952a5-f9f1-3b24-a94d-4946f7774f52 | -13.9821 | -55.9947 | 2025-05-23 00:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ebf220ed-2131-3c45-8111-33f31410c0af | -12.3324 | -49.9857 | 2025-05-23 00:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 0a1d6996-ecc8-32e3-9f5c-5964f5eb0213 | -6.2224 | -43.3693 | 2025-05-23 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| bb45b76b-d695-39bb-a168-ab620fc839ea | -11.7988 | -44.2733 | 2025-05-23 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 1cb66c60-8c25-3b8b-8324-435615efdfeb | -11.7984 | -44.2967 | 2025-05-23 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 308e8fe0-66d4-3afc-8564-e550a3ba63a5 | -9.0291 | -47.7452 | 2025-05-23 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| d938abe9-51d5-3f49-90a3-60add323fafa | -23.12571 | -47.49226 | 2025-05-23 00:13:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.8 |
| 6bd0c0e6-cae0-3dca-835d-c244de2ad94f | -23.1247 | -47.49881 | 2025-05-23 00:13:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.9 |
| c19a4423-031b-3f12-a77e-623fcf24dd34 | -12.40997 | -42.52866 | 2025-05-23 00:16:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 46211ddd-7bf8-32b0-8eeb-d6504503b480 | -12.84722 | -47.39144 | 2025-05-23 00:16:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| c2ea5c1a-e2e8-3c64-9b63-e8fa08908011 | -15.42683 | -41.41508 | 2025-05-23 00:16:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 08f8a091-3fa1-3347-b56b-5463022eeff5 | -12.09778 | -40.59504 | 2025-05-23 00:16:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b38cf030-05fd-3c58-8a3e-02b318741f1f | -15.14273 | -43.97193 | 2025-05-23 00:16:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9c9ca3b0-4627-3223-9d43-4117b76f9f1e | -15.14126 | -43.96014 | 2025-05-23 00:16:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 49e1fda9-7e41-339e-a66d-23bf2d1e821c | -12.84887 | -47.38585 | 2025-05-23 00:16:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 1ef191fb-b792-3af5-bf40-0ff7a0d5b93e | -15.74384 | -43.48515 | 2025-05-23 00:16:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eab5bcf8-518a-343e-a935-581ddfda824f | -12.85102 | -47.40496 | 2025-05-23 00:16:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 68423035-7169-3140-b746-7a1f12cdd6cc | -15.42559 | -41.40586 | 2025-05-23 00:16:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 429cefbb-0374-3f2c-a6c9-e1a7c9d84c29 | -12.41654 | -49.96767 | 2025-05-23 00:18:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 1f79bea1-4f32-31af-8c18-f5ac5b09c8a2 | -11.7864 | -44.28964 | 2025-05-23 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| a6e18760-93ba-37c0-9e93-0b4c11143a00 | -6.9482 | -42.79458 | 2025-05-23 00:18:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 80a35da9-614b-3342-aadf-78812f1fec37 | -7.21406 | -43.12595 | 2025-05-23 00:18:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 5f9af882-9fcf-31fa-8b75-ee8f58701c40 | -12.34564 | -49.98798 | 2025-05-23 00:18:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| bc8e802b-12e3-3ac1-86c0-55dd23065a75 | -6.23113 | -43.34911 | 2025-05-23 00:18:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 16c2dce7-7834-3b3e-8a10-6dea26b681bf | -11.28794 | -41.8632 | 2025-05-23 00:18:00 | TERRA_M-M | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 2e93add5-cec6-3423-8333-7272ee4f5ace | -8.67659 | -48.28329 | 2025-05-23 00:18:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f792d3cd-d655-3796-ad96-633a549f160b | -7.23945 | -43.11323 | 2025-05-23 00:18:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 95ba8b51-00aa-365a-9219-e799dd6b55fa | -11.78497 | -44.27861 | 2025-05-23 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 94408294-5060-3293-b2eb-86d7b80340ab | -12.27478 | -44.59637 | 2025-05-23 00:18:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5af3548d-197c-369c-b1e7-2ddfa301f020 | -5.58048 | -45.1951 | 2025-05-23 00:18:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 768e6ce0-55ff-30c0-8152-3ccecd230d34 | -8.1288 | -46.4596 | 2025-05-23 00:18:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 22424e67-279f-35a1-acb7-3b729907114d | -10.48969 | -42.41777 | 2025-05-23 00:18:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 1b1558cd-c53b-3944-9b18-fa5877e187b6 | -7.20642 | -43.13617 | 2025-05-23 00:18:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 1412e4d6-4a36-371f-a0bd-416b87d20e04 | -5.78875 | -43.61586 | 2025-05-23 00:18:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a3caaa9-fcfa-3f87-8ea0-f630bb2dd367 | -11.97197 | -44.15168 | 2025-05-23 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d7ec0e1a-1334-33ad-96ba-11f8baed2add | -7.23566 | -44.71656 | 2025-05-23 00:18:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 67e32a02-8f10-35eb-a59c-58d6c8794754 | -6.22471 | -43.36823 | 2025-05-23 00:18:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 7f2c3043-4011-3745-9003-6a23af5a294a | -11.9734 | -44.1626 | 2025-05-23 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d44b8dce-79b3-387e-b41b-877783547a8f | -9.96701 | -49.83792 | 2025-05-23 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 59166f5a-76a4-38e4-bb23-28075270fcfd | -11.56192 | -47.44365 | 2025-05-23 00:18:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 12ae89ee-39d7-3762-acb8-ab2c7aa3f900 | -6.22103 | -43.34143 | 2025-05-23 00:18:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e6bc820-449b-38b5-ba5c-232ca2a4bbbc | -10.71254 | -48.83974 | 2025-05-23 00:18:00 | TERRA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| a592aa9f-6ac3-3fef-a0f9-f04c3e832600 | -9.25248 | -40.95258 | 2025-05-23 00:18:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7e53f900-7f97-3ea1-9150-b839703cc96b | -8.67564 | -48.28993 | 2025-05-23 00:18:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f8826c2c-cd59-356f-97d1-13688f402058 | -7.07173 | -44.94026 | 2025-05-23 00:18:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| eeb42d5c-2733-3f0d-9417-bde70f7fa5b5 | -11.7947 | -44.27726 | 2025-05-23 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5c551015-f680-3b06-9dd5-b0ab8b4d6aef | -12.41928 | -49.97285 | 2025-05-23 00:18:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 9471947b-bad1-3868-b8b4-1fd896ff35bc | -12.33082 | -50.01387 | 2025-05-23 00:18:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| cc5f392b-a53c-336a-950b-4ec4f7d493e5 | -7.21529 | -43.13491 | 2025-05-23 00:18:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 759defc5-3b5f-3b72-a564-67ad00e65769 | -7.09004 | -44.3858 | 2025-05-23 00:18:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b3d7df63-4385-3671-b1e1-c0005bb49389 | -9.9623 | -49.81785 | 2025-05-23 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 8bd891ca-3058-3029-b255-5d0e67fda99b | -7.20519 | -43.1272 | 2025-05-23 00:18:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| c48dad09-3e31-3dfa-98b8-312b67964d7c | -11.51248 | -48.55183 | 2025-05-23 00:18:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ff58d976-6b0e-3763-9eea-82e4a805b3a5 | -7.70768 | -45.66179 | 2025-05-23 00:18:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7bad4f80-359e-311d-80c1-bd7a694f4f70 | -12.07319 | -47.34461 | 2025-05-23 00:18:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| a5148afe-633b-3e8f-991d-ee0d0f865168 | -10.65518 | -49.49456 | 2025-05-23 00:18:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| e77682d9-a416-3418-ba77-88a84c871fc9 | -11.5641 | -47.4616 | 2025-05-23 00:18:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e8b011a2-b8a4-30a0-8c78-8a5ee8d23e23 | -9.03889 | -47.74729 | 2025-05-23 00:18:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 8449b1ff-2292-396e-97c3-cf01107fc5b6 | -4.82102 | -44.35599 | 2025-05-23 00:18:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e82c0882-7b17-33bc-91e0-9f408216cbc2 | -10.49857 | -42.41651 | 2025-05-23 00:18:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |


[Clique aqui para ver as próximas entradas](README3.md)
