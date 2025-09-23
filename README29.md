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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82b9d6a6-75ef-34b9-b4b2-b0b4fe4aa1dd | -13.2535 | -43.752 | 2025-09-23 13:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 85615c65-0c26-3df8-bd1e-13c9c48dc780 | -11.4233 | -44.9331 | 2025-09-23 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| f9b1d24b-3d79-3506-ae7e-7a94c2eeb9de | -10.8319 | -46.0889 | 2025-09-23 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 350b6ca6-512f-3d1f-af58-6de7c00bfe1e | -12.8879 | -44.6378 | 2025-09-23 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| b8ca9f81-0d28-3de0-bbed-a218854472d2 | -11.9104 | -43.4319 | 2025-09-23 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 709e743f-f3d8-3721-99a6-c8ed788456fc | -8.1472 | -44.4633 | 2025-09-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 3cccb25e-fd43-3104-b84d-9fb3963ab1ff | -13.2535 | -43.752 | 2025-09-23 14:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| cecab5ef-1df5-3750-a5c7-4cd184b426a4 | -5.3884 | -42.2588 | 2025-09-23 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| cb5cd7ea-ea65-3063-96b6-0c9d6cd627a6 | -10.313 | -45.2219 | 2025-09-23 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a4573509-06e8-305b-8198-58ffed9ee304 | -11.6639 | -44.3171 | 2025-09-23 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| af59ec68-92a6-3220-a5ff-bbafe6ff595d | -11.4041 | -44.9359 | 2025-09-23 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 6bb427c5-6caa-3ce0-965e-71a5691d13df | -11.4866 | -43.5219 | 2025-09-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b8e1a835-c397-351f-9788-bc4457551f5e | -11.9301 | -43.405 | 2025-09-23 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 6482caa0-cc4e-327b-823e-93f62abea2eb | -6.3412 | -56.2009 | 2025-09-23 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 1659acf1-f1e4-3ad5-b29f-d0a807e593cb | -11.4857 | -43.5692 | 2025-09-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 0cf6c18d-7ebc-3ed1-af97-280bc32e914e | -3.8002 | -41.6947 | 2025-09-23 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 187.9 |
| 38b52367-63a6-34a5-bc20-27eb6dfc4142 | -10.3127 | -45.2449 | 2025-09-23 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d774601c-7a87-34ff-b2f0-de3767d44b76 | -10.8319 | -46.0889 | 2025-09-23 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 27983ec4-4f91-3b30-918b-5f14a7a2741b | -11.4037 | -44.959 | 2025-09-23 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0993b0ae-22a7-3b56-8fc7-0ffead3c0b5b | -8.8274 | -43.0586 | 2025-09-23 14:00:00 | GOES-19 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 152.5 |
| d5863dd3-173e-38ae-bb56-d1103c59dc6a | -8.2803 | -44.3801 | 2025-09-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 42a51bdc-33d5-3b01-80bb-e435da73b95e | -8.9399 | -44.492 | 2025-09-23 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 6a61b965-9b03-3bb1-9ee5-945e33106386 | -11.6826 | -44.3376 | 2025-09-23 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 187.3 |
| ad1db2d6-e4d1-3f64-91ab-e86a7eae1ec3 | -12.8879 | -44.6378 | 2025-09-23 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 7adb567a-3ac8-3cb6-9eb3-41a6feae07df | -11.4233 | -44.9331 | 2025-09-23 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 2fb397de-c140-3f69-84b6-ce9557666502 | -11.9104 | -43.4319 | 2025-09-23 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| c2aecce1-3e0e-3c78-936e-8c3271b1ae88 | -11.9296 | -43.4288 | 2025-09-23 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 8f65cd68-b361-3c49-b602-90817964f950 | -11.4097 | -43.5336 | 2025-09-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| fd44d8ca-5d0b-31b2-b775-dcb0df071730 | -8.9588 | -44.4898 | 2025-09-23 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 134.6 |
| a66fac24-7518-32b2-9b47-3029ec9c1332 | -11.5233 | -43.6107 | 2025-09-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 7431c7f9-9434-3da9-a35e-c2e17d0f6c1a | -5.8088 | -43.4724 | 2025-09-23 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| c8c2f84a-3b70-34dc-92cf-73290397b8e4 | -11.6826 | -44.3376 | 2025-09-23 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 2daed27d-41b8-319f-8043-378b6f09d9c7 | -8.8274 | -43.0586 | 2025-09-23 14:10:00 | GOES-19 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| e85700b7-6739-3931-9de8-c52e0b9ae2fe | -9.1937 | -45.2886 | 2025-09-23 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 74a09b5f-65e1-3e99-b3a4-385eb315ff75 | -11.9296 | -43.4288 | 2025-09-23 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| f4188a69-7daa-34d9-a0fa-b6003076c629 | -10.3127 | -45.2449 | 2025-09-23 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 2082ed57-9471-37c9-9c3f-e87a1fa00c33 | -10.313 | -45.2219 | 2025-09-23 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 7fc25de1-bb77-3714-8cc1-9499de034c9b | -11.9493 | -43.4019 | 2025-09-23 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 2f6b64c4-f4ba-35f2-a5d7-d9a375efebf2 | -3.8002 | -41.6947 | 2025-09-23 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| b211629f-b14a-35f5-a3c2-98ae57317aea | -12.8879 | -44.6378 | 2025-09-23 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 265.3 |
| e1f3e4fa-12ba-3051-b415-0acdab948acb | -8.5179 | -44.9749 | 2025-09-23 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 382.7 |
| 2f812663-ab32-3c57-9a0a-601101f2b404 | -10.3317 | -45.2424 | 2025-09-23 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 657fed98-1e2d-3de8-91ae-bdfdcc71ec10 | -12.8685 | -44.6409 | 2025-09-23 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 3090e8d6-dae2-3640-ba84-005ceae5afb8 | -8.8087 | -43.0372 | 2025-09-23 14:10:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 1716a1de-dd91-3cee-abad-90db8a70fb26 | -8.9399 | -44.492 | 2025-09-23 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| cb7098dd-b580-3e09-b375-d8a2f6b29875 | -11.9104 | -43.4319 | 2025-09-23 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 950d1a77-9328-38c9-a0c4-83348287199e | -5.3884 | -42.2588 | 2025-09-23 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| fc69a59b-91b9-3ebf-ab3c-61573564c373 | -8.9588 | -44.4898 | 2025-09-23 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 24fd3f9c-9dad-3059-8605-90ca0e4ffcca | -11.4233 | -44.9331 | 2025-09-23 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 99e6457c-12bd-30eb-8de9-06ccab5f6a2a | -11.6442 | -44.3434 | 2025-09-23 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 41a0f73b-2d0f-3ccd-9aca-39acb30915df | -11.4041 | -44.9359 | 2025-09-23 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 300d6046-ea87-39da-8865-f199f26f6e2d | -11.9301 | -43.405 | 2025-09-23 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| e45cbaac-7be0-3467-9714-509b88ac8703 | -11.4037 | -44.959 | 2025-09-23 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 2fb72677-1d71-3ccc-b2eb-0f6137f5613c | -13.2535 | -43.752 | 2025-09-23 14:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| c1441258-891a-382c-90f1-0fd33508cc3e | -11.9301 | -43.405 | 2025-09-23 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 584eaf7e-97f3-3b65-990b-a57eda2406f0 | -8.8057 | -46.0558 | 2025-09-23 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6eb04b04-fb5a-39de-9bbf-4dc007fb0fe5 | -11.4037 | -44.959 | 2025-09-23 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 580706e8-962c-32ed-abb6-691db603cb34 | -11.9493 | -43.4019 | 2025-09-23 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| a8112946-51f1-322b-a1a3-0ffc3f0e0179 | -10.313 | -45.2219 | 2025-09-23 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 13429bad-f00f-3604-9a6a-b1a1c789745e | -3.8002 | -41.6947 | 2025-09-23 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 170.1 |
| d641a82d-8a02-341d-9257-fe93272424c9 | -11.9104 | -43.4319 | 2025-09-23 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 81de2f7e-a892-38f7-8020-f9da289db4d7 | -6.1224 | -44.004 | 2025-09-23 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| b2194750-337b-3deb-83eb-f18d7851e732 | -5.3884 | -42.2588 | 2025-09-23 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| a532682c-27ce-381c-bbc2-7059bdca5b58 | -8.9533 | -46.3099 | 2025-09-23 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 7c1252ca-440f-385a-af03-70bbd836f36d | -12.8685 | -44.6409 | 2025-09-23 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 53daf23e-0450-3f5d-961c-37f254ba2159 | -9.165 | -44.6273 | 2025-09-23 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| ecfd401f-571b-39f0-84ec-618f1c638f1a | -4.7595 | -43.6155 | 2025-09-23 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| ffc6aac4-619c-3489-83c8-acc07ee33c5d | -11.9296 | -43.4288 | 2025-09-23 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| f6bdb0bc-4ceb-34b2-96e3-609ec7d6b8ab | -10.3127 | -45.2449 | 2025-09-23 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 8b0acdbd-92bf-3b91-96dd-03075d1ad70f | -11.4233 | -44.9331 | 2025-09-23 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| f80f3cc9-9fa3-367a-83f9-d882dc817628 | -8.8084 | -43.0608 | 2025-09-23 14:20:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 435.2 |
| 37a77059-4032-30fc-860c-fe10bcfbd340 | -8.9533 | -46.3099 | 2025-09-23 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 01a5c263-2122-3da8-ad66-c0a11ad5c317 | -9.1937 | -45.2886 | 2025-09-23 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| ca51d93f-02c8-3b14-a788-ca5b16ea3172 | -8.9588 | -44.4898 | 2025-09-23 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e420c54a-a004-3b66-bb1a-7a0b86d6fd14 | -5.7668 | -43.9623 | 2025-09-23 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 73271a02-f5f4-3afc-b4f4-e108f40f2c5d | -7.6007 | -44.4952 | 2025-09-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 393809cb-5363-3961-9db2-ed547c296ddf | -4.4777 | -43.8177 | 2025-09-23 14:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 840a746c-8ba5-327d-a091-2094c7e3fe83 | -12.1344 | -44.8042 | 2025-09-23 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| eaa6e33f-dd51-3a16-9d70-8930205e84fd | -3.8002 | -41.6947 | 2025-09-23 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| bde99ff1-d953-3e42-b737-ca25c73a0c1d | -11.4233 | -44.9331 | 2025-09-23 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| e54866b1-b394-3040-915f-41f49b2db28d | -8.2803 | -44.3801 | 2025-09-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c60cfaf4-c76a-3c80-931f-20ac63c265e9 | -5.3884 | -42.2588 | 2025-09-23 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| a2adaf63-7f05-325c-9708-dac1cb28fab2 | -8.5374 | -44.927 | 2025-09-23 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 786ac661-0175-3242-b2e2-d1253dea5b52 | -11.4041 | -44.9359 | 2025-09-23 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 67e0431f-1cfa-355a-b535-a4e397e707f4 | -4.7787 | -43.5447 | 2025-09-23 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5535121e-6129-39dd-a04d-8558922909fb | -7.0628 | -43.8305 | 2025-09-23 14:40:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 5467d41d-e62e-3f0a-9b69-1e8b1684cb90 | -5.3884 | -42.2588 | 2025-09-23 14:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| d525bfc5-4ba7-3669-99c1-eed9b0b108cd | -9.8632 | -46.1182 | 2025-09-23 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 65e50d20-b846-3e38-92a0-1cc66065500d | -8.8091 | -43.0135 | 2025-09-23 14:40:00 | GOES-19 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| ba936bba-6c15-3cc4-a510-d7a68b50fec6 | -12.1348 | -44.7809 | 2025-09-23 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 067651eb-1ead-39da-a8c0-f9e99cc2727d | -9.165 | -44.6273 | 2025-09-23 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 9f547fc0-40dc-37e7-8b9a-dc2638cf1179 | -3.8002 | -41.6947 | 2025-09-23 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 281.3 |
| e6ec7fb1-f2a5-3064-b554-fc1852fbdd5f | -4.4777 | -43.8177 | 2025-09-23 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a4f8b93b-fef2-30d5-82da-1c517df0bab5 | -3.3908 | -44.7428 | 2025-09-23 14:40:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| dcbc6111-7e94-3ebd-b838-fc0a56387709 | -11.4229 | -44.9563 | 2025-09-23 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |


