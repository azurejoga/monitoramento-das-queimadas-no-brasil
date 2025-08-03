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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9f89123-7fb3-3e38-ba41-a19b8bc2c82f | -12.64909 | -44.4927 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93642db7-f1a0-34c3-be59-e5b126b86fe0 | -12.41278 | -47.06316 | 2025-08-03 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2088812-5f0d-38cb-981e-7af14595afdc | -12.63119 | -44.49965 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9183c6d6-7a99-3d7c-9073-3a1beb4954fd | -19.13488 | -43.57996 | 2025-08-03 03:38:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67a960ca-15d7-35f5-bd11-f0e51252c7a8 | -12.42308 | -47.04437 | 2025-08-03 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a65f742-7f74-3963-ab88-ff838c60e60e | -14.16546 | -45.4445 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abedd44d-8719-3149-9790-5f2b52261d8f | -17.21245 | -44.85363 | 2025-08-03 03:38:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6ab122b-c29a-3d66-b63f-1ff86c85cebe | -13.67235 | -41.37088 | 2025-08-03 03:38:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1af77579-fc33-32b7-9aa6-e254f813d946 | -19.13577 | -43.57544 | 2025-08-03 03:38:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5eebaec-59d0-36bf-90f4-307c366810a0 | -13.67288 | -44.22401 | 2025-08-03 03:38:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3429a2a-9ba9-3f2a-8697-aee3af4dfe60 | -18.5041 | -45.681 | 2025-08-03 03:38:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a7870f3-5ce6-3c09-b57a-ea95877247bd | -14.16474 | -45.44815 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff8cdfce-a969-32a5-a73c-df67c5e54ef0 | -12.63241 | -44.50356 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9810fcb1-f494-3f89-8e22-e6c0df4298c5 | -12.63371 | -44.49673 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fe4b353-d397-31fb-92a8-9d13c94a2e8f | -17.06765 | -46.63443 | 2025-08-03 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eba77b6-9292-3d97-8600-f0ab25296eb4 | -14.1702 | -45.44937 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfe17251-8c0f-3574-bfbe-dda9215020cc | -12.66694 | -44.51411 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58c8ae67-d110-3dbd-93e4-d58d57e6e2a1 | -12.6338 | -44.51438 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85e506a1-3225-319b-ade1-4f02f2993557 | -12.42671 | -47.04595 | 2025-08-03 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20bea0a0-064f-3cb5-bcc1-08d3de3bf938 | -12.63186 | -44.49624 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ba8565b-8b54-3906-a6f9-19dc20f276a1 | -12.67024 | -44.49714 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7aed03b1-49ab-366e-bf6c-06bbad027336 | -13.69433 | -41.37053 | 2025-08-03 03:38:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6ef33652-78fe-39ff-bd78-7499f1f8fb64 | -13.3777 | -41.3419 | 2025-08-03 03:38:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc7cab47-1935-3125-b89a-8754f1722ff1 | -13.06917 | -47.44635 | 2025-08-03 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4166c702-0d67-3853-b542-936bfd6c504e | -12.65967 | -44.49491 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 483f5fb0-57d7-3243-8dea-3db3a7c37f87 | -14.16623 | -45.44011 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f768c33e-b821-3c07-ad8b-5bf3dfdfa22b | -12.65367 | -44.52558 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc8dc5eb-9743-31b3-baf0-74adf1b8ed36 | -14.17278 | -45.46525 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e460850-4f2b-3944-befc-588adcf208e6 | -14.16871 | -45.45587 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79386389-da92-3076-8a6a-2afcc11438dc | -19.50094 | -43.83164 | 2025-08-03 03:38:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1b05e42-fc98-3bfd-9962-b449710336d6 | -14.17422 | -45.45792 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c95255ff-3d5a-33be-a522-ea090e07ec65 | -13.69358 | -41.3746 | 2025-08-03 03:38:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 966bf8cd-f473-3b74-8b67-fac797458aae | -12.66694 | -44.48582 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b7c927af-5454-3401-ae8d-8b66726cea4a | -12.63783 | -44.49393 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2f3c659-fd47-3b16-89d3-497f26c71f8f | -14.16946 | -45.45222 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3394db2d-200e-32d7-ac4f-0da5cd2f887c | -18.92745 | -46.79106 | 2025-08-03 03:38:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb96f51b-2466-307f-9ca2-b700d21361e6 | -14.16077 | -45.43891 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60dbdab5-7077-36e8-a554-bb37c9b38850 | -14.16143 | -45.436 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9fac6cf-f334-365f-8cd4-e4d00130e166 | -12.65831 | -44.53008 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d314714b-15a9-34d6-9092-ea21d7c03e0d | -14.17268 | -45.46441 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f489c55-bf84-3198-8e9c-73222af716e4 | -14.16226 | -45.43164 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd9f0733-fe8a-36c7-bc8b-f5bdc82fbc33 | -12.63306 | -44.50014 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54bb63f9-f8ad-383a-8ce5-1eb028a3dc76 | -13.07255 | -47.43002 | 2025-08-03 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01f8bfc2-ddb0-3785-bb4f-35461d0c066b | -18.7803 | -47.46727 | 2025-08-03 03:38:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32a5c5d2-3374-3022-9ed9-b99c2e8362f8 | -15.60322 | -46.52614 | 2025-08-03 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15731560-b0cf-35c5-a2ef-829b2afe4af8 | -14.1567 | -45.43111 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b26199bc-b3f7-3406-8bd3-4872cf611e26 | -12.67223 | -44.48692 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22dd48a8-da72-3227-b391-faf77562b158 | -19.62194 | -43.17695 | 2025-08-03 03:38:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2dbed7e2-c36d-3c4b-9d81-746ffa701317 | -12.61601 | -44.6611 | 2025-08-03 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 681ff41e-1cac-307b-b3fe-9f719afcc6df | -14.16618 | -45.44086 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8f583b2-671d-3b85-8c80-4937f427d41f | -14.16474 | -45.44738 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7583c8f1-f3ac-3474-bd6b-e726d0145198 | -13.67735 | -41.36753 | 2025-08-03 03:38:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 077dcb07-c1f8-3beb-8248-a6168ca53c6f | -18.22639 | -44.70409 | 2025-08-03 03:38:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cad96c1-22e9-32c4-b371-83309302185b | -12.43504 | -47.03718 | 2025-08-03 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40f1654e-2614-324d-87cc-87f98a174e51 | -13.6851 | -41.37307 | 2025-08-03 03:38:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ec9ba7e3-a91a-3113-8024-e9d6a0f4c3a1 | -14.1735 | -45.46158 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c14e424-bbbc-3b48-b3bd-7f472540ba21 | -12.67822 | -48.10316 | 2025-08-03 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7321f1d3-c95e-3b3b-9ca7-b39d5a1f0058 | -16.13159 | -46.87737 | 2025-08-03 03:38:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae04698a-0d7d-314e-a859-df364b9d5323 | -12.38184 | -45.86736 | 2025-08-03 03:38:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7e741b7-4fd9-3129-ad61-20bf09f0dbd0 | -13.07912 | -47.4301 | 2025-08-03 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7583f80d-0460-38a3-8b4c-11de1d728eff | -12.65834 | -44.50169 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d09eb987-faeb-3e46-8c54-06ddf7f4ad3e | -13.6731 | -41.36682 | 2025-08-03 03:38:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 20657434-6686-35fc-abf9-a9ede527de44 | -18.50479 | -45.67771 | 2025-08-03 03:38:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57597885-5c7a-30c7-9d42-c8f26c6908b4 | -12.66363 | -44.50282 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5167e3a0-c983-38c0-98f0-1010c0b4eb08 | -14.14579 | -45.42863 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 757da83f-a885-3e0c-a0e0-ad15899e396d | -12.65371 | -44.49719 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a20a0770-2c13-3ae6-a6d4-679628dda460 | -12.70144 | -45.03729 | 2025-08-03 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 64d6d49b-34b2-32ed-9efc-d15159dc5ebc | -14.14506 | -45.43229 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffd64adc-660a-3688-a8f9-d4023a014bbf | -15.58812 | -48.51156 | 2025-08-03 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34d895f4-a389-3b25-981e-9e3ea9d98608 | -13.06398 | -47.43964 | 2025-08-03 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ecf6e941-c873-3588-9796-bfd15d47da3b | -12.64446 | -44.48821 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e31fdf00-d510-3804-8de7-888e875617f7 | -12.42776 | -47.04093 | 2025-08-03 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6aa48672-b516-32c7-b96d-32bc63f74b6f | -20.15466 | -41.17782 | 2025-08-03 03:38:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 38054f08-ae5b-34fb-b2a1-b246cedcb48b | -14.16549 | -45.44374 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ff2b711-be7d-3f46-af88-6d14d5861141 | -18.83787 | -46.45454 | 2025-08-03 03:38:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a87d3c0c-59b1-3aa3-a151-bbf738c39828 | -12.653 | -44.52901 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bcce2648-40e0-30ff-8cdd-3b3a3235459a | -12.65965 | -44.52324 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 145d7a7c-70e5-3d7e-9966-ca639b61f099 | -12.6385 | -44.49054 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bf61483-b8ab-38eb-9341-b98ca2649bf0 | -12.63515 | -44.50753 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ab725c5-6c92-3621-a344-43c92cd56511 | -13.68934 | -41.37381 | 2025-08-03 03:38:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 974fce0e-1935-35c0-99a9-d8cf96d0d70e | -14.1669 | -45.43721 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5101dfc3-8a44-3946-88d5-27a870b788e0 | -18.86247 | -41.99228 | 2025-08-03 03:38:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7b2db735-0555-3c28-b96a-94ce9cd55797 | -12.66495 | -44.52431 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87af0660-5c0c-3490-a70a-4d4053ec9413 | -13.07027 | -47.44106 | 2025-08-03 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 859547e5-41fe-3897-ac04-f1d5b413b66c | -12.66562 | -44.5209 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06e9de4b-6548-3b90-9619-17e658388ffe | -14.16948 | -45.45302 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b58f7a68-662e-3467-85bf-4fd44d732d36 | -12.65898 | -44.52666 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db5af730-9720-3bbd-b6d5-669f5582217b | -12.66164 | -44.513 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0b27c1a-ba7d-33f9-9406-09d430588663 | -12.659 | -44.4983 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa464a00-dbd2-3eb1-8c37-73e7cd9f674f | -11.94517 | -44.97294 | 2025-08-03 03:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76f8e3c2-7fe5-3644-a74f-fe8226818e20 | -18.83938 | -46.44735 | 2025-08-03 03:38:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 39dee0b0-85db-3b95-9743-df92f4ce56c9 | -17.21304 | -44.85064 | 2025-08-03 03:38:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd566efe-a94b-3641-91c9-cd870e66f461 | -19.62026 | -43.17348 | 2025-08-03 03:38:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0632a578-4bd6-313f-ac80-fcc3e3470230 | -13.69783 | -41.37534 | 2025-08-03 03:38:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dbd20f25-449e-31db-bd8e-7faddda62cdc | -18.83405 | -46.44613 | 2025-08-03 03:38:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c2fe12fe-6862-3a1c-b176-031a60cd9bc5 | -19.29852 | -46.15121 | 2025-08-03 03:38:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| badcd2f5-1eb2-38d9-8e67-ddbdd76ff7fe | -14.14033 | -45.42742 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 403e9483-6b90-3bb4-bc26-ac424363b880 | -13.07138 | -47.4357 | 2025-08-03 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 820552fb-facc-3ea8-80b4-91d148a65e6d | -12.41962 | -43.49143 | 2025-08-03 03:38:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 750318f0-41d1-3605-b189-3f807b034cdc | -12.66628 | -44.5175 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README12.md)
