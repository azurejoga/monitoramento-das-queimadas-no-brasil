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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2898a7e-1063-3981-9bdd-ced58ef88e69 | -12.91329 | -46.78114 | 2025-09-20 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a52d111-a5e7-34f2-9c23-6e7b24cdc3b5 | -12.91219 | -46.78654 | 2025-09-20 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1dafff5-d180-3c6b-b8ff-307cff5cc4b4 | -15.68098 | -42.47798 | 2025-09-20 03:38:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2646951b-c95e-34af-ad7d-94aaf6d13dd1 | -12.90011 | -46.78294 | 2025-09-20 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a6b34c25-4230-37c2-8f33-d3022fad62fc | -13.66133 | -44.31162 | 2025-09-20 03:38:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0f354ca-c7b8-3456-8710-185a5357c24b | -13.23141 | -47.26736 | 2025-09-20 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67535a9b-8eb0-3122-a6c3-a49b2113bcf2 | -12.90728 | -46.77922 | 2025-09-20 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef1b9472-2be7-3a21-99da-fba79acd7c3c | -12.90612 | -46.78487 | 2025-09-20 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1d219a5-4dc9-37d9-8255-e6730651a9d6 | -13.53048 | -44.12032 | 2025-09-20 03:38:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72b1ba6b-cb2f-3707-ab4a-c567ded9c3ba | -14.90519 | -41.65554 | 2025-09-20 03:38:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fbfe382f-1b0c-36f6-b495-e25259537475 | -16.32752 | -43.96426 | 2025-09-20 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 66ab7545-34a9-3363-b0e7-5063a164b993 | -13.94855 | -43.39762 | 2025-09-20 03:38:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f996ed4-93c6-317d-bfbb-bf36ade40810 | -13.23258 | -47.26173 | 2025-09-20 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6175b589-73d8-312f-8996-6e74cf602bad | -17.77948 | -43.79466 | 2025-09-20 03:38:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e42d92a-d5e0-3989-8d6d-9b79d7d8636c | -16.33119 | -43.96169 | 2025-09-20 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| facec64f-d8b9-3d6a-ab23-f07d41811cd6 | -23.41045 | -47.60286 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 3cfb4944-be4d-3fe6-b212-897f0ca86c72 | -23.69123 | -51.79315 | 2025-09-20 03:40:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 53ca90d4-d312-34f9-95da-618a7e2d3dcd | -22.94171 | -46.95548 | 2025-09-20 03:40:00 | NOAA-20 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e110c35c-2258-3b5e-b3b8-05ffaa8d0287 | -25.08715 | -49.38454 | 2025-09-20 03:40:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 841571d3-8a31-3697-83dd-e5072e53c9a2 | -23.32752 | -49.34792 | 2025-09-20 03:40:00 | NOAA-20 | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bc6de3b8-6577-3d0c-88db-faca5037c34f | -23.42814 | -47.61459 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0aba9238-0f19-39f9-8f43-5e1fb9fcc594 | -23.51663 | -47.19541 | 2025-09-20 03:40:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a101246b-7239-3d90-af14-2edafa74dbd4 | -20.02143 | -49.03676 | 2025-09-20 03:40:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87c81a68-9ed4-3a12-b86b-9c04b53784dc | -22.84649 | -46.46552 | 2025-09-20 03:40:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ef1d49fc-41ac-383c-be99-00ddf3b490a5 | -25.09326 | -49.3899 | 2025-09-20 03:40:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| add183e6-7eb2-323e-92ec-74b46908e628 | -23.28686 | -45.78216 | 2025-09-20 03:40:00 | NOAA-20 | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ebf43e90-4925-333f-a6dc-9c1d57d26802 | -22.81079 | -45.27644 | 2025-09-20 03:40:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 5cceb32e-c49b-3fc4-94a7-c2ed843ccc46 | -23.53382 | -46.25198 | 2025-09-20 03:40:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 89558540-9d81-3d59-9eee-4ab5560d161a | -22.804 | -45.28575 | 2025-09-20 03:40:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| aaf59966-b162-35a9-b085-d1650e89bb5b | -20.35423 | -48.78683 | 2025-09-20 03:40:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe98c93c-0e35-348a-b88f-930e84aeddbf | -23.69299 | -51.78627 | 2025-09-20 03:40:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| 41c34069-4604-33dc-909e-7364cb62eeb9 | -23.56283 | -46.25946 | 2025-09-20 03:40:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 27211b5c-84bf-36d9-98ee-028664779f9c | -23.40968 | -47.60633 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| ca844f51-09b4-32aa-b712-b18d4f658112 | -22.80045 | -45.27942 | 2025-09-20 03:40:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| b97e78f5-ff3d-3bc0-9dfe-652859d65059 | -22.63721 | -44.52104 | 2025-09-20 03:40:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b70717ce-b779-3fd4-9400-25d9cec18a44 | -20.34718 | -48.78981 | 2025-09-20 03:40:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a118ab6b-7705-3b6d-87b4-7bcee0c37ddb | -22.52719 | -44.66397 | 2025-09-20 03:40:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9e308ca7-17ca-39a2-b1bb-3648ddf5cca1 | -22.89834 | -43.33987 | 2025-09-20 03:40:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5e2bb7b6-c807-3869-9a63-5d95e5f25c58 | -22.90136 | -43.33701 | 2025-09-20 03:40:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 95b6f6a1-50ef-33ac-98e0-fb02d3709bd1 | -25.04334 | -49.24161 | 2025-09-20 03:40:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4e33df7f-0194-3ecc-b5cc-df897dd2f123 | -23.81075 | -47.57085 | 2025-09-20 03:40:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 801ffd6f-407c-31f4-9032-fa36882c2f05 | -23.42403 | -47.61693 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8de70f61-5a9f-3d1b-8cf3-5bd424327a18 | -25.03787 | -49.23956 | 2025-09-20 03:40:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1188abff-0ae1-3bbd-9557-6f7a39c92b55 | -23.2916 | -45.7833 | 2025-09-20 03:40:00 | NOAA-20 | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f9fd119f-7058-320e-8cde-82da3110c5f8 | -22.80617 | -45.2753 | 2025-09-20 03:40:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| a0278a93-ba90-3789-ba40-2a1aeee6f1eb | -22.53164 | -44.66526 | 2025-09-20 03:40:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a709221d-8a03-32fc-92ee-8403da90d795 | -23.43503 | -47.60883 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 44f7eb6c-2ba1-3380-9d8d-4271f1496ab9 | -22.9468 | -46.95689 | 2025-09-20 03:40:00 | NOAA-20 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 07d85d9b-4666-3cd0-afbf-64d889bde254 | -23.51145 | -47.19435 | 2025-09-20 03:40:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 80692ef0-a256-38e0-b58c-f9c0b7b362a5 | -23.42732 | -47.61819 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 68ec96a5-2eca-3e62-9715-8e5b253ee1c8 | -23.20197 | -46.21286 | 2025-09-20 03:40:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6b281fec-2434-33fb-8ff6-f667bd81b393 | -23.42281 | -47.61352 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 04ad552b-4b66-3246-96b9-868fb98dc052 | -25.08786 | -49.38736 | 2025-09-20 03:40:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 057a2da6-a49a-3e78-a447-20104bfb56e2 | -23.20738 | -50.25395 | 2025-09-20 03:40:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6989b061-a707-3cc8-9e07-57d4015290e5 | -23.25858 | -47.10355 | 2025-09-20 03:40:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 13afa229-f9f5-3ee2-a154-1f933a6f87e3 | -23.19853 | -46.21268 | 2025-09-20 03:40:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d1ef86fb-f7fa-3e23-8871-dde7929364e0 | -22.80508 | -45.28056 | 2025-09-20 03:40:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 97a53045-b359-3a46-8fb9-645186fd54e4 | -22.79693 | -45.27295 | 2025-09-20 03:40:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| e4b7b8af-1dde-3da0-9113-5118136c6e5b | -23.29425 | -47.31237 | 2025-09-20 03:40:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 37482bb4-03d5-3069-bd09-26da82318ed2 | -23.21101 | -50.26599 | 2025-09-20 03:40:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 42587acd-427d-3ead-902a-f4e69973854e | -23.43635 | -47.61157 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fd75d87c-f7eb-34ec-8e12-bc13099b9cd8 | -20.35312 | -48.79161 | 2025-09-20 03:40:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5d57778-1dff-36fb-91cd-bcb4e13a567a | -23.51073 | -47.19763 | 2025-09-20 03:40:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e1db84ff-ac53-3cf0-a71b-2fd2e529f045 | -22.48653 | -47.54796 | 2025-09-20 03:40:00 | NOAA-20 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 5385803d-3498-3d45-99a9-26a5bb62d4d9 | -23.437 | -47.60862 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 80bb530b-d6b2-3bc7-80ff-9f68079ecd58 | -23.2061 | -50.25922 | 2025-09-20 03:40:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8f26e78c-6e6a-3f3a-a5f0-528c74398aca | -23.5175 | -47.19656 | 2025-09-20 03:40:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f375df38-a307-3dd4-a087-2a8ae96be6d7 | -23.31909 | -45.98233 | 2025-09-20 03:40:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 01f59c37-41af-33ba-8f9a-e5018af74805 | -20.34828 | -48.78507 | 2025-09-20 03:40:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| db00e80d-e7c9-31ed-b44f-ae3e80fabbf0 | -23.28641 | -45.78325 | 2025-09-20 03:40:00 | NOAA-20 | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 16cb8d6d-e6a1-3271-921b-513510ae2906 | -23.43978 | -47.61245 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f097f9ce-5127-361b-9124-105681fc373f | -23.42483 | -47.61333 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 278f9d7f-7192-3d4e-a00b-b55e3252c986 | -25.08891 | -49.38306 | 2025-09-20 03:40:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 999defed-40be-37df-8e80-f609dc0b677f | -23.29114 | -45.7844 | 2025-09-20 03:40:00 | NOAA-20 | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 269f3518-92af-3b9b-8217-21e3e79e0ec6 | -22.80154 | -45.27412 | 2025-09-20 03:40:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 479164a2-5e29-32bf-94f1-4c50b8f52d70 | -22.89922 | -43.33548 | 2025-09-20 03:40:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9550a4c2-5d71-323c-9d6b-880a6c798cf5 | -22.49187 | -47.54935 | 2025-09-20 03:40:00 | NOAA-20 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 03877a52-808b-3aa2-b809-6c6c7dba3f2c | -23.79011 | -47.5645 | 2025-09-20 03:40:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fcebed86-f009-3bdc-978a-cdd54ff45e1b | -22.53329 | -44.66341 | 2025-09-20 03:40:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e28deafb-6f7e-3386-a8b3-a052d5c68744 | -22.52885 | -44.66215 | 2025-09-20 03:40:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 892b7228-7158-341c-8abc-6e1f5ab0cfee | -23.43433 | -47.61189 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3cc5969d-e3dd-3b7a-8700-ceb4b38a0674 | -23.32854 | -49.34361 | 2025-09-20 03:40:00 | NOAA-20 | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7b008a7a-e5a4-3727-9444-5454a154f85b | -23.2123 | -50.26068 | 2025-09-20 03:40:00 | NOAA-20 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d099639f-0b97-30f8-a9a6-433844b386a9 | -23.5123 | -47.19555 | 2025-09-20 03:40:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 319b4e29-7e1a-3173-8bec-34339a929a71 | -23.69465 | -51.77972 | 2025-09-20 03:40:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| f131defd-a050-313f-9d3e-e6beef857058 | -23.44044 | -47.60956 | 2025-09-20 03:40:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e809845d-cabb-37a2-b056-ee94d46cef16 | -29.73466 | -50.56472 | 2025-09-20 03:42:00 | NOAA-20 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1fd9e036-9598-3fa8-b494-0936a529fcd8 | -12.0762 | -44.8363 | 2025-09-20 03:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| c4e0c307-f9a1-3f8d-a178-38e29e1e503c | -0.2434 | -48.66533 | 2025-09-20 04:23:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80bf7ef6-28d3-31fd-8f66-047c4bc39d32 | 0.37596 | -51.04064 | 2025-09-20 04:23:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9d8482b-5e7b-3f61-8382-7f27b5e5eb19 | 0.38031 | -51.03995 | 2025-09-20 04:23:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 282602f8-c64b-360c-ab6e-cc1d5517088b | -4.08676 | -47.9566 | 2025-09-20 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df0f62d1-2134-3b71-ba18-00de154de5fb | -6.40436 | -43.31761 | 2025-09-20 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ceb881e-796a-3450-a08d-8d7189fa2e81 | -4.03808 | -41.80523 | 2025-09-20 04:25:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4206af2b-275e-3a25-a3a8-d02f5c888911 | -6.22668 | -47.31272 | 2025-09-20 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 668e587f-543f-35a8-8649-9fe821d3f3fc | -5.19678 | -45.48182 | 2025-09-20 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d25a189-b68a-386c-9939-9ebd90a5f3c7 | -7.25988 | -45.491 | 2025-09-20 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e86f4eb9-d9cc-3e27-8f08-426ee15c287d | -2.11186 | -47.11939 | 2025-09-20 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15582ae8-1de0-3834-9f19-077fd77f5065 | -4.47633 | -54.85567 | 2025-09-20 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a136b93-d2e6-3dc3-bbcd-33c53018b172 | -5.79809 | -43.64138 | 2025-09-20 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README10.md)
