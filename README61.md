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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c58c7aba-477d-3460-b374-1a820a50ed74 | -20.62942 | -42.28984 | 2024-09-27 03:49:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 69dd0512-ba5e-3cfa-a63a-f7962e374da9 | -20.62872 | -42.29391 | 2024-09-27 03:49:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 33a3a55c-9da9-31b4-b318-a12a5316118e | -20.62738 | -43.04254 | 2024-09-27 03:49:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d04d99a2-6f38-3e76-89b4-6a738357e595 | -20.62381 | -43.04193 | 2024-09-27 03:49:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7a62d2d0-c2a3-357c-8e6b-2fd41462ac5c | -20.62275 | -42.89988 | 2024-09-27 03:49:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c9b9ea98-4983-35dd-b783-84c9e1ac6bfb | -20.61921 | -42.89918 | 2024-09-27 03:49:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 486b7563-1f70-3de0-8df2-705580d78af6 | -20.61846 | -42.90347 | 2024-09-27 03:49:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| cf1d771d-873f-32f1-9fa5-1b6b195b84e2 | -20.6064 | -43.07857 | 2024-09-27 03:49:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b7df0f87-aaeb-35dd-9e12-c8be2972a786 | -20.60358 | -43.07356 | 2024-09-27 03:49:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 632159b2-c1f4-34b8-9f8f-72e60a863a02 | -20.60001 | -43.07285 | 2024-09-27 03:49:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e3e8a6ad-bdbe-3ac7-96bf-567c7eac1ddd | -20.49959 | -42.22358 | 2024-09-27 03:49:00 | NOAA-20 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 067f1ebc-c4a4-3018-bbc8-4af66ae0fb31 | -20.46512 | -42.15474 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| c6719938-daf9-3da4-9187-995d87679e57 | -20.33195 | -42.73398 | 2024-09-27 03:49:00 | NOAA-20 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c5a2123a-6339-3707-851b-1bfd748e630f | -20.21685 | -42.87518 | 2024-09-27 03:49:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3c63a4aa-b188-3073-a96f-5b6eb123ef21 | -19.94129 | -42.32428 | 2024-09-27 03:49:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7df46f2f-15dc-3294-942d-362f8d56988d | -19.87042 | -42.16395 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fc670189-6be3-3f3c-bfab-90e53c9427bc | -19.86969 | -42.16826 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4c53c465-063e-32f9-aa35-a7d3e9bf382b | -19.86696 | -42.16331 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fd5afead-0faf-3efe-8fdd-51bb010c4f2f | -19.86623 | -42.16758 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5f86d8a3-7fac-3376-a491-26222d13973c | -19.86409 | -42.18016 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 304b01b5-5718-3ea3-a70e-40fbb0414571 | -19.86277 | -42.35641 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dc5edb26-839f-3ff3-adf8-dbdc70b0e9a8 | -19.75369 | -42.18928 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e360fb98-8953-38e3-8563-b0f284bbaa25 | -19.75226 | -42.19765 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b2c68a41-b2d4-33ba-8322-918459d3c4b6 | -19.75021 | -42.18867 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f37990fb-fbc1-3952-9eb6-d9d3fbf4c2a9 | -19.74949 | -42.19287 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 64ba9d88-0298-3a61-b18a-4e8281a34a83 | -19.74878 | -42.19704 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bd00eb56-ce0b-338e-8e85-43256aad8777 | -19.74673 | -42.18808 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 60c5f139-87d5-3d91-bb16-d82ef8ca9e98 | -19.74602 | -42.19225 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 909e70ed-1c71-3bc4-9f99-e9f8cb9d5580 | -19.74396 | -42.18332 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ffc5724d-7f0a-31de-a789-0ddc662f5bd7 | -19.74325 | -42.18745 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 762c18bd-329c-33ad-a006-640869db8514 | -19.71914 | -42.39112 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c87af5ec-2137-38bd-b7ea-bb7b416196af | -19.71564 | -42.39043 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f710aaaf-5aaa-37b1-8e26-10ab029dea58 | -19.71286 | -42.38557 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5985e0df-f37e-316e-aeb1-e16e26efd962 | -19.71214 | -42.38974 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4a73e648-6ad0-33cf-8b71-60fd8c214c07 | -19.71143 | -42.3939 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e25133c1-2c1b-39fe-b06a-20392c3f34b6 | -19.70864 | -42.38906 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8a7c4445-702c-3c2f-92b2-3bf2984241a2 | -19.70514 | -42.38839 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ceaf83d9-d70b-3ffc-965b-4ba3fe1abee5 | -19.6847 | -42.4229 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 199131cb-980f-34ff-bd64-41af42ed003c | -19.67769 | -42.42153 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 03032af6-d5a5-374d-b727-397eb146aa39 | -19.67481 | -42.4381 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b37b675a-36dc-3192-8aca-f0894c989cdf | -19.6713 | -42.43743 | 2024-09-27 03:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3ff3b532-4115-3969-a5c1-0038023fcd46 | -19.65678 | -42.8579 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f8d78354-a648-3e8b-8bf2-577fb99d3922 | -19.65319 | -42.85727 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 667bd147-a7fd-3a63-8279-25981f0ce89d | -19.64961 | -42.85662 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 126e3d78-9d22-3bb9-83f3-ebc3a8e7389a | -19.64887 | -42.8609 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d4c3b239-2792-3668-abcb-8d65a0b890bb | -19.64269 | -42.83276 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7e9aa7c1-6ad3-3ce9-822a-ad3a1274df61 | -19.63842 | -42.83606 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 55bffff4-07db-3062-97e9-63075cba31b0 | -19.63411 | -42.83962 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 51af0612-7bc2-3dcf-b898-a8c560a7d3e0 | -19.63335 | -42.84399 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a18ab987-feb5-3583-9551-7ff40d51a941 | -19.63072 | -42.81678 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2aeb7cc6-9799-3b3e-abc1-96891e678c90 | -19.63053 | -42.83897 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9080d230-a47f-3bc8-8e0c-34f3a9b2e84e | -19.62978 | -42.84329 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| aeb87d98-766a-37da-af65-8bf4660c0eb4 | -19.62918 | -42.9313 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5ab0c370-f037-3e26-94e8-897180d3075f | -19.62857 | -42.80801 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 7abd3064-9fc9-345e-919e-7e0f365146f2 | -19.62789 | -42.81192 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f1420dd3-9a3e-35d0-83ec-d43150b710cc | -19.62719 | -42.81592 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1977d6ef-c494-38fb-8561-bb91bc87d2e2 | -19.6256 | -42.93054 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 7cf078f3-6b1c-3205-8ac6-d8819e7ae04f | -19.62502 | -42.80727 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2097977c-d82d-360c-822d-7b3965cecfe5 | -19.62434 | -42.81112 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bb48093f-c08f-3343-90c8-62c700a8e915 | -19.62365 | -42.81509 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 1e7871f1-edf7-380d-b663-00c46554d3c8 | -19.62294 | -42.81911 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 394e900a-2e81-369a-9aae-b70847475997 | -19.62218 | -42.82345 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 3ee8eb64-9c46-3225-a030-fbfebea09448 | -19.62079 | -42.81036 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 20620fc7-db8f-32c5-a7be-00929506250f | -19.61862 | -42.82272 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 42ae82f9-7921-3b06-ab9c-6669aafef924 | -19.61782 | -42.82725 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 748374f3-e328-3f9e-926d-403f97cdf4c9 | -19.61769 | -42.93337 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c8e0b263-d67a-3958-bdc6-affaa8a2230c | -19.61723 | -42.8096 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| eb03a38d-82a7-36e4-aee1-99ca56b420b6 | -19.61703 | -42.83173 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| d789a4ba-27a3-3d5f-9c13-4a2bf7ee1f48 | -19.61579 | -42.8178 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| bda871b6-05ec-36ac-966d-dea694dde632 | -19.61503 | -42.82212 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 0018808f-0b77-3a95-b882-235736b88398 | -19.61426 | -42.82654 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 403f0583-5e8a-34f2-a7cd-6419c9cb75a1 | -19.61368 | -42.80883 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f8f61700-8d13-3ebc-9e6b-47f127c1a81f | -19.61348 | -42.83094 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 36e7c6c7-c650-3feb-975e-c1938fc4ce39 | -19.61221 | -42.8172 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9bff97a2-dc12-3d9c-bbdf-dcd4598605a8 | -19.61145 | -42.82154 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 5b63052a-e551-33fe-a970-584b0618f002 | -19.61081 | -42.80418 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1b131031-3a4b-3f09-80f5-183803a021dc | -19.61069 | -42.82583 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 93ce3b0a-375b-3136-bf03-893c1b3933fd | -19.61009 | -42.80829 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| cf73153a-d26d-3d05-ade7-26779798c7f1 | -19.60935 | -42.81247 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8625b407-45ca-33e0-906c-f5240cea7ff3 | -19.6086 | -42.81673 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 85657bdb-0660-37f9-a5ea-ed69e64a8292 | -19.60786 | -42.82097 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 98145c85-382c-38c5-8bab-567e13f8f8a6 | -19.60721 | -42.8037 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| a9ef0774-f2e0-3554-9f04-d3f179d2d3c0 | -19.60647 | -42.80789 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| e54ad681-96e6-3ba9-8a63-2910ac1e9bc5 | -19.60573 | -42.81212 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| b6b27f58-6588-3948-9b26-8454beeabb07 | -19.60499 | -42.8163 | 2024-09-27 03:49:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3165f0dc-aa3e-3a7f-9032-24ac4801c358 | -19.59783 | -42.63177 | 2024-09-27 03:49:00 | NOAA-20 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b6755f48-432d-3953-abce-5df23affc3b1 | -19.56195 | -42.69111 | 2024-09-27 03:49:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| cb76f7bd-0aa1-369c-9398-69a58dd080fd | -19.56126 | -42.69509 | 2024-09-27 03:49:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| d0489f31-05fb-31c6-8350-f7807623cf8b | -19.56051 | -42.69938 | 2024-09-27 03:49:00 | NOAA-20 | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e89dcee6-752f-385a-9c15-195e449c3e12 | -19.55839 | -42.69048 | 2024-09-27 03:49:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4c5ce3b3-aa77-3bf3-b527-65a9c4c01666 | -19.55768 | -42.69453 | 2024-09-27 03:49:00 | NOAA-20 | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cd3d6076-0a88-391d-96f7-0fe08b24640a | -19.55613 | -42.59808 | 2024-09-27 03:49:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a20055b7-8f90-3996-8fc1-98084d8fb271 | -19.83098 | -42.01931 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 01022521-ac92-310e-8e2f-63f2730bbf4b | -19.82942 | -42.01601 | 2024-09-27 03:49:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c7f91e54-fb4f-3afa-bd6e-da007face4fa | -19.7905 | -41.95186 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 182678fa-22fb-3830-b3ba-55f1fd672ada | -19.78707 | -41.95121 | 2024-09-27 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9ba9da6b-ad2a-3008-886e-991869c8516f | -20.51138 | -43.49219 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 656a32a4-eccd-3999-8d1e-3c6c975d6847 | -20.50849 | -43.48725 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 581a1ebe-e633-3a91-ba56-5e949be9c811 | -20.50484 | -43.48658 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 48d71ae4-946c-3f78-b295-03e97a6d6f96 | -20.50039 | -43.49041 | 2024-09-27 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |


[Clique aqui para ver as próximas entradas](README62.md)
