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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60c85fb4-dc94-3434-aea2-694363bee4ce | -19.68005 | -49.36753 | 2025-08-28 03:47:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f7701c5-cbfe-3252-b6b1-2fd0f992b453 | -13.44461 | -46.96867 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7e5e860-1475-3751-9d45-5ca6fe1cd25d | -21.68093 | -49.05684 | 2025-08-28 03:47:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d1687e7-efaa-3d06-b63f-35fbdcdd57c3 | -11.57535 | -44.65102 | 2025-08-28 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 60b8dd40-1f9d-38bf-b0ac-f3c268dab5cf | -10.32856 | -46.77215 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab67ede3-6417-3f4b-b84c-14182e496cb0 | -13.5478 | -46.90154 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c413547b-5564-3e0a-826e-d63d3c8bd365 | -11.31456 | -43.54428 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09a5f29d-81c7-3123-8322-65f9cb3016bd | -20.66428 | -43.65281 | 2025-08-28 03:47:00 | NPP-375D | ITAVERAVA | MINAS GERAIS | Brasil | 3133907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a9f79352-ab4f-37b2-91a5-3392cf8dbdae | -13.6653 | -46.88332 | 2025-08-28 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5828e628-6bbc-3871-ad5f-9d925cf74c4e | -19.82037 | -46.03366 | 2025-08-28 03:47:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a63431c-47da-31fc-af3d-6f44048933e9 | -20.73171 | -45.85576 | 2025-08-28 03:47:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76e19958-8b11-3e37-bab0-0f150534da81 | -11.13385 | -46.34345 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a41f00fa-c995-3f82-b0c4-d417a3aec5a6 | -12.86803 | -48.11712 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 14166088-4508-3b41-b2bd-d6644edcbf3b | -13.18291 | -45.28366 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 399aa8a5-9131-3f68-8fa7-379c1210f46d | -9.67859 | -47.07174 | 2025-08-28 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d60de40-ee37-36be-87b8-99f5ea738ebe | -20.67852 | -47.07996 | 2025-08-28 03:47:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cb6c403-cd53-362c-8bb0-1f6505a31ec5 | -20.15059 | -47.38092 | 2025-08-28 03:47:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 168383ac-1266-37cb-809f-12b0f902e12e | -13.4336 | -46.97445 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 05e3e081-ab51-3ebc-84a6-930393059ec4 | -11.81169 | -46.82021 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5df2752-0662-3261-9026-7a658e048df5 | -20.14556 | -47.37942 | 2025-08-28 03:47:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28b9cedb-6416-32b9-bc03-1f68930d3642 | -19.88693 | -42.1622 | 2025-08-28 03:47:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 32421594-a54c-3553-a406-23860e0e8a72 | -11.6553 | -46.39891 | 2025-08-28 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39f586fb-d820-3c7f-a085-dc484af37ce5 | -11.23995 | -45.00248 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbab60a6-4e76-3764-9418-0dc8f4822de3 | -13.47901 | -46.85289 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f72af3a3-8b67-3de3-a61c-70f653b562e2 | -13.08438 | -46.34526 | 2025-08-28 03:47:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c110d224-10cc-305f-9dba-f6680ae129ad | -11.24356 | -44.9803 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae294ddc-7e50-3c28-9afc-375cda8c827f | -12.78649 | -48.17234 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3199c303-7152-3249-a868-69ffbd4403f4 | -13.46151 | -46.85314 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ea48044-7416-3959-8574-97aaacc9b2c7 | -12.78954 | -48.15762 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb565798-3028-3824-9c9b-ac82da56b325 | -19.69756 | -49.3165 | 2025-08-28 03:47:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf6e0cb7-c232-39d5-aacc-4ef4c705efb6 | -13.63186 | -48.21648 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb4af9f8-4d63-3797-8970-7ac7de4a3720 | -13.6151 | -48.23597 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84882eb4-f2ad-39ae-93b9-f4019785c9b0 | -12.80302 | -48.15425 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1816e7aa-8667-332a-b05b-029a46591720 | -13.46548 | -46.99102 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25028d3f-540c-3b5a-8bc8-b17eb626e986 | -13.45088 | -46.84803 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd3bb5a1-3d34-351a-8775-a01fa98cbed5 | -13.98904 | -46.34203 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a00c46f-9d4f-353c-b223-de5b156e6088 | -13.46004 | -46.98886 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8688834e-f5e0-308c-85d6-7f6baf584dec | -13.52281 | -46.88061 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 656c8e74-1901-3879-a550-6ef19373bd69 | -13.82863 | -46.68741 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbceec47-4fb1-38f3-a6a7-1a7671ee8ad0 | -13.43065 | -46.98881 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bd0a775-1954-3e80-b03d-04d487951973 | -11.79857 | -46.79581 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e6f2d8a-7e6c-3d9d-abab-69ae509fac8b | -13.42699 | -46.96878 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 00cc2168-e93f-3cc5-81e4-475f8dc537e3 | -20.14626 | -47.3761 | 2025-08-28 03:47:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cd07907-fad7-35f1-b592-ff7a48bcb89a | -13.08035 | -46.33693 | 2025-08-28 03:47:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76242939-24f9-3ba6-afb3-b24989bdedea | -12.81313 | -48.1362 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f72621c-e0bd-3ed5-aa3f-52e9d0d95c1d | -14.1426 | -45.40588 | 2025-08-28 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9c9114d-5bf2-3f9d-ba75-4fa57154466b | -19.53866 | -49.51631 | 2025-08-28 03:47:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e112c2f4-0ff4-3bf6-89af-dad0fa4f0461 | -20.15128 | -47.3776 | 2025-08-28 03:47:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c351614-725a-36eb-bf4c-7871f4c5d2fb | -13.42864 | -46.99021 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84e80cf1-23f5-3939-a06a-531b9854bd40 | -20.25611 | -42.00898 | 2025-08-28 03:47:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c0461ca2-d1ee-3b4e-8b15-3678fc2bf774 | -13.42208 | -46.99366 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e84ad635-6dcc-334c-923d-09886a886f93 | -11.33604 | -43.53293 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9c4604a-f322-3b4e-a43a-91198cd4631f | -13.46783 | -46.8506 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1186088c-8aae-31cd-8b65-f769b5633230 | -12.86748 | -48.11727 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fed6cff3-619e-3536-ac5b-9dfa519a991c | -11.65134 | -46.38934 | 2025-08-28 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f319215d-babc-3349-95ee-f3471e2f1c6c | -13.83417 | -46.6883 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea927afa-b32e-3877-a6ad-838a88d7fb48 | -16.36452 | -43.78883 | 2025-08-28 03:47:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b4b4fcd5-06ce-3a6d-8891-019517e55de7 | -13.46704 | -46.85463 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd422125-83fa-31a1-bca6-90d637950a28 | -11.3398 | -43.53877 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3dc4302f-2f40-3c40-adb7-6a7363dccf94 | -11.80753 | -46.81096 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0249a382-a44d-38fa-b6a8-fa4d7dc77d71 | -15.07546 | -48.64312 | 2025-08-28 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ace2e8c0-1780-3d39-8573-37958254b5d4 | -12.40855 | -47.79478 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 458f5026-8a7d-3798-a351-056fb0682da9 | -13.42336 | -46.99567 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c767a2f8-7827-3601-8aca-16a11e69cc58 | -13.47258 | -46.85603 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d58c01c2-76c0-329c-810b-3f4bfd1dd722 | -11.79698 | -46.80387 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20e9f68d-d852-3a25-8081-12094559299a | -13.53263 | -46.88985 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be7c7a96-79ab-3d05-ace7-4fa9baf3dc47 | -11.55399 | -46.3376 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96a770c8-d05a-365e-b65e-d314e69a6613 | -13.439 | -46.84921 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f7d9382-93c1-3502-8f4f-0aba77fab7df | -11.55088 | -46.35351 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 350008ab-2727-3fc7-9524-0359d135881a | -20.13571 | -47.37555 | 2025-08-28 03:47:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2e1b55f-c1f4-3342-ba24-fb8deb3f987c | -11.34735 | -43.55046 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5017bc18-44fc-3b29-9111-f9fff4ecf44d | -12.8632 | -48.1095 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f669cd7-2859-3f1e-8835-659dc655f487 | -11.21631 | -43.37382 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 21c068f8-ad9d-3a27-831e-b72d75937ecb | -12.71139 | -48.17215 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf4efdd1-70b9-3f6f-9c8f-afa8e9dcdb02 | -19.37676 | -44.86332 | 2025-08-28 03:47:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fcb02bf-6cb9-367e-abd0-227f5bd1bc3a | -12.80715 | -48.1342 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79694245-80fe-3320-9b29-75d11300bcb4 | -13.63688 | -48.22272 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dd7524a-0ca2-336c-85b5-f7216ab5896d | -13.18623 | -45.29385 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5659b75-41c6-3ac9-ae43-8e534b347114 | -14.13585 | -45.41373 | 2025-08-28 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69258a6f-5147-3767-85cb-2713c0883711 | -21.15062 | -42.44777 | 2025-08-28 03:47:00 | NPP-375D | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e6197043-9db0-3de5-8772-db17a6772890 | -21.13835 | -45.90137 | 2025-08-28 03:47:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 88be50ea-6830-3f75-ae5e-f492eca419c0 | -12.67777 | -48.18628 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f26073ff-8fbe-35ec-868b-e291f1535032 | -11.56734 | -46.38866 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 258e6697-ccd8-3d74-8199-395950c82163 | -13.54306 | -46.89604 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b8abeff-5c1d-36cd-9260-3d494e9ab180 | -20.1447 | -47.38354 | 2025-08-28 03:47:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aafbb0c6-6774-31a3-a122-0a5c77f8c730 | -11.74378 | -49.09025 | 2025-08-28 03:47:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7c5092f-b354-3a68-b8b3-64d9c42d277c | -13.45886 | -46.85101 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 314c1d76-4047-3f8a-b734-d11839807deb | -13.4502 | -46.85143 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc8d039e-0e59-3889-9c78-7f5f4a791db3 | -11.57963 | -46.38549 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae188377-adf5-33cf-9d42-ee310a9fb238 | -21.61289 | -48.92822 | 2025-08-28 03:47:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0ab3612-5f15-3432-90b1-11a4285c4410 | -13.43969 | -46.84574 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 472c666c-7aaa-35c2-b2c1-538a03221abb | -13.49927 | -46.85276 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2277bac6-4992-3182-bf09-f6ecec55a885 | -11.24817 | -45.47568 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 957894a6-410a-351a-b545-0e01e18df790 | -13.60019 | -48.21788 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61e82fda-f8a8-3231-9324-7e70fc2ec51d | -13.59921 | -48.22269 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9126949b-3b54-31d6-9998-726f09b28c78 | -11.56084 | -46.33234 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8f5ff52-9909-3091-8c15-2964d9cd595e | -11.23951 | -45.00227 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c788487b-77f1-3d6f-be99-59eeebfbd88b | -10.3278 | -46.7761 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a219d600-6764-3167-97f9-24e79d09d234 | -13.49849 | -46.85666 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a373df7-1bdf-397c-ac38-d8b4bb7bca1d | -13.51819 | -46.93293 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README28.md)
