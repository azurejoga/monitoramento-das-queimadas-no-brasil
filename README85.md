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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d75ae35d-de56-3194-8ab2-c4dfbf0b07c8 | -5.9561 | -44.27071 | 2025-09-01 05:33:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 54beb088-7688-3ff4-82d6-28a5787b36e9 | -6.20166 | -43.33526 | 2025-09-01 05:33:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| edd2580a-4990-3902-ab3c-505b8184c5ba | -7.0798 | -44.36654 | 2025-09-01 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e855eb26-522f-314f-ac69-6b506b9901c7 | -9.67284 | -47.04178 | 2025-09-01 05:36:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e072bb90-6b9e-36ba-b5fd-41cb58f44375 | -11.89674 | -46.68568 | 2025-09-01 05:36:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f35eeed1-b78b-3183-a1eb-320c60d01596 | -11.04796 | -45.15398 | 2025-09-01 05:36:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| afe21f67-d598-352c-a8c0-b8daf72ebad2 | -11.03846 | -45.15252 | 2025-09-01 05:36:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9df7ae9f-fe65-3093-93e0-2459f0eb7aba | -11.80705 | -46.42755 | 2025-09-01 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| af912e16-9f11-3bc0-9cfb-d264170dfd34 | -11.05133 | -45.13301 | 2025-09-01 05:36:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 9787cee6-d6b4-3d97-b90a-93d4164c6232 | -9.63964 | -47.80891 | 2025-09-01 05:36:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 88d8b15e-6d82-37d1-bdf9-bb33120a4830 | -10.03993 | -48.09798 | 2025-09-01 05:36:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| e14f1113-ed4f-3398-bb46-8a22f6137e7b | -10.05191 | -48.09982 | 2025-09-01 05:36:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 8919eefd-d1aa-3a08-b66d-145f2ea64fa8 | -11.7969 | -46.42568 | 2025-09-01 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 66230804-0dde-3c5c-94fe-3305984d9612 | -11.89843 | -46.73915 | 2025-09-01 05:36:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 266c0e90-3941-337e-8dd3-b15d45ca808a | -11.9017 | -46.67952 | 2025-09-01 05:36:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 808e6f88-fe35-37e1-a92c-b4066481c613 | -12.0988 | -44.72164 | 2025-09-01 05:36:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| efc38d17-d3a9-37c0-9e6c-d112dd5fbacf | -8.84653 | -47.50159 | 2025-09-01 05:36:00 | AQUA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 94cbcac0-c378-3b36-b9b3-886298d6034e | -11.04695 | -46.98647 | 2025-09-01 05:36:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 195d6425-775d-3468-8b08-a804837bffa7 | -8.47511 | -45.16931 | 2025-09-01 05:36:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 70b70fa5-6fa2-3d2d-8571-592ac49d2d48 | -10.60901 | -44.31877 | 2025-09-01 05:36:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 8af4760b-061c-3465-b0ab-0bd13676ad28 | -11.05742 | -45.15563 | 2025-09-01 05:36:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7a65a170-0e1a-3823-a4b6-ea9811de6a3e | -10.24172 | -51.0982 | 2025-09-01 05:36:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 3e5a3f9b-074f-3a56-b252-cf120a64ed29 | -10.60751 | -44.32845 | 2025-09-01 05:36:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 472.1 |
| 923a3f15-d277-3830-902d-d10a904b4b01 | -10.60602 | -44.33815 | 2025-09-01 05:36:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 54051b11-10b4-3c3d-aabb-ae8d6f16a7a9 | -11.04017 | -45.14196 | 2025-09-01 05:36:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| b3b9d4f3-be4e-33b7-ad23-c6d763aa406a | -11.06051 | -46.90483 | 2025-09-01 05:36:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 570850ab-190c-3649-b65c-3dbd3a36e19e | -11.38184 | -43.6277 | 2025-09-01 05:36:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9fbcb30b-6010-3be4-b73e-4c12be712bca | -11.03068 | -46.85168 | 2025-09-01 05:36:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c14802d5-c027-3755-bc0f-ad044948771d | -10.89098 | -45.80648 | 2025-09-01 05:36:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a68e0cd3-06bd-3f09-80fe-504e4b5bcb48 | -8.84381 | -47.51803 | 2025-09-01 05:36:00 | AQUA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| cda1564e-73c3-3810-8e17-eae5e23ed03a | -11.04964 | -45.14351 | 2025-09-01 05:36:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 590.2 |
| 331234e7-fd88-3a87-a888-63ef72d7419e | -11.04466 | -47.00024 | 2025-09-01 05:36:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| dcda389c-5f9e-3a47-8fa7-1d51f92a0d10 | -8.20417 | -46.77432 | 2025-09-01 05:36:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| a5bde58b-74b0-3ea7-b9d8-c0b5a7c5dede | -11.04234 | -47.01421 | 2025-09-01 05:36:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 76f89b86-c0eb-3eae-87ad-dd283349d8b8 | -11.05827 | -46.91833 | 2025-09-01 05:36:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8074cd4b-4464-33c9-8014-2d1af9ee0ff9 | -11.80908 | -46.41505 | 2025-09-01 05:36:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 56c02605-616f-3457-8c40-0b8a78dc96ec | -11.03543 | -46.8583 | 2025-09-01 05:36:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fbb0da35-3e8a-370b-a76f-d328f95f813a | -11.04187 | -45.13141 | 2025-09-01 05:36:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2230b6f8-fc35-3879-8998-bd1a2a0cca8f | -8.82964 | -47.82597 | 2025-09-01 05:36:00 | AQUA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 52d7560a-199b-3f00-8b39-8750b7abc03d | -10.61533 | -44.32649 | 2025-09-01 05:36:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| eacc6614-7d84-3c79-9542-734c46b9e021 | -11.96421 | -45.84733 | 2025-09-01 05:36:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3b06ed68-bb49-3ece-9897-269d484bf8fd | -8.20167 | -46.78947 | 2025-09-01 05:36:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7afcecc0-fc2e-321b-ac72-67360c58b78f | -11.38138 | -43.57181 | 2025-09-01 05:36:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6342304a-516b-3a4f-b834-5c0c93068e7f | -11.04923 | -46.97274 | 2025-09-01 05:36:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4588e632-ee27-3e38-ae77-5ca60c1fbc51 | -10.05472 | -48.08298 | 2025-09-01 05:36:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 480d4bd1-255f-3197-a829-7f92d9732d94 | -11.37999 | -43.58087 | 2025-09-01 05:36:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4f6153cf-dc78-3a49-a3f7-a4b2a078ecfe | -11.0591 | -45.14515 | 2025-09-01 05:36:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 181d3ba6-3214-3836-98d6-0eb338858b03 | -11.03772 | -47.04199 | 2025-09-01 05:36:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 28b799c5-0620-31b4-898c-2597a1a903c2 | -13.32139 | -46.85191 | 2025-09-01 05:38:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ab86da2b-a0fb-39a0-b739-a4718cbec63c | -13.50531 | -46.98731 | 2025-09-01 05:38:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 471fc316-9f79-3082-8878-9ba1700c1977 | -13.37849 | -46.93415 | 2025-09-01 05:38:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6d96fec6-d576-3eb8-b16d-f57255f64dc4 | -19.51544 | -45.31493 | 2025-09-01 05:38:00 | AQUA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 76e61e6c-ab27-3ecc-b6ed-b70e072b88a1 | -14.74793 | -46.73472 | 2025-09-01 05:38:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2a009103-fd81-375f-8aa5-f359b750fdf0 | -14.74609 | -46.74603 | 2025-09-01 05:38:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 321be5fa-62c0-34d0-8126-fd0469b0163d | -13.29452 | -46.88729 | 2025-09-01 05:38:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ebd2a761-716d-3618-88bd-655545053867 | -12.80435 | -48.07829 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d1d08fb5-65be-3623-9696-b6c5dd810940 | -15.70227 | -48.91606 | 2025-09-01 05:38:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f2f3c545-a0e9-3cec-acff-9cbf8271e3e3 | -13.16618 | -45.28109 | 2025-09-01 05:38:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| c2e8006e-0f80-3bd5-8a84-8623135d6ca3 | -14.74418 | -46.75779 | 2025-09-01 05:38:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 199ac0b0-d0ba-3868-925b-df09166f3146 | -13.54817 | -46.96329 | 2025-09-01 05:38:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 10c62c7d-1d82-3ddd-9dde-56e7195b38bb | -12.3965 | -46.47001 | 2025-09-01 05:38:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1ea7942f-4fa4-3006-bd79-fb7abda3b75f | -14.04853 | -44.55779 | 2025-09-01 05:38:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bf90114b-7226-362e-9a48-d579f554ded0 | -12.5755 | -48.21384 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 998c94f2-058d-30cf-96fc-ededc353cda4 | -12.57137 | -48.22 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 08bb1cbb-730b-3f41-85a2-6a2cae850b3d | -14.75216 | -46.77155 | 2025-09-01 05:38:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 16b3f0f2-1121-3dd1-ae02-987da4457992 | -13.32351 | -46.83892 | 2025-09-01 05:38:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 13378757-6ccb-34b1-ae37-744f06fcf543 | -13.17711 | -45.27247 | 2025-09-01 05:38:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bdddfe78-ec7d-3605-98b9-0708cc04b27e | -13.51336 | -46.98183 | 2025-09-01 05:38:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a9ff08fc-0c8e-39ac-bd9d-830eb786a366 | -18.67157 | -52.58237 | 2025-09-01 05:38:00 | AQUA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| c3a03c35-7bcd-3da4-861c-987ffbe5b5c7 | -14.04707 | -44.56715 | 2025-09-01 05:38:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a378318a-a1f8-3bf3-937e-f43f5e9a42e2 | -13.52352 | -46.98431 | 2025-09-01 05:38:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| fa4ebb58-11a6-3714-805f-222ac45f0f5e | -15.59416 | -48.32954 | 2025-09-01 05:38:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 031bf91c-1123-327e-81af-3351bb8b55c7 | -14.75414 | -46.75925 | 2025-09-01 05:38:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| da9d6339-8145-3bb4-8025-428672666b32 | -12.39445 | -46.48226 | 2025-09-01 05:38:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 727a4b55-143c-3e80-93dc-2d3b765cee9d | -14.76654 | -46.75507 | 2025-09-01 05:38:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0e8e6069-ce0c-387a-90ac-6756956af6e5 | -12.5856 | -48.20608 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 209330b5-2166-36fe-9b21-060a7913d862 | -15.59161 | -48.3447 | 2025-09-01 05:38:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 54695af2-8dfa-3f98-9a24-5618905cbd8f | -13.37647 | -46.94632 | 2025-09-01 05:38:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 5dee25df-5452-3481-84dd-9616e71464e9 | -14.79027 | -46.73497 | 2025-09-01 05:38:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fc5637b7-0278-377a-86ae-a538dbeef815 | -12.97308 | -48.10559 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6f8fede0-7de8-3ca9-b5d0-bbda24f349cd | -15.70785 | -48.88453 | 2025-09-01 05:38:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 315d4134-221b-338b-b4db-914711f00b95 | -12.98439 | -48.10744 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f3e69229-d483-31f1-9893-2e119ef59f82 | -19.48232 | -46.58471 | 2025-09-01 05:38:00 | AQUA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 01bd4126-d9ed-3592-ae75-7c6f79915b23 | -12.85219 | -48.0706 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| a5fff07b-c660-3830-bb8f-3dd1b75a31ac | -14.75464 | -46.76518 | 2025-09-01 05:38:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 35.6 |
| ab977fbf-f6cf-3ae1-b888-9863e897b874 | -12.85472 | -48.05546 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2635d964-c291-3f74-a95d-ad41e4e045e7 | -15.73641 | -48.99041 | 2025-09-01 05:38:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| f5ff50cf-c999-30df-8094-3214ac8d80ab | -15.7251 | -48.98746 | 2025-09-01 05:38:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| c6db10d3-4c67-3722-9511-ee6fa27b86bd | -13.49504 | -46.98548 | 2025-09-01 05:38:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 764d0403-c17e-3860-9ae9-4fcb51cf42f4 | -12.86621 | -48.05614 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 3c767652-a039-313c-bb3b-725493dd1ee7 | -15.72789 | -48.97148 | 2025-09-01 05:38:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c2f09af1-37f6-36af-884d-839ebd2b8bb0 | -12.39559 | -46.47668 | 2025-09-01 05:38:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8c55c219-2ca2-39e3-9755-8262532d043d | -12.9419 | -48.09216 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8a37fa22-6785-358f-a685-9f9c2971fc0b | -19.48063 | -46.59526 | 2025-09-01 05:38:00 | AQUA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 4ef119fa-fb46-3bfb-92c7-833e517ab833 | -14.75667 | -46.75314 | 2025-09-01 05:38:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ad684e33-72bd-3fb7-a9e0-1aadf4aefc88 | -19.49154 | -46.58633 | 2025-09-01 05:38:00 | AQUA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2a179a2e-e39e-395b-bcb7-4058edd31ae4 | -13.29243 | -46.89989 | 2025-09-01 05:38:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 50b74bc6-ac1d-34a7-9a9b-50d58f5059b4 | -15.59367 | -48.35141 | 2025-09-01 05:38:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| d2c69bfa-4ddb-3634-a97b-ec9428032810 | -15.69658 | -48.94815 | 2025-09-01 05:38:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d4bbfba0-c4c2-3cd9-b166-75d7f01d1a5e | -15.70516 | -48.8997 | 2025-09-01 05:38:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |


[Clique aqui para ver as próximas entradas](README86.md)
