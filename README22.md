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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d9a3782-6bea-390f-8a1e-60ffa226584a | -10.95207 | -54.37088 | 2025-06-29 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ce9746b-6684-3071-a562-515617439687 | -12.99427 | -54.67557 | 2025-06-29 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 790569aa-9eee-3c06-88af-2807cb43ccc9 | -15.72475 | -49.5529 | 2025-06-29 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 551e5824-f798-3d09-99f7-768b97d7d8d0 | -14.21845 | -45.50594 | 2025-06-29 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9da01ea-ee04-3b08-be31-a76b53813034 | -11.0388 | -55.37659 | 2025-06-29 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b82e2db0-70ab-391a-b699-86bc562e77e4 | -11.2592 | -52.74305 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e3fe367f-6941-3051-92a8-b69ac43478c4 | -12.09978 | -54.66901 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f6d4dce-9c3b-31fc-8b89-288fe25f5cb9 | -11.55273 | -52.80264 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1bc6e47-de67-3094-b3af-0a665aecdf42 | -9.9165 | -59.91043 | 2025-06-29 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f943dce-451c-3088-9f02-a179a15420ba | -11.01318 | -56.23286 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13409af1-9121-31c0-99c7-63ad0f378baf | -11.2629 | -52.7437 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b59fa0a6-ea53-33be-83b3-dd08c49dd48d | -11.55287 | -52.77968 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5a599b80-137b-370e-b58c-c78a3016671e | -11.53686 | -52.77011 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3914a201-6252-361b-9cb9-3d9eeab03978 | -12.09635 | -54.66451 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76056269-9825-3892-af88-92dad995c42e | -11.5535 | -52.79817 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 26814e59-1c91-3738-944d-35e311c2409d | -11.01682 | -56.28123 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19525f1e-89d0-35eb-a5a9-0e2b99457bda | -11.55872 | -52.78991 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f43f23a7-ab32-318c-b173-5b6ad670dc35 | -12.93247 | -51.56543 | 2025-06-29 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b98f5afd-5fc5-3ca0-9ed5-44187e58e440 | -11.55936 | -52.80841 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12699632-25df-32fc-ab53-5d333147b58a | -11.54687 | -52.79242 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cc1ff4f4-e547-3aff-b6b4-f2a50649cd55 | -11.02515 | -56.26232 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ea201d7-9696-36ad-8f2a-234e6d15db47 | -12.10045 | -54.66525 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 948f17bb-17e0-3791-946e-bfdc90b9b287 | -11.0345 | -56.28959 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1397910d-0779-334f-85d2-b2d7a7637685 | -12.61706 | -54.20939 | 2025-06-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 26644058-ff15-3ce1-94c4-fdf02c59ca88 | -14.66545 | -47.98333 | 2025-06-29 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a1b5bb2-4827-3cf9-9971-31c9697ceba5 | -12.98021 | -54.68415 | 2025-06-29 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7d972bc-5359-32c8-a9ee-a447a8d8162c | -16.57976 | -49.33222 | 2025-06-29 04:34:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f457dce-186b-3351-9dc0-311768e3e07b | -11.02822 | -56.25592 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6c43c3c-d7b7-3e79-a24d-85561bfe840c | -12.05704 | -48.469 | 2025-06-29 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a2e49b6-ffd6-3bc7-af8e-49d86967ab29 | -12.06036 | -48.46953 | 2025-06-29 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32a6fb7d-c0d1-3844-bcf0-757608507a4e | -16.67901 | -43.8855 | 2025-06-29 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38333880-1286-36cb-b5ad-c239efbce286 | -12.76398 | -44.40052 | 2025-06-29 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7281ba63-78e9-3b0c-adc7-1b1deafb44ce | -16.25709 | -53.67493 | 2025-06-29 04:34:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb074c54-cd8e-3832-8203-424244a634d6 | -12.10829 | -54.57447 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55687577-2646-35d9-890e-c44bdc0698a2 | -11.55134 | -52.7886 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 881ff543-f716-324e-86c0-c4e641314688 | -11.54102 | -52.78223 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 09f093e3-583e-3531-ae89-b2a6c4d3438f | -11.53242 | -52.77393 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| baae19cb-d574-376d-9180-410f363d1bce | -11.0227 | -56.26 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b270091f-9b94-3003-bb2f-4c226bddee8f | -13.3046 | -47.51719 | 2025-06-29 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68316c38-7237-3d52-872c-c9521a372664 | -11.01404 | -56.22801 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3b2880f-7769-3b85-8b3c-db0683b861c3 | -11.03634 | -56.27966 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1bb81be-1c14-3e60-a2ec-1c6d2b65a39e | -15.64997 | -49.72775 | 2025-06-29 04:34:00 | NOAA-20 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5a581ce-b179-3c2b-9373-063830320ffa | -15.72751 | -49.55705 | 2025-06-29 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 981c449f-ff8a-33ff-bf2e-4eee2b4414cf | -14.53418 | -53.77085 | 2025-06-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42d25fa0-f199-3e76-94cf-bee5854418ad | -11.56458 | -52.80017 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7fe5831e-35d7-3afb-a8e8-47f65341f1c3 | -12.50362 | -58.35269 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94635078-82fa-390d-924d-ff1358b2e961 | -11.02181 | -56.26497 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9c4e29f8-5ad6-34d8-97f6-1f821d2fe672 | -11.00387 | -56.23137 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbc01e82-4117-38b0-8b94-2b1567793aa2 | -11.54549 | -52.7784 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 0a280493-8ed7-3d71-8fc6-c73bd583d012 | -12.05594 | -48.4761 | 2025-06-29 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d0bcae3b-b7e2-36d5-ae31-f7f7312ffe64 | -11.03169 | -56.27882 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1f122fb-d59e-3f25-a43f-1e978c27f435 | -11.56088 | -52.7995 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f83bdd44-9fd5-3a6f-9df5-a101b3ec0b2f | -12.99831 | -54.67634 | 2025-06-29 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54b914d8-0317-3852-997d-131857b6853d | -12.1117 | -54.57889 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59df3bf1-6038-3e2c-a997-03d0b49b5f38 | -12.04997 | -48.07615 | 2025-06-29 04:34:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3ee2217-7ca7-39e4-8d7d-18b080d9eea4 | -11.02612 | -56.28294 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 637e7255-0552-3e84-821c-37879790d048 | -11.77619 | -54.37122 | 2025-06-29 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28d19fb3-2e8f-30cf-b8a0-5c1476d7fbda | -11.54472 | -52.78285 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 6057099b-6fa5-314f-b7ae-55bb5d0589d2 | -16.34946 | -43.69544 | 2025-06-29 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42a02b94-9d77-3474-858d-e2d42a94ff26 | -11.03442 | -55.37587 | 2025-06-29 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e707629-9366-383d-9db1-4534a40a4636 | -11.55196 | -52.80712 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a29800ce-e32c-3acc-9b1d-af4b59df9ad8 | -12.05981 | -48.47308 | 2025-06-29 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a4950f2-130b-3df1-9b31-9801a5d45546 | -11.54702 | -52.76952 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 8683129c-1b18-38df-bc05-1952f16d0e80 | -11.5461 | -52.79689 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eb087db5-45d6-3118-8945-6f082d846d4c | -19.03125 | -46.58853 | 2025-06-29 04:34:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1196d09b-2e50-3679-a1d0-9538e137e2d0 | -11.5544 | -52.7708 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8f288e5b-7f9f-3079-8414-7b30dc4b0687 | -17.92205 | -45.55849 | 2025-06-29 04:34:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eddea10-a60f-33e9-8a3c-71de286103da | -12.48086 | -58.4697 | 2025-06-29 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db2d52d1-33fa-339f-b6f2-d253a8e64dd7 | -12.09501 | -54.67204 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ad4c5b1-01a6-38f4-9486-a751b01144f7 | -11.0247 | -56.27571 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2d1c5840-9f4a-3ac2-8118-f12574bb8c53 | -11.02147 | -56.28208 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b6aa8cb9-64fa-326e-af85-e55dc70d2029 | -15.94876 | -47.98514 | 2025-06-29 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b3e8916-4001-3aea-b18d-b67f4929ccfd | -12.60648 | -57.87463 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f4fdbc6-bd5c-3c01-b1fa-0153698f93eb | -12.06259 | -48.47716 | 2025-06-29 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d0b0ff4-cf45-365e-a3e7-3f6834c0f55e | -11.55719 | -52.79883 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e029044-5500-309d-ac22-598282c08dcd | -13.01563 | -53.42387 | 2025-06-29 04:34:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 59c2f6c0-cc7a-30d8-bacb-7e71b7513eb5 | -11.04832 | -55.37386 | 2025-06-29 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cf085d7-96f5-3b67-9b20-27877efca182 | -12.76797 | -44.4011 | 2025-06-29 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5a267da-4d7b-33b7-b6b4-84918adb2da6 | -19.31992 | -43.73071 | 2025-06-29 04:34:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a810ece-945d-30cf-8cff-292cf10ebcef | -12.4198 | -54.87036 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6633fd83-745a-3a0b-99f8-0a70f59c8ce9 | -11.54179 | -52.77776 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 46ab0b21-d62b-3e03-8d05-20e4a798c0e9 | -11.2703 | -52.745 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa25fd31-6bfd-352e-9d05-563be2dfc2af | -11.0311 | -56.26668 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06eecb04-41bc-3e34-8d5d-782873bdc58c | -11.54317 | -52.79179 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6f0d87e6-e574-350a-bd44-90c69b040351 | -11.02381 | -56.28067 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80a643e4-9cb7-37fa-90ef-b2a706f8f241 | -17.39866 | -42.62801 | 2025-06-29 04:34:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e3bc4318-cd1d-3bea-9dec-dd50bc8f8b84 | -9.92113 | -59.90952 | 2025-06-29 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c9fdee9-3930-33bd-952f-7cb2f72e1c40 | -12.09911 | -54.67278 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d62ea9d4-dfcc-32b9-94d7-55279f4f2d2f | -11.77279 | -54.36679 | 2025-06-29 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9225cbeb-d582-31a8-8a01-716e9a3ec3b9 | -13.69434 | -47.13088 | 2025-06-29 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1be472ad-acfe-3ce0-987d-839a0f906a0e | -14.88495 | -48.38838 | 2025-06-29 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0b934a2-8f91-3537-bf45-a37a340847f6 | -22.35196 | -45.77353 | 2025-06-29 04:36:00 | NOAA-20 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 24955436-0807-3a1b-ae9b-98adefc56c36 | -22.53927 | -52.96627 | 2025-06-29 04:36:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d7c664d3-6e3e-3f34-91f9-508da1472eab | -23.40566 | -46.55718 | 2025-06-29 04:36:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 696c7b50-fa80-377e-80cc-063355d8524c | -22.19097 | -45.82022 | 2025-06-29 04:36:00 | NOAA-20 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ec164570-1a0f-3d07-9c22-62622dd74531 | -22.58292 | -43.65092 | 2025-06-29 04:36:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bb324956-1cbe-3d8b-a24c-432590b43ce5 | -21.13083 | -48.59089 | 2025-06-29 04:36:00 | NOAA-20 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 853d3f07-84f3-35d6-9416-e93192da0f2a | -21.53486 | -45.46303 | 2025-06-29 04:36:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ea3706bd-e929-3cc1-af43-5f4b71ba4d87 | -23.38771 | -46.46951 | 2025-06-29 04:36:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3d3c44c9-3db6-370f-a69e-9a095588b18c | -22.9954 | -47.11992 | 2025-06-29 04:36:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README23.md)
