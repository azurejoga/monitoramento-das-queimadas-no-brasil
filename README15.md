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
| 2d7dae0a-8ca6-3843-8267-4ba2867dad73 | -3.51632 | -44.03745 | 2025-09-18 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8b9e0ad-1588-3166-8bdb-1a38912a6a68 | -4.80467 | -42.73159 | 2025-09-18 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 37.4 |
| f0c1180c-054e-3937-bb9c-ef680b587cc4 | -6.49551 | -46.00021 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2d2150f-3286-38e0-8d00-812a0dfbddbc | -5.9597 | -43.80227 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49e4d8ee-a0a4-3f97-b77f-3c38a8c3f7d7 | -5.79224 | -42.45504 | 2025-09-18 04:12:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a2314150-8f75-3bfd-b292-6397dd52fb25 | -4.70109 | -46.4374 | 2025-09-18 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26b1ce25-05e7-3741-b76b-df952c4bcfe6 | -2.64884 | -48.04872 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41a59c2c-05c2-348c-9cab-87e44354495e | -6.36398 | -42.81474 | 2025-09-18 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bc401f55-73b6-3f9f-8a60-6d1122c030cf | -2.92004 | -48.67491 | 2025-09-18 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a01dae3-0a5f-345d-9c14-72e4766aed41 | -6.75557 | -46.00702 | 2025-09-18 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d22bcf37-d231-3ed5-a50f-74718d9c37d4 | -5.62331 | -42.903 | 2025-09-18 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc3abee5-8b56-3dfe-b6ea-cc380e0b2c0d | -5.94913 | -47.01305 | 2025-09-18 04:12:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aeefeae-5329-3438-b445-bab03c35028a | -6.29011 | -42.37651 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 93dee384-733c-3bef-ac41-3128546b6b10 | -7.50993 | -45.30595 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87eb1b7a-05ec-3414-b8c3-3053ed228952 | -7.85311 | -45.58831 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d22f7c61-d803-36ee-bdf5-a38251814ac6 | -13.07777 | -42.14091 | 2025-09-18 04:14:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 036a108a-8bdb-3e1d-894b-73884e14b165 | -9.16723 | -46.9607 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| c7cef40d-691e-3ee0-aa5c-7774bf4a7aaf | -8.70015 | -46.36713 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cfc5c8c9-6039-3cf8-bb43-07a6139dfc4b | -11.99444 | -46.70651 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e02389a0-0013-31c2-b20f-f143b39afe17 | -7.5623 | -44.76439 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e65d7171-d53f-3ef1-9e78-fa5b7b83554b | -7.63187 | -44.4596 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db14038a-f060-3a66-941a-4d504956b78b | -10.63443 | -46.44467 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 870dcded-49c4-3ddf-9097-2bfe27df6cef | -7.54011 | -44.70911 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2fd2651-bcde-3907-9d82-8af970d614c1 | -11.46051 | -43.54947 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc51ed3b-fef3-3874-901f-e36b72edc480 | -10.60754 | -46.46884 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bffa1ff-ab91-3549-9d5b-b7fa5bb995d9 | -11.23984 | -47.43845 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0a5188ef-e3da-3efb-a6e0-e420a51ccbad | -7.86248 | -45.57436 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8e7a9d64-f2ce-3191-87a8-c12b333a22ac | -7.98931 | -43.94357 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b5d43ea-58ad-354c-8741-66fc12ad2e68 | -11.1775 | -45.3568 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73453cf0-ed84-3d43-a12a-291d55dc09f8 | -12.09688 | -44.83541 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14c5ca80-36ff-3061-afad-8ef2fdc42020 | -11.03501 | -45.06131 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a41d5bf-72bd-3111-84fb-d8e46abebe64 | -12.09631 | -44.83895 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb80b9a7-52c3-3e26-bd4f-a7170fe64765 | -7.40259 | -50.00871 | 2025-09-18 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e4a2506-e144-337c-81cb-9c44f55462a7 | -7.56288 | -44.7608 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3671e58-f19f-34e9-b8bb-4bd4d18d84d7 | -9.00822 | -48.17326 | 2025-09-18 04:14:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87d8bca8-c81c-3054-b65e-f58706efb2e4 | -10.64562 | -42.31504 | 2025-09-18 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ed6c9139-cfa8-3649-b363-2ea9adc98174 | -12.10471 | -44.80765 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93510677-2012-35d3-a8ca-03646d20cca3 | -7.51695 | -45.2842 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71684884-e691-361b-b61c-e5ccee223af4 | -12.4071 | -51.41435 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e9a354b-16c6-391f-988c-5d8f8112c20a | -7.22236 | -44.38705 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aa76007-0eca-3852-b646-2c7273a6c9b3 | -7.54942 | -44.75847 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2219ab96-d772-37d3-a274-86aee0491272 | -8.69086 | -46.35736 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b976c66-e0de-3a1d-8da0-dfb13d44fc1d | -11.16307 | -45.33959 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b3c4bfd-e6d3-3fac-bd6a-31255b829a58 | -9.12132 | -44.85629 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c5619c4-bea0-3265-adfb-181b5e9dde95 | -8.70302 | -39.60321 | 2025-09-18 04:14:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84ea8ce0-38e8-303b-a047-9773d980fed0 | -12.23918 | -46.77944 | 2025-09-18 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 44ed6dbf-e9c8-3d57-859d-ff6813b4b382 | -10.91575 | -47.83941 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b74e36b-e7ec-3fb9-a15e-811661900736 | -7.42078 | -49.99518 | 2025-09-18 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10c1faee-1e7a-389b-983f-221cedc40ab6 | -8.35581 | -44.67042 | 2025-09-18 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3787357f-a569-3dcc-b243-0f2cca56ab81 | -10.60481 | -46.47188 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56b4441b-0a0a-3cd6-a73c-f2bd8819b5e5 | -12.10802 | -44.8082 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2077bc6-1632-3e03-bc6e-702ee097dfe0 | -7.51062 | -44.34566 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 918f574d-5715-3f83-9fc1-90e8340bd297 | -9.1643 | -46.95592 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7863a695-3535-3132-bc54-87d38caff315 | -7.53558 | -44.71573 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41b1d6a7-a8e7-3849-b171-13bd57b18ee6 | -11.46938 | -43.55815 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2d7b533-635f-39f8-bda3-f9b15d9e5624 | -8.65258 | -46.43388 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0b3526f-a298-35b1-803f-6fc5906a45bc | -12.1002 | -44.83594 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 999009c7-82b3-3c0d-8d7d-674648720e81 | -8.63193 | -45.30973 | 2025-09-18 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fedd2ffb-2cb7-3f97-8e8a-1e2bda1f61b3 | -11.45718 | -43.54894 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ef09f5a-589b-3171-a99a-23507ce3d80b | -11.17633 | -45.36402 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3e5cb6f-3c23-391d-aabf-e9f1bda22e82 | -7.67159 | -44.40407 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd4248fd-7770-3b56-8331-0c9e0dbb6889 | -8.95332 | -45.53196 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1fa5e44-4e68-3c94-a4d7-d5797163076b | -8.62258 | -45.71155 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7d2fcc6-5255-328b-9f61-dfbb1b6dc9ba | -7.87778 | -48.14563 | 2025-09-18 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8bc80ab-b386-34bf-97b2-652ed8ef196b | -10.91797 | -47.84866 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39d649da-685b-374a-9e35-fde789c1da23 | -13.86529 | -44.41101 | 2025-09-18 04:14:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac7ae86e-7e7e-3b3c-9c4f-da782be8277a | -7.34323 | -44.58156 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6752bfee-ac9e-3480-9d03-6f6e3b10b0cb | -7.26263 | -44.90262 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 25f9bc55-8c8d-3f4b-9a96-6aa3176469c9 | -7.63522 | -44.46014 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ef0ccaf-c411-3090-a2ee-f25b6883c846 | -9.23216 | -40.26348 | 2025-09-18 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 09876e74-d9f1-3853-98ed-18f3d022fea1 | -7.66068 | -45.13203 | 2025-09-18 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84eb06e1-8dda-3d5f-8d9c-2cf6274b8e88 | -14.50353 | -44.86483 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eeacb7f-ac6f-34ed-a3d7-fdb476f1196e | -7.59329 | -47.13619 | 2025-09-18 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50fa493b-396f-3192-93a8-a4b86ebbed1b | -8.92594 | -44.50396 | 2025-09-18 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b51ee8c7-6d4a-3f76-b2e3-11b8cb2fa476 | -13.66366 | -44.39669 | 2025-09-18 04:14:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fde8c628-d8f3-3b96-a6ab-35eaa0d448db | -7.29243 | -44.1369 | 2025-09-18 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 739d08b9-d9a0-3d05-9cce-d7b95b5a5857 | -8.13394 | -44.84873 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c89f04a9-6258-38ba-ae89-378b51aa5032 | -7.53291 | -45.29427 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f32299bb-ed0f-398c-9165-12d5296e4f36 | -11.24118 | -47.38677 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1705a462-717d-3b83-a0b6-f7f1a4f26987 | -7.24878 | -46.61708 | 2025-09-18 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5690d669-4b49-3b4c-bec5-35593e6f2512 | -8.07223 | -45.44895 | 2025-09-18 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0ee16c6-aecc-32ec-a55b-8f9c3ae46089 | -11.20199 | -45.37564 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19714be9-bdbe-3479-a288-2e88bbf633f9 | -8.6473 | -46.42549 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 384147da-d026-3e25-a7df-7402e9dee7fe | -10.87895 | -47.77587 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 899130b0-8942-3409-9712-b98a5c73a6c6 | -8.68687 | -46.38134 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 588540a0-3ffa-3a99-b3b3-d46595d38705 | -10.21113 | -48.87368 | 2025-09-18 04:14:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 25fd524a-de6d-3521-961a-26bd2226c634 | -11.49544 | -43.60941 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3d67fc6-b84f-37a2-8a5e-bec80a5774d6 | -7.44517 | -42.63228 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 98c2ea16-4b9f-3ed4-a80c-9f66af4277b8 | -7.26845 | -45.36779 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 58a17203-3411-3d11-8979-dbba2e34bdd5 | -7.86593 | -45.57495 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e6f6fc7-8a31-3fe6-8fde-ac93eee792c1 | -10.6652 | -46.45328 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 452d0897-0fe0-3d9a-9830-f9448853fbe4 | -11.32572 | -43.47727 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7714de41-1145-3f71-b8aa-b7307bca3fbc | -12.01266 | -46.72577 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c600d8f-4f93-368e-aa24-8a50c45d7145 | -14.74211 | -41.34361 | 2025-09-18 04:14:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9922e6eb-9a9a-3ad3-8313-792fef7545cb | -8.9882 | -47.04578 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7818f94f-206e-3f76-8ab2-802f17af9369 | -14.08297 | -44.47205 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c69e821d-4fc7-35bb-bd12-439872f04c89 | -7.20343 | -44.37654 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1589c8b-773d-3e37-98ef-b70cdfd84683 | -7.21346 | -44.37823 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fbfb038-8a81-3fdf-b897-55b75dfc9cfc | -10.69049 | -46.47356 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb8cbdb2-38ae-3ea5-9c51-64abb648b298 | -11.24709 | -47.43962 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README16.md)
