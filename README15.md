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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82f886dc-ca93-3ae7-8ae1-0b295eb17c70 | -7.53996 | -36.73669 | 2025-08-23 03:38:00 | NPP-375D | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 06974164-53a4-36da-8e1a-8fcadd998633 | -8.03994 | -47.31169 | 2025-08-23 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c02d4542-97d3-3e86-b623-254f038d6e70 | -3.81609 | -41.55376 | 2025-08-23 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a6805e0b-c222-3ce0-a2b3-cbafaf5bd6a0 | -7.60784 | -44.37169 | 2025-08-23 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfeb7bc2-4134-3097-bc1d-2757026c866e | -6.4797 | -43.46547 | 2025-08-23 03:38:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58d005dd-8e6b-337b-bfed-82ae9dee9a11 | -5.89189 | -43.44901 | 2025-08-23 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6317dafe-1266-3e6a-ba9b-fbd75ecac2b8 | -7.63865 | -45.23631 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc54abf1-52e8-3062-ab90-54c7d9322333 | -6.41947 | -41.21343 | 2025-08-23 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d98becc5-811d-3847-9815-64a7c1411e0a | -7.6264 | -45.24197 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 09fe21e4-5370-3ffc-beea-bf682c1ca53a | -6.59854 | -44.56898 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 3a9e248a-223b-34b0-81ea-77d732c1df50 | -5.48957 | -42.16082 | 2025-08-23 03:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3f63a042-0103-3e6f-9df5-913e04cec752 | -3.81809 | -41.57338 | 2025-08-23 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0886b6d5-03eb-3cc6-8a88-edef02f72827 | -9.44199 | -47.65352 | 2025-08-23 03:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6357afb0-5b9f-3b51-84dc-6cab191d317b | -6.41465 | -45.48513 | 2025-08-23 03:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27822142-7bb8-31db-95c5-e2a604203fb9 | -7.02428 | -44.6457 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 3a4f2052-cb12-3089-83ff-e5ffdd4d7e30 | -5.83432 | -45.16431 | 2025-08-23 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee654dfd-955e-3ab5-8947-5cf5016904b7 | -4.52736 | -38.22853 | 2025-08-23 03:38:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 53a5a87a-86b4-3b5b-a09e-74e2ef0b2984 | -6.93371 | -39.56566 | 2025-08-23 03:38:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 79f5359e-c1bb-3f9a-8da8-32b40a952b00 | -9.82979 | -46.38401 | 2025-08-23 03:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e71bc61-8b15-38cd-85c3-cfaafb2dd4dc | -3.98969 | -43.24121 | 2025-08-23 03:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d52d5e16-c2db-3b80-b93b-bfa9765d07b9 | -4.14281 | -46.46023 | 2025-08-23 03:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eddff455-63d9-30fb-a090-0b112d7a11c5 | -6.6047 | -44.56658 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 41182d18-89f5-3ddf-ba61-919ede03d79f | -7.13722 | -44.17003 | 2025-08-23 03:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba054daa-9870-34fc-aab4-bdcdfff84788 | -7.02436 | -44.64972 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9492de9a-2fe7-3d53-86b4-ffea44ec2cae | -4.1738 | -40.71784 | 2025-08-23 03:38:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 81e40f40-1acf-34db-94b3-7ff1e6cc5db1 | -9.45031 | -47.65673 | 2025-08-23 03:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 00cda05f-611a-3a94-9099-c62aee709348 | -7.08021 | -44.06086 | 2025-08-23 03:38:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa2a9ce1-2e62-32ea-971c-b5c8c305f3a0 | -6.18425 | -45.43407 | 2025-08-23 03:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c1edc007-50d4-3371-9637-56d240283617 | -7.02354 | -44.65417 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4a27b04c-419c-3a54-a29d-fa42abb8753b | -6.9544 | -37.39398 | 2025-08-23 03:38:00 | NPP-375D | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 581aa3d2-7314-3ce2-80cf-35a5dfa35199 | -7.60608 | -44.37166 | 2025-08-23 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc234df5-eac2-30bc-9894-d8bba038383e | -4.34158 | -46.46925 | 2025-08-23 03:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7b10c93f-b7e8-3549-9d11-0abf06d4be06 | -9.44891 | -47.65492 | 2025-08-23 03:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fbbf79a8-9f6d-3c54-b00a-e5f487627ee1 | -14.6703 | -54.9349 | 2025-08-23 03:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 87854538-1273-3950-8351-e725179cd8c3 | -9.9681 | -60.1743 | 2025-08-23 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 31bc9554-95b0-3900-b58c-e6245b9e8469 | -8.5759 | -62.6133 | 2025-08-23 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 0716a07b-c03b-3352-9353-d24c06e8383b | -4.3482 | -46.4695 | 2025-08-23 03:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9493ef86-752b-3a52-b3c4-8f6868884e03 | -15.2288 | -53.8481 | 2025-08-23 03:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| b541f62f-6c68-3949-baa1-292db2b7f4cc | -8.5944 | -62.6126 | 2025-08-23 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 9561b16b-7e18-3525-81f2-61af4781ebb2 | -8.5943 | -62.6315 | 2025-08-23 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| dc493ca1-211e-3547-86ab-98de541c5b0c | -9.9493 | -60.1947 | 2025-08-23 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 252.5 |
| 2e8d76dc-4e20-3e82-a96d-63d2a08bc5bf | -14.2936 | -58.5249 | 2025-08-23 03:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 3ae20921-834a-3d0f-8953-21277f5c2144 | -9.968 | -60.1937 | 2025-08-23 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 52912329-f7b0-34f8-b618-6a6e92447c29 | -15.2284 | -53.8691 | 2025-08-23 03:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 5319d2a0-f721-3931-baa5-1c9ada466cc7 | -6.6044 | -44.5624 | 2025-08-23 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| a09c22c4-4fda-34b5-9184-fe100f7dd3fb | -9.5177 | -60.5653 | 2025-08-23 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 37e4e319-3cbc-34c4-a3ed-3de4c33413f4 | -9.1897 | -59.6171 | 2025-08-23 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| a19092f1-4d6e-30f8-9841-58e552afd49c | -9.518 | -60.5268 | 2025-08-23 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f63da341-cfa3-3360-b486-e25baedcc383 | -14.6706 | -54.9142 | 2025-08-23 03:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f55cf915-d8fa-3b8c-ae60-72c788bb1809 | -9.9495 | -60.1754 | 2025-08-23 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 153.0 |
| bbc9a5f7-d08f-3d3c-beb3-d6c1bd2fe45d | -9.5179 | -60.5461 | 2025-08-23 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 968bb906-fb62-3aa1-baa8-fba739f6491c | -15.07755 | -48.50726 | 2025-08-23 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cafeb778-df85-3d22-bbc8-70c1789055cc | -15.24555 | -40.27911 | 2025-08-23 03:40:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| adfedcb0-6aeb-3cab-a884-c9ff3b5f169e | -12.95776 | -46.29912 | 2025-08-23 03:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a2b3b2e-15af-3716-a0cd-7380513c49cd | -15.90764 | -42.30371 | 2025-08-23 03:40:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e74f9df6-1a00-3d2a-9b91-a67981a5a919 | -15.05516 | -48.46736 | 2025-08-23 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6a1c1a2-1fbf-3f51-afbd-8d7a975a1f99 | -17.26974 | -46.77129 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f8378526-2083-3292-a5d5-f702cebbef29 | -13.48852 | -47.03064 | 2025-08-23 03:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3955a756-109a-3aa7-b5b2-26ac57d0c603 | -12.77439 | -48.71353 | 2025-08-23 03:40:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5218e097-9c5e-3d04-87f2-dada775a306c | -13.64695 | -46.88208 | 2025-08-23 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b40fe10d-b8ce-336a-9e87-264d00a730cf | -13.64294 | -46.88058 | 2025-08-23 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74156332-b91c-3c8c-8bd8-91ca32f506bc | -18.26024 | -45.57482 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 445000e1-c58b-333b-8b66-bc1218d71bda | -12.94339 | -46.30786 | 2025-08-23 03:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7989b17-8b97-3d19-9260-eb103fd587f1 | -13.37934 | -46.22167 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 05a2927c-6d77-3786-b6fe-d1417bd37c94 | -11.12843 | -44.76839 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f31a89ca-4ad3-3922-aa16-89774771359e | -18.2505 | -45.56919 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fb1ffcc-3b0f-337c-945d-8a339334f450 | -12.67177 | -47.81268 | 2025-08-23 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83880266-f181-345a-ba47-bef270097476 | -14.80949 | -47.94878 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ab86e6e3-2c8b-3bc7-9ed0-41d351ea302d | -15.71167 | -41.93061 | 2025-08-23 03:40:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 1f3b6fda-db1e-3ae4-ac43-07cb79f15ae3 | -14.78607 | -45.4917 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2ff457b-c6c0-3c16-976d-83d8dd5b60f9 | -11.1186 | -44.75843 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 789f85eb-d080-3711-9ca3-b6a9f0f9499e | -15.20621 | -48.70868 | 2025-08-23 03:40:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 68a26c09-199b-3d24-b26d-b3a09c591509 | -17.69066 | -48.50196 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e17b4b09-fe95-3825-8788-7133ae9ae531 | -17.59601 | -46.57023 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f38f17d-3113-3cf1-a952-5ee80cf37301 | -13.39603 | -46.35291 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ffc71c3-93eb-303e-86f4-22b7395fec6c | -12.94213 | -46.31406 | 2025-08-23 03:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3627ce15-f5eb-3b8d-95dd-deaa6a40591b | -14.94418 | -48.00912 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 19464e43-7092-37c5-ae27-0c2d7e82a1ee | -13.13051 | -46.9033 | 2025-08-23 03:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 600d03ad-8c4c-3644-b0cb-ea7118fa0b22 | -15.53568 | -41.69219 | 2025-08-23 03:40:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 992a5c35-9d95-3680-854c-c33ad45b2e69 | -12.98835 | -45.22554 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 00070b48-dded-31cd-9513-379b65d558e7 | -14.79633 | -45.49825 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b254892b-42ae-3c5a-b622-1088e62944f3 | -18.27445 | -45.5852 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2e22d53-ab58-30fe-9f0e-f7c30b050e0f | -11.12352 | -44.76337 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f16f4e2-371a-3f97-b9ab-9e53add7fdd3 | -15.71181 | -41.92804 | 2025-08-23 03:40:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| e48621ea-4013-3c21-b41a-3e8f91ac996c | -13.04152 | -46.32465 | 2025-08-23 03:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee750dbf-fefc-302b-9562-55a12c9bd883 | -14.82696 | -47.96187 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91cf3745-f47c-388e-8f68-d622c20484c7 | -18.25035 | -45.57479 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 487ab178-ed6c-3430-a064-21d564f5b694 | -12.78136 | -48.7149 | 2025-08-23 03:40:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 01c3b6e5-3e9a-3fa8-9b6e-e83000708efc | -13.16662 | -46.91727 | 2025-08-23 03:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e985824e-7d08-3f58-a2f7-154775ac1de2 | -11.32488 | -47.84399 | 2025-08-23 03:40:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2181934-7a27-3ef3-8bc9-28aa6428540e | -13.7228 | -44.40056 | 2025-08-23 03:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e52f4e03-fb99-3f7e-a8fa-eb47828a65d0 | -13.37334 | -46.22065 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d704e239-a5fd-328d-ac57-6450313ddb6f | -17.5855 | -46.55514 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c157ccea-d005-3965-afa2-2fb777e8d6fc | -18.29524 | -45.53808 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c50cfeb-d70d-359b-8c41-e8b99b528bac | -15.05397 | -48.47292 | 2025-08-23 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f52d9d4a-1113-34b3-a56e-a99403b8acc2 | -13.37232 | -46.21708 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e96f4838-1c32-34bc-80b3-4ee6fc99862d | -18.25572 | -45.57034 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84decaef-3cb1-3e30-8c70-796eb36c5442 | -15.24401 | -40.28057 | 2025-08-23 03:40:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d66f4e86-9f11-397f-83af-671c5ef802f2 | -12.95697 | -46.30299 | 2025-08-23 03:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3da836b-65bd-30dd-992a-8460854fe4b5 | -14.78362 | -45.47509 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
