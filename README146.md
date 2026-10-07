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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7834681a-79bf-3885-87b9-eaaa8917a81b | -14.94712 | -45.45335 | 2026-10-07 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 18d65627-468c-34d2-835a-448e2425b807 | -19.05212 | -44.6697 | 2026-10-07 15:58:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f55dda97-8a4d-39f8-82d4-599f3965a28c | -15.97824 | -45.69209 | 2026-10-07 15:58:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cabe0701-9f2b-3bf0-9263-bfa95dd7ce3a | -17.5008 | -39.87621 | 2026-10-07 15:58:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| c0b298af-bfb3-33e5-b1cf-8e938d1a8029 | -17.0217 | -45.92365 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 5e80e64d-b5e1-335f-96cc-6c64d288bdfc | -17.64223 | -47.04712 | 2026-10-07 15:58:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ee285074-439d-32d3-bded-5f670cefa4c4 | -15.05902 | -41.39562 | 2026-10-07 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c7f3631f-c5d1-3fec-be1c-7fdc658fd77f | -19.44292 | -41.31853 | 2026-10-07 15:58:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a7b880bf-0c49-3141-80ff-d82984bf8940 | -13.88917 | -39.51985 | 2026-10-07 15:58:00 | NOAA-21 | NOVA IBIÁ | BAHIA | Brasil | 2922755 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| c84e8cd2-d541-3913-9c6b-0ac5393f3660 | -17.20492 | -40.81025 | 2026-10-07 15:58:00 | NOAA-21 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 4a3c788a-052a-3834-bb33-ecf7ed9407b6 | -14.9249 | -41.82859 | 2026-10-07 15:58:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1ee848c2-6a44-3a64-ac8d-6072269a8dca | -17.11558 | -41.3425 | 2026-10-07 15:58:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 951a22bd-6b4f-3e00-9c0b-ecd9d278081f | -15.43589 | -41.29694 | 2026-10-07 15:58:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 209f9906-7917-3017-9cb2-2283e2ceaeef | -14.24548 | -42.00115 | 2026-10-07 15:58:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| dd5535e1-db8d-3642-b367-376c92b98e0f | -15.25059 | -40.99264 | 2026-10-07 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 51805f4f-0095-319c-b86b-9fdcc9380bee | -17.52091 | -45.46821 | 2026-10-07 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5b2be479-1a92-3950-87ac-54c5da61b0f6 | -17.02693 | -45.91906 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 2b25ea35-1cdd-3223-8c12-f07ce3c15e85 | -15.97113 | -40.69881 | 2026-10-07 15:58:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 69a4df7d-55b4-3f79-bb40-d17d6d35944f | -17.52598 | -45.46558 | 2026-10-07 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 512aac52-69b2-374b-86a9-1e43a54078e3 | -15.52069 | -48.51995 | 2026-10-07 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7e473c02-d28e-3301-ad63-417baa858196 | -17.02 | -45.90771 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 50250b1b-dc1b-39e8-b27e-dabda3542a95 | -16.01427 | -41.8258 | 2026-10-07 15:58:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| 0c6a7b79-4967-38cc-96a9-435742506936 | -14.92122 | -41.83308 | 2026-10-07 15:58:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cab6253f-2656-3943-a533-4d423a4981f3 | -15.30982 | -44.64118 | 2026-10-07 15:58:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6dfee9bc-f145-3347-a395-66b41eb4ddb5 | -15.11143 | -48.50661 | 2026-10-07 15:58:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 16142301-b887-36d3-996f-024bef8606de | -16.86666 | -45.22657 | 2026-10-07 15:58:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 89be6805-46ea-3862-8785-7652fcf1e021 | -16.97887 | -45.47556 | 2026-10-07 15:58:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 11a43ae1-5c03-35f3-871c-aebdf94587e9 | -15.25695 | -48.5161 | 2026-10-07 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 14e222d5-92ba-39f4-8038-3d644775aa02 | -17.76656 | -42.70147 | 2026-10-07 15:58:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a4f8f2b1-74dd-33d7-a094-d7af7ad2637d | -14.16352 | -41.36342 | 2026-10-07 15:58:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c374e833-4c30-366c-8e9b-5d1be88dfc68 | -17.24391 | -47.48525 | 2026-10-07 15:58:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b72943a7-a97f-3a9e-8faf-9e91782e9899 | -14.21519 | -42.75836 | 2026-10-07 15:58:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bd3fdef4-d7a4-35ab-ad79-d4db20b8f662 | -15.39619 | -41.70221 | 2026-10-07 15:58:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.3 |
| 40f9c2e4-9713-31aa-b45b-6e73c50de08c | -14.38311 | -40.3379 | 2026-10-07 15:58:00 | NOAA-21 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 05a8ded5-0f3b-364e-81ea-e6592431d881 | -15.53239 | -41.24309 | 2026-10-07 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 287ecebe-db72-3a40-b4e4-cd3e261e948f | -15.08591 | -41.41077 | 2026-10-07 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 58.9 |
| 14c0e209-7779-3b9f-8db5-a1b40919f199 | -15.57138 | -40.5466 | 2026-10-07 15:58:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 32.9 |
| df322923-ba1f-3f0a-b3ca-15930b873e10 | -14.3753 | -41.27069 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7c755e84-afd0-3d9b-9d99-227afd42bafc | -14.77253 | -47.15243 | 2026-10-07 15:58:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3674ffb3-888d-33d9-8204-35baf53ff933 | -17.20156 | -45.09308 | 2026-10-07 15:58:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 8448e711-f22b-3d0b-a83c-6f90364edd07 | -16.85418 | -40.58414 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| ec64a742-5592-340e-906c-05057adc076e | -17.02608 | -45.9111 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 9406d400-a91d-38e3-9542-3df3ff6f3291 | -14.75581 | -40.91113 | 2026-10-07 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 8836d893-5f86-3262-aba7-025b4eaf2e12 | -15.31745 | -48.013 | 2026-10-07 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6b343bde-4a7b-33ab-b79a-b8beca1a60cd | -16.68036 | -41.47451 | 2026-10-07 15:58:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 130e57ce-1605-3ead-8796-8d8fe40301a1 | -14.68711 | -42.80799 | 2026-10-07 15:58:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b2456721-70be-349f-8e1a-b4b225810f0f | -15.97186 | -40.70437 | 2026-10-07 15:58:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| a58d4b9b-f6e0-32a1-a154-fa497925cd3d | -14.35357 | -41.27374 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 81b3808a-25f4-3219-8b77-424205a717fc | -16.79867 | -39.18081 | 2026-10-07 15:58:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d3e2e33e-f8a1-3fd8-a087-c703c06f8d17 | -17.02042 | -45.91167 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c73b898a-4951-3da1-be6d-20db2bad6e22 | -16.65428 | -42.45673 | 2026-10-07 15:58:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5aed9bb5-55c9-3b73-8ad2-f38204c2fe67 | -14.53902 | -44.03442 | 2026-10-07 15:58:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 16.6 |
| e15ea88a-96a4-3643-917b-08e6c9b6224f | -14.98669 | -41.66909 | 2026-10-07 15:58:00 | NOAA-21 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 61e9e5f1-0ef0-37ad-8256-7835e6ce2f4f | -18.29034 | -42.55718 | 2026-10-07 15:58:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| a04957cf-f1e5-3cda-bf49-7a08a36df989 | -17.01829 | -41.03446 | 2026-10-07 15:58:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| db3c607a-0351-3e66-9020-58bba068fd68 | -17.19367 | -43.51969 | 2026-10-07 15:58:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| abf8f9e4-f60f-346a-ba23-64338e9d7dd2 | -15.79761 | -43.27276 | 2026-10-07 15:58:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b23d4b29-8908-33e0-b204-eab5e9fc3319 | -17.19966 | -43.53939 | 2026-10-07 15:58:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bfbcb131-0f7c-3b25-bcc3-b5cc34d8256f | -16.9332 | -42.10716 | 2026-10-07 15:58:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| d62e46cf-b75e-3e22-a0f4-2ba99c6d9ce1 | -15.88655 | -40.72354 | 2026-10-07 15:58:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 58784d1f-e167-3f13-baa4-e57ac59d52d3 | -16.8555 | -40.5946 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.8 |
| 7667085e-ea46-390a-a305-f71f97a85840 | -14.84967 | -41.5078 | 2026-10-07 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 443e7796-3d9b-37cf-8159-c4563e2dd8c5 | -14.35455 | -41.28091 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 115.1 |
| e3a3bf48-25f2-353b-a6a7-993a54ffc7a7 | -18.0406 | -44.57624 | 2026-10-07 15:58:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4d0205db-c77b-3e1d-b042-28eb325998b6 | -15.08543 | -41.40713 | 2026-10-07 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 58.9 |
| 338aab51-fad5-3e8b-bb6d-e9a6722062e4 | -17.19304 | -43.51437 | 2026-10-07 15:58:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0bc9a90f-45b5-3f61-a311-084f6f0fc67b | -14.90755 | -48.76476 | 2026-10-07 15:58:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 66c9abc9-46cf-3538-abd4-72ce89181c7e | -16.92811 | -42.1069 | 2026-10-07 15:58:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| a2ad5820-3faa-39e6-bd5e-68c8351f57af | -15.38785 | -41.70345 | 2026-10-07 15:58:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 809748bc-9b7d-3f7c-9e91-69609b5982ab | -16.84752 | -40.59547 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| d30a2d66-1eee-32d8-9c40-df8d6b19e2af | -14.91615 | -48.09286 | 2026-10-07 15:58:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6812eb63-9bec-3cc3-9fb0-b9a00df3ddce | -16.35984 | -42.82834 | 2026-10-07 15:58:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 351c3567-f42c-30b2-b513-d37be053ccd0 | -18.34046 | -42.38913 | 2026-10-07 15:58:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 66f56faf-01f1-3302-9d81-7ffce50821c5 | -15.00315 | -39.74022 | 2026-10-07 15:58:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 1da4dbcd-dda5-31cf-87f8-bfa432b1fab0 | -14.39129 | -41.26822 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e82d429f-35d8-3b88-b5c8-5d410804b30a | -16.12008 | -42.23072 | 2026-10-07 15:58:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| 7d7c5046-329a-3bca-a3a1-dea0d646cb98 | -15.53272 | -41.24244 | 2026-10-07 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 1f24c8df-0ad3-3c3d-8945-c3a948aa3ae2 | -16.43641 | -42.03858 | 2026-10-07 15:58:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d1467b92-9d77-38ab-91c3-ead39c522674 | -14.93334 | -41.10191 | 2026-10-07 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| ea74fe25-d0db-37f8-8e62-7220525b8bc6 | -14.56854 | -43.8328 | 2026-10-07 15:58:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b8c0c0d3-1847-3403-887e-3f1f63b56edc | -14.46088 | -40.56602 | 2026-10-07 15:58:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d6c71246-1b7f-3210-9369-e1562732cc5f | -19.05026 | -44.67035 | 2026-10-07 15:58:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ad345442-5997-317e-9447-1e10dc5a2005 | -17.74827 | -45.40031 | 2026-10-07 15:58:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| df06df89-4c12-387e-9cf5-97f0a41e3e14 | -17.52605 | -45.46376 | 2026-10-07 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 062b1f47-6668-3825-bb53-3695840d751a | -14.83273 | -43.56955 | 2026-10-07 15:58:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 47.4 |
| c6b665c3-83f3-3b9c-93d3-8ee3ef9e7679 | -14.27459 | -41.549 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 0029cd99-e844-33b4-8dc6-c977439705fb | -16.79086 | -43.90271 | 2026-10-07 15:58:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6d06c0b1-3c62-3cf7-9c12-e32904ded104 | -17.20105 | -43.54065 | 2026-10-07 15:58:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 66ecbaab-74c4-36d9-b984-b46fdb81a602 | -14.30955 | -42.30128 | 2026-10-07 15:58:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 380a2710-4d94-3ffb-bdf7-32d9db7b80d0 | -19.49661 | -42.19416 | 2026-10-07 15:58:00 | NOAA-21 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f7faf188-9834-3d14-aae1-1992188a8aa9 | -18.36888 | -42.0722 | 2026-10-07 15:58:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 20d13f91-6bd2-36c4-bddb-7e24d1c3a051 | -17.01875 | -41.03519 | 2026-10-07 15:58:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 3b1349db-6805-3c82-b8b4-6618ad87d03f | -17.1913 | -43.54131 | 2026-10-07 15:58:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 32d405b3-d71e-35ca-9b87-1570360a50e3 | -17.52131 | -45.4721 | 2026-10-07 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bc85e9f6-997b-3389-a5f4-385c509327fe | -17.02085 | -45.91566 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 996ee867-6956-3c93-80cf-4d88adf58437 | -16.45463 | -41.06379 | 2026-10-07 15:58:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 4cd20112-b58e-3407-9a6d-e780397c3756 | -14.25131 | -41.62373 | 2026-10-07 15:58:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| efda7af7-e27f-3e4f-8203-88e72ef4afc2 | -16.85948 | -40.59417 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 363bc833-1b80-3b20-afe2-3d1ceb8430d9 | -16.17271 | -41.68327 | 2026-10-07 15:58:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| c612b180-bcc0-3a23-967c-0e90086903ac | -15.22579 | -39.94957 | 2026-10-07 15:58:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |


[Clique aqui para ver as próximas entradas](README147.md)
