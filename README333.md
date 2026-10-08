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

## Dados Diários - Página 333

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e608d1f-049a-3321-aa26-96b0d1deb5db | -10.40489 | -46.26969 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c42757ba-40f6-391a-911c-878e7ec68bc1 | -17.54347 | -42.95231 | 2026-10-08 16:37:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 567cd1c6-1418-3ebf-8b62-2ada6f39dc2e | -9.36598 | -45.9459 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1a0e7cfb-478e-3138-9bdc-fc3b8be2b415 | -9.20655 | -46.53379 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 99a706ba-7c8a-3df9-b9e3-62c1eec17be8 | -7.1092 | -42.52851 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 2f815735-d17b-32cd-b4cf-2a9339603e31 | -10.45001 | -47.27782 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 24cdc2c1-7613-34f6-94e3-a17a1fbc51ad | -5.76863 | -42.06632 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 3bb66f0d-e0c8-30af-bb72-b1e8e9fd8272 | -6.16412 | -39.43611 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| a0d4dab6-481b-397a-b67d-681ce944ad37 | -11.34472 | -41.59026 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 92862415-67af-335d-8bbf-74881192d25a | -11.08806 | -44.00742 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2b3f990d-d834-3057-87f5-73584fc5becb | -8.95833 | -45.16082 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 0db72663-155f-307b-915d-e1327075a9ff | -8.93149 | -45.18671 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 03fe1e92-ae18-3044-b5e4-1c7ff80416c3 | -13.20278 | -47.8786 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0c532b23-8a28-3778-9f62-8258214e5346 | -5.51125 | -37.48983 | 2026-10-08 16:37:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 142d7448-e9a0-39b0-a060-5384411388a5 | -11.31061 | -44.83355 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f30301ee-ff21-340f-9bf5-b4763501b153 | -5.98666 | -40.92982 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 3044a89e-9391-3fd8-b1b1-116593ddcca7 | -11.07578 | -45.76968 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 1037bd67-b4cf-37a1-9e19-2d4735370677 | -12.23736 | -44.74835 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 12440483-8df5-3a53-9705-bc99e5338345 | -5.71704 | -41.65248 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| cbbeecd5-2743-3944-8a9d-8b9b9e066010 | -11.24434 | -45.24632 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7a9e4f3-9361-32a6-99fa-279985c15c85 | -6.43894 | -45.93034 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 340c362d-37c5-3356-8bee-b0d031497227 | -9.43854 | -44.59959 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c58879e4-4c6a-3f86-b416-282252c953ce | -8.22936 | -37.04055 | 2026-10-08 16:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UMBUZEIRO | PARAÍBA | Brasil | 2515203 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5712d2e3-96ca-3e16-be12-f5706d6839b3 | -7.02729 | -44.78698 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e5a9d214-75e5-3594-bf5c-4f284c09d968 | -6.98526 | -45.13187 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 32cd5a87-5e7c-3ad5-a3fb-b9e719a7e791 | -6.4691 | -44.0322 | 2026-10-08 16:37:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34600236-c2a6-3b51-975d-79242407a441 | -9.8136 | -45.67674 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7e742492-3a2a-371f-8382-0fe16392afbf | -6.53275 | -45.38997 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ebd34c11-6a3e-36ac-99c8-2eaa4dfb934f | -7.168 | -44.82215 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0597039d-1359-318a-be7e-1c6ba4014f15 | -8.51092 | -54.61968 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8d256585-7297-3d82-9e82-05d66f43b814 | -8.75215 | -46.84708 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 885966f8-b4ec-31fe-836f-b4e3b3d147b5 | -5.96467 | -40.9221 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| d028e36f-a4fb-370e-87ad-2a3824fd3e2b | -10.74734 | -48.5462 | 2026-10-08 16:37:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c697396d-6e17-3ed4-8453-b219ed1c11a2 | -8.28256 | -45.71376 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0643f2b9-741a-3958-a124-5b2137bee448 | -10.78145 | -48.75582 | 2026-10-08 16:37:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0efcfe55-f0c7-3d5e-a4ad-13db0ec102d6 | -8.95129 | -45.13697 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 52c003f1-45c4-304c-a83c-1d1b5dbec6ea | -6.30942 | -35.13918 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 7ba2079c-3c6a-3a53-96fb-6f8d910744c5 | -11.24898 | -46.27258 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eb4d1eef-e2cf-3ded-92dc-da6a8684ad1b | -9.93887 | -43.56453 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 5c983e1f-ac90-34e6-95cf-ba1937133b17 | -10.41536 | -47.28293 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4289069f-adfc-3b78-8f40-e2733b0bce57 | -9.76345 | -44.79074 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2ff9cca4-acf7-37dd-ade0-61ec1d7bd218 | -6.64838 | -43.76609 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 25837f7c-8551-31bc-b22e-0881efd7993d | -8.93533 | -45.18968 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c57bf61f-8ea3-3a43-aea6-f94ae096b514 | -6.36409 | -42.57365 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 9c3224d8-123d-3c8e-86e2-f7c0a973d580 | -13.11651 | -46.34441 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f4e184a9-9abc-3fff-95cf-b9338d6e35e8 | -6.50751 | -42.02966 | 2026-10-08 16:37:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| de1d6bea-d83d-3af6-93c4-91cbee47fc1d | -11.62385 | -43.69637 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| de2c6695-673e-3d70-b3b4-1a65ef955fc4 | -11.60817 | -43.63981 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d144de04-f90b-3a3c-8000-c8c2eb0f6619 | -7.3447 | -50.82662 | 2026-10-08 16:37:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c428ba1-5932-3c5e-ac9c-8cc1d9c823c1 | -11.24712 | -45.24228 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a5611b16-b50a-3980-82b5-6710d011b61a | -11.38754 | -54.04103 | 2026-10-08 16:37:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7db432d5-ab1b-3376-9616-b8a01d34e96d | -11.84417 | -47.30268 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4b1e6237-feca-31ec-a2f5-77c22582251b | -6.36438 | -42.52911 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 47d3b916-e5c6-3bf4-adb1-591c296bec2c | -12.01997 | -43.45017 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| f80ee13a-b84b-3936-a980-c98e6951783d | -6.50504 | -44.70708 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 40e3d93a-4b75-3c36-8f8a-20cd56f85309 | -8.28692 | -45.7202 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| e503bd67-04ba-391e-af5f-8e3a8c4b3772 | -10.98227 | -45.39695 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a6323b39-0fec-3259-be21-691e645bb104 | -11.77805 | -43.53421 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 436aa81e-0466-3c92-b681-16528549b5da | -6.85834 | -39.4627 | 2026-10-08 16:37:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 21.4 |
| a9a058e5-e3d1-3b17-be30-85b24510978d | -8.321 | -39.77029 | 2026-10-08 16:37:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0fb15ad1-2b1a-374f-82b4-6caef41ef6ae | -11.85666 | -43.53995 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 76108616-5404-334a-a765-052a282f86ac | -9.23412 | -45.65844 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f2f83cd8-680e-3ad2-8023-d544b01cee33 | -19.07726 | -48.64171 | 2026-10-08 16:37:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ee538885-6d1f-3e16-80a2-b460c31c0c07 | -9.43474 | -41.73704 | 2026-10-08 16:37:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 5e2c48ae-9da3-36cf-bf05-a70110acd7f8 | -7.85348 | -45.15001 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8850b829-7539-3088-a507-189129b21b70 | -9.57786 | -46.84356 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 738b3b32-019a-3e25-b28c-34ddf7340b6d | -7.34914 | -44.37017 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1c292d97-64df-3470-8ac7-8758f4f05717 | -11.265 | -45.20356 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 977a28b2-9098-3093-a7ec-ca447a6e4ef1 | -11.7743 | -47.7449 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c70833b9-8e0c-3e1c-825d-ca3cf4972fa7 | -8.29288 | -45.73705 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 25dd6fbd-c1c6-3015-8a1e-a5baf28cfe73 | -11.3073 | -44.83407 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 9aed4351-b82c-3804-80ff-a96c45e3a0f4 | -5.7641 | -42.06232 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 34340a03-132e-3921-bba5-8c891aec4018 | -6.97472 | -47.66395 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 24b469b7-505f-33da-88d8-1b7debf21343 | -9.94341 | -43.57131 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d11db02e-e942-3085-b9f4-7bd51a3cda17 | -5.77014 | -42.07557 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 918248b1-c6b3-38fe-836a-248b329ef845 | -8.29167 | -45.39613 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2d35a437-4e4f-36ae-a64d-07fc7f5eb84e | -11.27653 | -45.21252 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 05bea5c1-400c-34c5-a9bb-8c852ca0ac5d | -8.77158 | -47.25694 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5087a57a-a94a-3514-a626-d234a75e1558 | -9.83304 | -47.46707 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7ca2ed9e-0c17-36f6-bb01-d991aded7769 | -7.7065 | -45.42945 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7afa7013-9f98-3996-b04d-f1be0add6848 | -10.47115 | -47.23856 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| ecff553d-a327-3640-bf07-6bbc6139194a | -8.66419 | -54.53095 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c8262a23-6742-302e-a795-67b798b72f0c | -11.22019 | -45.26563 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 050eac01-602d-3dce-9279-1279f1bb7664 | -6.77527 | -44.13039 | 2026-10-08 16:37:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 03af8bfd-4c09-3d61-84d7-3a063c80519b | -11.08996 | -47.62709 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ae5366a1-5028-3d67-9e08-61e406bfdb6c | -8.66986 | -36.68591 | 2026-10-08 16:37:00 | NOAA-20 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9e6b02c2-f1c5-364e-8216-4c0affdb0765 | -8.25424 | -54.6503 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 7923b821-4705-3ec6-8d38-9f0770f99486 | -13.20645 | -47.87815 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 24a1a948-2ad8-3617-ae21-2ccf23b3136a | -8.99017 | -45.95148 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 33aaeb71-4aea-3bbf-bd84-ac8b5324fcc1 | -6.13652 | -43.85807 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7176e1ae-93ef-3da9-a1b7-c30233cd34e9 | -6.97653 | -43.29309 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 61e74e35-8e27-326b-a8c0-a801dcb91147 | -10.5037 | -47.31664 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 4e2425ae-0e68-3586-b9e4-ac4c27dfa61d | -12.21813 | -43.93814 | 2026-10-08 16:37:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| b43ad02b-99f7-37d6-96ab-e910b1fc65c2 | -7.76105 | -54.95295 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| f72e6b30-699b-3cd2-a9f6-1ccee8649118 | -6.66239 | -35.11976 | 2026-10-08 16:37:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 67af38bf-781f-311d-a042-3263113600b6 | -10.76956 | -46.60178 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 4fa47a97-754e-34d6-aa49-b1e25fce8e29 | -6.95478 | -43.73267 | 2026-10-08 16:37:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| eb16c29c-6fc0-3185-8cbb-3a5dbe7bd5b4 | -11.29456 | -40.84772 | 2026-10-08 16:37:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 6e9621f0-e73c-31dd-b6f2-f1784cf7d80e | -8.43964 | -47.0249 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c006995e-3678-350c-9db2-cfea5303d2d6 | -12.23352 | -44.74536 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |


[Clique aqui para ver as próximas entradas](README334.md)
