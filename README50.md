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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d96b7e3e-83bc-385b-bcbb-85520bc51506 | -11.02058 | -45.42357 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| edbd3f48-58a0-320a-adf5-c1312f6fc8bc | -11.01489 | -45.41432 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b6538837-cb43-3802-9f2b-8d6d4c0b062a | -13.35879 | -43.89951 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22e2ae8b-a143-33fa-9720-0b7962f5374a | -10.04549 | -48.21412 | 2026-10-10 04:10:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fabc3e62-17b2-370a-9d78-72e59336da12 | -10.97798 | -45.2024 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffc25a44-875f-38a8-8407-37387ba6a895 | -14.34176 | -55.01107 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a9b1f9f-085f-3bc5-b015-a53391ca74bd | -14.5327 | -48.03702 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85efe952-6745-33cb-9417-d3aabfdc7267 | -13.81008 | -42.66181 | 2026-10-10 04:10:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e4fa487b-320f-3d55-a46e-352e4bab9c2b | -14.02985 | -48.76023 | 2026-10-10 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 069491cc-04f9-33c3-a2c9-d85973aba83b | -14.79231 | -47.98056 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8d757f5-b8f9-3d2a-9d9b-4156e6a2a4e7 | -11.09122 | -44.11547 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b89e5ff0-6f1a-3140-a5c4-822e4e49b999 | -11.96406 | -43.48484 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43319680-945c-306f-bf44-67ee6bb8efc8 | -13.17545 | -48.12552 | 2026-10-10 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1878f6f6-9fea-331e-8bb8-5ce470ea2162 | -16.71646 | -41.88287 | 2026-10-10 04:10:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 04789092-44d4-3e8b-ad91-d6a6eb6b53ba | -11.88307 | -47.35911 | 2026-10-10 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16a8a7f2-bc5f-35e4-8bb9-5eee591d58df | -14.46124 | -43.94406 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa931d2e-7127-3783-874f-71412f7c6e69 | -14.43706 | -43.92549 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d871d10-261c-37e8-b9df-1e855040cb39 | -15.38144 | -41.91617 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 55bd1db3-1c5d-3d77-808d-69697a9c61cd | -15.3751 | -41.9313 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| b5e5eb57-4138-3b17-a72e-d6c50294c32f | -11.02328 | -44.03062 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8eadfcc6-90d1-39fd-a57b-9e73cd879c1d | -12.33782 | -47.3156 | 2026-10-10 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad8c7e53-a747-3f5e-9d59-6828f5b362bd | -15.26644 | -42.38039 | 2026-10-10 04:10:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 985ea4ed-f0df-380c-8077-292c539260bb | -11.60707 | -43.7411 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3f92320-fb4b-3406-8f31-3ef5aa3f6c5a | -11.86396 | -43.53695 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c839902-3bca-3ac9-9d12-d3e03005c6af | -12.06933 | -47.38226 | 2026-10-10 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6381e916-b293-3615-b613-d35cdc373b4b | -11.03289 | -45.44233 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 014c1e5c-39eb-32bd-82cd-d44895da41bd | -12.4996 | -51.29794 | 2026-10-10 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36411daa-8025-3fa9-adec-981d8e0dc358 | -12.38247 | -46.57809 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f42b3d8-fdde-3f7a-a807-36bb3b96e5c1 | -12.4947 | -51.29699 | 2026-10-10 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b670844-cec9-39c0-a3c8-8bccb3812c38 | -16.60081 | -46.74704 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e396cf8-43c0-31f7-8fb8-27e9b764150b | -11.46663 | -43.38229 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 379f8d92-2a8b-3ee9-8bfb-2867ff095072 | -16.82052 | -42.29773 | 2026-10-10 04:10:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 88497ba8-42b6-312a-8f1c-430b0df4b10d | -15.25188 | -42.36293 | 2026-10-10 04:10:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 44e4ca16-980e-3cd8-b327-3b71ba660ce0 | -11.82535 | -43.5237 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 254962ea-4088-3645-8fbe-29d089f3ec0c | -11.75962 | -46.79799 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f686d907-b8ed-3b3c-850c-8702328579f2 | -11.9773 | -43.46535 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6605060c-d5b6-3299-b2bc-1fb0af9db49d | -11.97289 | -43.47186 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff817798-22a9-345e-9527-1b1b9c99a902 | -12.0582 | -43.40693 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c239b5f6-f002-3b96-9944-1d1dd11366a6 | -16.12425 | -43.75336 | 2026-10-10 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1069d0f0-e090-3990-94c3-04d58b86b413 | -14.45519 | -43.93941 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a31e37a-eb7b-3690-ba43-c2e639f94ae1 | -10.89582 | -44.82638 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8f4ca527-b126-3ddf-b7c0-5d9b68b14173 | -12.37287 | -46.61231 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 894b4fe7-5b7c-3c02-845c-d56886b55138 | -12.29511 | -47.04246 | 2026-10-10 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| baca404c-84c6-3a33-9e6b-130f6d9bd750 | -11.03572 | -44.05457 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 803bd93a-649a-3c12-9e83-787f0b0bf407 | -11.98168 | -43.50207 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6565ca0d-7d37-39b1-9fe6-2a5684d9992f | -15.98498 | -47.34942 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 437793d6-1481-31c1-8ae7-95a4209c9b71 | -13.37371 | -43.89107 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7df16762-e2ba-326e-9069-b038d273f8f3 | -10.6096 | -43.27098 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e85bd51c-92fe-3d29-8638-5a91b5a4b4f1 | -11.08394 | -44.11798 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c434d74b-0374-37a8-9317-e4d048c68f3c | -12.25636 | -44.42984 | 2026-10-10 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3af2e9d9-3d7d-3a08-a683-af8fc4d7744c | -14.45083 | -43.92414 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65bdccfd-37bd-3f72-a28f-65ca7a0c2ecd | -11.02872 | -45.4457 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71c58492-660c-3e97-9e12-1339094afc85 | -11.00284 | -45.39997 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a9d6097-04c0-35a4-9515-9775a6040095 | -13.50359 | -48.60658 | 2026-10-10 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80cd3f9c-38cf-3879-a6a8-cc69baf28e7c | -13.35816 | -43.92485 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5590cff6-0ac7-3f09-8cd1-0406eb0d28cf | -10.45267 | -47.18757 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c548aa67-a22d-375a-a7de-d95e899d787a | -12.50064 | -51.2923 | 2026-10-10 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8d30689-53d0-38ee-ab25-a2ccfd7862e5 | -17.35017 | -42.67846 | 2026-10-10 04:10:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8c601a2-97eb-3b49-9448-9e8ef9bc3906 | -11.08903 | -44.1077 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bad9ef3-a5a5-3e6e-a2d7-196875cb3b1d | -16.07232 | -44.32314 | 2026-10-10 04:10:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddf9f35c-7c1c-3efa-940d-d18e38ddb9c5 | -12.38031 | -46.56875 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ccc964a-d4cd-3ac2-86ad-10024c19aea6 | -10.44794 | -47.19188 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e64e758f-6844-3a9d-96d4-421150aad6a5 | -13.38464 | -43.71502 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1c2efad1-836e-3374-b316-8b660d8709d2 | -11.98502 | -43.45939 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec52fbd9-243a-3fc6-a1af-9e6838c63202 | -14.3418 | -55.0192 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9bfbde0e-59db-39c7-9993-a4d37bb640fc | -16.1182 | -43.74871 | 2026-10-10 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fa5c0df-47ec-3a1e-a66e-ab92741852d1 | -14.45133 | -43.94242 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39981168-abde-32f9-88b5-0e1341e7d11d | -12.37667 | -46.56812 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1197dd7e-25e0-3839-a081-888ce7b1f84f | -15.11911 | -39.92595 | 2026-10-10 04:10:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 26f14fd4-db64-37f6-b5df-f126adcc680c | -11.2552 | -46.35301 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d815ad0-98d9-3be1-a5d8-4de83e69b23a | -10.8946 | -44.83395 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55322d81-6748-3775-bcaa-df265a79a89f | -12.36997 | -46.6073 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2964837-dfef-3e46-9151-421b62794a7a | -11.50718 | -47.60186 | 2026-10-10 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59121e71-30c3-35fd-9dc1-f88de16c01a1 | -15.56514 | -44.51727 | 2026-10-10 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 179a382f-f78b-33c1-ab74-2c87896b3195 | -11.23918 | -46.29207 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02893f19-6143-35c2-8b0f-c6fcd00cd85a | -13.26334 | -44.00758 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8d93bc0-cb61-39ce-a236-4fa8309cccf7 | -9.95528 | -55.33534 | 2026-10-10 04:10:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80aa4406-4efa-3db5-a025-49be1e45cdbc | -12.01966 | -43.4366 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17e8f0b2-a726-393a-948a-ba6af2e26ffd | -14.05719 | -43.82991 | 2026-10-10 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 850a6b61-1641-3ddd-a22f-5ffefa357747 | -17.2109 | -48.97283 | 2026-10-10 04:10:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ada2600f-21e3-3f01-95ba-cb1110fc1112 | -10.99998 | -45.39541 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05d8f5ce-a1fe-3693-b681-b916b1c1cdff | -11.29113 | -45.20064 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b541ddf-5224-31b2-aa1d-2459380c37fb | -11.60437 | -43.71515 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 160c816e-e461-39df-9b45-163029251e4d | -11.97012 | -43.48941 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4628776c-a59c-3372-8da1-41f1432cc068 | -17.45151 | -45.06913 | 2026-10-10 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 302a872d-58bf-3155-ae20-38d68545aca4 | -12.22769 | -44.67308 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63393927-dc8e-384b-b308-660437195ef8 | -16.06838 | -45.25937 | 2026-10-10 04:10:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eecfb2a-d120-3111-83f9-3b22638133ac | -10.36275 | -44.25791 | 2026-10-10 04:10:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f8c859b-2d1f-3d26-983e-14f454a0af1e | -13.36928 | -43.89761 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57561be3-6083-38a9-99f1-7689a7789efc | -11.26181 | -46.35847 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa91b9a7-610a-3ead-bbac-98a8575dc78e | -12.04553 | -43.42287 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cbcc5a4-e1a7-39d4-8114-635e87fa8bfa | -13.37533 | -43.90224 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31799e9e-7396-3df8-81f2-c1af625aab17 | -14.45027 | -43.92768 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b266bc4-3fcb-312d-80b6-7b6dfe2718aa | -11.29395 | -45.20504 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98b5431b-2dbf-35db-ba9c-3f83c8b766dd | -10.49544 | -51.9406 | 2026-10-10 04:10:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3fab21a-de28-377d-bebc-35ede2cdb108 | -10.89643 | -44.8226 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 53859feb-bb8e-390a-8a9d-d071053a343d | -15.37622 | -41.9238 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 20922488-04e7-39d5-8cc2-e01e7e3c3ad2 | -14.24405 | -47.30213 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c04c0a96-6181-3266-8e5e-40954d6106ec | -10.90206 | -44.83078 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 18c17c6a-e1ab-32c3-b99b-1bf4c0f4208f | -11.08291 | -44.10299 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README51.md)
