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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aecb312f-ea7c-3600-a40f-bab2caed8491 | -4.3774 | -47.7627 | 2026-08-30 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 758eec69-b44b-38d9-bdd3-cce3346c46ed | -10.8062 | -45.3178 | 2026-08-30 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 0627c6ea-5b7b-356f-a346-308c9d7746d0 | -10.9405 | -43.0117 | 2026-08-30 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 778806c9-6e8a-3d06-957c-f9aa3199028c | -5.4876 | -57.1416 | 2026-08-30 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| eabee2fd-def4-3081-9208-9325a7bc1bb2 | -11.8208 | -51.0535 | 2026-08-30 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b0c1fa96-27a9-3dcc-bd1d-8fa459c3cd4b | -4.3587 | -47.7853 | 2026-08-30 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8a86fef0-9509-3032-9f09-529e3daa2210 | -4.3588 | -47.7636 | 2026-08-30 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 0dcc5592-2ff7-3b52-ab9f-63231ea30dad | -9.8927 | -60.2752 | 2026-08-30 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| f65e119f-89da-3a48-a816-0d6d0fab0dbe | -10.9593 | -43.0326 | 2026-08-30 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 291.9 |
| b30090bf-8464-3163-a3d8-d516a2bc04de | -17.4246 | -42.6137 | 2026-08-30 02:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5e1bf428-fe8e-3a79-b391-56d518449c8d | -4.942 | -55.8431 | 2026-08-30 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 70191090-0783-3134-9227-c133a9699693 | -10.7647 | -50.6579 | 2026-08-30 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| bcaa9dd2-c6b6-350c-9ec8-7bc2a2ce5d6f | -4.9604 | -55.8424 | 2026-08-30 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 185.0 |
| 0520a589-2fc3-3ef0-ab64-2282c5a827b6 | -9.0615 | -65.4169 | 2026-08-30 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b2cdc84c-b023-3735-adf4-ffa49f790b24 | -10.9597 | -43.0088 | 2026-08-30 02:40:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 206.1 |
| d219dee4-cc23-374a-9312-5bfdbc7c74ef | -5.8894 | -57.7708 | 2026-08-30 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9913de2b-700f-3b0a-85de-45333bc8b23e | -6.861 | -41.6772 | 2026-08-30 02:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| f0570ee9-e0c4-35a4-818e-f3cad3ed042f | -10.9401 | -43.0355 | 2026-08-30 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 0f13e558-3168-3bf5-bc40-81ff8beda937 | -4.3774 | -47.7627 | 2026-08-30 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 072fcccd-323c-366e-a24a-f1acb3ffbdf4 | -4.9604 | -55.8424 | 2026-08-30 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 190.5 |
| 6c36174b-c1b9-325f-9eee-a4233278556c | -10.8062 | -45.3178 | 2026-08-30 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| c1835446-cebd-3361-aa18-dc47bdd76fe6 | -9.0615 | -65.4169 | 2026-08-30 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| cc9612c6-7391-3871-8805-23cd0704254c | -10.9405 | -43.0117 | 2026-08-30 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 728c5a33-372c-3ea1-9d12-6c0a71b37131 | -10.9401 | -43.0355 | 2026-08-30 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 329.8 |
| 29cfc2f2-bbb4-384b-b2b0-4a0144a8838f | -6.861 | -41.6772 | 2026-08-30 02:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| a3bd9c9d-3dad-3521-a073-c01350e4c241 | -17.4246 | -42.6137 | 2026-08-30 02:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 96e05f87-c32b-32fc-ba16-afdedbbdf0ec | -5.4875 | -57.1611 | 2026-08-30 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 585b9975-648e-386d-be36-8ab6f6d7bbff | -10.9593 | -43.0326 | 2026-08-30 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 289.6 |
| 770b670b-0510-3c72-bb25-85a88b6a5a55 | -10.8253 | -45.3152 | 2026-08-30 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 716b43cf-f962-36da-a086-f5821435c22d | -5.8894 | -57.7708 | 2026-08-30 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 93bfc043-2b55-39cf-9af2-374bcc15ef60 | -10.8058 | -45.3407 | 2026-08-30 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 6f4adff4-bf11-3338-b660-ef9a08289edc | -10.9597 | -43.0088 | 2026-08-30 02:50:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| b8048294-990e-3dfa-a5c1-1a9ae924dfcd | -5.4876 | -57.1416 | 2026-08-30 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| a6c55a2c-607b-39d8-b1d1-c6de1a4d4b4f | -4.9603 | -55.8622 | 2026-08-30 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| fa7522a2-3d95-31d4-ac69-6de932539697 | -9.8927 | -60.2752 | 2026-08-30 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| b810ecc4-5d67-3a2c-b565-a9be678598a6 | -10.7647 | -50.6579 | 2026-08-30 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 79cf9e60-8a59-320c-b4e6-b62d6acc981b | -4.3772 | -47.7844 | 2026-08-30 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 2458f372-f953-328d-8722-158669b06914 | -6.861 | -41.6772 | 2026-08-30 03:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 0470e6e7-33cb-3786-bcf8-7ce5d16b25dd | -10.9405 | -43.0117 | 2026-08-30 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| f207a3d7-7f61-33ff-b25b-9cef1bea9214 | -10.9593 | -43.0326 | 2026-08-30 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 456.6 |
| f1725bfe-916c-3790-90dd-637d923f2be9 | -10.8249 | -45.3382 | 2026-08-30 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d5fa5aea-0990-3ebd-b213-81baf5dbcdb4 | -11.8018 | -51.0556 | 2026-08-30 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 1ba14a13-723c-3e13-8039-84cc65c21c38 | -11.8208 | -51.0535 | 2026-08-30 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 367b27fe-2832-3f66-9980-caae4a6a48c8 | -10.9597 | -43.0088 | 2026-08-30 03:00:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 9ea9141c-1b04-365a-8704-12c188771dd1 | -17.4246 | -42.6137 | 2026-08-30 03:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 1b39a109-2fcd-3ee6-9976-066795428ea9 | -4.3588 | -47.7636 | 2026-08-30 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a2fa7c9c-f3e9-3d37-b430-36d0d150a96a | -4.9603 | -55.8622 | 2026-08-30 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f8840d49-1a66-3643-9150-83375c280ab4 | -10.8062 | -45.3178 | 2026-08-30 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 369097f3-6226-32a4-94b0-d01816a9138a | -5.4875 | -57.1611 | 2026-08-30 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 95e7335a-241d-3d0c-9c13-aad356309a59 | -5.4876 | -57.1416 | 2026-08-30 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 319dcd56-343d-3e32-9076-45e54a798cc9 | -10.8253 | -45.3152 | 2026-08-30 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 79fa1249-ebee-3303-839b-febfa69c25e8 | -4.9604 | -55.8424 | 2026-08-30 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 1a515ae2-0af2-34e3-a9cb-91e200f74527 | -10.9401 | -43.0355 | 2026-08-30 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 02fdb5c0-3cb1-3173-ae5e-a4d72b9d58be | -9.8927 | -60.2752 | 2026-08-30 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 0c07436a-6148-3eb1-a824-1a918d628de5 | -9.0615 | -65.4169 | 2026-08-30 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 56d8bc9a-0447-3f5e-a1b2-135bdcb1eb93 | -4.9788 | -55.8417 | 2026-08-30 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 3ce436f7-3c93-33b2-ac11-b73406eb2291 | -10.8058 | -45.3407 | 2026-08-30 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 1b71592f-5fc0-365f-b1dd-31f42ba0ff8f | -10.8062 | -45.3178 | 2026-08-30 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 201.5 |
| a171f7aa-5488-3a06-a447-7f01d2948408 | -4.9604 | -55.8424 | 2026-08-30 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 96f4df71-fad3-327c-a42c-8227c4bd6e41 | -11.8208 | -51.0535 | 2026-08-30 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.0 |
| c431dcb2-cb7d-3dfa-99db-bec683be827a | -10.8253 | -45.3152 | 2026-08-30 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 51e50755-4a61-3732-bb00-d38b7a87789f | -4.9788 | -55.8417 | 2026-08-30 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 8aac4cf8-1275-3417-85b8-eb1304d16ba2 | -4.3588 | -47.7636 | 2026-08-30 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 5f5aa3ab-870d-3daf-b45a-9b08c8d45577 | -4.9603 | -55.8622 | 2026-08-30 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| c2c6330c-a517-31f1-a12b-3786b16ee9c1 | -5.4692 | -57.1423 | 2026-08-30 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6208de42-0dc9-38a3-b28a-1a5313864dbd | -9.8927 | -60.2752 | 2026-08-30 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 8b7281bc-3cc6-3448-8a41-8dfcb0f7df74 | -10.8058 | -45.3407 | 2026-08-30 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6fd4e09e-f02e-3c5d-9359-67e68e70e224 | -10.8249 | -45.3382 | 2026-08-30 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 718f9fcd-eeb6-311c-9f58-b5966c64ba7e | -11.8018 | -51.0556 | 2026-08-30 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 34226f27-3f13-321d-b143-4bf4caa89a15 | -9.0615 | -65.4169 | 2026-08-30 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| f4cf35f8-27fa-398c-b99a-50a991f899c3 | -5.4876 | -57.1416 | 2026-08-30 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 3f6a31a9-2447-36cb-9d02-726141787e9b | -4.3587 | -47.7853 | 2026-08-30 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 29b882cf-86a0-3c9d-800b-759dfce068cb | -10.93 | -43.01 | 2026-08-30 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40edc3a3-13d8-31ce-8979-c1b9d73513ce | -10.97 | -43.06 | 2026-08-30 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26aee81b-90f3-32ca-af8b-c850094b15f9 | -10.96 | -43.01 | 2026-08-30 03:15:00 | MSG-03 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 413d25dc-34a5-3cd8-891e-e6b7fec146c4 | -10.94 | -43.05 | 2026-08-30 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a3990ce-5ea6-365b-8b3d-9eed4608d90b | -4.9604 | -55.8424 | 2026-08-30 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 862d3916-5fc6-38e7-87aa-c6326ecf002e | -11.8208 | -51.0535 | 2026-08-30 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 16bd59ef-6588-3581-ba87-24f5cd34791c | -11.8018 | -51.0556 | 2026-08-30 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 3d926284-ed88-345f-8fb7-31492448e95b | -4.3587 | -47.7853 | 2026-08-30 03:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c458fbfe-28ec-3c02-9e93-c5d951150c0b | -9.0615 | -65.4169 | 2026-08-30 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 261ad57f-9a0d-3439-b732-212926f567ed | -9.8927 | -60.2752 | 2026-08-30 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7d23f2eb-07a8-31fd-a596-7e894f73456e | -4.9603 | -55.8622 | 2026-08-30 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f34b8657-cb42-3620-974b-b4ad5f734fe2 | -5.4876 | -57.1416 | 2026-08-30 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ce4d5e64-b74f-3ca9-9dfb-125c2862cb04 | -4.9604 | -55.8424 | 2026-08-30 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 1f654710-71bb-3dec-ae11-fd46f6779628 | -9.0615 | -65.4169 | 2026-08-30 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 7d0ae34e-8a17-3835-9bd5-48fe59a1538c | -9.8927 | -60.2752 | 2026-08-30 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 627ff87d-6d4b-36a8-88e5-5345bc6405b2 | -11.8399 | -51.0513 | 2026-08-30 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| e931320d-9772-34f0-856f-7400ae76fa25 | -4.3588 | -47.7636 | 2026-08-30 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 317b5589-f295-382e-bb24-19e273ca7f31 | -11.8208 | -51.0535 | 2026-08-30 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 93465c0e-15b9-3c84-9771-4c2421ef73aa | -11.8211 | -51.0322 | 2026-08-30 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 5ab1058d-d14b-37db-bebc-3536f68726b2 | -11.8018 | -51.0556 | 2026-08-30 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 147.1 |
| dcecf1da-9ad5-3d0c-9c4c-a30c2a2f5583 | -5.4876 | -57.1416 | 2026-08-30 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2b738238-71e6-3972-af39-8aa6cff4c444 | -17.4246 | -42.6137 | 2026-08-30 03:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 688a6583-164c-374c-bd54-16faadb08553 | -7.04573 | -42.20429 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd027d5f-6870-39b8-a914-577c94a8bf20 | -7.10049 | -42.21663 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bbfaa467-72b9-3748-9129-19e970ffbd1a | -7.05486 | -42.15232 | 2026-08-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 013e941b-d4bc-380f-8734-961347e5c128 | -7.18007 | -43.71761 | 2026-08-30 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc04f93e-3516-3bdf-9931-a4c2ac8e0b8e | -8.31795 | -37.26725 | 2026-08-30 03:36:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f7ffeb64-59c7-36f1-979b-f4bc7d756f64 | -1.99917 | -44.79846 | 2026-08-30 03:36:00 | NOAA-21 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README22.md)
