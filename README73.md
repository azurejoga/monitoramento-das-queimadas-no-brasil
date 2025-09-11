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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11548ed5-74d3-3323-b9b2-b0f942b6a8f4 | -18.28897 | -47.67709 | 2025-09-11 04:25:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2c0e295e-cf8e-3ef5-99ed-926e3b42e89c | -15.54874 | -54.76238 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c52f470-5d10-3da5-acb3-3113800cd8af | -18.01497 | -47.13797 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5634fb89-e5e7-3464-b4d6-ef62caca21dd | -16.60966 | -49.77763 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cadf942-4e02-398a-a4f7-954a248e5f57 | -20.09088 | -47.35637 | 2025-09-11 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f95dad6-06be-3e85-bb9b-dd2dd5a67fd0 | -14.91789 | -55.93604 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c69d1b2-ebfd-3936-a2fb-771f5b3987ba | -17.83096 | -46.7331 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb160c67-41e8-3ee0-8e5d-e8cc62485fca | -15.80504 | -52.27904 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3101c009-58f7-331c-83c2-142fef75003c | -16.05245 | -49.99244 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1998333d-2d8f-314c-9500-88f453738391 | -17.24629 | -46.08494 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5a2d222-f4cd-33c1-88b4-137214528d80 | -21.06085 | -46.14585 | 2025-09-11 04:25:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 85ce21b8-b5a3-35e1-a84a-b3ff690bf8ad | -14.50218 | -53.94701 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07d6223b-7431-3007-b4ee-105fa5f09301 | -15.67143 | -47.03395 | 2025-09-11 04:25:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83d91b61-85ef-3d3a-b714-a1f1b5f39aef | -17.75173 | -44.49718 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed60010f-6ee9-34c2-9494-8155e813a826 | -20.44399 | -50.0013 | 2025-09-11 04:25:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25860b91-ab48-319a-98dd-6565c0702126 | -15.94669 | -46.77013 | 2025-09-11 04:25:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e367ff09-4b69-32f8-be7e-537852d6f69a | -22.51824 | -49.08934 | 2025-09-11 04:25:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3e02633a-9dcc-3034-90b2-e9eac69b9fb2 | -14.94067 | -50.10917 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa988814-17eb-30e5-84ec-ec26b269c149 | -19.66085 | -45.85226 | 2025-09-11 04:25:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 696cc636-993d-349b-8965-c00542397497 | -16.55505 | -49.73943 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4b16716-42df-3f0d-b736-4b7d0bc1e33d | -15.672 | -47.03037 | 2025-09-11 04:25:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8fffd61a-98cd-3b8b-8cb4-4ed618ed1413 | -20.38696 | -46.63128 | 2025-09-11 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 989e6696-c1d6-370b-8bdb-16c7a2eaa593 | -20.93538 | -45.79157 | 2025-09-11 04:25:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eee91c7-c53e-3ff5-98b8-6dfbc1e24d1f | -20.07623 | -47.52753 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8bd31aa-7247-3686-9e1a-0d7d1ae59908 | -22.79071 | -45.62107 | 2025-09-11 04:25:00 | NPP-375D | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6ad8bb74-1fa2-32f6-abc6-9ee33c224815 | -15.79857 | -52.24557 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db3258ee-aef9-3c75-a431-bb9a3636a77e | -14.94432 | -50.10993 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bfa5b8bf-b6ba-3dfd-ae2a-c5809392285b | -16.63019 | -49.76423 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6309fc08-0a6d-3435-a9c4-ec8519336b84 | -18.01024 | -44.45073 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faa3ebf2-bc4d-3277-80b5-2eda0eedf133 | -19.49141 | -48.45188 | 2025-09-11 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1cf4bf00-b269-35e6-8fbb-1d134c3507f3 | -17.94107 | -44.48829 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8687c7d2-a5d8-38be-87fc-9745083987b4 | -15.70074 | -47.89718 | 2025-09-11 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 153f3469-7a76-3677-b215-edd1317c20ac | -19.70131 | -45.92636 | 2025-09-11 04:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b74360ad-472a-3ebb-aab2-ec7d8e56e946 | -14.91858 | -55.93262 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3483952-16cc-300a-9139-08bdc97903a8 | -18.58908 | -43.87036 | 2025-09-11 04:25:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99f23f36-37af-30f2-ab94-975f6e6f5d7f | -15.80621 | -52.22732 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78b88d2a-2b6d-344d-8540-2dc8ae0c1167 | -21.00111 | -46.05584 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 98291dc9-a9e2-3264-901d-ceffd15ed8a3 | -15.13634 | -48.61063 | 2025-09-11 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9d23d936-0058-3e9a-89b2-924b891f078b | -17.9048 | -44.58796 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 182d8468-93b1-31b9-bf23-7759392cacee | -17.55699 | -44.5549 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a844a30c-a3d1-3bef-8abd-a27006c7fd82 | -19.80703 | -47.16055 | 2025-09-11 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c67bdae-8ab0-3395-acf8-b490962de09b | -17.47035 | -45.10066 | 2025-09-11 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fa88bed-9d39-392d-9025-9a3909f070d5 | -17.75515 | -44.44759 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fb7a39c3-c57e-3d8e-ab29-06b72431f1bc | -17.24977 | -46.76054 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14017c4f-d630-39c7-a501-356dbb996d5b | -20.46449 | -42.85223 | 2025-09-11 04:25:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9f20b0a9-c09c-3b15-b215-765013a019a2 | -18.59214 | -43.87559 | 2025-09-11 04:25:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91fab3d0-9c30-3484-92e6-c514e48ee814 | -15.80364 | -52.22791 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72bd1725-e800-3aa0-9f4c-0d3bc0af800d | -17.83153 | -46.72943 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26a4cc6b-afec-3da7-8bff-2c21d8279ee2 | -15.80088 | -52.26687 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fb151a40-4309-3083-b103-a8499e766b77 | -20.06876 | -47.54215 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b75698b-7dd8-3fcc-afa3-7e943e036c31 | -19.88399 | -44.05679 | 2025-09-11 04:25:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fb61996b-0065-3ff3-b0f8-38d7030d7e21 | -19.96684 | -43.81466 | 2025-09-11 04:25:00 | NPP-375D | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f44579c7-ff43-3c7e-b8f1-c7fce31ca959 | -20.06813 | -44.65695 | 2025-09-11 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c5dbc7a-50ff-3a4d-9d6a-0780f2043e1e | -20.08311 | -45.9865 | 2025-09-11 04:25:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c9ca807-7bfa-3eaf-bb69-6c6d1a7cf7a4 | -17.90419 | -44.59211 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6f3ea42-1bc2-326f-83c2-0307af3e32ee | -15.81446 | -52.22848 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d15ec32-e90f-3fb1-b9c8-d28cc7f8bd98 | -15.15766 | -52.42167 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80ea30d2-06ce-33be-adf2-5c5bc3283885 | -14.8873 | -55.85098 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5ff76e3-b702-3f87-aa1e-664e8c49e95f | -15.79787 | -52.24928 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e5ddf2b-ae4d-3abe-8f69-e1a32b4fb4a1 | -21.81469 | -47.23515 | 2025-09-11 04:25:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 09991ced-830d-3737-b6cb-e9fd040583ed | -15.1066 | -50.14079 | 2025-09-11 04:25:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a0d098d-e758-32ff-b431-78cf63f858be | -17.76698 | -44.44122 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| faf3828d-9b56-36be-a9a1-7a30ba806d47 | -15.7991 | -52.26544 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81bdbd75-50ab-316c-a297-c711b5ac34a5 | -21.56758 | -51.93109 | 2025-09-11 04:25:00 | NPP-375D | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a2b35e5-893b-3d95-bd78-9c02aa4f3f1a | -17.68315 | -44.19681 | 2025-09-11 04:25:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa6eee38-52a4-3d02-8361-ffe7ced62c3f | -21.45501 | -45.14156 | 2025-09-11 04:25:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5f11566f-5a64-3714-9c26-6fd220329c49 | -21.35733 | -44.22697 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b439c924-6f82-3b3c-9ed3-36993a4c89ba | -16.43183 | -45.68938 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fba7c91-dc17-30c8-9fd5-8df82614a1b9 | -18.34765 | -49.33004 | 2025-09-11 04:25:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecd6d028-f9ec-328a-b012-07b262f62977 | -21.57125 | -51.93184 | 2025-09-11 04:25:00 | NPP-375D | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d381e854-5c66-34ac-bce5-8fbf489f234c | -14.88994 | -55.83756 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ab92ae7-68c1-38da-8475-eb8cad640b7f | -17.81982 | -46.7387 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e90ef0f1-536d-3826-97fb-869dfb672e00 | -21.43003 | -45.47385 | 2025-09-11 04:25:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c0b4e4a1-b420-386c-b24a-1c90a6a31814 | -19.99045 | -47.62689 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cd1e9d39-57e4-3797-b31d-033654f69b09 | -23.0898 | -46.66905 | 2025-09-11 04:25:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 301c1e11-5b33-3b95-a8b5-2c751c1efb12 | -15.66753 | -47.03699 | 2025-09-11 04:25:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7e04f19-050c-393b-bfbb-95e8f53f4f4b | -15.60104 | -52.74267 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c22f6d6-0444-323b-95d8-8f50e83c798f | -21.77518 | -50.83732 | 2025-09-11 04:25:00 | NPP-375D | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 424db6e9-2fd7-3f2b-957f-31734a71acf6 | -19.01895 | -46.25494 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ca824f1-51fe-3694-a238-1b92ad523eda | -14.88602 | -55.87659 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50818f0a-e002-3ca0-a581-6f8323bbb5e9 | -20.33799 | -46.61138 | 2025-09-11 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 619f11bb-f647-342b-ba7c-a7f8e190ba47 | -20.00826 | -47.62244 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2b5f38a-394c-3934-9a64-d097f479406e | -15.14591 | -48.60756 | 2025-09-11 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d236d3e2-8440-36e0-995f-7dc6958b9277 | -17.55462 | -44.54624 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b578a2c2-fc42-3ae8-a7ab-f954e28dc716 | -17.50346 | -43.75435 | 2025-09-11 04:25:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41421c2e-d256-32ce-8800-ced8e1434a63 | -18.58327 | -43.40331 | 2025-09-11 04:25:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 354e01f8-77ff-318a-9dea-d565b6903b15 | -19.9549 | -49.27295 | 2025-09-11 04:25:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 76d76fa0-2ae5-3c9a-a58d-9e7975f4fee5 | -15.14726 | -52.40765 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ed920c2-7729-32bc-a116-a5d228a0b8d3 | -20.07106 | -47.52741 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72736af9-85be-335e-8566-ff06ddd49322 | -15.50318 | -52.92018 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e567460-a17f-3ec0-8d05-cf6d8d38b7de | -18.00831 | -47.13682 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c0ea19e-1be4-3dad-a3df-66d775fd7251 | -17.32287 | -46.67921 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2cdea2b-1df6-3ef5-be13-de73486dc981 | -17.46633 | -45.10396 | 2025-09-11 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f99db780-c1cd-360a-b5a1-344947dd9477 | -14.89917 | -55.84618 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92cd3b85-f3a4-3e65-97d5-959785725aca | -17.55168 | -44.54149 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 947df680-7879-3d27-946a-b2903bb94870 | -19.48005 | -44.32086 | 2025-09-11 04:25:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b1f52a0-3624-3ebc-b737-a289ed8c0ee1 | -15.80776 | -52.22845 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76667811-9340-3ac9-8181-612e461d1b14 | -20.07325 | -47.53537 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccc81bda-f4a9-3eb1-abc9-f2a16f5a9680 | -15.79573 | -52.26071 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 917ccec3-590d-352a-becd-3173aa32b695 | -17.26968 | -49.20865 | 2025-09-11 04:25:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README74.md)
