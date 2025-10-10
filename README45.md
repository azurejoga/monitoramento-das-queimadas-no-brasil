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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0df6d4be-c739-30bf-b085-81aba74fcfd5 | -16.01238 | -59.54646 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 447aaddc-f5da-3c40-9961-23978b52d75a | -10.08181 | -67.53209 | 2025-10-10 05:23:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db78b877-6e5d-3983-a2aa-00838f4fa046 | -16.005 | -59.54906 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 45d1b24c-0124-3188-b1f8-9a14a5dd29b7 | -16.67859 | -47.5904 | 2025-10-10 05:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11a96d30-db01-30f7-b83f-d6bfc8ae4fe5 | -14.42993 | -48.01023 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48119380-b9f4-3df9-8ced-b0d389c03a15 | -13.37386 | -47.74935 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33551ee9-5dd6-3c51-8bc1-1e28ceee158f | -14.4212 | -47.99717 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 974d4e59-4204-33b4-99fb-16bec7899bd1 | -14.68736 | -48.06227 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 12d1f5a4-658a-3f93-828d-1f9e4869959d | -13.3672 | -47.7479 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5ea6572-983d-3cf2-88cc-e224f18ae30f | -9.79802 | -60.14609 | 2025-10-10 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66f6fa1c-6875-3f63-82f0-2ccd55cebade | -14.93753 | -46.76312 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29f01657-f98a-3519-b652-02668d3734ad | -10.6342 | -68.96826 | 2025-10-10 05:23:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a504acd0-64d0-30b2-b4fd-d5f2e32e47e5 | -14.42892 | -47.98809 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 231d8ca7-0fdc-365e-b913-a93c1a96ee8c | -13.32925 | -48.48095 | 2025-10-10 05:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bfb7760-a620-344b-95aa-f94a857bcf90 | -14.68472 | -48.06285 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9043d68-c790-3c91-ba20-0c51bab9fb59 | -13.26918 | -48.02526 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b47d81c8-3a85-39dc-8d6d-095aed37ad43 | -13.03432 | -62.33171 | 2025-10-10 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e0e43852-d8e2-39f0-be98-e8cd8df7ecec | -14.44017 | -48.01055 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 141d7164-2d2f-3202-af10-c1be44c48e12 | -15.09261 | -46.60274 | 2025-10-10 05:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 061792c7-3e9a-3bdc-8bc5-092a852f4376 | -10.82073 | -68.23356 | 2025-10-10 05:23:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe07fce1-8c6e-3bff-9614-97b64210af2c | -10.04006 | -59.3617 | 2025-10-10 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f5cd5b5-5096-38e0-819b-27443546ba69 | -14.93365 | -46.78167 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36bf3e9b-333e-353d-9ce5-676819804b08 | -16.00897 | -59.54589 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5bbcdb5-f34f-37c3-b125-d98e53180eef | -14.94914 | -46.77279 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cb557e5c-b4d6-3170-8988-6e6cbca72209 | -14.69351 | -48.06856 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5413395e-2b69-3f2d-88af-5bf05c763834 | -10.98949 | -59.06356 | 2025-10-10 05:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d23bec8a-0c4d-33a3-9527-d321ba38186b | -13.28096 | -48.01601 | 2025-10-10 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bebe893b-a657-3593-b76f-5d88132c3e16 | -14.73069 | -48.36374 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76d42c72-2658-3713-82ba-58f5cb90af76 | -16.00273 | -59.54091 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a1dba2a-63c9-3ebe-ae8a-0d233309101d | -15.42584 | -47.99186 | 2025-10-10 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5ffa831c-a121-379c-820b-71df6d6a5d9b | -14.88166 | -48.24488 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 162caed4-1283-329d-bca8-b7ae2daeaf31 | -14.93493 | -46.76883 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c103bf1-e406-3bc3-aaee-dc70f37ac1e3 | -14.88579 | -48.23748 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b82357e0-6243-3a25-89a9-b489891fa184 | -14.67795 | -48.06288 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7eeb020e-299a-379a-bcfb-9985a6d541d2 | -14.23988 | -49.08794 | 2025-10-10 05:23:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 821f9870-bc52-3456-ad0e-ee2bbca6a856 | -14.23356 | -49.08768 | 2025-10-10 05:23:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5724092-b518-3260-8561-58ee0f479675 | -17.20727 | -47.65712 | 2025-10-10 05:23:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 387d34f5-2682-3028-b874-cae418a8a56d | -15.75371 | -48.98257 | 2025-10-10 05:23:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2371d6d-6b41-31b6-ba41-a5c5d113bad6 | -15.46632 | -48.53752 | 2025-10-10 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29efbc54-8ec1-3607-bf4e-b1ba2502ebf0 | -16.67797 | -47.59711 | 2025-10-10 05:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b84e3e8b-b6d1-3273-9371-78e1f0f3fe5c | -14.92731 | -46.77193 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35a80d3a-b4fa-3434-8aba-6518c28f39fc | -14.42456 | -47.99725 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25624461-54c4-3569-84a2-3f87b401dd85 | -13.32294 | -48.4791 | 2025-10-10 05:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f74e03e2-99a9-3786-b1b5-1302d54e14a1 | -13.38006 | -47.75508 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f331f39-378b-30ef-84be-7ae55093df44 | -15.97652 | -59.52916 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b73df63-427d-374a-b8f8-b9e3f98fde20 | -14.86301 | -48.46711 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6c71672-a09f-3f3d-8fe4-7f16d4e88c9a | -14.87892 | -48.23906 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cc92da34-1b72-3830-9574-f94c30c8f997 | -14.99281 | -47.19973 | 2025-10-10 05:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e102c40-65f0-31c1-9146-edbb41543546 | -14.86246 | -48.47252 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45f593d4-4aa7-3a61-a542-5dd40cfcae60 | -16.92849 | -48.73936 | 2025-10-10 05:23:00 | NPP-375D | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 28607792-c277-3ca6-9264-ae15af497b2a | -13.68866 | -57.75732 | 2025-10-10 05:23:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef5b75e8-dfa1-384f-9de2-57b5de359b07 | -14.43334 | -48.01105 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abf9fc64-611a-35e7-bb56-9056367125a1 | -13.03775 | -62.3323 | 2025-10-10 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e252de1f-4379-3cb8-b4b1-85c1e418e340 | -9.95246 | -66.77004 | 2025-10-10 05:23:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea53a9ca-cfe5-3ee3-889e-138fd374eba4 | -16.00556 | -59.54535 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20b080cb-133f-3106-b8aa-7ee945f53a12 | -13.28912 | -48.00256 | 2025-10-10 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b49c09b8-8ec8-3658-801c-a08aab823e03 | -14.98897 | -47.20126 | 2025-10-10 05:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ad50216c-8163-3b60-a54f-76654d966f6f | -15.09142 | -46.615 | 2025-10-10 05:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3130afd-4956-3129-b665-1d956a58a3e2 | -14.92986 | -46.76704 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1174ebb2-7723-3697-8a63-8c487201cc71 | -15.74687 | -48.98587 | 2025-10-10 05:23:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0cc5d3fc-cb5a-3da7-a4dc-68b25f26e187 | -9.66976 | -66.82594 | 2025-10-10 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c28ba308-09c7-3e48-9cc2-93f72f8cd9b7 | -16.00956 | -59.54202 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b909d2b-4ab9-33b2-be70-15e79244b277 | -14.43058 | -48.00426 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e07ecf22-e38c-3a49-ad22-aede6c0bf12e | -14.42395 | -48.00284 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93fb0d32-ffb4-3443-bf54-1f5513214ca3 | -8.72127 | -67.0535 | 2025-10-10 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9416dec1-ecba-3524-9608-8dfbd4c59a38 | -16.00159 | -59.54849 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44775a56-0d81-356c-b320-58f59363468d | -13.32162 | -48.01173 | 2025-10-10 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74ed4160-875e-3927-9859-f05342da7ef4 | -14.88706 | -48.22457 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a7dcdb9-20bc-3746-b2e1-cc6215984c57 | -14.6841 | -48.06878 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6eaa4b7-d5b4-3769-a616-0a67b89d8dc3 | -14.92856 | -46.78097 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 567a7091-f75e-3c4b-994d-3602fb6664c0 | -16.02267 | -59.52466 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa4ff38e-1f3a-33d5-99e4-bac758ce8277 | -13.37665 | -47.75832 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08089584-d285-3e43-8522-69f9285f3421 | -16.00389 | -59.55646 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 709221be-c013-36e7-80d1-0a0acab911dc | -8.51565 | -66.9969 | 2025-10-10 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82e41571-6975-348f-bdc9-13195a8b31c9 | -15.11968 | -48.71533 | 2025-10-10 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35dc9251-b1e8-3f8b-8f18-0a4f87327449 | -11.75935 | -61.06494 | 2025-10-10 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98ce917b-7c97-38b9-a6ac-aa8327cac449 | -15.96859 | -59.53544 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 858be295-1fbe-3209-a4d7-5c3b60589423 | -14.8887 | -47.22897 | 2025-10-10 05:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e875f2bc-cad9-3189-8329-414f702a207a | -16.02378 | -59.49403 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f41fbad-4cac-3739-b218-ce7adc08ddc7 | -14.89573 | -47.22977 | 2025-10-10 05:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a183d479-0ad8-335e-945f-53b0d6e3dc3b | -15.97255 | -59.53233 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60b3f360-eaef-365a-a83f-f40dfeeef18b | -15.09038 | -46.625 | 2025-10-10 05:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d64234c3-37c7-3d71-b376-917d3350be41 | -13.29571 | -48.00358 | 2025-10-10 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0c1eb65-9f04-3f92-93b7-7d68b82a6406 | -16.00842 | -59.54961 | 2025-10-10 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 40c206c1-9d4e-3480-a81d-b7ec16daf667 | -9.66429 | -66.82986 | 2025-10-10 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24fd48a6-2fad-3f33-9e2f-ea90fd2103c6 | -11.76269 | -61.06549 | 2025-10-10 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35bb32dd-9203-309d-88b9-c704cbe975f8 | -14.84492 | -48.46707 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56dc2a5d-0876-3b75-89da-fcdc984cc449 | -14.88018 | -48.22616 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95ba243f-d7c5-3e08-9d55-027dc726b056 | -13.3172 | -47.99096 | 2025-10-10 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e0847b9-0b9f-3f50-a31a-b4300b05ca1f | -13.34326 | -47.7526 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b8eb8ae-fc48-36d7-8885-5c2874def0e9 | -13.26975 | -48.02029 | 2025-10-10 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abdca35b-ba29-3c65-b9f7-fcb6ef452212 | -14.94994 | -46.7648 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6539e6b-b13d-3d6e-aecd-7cdf6748d855 | -13.33031 | -47.99369 | 2025-10-10 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ffb9939-05d9-3a67-800e-96be541a642f | -14.87949 | -48.23325 | 2025-10-10 05:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93a1cd87-752b-3019-a0d8-21db2f73ff81 | -15.74774 | -48.99164 | 2025-10-10 05:23:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c15ed62-b634-36ec-ab76-29d82f493e49 | -14.93429 | -46.77527 | 2025-10-10 05:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca3d9c19-ec36-3482-88f9-4bd281357891 | -15.09074 | -46.62226 | 2025-10-10 05:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e91ff3ce-e846-3b92-bfe5-a0b00e6a909e | -15.09186 | -46.61025 | 2025-10-10 05:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2974fd1-b1d8-365e-a4c7-ab55b0886740 | -12.09604 | -64.23137 | 2025-10-10 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec67df0b-176c-3bf8-a006-540eaf3a91ac | -14.83898 | -48.46052 | 2025-10-10 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README46.md)
