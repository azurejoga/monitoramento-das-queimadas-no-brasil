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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40ef6b9b-94e3-30fe-8f23-c95f900719a8 | -10.96202 | -45.08928 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33f6c795-440d-33f0-bdbc-2de657aae134 | -10.13209 | -42.07162 | 2026-05-02 03:40:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c1e008a6-c1aa-37bc-a043-ff23174c9647 | -10.98915 | -45.07724 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9dda5fb5-ced4-3e66-bef6-44e0b08216f0 | -10.98759 | -45.08513 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bef31113-95b7-3967-9235-cb8985804abf | -10.98735 | -45.08123 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3060a5f3-78e6-3a96-b921-30a1d4c2f655 | -10.97767 | -45.07513 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| dc30fcc1-5a47-37e3-8f41-356bd80d1af6 | -12.28457 | -44.63104 | 2026-05-02 03:40:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5de616ee-10ec-39e4-ab6d-18714a3f0559 | -10.97853 | -45.09629 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83307567-3f21-33ff-944b-996e295a657c | -10.98085 | -45.08416 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2582a56c-df18-3c28-8e9e-b17ae12c6787 | -13.78294 | -44.10091 | 2026-05-02 03:40:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0a4cf46-8884-35f9-9311-73f01de83b3e | -11.04568 | -44.70232 | 2026-05-02 03:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1ffb19e-cb76-3f3c-825c-aec2fed6a2c8 | -10.98105 | -45.0881 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a05a1c4a-26f7-34ed-bf8c-d8bcf3e648d5 | -10.96778 | -45.09029 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dbda5ea5-822d-3cd3-bc51-474d61fe40d9 | -9.67315 | -43.79043 | 2026-05-02 03:40:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f9b86c10-f878-327a-8540-6e4f2cd3b1ad | -10.98583 | -45.08921 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a10cf575-b5f0-3275-ae08-05ce2d198dda | -11.55555 | -48.2693 | 2026-05-02 03:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebfe1417-eadd-3ee4-b89f-ee4623ef8b7a | -10.97368 | -45.09523 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e8fdd75d-4e22-3048-b919-211c9da71b9a | -10.13245 | -42.06791 | 2026-05-02 03:40:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f20c49ee-5c1a-325a-bc47-0e0e1600c68a | -10.97277 | -45.09529 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8fa4de92-92cd-3651-b4fa-074d3110e832 | -10.96701 | -45.09433 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 86d65105-8ba2-36c2-a72c-3924d3c538c0 | -11.54868 | -48.26794 | 2026-05-02 03:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20c08bf9-d20f-317f-82b0-93372626dc34 | -10.98161 | -45.08018 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bc7a1498-2445-35ec-9c86-f7b5663a4ac8 | -10.97688 | -45.07911 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3f01d2fe-fa65-346e-a728-eadd7f953b10 | -10.71613 | -46.35575 | 2026-05-02 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a014693e-1058-3a51-8162-d7d4a8d9d492 | -10.9866 | -45.0852 | 2026-05-02 03:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 56b64db8-7fd2-3249-b231-13b0acbfacb9 | -20.27689 | -46.44474 | 2026-05-02 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 492fa97f-331d-32ec-a327-8033b7395df2 | -20.19454 | -46.448 | 2026-05-02 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69e8eaf0-90ed-3cbb-b5c7-d408a569eea7 | -22.40879 | -41.92511 | 2026-05-02 03:42:00 | NOAA-20 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5e2cc69d-dfd4-30ee-8f5b-c6c6012d42b4 | -20.28242 | -46.44463 | 2026-05-02 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c8db086-38fb-3377-8c6d-2a3230b11b94 | -20.27764 | -46.44131 | 2026-05-02 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf00a052-7a5a-38f4-948c-b036e12e7e00 | -18.47635 | -48.40233 | 2026-05-02 03:42:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a5579d5-d98d-3697-9b5a-4b8934223d01 | -20.19525 | -46.44469 | 2026-05-02 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3392a67-eee9-3b5d-bb28-79b8cb46a9e8 | -21.2375 | -44.01562 | 2026-05-02 03:42:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c61ba2bd-bf67-3265-9368-e29eb9dfae74 | -18.48246 | -48.40373 | 2026-05-02 03:42:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 08ebf1ed-875e-3a2f-b5c3-6840974a3279 | -20.19913 | -46.45229 | 2026-05-02 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9eb35c5c-df9a-3d4e-921b-9a9799fe24eb | -20.28178 | -46.44757 | 2026-05-02 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a337086-3116-3c56-a902-a51dafba61d7 | -12.3891 | -50.0218 | 2026-05-02 03:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 5b20c8b4-3ca0-31c0-9b7c-8d48f511cb57 | -10.9815 | -45.0874 | 2026-05-02 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| e7092dfa-348d-34e9-8bdd-c790b2e5d52d | -12.3887 | -50.0435 | 2026-05-02 03:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 47be7bfa-dcc0-35e1-8785-5208a26c4a2e | -12.3696 | -50.0459 | 2026-05-02 03:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 4fae5a61-85fc-3ede-abfc-6b3da8d5c575 | -12.37 | -50.0242 | 2026-05-02 03:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 2ca29b9b-4f77-3ed8-8ef4-f9380b397e33 | -12.3891 | -50.0218 | 2026-05-02 04:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| cca30fcc-431b-3bcd-9a9f-aad7514a351e | -12.3696 | -50.0459 | 2026-05-02 04:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 9e3a2109-64a1-38bc-b875-e4158c316481 | -10.9815 | -45.0874 | 2026-05-02 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 16e92dfd-e5c4-3202-b102-770956d07e29 | -12.3887 | -50.0435 | 2026-05-02 04:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| eb94d5fd-66ef-39d2-b38f-05698dd8616e | -12.37 | -50.0242 | 2026-05-02 04:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 820236ee-ecba-3a5c-bd0c-c26e49a706b6 | -12.37 | -50.0242 | 2026-05-02 04:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 85651ed0-671c-3edb-9ead-07335d8eae54 | -12.3887 | -50.0435 | 2026-05-02 04:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 4e357c3c-82ac-3430-be5b-71ceafe41fef | -10.9815 | -45.0874 | 2026-05-02 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| eb87efcb-fb15-343a-90b4-4d51bbe45a56 | -12.3696 | -50.0459 | 2026-05-02 04:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 92abc623-3c40-3a03-9ccb-6d497159025b | -12.3891 | -50.0218 | 2026-05-02 04:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 728b862c-c398-315b-84df-837cd797b586 | -10.9815 | -45.0874 | 2026-05-02 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 15c0a25a-8102-3d98-b510-d670539ff26b | -12.3887 | -50.0435 | 2026-05-02 04:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6b1f3180-c9be-3367-b67e-ea2d31344d0e | -12.37 | -50.0242 | 2026-05-02 04:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| fd230e76-5917-3aee-bfbb-c311ed72d14a | -12.3696 | -50.0459 | 2026-05-02 04:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| bfab7cd3-7cb9-30c7-a6db-e93daa971009 | -10.97629 | -45.09674 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a77b1770-bb0a-3be7-9f1a-5801b12dfec2 | -10.46596 | -45.06799 | 2026-05-02 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48903e66-1305-3d9c-8e47-e5bf63902b06 | -11.06356 | -44.52301 | 2026-05-02 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4eb7aa6-97d7-3473-91aa-f430c333b48f | -11.44466 | -55.10796 | 2026-05-02 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2834a1a5-0eb5-3a04-8459-bcf68bccaba6 | -12.372 | -50.0443 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| ee15a5bd-5cd4-3faf-a2e8-c5573d8c7000 | -10.99286 | -45.07984 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 18415478-e206-30f5-9f64-c7a1d102a5c5 | -10.97286 | -45.0962 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f195e559-89ad-3307-a966-d1869d6153f3 | -12.32993 | -44.59098 | 2026-05-02 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed60a8f5-4104-3322-99d1-b83adf04c509 | -10.9671 | -45.08746 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9ecfc63b-b3ae-3702-8ddf-8373dd7a51d0 | -11.04864 | -44.69971 | 2026-05-02 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28348234-ae6b-3ed8-9046-399a2cecc5bd | -12.37682 | -50.03699 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 76cfa30e-f2c7-39de-b120-9c6dc3155632 | -10.98429 | -45.09021 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f1a3154-df74-3288-bea0-b7a3d2536aa4 | -11.43122 | -55.10009 | 2026-05-02 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aac85774-d8c7-3dcf-ab98-cd8b1081f580 | -10.97342 | -45.09238 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 655e1cf4-2113-3f68-b40a-57853412b8f3 | -12.15267 | -46.22599 | 2026-05-02 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7588d9c9-447a-385d-bcee-7e9c9ef9dff0 | -10.96654 | -45.09128 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 95371547-3aa8-3dc5-831b-9a7640c7c36c | -12.36983 | -50.03582 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1a00d48-249d-3b0e-88c6-c333be991660 | -9.94988 | -48.16386 | 2026-05-02 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c96f220-5fa4-371d-bc9a-fd93ea6cfd7f | -12.37266 | -50.04035 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 320154a0-bd32-3109-8c83-de1174c6ef1e | -10.9664 | -45.09605 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9c40a592-4ae4-381a-a23b-16603e0f4947 | -11.79562 | -43.63859 | 2026-05-02 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d31fad6-cdd1-33ec-b452-9656adf7f360 | -12.36851 | -50.04371 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 260eb307-5028-37c6-acb4-7f8b7cfd18e8 | -11.55687 | -48.26831 | 2026-05-02 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4e42ff06-1005-3e3c-b0fb-5b6ab7bc89a0 | -12.36917 | -50.03976 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d911a74-59d5-38d1-9ea0-2d655c94ad50 | -10.97566 | -45.07711 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 427f2575-a28d-3477-8ef5-2b584b87876f | -10.98717 | -45.09457 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0bf12e2a-fb49-3d28-a8fd-b62478529085 | -10.96942 | -45.09565 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 132d95c4-9e28-302c-be40-a9d7edd9c6e9 | -10.98942 | -45.07929 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 10966c9f-4580-3156-be58-4e53295f98f0 | -10.9831 | -45.07436 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 583759a6-2cd9-35bd-a125-668e235fb162 | -12.37399 | -50.03246 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 49316662-b300-3b0e-a7d3-96cd788fab90 | -10.96698 | -45.09225 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 434ad0c1-fcca-3842-8a34-ad37fb513d2a | -10.97454 | -45.08475 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80297332-7390-3bc3-8852-deda2bd54c30 | -13.78685 | -44.1017 | 2026-05-02 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 869fc37b-2793-35df-8727-bff31f140753 | -10.50341 | -47.11637 | 2026-05-02 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68c19294-2ca8-3739-b0f2-9c9e5e6efefc | -10.97398 | -45.08857 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 619e43cd-51e6-3d88-b8c7-20df2cbe4069 | -11.44946 | -55.10883 | 2026-05-02 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 392a06bf-6f19-3e49-9f80-d03862586588 | -10.98829 | -45.08694 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3a32acb-763a-3ea5-845c-f22b86d35576 | -10.9751 | -45.08094 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 50ec3618-c8d9-3c70-9a00-06a409bb7dbc | -12.38031 | -50.03757 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| aab1c13e-ede8-3b52-b339-da6765885342 | -10.98598 | -45.07874 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c0f993a5-3974-3b22-8d10-2e513bca7010 | -10.96598 | -45.09509 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4d7f5ea0-5f7c-30db-8ac3-515e00bcd179 | -11.04514 | -44.69918 | 2026-05-02 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22a63b82-30c5-31e3-8048-4b2e1f620280 | -12.37965 | -50.04153 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1050c9e1-c30a-39bb-895c-dc7cd2533208 | -10.97966 | -45.07383 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34466e8e-c38f-3b36-9c90-d67b8a42dc67 | -9.6739 | -43.78866 | 2026-05-02 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README4.md)
