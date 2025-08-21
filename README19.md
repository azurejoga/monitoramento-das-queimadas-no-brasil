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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f9d521e-b080-302e-ba13-4023a7b8fdba | -14.46601 | -48.36889 | 2025-08-21 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a16149a-7584-373c-9f3a-9b1dc32020bf | -17.76319 | -42.67357 | 2025-08-21 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0afa23c8-94ae-3ded-ac91-383570b7fbf6 | -13.62918 | -46.88547 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07a0dfef-cdca-3e3d-8d0f-da79b6523ada | -14.84953 | -47.94856 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91da2e99-dba4-33fa-97ba-7136da10f682 | -13.57222 | -47.05017 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb85804b-ff13-37a1-ad00-f207f3844b5b | -18.28589 | -45.52013 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0487ff46-d65b-3a90-84f9-3f4ab402c2e0 | -15.7417 | -49.96444 | 2025-08-21 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ab82eba-dd87-32e5-b983-22f76e58fb74 | -19.29342 | -48.43178 | 2025-08-21 03:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d6a638d-5bb2-3778-8d83-7a7657a048b4 | -20.49619 | -43.87698 | 2025-08-21 03:51:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 22fb23ac-1258-316d-a92d-7c9a465f581a | -14.50236 | -45.95886 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a61c6ec1-fa1e-3e72-b4f2-50a44b4b5a08 | -18.13144 | -43.9546 | 2025-08-21 03:51:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 806d47a2-739b-308b-847d-d54a1d0a441e | -13.54107 | -47.05061 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e70d75b8-d822-31c6-a329-ee9d0f7ec0c9 | -13.49654 | -47.0663 | 2025-08-21 03:51:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4cafc72e-83d7-37ab-b503-6bf10f629d86 | -21.34961 | -41.87054 | 2025-08-21 03:51:00 | NOAA-21 | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 53532911-c0f0-394b-965c-e31b8eec5412 | -17.38995 | -44.24884 | 2025-08-21 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37786ce6-f9fb-354e-9436-ba3a0ccb89c8 | -14.8458 | -47.94046 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a927bee5-1ce9-34ac-b348-39933348db57 | -14.85603 | -47.943 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| febb58e5-32d6-345a-a3a7-5712e8d7bdcb | -13.57281 | -47.04706 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dba71aa8-c732-3615-a223-ffe882abfbbf | -19.04019 | -45.26358 | 2025-08-21 03:51:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3beee973-e96e-33d5-b461-6b18e17415e1 | -14.85733 | -47.93654 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b41c9f64-edef-3940-bb35-bd664eda4943 | -14.85159 | -47.93839 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0cf758e-a262-3936-84f3-6fab289fffbc | -14.49871 | -45.95315 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29b4fa55-8635-3d84-ad83-ad97f2cc95f0 | -15.76756 | -43.22377 | 2025-08-21 03:51:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5dbd3179-69c4-3446-998f-e00d69590e5f | -14.856 | -47.93663 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0223ab4e-480c-3c3a-b329-062f307d899a | -15.74255 | -49.96032 | 2025-08-21 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a762b54-124a-36ce-9295-7b974e87581a | -14.38011 | -52.02818 | 2025-08-21 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9e129066-9a7c-3021-b59a-c15a469e4796 | -14.85911 | -47.95433 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 82d303cd-80fc-372d-82bf-2ac9dad34dd3 | -13.55448 | -47.03472 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e59e2e47-fc9e-3a17-8eb2-0ebbe8d89dff | -15.49989 | -48.04168 | 2025-08-21 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb51ece7-1fad-38d4-9066-8bfa46e259aa | -15.50889 | -48.05008 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8e9dde6-2770-33a6-a9cf-a9fa0da4034b | -18.29001 | -45.5211 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da73e9d6-a75c-368e-8941-665dd79f22a0 | -15.51337 | -48.05438 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4423c62d-66ba-3e0b-ab05-3ea59ed23996 | -21.36798 | -45.05701 | 2025-08-21 03:51:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| beba4b07-0212-31c7-a9ea-5702c3f817af | -14.47684 | -48.37034 | 2025-08-21 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 495db9ee-2712-36fa-ac1b-6b28ac72526b | -13.63504 | -46.88149 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a5486c7-ef07-3813-be05-12e177ed7991 | -15.86313 | -48.77691 | 2025-08-21 03:51:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 256b76cd-17ef-306a-ab2d-14ca12c6d669 | -16.10339 | -48.01102 | 2025-08-21 03:51:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22f9643b-fbcc-3c21-ac8f-053d509e3dde | -13.47945 | -47.04878 | 2025-08-21 03:51:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1c2c51f-3f49-3813-b15d-6000a81ea304 | -13.53721 | -47.04378 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7048bfd-039a-3b1a-87a6-fbc657fe38c8 | -16.50937 | -46.73023 | 2025-08-21 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c7563ac-6802-3d03-a4fa-26dc0531eb61 | -15.89046 | -49.01269 | 2025-08-21 03:51:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 416b7120-95fb-3600-9e68-541dc5a9bb9b | -15.51404 | -48.05105 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c659ad1b-b510-36e9-822e-1fd09f69eae3 | -19.81025 | -41.90606 | 2025-08-21 03:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d6d1d167-40c8-3970-84e1-7a3dac318809 | -14.85854 | -47.95127 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 68f8be5b-af73-3c80-92f0-6a41bf9e2a79 | -13.56836 | -47.04327 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35d904d9-503f-390a-9464-036a3d89d159 | -14.85156 | -47.9319 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bd844d0-da83-365e-97c6-092c21909a15 | -13.49328 | -47.05785 | 2025-08-21 03:51:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7723035-2e68-33a1-bd4c-1b3b4042400a | -13.59058 | -47.00801 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 397aacc5-369f-387b-81a8-30ccf14dab84 | -13.56891 | -47.04038 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5f895e6-652f-30ec-a14c-7df18770ae4d | -13.49383 | -47.05492 | 2025-08-21 03:51:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a921059-3974-3c98-aa7c-c2891227f955 | -15.54246 | -42.27016 | 2025-08-21 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1a547af-ff99-34dd-82e5-9020614bc222 | -14.85025 | -47.94501 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 760b4690-efeb-3872-b59b-18e7acad4359 | -14.47615 | -48.3738 | 2025-08-21 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 48eb3762-4241-38b5-b8b4-6dcdd06e830b | -17.39478 | -44.24435 | 2025-08-21 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae7c9050-21e0-3619-a279-e153aa867ac7 | -14.1243 | -45.38975 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e57cd4c4-5700-37a8-b77d-30dc947f78c0 | -16.11232 | -46.82805 | 2025-08-21 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f56daa9-0863-3364-831a-a87065a760ff | -15.43011 | -46.71671 | 2025-08-21 03:51:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c535106-cdc5-3b73-a7ee-f43aa3a3ec87 | -15.5012 | -48.03519 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 995ae496-a21a-30ce-9213-d4fff77e420c | -14.37605 | -51.98289 | 2025-08-21 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 66bf86cf-99c7-3383-b18f-ba7c5d6e0588 | -14.8604 | -47.94793 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| caeb7bf0-fe35-344f-86de-f059ea1bb4e6 | -14.94539 | -44.3218 | 2025-08-21 03:51:00 | NOAA-21 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 955523e9-0d58-3580-96d2-60325561237a | -14.89974 | -48.07511 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fb8487d-81f6-3376-bdbd-f50333dc11d1 | -14.0603 | -43.53408 | 2025-08-21 03:51:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 966c3a50-f667-3c2d-9bc4-325fde16946b | -18.29672 | -45.53115 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c888245e-b6f6-38e2-840e-a544e8b071bc | -14.46666 | -48.36569 | 2025-08-21 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0dad812-3556-3a1a-8b1e-6447c56f5714 | -14.87603 | -48.05837 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 244a72f1-4f53-37b8-842d-49a23d885f66 | -14.8478 | -47.93058 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93384342-2e60-3409-99a8-a7c9dd5008fd | -14.90501 | -48.07582 | 2025-08-21 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0b32d9d-bb76-3dca-9a83-f353cb15d886 | -15.19287 | -48.70135 | 2025-08-21 03:51:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3a28f6c-ea0c-3a2b-98b3-4c03f331eb8d | -23.10324 | -45.74294 | 2025-08-21 03:53:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 13c70c9b-4461-34ce-aad8-59d9bcaa2eba | -23.1836 | -46.11506 | 2025-08-21 03:53:00 | NOAA-21 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e31d74d3-9a5a-3823-a166-74e36e755b69 | -23.71223 | -47.37766 | 2025-08-21 03:53:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1f418591-5dc1-3b04-935b-de64230ef3cc | -22.7076 | -42.64769 | 2025-08-21 03:53:00 | NOAA-21 | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b14be065-0579-3b8d-97de-f9bf57ba3bbe | -22.30647 | -43.18122 | 2025-08-21 03:53:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 108f775d-ef87-339e-985a-191e9ae0efe6 | -22.52541 | -43.67851 | 2025-08-21 03:53:00 | NOAA-21 | ENGENHEIRO PAULO DE FRONTIN | RIO DE JANEIRO | Brasil | 3301801 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 32bb8395-0b1f-392a-bf9f-397b8a6f03fc | -22.96073 | -47.10444 | 2025-08-21 03:53:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b209eb50-4417-3961-9c24-af36e2184d1b | -22.71111 | -45.05433 | 2025-08-21 03:53:00 | NOAA-21 | CANAS | SÃO PAULO | Brasil | 3509957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a1aa72f-2e96-37f5-9de4-c73c5379557b | -22.68439 | -42.8684 | 2025-08-21 03:53:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2424c70a-cfd4-3bc5-9cd6-17f818c22e71 | -22.07559 | -43.21139 | 2025-08-21 03:53:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e0d1a025-a367-3a23-807e-a84d475f452c | -22.80565 | -43.38852 | 2025-08-21 03:53:00 | NOAA-21 | SÃO JOÃO DE MERITI | RIO DE JANEIRO | Brasil | 3305109 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 99d387e1-d761-30de-988b-f6aa1ed85c41 | -22.60145 | -43.68059 | 2025-08-21 03:53:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| abddbaf8-100e-3231-814f-5ed3811e9651 | -25.42518 | -49.16718 | 2025-08-21 03:53:00 | NOAA-21 | PINHAIS | PARANÁ | Brasil | 4119152 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d7d6b6db-8b40-3986-8346-977f5ecf7067 | -21.98001 | -42.87249 | 2025-08-21 03:53:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 17f4d6ed-c62f-32de-8b78-d10215758077 | -23.40094 | -46.30806 | 2025-08-21 03:53:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 054144eb-c4c5-30df-9ce3-865d8b65e3e3 | -23.45979 | -46.97525 | 2025-08-21 03:53:00 | NOAA-21 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| fe7ac73f-1b8c-3e36-b180-a46d3ba17a12 | -23.22524 | -46.47683 | 2025-08-21 03:53:00 | NOAA-21 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 747b5e95-e4e5-34b3-a6dc-81e3650f1f47 | -25.42538 | -49.16533 | 2025-08-21 03:53:00 | NOAA-21 | PINHAIS | PARANÁ | Brasil | 4119152 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c53e538d-82b6-346c-bd06-47bc788183d9 | -23.1817 | -46.11722 | 2025-08-21 03:53:00 | NOAA-21 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| af100f54-dc15-3a01-95c5-91b93c07b7d3 | -23.4606 | -46.9712 | 2025-08-21 03:53:00 | NOAA-21 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 4b9aeba5-62b7-3091-a85e-7786d61a0a52 | -22.69134 | -43.70729 | 2025-08-21 03:53:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bde2f670-77bf-3de5-8fdf-6976a0c13d8b | -23.89723 | -46.81114 | 2025-08-21 03:53:00 | NOAA-21 | EMBU-GUAÇU | SÃO PAULO | Brasil | 3515103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b481c94e-0e40-3e5c-b0c3-ab931bc3f853 | -22.94334 | -43.70234 | 2025-08-21 03:53:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 534a2617-10c8-32b6-8924-b7c775010d0e | -23.23434 | -47.52868 | 2025-08-21 03:53:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a1e1fd4b-ae0e-38ec-8eb2-c98c1b0d3082 | -23.3108 | -46.90387 | 2025-08-21 03:53:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 07454849-3798-31c3-8456-b2cc2246e573 | -22.94612 | -43.70732 | 2025-08-21 03:53:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| efad637a-6908-3b52-ba12-5dc631590470 | -22.69745 | -43.73496 | 2025-08-21 03:53:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 336a7cad-5434-3375-a3c6-9107978d19e7 | -22.78878 | -45.07846 | 2025-08-21 03:53:00 | NOAA-21 | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 21930e01-af72-304c-851d-5d4f54e4d383 | -22.9426 | -43.7066 | 2025-08-21 03:53:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c0350f9b-d8cd-33eb-9609-330256654ac1 | -23.31572 | -46.90069 | 2025-08-21 03:53:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9a1ee295-3735-352a-a1d5-05e8d5926daa | -21.97929 | -42.87672 | 2025-08-21 03:53:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |


[Clique aqui para ver as próximas entradas](README20.md)
