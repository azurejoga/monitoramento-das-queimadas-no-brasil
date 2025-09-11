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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08cee3fc-eed5-3100-8cb6-aaeafb8339d6 | -20.35024 | -41.92554 | 2025-09-11 03:57:00 | NOAA-21 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f32b8395-2839-3c73-85ae-faa6ff53722a | -20.40277 | -46.2756 | 2025-09-11 03:57:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b73dd064-c485-33e9-a100-d099f38d95e7 | -15.52744 | -48.563 | 2025-09-11 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbffaf18-a655-311e-bef6-2bd32e79993d | -15.2312 | -44.04101 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6a7d2c0-10b9-3b3f-a832-3deda8de2582 | -16.61014 | -49.78507 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d048a9b7-fbab-3e1c-843d-6bfa430985fc | -20.70748 | -46.05928 | 2025-09-11 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02871b1c-ff1c-322c-a6fd-25861dec9195 | -19.16277 | -43.05397 | 2025-09-11 03:57:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4423cf04-eb7f-3a07-9314-405a56a494d8 | -17.83136 | -46.73774 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c845f7d7-ef29-3a04-95b3-b73ae8327453 | -18.34951 | -49.33169 | 2025-09-11 03:57:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a22b1ab3-b39c-341b-b2a9-70ec03aa3f2d | -17.94999 | -44.4857 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b394d2b5-e747-36b0-a59a-78b74b90dce3 | -19.23212 | -48.00438 | 2025-09-11 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 47bb919c-c320-3681-aae4-6ed21263c213 | -18.0829 | -45.4267 | 2025-09-11 03:57:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b634ec4-8289-3d7d-8608-ac3b2b010c5f | -15.21874 | -44.04786 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3cb2aad3-5bbd-3816-bbdc-11ce8a7d67a5 | -17.50258 | -43.75249 | 2025-09-11 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27fb27d3-64f6-364d-9343-aa8e549bf528 | -20.00192 | -47.61028 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16ba2531-19f0-3300-9293-56550d1d527f | -18.03879 | -42.70282 | 2025-09-11 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 677d05b9-84e5-3ee0-acde-d4f9d772e7a9 | -15.24879 | -44.02605 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bade979a-7992-3b3c-8b7c-f56cb8e55138 | -19.18907 | -48.79476 | 2025-09-11 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd318cc9-f2ba-35f2-bcfe-686adfe7a393 | -14.14416 | -45.41316 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88cf4217-aa83-3132-b26a-f82ab2f65591 | -15.13314 | -52.45167 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fc7c5a71-4d9c-382e-a555-90be7ae3ae94 | -20.04027 | -42.73581 | 2025-09-11 03:57:00 | NOAA-21 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 94151dd7-31e5-38a3-937e-3a9c8429e2c2 | -17.56539 | -40.63462 | 2025-09-11 03:57:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 708335eb-a577-3902-952e-16fbc5bbacc6 | -17.90817 | -43.39971 | 2025-09-11 03:57:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e8d9272-49a8-311a-b83c-3e487c462c7f | -17.57866 | -47.49005 | 2025-09-11 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7d0bb60-2b71-359e-9b19-9ddac0b4d1db | -20.53736 | -47.62539 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f1f8bf4-57d7-3c28-93d6-704963e39ad7 | -15.78173 | -43.13521 | 2025-09-11 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 73f52878-6d04-3eb0-997b-21f4395de4e7 | -19.98642 | -47.6234 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 78cd0697-d9e4-3931-91eb-edae2ad67cde | -17.70941 | -44.43562 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 47a82f1c-7c1c-339d-bacf-dea92f77d40b | -15.13172 | -48.04961 | 2025-09-11 03:57:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93b33365-dc78-367f-b587-24194863ac34 | -19.35554 | -41.30434 | 2025-09-11 03:57:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 15e6578c-05ee-3611-a420-681df6678b5e | -14.57207 | -48.77078 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2841dda-d4e8-3364-bf7e-5fb013ddae0d | -17.33775 | -46.70116 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5540442a-9fa2-39e3-a53a-5eb77997464c | -19.48542 | -44.30083 | 2025-09-11 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75aaac00-931f-33f7-b4a0-c8ee3067ef26 | -13.86012 | -47.36392 | 2025-09-11 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f24238c6-5422-3db7-a5a0-d8a0a9b8d2e0 | -20.15797 | -41.03847 | 2025-09-11 03:57:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| ee7d3758-872e-3cac-a6e4-77e9b2a88926 | -20.70341 | -46.08021 | 2025-09-11 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 783e473f-c53b-367b-b299-c69b8171e318 | -16.62312 | -51.82229 | 2025-09-11 03:57:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 399e4656-2187-32c3-9784-494fd5e682f0 | -18.5574 | -46.56036 | 2025-09-11 03:57:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74af70a7-9d88-38de-afeb-f994f93ed25f | -17.31857 | -46.75781 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7324c69-dfae-3541-8dd4-ec4eac0325b1 | -19.64692 | -45.0472 | 2025-09-11 03:57:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c85f5d30-0b70-3602-aaa9-4ff58a4f5eaf | -19.03472 | -42.15081 | 2025-09-11 03:57:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 29ffbcc6-15d5-379a-8857-c4ba67edae24 | -18.28964 | -47.67479 | 2025-09-11 03:57:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9dcb14cd-ec5c-3991-9516-aadf92410d74 | -17.50503 | -43.75397 | 2025-09-11 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0314c98-a186-3640-9b4a-0cbe963c30e4 | -20.0875 | -44.47885 | 2025-09-11 03:57:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d5d1663c-2dca-36bc-9d61-0983dd5bb598 | -18.84348 | -46.87198 | 2025-09-11 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49ccc312-b510-3e80-bcf6-a663605e1b8e | -20.091 | -44.47953 | 2025-09-11 03:57:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3862cb06-4dda-3af5-8129-81024109d4b3 | -19.98078 | -47.63017 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 44624b47-ec66-3337-ba6d-ac36ebe5068f | -16.28066 | -45.68246 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5bd0f0c5-8e42-3d50-989f-dae8146088ec | -14.36804 | -47.30148 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd3c0ef4-ce56-379a-917f-31e48343ade4 | -16.26603 | -46.78135 | 2025-09-11 03:57:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4651dbdb-1715-33a4-9fbd-c5745cca6f6c | -16.30192 | -50.06396 | 2025-09-11 03:57:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dd7281f1-059b-330a-9f82-5d12516f53c2 | -13.58485 | -47.69723 | 2025-09-11 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1174ac47-42d4-303e-bee9-fb01b06d4873 | -15.15979 | -52.41698 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72a996e6-4c27-347b-8340-631b649d6df9 | -15.1433 | -52.40388 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ee38e0da-227b-37c0-afd5-07ff8fb7de5c | -16.29247 | -45.68468 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41f1a5d4-f1bb-371f-9ca4-47012b73786f | -14.39152 | -47.30828 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f645e9a2-69ce-3736-b4ed-52a5ffaef137 | -17.55248 | -44.53986 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0ba37b8-6cb3-3eb3-b59a-48d90c21cf9a | -13.65782 | -45.72431 | 2025-09-11 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e60dff91-87e3-33e8-9815-b3a2435fdcde | -19.71967 | -43.92831 | 2025-09-11 03:57:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddf95a9e-8baa-37a5-8ac2-e729fda2f94a | -19.99135 | -47.62026 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6db068f8-bf3f-36f9-b07c-cdd81abb03c5 | -18.59468 | -43.87427 | 2025-09-11 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e1bd129-4571-3c58-ad08-47bf8b681e97 | -14.71826 | -45.33969 | 2025-09-11 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c806c90-09a8-36b7-8564-62f16161284f | -19.42011 | -43.13171 | 2025-09-11 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7e152036-0fa3-3b34-b6bc-f71ec243c570 | -13.66975 | -44.22166 | 2025-09-11 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9b2b6aa2-228e-3d80-95e7-b9893a227a33 | -15.25457 | -44.03613 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ccacd60b-2766-30c0-93aa-ce18c07e731d | -19.10941 | -43.22151 | 2025-09-11 03:57:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a5689619-0225-3ac3-9a09-c178aeaf5028 | -14.14142 | -45.40523 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5d6cdda-54fe-3ffe-ac18-5404d58dd9a3 | -13.65714 | -45.72816 | 2025-09-11 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d261df7-e1b4-3fcb-81ce-e78af5b93069 | -14.40366 | -47.31829 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6ed8b2f6-4c22-309e-9b8c-efe29805a835 | -19.20442 | -47.98499 | 2025-09-11 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b73071b1-8877-31f8-9ec5-52e6abd27764 | -15.13439 | -52.44581 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3c0c591f-c8f5-31e6-80ba-23c42a5eddac | -20.0005 | -47.61768 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fce0b6ab-b9a0-3580-a8e2-641fa6765575 | -19.39884 | -43.28126 | 2025-09-11 03:57:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2d9adb62-f1b6-35b8-bb71-09cabb023bbf | -19.95347 | -49.27528 | 2025-09-11 03:57:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 218fa6b0-3bbb-3cb8-b6a7-bff92dc4d9f4 | -16.62988 | -49.76618 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 006c4ed8-26d9-3575-b042-50417a530f87 | -13.97917 | -46.64771 | 2025-09-11 03:57:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4bd2c07-c282-3e3c-badb-0ad6dd1ac8a5 | -17.95796 | -44.48261 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e35a0e19-71ff-3cc1-9190-73f778948cb9 | -20.15853 | -41.03484 | 2025-09-11 03:57:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| df21d7eb-343e-3803-bec8-f506bb98c867 | -17.5569 | -44.53598 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a242f76-6486-3fe7-9302-33071f58f506 | -16.61132 | -49.77931 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86f1c427-5f44-3d8c-bac0-e64a37aa41fa | -12.9865 | -46.73895 | 2025-09-11 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fd7bcb6-528b-3b46-a0d9-bfe3c20e6272 | -14.14205 | -45.40165 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f01d6ff-5ad7-34ac-86e5-056e93df7776 | -20.24666 | -43.57656 | 2025-09-11 03:57:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a544097f-96fd-3f96-9a5e-5c086ab8e453 | -16.60681 | -49.77547 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcdd958c-99d6-3f51-bd3d-5d8f5a849f03 | -15.12323 | -52.40767 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a136a42-338d-3af9-9ffa-fc3e1cd9e234 | -13.65042 | -44.19905 | 2025-09-11 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1274b1c2-9555-3c5a-89ec-0a9fd47ed9df | -20.54977 | -47.62766 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cab519eb-1fea-33ce-addf-dd538421ed66 | -20.00265 | -47.60653 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 346d03db-37dd-38fc-81eb-6b6ec078a0a9 | -19.00747 | -46.25031 | 2025-09-11 03:57:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 98099517-1693-3afa-9abd-c42c4c9d7478 | -12.39384 | -54.16358 | 2025-09-11 03:57:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f58930c8-6e52-3e7b-bf0d-b3a677d93217 | -15.86907 | -54.93455 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8261f622-9c68-3da7-bd71-35222f7a0f71 | -18.91533 | -41.11784 | 2025-09-11 03:57:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c179fffc-8bde-3f68-8523-7fa579db84a3 | -15.14849 | -52.40969 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7d66ada-3001-37f1-9ed8-abc39295bfcb | -20.16536 | -44.61829 | 2025-09-11 03:57:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e4daae6-70e3-3fe7-b1e8-92757ec698e9 | -19.71057 | -44.23545 | 2025-09-11 03:57:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e288b46-6f65-3abc-9f85-88048073cd2d | -15.48367 | -49.35863 | 2025-09-11 03:57:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e123ad8-f297-3a62-b6e7-cd7c15069dc8 | -19.23897 | -47.99975 | 2025-09-11 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| dc124de2-f142-3b70-bad8-8547fe94a713 | -17.68629 | -44.20518 | 2025-09-11 03:57:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bee77a9b-d2c9-393a-bb73-e50a5d4be30b | -17.73377 | -44.45237 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 89775f4c-afc2-3637-9f01-df937755ad0d | -18.01326 | -47.1278 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README36.md)
