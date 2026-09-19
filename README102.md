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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ceae0b6-80f2-3386-802b-d785fc89bc7b | -9.25003 | -45.93516 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| dbc393b5-3974-3967-a0c1-9ed63c8364e6 | -10.93439 | -47.84067 | 2026-09-19 11:28:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3b68fded-fc28-3765-bc58-03095527398a | -9.82429 | -46.40385 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| a1595375-a704-37fc-8d95-83cf85a84ed2 | -7.87244 | -45.11332 | 2026-09-19 11:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6af6908d-b300-3493-8793-de67d6f2a755 | -7.52944 | -44.93618 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5f2982b4-1df6-3c2e-a018-4e3715735197 | -5.94968 | -44.81755 | 2026-09-19 11:28:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 5f66a29d-f1e6-3657-8f10-058f167ce084 | -11.33712 | -47.35682 | 2026-09-19 11:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| eb9b4bb0-cc1e-3a3d-b8d5-a421195375b8 | -7.61193 | -45.43115 | 2026-09-19 11:28:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 34b25895-70d2-3081-91be-6faffbf9592e | -7.04755 | -42.08031 | 2026-09-19 11:28:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e89d0c5d-8672-3dec-abb1-36464aa95229 | -13.00569 | -46.98962 | 2026-09-19 11:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fd39fa81-eab2-3687-8eb1-3a48ae79fab3 | -10.15748 | -45.56131 | 2026-09-19 11:28:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 48304ac9-53bb-344e-a8f7-7d5f268a3f61 | -12.96489 | -42.66535 | 2026-09-19 11:28:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| d7418de1-0320-37b4-a0f8-df5483ced865 | -6.4456 | -44.94679 | 2026-09-19 11:28:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a4577929-5415-33d6-8aab-61f3409817eb | -8.29818 | -46.85491 | 2026-09-19 11:28:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| c94e1a46-6cd3-3085-9f84-9cc7c8bb7e06 | -12.58105 | -47.08465 | 2026-09-19 11:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9a308f28-0d8b-3ce4-9dbe-ffa1bc9f8f3e | -7.11471 | -44.04669 | 2026-09-19 11:28:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 1998b568-9228-3427-8839-691444c45bbd | -9.2587 | -46.20542 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3440f986-a345-3151-9cca-93b3f441fb81 | -13.47408 | -43.57888 | 2026-09-19 11:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3efeda3f-1d7f-3667-8762-f07bc833a9cb | -9.99815 | -48.36404 | 2026-09-19 11:28:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a071bf21-edfb-388c-ac7c-c2efc1bb8163 | -11.08306 | -48.28306 | 2026-09-19 11:28:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 9260c647-aac1-32a8-9baa-86e3783554ef | -8.6198 | -41.114 | 2026-09-19 11:28:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3bf6ffd5-94c7-3082-8139-2caf3c0b13cb | -6.97712 | -42.18197 | 2026-09-19 11:28:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| d3923fec-0832-3c73-abf5-37a6cdae93f3 | -9.7483 | -46.08503 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 60ff8bda-38e4-3777-bdbb-17f3b20823ee | -10.12252 | -45.56063 | 2026-09-19 11:28:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8daceb19-2ef9-30dd-9c1d-0ee3348cb650 | -11.90957 | -50.12553 | 2026-09-19 11:28:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 186e824f-16cf-3add-982e-ae09f671bdf6 | -12.71106 | -45.95919 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 34df79b7-b9c5-3d87-8900-292b45fb8272 | -11.46527 | -45.71239 | 2026-09-19 11:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 56a1b9f2-1bd6-314a-a2c8-613ea3b96677 | -12.13034 | -45.14841 | 2026-09-19 11:28:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 19750d6d-9b4b-3521-b62a-5b120e1ec62a | -11.46925 | -47.64589 | 2026-09-19 11:28:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f2410a72-3596-3782-b5ef-bd2cf79364c6 | -8.45072 | -45.8589 | 2026-09-19 11:28:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| c0eb7142-7a8f-3a5e-b479-fa6216bc3161 | -11.84142 | -47.62527 | 2026-09-19 11:28:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2b74b16f-9762-3cfd-9c81-dced4dfc815e | -13.02409 | -46.93523 | 2026-09-19 11:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| b54d2be5-1ec1-3bf6-84c6-f4c5eccbc2fd | -13.23214 | -46.91248 | 2026-09-19 11:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5ed28ee8-2ee1-3c93-bfca-5339433cb31a | -10.76609 | -46.19759 | 2026-09-19 11:28:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 27b9d041-6ff0-38d0-bb66-3bf702efd3a3 | -9.82369 | -46.39774 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 255415f6-bfbc-3090-bd36-ba5fc107ac8e | -11.3404 | -47.35151 | 2026-09-19 11:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5aeeacd2-26d2-3dac-9019-8eb6bf2e88ac | -8.66387 | -45.44252 | 2026-09-19 11:28:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 992eeb71-0a96-3858-8d05-218842a66a77 | -12.85919 | -46.32893 | 2026-09-19 11:28:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 83b5ca81-8473-3390-a573-a61d2d9f1abc | -9.56444 | -46.55656 | 2026-09-19 11:28:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 15cdcb58-bb44-3732-bf3d-6552f9b6a4ae | -7.12638 | -44.02955 | 2026-09-19 11:28:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| a790ae78-ff90-3c55-adb7-a0c46dd9f195 | -12.13512 | -46.97683 | 2026-09-19 11:28:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 678ae939-8312-35dc-8655-042bf8800db0 | -12.70026 | -45.9679 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 638e591d-e8e8-33c1-b714-426e8abbcd30 | -7.46515 | -44.68021 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fa105d8a-fdef-37d7-80b5-4cdfe8cc2848 | -11.47353 | -47.41126 | 2026-09-19 11:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 46b47485-5026-3f5a-b0fe-ae7c98c1d3be | -7.60236 | -45.42978 | 2026-09-19 11:28:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| d26429f3-de26-35da-97e5-f689b9bd050c | -6.12101 | -44.90702 | 2026-09-19 11:28:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1f53f94d-28d5-3a7d-ac93-26be193d2a41 | -11.06405 | -47.95414 | 2026-09-19 11:28:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 40fd2d11-cc8b-3236-a2f2-95ad3c9e82ed | -12.99595 | -46.9878 | 2026-09-19 11:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ef5f86b3-c153-3f5c-8db1-6c43ddf4f0e4 | -13.14139 | -45.24057 | 2026-09-19 11:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4198e9cb-8033-3115-9606-d6095b59aa4c | -12.27462 | -49.19161 | 2026-09-19 11:28:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 1eee1617-c71f-3f86-9d98-4aaa2c44fb40 | -6.05748 | -43.76501 | 2026-09-19 11:28:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a261e5aa-ec88-3f29-8cb4-9af55e12da19 | -6.04592 | -44.03487 | 2026-09-19 11:28:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ffc86879-d213-31bd-a4c0-457f4399cd83 | -7.64359 | -46.10729 | 2026-09-19 11:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 801e101b-6e7d-3a94-87ba-9e1242552497 | -8.75986 | -44.21699 | 2026-09-19 11:28:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 601d5c01-1966-3071-8482-4e562e59251e | -13.23384 | -46.90133 | 2026-09-19 11:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b05709f8-de8c-3c6d-b883-b910111e8b95 | -8.47977 | -47.01333 | 2026-09-19 11:28:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 06a3a559-b317-30d6-98fc-329ea870db1f | -9.24452 | -45.95015 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 78c12ac6-71c3-3bed-bfd5-68cc52101ae3 | -11.16019 | -42.7864 | 2026-09-19 11:28:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d6cf6475-4a82-3f11-a153-afc82ed33443 | -8.35763 | -47.57227 | 2026-09-19 11:28:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 312d1fff-d099-3dcc-bc39-7fa0984c786f | -10.96807 | -49.75294 | 2026-09-19 11:28:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 3733502e-3329-3e4e-80bf-92c2538e4fa1 | -9.2613 | -45.92598 | 2026-09-19 11:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b1ce432f-5dd5-369e-8f37-bff80b1db34d | -10.97107 | -49.73396 | 2026-09-19 11:28:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 52e2e7e6-691e-3181-9009-6ad5ee452a47 | -7.86947 | -45.13359 | 2026-09-19 11:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a5245c9c-e11a-35fd-80c7-5d105ead6f01 | -6.67751 | -43.62684 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2d73edef-3e48-397b-99e7-2a4058f1b068 | -11.06898 | -47.94689 | 2026-09-19 11:28:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d8b9d387-b028-33f1-a90c-fdca8e50fd64 | -7.11738 | -44.0282 | 2026-09-19 11:28:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0405c5d3-627c-3c8b-b3e4-11d7852181c7 | -9.96539 | -46.54798 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7d150400-6c00-34f6-937b-7d211634d361 | -8.12541 | -44.82602 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 94248573-b0be-31d7-b0a3-ba8ab78eed21 | -7.75432 | -46.72284 | 2026-09-19 11:28:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2d804720-a992-3779-b380-dba73df604a7 | -9.79066 | -45.05363 | 2026-09-19 11:28:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2e3c2ea5-eac0-3ac5-aa0d-fb02761681b3 | -10.70515 | -50.24937 | 2026-09-19 11:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 31a1bbbf-5831-3698-b310-3a08550f1e7b | -12.70955 | -45.96924 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 3f492f47-fab2-3d20-acec-6a9663e30d0d | -7.11605 | -44.03745 | 2026-09-19 11:28:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 5faf5d43-9f64-3acb-afca-a87b79ac8395 | -6.82261 | -40.855 | 2026-09-19 11:28:00 | TERRA_M-M | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7a1332ab-c745-3925-a407-65b0818c50ab | -7.8597 | -44.87762 | 2026-09-19 11:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5e42f971-ef17-36b1-97d9-3e7338fad85c | -6.30243 | -45.68658 | 2026-09-19 11:28:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b3b8d847-735b-3ce7-b576-b9551b78462a | -13.14279 | -45.23121 | 2026-09-19 11:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1272db50-a594-3551-a4af-398ed9bc4473 | -11.83102 | -47.62359 | 2026-09-19 11:28:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 051dc8e3-3996-3092-a945-c7bb13baac04 | -9.96191 | -46.57108 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 74adcb12-07c4-3e46-9273-c829c02ee6b6 | -10.71562 | -50.25726 | 2026-09-19 11:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| e4711586-5c5f-33b9-bb1c-f5a9cc597a43 | -12.33802 | -50.7128 | 2026-09-19 11:28:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 6d170f3a-c979-3d16-a512-6f93ff137a56 | -9.56264 | -46.56838 | 2026-09-19 11:28:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 34398e2d-4fc4-341b-8d66-b3d00a1e872b | -11.15892 | -42.79547 | 2026-09-19 11:28:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| a5f8bc16-403f-3922-9889-87c20ec0b322 | -9.02985 | -48.72699 | 2026-09-19 11:28:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 2ceb5b33-bec7-385f-882d-cfda178ffc73 | -7.09183 | -42.08648 | 2026-09-19 11:28:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 18c6ee05-5316-3837-9f2b-d4659a6f5f2a | -12.70177 | -45.95788 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| bb1a7f73-2b48-35cd-8aa1-f2e2ec2d0139 | -11.81535 | -46.86061 | 2026-09-19 11:28:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 823e5048-ec77-37ac-8ea1-8ac05413d56a | -9.95547 | -46.54637 | 2026-09-19 11:28:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 32143c6c-dcaf-3107-bf3f-febd80418eb4 | -10.97276 | -49.74015 | 2026-09-19 11:28:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 9d97b527-ff45-30a5-97fa-84e4ae0d0b16 | -12.50503 | -50.02826 | 2026-09-19 11:28:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| de496df0-4d5a-3fd8-89ca-52760e673e5c | -9.00917 | -44.91193 | 2026-09-19 11:28:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 9f108523-3af4-33ef-96c5-430beda55eb4 | -5.95119 | -44.8073 | 2026-09-19 11:28:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b9a61449-148e-3123-a89f-e31b8a6dcd06 | -11.30819 | -46.75404 | 2026-09-19 11:28:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 725fde76-f918-3fe2-88f5-e6269ff16772 | -8.75854 | -44.22615 | 2026-09-19 11:28:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 911bc372-643f-39f0-8b81-e18fb64c371a | -6.98984 | -42.86545 | 2026-09-19 11:28:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 94c77c46-4492-338f-a528-292b26768483 | -6.324 | -45.60862 | 2026-09-19 11:28:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 9ace3975-eed3-3861-a0db-1055227a0133 | -11.41201 | -47.2812 | 2026-09-19 11:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 908fb021-1d95-38dc-9279-64dbbff2acfe | -11.88255 | -47.61179 | 2026-09-19 11:28:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8b73d94d-16b3-30e7-b8c1-d84ab860c4ea | -6.90444 | -41.71266 | 2026-09-19 11:28:00 | TERRA_M-M | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| ff36fff6-9de8-3851-8287-9bfd63d610a3 | -8.96236 | -44.66423 | 2026-09-19 11:28:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |


[Clique aqui para ver as próximas entradas](README103.md)
