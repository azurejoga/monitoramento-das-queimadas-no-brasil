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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38d579ee-a2d6-341a-87f2-1f70718b4ef6 | -11.39282 | -58.32444 | 2026-09-15 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7a8e3a0-2dc3-3a5b-9e95-b12ae7cc1d4a | -14.3899 | -48.30521 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dea7b7d-e391-34ef-8dd1-b5bad969db01 | -13.27276 | -51.28819 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adab14f0-1d0e-35b3-a376-e9223505ba41 | -13.23298 | -51.65504 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 567a96ea-d296-3e0f-923d-7e726c4f5083 | -11.39226 | -58.3282 | 2026-09-15 05:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 334c6551-0afd-34c0-8420-d223d7ab2b7b | -14.68127 | -48.00418 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 207731cf-475f-396b-913a-9c5d72fbccd9 | -13.23181 | -51.66387 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cdb5c9cf-f5a7-37f9-9ee1-58202aa74e61 | -13.77341 | -48.82356 | 2026-09-15 05:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ed55370-aa31-302f-9cb3-77c307fe8b2b | -14.2123 | -47.42569 | 2026-09-15 05:21:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1c0dee8e-a181-3698-8407-b216d315870d | -13.23305 | -51.65392 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab336177-69b4-39b4-9c64-e6e20178ff63 | -11.90289 | -55.91194 | 2026-09-15 05:21:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb5e255f-e942-37e2-a1f8-d4e6a41ddd60 | -14.20464 | -47.43278 | 2026-09-15 05:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0e97ca3d-2cde-3d04-bf41-39f24269512b | -15.36565 | -52.99888 | 2026-09-15 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69a6d1b4-eae6-3dcf-83a6-af364676d7a2 | -18.16888 | -51.74771 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3772632b-32cf-37af-87ea-a1a3a4ae9790 | -13.38926 | -57.0369 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5befafb3-a525-3f4a-8422-103fd768f593 | -18.17248 | -51.76733 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| baa7caaf-4347-30e9-ac0e-bb3f724254f2 | -15.57802 | -48.79635 | 2026-09-15 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45f6c3c6-ac12-3f7e-8080-0b7d9e13ccf2 | -13.26285 | -51.27982 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d5f6ffa-288b-3372-946f-b47b024dbd88 | -13.26738 | -51.28748 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85992192-d8db-329e-81ae-b8c1f5c5fa8f | -13.33396 | -51.61284 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8184f881-1f49-36cb-b606-755552ecc514 | -18.1677 | -51.7592 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cad027ff-0180-3fa0-bead-b3f4dcbfc39c | -14.16564 | -47.40084 | 2026-09-15 05:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c0eb606f-da2e-3d63-99fe-777300901d40 | -13.23347 | -51.65055 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5767085e-a33a-39fd-ba17-00aec9f62ece | -13.58168 | -47.91138 | 2026-09-15 05:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71887d44-8e24-33ec-b483-eaaac6d790a4 | -13.76845 | -48.81048 | 2026-09-15 05:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f61afd36-ace2-3bc0-a319-f30da6e4d676 | -12.12243 | -57.19278 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 037add5b-80d3-3027-9a0b-0c1eaa46ab41 | -13.76311 | -48.80074 | 2026-09-15 05:21:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 146e1fbf-5c6f-3704-ab0f-fac1112f923b | -18.16251 | -51.755 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 09847dce-7e85-387a-9e00-fa3001b5255f | -13.40862 | -57.02364 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5d1ca28a-0e7d-329f-a114-3019808a4df4 | -13.30307 | -51.28585 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 135468a9-11e6-3aa9-a30b-236ad9d98194 | -13.33399 | -51.61412 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e260c871-2d1f-38e9-b9ab-1bc7eb6bbba8 | -18.16848 | -51.75163 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5aa22651-37f9-3606-b5bc-b1e4838bce4f | -13.57286 | -51.45162 | 2026-09-15 05:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e902eeb3-3215-3418-8d9e-1c43cc46a08e | -15.04847 | -48.55727 | 2026-09-15 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c58fb7ba-6dff-37a5-a8d4-ec039ebf9b91 | -13.72809 | -48.97977 | 2026-09-15 05:21:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a85e7afc-5343-3271-9a4f-7dce569148f1 | -15.54225 | -48.81873 | 2026-09-15 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c983e3fe-3d32-316a-bfc7-cde55d322065 | -15.54943 | -48.82143 | 2026-09-15 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a670ac0-2877-3920-8bf6-30de370b8e49 | -13.33435 | -51.6095 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8da2da09-88a5-3cc4-95f7-f16b4843fb89 | -12.12543 | -57.19756 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0704ac63-d2b2-3eb5-8429-a7dc7752106b | -14.20477 | -47.429 | 2026-09-15 05:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| b2601ff1-6b03-3744-8f87-c6629e1927f8 | -15.53447 | -53.84932 | 2026-09-15 05:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9927951-af39-3fcf-a1dc-50361fb80b50 | -14.67783 | -48.00858 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f66c01f5-359b-36a5-8215-6eeed3602f79 | -13.78077 | -48.81514 | 2026-09-15 05:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2db23787-2f1d-3e2c-bd41-1524031c8ef2 | -15.3614 | -52.99249 | 2026-09-15 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76f28c97-e332-3895-b116-6a723b6de295 | -18.17288 | -51.76348 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5d8797c4-2e56-3faa-97f9-060991d64d6c | -18.17366 | -51.75591 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 801209e7-5ca5-37ab-8153-6434213418a5 | -14.22633 | -47.42331 | 2026-09-15 05:21:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5acc525-9e17-3423-bf69-adee3ed95dbd | -15.04906 | -48.55107 | 2026-09-15 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9213028f-93b1-35f9-9d93-ec1d2fcc532b | -15.54301 | -48.82032 | 2026-09-15 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e71a75d6-bde8-3bf2-9b0d-e286c048e6c6 | -15.54894 | -48.82661 | 2026-09-15 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1d8276e-acec-3fb1-8a79-323c90238cfa | -17.31288 | -49.23212 | 2026-09-15 05:21:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d44942f-10f8-3e6d-bc04-39d6b152c1ac | -18.16175 | -51.76242 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6dc01c12-aba7-3102-aeec-b41db8ab519e | -14.20623 | -47.41469 | 2026-09-15 05:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9857677f-f9a2-3a41-95c6-cabe02ad7798 | -15.58192 | -48.8234 | 2026-09-15 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bc6befbd-8b17-3f36-a761-30042b07f5a2 | -13.29647 | -51.29559 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1421984a-d375-357b-a3b7-83613b2078f6 | -13.22778 | -51.65342 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91876015-be59-3a21-869f-18c0c958b6e0 | -15.57854 | -48.79102 | 2026-09-15 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c259c121-bcbb-3ad6-a943-24f5d93fffba | -15.54811 | -48.82529 | 2026-09-15 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7a8b2ec1-6092-3b04-a667-4cd08f0f91a9 | -15.57914 | -48.78473 | 2026-09-15 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11ad3553-adb1-3a7f-a491-dede6d062ac0 | -14.07062 | -52.15478 | 2026-09-15 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bc5b814-f048-355e-b0d5-99285d8fdb49 | -13.77628 | -48.82344 | 2026-09-15 05:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c40d2991-c4f4-3af6-9dd7-c6367238301b | -15.35356 | -52.97388 | 2026-09-15 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 061ddc36-b874-3ab1-bb1d-133a9b67f5d6 | -13.33441 | -51.61078 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 46605831-55d5-329e-83dc-71977342f705 | -15.57798 | -48.78945 | 2026-09-15 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92f2f9b0-cd63-34c3-a524-db31912cd51a | -15.53771 | -48.799 | 2026-09-15 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c9fbb75-5b0e-3e82-a532-f96abcbdf17f | -14.15872 | -47.40007 | 2026-09-15 05:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e1ac2f0f-570d-33e0-a440-276518baaed8 | -12.12604 | -57.19333 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3409b8e4-0b14-3cc6-a13a-8e0f898d1421 | -15.04566 | -48.58939 | 2026-09-15 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 338cfabf-6055-330c-b110-0e75632a4b1f | -18.1629 | -51.75115 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 810d24a4-e3a0-3763-921a-dd76f2c89d06 | -13.76261 | -48.80523 | 2026-09-15 05:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81be8de0-6823-3913-b8d7-1e0d763db14d | -15.55594 | -48.8217 | 2026-09-15 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e59f9367-d1ef-35d7-ad1a-3ff9500cfdad | -14.16512 | -47.40602 | 2026-09-15 05:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6fa78007-583f-3bbe-9f66-1cf76fe582db | -12.12727 | -57.18483 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efe73b0c-4ee1-3a76-9597-9cd28f66f74b | -13.4229 | -54.62523 | 2026-09-15 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f048b63-1122-3571-9ea2-c416ec398de6 | -13.73048 | -48.98022 | 2026-09-15 05:21:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c1cf84c-4e4b-3931-9e51-b03b4630d425 | -15.57743 | -48.79477 | 2026-09-15 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| edd93b06-fd74-325e-b382-f726de6a681a | -14.65776 | -48.00558 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0e373297-e772-34ab-a634-66a06981332a | -13.22819 | -51.65007 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a30d721-9c6a-32a4-9262-b0b661eea672 | -13.39751 | -57.02196 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2096d39d-f107-3df1-9a6f-c387f510daa0 | -18.17923 | -51.75631 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9a1064e-b481-364e-9c40-905608f22343 | -13.7803 | -48.81934 | 2026-09-15 05:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d05ce5fb-98e9-335d-b9b9-642c86c14062 | -14.39044 | -48.29997 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65eb974e-17ce-3dbd-a99c-6e6ee334bead | -15.60175 | -53.7875 | 2026-09-15 05:21:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd550bbc-c332-35c5-901a-4c6148439827 | -13.3543 | -51.7128 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05a68238-c9c0-30df-83dd-a0c163d12b0d | -15.04955 | -48.55185 | 2026-09-15 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55d2e7c3-c380-3c4a-a66f-3387db41c506 | -15.04795 | -48.56264 | 2026-09-15 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ab062af-791c-329e-9713-1d811010bca4 | -12.86483 | -60.02417 | 2026-09-15 05:21:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bc0a9ba-0b82-33d8-abe7-7945c8bed73f | -13.57553 | -47.90553 | 2026-09-15 05:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 862528d7-9f75-3c93-a141-5563b21208a6 | -18.17327 | -51.75969 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d64cd5d1-96af-3e96-8082-ae5f456bf556 | -14.66112 | -48.00176 | 2026-09-15 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2edcf816-2f90-3454-9ff3-3f17580a5804 | -13.70058 | -51.80698 | 2026-09-15 05:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e09a67d8-7149-3c98-81b0-3a6f529a9df1 | -16.05293 | -52.27717 | 2026-09-15 05:21:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a6d4a58-a35e-36de-8021-c457d46e3c08 | -13.56947 | -47.89878 | 2026-09-15 05:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68b8ebbc-26f6-3d83-8896-20898bccc2ec | -13.27814 | -51.28889 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3f890cc-c513-3a03-8947-d3b2ae47fc6c | -14.2059 | -47.41959 | 2026-09-15 05:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 26ffc457-48ba-3ce7-9349-6dd036457d07 | -13.40059 | -57.02706 | 2026-09-15 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7628c26d-90d3-3ee7-81f1-6d5c613261e7 | -13.77674 | -48.81912 | 2026-09-15 05:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49e0f893-b0e4-309d-8236-3c591f36da05 | -15.58492 | -48.79277 | 2026-09-15 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a861d54b-338b-3b4b-a841-23185514409c | -13.23264 | -51.65724 | 2026-09-15 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 259827ca-a0d6-3692-8623-5a3b83f43aee | -18.16213 | -51.75871 | 2026-09-15 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README63.md)
