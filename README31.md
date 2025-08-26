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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4190c407-2b1a-345a-b4a6-3fc3dfa44d57 | -12.93371 | -46.32765 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb3e85fe-e90f-3c2a-b3a9-b36fd407daa7 | -16.15633 | -40.35372 | 2025-08-26 03:57:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 383e81fd-d859-39af-b63f-ee3a7ce5ebf9 | -15.02531 | -48.50802 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe04ae5f-062d-3e6e-9836-48d594152adf | -13.49819 | -46.88068 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ada6f1cf-f64f-387a-8bca-66eeb87af44f | -13.58468 | -48.20039 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6732eddd-32b2-371a-931c-2c5e885d362c | -20.81411 | -42.78193 | 2025-08-26 03:57:00 | NOAA-21 | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d9298937-c4ae-33cb-b1e0-f605b3c7841a | -11.5422 | -52.12963 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8cae5ea5-26c9-3e11-a6c1-4dbeeabdf07a | -18.80778 | -47.60169 | 2025-08-26 03:57:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a18d06e1-784b-31ef-8175-98b4dbd25786 | -13.05488 | -46.31023 | 2025-08-26 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ae2e071f-9075-3649-926a-0f40d2632e8c | -17.87175 | -42.24276 | 2025-08-26 03:57:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 588f40ce-db3e-3622-822b-dfb35f78279f | -16.7419 | -47.60101 | 2025-08-26 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0775b7fd-6596-394b-a550-b2c65ba08de2 | -15.88177 | -48.14896 | 2025-08-26 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 92acdcc3-924f-3c83-80ef-cc8eb8fd868f | -13.44775 | -47.02609 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 078a5ee5-d019-382d-ae08-62f36e19688d | -14.27766 | -49.13877 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a37c9329-d743-3f15-a948-7aeb0beea996 | -15.62659 | -52.71552 | 2025-08-26 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 983d3d9e-a26d-320a-9c87-b13e6a4871ed | -19.28135 | -43.73782 | 2025-08-26 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d8de4da-5a48-3232-92a2-e9d27e3befd9 | -13.64831 | -45.70375 | 2025-08-26 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93cf91bc-9dad-3ba6-a544-6bd05c5bfda3 | -12.78368 | -48.13148 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4007ddca-6771-32f9-b47b-ce832f630c26 | -12.48377 | -47.22049 | 2025-08-26 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bc94ee6-1d6f-3440-8768-66c08ab5ef72 | -18.1398 | -47.94659 | 2025-08-26 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1688bbc-cd77-31ac-b9fe-125470a93bb3 | -13.44274 | -46.99236 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 075db1a3-6ec1-3cf5-b343-fe18b211e3a1 | -18.71902 | -41.27773 | 2025-08-26 03:57:00 | NOAA-21 | CENTRAL DE MINAS | MINAS GERAIS | Brasil | 3115706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0396561-7b1a-3848-852f-8628c12b2d80 | -13.58576 | -48.19476 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3fe9a20f-7ae0-399b-8b8c-f4bda4bd3786 | -14.25385 | -48.03562 | 2025-08-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbce9dd1-9b82-323c-b3ee-7ef3efb106cd | -13.0584 | -46.31536 | 2025-08-26 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95216d66-9094-3792-a745-396418135830 | -14.24786 | -48.0415 | 2025-08-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d77a67a9-907a-3540-a16b-049de3699ffb | -18.34833 | -44.96528 | 2025-08-26 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f579acbc-ef1e-3696-98ad-bca8ce112a4d | -14.72421 | -45.3763 | 2025-08-26 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 211d7b20-87d0-3d8d-a3ea-dc482112660e | -15.06294 | -48.69687 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 452eb3c2-a73e-313f-8d6b-0b61396409e4 | -12.92757 | -46.31245 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efd126eb-1477-34f2-9178-cd6d7262537c | -13.41667 | -46.90726 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9993832c-18d6-31eb-8918-4bb788d98f19 | -13.44873 | -47.02092 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b53a8089-2b2a-371c-ad64-14e69cdc9cb1 | -13.4902 | -46.8742 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6bb4d00-15a0-3256-957f-40a1fa40c211 | -11.54974 | -52.12546 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2caddc97-2352-3a5f-9413-595b16f934d4 | -15.05224 | -48.69986 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70da7527-f1bd-3ab2-8850-ba24204072b0 | -20.93612 | -42.4029 | 2025-08-26 03:57:00 | NOAA-21 | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 94bcf436-005a-3059-bff2-43755c5e70e6 | -13.41414 | -46.92098 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 574b5254-709f-3fa5-a54f-6d1dc6a8e4d7 | -13.16829 | -45.29324 | 2025-08-26 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 89fda03c-bd3e-30f5-90f6-9ad558e3ac71 | -18.85199 | -47.00024 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf9c5d3a-97bb-3b3f-9282-5cedaa62772a | -17.79466 | -44.49419 | 2025-08-26 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8d93370-fb5e-3d9f-ac62-12583bfab3e0 | -14.24893 | -48.03568 | 2025-08-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c76eb90d-a57e-3483-9f53-54154d41c358 | -19.17831 | -48.73461 | 2025-08-26 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7015efdb-2618-37b9-8204-f1f69ce45c21 | -13.42151 | -46.88095 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9ea2a57b-0840-3a02-a893-7dc49f856716 | -17.1993 | -44.32431 | 2025-08-26 03:57:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da5244e0-d88f-3981-b684-fa453088d687 | -15.02991 | -48.17226 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 59fa896e-a194-3523-9d16-bc4b1a4dbdc8 | -12.75215 | -48.16423 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9bae197c-7b76-36f3-b6a0-534d93646007 | -12.65662 | -47.85498 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99647eb6-c905-32ed-9e68-03ff68fa6006 | -19.79215 | -47.98652 | 2025-08-26 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d75a1eb-5a16-3240-afc5-8a1727c3d08e | -16.32268 | -43.62106 | 2025-08-26 03:57:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b215da58-1a5e-32df-96d0-96b56feaac6a | -14.25532 | -48.03254 | 2025-08-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b00356e3-3108-3ab4-86c8-8b4b1dc7f51b | -17.2029 | -44.32499 | 2025-08-26 03:57:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02e8ecd9-f02c-3f1f-b056-c018c96411a0 | -13.4472 | -46.86643 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd207af8-8f92-36a0-be45-f3b8b8e3592f | -13.49378 | -46.87968 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63cf0404-b9df-3098-aca8-3121831d6480 | -11.56363 | -52.12291 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b35f9493-5400-38f7-a264-a8894692af3f | -14.2611 | -48.02803 | 2025-08-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef2936e1-c318-3574-b650-ac56f38581a5 | -18.14752 | -44.43115 | 2025-08-26 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4107df8e-15fa-3757-bfb9-f5d08a20ad83 | -14.64264 | -49.07525 | 2025-08-26 03:57:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b610c91-18d4-3f8a-b966-42168adb93a3 | -18.85606 | -47.00111 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f426dacb-49c4-39b7-93c6-59f083be6b24 | -13.52423 | -46.91418 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4680310b-197f-37ba-b662-504ee86b151c | -15.08654 | -48.57407 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8ede1b5-bc93-3be8-ae5c-15342edf191b | -12.65703 | -47.85892 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2823a5b4-278e-30ea-9d28-890a01b3cda7 | -14.1176 | -53.98635 | 2025-08-26 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 627613e5-19a0-3bc7-9efe-b55f576dfb8e | -13.43729 | -46.87031 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 701799ae-14a5-3d5d-8bb0-2167539d6ed3 | -12.73169 | -48.13809 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1f939135-9cf1-3960-aa92-3656a0e9826c | -13.44966 | -46.99144 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 222fcc24-c75b-32f3-a589-c1d6ab064d5b | -14.24943 | -48.03759 | 2025-08-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 52b4b16b-329f-370e-a670-38dfe4a43036 | -11.5541 | -52.10391 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c612433-3ccf-318d-bcf0-c1a1b5f1a1cd | -13.44197 | -46.99658 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e331fda-b77c-3321-8fda-b34e2372aa40 | -20.80232 | -43.12279 | 2025-08-26 03:57:00 | NOAA-21 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 326757f4-05f3-3972-90c6-daef89aa56e8 | -18.56785 | -41.9125 | 2025-08-26 03:57:00 | NOAA-21 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 638d36e4-b708-32be-9521-4618743d35c4 | -11.56805 | -52.10098 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22bc158b-5eb3-3e9c-9a8b-276e2fb6da9f | -19.18026 | -44.5131 | 2025-08-26 03:57:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e09478b-1e85-3884-a3a4-a55d11c939ea | -13.82689 | -46.69894 | 2025-08-26 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cf198b1-115a-3a9c-908f-b53cdc0a7073 | -11.55392 | -52.13787 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 307b5ffe-255a-3168-aaaf-e1dad8f80fca | -15.08483 | -48.55685 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ac8a985-1051-383d-b497-ddf8cc358724 | -12.93287 | -46.32456 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a9d45e0-54f7-3b65-928e-bd1843559169 | -13.89302 | -43.80866 | 2025-08-26 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1e0cb7b-1470-38e3-8b09-ce193b22b9b3 | -13.42201 | -46.90333 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8a5f173f-815a-335e-a045-20c01c86fbb2 | -11.52067 | -52.13676 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 289a686a-5cfe-323a-85b0-b8c9316ab5ae | -11.5282 | -52.13268 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4230a6ed-d0e2-3906-a80b-8fc97f04f208 | -15.07513 | -48.65974 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f3f6332-e922-3357-84b4-86e73cfe5b49 | -13.44107 | -47.00152 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b9b8498-5bc1-3555-9fec-cc1760edf7a4 | -14.72367 | -45.37268 | 2025-08-26 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bcb5b59a-cd2a-34ea-be93-74780cbd30a8 | -12.94154 | -46.33375 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0b4d85e-02fc-32e9-85d6-773a275e5508 | -12.98774 | -45.22316 | 2025-08-26 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 339cb121-4ccb-3d7d-ab39-d7f9134f52db | -14.72025 | -45.37557 | 2025-08-26 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13c0214a-b156-3343-819a-cb649954fff4 | -13.43305 | -47.02003 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02d0e322-26c3-3776-9208-7e775f8b0334 | -13.48338 | -46.86982 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60876ba8-fc17-3485-bd9f-80fd93567a4f | -15.13371 | -48.68433 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec578433-0d2e-3051-a757-b78c8a50efe7 | -13.484 | -47.00631 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a7cf9320-4720-3191-a572-567bad3af475 | -13.62436 | -48.15015 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43b29847-aeee-3445-b1b1-4e99d8f78918 | -14.33131 | -48.64828 | 2025-08-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 067a7eb0-f7a1-3200-99e5-a0e7ac412332 | -20.38075 | -42.1944 | 2025-08-26 03:57:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3c47d7f1-ebd1-322e-85ec-53466486aa76 | -14.34315 | -51.94637 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c0f33401-321e-30b1-857a-f96090eff44e | -15.64929 | -52.7305 | 2025-08-26 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec5be300-553f-357d-8808-ffb544ef9ee7 | -13.83208 | -46.69521 | 2025-08-26 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 549eef06-29b1-3623-98ca-ae06a60271ec | -16.44406 | -49.45359 | 2025-08-26 03:57:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31129e38-6bef-3ea7-ae13-f50f198a339f | -15.12013 | -48.67628 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f61af5c1-7d84-3247-8bc3-c1c146065cb0 | -12.95547 | -46.33104 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 758cbd0f-b8c0-3716-8b2f-9ccb20164ca8 | -13.43741 | -46.99612 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README32.md)
