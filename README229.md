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

## Dados Diários - Página 229

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aafae69a-02fb-329f-a554-938a6cc61188 | -8.49482 | -54.62477 | 2026-10-09 06:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d584a831-ddf2-3d30-b977-46ba4309e145 | -13.16531 | -54.36352 | 2026-10-09 06:59:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 066e93cc-e7a2-3ff5-9be1-699e772da694 | -15.51575 | -50.41123 | 2026-10-09 06:59:00 | AQUA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 52e13672-d4f4-3ed9-a413-e98659282c11 | -8.73761 | -45.15385 | 2026-10-09 06:59:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9b0880a8-a5b7-3e7d-bc12-a9520b8ad262 | -9.39678 | -48.99741 | 2026-10-09 06:59:00 | AQUA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5e9f6623-c563-3daf-a2ee-a5a889865678 | -11.78082 | -46.7976 | 2026-10-09 06:59:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b3ecdd22-1bd4-3a7c-8ded-bfb89e8bcd6e | -14.01783 | -48.76143 | 2026-10-09 06:59:00 | AQUA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e5d75606-dac7-3c7a-a447-487f01b323bf | -9.88587 | -50.48393 | 2026-10-09 06:59:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c41819e4-747b-3f07-a82b-f1c6e39119f6 | -11.31394 | -44.83838 | 2026-10-09 06:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 16e0dab4-6728-33aa-9bc6-1546f199b61b | -11.30861 | -44.83055 | 2026-10-09 06:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 8f963356-2602-3655-a35f-f935e997792d | -12.20964 | -57.07777 | 2026-10-09 06:59:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 99ea6f59-a33a-3746-8f42-7bf5fff00e48 | -11.88242 | -47.39995 | 2026-10-09 06:59:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3e0d5af7-9f3b-3587-9ba1-3e829b589148 | -11.26142 | -46.27642 | 2026-10-09 06:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 713f11d4-b298-3b89-b90f-94edcebf2f1d | -11.78457 | -46.79096 | 2026-10-09 06:59:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| dde2221a-f6d5-352a-a1d5-659b634911a6 | -11.39238 | -46.66162 | 2026-10-09 06:59:00 | AQUA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 128386ea-3313-3ad8-8382-c6a5f879c11e | -11.99772 | -43.46152 | 2026-10-09 06:59:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 5ec3da2b-68c5-3aaa-bbd1-6eaeecde634f | -7.90185 | -54.71493 | 2026-10-09 06:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 622d02e1-9032-3347-b84d-b3e760b9095c | -14.0085 | -48.75989 | 2026-10-09 06:59:00 | AQUA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d1fd64f3-2f51-38b1-a5c2-04698218a60e | -8.96771 | -45.15907 | 2026-10-09 06:59:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 43685c32-c341-3941-809f-3783c47fc995 | -8.17973 | -54.70795 | 2026-10-09 06:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bf550dc2-9310-3f07-973b-a6db79040ed2 | -11.76163 | -44.95819 | 2026-10-09 06:59:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 20eb5776-6dfd-3820-82f5-c4b0d924256c | -8.49725 | -54.61009 | 2026-10-09 06:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| d71f0ad1-64f1-3f77-b21c-adf04f5e7f0d | -9.87575 | -50.49142 | 2026-10-09 06:59:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3d3f555e-ea15-3077-832d-52a1767e792b | -12.23138 | -57.10172 | 2026-10-09 06:59:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| c5efdaa4-cbdd-370e-bcf8-6b01c10311e3 | -11.90739 | -46.56844 | 2026-10-09 06:59:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 30dd140f-0c80-3831-a7dc-6ff32e56fc4e | -8.96689 | -45.15352 | 2026-10-09 06:59:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 84f0e33e-867d-3887-a3d4-ff507d921341 | -10.57315 | -46.28449 | 2026-10-09 06:59:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 213d62cb-b9cc-308d-9dbd-52772a3b227d | -13.16731 | -54.35148 | 2026-10-09 06:59:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 183998a2-fa78-3617-b5e0-d1712df8abe9 | -10.45874 | -47.85157 | 2026-10-09 06:59:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ff0e630f-c3d3-34c7-93c1-b69f246a0688 | -11.26326 | -46.26296 | 2026-10-09 06:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 95314b04-056e-3199-84e5-e05c2e713d1a | -14.73687 | -48.21966 | 2026-10-09 06:59:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c5fecc58-1093-3ee3-b2d6-f4e09aed59ad | -11.39064 | -46.67425 | 2026-10-09 06:59:00 | AQUA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| e343c475-0b33-3af3-9931-17ab991e141e | -8.13854 | -49.43245 | 2026-10-09 06:59:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| de34061f-6897-39f9-a01c-211e33037537 | -14.87486 | -50.30073 | 2026-10-09 06:59:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3b1feaa2-e4cd-3a79-8094-a5f559f70d89 | -8.72849 | -45.13782 | 2026-10-09 06:59:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| bc17a140-c6ad-3890-96e5-c4163630fa91 | -9.3007 | -47.42457 | 2026-10-09 06:59:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 81fde284-ac1e-3b14-9d96-e0f78e64d6fb | -12.21958 | -57.09259 | 2026-10-09 06:59:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| cad0c835-f1bb-362e-aa05-7c14567ce959 | -8.98095 | -45.89858 | 2026-10-09 06:59:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3f10bbd7-5c2f-386f-87fe-809f055231d1 | -11.78273 | -46.80392 | 2026-10-09 06:59:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 1d188add-4f86-3476-be18-7155c6af41c0 | -18.32441 | -42.37685 | 2026-10-09 06:59:00 | AQUA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.8 |
| a5d29674-e085-3619-892f-c32c1eae3d91 | -8.17722 | -54.72295 | 2026-10-09 06:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| eb0bacc2-fbee-3d8d-a008-e97df512cfad | -10.74687 | -46.59165 | 2026-10-09 06:59:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 8add83e5-0ccd-3a77-b2c1-9656d8ef3783 | -8.73962 | -45.13921 | 2026-10-09 06:59:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 1f170654-9e0d-3581-bbcd-152feffb3462 | -11.19616 | -45.31554 | 2026-10-09 06:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| def203fb-fcdf-37f3-98b9-0aa3aed6e6ce | -7.21905 | -55.14389 | 2026-10-09 06:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 143edd96-d075-30a6-83a2-1f7489fd600f | -12.23482 | -57.08224 | 2026-10-09 06:59:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 94669e9e-efcb-36b5-8399-a896f078a63d | -12.21876 | -57.09951 | 2026-10-09 06:59:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.4 |
| bd829370-492e-32cb-a0e3-5b8f6e51188f | -10.87538 | -44.78414 | 2026-10-09 06:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1a4b86f0-deee-393e-999c-f93bf9960fc0 | -11.31616 | -44.82102 | 2026-10-09 06:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| d7961871-5f96-362d-a917-bcff23ed3406 | -14.00707 | -48.77016 | 2026-10-09 06:59:00 | AQUA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 62e07bac-35d5-37ad-97b6-0631b62fd688 | -10.87314 | -44.80141 | 2026-10-09 06:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| db2b1ca5-bfe9-3930-b81f-06e3849db104 | -11.90484 | -46.5605 | 2026-10-09 06:59:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b6b69136-5cfa-36c9-a80b-8664fc51682b | -13.25375 | -42.24913 | 2026-10-09 06:59:00 | AQUA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 269d1993-f7f9-3d84-b9f7-d67c44595a11 | -11.19817 | -45.30043 | 2026-10-09 06:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a96684bf-e677-3ae4-9d27-42f61fbca886 | -11.79115 | -46.79866 | 2026-10-09 06:59:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 4a49a64c-2d52-3c46-a132-99b226d82677 | -11.01012 | -45.4206 | 2026-10-09 06:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b4678c0a-a153-3c15-b468-fd8146dc47ff | -11.401 | -46.67533 | 2026-10-09 06:59:00 | AQUA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 80a92c1e-ee33-3bff-9088-a439570c791f | -8.99144 | -45.90028 | 2026-10-09 06:59:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a199db5b-4b30-3058-8e61-b35c2ff4a5b6 | -8.48368 | -54.62303 | 2026-10-09 06:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 7fc7d344-d3e4-330b-9a60-7810058a5f6b | -11.99483 | -43.48458 | 2026-10-09 06:59:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 90f397fd-8fd4-33ce-96b4-cd16b96c6371 | -7.90115 | -54.72056 | 2026-10-09 06:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 53345ec2-cea1-3600-8d09-6a4ebe3a09f0 | -13.25133 | -42.25576 | 2026-10-09 06:59:00 | AQUA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 98a38fac-7fbc-3c7a-8d75-ace42b4da901 | -10.58363 | -46.28593 | 2026-10-09 06:59:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d8223819-0b34-30bd-98e7-359443f89753 | -11.67391 | -46.77023 | 2026-10-09 06:59:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9f032e98-4b1f-3311-89f0-14911916390e | -12.2348 | -57.0871 | 2026-10-09 07:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 59461be4-4ff2-3871-95a0-4775f8d314f2 | -12.2346 | -57.1071 | 2026-10-09 07:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 797e84c6-0f2e-35d3-b8da-8415e26c40e0 | -12.2346 | -57.1071 | 2026-10-09 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b1dcc743-f809-36f4-be6a-0bbc5fd29f8c | -12.2348 | -57.0871 | 2026-10-09 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 4912c790-b072-33ad-b512-23bb250e594d | -13.1636 | -54.3591 | 2026-10-09 07:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 01f0dc2b-6813-388e-b8ec-2bdf8c5bff06 | -12.2158 | -57.0887 | 2026-10-09 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 7d0fe223-4d21-3142-bda2-7d034e47d519 | -12.2348 | -57.0871 | 2026-10-09 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c45b1b88-9b60-3bb8-93dc-00e5d7f9bac7 | -12.2346 | -57.1071 | 2026-10-09 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 5555bb0e-60bd-3cf9-8bd8-a828de183c21 | -12.2156 | -57.1087 | 2026-10-09 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 2a916de4-6ba6-35a8-b12d-107b178977ea | -12.2156 | -57.1087 | 2026-10-09 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1e2c5bb4-3b2e-32ba-a5f6-e9c604eac566 | -12.2346 | -57.1071 | 2026-10-09 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 25d592d0-bae2-34a1-803a-9b65b504b37c | -12.2348 | -57.0871 | 2026-10-09 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d33db558-1edb-3260-a4e3-f661765b58ac | -12.2154 | -57.1287 | 2026-10-09 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 84f8ac53-8e40-3a29-be8c-29fed821a1bc | -12.2343 | -57.1271 | 2026-10-09 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| d34e49bf-7632-3eea-8ef1-1803e1e42576 | -12.2348 | -57.0871 | 2026-10-09 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 5cafc68f-556a-35df-83ec-52a37a127fd0 | -10.6199 | -60.4852 | 2026-10-09 08:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2977d0c0-278e-3dd6-b773-5241080c8bc5 | -12.2346 | -57.1071 | 2026-10-09 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| a1d42fdf-9999-35bd-af4d-0c5e1bd5a8a8 | -12.2156 | -57.1087 | 2026-10-09 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| b1631606-4386-3682-9d23-6dabd4f2fd71 | -12.2156 | -57.1087 | 2026-10-09 08:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 2c4fa118-abe8-3a09-9187-6710a8cce248 | -12.2346 | -57.1071 | 2026-10-09 08:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 43988f2f-347f-3c12-ad48-00afe9d79481 | -12.2348 | -57.0871 | 2026-10-09 08:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d9666346-c87d-3372-b680-049dba004e02 | -10.6199 | -60.4852 | 2026-10-09 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| be02f525-6b0c-306d-9b5e-712f18f73169 | -10.6012 | -60.4863 | 2026-10-09 08:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b8f4a648-d2c0-38e6-8c2d-e38ede170d9c | -12.2346 | -57.1071 | 2026-10-09 08:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 14909b46-c66f-3f7a-853a-23837f679272 | -12.2156 | -57.1087 | 2026-10-09 08:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 70ace733-4f8f-33dc-83f3-27dd4fdfbc40 | -10.6199 | -60.4852 | 2026-10-09 08:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 5398cc2e-b74e-3abf-b8a0-1d4a878c8ed5 | -12.2346 | -57.1071 | 2026-10-09 08:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 769f6be1-0c9d-30c5-a34a-951cd4f52c2f | -10.6012 | -60.4863 | 2026-10-09 08:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 3a08109d-fa96-3c81-91ca-83dd2ad6d3df | -10.6199 | -60.4852 | 2026-10-09 08:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c9aabc34-9a42-3eed-b380-fd07e4491564 | -10.6199 | -60.4852 | 2026-10-09 09:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c6a9f292-a07f-39e9-b81c-de7b3d52d068 | -10.6012 | -60.4863 | 2026-10-09 09:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 72b20feb-1819-3fa8-9fa1-de73c2510c19 | -11.4131 | -46.6671 | 2026-10-09 09:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 8a8f9130-cda4-3849-b044-d6e60a5c8a07 | -12.0058 | -43.464 | 2026-10-09 10:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| d57819b5-0f63-3266-afaf-4468869dbf15 | -11.4128 | -46.6897 | 2026-10-09 10:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| bb41612a-ff0a-3197-a647-d11cbcb459e4 | -11.9865 | -43.4671 | 2026-10-09 10:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a4f3bc97-ad87-34e0-bf09-16252f14ba59 | -11.4131 | -46.6671 | 2026-10-09 10:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |


[Clique aqui para ver as próximas entradas](README230.md)
