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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00f7def7-28d3-39b6-b18b-b6b7d78c9ef5 | -15.11062 | -52.46302 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 433e67de-366d-3396-9edd-02a646c6df86 | -15.7996 | -52.23311 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e83f4a8a-691c-3ae9-88fa-090a06de3d4f | -12.82361 | -47.96919 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a8a08ce5-357a-3623-94ed-5e73ae57baa7 | -15.81915 | -52.22002 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04de42b0-c13e-3a84-83c4-bdb00ef52a73 | -12.87773 | -47.94924 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79a1e3cc-e032-3d86-8b82-3ffd726cea6e | -13.00237 | -47.99795 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98479870-e34a-3b17-9d05-0deec6cbc3e3 | -13.89955 | -48.25168 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2b1b00b-507a-384f-8646-0ad2b2ced3f5 | -14.43874 | -48.4277 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64814806-6a27-310a-811e-c3b07d69f055 | -12.84117 | -52.97091 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 100e75bd-e12b-350b-8c02-61ed47427e1d | -19.93315 | -43.87111 | 2025-09-12 04:27:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6a799fa3-c1e4-307b-9a99-11a464f0a1c9 | -13.19761 | -51.75449 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cbfe80d-d934-33b2-820a-984cf6dfce35 | -16.41563 | -45.69865 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc10049d-7156-327a-a8af-9eedf0c16afc | -15.16401 | -52.31594 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb63792a-8e27-3194-828d-c74dc8d904f1 | -20.26787 | -42.12957 | 2025-09-12 04:27:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 285d00f8-4373-3664-9878-90527f97bb9b | -14.18869 | -46.17184 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86b92581-fe49-309d-8e4f-8c63e88b45b0 | -18.05623 | -45.45178 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb82a172-8dc5-325e-8933-fc2a7063565b | -11.61433 | -52.21514 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2537ccbb-7671-3152-986a-7a3958c55225 | -15.68379 | -47.04885 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee86231f-8cc2-36ae-84dc-36b788e7f645 | -12.5036 | -47.43584 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 66e49de0-4bac-34e1-beae-e5806eae5390 | -12.85675 | -47.953 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ac33e499-41aa-383f-aecf-3962ee774751 | -17.72882 | -46.14978 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fa7bff9-7e08-357a-8247-a411fd6bfe6a | -18.33267 | -52.06007 | 2025-09-12 04:27:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40809a6f-95ad-33b3-acc9-9ec86a596a43 | -16.18344 | -48.71218 | 2025-09-12 04:27:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93790e71-87ca-3e74-b31b-405159c776ec | -13.35171 | -41.9256 | 2025-09-12 04:27:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cbdbb430-2720-3c78-af60-06c80ad4d607 | -15.11718 | -48.62543 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe6b91b9-05c3-3779-8c30-148ff840b827 | -17.34786 | -46.69429 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2e70e13-18b6-3970-8f38-4ad63b729295 | -14.1289 | -45.37252 | 2025-09-12 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0543bba5-0b91-3d1e-b888-9c1d3bda7b61 | -11.87353 | -58.80977 | 2025-09-12 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06c5cdef-5d0e-3d32-882d-d538181569e4 | -20.11035 | -45.26743 | 2025-09-12 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8c1312cf-0276-3c27-a6a4-b645ff6e2c4e | -11.95747 | -51.17559 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 97fe0cdd-8afd-3ab7-9810-0b736374f637 | -13.30741 | -42.3874 | 2025-09-12 04:27:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6b384c8b-238a-3b40-8c47-a1698540c813 | -18.05506 | -45.43361 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0dad6b8-3a57-33e8-8a1d-9e49afcf9600 | -16.58323 | -49.23027 | 2025-09-12 04:27:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26967e36-9894-3988-89c5-675330c64819 | -11.18388 | -55.06902 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e9c3fb9-ead9-368a-af49-bcc8bc629ed0 | -19.14433 | -47.69423 | 2025-09-12 04:27:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fac3e2c8-e640-3709-a04f-cfa66fc63208 | -17.91573 | -45.71347 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 75977524-fc86-3db9-82f5-05ffcec83851 | -15.10386 | -52.45709 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2e39ffa-ebc8-31d0-9b95-d2c65804d0a8 | -18.67836 | -47.67112 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6af4dcc6-d1ac-3213-a18b-ca35155a1da2 | -12.96286 | -54.74425 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 695f415f-3bcf-37b5-b5eb-20e07162b5e7 | -16.49385 | -51.96997 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb6c2a4e-aa0d-3bf6-8fb8-a189e57c429a | -14.39458 | -52.94534 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ba2bf49-437e-3843-8cdf-c32426c598cd | -16.44093 | -49.03522 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7a53bb8-ccb1-38b5-bc9d-cd5667f214a5 | -15.57408 | -54.76986 | 2025-09-12 04:27:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c352739-46d6-315e-92f0-a5e8c6e81a5a | -11.94747 | -51.17582 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1af491d0-103c-300e-9d04-550cea62139a | -14.16932 | -46.18456 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3955fa20-d59a-33b5-8329-7d0ddf35962a | -18.31198 | -52.0736 | 2025-09-12 04:27:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c123909-3f45-3590-bdfa-529e0afa0f7e | -18.29858 | -50.42328 | 2025-09-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 50c644c4-479c-3c9c-be89-489a27bbb2f7 | -12.99906 | -47.99739 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b0adec5-7ed6-3dee-b3ae-3ea5df222475 | -15.08751 | -52.44165 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20cf3003-92ba-3624-bfb7-8253292da352 | -12.46826 | -47.48792 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41419f45-4808-392b-9e66-51953b298471 | -12.24305 | -47.34335 | 2025-09-12 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11838fb3-d98c-3c00-b793-3079fc62a5f1 | -16.24031 | -47.87092 | 2025-09-12 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d057650-0714-3442-a582-69236d00ca49 | -19.194 | -48.00825 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ad3e014f-89e2-300c-9670-0aa938245e78 | -15.11558 | -48.61411 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d8fb26d-675d-333c-a39d-1b451a23ad2b | -13.9201 | -47.94968 | 2025-09-12 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8eb4faac-49b4-38fe-bf77-eaea7f7fbcd4 | -16.65837 | -47.62648 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c72972ce-3acd-38fe-b830-057a45a0ef8c | -15.78908 | -52.23859 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1dbcf823-bd46-3644-ad75-b5c132569e36 | -12.92737 | -47.97831 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 211088b1-5687-3a49-8a34-328723c5806d | -18.44871 | -49.56605 | 2025-09-12 04:27:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4a2a0680-dc44-3e7d-b892-2449a04ddb30 | -12.93012 | -47.98238 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 33fb3252-e0ac-345f-bb9d-7105bf053495 | -12.01399 | -48.54967 | 2025-09-12 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f74c38c-1a65-3479-8164-37aed6b9a16c | -14.28609 | -53.07983 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2401c59b-654b-338f-aa7e-0adda7cf7e0b | -12.84859 | -52.97605 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5618dc0a-4de6-3959-8b1d-2b2c21c72588 | -12.98027 | -48.00883 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34242da8-7c29-3a01-9105-5d16506aee53 | -11.93128 | -51.15922 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce442ce1-2017-39f8-8c27-46be458a915c | -12.89704 | -47.95601 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86b44992-c24b-3ec8-9b40-72de7cfb49b2 | -11.96484 | -51.17689 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca5d99f6-b020-33e8-9ad6-59d3151474a9 | -18.59646 | -47.18846 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0daa8edc-5fa5-3d28-bc3d-c4a11a1128ab | -17.91633 | -45.70908 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b404a7d-7ebf-35b5-9ac6-a1dd909d7a8c | -11.80517 | -50.57051 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 993ac393-60a3-3707-aa8e-65cae29a35fb | -12.93761 | -54.75374 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 458d268e-3995-382c-803a-c0dd865e71c3 | -15.653 | -47.06009 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82a37fa6-5fac-3659-a0a5-c3101339b65f | -15.86644 | -48.33284 | 2025-09-12 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46fffcf4-b02f-3321-bfa5-31bb6854eea1 | -15.08373 | -52.44093 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 114727eb-3877-3770-819a-ea37bc928b04 | -15.26423 | -51.47844 | 2025-09-12 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35b281ac-a1c1-3e28-b0a7-d3d756434d82 | -19.63664 | -41.58226 | 2025-09-12 04:27:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 19eb95a7-a697-322d-b2b5-e30c8b44b31f | -11.98047 | -51.15229 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1c1659a-1685-3b94-a81c-dec8f3ceb08e | -15.6726 | -47.07744 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 577e5d46-b3b3-37b1-b05b-dce4e3852254 | -12.58631 | -45.68696 | 2025-09-12 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dcdedca-18e3-3a84-8ad7-edddb40c110d | -15.24462 | -44.04312 | 2025-09-12 04:27:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c0f91ae-516a-3395-aa00-dcf8792db4bc | -14.61526 | -52.09422 | 2025-09-12 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 70aadc49-c606-361b-b865-375b012d753f | -17.82038 | -46.73863 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c9e1e2b-b902-3883-ad6c-bda99f23ff36 | -12.88436 | -47.95033 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da2ca242-7635-3061-9bba-f9da632ae98e | -18.74941 | -47.62075 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3718848-8916-3759-ab96-99a426c68b4d | -17.78569 | -51.73313 | 2025-09-12 04:27:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8c4da66-e429-365a-9535-57c6703d2485 | -13.27126 | -51.71406 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ef5583f4-e9b1-3bfa-9e30-dec158893806 | -17.5771 | -45.38706 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4cf3639-0d6c-3885-afcf-296fdb8f35c1 | -15.57923 | -54.76641 | 2025-09-12 04:27:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76f35585-1f46-31df-8ea9-d50758f050a4 | -15.15352 | -51.25155 | 2025-09-12 04:27:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be628ea1-155d-36d1-8e85-f32d5f3e0021 | -13.53746 | -43.0064 | 2025-09-12 04:27:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 8f73a335-0806-3cd1-899d-29b853b9673d | -14.18527 | -46.17131 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f593fe8f-2bf0-3b75-a06e-d4a4a7575cb7 | -18.449 | -47.16976 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c8d8311-b5f5-3177-8063-ce49f5aa5cc2 | -15.59957 | -52.73888 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31f6ce81-b0e1-3c1c-9fbf-5d83f47cec65 | -17.54969 | -44.54353 | 2025-09-12 04:27:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbdd2254-f32c-3c63-b0c1-f0f170c251d8 | -16.95753 | -45.81773 | 2025-09-12 04:27:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 364252b1-922a-331f-8f76-1c64513e39aa | -13.30549 | -42.38391 | 2025-09-12 04:27:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9234d3f2-bc1a-3270-a8cd-996c8bc9a4be | -18.68512 | -47.67218 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dae583a-8a51-3042-a924-1b22ceb42ce0 | -14.23568 | -44.2506 | 2025-09-12 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a00fed8b-590d-341a-80e6-4480d9726f22 | -20.8077 | -46.88587 | 2025-09-12 04:29:00 | NOAA-20 | PRATÁPOLIS | MINAS GERAIS | Brasil | 3152907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| db5119ac-1b12-38cf-b218-11540984ef49 | -22.74523 | -47.61484 | 2025-09-12 04:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README93.md)
