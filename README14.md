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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8022079a-d28d-3c42-b5d8-d56b6f6b46ac | -7.78804 | -44.12304 | 2025-10-06 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d9d4c06e-b1bb-349a-adaa-5720353ac2d0 | -13.10168 | -48.01107 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 981788bb-b050-3828-8f15-b01b34280c98 | -11.80382 | -45.12217 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4795a725-50c3-386e-85dd-f02941926bc1 | -8.88133 | -47.63063 | 2025-10-06 03:36:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e5af5461-b7e9-3a6b-80ca-4563263cfca4 | -12.44658 | -45.54828 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77a4f18b-0a9c-3eb1-8323-52fdac602ade | -12.90204 | -47.29788 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 82cdc06e-7b88-3fb8-be64-a0d40a09ee27 | -12.48282 | -45.5473 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 97908920-7d53-36f3-8f16-b411b5922168 | -13.07694 | -47.87844 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 633f3677-73a7-3445-a542-f9c4b9c275de | -13.27986 | -47.58213 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 541d6b2c-5dd5-3a37-b6d4-65d2f2913696 | -11.83957 | -45.06866 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65b82fcb-96a8-3de2-af49-038d4168e9e3 | -12.20012 | -39.84819 | 2025-10-06 03:36:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a186dc8-efa7-3d14-a9c2-aa0f973d1f44 | -11.49582 | -44.97789 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9caa14fb-87a5-3690-9b60-c898f7265a9a | -11.48429 | -44.97661 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07cdc2dd-d80f-312a-a713-c3773158c130 | -13.2688 | -47.63607 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29267b32-3e0a-35b7-b3e1-262fef6003c0 | -9.31415 | -46.00729 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 18833825-673f-38aa-9170-63dce2d3e04d | -9.31127 | -46.02213 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c196454b-d99c-3d36-874b-5959b1be40f4 | -11.43377 | -43.48356 | 2025-10-06 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3e7d519-0ecd-3639-addf-85bbad2d8f74 | -12.45399 | -45.54122 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b6aea16-0f86-39a9-a1a0-c6c4362b2c36 | -8.61024 | -46.28129 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a498848a-60e1-3e0f-a0b7-37c1741d73cf | -13.34081 | -47.18794 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4741c776-3ab2-3593-85ff-4397b0f25580 | -10.34432 | -47.01722 | 2025-10-06 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbb6259c-b814-370c-9e9a-ec961259217f | -12.25134 | -49.21833 | 2025-10-06 03:36:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e57cb96d-7001-3517-89a3-d17a768cca28 | -7.71787 | -46.2579 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d80412d7-388e-36c7-8c4d-2ec6b4b79e2b | -12.44731 | -45.57499 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 325caff8-01e8-3bb8-a109-40d7afb43a33 | -12.57672 | -46.73806 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 725ec02e-33b6-3912-b66c-1f8008e94be3 | -9.31608 | -45.99735 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 613227a6-da5f-3d8e-8730-b09096e51d2e | -7.71889 | -46.2524 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1bbad581-1d30-3256-8b6e-4a92623e0006 | -13.36213 | -47.57424 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 413eece1-82b0-38b9-9729-bc4cf2f305f9 | -11.02182 | -46.55238 | 2025-10-06 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0547113-a069-3bd0-b920-e3e5c29ec50a | -7.71743 | -46.2529 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 03c14d61-18dd-3a37-b57d-b12ceced9fac | -8.62639 | -46.33669 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc737d5a-3045-3851-a106-3affdee02a1f | -8.50976 | -46.3865 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2febc3f-6197-3d6e-9f02-c6e1e7266e0b | -13.26313 | -47.18287 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bea2fbf-1631-3b24-b052-de39b742d45a | -12.44575 | -45.55251 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e47f9071-ddbb-3ff7-a28e-51169c78665d | -13.35038 | -47.18695 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef035bf0-5c04-328b-84d2-f32545d2d210 | -13.07282 | -47.89807 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d064a4cb-f652-361c-b01f-0ce68cc12f56 | -11.80849 | -45.12861 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8cc8ea1-1951-3fe8-9692-7eb8c2cb8cd3 | -11.48429 | -45.03772 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e255d885-31f1-3a8d-933d-114b6d9e1e9a | -13.06366 | -47.89878 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e51e7526-31af-3165-9000-de0e113fe041 | -11.15581 | -47.92967 | 2025-10-06 03:36:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba2aa044-deb6-38da-9443-cce536b894f2 | -13.24528 | -47.80901 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e9a9ce34-eebc-3f84-b27b-7f7a1be08195 | -13.07782 | -47.83319 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 931ea775-8685-3b59-a809-516e53b3bf2b | -12.89341 | -47.30724 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ee05599-a2dc-3a0c-aa19-c4b6c88858f5 | -13.26231 | -47.63486 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1d7c3ba-9de2-3f7e-aaed-d48f27a0cd40 | -12.44491 | -45.55674 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2ab57244-100d-3214-a4c7-aa5ea4ccf1bd | -11.48497 | -44.97307 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c03289a-eb2f-3a50-bcf5-f4430af70610 | -11.80457 | -45.12558 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fedaffcd-d34b-32c8-bd75-11ab7d96c51a | -10.27687 | -44.36345 | 2025-10-06 03:36:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b472b06-2ecd-3c5f-b935-8080fe0e0d2b | -13.08298 | -47.88232 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 639ebca5-47e3-38a6-b98a-3a5f2483bb13 | -13.27305 | -47.58289 | 2025-10-06 03:36:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 974a4c66-ef39-3978-a317-65487e8957ec | -13.23746 | -47.81374 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d46f9d27-53f6-3f0b-80d9-1fd03d4d6078 | -13.07126 | -47.89541 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b33936ad-6c9e-3dd8-a13e-566652e2ce6d | -12.24733 | -49.20195 | 2025-10-06 03:36:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d70ace2e-3efb-3fca-b934-df989c4723ac | -12.48197 | -45.55149 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7387375f-7a6b-347f-8e07-4608c7814fe4 | -7.71637 | -46.25838 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6686a3b7-43f2-36a5-b899-3e7d2f518b99 | -8.5686 | -46.25456 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e97625c6-5e64-35e0-93e3-ce6a24a0059e | -13.10323 | -48.00373 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9a5d4c84-fa9a-3df8-a7f1-504074d0061b | -10.27545 | -44.37086 | 2025-10-06 03:36:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7dc9f38c-f609-33e3-b715-02a29ccd8304 | -9.39013 | -45.87122 | 2025-10-06 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88de660b-6059-379c-aae5-19ec6d0a47e7 | -11.01629 | -46.53256 | 2025-10-06 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 136a0b0d-b8c2-3fc9-947b-89cd8e46d2c0 | -13.36316 | -47.25096 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8efdba79-0605-38b2-bc8d-06a06b828885 | -12.44814 | -45.57078 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc797296-9387-3dc6-993f-bf19dbc1d4e6 | -13.35318 | -47.19161 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 403cb528-b56e-3408-bd87-f2a5152748f5 | -13.27073 | -47.17791 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 841cb79e-2779-3126-a66b-54acf87c1008 | -11.05306 | -47.77153 | 2025-10-06 03:36:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60854e8d-f2bb-31f4-b1b7-76d1b5e7d7b1 | -8.56079 | -46.26023 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbe5deb6-a606-38ec-9522-83050995b0a1 | -11.80202 | -45.13151 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19aff364-12b0-3aa9-a72a-4eb50976784b | -12.48276 | -45.54774 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 46799772-2c32-3863-bc0c-b53befdc7d42 | -8.72102 | -41.68615 | 2025-10-06 03:36:00 | NOAA-20 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a270ab5c-d3c6-3a0e-8fb9-afe54e3afd90 | -12.24952 | -49.20152 | 2025-10-06 03:36:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d27c978-aeb2-30a7-ba37-03dfe20f9de9 | -13.37349 | -43.62481 | 2025-10-06 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69b3dec3-9ce4-3def-8fbf-51344ba3b13a | -12.39315 | -45.006 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3aecd169-2334-364d-9e86-ca71ac957bc8 | -11.86359 | -44.94757 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5769424c-6636-3418-b20c-6b6926739f79 | -11.44762 | -44.95312 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83e59f8c-6fbf-3247-9c2d-0c9fd76ba40f | -8.16687 | -43.34141 | 2025-10-06 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 35e3cede-571b-3a04-9316-1498925ae9b7 | -13.3555 | -47.19377 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6dac6aaf-2c63-3ba3-800b-b13728336be7 | -12.48358 | -45.54353 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 404085e1-1202-3ee8-ab5f-d237f1458006 | -12.21914 | -44.24224 | 2025-10-06 03:36:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bcd585b-5621-3fe8-bb9f-2f6046ee3134 | -13.2913 | -47.81692 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab1bd5a5-b094-3c1c-b081-61b800302424 | -13.35798 | -47.24434 | 2025-10-06 03:36:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0d326a5-1aaa-3bf7-a003-43eae68dea95 | -11.86147 | -44.94426 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb29290c-7638-30dc-aa45-93da32f112ae | -7.71677 | -46.26381 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 58a68a1f-8b23-353f-bbad-4597fe491efb | -11.91764 | -46.64071 | 2025-10-06 03:36:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0097d31e-302e-34fc-abf9-fa48ce595d47 | -12.48194 | -45.55194 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 456e210c-4ecb-3921-8ba4-c63020322337 | -8.60801 | -46.29284 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a217ec2a-cd26-3d0e-abe8-e2a75ae75c25 | -13.07607 | -47.88258 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 75a2f4aa-2b37-3bb8-9a71-f719e3a7ad55 | -8.51737 | -46.34675 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b735a312-b2d3-3d02-8622-a4860ade0008 | -7.79733 | -44.1368 | 2025-10-06 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d29b67ad-d410-32f9-a73e-48f63b7a147e | -7.9952 | -45.47806 | 2025-10-06 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 01641d15-2da3-3f04-bbf8-4e0c3db03417 | -12.58292 | -46.73937 | 2025-10-06 03:36:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63f7ed02-00cd-3014-a555-18f0bfb8540c | -11.71601 | -44.30531 | 2025-10-06 03:36:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70b3976c-33af-3e6d-b39e-f36a185b9880 | -11.9065 | -46.22183 | 2025-10-06 03:36:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06ddea5e-1587-3364-934c-c56237a384be | -8.87187 | -46.80268 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73d1c469-ad4a-363a-914e-0d4e6e7bceb5 | -13.04774 | -47.91942 | 2025-10-06 03:36:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47da0878-9f34-3d61-b3d5-f177fc9e8874 | -11.85877 | -44.94239 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fa122d3-e3db-3fcd-99a2-9abe5070cb25 | -8.63603 | -46.3214 | 2025-10-06 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aeeb6d45-d379-31fa-b59f-669a76412542 | -13.85575 | -43.99194 | 2025-10-06 03:36:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42fa855b-158f-3825-b071-93ab577cae29 | -8.15935 | -43.34254 | 2025-10-06 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2038249-e2f6-33c5-b919-e0a4f1c4013c | -12.44741 | -45.51382 | 2025-10-06 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 767a0152-86ce-3870-90ea-899e4b64bade | -11.79808 | -45.12843 | 2025-10-06 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README15.md)
