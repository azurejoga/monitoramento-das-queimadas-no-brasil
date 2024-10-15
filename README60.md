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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8af2fc77-784a-3337-a102-486ba85d4911 | -3.92198 | -48.34672 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09ab5fdb-bcdf-3b25-acd7-e875ce4cd398 | -3.9213 | -48.35112 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdd0e8ac-f9e5-333c-b47f-894e1e2f063e | -3.92062 | -48.35551 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a58403f-0852-3184-a815-ef70b65f7042 | -3.91994 | -48.35991 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46dd7f45-b8a1-321b-ba91-baee4b3018c6 | -3.91927 | -48.36428 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec8689a7-4162-3a25-a7ac-9fbf197a00c3 | -3.91895 | -48.34179 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ada8ecce-5299-37cd-9bd8-3d114207182d | -3.91759 | -48.35056 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da984a1c-9543-359d-85b0-88252f838006 | -3.91623 | -48.35934 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7754954-6d56-342c-a4c4-de0ffab52fb8 | -3.9159 | -48.33688 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c489f149-d098-39e7-877f-5920845e5ec7 | -3.91556 | -48.36372 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 226e1291-17c4-35cd-9dfa-0e9db49a7a79 | -3.91523 | -48.34126 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 609fc2e0-6b57-3ab0-a9fb-3d7d2a0b099c | -3.91253 | -48.35877 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9c50a0b-8087-3241-b815-002b6e4e6048 | -3.91219 | -48.33634 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7d1cc17-e571-33da-b737-7b21178e7ea6 | -3.91185 | -48.36316 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7e57f48-ea2e-3cfa-aef9-993de5427cda | -3.90882 | -48.35823 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daddd095-6e7f-387e-ad4f-b36b54090ab8 | -3.90814 | -48.36262 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24d8b806-a97c-3b93-9f86-be3e533d2190 | -3.90578 | -48.35331 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37eee1c2-c58c-3a24-a4d4-d487b01e2621 | -3.9051 | -48.35769 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cae52086-b85a-3183-8297-bb977e30fca2 | -3.90443 | -48.36207 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d04ad445-5b9a-3c9f-9192-d175fbea04a8 | -3.90072 | -48.3615 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65785b01-6176-378a-8205-167854e1d19c | -3.90037 | -48.33905 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80522635-f3b5-3b05-8c4e-9938844ce97e | -3.89969 | -48.34349 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd0ba75c-2c53-3ddb-9ea1-fb815215828d | -3.86906 | -48.37016 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63246a7a-a3ec-3a39-9d96-a2874b4fb22b | -6.57631 | -48.23701 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 38.9 |
| a383ddb2-df29-3869-90ee-b443b6212344 | -6.5756 | -48.24185 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 38.9 |
| c34e36b5-775b-380a-8206-ccdd6dcbe4f6 | -6.57314 | -48.23161 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 89f8e4fe-c154-33ea-9fdf-223b1fc845af | -6.57244 | -48.23645 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 06370228-c2cb-32be-a90f-9dae927be1f7 | -6.57173 | -48.24129 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 60ad5909-638e-302c-8516-2b7a948604e2 | -6.57103 | -48.24612 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 67e428a8-e665-3070-a99a-74ecfbddda2f | -6.56856 | -48.2359 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 6b791ad6-e9de-38a9-b3e9-56f573bdf727 | -6.56786 | -48.24073 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 7aa31118-70b8-3c46-8b26-dfb185c09f05 | -6.56716 | -48.24555 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b466c94e-3338-3cf7-802e-c2cbbb3d9f02 | -6.56646 | -48.25037 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3f688e6a-a6e5-3950-afc9-6172d84cf3f9 | -6.56469 | -48.23534 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 6f299b00-faa5-33c8-8394-e2769b17b121 | -6.56399 | -48.24017 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 25007d89-708e-3ee1-938b-e4eff1b91604 | -6.56329 | -48.24498 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dc6a798f-a08e-3ca5-b03e-f1bacafe1f48 | -6.56299 | -48.23788 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 6725f87f-429b-3ef1-8736-88f46bb63ac5 | -6.56259 | -48.24979 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c06fc638-9ba9-32e4-a942-6a10f84e8826 | -6.56226 | -48.24269 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 25.8 |
| a500b9b9-f6ea-374a-bbe9-84933ffba897 | -6.56189 | -48.25462 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 791f0da8-a5a9-391b-9479-089a56bf0248 | -6.56082 | -48.23478 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2b358a6e-8f65-3b06-a296-a6bd0f26be29 | -6.5608 | -48.25231 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc4bdacd-7cb0-3252-adfb-4c1cd5e776fe | -6.56012 | -48.23961 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0a03e194-7d24-32c3-823b-142bddc9d657 | -6.56006 | -48.25714 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0970ee3b-691c-3f96-bc00-63aeaa1f24f1 | -6.55942 | -48.24443 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62f5ef75-2ff6-32f5-88bf-1c394fb4ebe0 | -6.55912 | -48.23734 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 25.8 |
| a0ebecee-c2cb-3219-9c5f-9bde74261639 | -6.55872 | -48.24923 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fa0c29f-033c-3dd5-8841-07ef9125d042 | -6.55839 | -48.24215 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 25.8 |
| af2376fb-f318-3cac-a150-9562b222c111 | -6.55766 | -48.24695 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fad88951-8a0a-30e0-a44b-9aeadd1e51b5 | -6.55693 | -48.25175 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95cc2258-1941-347e-91e6-256e7d1b04a5 | -6.55625 | -48.23906 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 81fd3c25-529f-343e-b42e-03146eea0ac6 | -6.55555 | -48.24388 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 121c4c4e-2c45-3248-873f-4863782d08e6 | -6.55485 | -48.24868 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae86f213-e221-34d4-9b16-fe12c7bd2c8a | -6.55452 | -48.2416 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b9d6b0e-1f92-3b5b-ac06-537c67f00fcc | -6.55416 | -48.25348 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bcac857-6b8c-36c3-b23c-de9365e4b69a | -6.55346 | -48.25831 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68d28723-ffc1-3514-a558-89f54e9e6ca3 | -6.55306 | -48.25119 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 617b45f6-9571-3d78-913c-0893c9155238 | -6.55237 | -48.2385 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac21b5c7-1b81-3c81-bae9-91c166df519f | -6.55168 | -48.24332 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4f1f60b-f824-30d4-a906-dfec7fdea85d | -6.55098 | -48.24812 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24ede50e-4b4d-317d-b713-f87d9513aee9 | -6.55029 | -48.25292 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 065c72ac-9fda-36f9-a966-67f20e25eaad | -6.5492 | -48.23313 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea007dc7-646f-3bf5-8d37-491e41ef85f7 | -6.5485 | -48.23794 | 2024-10-15 04:49:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59932803-d441-324c-a890-c8fe6ec1ccaa | -6.50591 | -48.459 | 2024-10-15 04:49:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1915a516-c938-3cba-b92f-3d61db125275 | -6.41628 | -49.59286 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 186622ac-c2f9-31bf-8b48-3b2c9721fe63 | -6.41565 | -49.597 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9dee1347-bae0-34c3-b2cf-34584da3ac45 | -6.41505 | -49.60099 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb844914-d43d-3729-8a22-fbaa7897c03c | -6.41444 | -49.60496 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76889cab-da78-3e9a-a5da-3157f85e2bdd | -6.41331 | -49.58831 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93397a57-b93b-3411-99fb-463660f422b8 | -6.41267 | -49.5925 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20fbd808-e621-3823-bd63-6509d4adcf35 | -6.41146 | -49.60052 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c75f85df-237b-3c40-a431-e063ca8d2624 | -6.41087 | -49.60443 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f1ed0d5-2fb2-35db-99cf-47005beee870 | -6.40971 | -49.5879 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6531f7f-7bbd-3f4c-a004-eb002f8eec62 | -6.40909 | -49.592 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a7ce366-7fc0-3ac4-893a-878ac9c5d296 | -6.40789 | -49.59995 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed1a8e4b-6276-343d-a3e6-ee56a3075f27 | -6.4073 | -49.60386 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeda0852-d0c0-3920-919d-a754d27a5176 | -6.40611 | -49.58749 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 76645a65-0ebd-3378-9458-bd98353f4439 | -6.4055 | -49.59151 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17c82337-ae8e-3a2f-9ca3-fe0df85e54fb | -6.40491 | -49.59544 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 41d6404b-f5ef-302b-a142-f8c47d93bb1b | -5.48371 | -48.96288 | 2024-10-15 04:49:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b8251fd-8efb-309e-83dd-0ff7a81e3d0a | -5.43388 | -48.97065 | 2024-10-15 04:49:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fee4fadf-cbcf-3ebb-94a1-fd857da4cdb4 | -5.41343 | -49.0805 | 2024-10-15 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdd793ec-dfbb-3668-b0ec-7c6194a7ccf5 | -5.25729 | -48.07042 | 2024-10-15 04:49:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 538efa00-529c-3282-a8a8-bead1a20d4bd | -7.01757 | -49.3246 | 2024-10-15 04:49:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d7be8e1-cff7-31f0-a823-dc070276bdf4 | -6.99935 | -48.54366 | 2024-10-15 04:49:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c3f65ac-9a6e-3b2b-83cc-cf5e361702a5 | -6.77297 | -49.10976 | 2024-10-15 04:49:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63bf9cab-64b9-3ce0-8793-582cbd98da17 | -6.66409 | -49.46155 | 2024-10-15 04:49:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 35188cde-ac93-3ac0-9d8b-532092a7c2bd | -6.66346 | -49.46574 | 2024-10-15 04:49:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b7390af3-3628-3ed2-a9b2-83c62313c0e0 | -6.42286 | -49.59775 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ff25161-a5d6-3b43-8a73-69c7d9a661da | -6.42223 | -49.60187 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d1b101d-9111-3a21-8b25-c85ac8457a61 | -6.41989 | -49.59321 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af60940c-49d2-36da-b371-52b70a71ae00 | -6.41926 | -49.59734 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 255ac194-08d2-3bf7-8976-f8d26c02fec7 | -6.41864 | -49.60142 | 2024-10-15 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bf050b6-c22f-3b7e-afe8-9bab489bb792 | -7.95874 | -49.06446 | 2024-10-15 04:49:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24dea542-89be-3a0f-87f6-b5dc642326ae | -7.95808 | -49.06903 | 2024-10-15 04:49:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc71f9c3-251d-3323-981f-c505cb3bb24c | -7.65421 | -49.36499 | 2024-10-15 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21e73320-7efa-33e5-8f64-33aced8606cb | -7.59733 | -49.44505 | 2024-10-15 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9039eeb8-52d5-3d2d-8c0c-6d95aa50086b | -7.51978 | -49.48825 | 2024-10-15 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47a018bf-f18a-3af2-81de-a3c8abb071d4 | -7.51613 | -49.48773 | 2024-10-15 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 063f04dc-4b8b-3cb9-a3d7-8e1d4da57cc3 | -7.51549 | -49.49202 | 2024-10-15 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README61.md)
