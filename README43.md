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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e949496-3bbc-3332-811b-76362aacf456 | -7.85295 | -43.0818 | 2024-10-01 03:47:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a1c51841-b13c-38bb-90b1-73ef6787b870 | -7.85224 | -43.08598 | 2024-10-01 03:47:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 670f282b-f610-3af5-a3ce-8bf6f6da7527 | -7.85153 | -43.09018 | 2024-10-01 03:47:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8f59e78-86d7-3e1d-b6ae-68c564c6e108 | -7.85081 | -43.09439 | 2024-10-01 03:47:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 386c2e6b-2f70-36f7-9dfc-ebe0eea96969 | -7.85009 | -43.09863 | 2024-10-01 03:47:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5ec609f3-0945-3894-806d-76b1da68486c | -7.84864 | -43.08101 | 2024-10-01 03:47:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b3bdcd58-89cb-3d11-b5ad-df4dffadfa4e | -7.84793 | -43.08517 | 2024-10-01 03:47:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e56e462b-c375-39ad-8339-8ee949ed1e6e | -7.84361 | -43.08442 | 2024-10-01 03:47:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4420cbbf-7700-3774-af26-5ee7a113fa8a | -7.76196 | -43.78139 | 2024-10-01 03:47:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3634778-b268-3ada-8e41-b72362deaf30 | -7.69348 | -42.99221 | 2024-10-01 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01a482e8-72fa-350f-afd9-edd5fc9b6ce4 | -7.69275 | -42.99641 | 2024-10-01 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 09b56d52-978f-3161-b198-8b5f4c0d2e4d | -7.659 | -42.43589 | 2024-10-01 03:47:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2895bd6b-8405-3282-8e2a-2a4cd70fc417 | -7.56466 | -41.95544 | 2024-10-01 03:47:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d36be6c6-7c53-37a6-9037-aee922c9071d | -7.28349 | -42.26178 | 2024-10-01 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4aa1975b-9165-3d06-856f-bf13354c4a1a | -7.27936 | -42.26111 | 2024-10-01 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 157fa892-1f2d-339a-b274-a4d5df8df741 | -7.27872 | -42.26485 | 2024-10-01 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b2749edd-3be0-3199-9bd1-42806ceb76e7 | -7.27715 | -42.24926 | 2024-10-01 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 223c5df7-081c-37e0-8564-f598edd3e6e0 | -7.27651 | -42.25299 | 2024-10-01 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e4484255-ee21-3171-b1b6-ede73505ea1d | -7.2765 | -42.06116 | 2024-10-01 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 150b4537-b525-3a03-9070-4c9a89d50f4a | -7.27523 | -42.26046 | 2024-10-01 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e67b511a-89a8-3c9b-9bc7-913d551adbe4 | -7.27243 | -42.06047 | 2024-10-01 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ae910545-ca29-396c-b6cc-2109cf3af27d | -7.27109 | -42.25982 | 2024-10-01 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66c99cf1-d84c-3818-b9c0-1bceebc313dc | -7.24472 | -42.25224 | 2024-10-01 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2636c8a5-6cb8-373a-8573-2d337b74e903 | -3.96451 | -41.51086 | 2024-10-01 03:47:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0a1c8fac-53b3-3839-b16f-c815473f9f21 | -3.96344 | -41.49162 | 2024-10-01 03:47:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 02385924-6ef3-3b61-904f-675949498048 | -3.9593 | -41.49099 | 2024-10-01 03:47:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cdf073b3-4e8b-3e98-965a-ef647a422af2 | -3.95499 | -41.51702 | 2024-10-01 03:47:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9d07bf3b-dd24-3e37-944b-1919e5fc5ecd | -3.95084 | -41.51637 | 2024-10-01 03:47:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f15c63ab-8076-336b-b0da-822847c39abe | -3.95022 | -41.52012 | 2024-10-01 03:47:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d4c3bbe1-8fda-3460-92ab-43cf2979ca96 | -3.9467 | -41.51572 | 2024-10-01 03:47:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fae66c00-dfe4-3d41-b3d0-0469bdf47538 | -3.94608 | -41.51945 | 2024-10-01 03:47:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d746d55d-bdbd-3e9a-8364-9582b60c2480 | -9.94338 | -44.02865 | 2024-10-01 03:47:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a724db0-c67d-3b87-a3f8-ecaca4a62e98 | -9.93738 | -44.03667 | 2024-10-01 03:47:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1405c7e-4b0f-3ce5-98ab-b01ac6767fb6 | -9.93294 | -44.03584 | 2024-10-01 03:47:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21f62908-687c-3678-aa63-d5d8ef46354b | -9.91169 | -44.07798 | 2024-10-01 03:47:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d775716d-a144-326a-be77-2873823baa8f | -9.90805 | -44.07261 | 2024-10-01 03:47:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d792c962-25f9-3ec9-bb12-aa1540892696 | -9.48693 | -44.06204 | 2024-10-01 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15a4e941-d847-326b-bcb1-b804e10965fc | -9.48242 | -44.06137 | 2024-10-01 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f5a7a8e-38fe-3950-82e5-c4504b524f92 | -9.47709 | -44.06528 | 2024-10-01 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f61cdbd-0228-38dc-9840-3d8dfbdbe3b3 | -8.5319 | -44.71679 | 2024-10-01 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cba78d74-c0e1-3662-baab-8e833c3bc175 | -8.53098 | -44.72202 | 2024-10-01 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b233c3d-c946-37fb-928d-13790d8bf1fc | -8.52895 | -44.70555 | 2024-10-01 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8c0e2865-83a2-3b2c-8893-afcab6724a21 | -8.52804 | -44.71075 | 2024-10-01 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 31582226-2075-36b3-b137-ec0ac66833a0 | -10.4758 | -43.64761 | 2024-10-01 03:47:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a6b7102-55b5-34ac-b83f-27119c717b97 | -10.47349 | -43.64854 | 2024-10-01 03:47:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a535392-8c8d-3b97-b288-0ef583c429fb | -10.3804 | -42.59309 | 2024-10-01 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c8faaa8-817f-311a-b09f-563ed87dfbe5 | -8.17639 | -43.66182 | 2024-10-01 03:47:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 612d6b03-c174-3fbd-8627-8bc7002ab89d | -8.17563 | -43.66624 | 2024-10-01 03:47:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 035e382f-8af9-32f0-a4fa-584574b7141c | -7.79571 | -44.17327 | 2024-10-01 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94ef67e3-93fd-347e-8ef2-74153518b332 | -7.79302 | -44.17447 | 2024-10-01 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70c6121c-6780-3df6-9267-16f8f4e52343 | -7.78918 | -44.1689 | 2024-10-01 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b4db2ac-7418-3caa-ae72-39e5c33939f3 | -7.59952 | -43.85149 | 2024-10-01 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36562141-ce3b-3ccc-b6e9-029cf5d8a786 | -7.47276 | -43.85291 | 2024-10-01 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29093c54-8c0f-3b72-998e-a75b83b25f7a | -7.32385 | -43.82083 | 2024-10-01 03:47:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be0ee676-9930-3375-a6bb-89b68bdaff4b | -7.32021 | -43.32722 | 2024-10-01 03:47:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be7a6fd6-fcea-3317-9beb-8cfa04d729b6 | -7.30031 | -43.79288 | 2024-10-01 03:47:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 23eeee17-788a-39e0-a61f-7bcdf07277b4 | -7.27466 | -43.38865 | 2024-10-01 03:47:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb14f575-7871-3957-a341-7e8dd0b63b2d | -7.17775 | -44.22559 | 2024-10-01 03:47:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e743287-100d-37a3-8719-31080928ddc4 | -7.13371 | -44.10754 | 2024-10-01 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1147bbb-0266-3a24-8e03-c229fea5e322 | -3.47153 | -43.35905 | 2024-10-01 03:47:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aab0648-e51a-3337-9706-268897a9fb02 | -3.4668 | -43.35826 | 2024-10-01 03:47:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b65dfb7f-4efd-3abe-8d27-9c71b3f84477 | -8.97644 | -35.20597 | 2024-10-01 03:47:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 03fed41f-5ffd-3ac3-94da-0e0fff84f136 | -8.97587 | -35.20975 | 2024-10-01 03:47:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 60e57e47-89bc-3764-bcbb-2cdb5f0a05f1 | -9.20642 | -48.65647 | 2024-10-01 03:47:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3c31054-0738-3530-9929-5dd77ef812a3 | -9.2056 | -48.6608 | 2024-10-01 03:47:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f90be750-f567-33a1-a3da-900868b90ba2 | -9.20463 | -48.66597 | 2024-10-01 03:47:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0fce7558-685a-32a7-8c88-dcf3bfeba9d6 | -8.77366 | -46.82116 | 2024-10-01 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae3b4375-4551-3948-a3d1-8d1e92bccef6 | -8.76816 | -46.82035 | 2024-10-01 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c84bb095-8cb9-37cc-862b-43b95059d23f | -8.75157 | -47.12868 | 2024-10-01 03:47:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 419bcbf3-d778-3eed-a026-1ae3bca5048f | -8.74529 | -47.13147 | 2024-10-01 03:47:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cc46642-e71d-3ba9-867f-423c70b3cad6 | -8.7446 | -47.13524 | 2024-10-01 03:47:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ddd10ef-86fb-314d-a33a-94ce4d44ddf6 | -8.55056 | -49.60806 | 2024-10-01 03:47:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e29168f-acb3-3b97-9f58-e38b961b3ba7 | -8.46191 | -46.85646 | 2024-10-01 03:47:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6b5decfa-7ddb-3734-bc81-46ad64221c7b | -8.43684 | -47.13597 | 2024-10-01 03:47:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d78b0b6f-26aa-3ece-b17e-dd7a7f9f1895 | -8.43612 | -47.13977 | 2024-10-01 03:47:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 206abf2e-c732-309f-9631-6db905e0f2d4 | -8.43538 | -47.14368 | 2024-10-01 03:47:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9b17451-85b0-3aa6-b000-f256f6507375 | -8.43314 | -47.14122 | 2024-10-01 03:47:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5965a1dc-ac5d-3b64-b54a-fb69b22bba68 | -8.43244 | -47.14509 | 2024-10-01 03:47:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57253069-bcc3-34e0-82b5-2a99a4fae60c | -7.7383 | -49.21368 | 2024-10-01 03:47:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 409f0284-a978-3ba4-9b35-afd2281d46c0 | -7.29176 | -44.97781 | 2024-10-01 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0263f179-3f5f-3d8d-ba5a-113cd9d777fe | -7.0967 | -44.46744 | 2024-10-01 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3477260c-fa7d-3dba-977f-ac0458c5ea9c | -7.0955 | -44.46909 | 2024-10-01 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dab84a41-746f-3933-a34a-417c6a5a98f3 | -7.09108 | -44.54981 | 2024-10-01 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 059136cc-3785-3a7c-83fd-4ab40a72576f | -6.97649 | -47.61619 | 2024-10-01 03:47:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9d414e2-b218-3760-a510-ec2a881c06b5 | -6.9757 | -47.62046 | 2024-10-01 03:47:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c3ddccd-ef97-378b-b500-dddac10d9692 | -6.69185 | -44.53873 | 2024-10-01 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70c18928-a0ab-39f3-b681-8038bafe4d93 | -6.687 | -44.53785 | 2024-10-01 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5eb711ac-bc55-3ccb-802e-77372c2db2c2 | -2.72448 | -46.72315 | 2024-10-01 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 392580b5-9650-3150-83b4-0d155c9219a4 | -2.71849 | -46.72209 | 2024-10-01 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 995caee8-7103-391e-8386-2fc640f2bdaf | -23.0793 | -45.3951 | 2024-10-01 03:47:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| 4ff9eff1-65e6-3da7-8770-a4e277761475 | -10.99296 | -46.52359 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a2e8121-8cd1-3c68-9fd6-3704671e0fac | -10.99239 | -46.52666 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd276928-0d2c-38d0-8f7e-b2ff2fecc27d | -10.99181 | -46.52976 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 31e702a2-5ef4-35ac-8a49-18d07a5bcf68 | -10.99026 | -46.45256 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ec1e268-beb5-390e-b965-68acb244ae20 | -10.99009 | -46.51041 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 179156d7-b5ae-31f2-94b3-2fc0ee3ab13d | -10.98961 | -46.45601 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7bfe97dd-fc52-33e5-bb53-581673197792 | -10.98837 | -46.51957 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8657bc1e-9149-3aa7-b7db-63e0cc5837c6 | -10.9878 | -46.52264 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 424e3f4b-fa19-3f85-93fc-3a3649e7b2a8 | -10.98722 | -46.52571 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 869ac25e-704c-3d2f-94fe-37f943ad619d | -10.98665 | -46.52881 | 2024-10-01 03:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README44.md)
