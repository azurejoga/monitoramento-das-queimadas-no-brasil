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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a34e896a-3e38-35cd-bcff-9c144f7911b7 | -4.25399 | -48.60199 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5e16a01-483d-3247-b05e-ae80aded162e | -8.79996 | -43.0595 | 2025-09-22 04:17:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9a49de52-02e4-37c5-96a3-e323aa64fe00 | -13.50531 | -47.25903 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7ca2749-3e44-3ca4-91b5-9ecebcc43bf5 | -7.96423 | -43.9005 | 2025-09-22 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cab95b66-ef28-3493-9128-c7def5e27b30 | -7.60951 | -44.44398 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dbe043c-43d1-32cc-8cee-ea7bb0e57714 | -11.64583 | -44.31656 | 2025-09-22 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 717be114-cfbe-3865-b5f6-0a117f2bd02e | -7.35063 | -44.55628 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 971730f3-956d-323c-ab3b-8a013aa57651 | -11.73665 | -47.80822 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f037e19-2b68-3ad5-a466-fc71137e0679 | -14.07735 | -50.15403 | 2025-09-22 04:17:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d2cc8bf-c8a2-3cc9-8c44-7cb04c2cf227 | -8.20571 | -42.20912 | 2025-09-22 04:17:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8906512a-2593-3ed0-b5f1-3d621f899391 | -7.02451 | -46.30994 | 2025-09-22 04:17:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ae89751-675a-3999-83a8-55b66f1d15b9 | -6.61317 | -44.60178 | 2025-09-22 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 122c0252-ea13-3918-b4f0-b8f63c6d6224 | -7.22978 | -43.75503 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc88134e-f4c1-3fe4-b55c-4b884fedcb8e | -14.48186 | -46.50406 | 2025-09-22 04:17:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39bec1a3-73ed-39e6-ade3-08fc5bee451b | -14.9774 | -44.40988 | 2025-09-22 04:17:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f33310c-6669-3e22-b7b2-e4c4b611b295 | -13.75066 | -43.72808 | 2025-09-22 04:17:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a65fc9d-1054-3b68-9e45-30092d01195b | -5.40579 | -38.56902 | 2025-09-22 04:17:00 | NPP-375D | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a8854efa-b5ce-3cc9-aee5-4b5910e4a111 | -11.55339 | -48.59189 | 2025-09-22 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15068abb-5609-3517-86f2-3435b0b626eb | -2.25411 | -47.88098 | 2025-09-22 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1f85a09-652d-31f3-b2d2-e092230f568d | -12.34993 | -44.09697 | 2025-09-22 04:17:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5a23934-2e85-3cf4-827b-afd9e9151992 | -5.64254 | -45.95166 | 2025-09-22 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aa46bf24-749a-30c4-a734-f67add3d3d99 | -6.22643 | -44.65997 | 2025-09-22 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29f9d1da-cd02-374f-afff-2280d4dbf8ee | -6.44563 | -45.69887 | 2025-09-22 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 761e358b-9a17-350c-a18a-063ad1a86175 | -6.03788 | -44.13863 | 2025-09-22 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dfb283e1-4134-32c3-b1fd-ec99a33404c5 | -7.58912 | -45.50117 | 2025-09-22 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03a372b3-d3c3-3483-8db0-7e9b0f152238 | -4.56788 | -41.50459 | 2025-09-22 04:17:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 73e81e92-9159-36b9-a3fe-249fa8737534 | -11.55908 | -48.59011 | 2025-09-22 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af079be7-4b68-38d5-b81a-ac5388a3ae27 | -5.1113 | -46.16897 | 2025-09-22 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc023ebb-602d-3e76-8e0b-fbe1e353315e | -7.36528 | -44.55122 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41c5fcfd-61d5-3a9e-bca6-b071140aa28d | -12.71125 | -47.70026 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fd0be66-ef41-3a11-836b-9a3227116fb8 | -11.66551 | -47.49955 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 799df7fe-64ca-32d9-9661-7054cd171b36 | -14.44366 | -46.52395 | 2025-09-22 04:17:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b4bcbbf2-f5dd-3387-86b9-3cc9b0d036fd | -13.74959 | -43.72848 | 2025-09-22 04:17:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ca8a012-e10a-3edd-b4a4-5afbe9928998 | -12.08349 | -44.85871 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64cdc515-5cb8-339b-8482-bd4ad3039f9f | -7.35304 | -45.62164 | 2025-09-22 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c3c888e-9625-373b-9abe-0c32a7a0f8ff | -11.46862 | -46.93515 | 2025-09-22 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec241272-320f-37cf-881f-90064722cd6a | -13.71096 | -47.58121 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e27a14e7-1e93-3c30-8832-00a7c9574c08 | -12.34937 | -44.10051 | 2025-09-22 04:17:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 886c0836-f5d3-3ebf-a070-7e45b5d06578 | -13.72627 | -43.91013 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b0a9dd4-3d31-3429-87d3-b940329017ab | -3.13652 | -44.42131 | 2025-09-22 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a5d11e9-d3d1-3ee2-95af-3e3709b5a252 | -0.94975 | -47.35292 | 2025-09-22 04:17:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1db7c47-f95d-387c-8f85-b4c483287e4b | -11.42524 | -55.01541 | 2025-09-22 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d22a4e21-1687-38b5-b2e8-10a977957b6b | -14.97572 | -44.4207 | 2025-09-22 04:17:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c47886d-4ef0-3fc3-9953-d4226d8ec2df | -7.22367 | -43.75047 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a652dd0-6912-3b90-a16b-2700b4147c23 | -13.61613 | -47.41404 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ea71701-6639-3c8c-8efe-cf6dfe4bc771 | -7.96145 | -43.89648 | 2025-09-22 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0e595cd-6650-389c-b3b5-0f67b1065e5d | -7.60136 | -45.49145 | 2025-09-22 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b502dfa-c255-385f-a60f-7acf813ae37a | -7.50809 | -43.68105 | 2025-09-22 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c1996d1-8819-3195-85c8-e4e7357425a8 | -5.57121 | -42.12632 | 2025-09-22 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 085e5e3b-12a4-3597-916e-195e50d7df7a | -12.71414 | -47.70515 | 2025-09-22 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 452d9556-0ebf-3213-a9d0-9da8e499f484 | -12.43044 | -45.14933 | 2025-09-22 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0341559-6f7d-3313-a218-3eecca885f4a | -12.0837 | -44.79322 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 235f7c55-30a6-3ada-b59e-af94bcb4cced | -12.68612 | -46.84159 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4f31eb4-6933-33de-aa37-6a4ea54063a1 | -15.0961 | -43.83854 | 2025-09-22 04:17:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7debb23-137f-3e33-af9b-5068050cb836 | -14.26639 | -44.38025 | 2025-09-22 04:17:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c07a377-cde4-3ba2-99c6-af60a04a65cd | -15.55094 | -41.01722 | 2025-09-22 04:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e859e164-6f1c-3cae-9a0a-3533a51d501d | -3.8567 | -40.34241 | 2025-09-22 04:17:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc90a49c-941c-3974-8e93-0e8e789fc13d | -11.77737 | -43.76173 | 2025-09-22 04:17:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f54cdcc-518c-3576-8f4a-e98cc795dfcf | -7.227 | -43.75101 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76a67d46-2cbf-3cb9-902a-c8c2f0d93cbc | -1.19991 | -46.15346 | 2025-09-22 04:17:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d189fe3-b8fc-3321-b9c0-eed029994ede | -14.85118 | -45.47318 | 2025-09-22 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c7c1efb-1b61-3c97-a978-9f9ea9d27b6b | -5.06562 | -40.4734 | 2025-09-22 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 87fc3ab6-6952-39e5-bfe6-b5b3df4587a7 | -7.23367 | -43.75208 | 2025-09-22 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 187af7ea-c3e0-37d7-b408-89bce4832ba1 | -7.20577 | -40.24695 | 2025-09-22 04:17:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4f526762-7e88-3cb0-9f26-5d3b6315b8db | -2.91344 | -40.39034 | 2025-09-22 04:17:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6c2731c0-3d3e-348e-8ca4-56e298a2835e | -13.73724 | -43.78606 | 2025-09-22 04:17:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb8022e7-571c-355e-845a-53100a7ec642 | -14.35241 | -47.78461 | 2025-09-22 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bcde2f42-c1e2-33d7-b2c0-57f844c2677f | -5.57011 | -42.13336 | 2025-09-22 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 4c45c5ca-48ec-3d3f-8d7e-4accd3caa9d7 | -5.33454 | -44.82302 | 2025-09-22 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08dd90de-f10a-3ca1-9c64-a68d1bfcc564 | -5.81684 | -43.87535 | 2025-09-22 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14496c85-baf0-39db-a6a6-875e6692eb34 | -8.30322 | -43.6829 | 2025-09-22 04:17:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b63e7e8-4aeb-3a5d-b990-9e6e1fb0613d | -13.4972 | -47.26327 | 2025-09-22 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c22ffe9f-eacf-3aca-8ba4-3b5000fb36a0 | -14.35595 | -47.78532 | 2025-09-22 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1a10c157-1a28-335d-ad11-b5f53725fbc2 | -12.07534 | -44.80277 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b8428ac-423b-3acc-bdf5-54ba3f4ec17a | -7.64483 | -44.43863 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b98ac0f-3757-3811-8646-e3721d7b643e | -6.44404 | -45.68645 | 2025-09-22 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f81e2ec9-6857-375b-960e-26010d427317 | -7.34887 | -44.45346 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d826b153-e498-358f-a577-7a254ce35d25 | -7.59706 | -44.47848 | 2025-09-22 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e92cb2ed-50ff-3d8d-933f-c914b6af9c41 | -5.55168 | -42.13079 | 2025-09-22 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 345015a2-5128-3a4d-8c1e-2d71c691da54 | -5.65113 | -51.46541 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e858bfbc-3fa1-3f13-9922-ffeea7779635 | -6.90081 | -44.76588 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9a45de60-810c-3351-a8e6-d7b99bb4e7b9 | -7.62979 | -46.82256 | 2025-09-22 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9a3d367-e141-36a3-a4e2-f7d43646fbd9 | -3.1415 | -44.42546 | 2025-09-22 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa57b662-0365-3974-b681-ed257667309f | -4.25831 | -48.60266 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eddab14-b0e9-360f-9bd3-446ba6737fa6 | -11.63861 | -44.319 | 2025-09-22 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 041b3e1a-e1cf-30eb-a073-1b4861a00148 | -5.64867 | -51.46721 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ef51ec8-e8a3-3826-8290-f1d2365df44b | -11.25989 | -49.24527 | 2025-09-22 04:17:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0317a77a-9d24-3821-804a-03ad04fa3a1a | -11.6619 | -47.49889 | 2025-09-22 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2c8e93c-19ba-3b9e-b252-0a301664cb05 | -14.43904 | -46.53076 | 2025-09-22 04:17:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0dac1c7-7658-3e5b-bf53-1cbaccb5d30f | -12.73936 | -46.8299 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68d74ea7-0d21-38f6-9888-ae5a3bcb1ccb | -0.79892 | -47.59874 | 2025-09-22 04:17:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8d198dc1-bf30-31c5-b880-47863771aae1 | -5.06212 | -40.47287 | 2025-09-22 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1b3dd791-0775-39e8-9045-6d5cdb27e7ee | -13.24076 | -47.21992 | 2025-09-22 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f27dad5-410d-35b6-a3e2-01e326fc352b | -7.90982 | -43.87747 | 2025-09-22 04:17:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3179a440-6bad-3e69-a8f8-3e39424d846d | -4.30824 | -48.09115 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 202f7864-abf2-3d47-9c47-7ca4523e84df | -12.72893 | -46.82807 | 2025-09-22 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9badff91-5bb7-3340-a14f-e300e13f5d96 | -14.97684 | -44.41349 | 2025-09-22 04:17:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68f25564-74fa-3628-b90a-8503b4ba0cf5 | -13.54682 | -43.32566 | 2025-09-22 04:17:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 88505b63-f46b-370b-ab81-3678fd757174 | -11.63971 | -44.33364 | 2025-09-22 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dffe543-62c2-33f9-a380-e667535cdfe7 | -5.64547 | -51.46752 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
