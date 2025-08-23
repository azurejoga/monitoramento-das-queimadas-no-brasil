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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a69d8596-2d49-3953-975c-cc0282a9e880 | -11.96734 | -46.77259 | 2025-08-23 03:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8324fcbe-e3bf-3e99-9cb7-81f9cb148809 | -11.0601 | -44.59605 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 012aa820-e322-37e0-9ab2-6b94846d7bbf | -16.49341 | -46.74741 | 2025-08-23 03:40:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7160525d-00e0-34f8-8b1c-3a803ea656a7 | -14.8207 | -47.9597 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 615afc19-bf0b-3162-8dc3-eb6bba8ae47d | -13.00137 | -45.23135 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d847783-28cd-3934-93ad-7b90bef17619 | -17.61031 | -46.69559 | 2025-08-23 03:40:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f415444-40e0-3cf7-9d5d-84f2fc5acc23 | -18.27517 | -45.58176 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65127585-f273-3af4-9462-8adbebc4bb35 | -17.59194 | -46.5525 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc0b7bb4-0909-3d19-86f6-ec958a3ebdb8 | -12.78283 | -48.70803 | 2025-08-23 03:40:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 695dd166-2c23-3e23-82db-90d661792d13 | -14.80933 | -45.46203 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a7c4e52-9cb0-3871-9aaa-e8c14d00ed97 | -13.37525 | -46.2114 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c8a27c5b-5690-3147-bb1c-c3427d63ae8a | -17.59301 | -46.55694 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fde348a9-9a5e-33d1-9e7e-09f9f2e99b0e | -14.79005 | -45.50069 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a26fcd3-e5fc-3a25-b384-283f11780f80 | -13.368 | -47.49628 | 2025-08-23 03:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 383da432-919f-35eb-9bc1-22af05e3cfc9 | -13.3724 | -46.2252 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67356737-d7df-3c76-91b3-e99176ac3308 | -16.23242 | -48.7609 | 2025-08-23 03:40:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| badc7deb-f58f-378c-b0a7-a9e29e0bbc5e | -18.25242 | -45.56464 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26c3d9c6-74ba-3fc7-a73b-8dc1f415ea5f | -14.82295 | -47.94942 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d6ab5305-2eae-3bd5-8ae0-0cdebc215981 | -14.80921 | -47.95068 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3b053d53-34d2-3da3-961e-cd2b4df27c0b | -16.32695 | -46.7723 | 2025-08-23 03:40:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 840ea3f6-3e85-3e6b-9d58-e95826bb77d8 | -13.4114 | -46.24703 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9d94372-f6db-3a03-a755-28f7b5fbe214 | -17.27714 | -46.76482 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a73b7ef-5e5f-3340-aad3-7f065e4a7925 | -18.30016 | -45.56672 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f86271fd-af5e-372e-ad96-52c5ece8766b | -13.47871 | -46.9034 | 2025-08-23 03:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d911c92-aa64-3ddf-92e3-6fa8b4cb4d0c | -14.77553 | -45.23175 | 2025-08-23 03:40:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b01fab6-53b9-3ed0-b48d-d78854e06822 | -12.99166 | -45.23852 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9ee440ac-c325-3742-ac18-9c1d2c760ca9 | -17.26316 | -46.77399 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 563a9327-6dfe-33ba-98b5-5f119bbea472 | -17.26885 | -46.77547 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 65cab53a-59b5-3c1e-a939-cd740a925a9a | -12.77581 | -48.70689 | 2025-08-23 03:40:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2f16de4-2821-3459-9139-2986a95d62fc | -16.49432 | -46.7432 | 2025-08-23 03:40:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc8979cc-cf91-3fa7-aab1-a06d2d0b9fd9 | -11.11934 | -44.7546 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f11e614-2871-396b-952f-bb15ba75b28d | -13.00296 | -45.22357 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc98d333-f2b9-3152-8125-bcd2b8477746 | -15.53442 | -41.68957 | 2025-08-23 03:40:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4c2a356c-d468-3dc1-9b7b-a3bb89cc1c23 | -13.64537 | -46.88954 | 2025-08-23 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19a7d960-c48e-378f-9de0-27ca2a101e91 | -17.59587 | -46.56182 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ead004b6-0501-3db3-826e-e59108f9aa68 | -13.72058 | -44.40101 | 2025-08-23 03:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 214220b0-e705-3b7d-b2a8-175457005969 | -18.28737 | -45.54962 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b5b97f1e-a792-3870-a6f9-4f48e881daac | -17.265 | -46.76544 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ebe4fe8-846b-39cd-9a91-4a3f483ce93a | -14.79604 | -45.43336 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d25fdbbc-ecf7-3290-a8dc-addb5499f82a | -15.06814 | -48.48714 | 2025-08-23 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0a8c0b4-84dc-3043-ae53-69b028e4d04f | -14.79741 | -45.43514 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58a0b4da-03b3-35f2-a3b7-3241cfcd6025 | -17.70167 | -48.51194 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6734df74-08d5-3e8c-bc27-2c6d56367a35 | -12.99552 | -45.21891 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aef4e4e1-5cbc-3ab1-8a6d-67ea866d0997 | -14.91129 | -47.31564 | 2025-08-23 03:40:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d6336a6-442d-3164-b44b-e081c67bfc9c | -17.26588 | -46.76136 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d07af0a8-7726-3e37-82b0-ac8ccacf9b53 | -14.48059 | -46.0521 | 2025-08-23 03:40:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3359c297-97bc-339b-9d86-c8b18105d382 | -17.6926 | -48.50385 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ab58c42-9292-3a8d-b83d-f54b45a6068d | -14.91647 | -47.32174 | 2025-08-23 03:40:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 894d9d22-f73c-313d-a2d3-f522441c2d7f | -11.32375 | -47.84958 | 2025-08-23 03:40:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba6db9a5-fe6c-3c44-a185-15b28afff7e2 | -13.3705 | -46.2262 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f8c3978-1d20-38aa-803a-a4d8acc70f04 | -18.27068 | -45.57712 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3e2b33e-550f-35e0-bad7-3658b80bac06 | -11.12502 | -44.75558 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47ca4a21-3213-3906-87fc-c32f397fc9a8 | -15.19839 | -48.26091 | 2025-08-23 03:40:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6033a6e-4177-356a-b943-ad3037e80146 | -14.93758 | -48.00848 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58c0ec76-5076-3594-8c3c-220e47914f60 | -17.58567 | -46.56354 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 008e3cf8-6c19-3973-a6ce-b65191a0185f | -14.78683 | -45.48794 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2ae90c3-534e-388b-b0f7-550dda083fd2 | -18.255 | -45.57374 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2ad2487-8b66-392f-bb6e-a508445b088c | -17.70223 | -48.49076 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf193722-c738-3309-9131-820b98477c40 | -15.53648 | -41.68798 | 2025-08-23 03:40:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| edae637d-7cc5-32ce-bc78-169bc503a291 | -14.80546 | -45.44355 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b02acfdf-5a74-3c46-8d4e-488bc4a083bc | -13.64832 | -46.88572 | 2025-08-23 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6e235fe-ecfa-3c86-9ab0-668168b66549 | -14.81469 | -47.95595 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 434fe5d4-e4b7-345f-acc1-51214fd4d437 | -16.23632 | -48.7618 | 2025-08-23 03:40:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7152fe80-e9f0-30fe-bfaa-1dcbde642a71 | -15.53091 | -41.68452 | 2025-08-23 03:40:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 67bed363-bf56-38c6-9c32-61eaee0a7adc | -18.31154 | -45.5121 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2bdbc89-dde3-3ac1-98fc-a446455d6dd8 | -15.71985 | -48.21593 | 2025-08-23 03:40:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29482703-a816-38ac-b1eb-eb35e9d35a30 | -14.91273 | -47.99889 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1a00f01-429c-3c5e-9c6b-c3df32c54bc3 | -13.174 | -46.91301 | 2025-08-23 03:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fc1f35e-6d56-3acd-9bea-a09a44c5b0fd | -13.38276 | -47.48981 | 2025-08-23 03:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca572b7c-18be-380d-816d-8dc5d7c918dd | -17.69627 | -48.51674 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fa950be-06d4-3722-90b2-12d3dde47344 | -15.72015 | -48.21564 | 2025-08-23 03:40:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79fed15b-b86d-33a3-b729-64eda7074895 | -17.27064 | -46.76716 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5730e8ac-eb9b-31c2-b88d-52bfe9c41b7d | -16.33277 | -46.77367 | 2025-08-23 03:40:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e66aa840-6baa-35cc-8973-95949704b0da | -14.78211 | -45.48265 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c57e8e1-fc27-34d0-b972-31348c273ddf | -14.8029 | -45.4365 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d0532ad-daa7-30fd-8372-ac4f4c0373cc | -15.55735 | -42.68172 | 2025-08-23 03:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 63aab735-0050-3f1d-9fff-f06db4b14598 | -13.72127 | -44.39755 | 2025-08-23 03:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a313a87-b0ff-3856-bdbe-8b4b08097dad | -14.79454 | -45.49621 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e367e53-79e2-391d-a9ae-e4ae8f1cbb04 | -11.97364 | -46.77393 | 2025-08-23 03:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8851622-24c0-3d36-9fe6-25e005e769a1 | -13.04443 | -46.34108 | 2025-08-23 03:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b90e97c1-7ef1-3583-8179-74e088fbb0b2 | -14.80076 | -45.43842 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbc7bb17-9ea5-311c-88eb-bd54de63f7fd | -13.42258 | -46.25315 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d0cef7de-d193-379d-8a06-3555ba1e85e0 | -15.70735 | -41.92971 | 2025-08-23 03:40:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 66f39e08-42e8-3e4d-8327-e36d3da83675 | -11.32388 | -44.96256 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 505483bb-6241-354f-9ac0-eb85cc1953ac | -11.12609 | -44.78055 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 016d4b47-8c51-353c-b5db-a2a5c666e032 | -14.7934 | -45.42641 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc8113ba-2580-320a-8fed-75c92cbe05d2 | -14.80612 | -45.44924 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b256b321-ba76-3785-aeb0-a0431021dcb9 | -15.20752 | -48.7028 | 2025-08-23 03:40:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3acd44f-69f0-3810-9c2d-1ff4c5bfd3bb | -15.70815 | -41.9255 | 2025-08-23 03:40:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 74a7aff6-0be3-3246-8e09-14cd30ced23a | -17.69675 | -48.50432 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d347235a-d19f-344a-98e5-cfaafda0d05c | -13.12562 | -46.89557 | 2025-08-23 03:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03e08ba7-e962-3aef-8251-5b05e2a50731 | -11.12766 | -44.77239 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35710a15-fd99-3d6a-a3c2-462941a50218 | -13.39003 | -46.35163 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c561ee40-f288-3bdc-a7b7-3a9577dfd84e | -14.80467 | -45.44738 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16d9066b-019a-34fd-a7e7-fc2b9c55e68a | -17.58943 | -46.56445 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6913b22f-bb75-3d76-a507-abe2f724bc5e | -15.07104 | -48.50538 | 2025-08-23 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f05f2f2-a365-36fc-a973-2723d569e23c | -18.26996 | -45.58056 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df75584c-104a-37eb-8e69-c6574bf7527a | -13.37429 | -46.21604 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b2fd6fc7-fee1-3fcb-98b4-21f98767ebe8 | -12.67842 | -47.81396 | 2025-08-23 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c44db09-b1dd-357f-a11d-356faefebe9a | -14.82209 | -47.95279 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README18.md)
