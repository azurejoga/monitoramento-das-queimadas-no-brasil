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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb729973-2fad-3a77-a7f1-67d2d632b6cb | -21.0273 | -48.7593 | 2025-03-05 00:30:00 | GOES-16 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.5 |
| 63c95eb1-45ae-3dba-902c-5e6a71a8b0c6 | -20.2962 | -50.9806 | 2025-03-05 00:30:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.9 |
| ed41e56b-894e-35a5-84f4-0ceded52e498 | -20.2967 | -50.9581 | 2025-03-05 00:30:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.5 |
| 44f10e7e-20ac-3d59-98e1-92877c1e9774 | -22.67957 | -42.86242 | 2025-03-05 00:32:00 | TERRA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| d8ae3f20-7078-3b67-938a-c096755462d9 | -22.96166 | -42.90715 | 2025-03-05 00:32:00 | TERRA_M-M | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 21f4866e-0357-3d47-9f88-f6186904a670 | -22.68716 | -42.85136 | 2025-03-05 00:32:00 | TERRA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| e71815bc-6d59-3490-8a1f-714ff8b97fc5 | -22.67826 | -42.85279 | 2025-03-05 00:32:00 | TERRA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| c4b556db-635e-3ef2-a2b1-4b7788a01b90 | -22.7688 | -42.8417 | 2025-03-05 00:32:00 | TERRA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| cd81f10c-f934-3729-8058-c8b954f79067 | -22.89984 | -43.75529 | 2025-03-05 00:32:00 | TERRA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2cb18a91-ce89-32e3-8394-b2d72385397a | -22.8802 | -42.57565 | 2025-03-05 00:32:00 | TERRA_M-M | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 6e02840d-fb84-3233-9daf-afe59abc1d39 | -23.20561 | -46.40707 | 2025-03-05 00:32:00 | TERRA_M-M | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| ae20235a-3963-31de-a680-763fbe010ba3 | -20.10276 | -44.01079 | 2025-03-05 00:32:00 | TERRA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| aae394d1-932d-3a87-9dfb-578265cfe035 | -22.88151 | -42.58525 | 2025-03-05 00:32:00 | TERRA_M-M | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 096dfc22-8f44-3a5c-82e4-7b556651c829 | -22.84244 | -43.59972 | 2025-03-05 00:32:00 | TERRA_M-M | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 04a6182e-57ab-3553-b302-8c6133dbb56b | -22.33341 | -45.89977 | 2025-03-05 00:32:00 | TERRA_M-M | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 9c1776d3-1053-359e-8c56-c5890c777325 | -11.82694 | -43.82352 | 2025-03-05 00:34:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a07e9126-baae-387f-bafb-289ed262a324 | -9.85751 | -38.00483 | 2025-03-05 00:34:00 | TERRA_M-M | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 656fb3a5-4a55-3726-aa46-210be25171e9 | -14.08248 | -44.1366 | 2025-03-05 00:34:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 448318db-0d6a-3ad1-a5ea-5f80f8e1a455 | -19.68244 | -45.3754 | 2025-03-05 00:34:00 | TERRA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 33926cfe-7f19-39ed-91e7-6ff7444b24af | -20.00468 | -45.40406 | 2025-03-05 00:34:00 | TERRA_M-M | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99554517-abb3-3c70-9eea-de711dc23acc | -6.96957 | -43.0163 | 2025-03-05 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 2ee7d034-c225-3586-9f98-333a4dc95783 | -8.37487 | -43.98315 | 2025-03-05 00:37:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 10c0d3bd-04a3-3ebc-a051-031184190c95 | -6.96579 | -43.01185 | 2025-03-05 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 73efe9b9-8339-3403-b282-b9930e581887 | -20.2758 | -50.9846 | 2025-03-05 00:40:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.2 |
| 89b041ed-e3d8-3cd2-bc0b-fc335c3ad86a | -20.2962 | -50.9806 | 2025-03-05 00:40:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.5 |
| da9b9ca0-170d-30b6-a266-b7cd32064de9 | -20.2962 | -50.9806 | 2025-03-05 00:50:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.6 |
| f77d35d6-8729-3624-9b8a-0e23feb557ae | -20.2967 | -50.9581 | 2025-03-05 00:50:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| a7f23083-af53-37bb-be82-b6bb045a47f7 | -20.2758 | -50.9846 | 2025-03-05 01:00:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.4 |
| a98f9837-4ec5-3e63-8b35-a8a9757f7799 | -20.2962 | -50.9806 | 2025-03-05 01:00:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 149.5 |
| b2d11c61-c690-32e4-ad9d-4837f2b984ac | -20.2967 | -50.9581 | 2025-03-05 01:00:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.2 |
| 8b027509-1deb-33be-93e9-ffbc18772d33 | -20.2758 | -50.9846 | 2025-03-05 01:10:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.6 |
| 6f2bb269-a522-3c13-b291-62a9e80ad51c | -20.2967 | -50.9581 | 2025-03-05 01:10:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.7 |
| 4dd204a4-dac2-3a9a-a6ec-71986b2a3c8a | -20.2962 | -50.9806 | 2025-03-05 01:10:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 159.9 |
| b0ae3b3b-94c5-3d33-97e5-3e82e0c7d35d | -20.2962 | -50.9806 | 2025-03-05 01:20:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.4 |
| 5567f302-4919-36d8-8236-ab5b0f177f96 | -20.2967 | -50.9581 | 2025-03-05 01:20:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.9 |
| 877c2991-09e5-3a75-bf51-143d28529a64 | -20.2758 | -50.9846 | 2025-03-05 01:20:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.7 |
| 9656308e-4ba1-3d62-add5-2b15d6fe7440 | -20.2758 | -50.9846 | 2025-03-05 01:30:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.0 |
| c4806ac6-ba3d-3dfb-9716-74a73cfe6389 | -20.2962 | -50.9806 | 2025-03-05 01:30:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 125.6 |
| dce38da4-9bb1-3fcb-b882-c3659b2898b6 | -20.2967 | -50.9581 | 2025-03-05 01:40:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.8 |
| c7838ba9-e131-3ab2-9626-d9041c88747e | -20.2962 | -50.9806 | 2025-03-05 01:40:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 178.5 |
| a0513275-12bf-350f-9589-fdfb68e6c73f | -20.2758 | -50.9846 | 2025-03-05 01:40:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.3 |
| dde28e0b-8f55-3991-b669-a5e9a5041774 | -20.2962 | -50.9806 | 2025-03-05 01:50:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 154.1 |
| 61e52167-7076-35f2-a5ba-71174c6bb5ea | -20.2967 | -50.9581 | 2025-03-05 01:50:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.4 |
| 795a2c3f-fb07-3fa8-b7ba-95300939264b | -20.2758 | -50.9846 | 2025-03-05 01:50:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.5 |
| e85787d5-b1fa-35d1-ae41-65ffc6036e1b | -20.2962 | -50.9806 | 2025-03-05 02:00:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.9 |
| 7661f7f2-d64c-3783-af11-84a19d13d2a7 | -20.2758 | -50.9846 | 2025-03-05 02:00:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.2 |
| 15a6c046-61b5-30ae-94b7-e18f3726f9f8 | -20.2967 | -50.9581 | 2025-03-05 02:10:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.1 |
| 06b8de1a-c801-3508-a275-cdadb903b465 | -20.2962 | -50.9806 | 2025-03-05 02:10:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.9 |
| 0928c528-44af-3b12-9502-5f0b31ab397e | -20.2962 | -50.9806 | 2025-03-05 02:20:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.0 |
| d562cadc-f859-3acc-8cfa-307a9fb009c4 | -20.2758 | -50.9846 | 2025-03-05 02:50:00 | GOES-16 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| 1814e321-c667-3625-a114-465e184043d2 | -6.99571 | -34.96957 | 2025-03-05 03:17:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fa94de90-f9ab-3fd6-862e-e9ae7257267b | -11.95281 | -37.83274 | 2025-03-05 03:17:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fcde7d4a-c2a3-3b23-a833-1273d50e235a | -9.85525 | -37.99652 | 2025-03-05 03:17:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6c65938-e731-3912-98aa-99bdfb630ea3 | -9.3443 | -43.08738 | 2025-03-05 03:17:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a1fee7d6-2314-3263-ab75-12bc09dbaa3c | -17.67864 | -42.74284 | 2025-03-05 03:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 247fbeb7-163f-36bd-bb12-16cb1a62ae1f | -22.84149 | -43.59693 | 2025-03-05 03:21:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f2277b28-6f50-37a1-b77e-a5ea1d491c11 | -22.67295 | -42.86716 | 2025-03-05 03:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| dfd86a0c-ba61-37bf-b5f3-84c97d0c6de3 | -22.67459 | -42.85988 | 2025-03-05 03:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 7965d76a-c5e3-3192-88c8-ec7e06cc2e46 | -22.67377 | -42.86351 | 2025-03-05 03:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| dc9890ca-62f9-3d43-8a9d-14eda660d6e2 | -22.96427 | -42.90912 | 2025-03-05 03:21:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| db104601-7007-31e1-a02a-319d50473b61 | -22.68154 | -42.85397 | 2025-03-05 03:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| ccd43a77-dc91-3fdd-9dad-7e4f8c5ab898 | -22.67827 | -42.86854 | 2025-03-05 03:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1ac560b1-413a-3038-b952-1913552c428e | -22.87964 | -42.58139 | 2025-03-05 03:21:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 336210d3-15c1-3d24-b08b-a2505da2996f | -22.96509 | -42.90549 | 2025-03-05 03:21:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1da1cf5f-8af9-3ca4-a435-1494e6112123 | -22.96218 | -42.90489 | 2025-03-05 03:21:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5b403687-b396-33a0-8507-1a85a0616d9b | -22.76938 | -42.8376 | 2025-03-05 03:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 58f47ec0-f68d-30ef-8f27-e2ba92fb426d | -22.77143 | -42.84182 | 2025-03-05 03:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b765603c-7d14-3dd3-90cf-c4f12a274bfa | -22.88041 | -42.57792 | 2025-03-05 03:21:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cec886c3-c265-34f9-a795-f99ebd056408 | -22.96138 | -42.90855 | 2025-03-05 03:21:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b4bf0027-32fb-3cdd-ab4d-bc286a4a25d0 | -22.84672 | -43.59969 | 2025-03-05 03:21:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b4e12dfb-f288-3660-a247-f82b302a05a2 | -22.79103 | -42.8046 | 2025-03-05 03:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 30fba9f4-ffcc-338e-a9b1-57293c92e6fb | -22.77225 | -42.83822 | 2025-03-05 03:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 643fe165-0a71-32a6-a0ff-e4dddaada6a7 | -5.24705 | -36.19985 | 2025-03-05 03:42:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a87e4a03-897b-37ee-b5b1-47b04b0bc74d | -8.07219 | -34.97699 | 2025-03-05 03:42:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 115c65ad-d07d-3b81-b696-34ade0458f42 | -7.2431 | -44.78493 | 2025-03-05 03:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1bac091-1efa-37cd-98bc-a39aff6cad79 | -5.24368 | -36.19932 | 2025-03-05 03:42:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22c974c1-59ad-3edc-904f-0e33b85b73f6 | -7.47752 | -34.84466 | 2025-03-05 03:42:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e8fccbe6-85ac-30d0-a6ac-1e694c1c5429 | -7.09324 | -44.38496 | 2025-03-05 03:42:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce76bbef-302b-3711-9a0f-faa73fa1ae65 | -7.24371 | -44.78151 | 2025-03-05 03:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 329a094c-8dac-3dd0-acd0-70b6056f494d | -7.24792 | -44.78929 | 2025-03-05 03:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b58a5b33-fbfc-3d7c-b434-46becba26333 | -6.16992 | -35.30403 | 2025-03-05 03:42:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5e9f59cf-19c2-34e4-9c48-4aefdfff05d9 | -7.09847 | -44.38623 | 2025-03-05 03:42:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d03ce1d9-3090-3217-a5db-905a5e6bc321 | -7.24249 | -44.78838 | 2025-03-05 03:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3013f0c9-5fde-365d-8f0b-3a51deb09c34 | -8.07552 | -34.97751 | 2025-03-05 03:42:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 297afb73-8d0b-3eea-b944-b8e12c6e22ef | -14.90817 | -45.17793 | 2025-03-05 03:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78edc481-c425-3712-a61f-a1a1aa5d1bd1 | -14.08574 | -44.13717 | 2025-03-05 03:44:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fa873c1-06e5-34f5-825c-ba8410137b81 | -9.05892 | -36.82124 | 2025-03-05 03:44:00 | NPP-375D | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b0d6921a-1497-37b6-b061-dd332128a99d | -9.34152 | -43.08319 | 2025-03-05 03:44:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6bcae664-4cfa-3778-bab1-71365360478b | -11.89521 | -38.35674 | 2025-03-05 03:44:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fb5aa41b-4fe8-360b-a18d-2f71cf15db31 | -10.69508 | -37.05022 | 2025-03-05 03:44:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 32672a0d-0680-39c3-81ce-5eed29b3409e | -9.34619 | -43.08398 | 2025-03-05 03:44:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0439eeb1-2b79-35f8-9a1b-7f3f389c69b2 | -11.82958 | -43.82308 | 2025-03-05 03:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2057dc4-5f6f-30e3-8423-cc0831e62647 | -12.86151 | -38.36657 | 2025-03-05 03:44:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 08f9d4ec-9475-3a41-8d24-af0106229a1d | -9.36656 | -40.44167 | 2025-03-05 03:44:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7923f89c-5f8e-3aae-b50b-7214e226e148 | -9.85613 | -37.9972 | 2025-03-05 03:44:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6c24fbc1-c13d-3612-9bf6-608540d41f14 | -14.08436 | -44.13895 | 2025-03-05 03:44:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6d057c1-3146-3632-8a7d-13ffae40612f | -11.95641 | -37.83364 | 2025-03-05 03:44:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8890d86e-261a-3601-b9fa-6fd2c739f202 | -18.04103 | -39.92652 | 2025-03-05 03:46:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4f862a7d-d68b-30ff-b110-ce048d99ae42 | -21.61344 | -48.47567 | 2025-03-05 03:46:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 856e3682-8ce8-3e47-a4d2-06295eb82ef9 | -20.73278 | -42.70155 | 2025-03-05 03:46:00 | NPP-375D | SÃO MIGUEL DO ANTA | MINAS GERAIS | Brasil | 3163805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README2.md)
