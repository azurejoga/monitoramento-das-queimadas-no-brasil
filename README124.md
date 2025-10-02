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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df7a7613-a5f7-3fa4-b000-16b65a671783 | -11.85303 | -48.02939 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d0a63fef-8cfd-3892-9c8e-91788db5815b | -14.31607 | -46.00647 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4c913b5f-d701-3774-9ec7-8fc3e15fa14b | -16.06592 | -51.01025 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79b3a74b-a7ef-3475-a48b-1410ddee5f1c | -10.68182 | -48.583 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 189f8efb-734a-35cc-8e2b-ca5445bde51d | -12.83929 | -46.86648 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd0a1648-0431-3acb-a092-2ca00fb4db1b | -15.00508 | -55.27627 | 2025-10-02 04:51:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e79128af-3c1e-35c7-8ada-23a74ed01d6e | -9.94463 | -43.6773 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2539eb79-6fdf-31a6-95e8-e9711a95660e | -14.4142 | -46.08094 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 99336afa-bdf8-3cc0-9d9e-05ec98e7ed93 | -9.85713 | -44.60358 | 2025-10-02 04:51:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 841f3ede-f73d-35e4-a800-d1af81b0c3d9 | -13.5373 | -47.27977 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6e79df9-4fd6-3b68-b094-2aeadf628206 | -15.25996 | -49.30206 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b62dca3-c22f-3e5c-bc21-1c5f6c3f736e | -11.83041 | -48.06993 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f653f45c-44d6-3c38-82c9-6f53a39d82de | -11.85829 | -45.03728 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2231853-43e2-39fc-812b-23d3b909eb25 | -11.18846 | -47.75493 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee6d00c5-1feb-39d3-96b7-0c1aaa2c2621 | -11.62188 | -45.05059 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31fc7161-b6e1-3296-8695-0a9d3bd2591d | -13.51295 | -48.20581 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8705ab0-846b-3a26-a044-98d1255b2f73 | -14.50784 | -48.48768 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51f44e27-e202-3297-82bf-8170ed19af68 | -11.42239 | -43.4982 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d3a6c54-7a4d-3ba3-a176-0ac518683912 | -12.8623 | -47.01375 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a1ed7b9-327c-388b-935b-a5ba72124919 | -11.80432 | -44.9658 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e752e87-cb44-30fc-8741-ecfdc7f0ea07 | -14.91315 | -47.23265 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f45a2ad7-9329-375b-9e25-8b66f2e8fe40 | -11.10528 | -51.07276 | 2025-10-02 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f4509c4-1e67-3574-830d-cd06f908756f | -13.76649 | -48.00457 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64192c79-6350-32e1-9c3b-5a2b72c15898 | -11.58245 | -47.64334 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ec35e5e-4935-335b-b6f0-a60fb26538e8 | -11.60517 | -45.05885 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0df6c11-62fd-38bb-b34c-986b771c95fc | -9.91619 | -43.72134 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1fa00d44-b03c-3013-89be-42afd0e9024b | -13.77828 | -48.04919 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d921e039-8ddb-376a-bdcc-85f50b0cf9ea | -11.03574 | -47.83092 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 393ed0fd-61c1-3785-8616-9b6d49e88880 | -10.95733 | -46.66406 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1b5ce70-2c45-3acf-bb9d-176c4208c15f | -13.0821 | -47.08107 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6a903bb-5e93-341d-ba3f-bc72535e21a6 | -10.98832 | -46.60636 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf9031b2-e0a8-32fc-b5d7-f67701607d92 | -11.35684 | -44.94291 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f2fbdaa-2244-30b8-972c-aa7558ec1a85 | -15.34647 | -47.09313 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccb18485-0519-3d36-8180-f1e529c58e46 | -13.8082 | -47.53827 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 90cfff6d-ad2c-3e82-9e39-4b23e8adaa4a | -14.48672 | -48.45159 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26f21958-bcd4-38cd-8f1e-d1b27b89fb59 | -12.58453 | -49.88926 | 2025-10-02 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b00b2bc-8fd9-38be-b96c-968948b621c9 | -11.86779 | -48.01555 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95724b37-a960-3281-b331-2ac5734431bf | -13.35967 | -48.09471 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c172f1f-b422-3ece-9092-028041cb8eaa | -15.34716 | -47.08765 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b97a674f-1aaa-37ab-a0e7-b452c92aba7a | -14.47984 | -48.40495 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b1a1daa-33cf-3dc0-9770-946765966322 | -12.89216 | -46.92852 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 57e8daa7-0446-3aa1-8a61-119f02c1658b | -14.57808 | -48.30902 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 981b5a54-e3f0-378b-a5fe-4179e285e383 | -11.08829 | -47.82494 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2cd7363-c5ce-3508-9f74-38042a4ef80b | -12.80741 | -46.86312 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54a83d72-e2bd-32d0-955c-702602307519 | -11.87121 | -45.01842 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ab53900f-779c-3dbe-bcec-3517a5297f9e | -11.46736 | -44.97171 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a05def98-d9da-38a3-9cd6-4159778a4fa5 | -9.58331 | -47.08271 | 2025-10-02 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c05dda51-57ad-3e5e-bc2c-108e876511f7 | -14.31604 | -46.00555 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bcbfcc57-0e4a-3ace-b966-de649ff6e2ec | -10.35205 | -43.73761 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aba6466-802a-3b2b-a01e-b7ac53259d29 | -14.90016 | -48.30959 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbc15618-17d8-3c67-b4b8-ff406d4e5e45 | -14.42196 | -46.13269 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3bf73137-2e80-311c-af2f-e20221035de0 | -13.01544 | -45.21877 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03357ec8-c549-3b81-90c6-c8cf29de3d62 | -13.74914 | -48.00249 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2227f3ba-b617-38bd-990f-6060d6c6c2fd | -13.29951 | -47.20097 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12a3a3c6-664b-3776-89a3-23c881a9d326 | -10.83316 | -46.61472 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d99add9a-ec58-35b9-b29a-be769ffbe7ac | -11.84621 | -44.96749 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c43e6607-2382-3be6-835b-c430bdc5608f | -14.40722 | -46.09734 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ab2bdb3-2cb0-3849-9b1d-a3a863c020b8 | -13.68174 | -48.065 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18430e6e-6194-3d30-95b0-bf8dd80d8c0e | -10.818 | -46.58863 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 574d01de-81d7-3501-978b-3fc525eeb277 | -15.14726 | -48.02018 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fba7b8cb-f27c-3c43-97fa-0dce73dfcaa5 | -11.58266 | -50.16607 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9083d4b-ac44-3673-9055-d00ae5be60b9 | -14.59299 | -48.32881 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3005725-2113-36f7-94b2-5d5605291276 | -11.1041 | -51.08065 | 2025-10-02 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c91d993f-423a-35c8-8b8f-a75338e29f74 | -10.2631 | -50.3273 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 247c746d-df75-3b51-aeae-65cc3025d23e | -9.93878 | -43.76706 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b3a51f27-4d0a-314a-8f5e-43d8ef0d4f3b | -15.50804 | -45.90892 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 257c39af-9719-3cf7-939f-ba1804681064 | -13.74086 | -47.91894 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 389d7f58-dc40-31e0-bf29-66ab0d0b5faf | -13.32919 | -47.87962 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8a86c53c-d0d1-37b1-9d08-83f857768415 | -11.58993 | -47.65272 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af7c2016-e055-3f42-8e57-e9b6c77726cf | -12.47438 | -54.42644 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03d37224-2f06-334f-8eb6-19e02ea482fc | -13.32569 | -47.22049 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38af73b9-ed66-3ff9-9fa6-19761eb6b016 | -15.83143 | -42.62236 | 2025-10-02 04:51:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4d5a4df6-2bd5-3971-b2c6-a72db098b3fc | -11.86935 | -45.03277 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3a87b9e-2dee-3c66-82f0-206b309360e4 | -13.32456 | -47.22944 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab4ef3e1-3472-3aa3-984e-9bd5732e2ebf | -14.44212 | -46.34789 | 2025-10-02 04:51:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 594c69ed-8cc1-3aee-8713-d206b86162bd | -9.93132 | -43.6498 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55917369-6d38-39f0-b9f8-ae1aa717ede6 | -13.40897 | -47.79042 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ba63bd2-63c2-3056-abb6-42f0d78f111e | -11.81769 | -45.02678 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37908a24-7758-3358-90b6-aae3d8ce51c7 | -9.39969 | -63.6915 | 2025-10-02 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bb7f240-7582-356c-8543-0603edb5cd38 | -15.27171 | -49.30685 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f929318-c1c1-3da5-8e65-7f6a8568fbad | -13.75739 | -47.96036 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 292b4408-4917-3f62-aca3-61fa736cbcdb | -10.83788 | -45.39691 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc563587-0d11-3ee0-bc51-e9aa74280f3e | -12.64065 | -46.96057 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b80d6ed6-8b6e-310f-b25e-3def1df50234 | -14.47926 | -48.40944 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 676338bc-5b2e-34ef-980c-5b3c0bb772ac | -12.49245 | -54.39662 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70c2d9de-2c08-300a-ae46-c8a2caa6a419 | -14.20903 | -46.12469 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a99c0306-8ee7-33b4-8cf2-1efdf8ccedb1 | -15.59847 | -46.9094 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86037cf5-18b8-3177-831b-009c552df581 | -13.87148 | -47.95399 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d185a7cc-bc85-393d-85b6-9d20f0ac477b | -11.43841 | -43.88185 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7acc41ab-fc15-3f0c-8d73-9ade7f9a6237 | -10.2188 | -50.3291 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ddff1c39-476c-3c7e-a1f7-9d5258b5f784 | -10.22598 | -50.33018 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0331d491-bb75-3ba7-bc0d-eae528d0d56d | -15.18179 | -46.41765 | 2025-10-02 04:51:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b16512fc-4986-3025-b423-de677cef651d | -10.99875 | -46.59813 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| b7a1bd60-adf0-30b7-8394-edde2989348d | -15.2621 | -49.31682 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca709926-7f08-3746-99e3-905a2499f21a | -10.80038 | -44.24132 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8adf20fc-31b1-3205-b550-027aae2c96a7 | -12.12018 | -43.42965 | 2025-10-02 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 042a104b-7ff8-32da-bd4f-286f6372c9d2 | -11.17451 | -47.28034 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a67ff5ca-389e-35c7-b601-e18f005df2cd | -15.29447 | -45.09392 | 2025-10-02 04:51:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fde44b8e-1a75-3ce3-a96b-7a22c7439fbe | -11.17174 | -54.11543 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c44f6f0-4124-3a93-994a-5b1f50954d18 | -15.28813 | -56.77602 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README125.md)
