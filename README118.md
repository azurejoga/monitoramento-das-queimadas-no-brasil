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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92c8f3f0-27c3-3ef5-88bd-54ec2f6c8292 | -8.95409 | -45.17932 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bb03004-4be1-3493-8f9e-fbd3faf20d5a | -16.02837 | -45.13043 | 2026-10-09 04:29:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b5a50d4-0fee-3822-8aa3-b36b11da779d | -15.73354 | -50.79949 | 2026-10-09 04:29:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d62878c-6a39-359d-89cf-e7657fe16841 | -16.53578 | -52.74484 | 2026-10-09 04:29:00 | NOAA-21 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 657ef79b-6646-3aa8-8942-07bff480bc59 | -16.59061 | -46.75212 | 2026-10-09 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2f25396-5a65-32ef-aad5-86ab3ef52e86 | -15.62288 | -42.9895 | 2026-10-09 04:29:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ee5025c-0b44-34e3-896c-296b2142b0cc | -15.10737 | -43.63745 | 2026-10-09 04:29:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c820ddcd-f3d1-3f42-9c9f-ca6d2ef439a3 | -16.88291 | -40.70996 | 2026-10-09 04:29:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b546d794-00fb-3ed0-a998-f20c782a92f7 | -15.2575 | -42.37018 | 2026-10-09 04:29:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f283b623-1f84-32af-9db5-77feebf87a99 | -19.32962 | -48.73255 | 2026-10-09 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b66e0f07-8098-380e-8aae-16d65467c3b4 | -17.00562 | -41.1679 | 2026-10-09 04:29:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 4196e286-a782-3ce3-9429-3528af7b4ba2 | -17.17883 | -51.74551 | 2026-10-09 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a9c8ad6-2411-37aa-a5fe-4a4ee3bc868d | -17.02719 | -41.06285 | 2026-10-09 04:29:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ae6d60c6-c230-3d44-b012-2802e6e56cb9 | -16.9688 | -41.22731 | 2026-10-09 04:29:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 540cfc7b-30be-31ff-b2b1-0c9fa9b68aa9 | -15.25513 | -42.36755 | 2026-10-09 04:29:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 65849092-0ced-3527-be4f-25d0a72bff27 | -15.38466 | -41.88839 | 2026-10-09 04:29:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b1ece95e-42bc-3cf4-8a89-70ddcbd1bf3d | -15.44066 | -45.68522 | 2026-10-09 04:29:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8093871-50d8-359c-84fc-b3bbb01d34c8 | -14.35405 | -55.03271 | 2026-10-09 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1e0bcef-2134-3fa9-9cd8-6f35d572f4cd | -15.78434 | -44.68741 | 2026-10-09 04:29:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a92a22c-11d2-3b75-83ca-7b24c4654ce1 | -14.93075 | -48.08961 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e16e6b67-c38c-371d-8d9e-1f404ae13fcd | -14.98031 | -47.54422 | 2026-10-09 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fa473a9-4561-34de-88a1-05e8335b7a3c | -14.40384 | -55.44451 | 2026-10-09 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb07cda1-6a01-3cc0-8e1a-7429f317661e | -15.56154 | -56.40536 | 2026-10-09 04:29:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5362e6b3-1aad-35f8-b0a3-e7885169893f | -16.91566 | -40.89681 | 2026-10-09 04:29:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fefd0ecf-e128-3048-b9a8-0be12d0e5335 | -15.8103 | -47.4727 | 2026-10-09 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87f455b1-8b20-33fd-bdd8-6365979dbec8 | -14.94287 | -48.09882 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f1ce999-67be-3269-889a-b9db33e78c22 | -15.24419 | -46.94651 | 2026-10-09 04:29:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b733c7a-ec63-3fab-9012-4d2c604dc175 | -17.41191 | -52.02053 | 2026-10-09 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 76f9a75b-4c66-30b1-8292-c1ad13b2a780 | -17.00497 | -41.16734 | 2026-10-09 04:29:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 78683811-062c-3179-b51f-e492cb3d1278 | -14.87329 | -50.30151 | 2026-10-09 04:29:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 56865f77-0a62-34fc-8755-340b44af8bae | -19.05779 | -46.25696 | 2026-10-09 04:29:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d46df9bc-b834-3458-9e49-da3b8544de4a | -16.63935 | -47.21144 | 2026-10-09 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc0d6ea5-1d3f-3586-917a-655c21c4226c | -14.88134 | -50.2951 | 2026-10-09 04:29:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 446e0a1d-0370-334c-b4c6-28a4da158ea1 | -16.12585 | -43.74189 | 2026-10-09 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61145998-0f88-34db-a6f6-2ceb730351eb | -16.58948 | -46.75983 | 2026-10-09 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 239a7520-c437-33cf-8a1f-3496a838fba5 | -18.64315 | -41.34945 | 2026-10-09 04:29:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e5c36bec-3971-3186-bb7f-b8beb5fa56df | -15.95412 | -41.08443 | 2026-10-09 04:29:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 69580584-f717-31e1-8046-27a704be31b7 | -16.51479 | -52.59069 | 2026-10-09 04:29:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a4b8f55-2ccb-325d-b493-e4a290dc7eeb | -15.10411 | -43.63166 | 2026-10-09 04:29:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e8ae4fda-2d7d-3a9a-b764-3a2f96d1d211 | -14.70367 | -48.86726 | 2026-10-09 04:29:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b7cf0c2-2fbd-3143-ae49-f9f3dc227bda | -17.28625 | -41.22081 | 2026-10-09 04:29:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 26531d19-8f75-3089-a97e-dc5ee7aa9f0a | -15.11132 | -43.63802 | 2026-10-09 04:29:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0dbdb0f9-c773-33f8-ae95-9467d26f5e0e | -14.55749 | -50.03561 | 2026-10-09 04:29:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c45a277c-c09d-3abe-b108-7074cf7b84a6 | -18.47964 | -42.25071 | 2026-10-09 04:29:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| cc3a446a-2482-3bf9-98b4-1bd05de52780 | -14.94507 | -48.10646 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 410eff99-b007-34ba-8c33-57f100a345cb | -15.10274 | -43.64209 | 2026-10-09 04:29:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6b777e58-d28f-373d-ad0c-ead122adff27 | -15.94882 | -41.08874 | 2026-10-09 04:29:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cd1f4b45-5be5-3964-ba86-d597949a4dae | -16.41013 | -47.00217 | 2026-10-09 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d256b652-c778-3cce-a433-6592f252824a | -14.88072 | -50.2989 | 2026-10-09 04:29:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e426364f-5ae9-327d-9372-52689eecbbe3 | -18.4791 | -42.25547 | 2026-10-09 04:29:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5f484170-7175-3bd5-a61a-49a080004d40 | -15.09296 | -47.83126 | 2026-10-09 04:29:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8f11459-e21f-3c15-a774-c541afd2052b | -18.66644 | -44.25687 | 2026-10-09 04:29:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9c189fd-3b3c-3a55-8958-04f1448e2f35 | -14.13901 | -50.33829 | 2026-10-09 04:29:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0efe55f1-0df6-3e03-8e0e-208879da92ce | -14.9159 | -48.07628 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 732d7f6c-5f92-3306-a732-64448544e711 | -14.70754 | -48.86423 | 2026-10-09 04:29:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 077c71d1-5d97-3fa4-9d3f-01eeac0007cd | -18.18913 | -49.89532 | 2026-10-09 04:29:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c7c972e-da51-37af-92de-a566b047cfb3 | -14.92251 | -48.12104 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c950568f-c568-3fac-88e3-4bf44dbf2ac4 | -18.63292 | -41.35361 | 2026-10-09 04:29:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 6264bf86-ff9c-3bfa-8d3d-de1a0f256ff1 | -14.14243 | -50.33889 | 2026-10-09 04:29:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59eaa963-d266-390f-8b30-8726d07831af | -16.96356 | -46.355 | 2026-10-09 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 14f10edb-6f72-3337-ba4e-b69cf72de252 | -15.95208 | -41.08755 | 2026-10-09 04:29:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8d1e47f8-01bf-3da1-98ff-9d5fcc305602 | -16.63834 | -47.20824 | 2026-10-09 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a8e546d-01ef-3736-8580-f5df68ac4094 | -17.71424 | -39.74804 | 2026-10-09 04:29:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a471c0a1-16a3-3022-8242-be6cdd2b1229 | -16.9895 | -41.17526 | 2026-10-09 04:29:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 37451903-2b7d-3422-8c3b-9606b4e416e4 | -18.32897 | -42.36996 | 2026-10-09 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| 61916412-f1ab-3da8-ba09-1a2e5e299d68 | -18.05235 | -44.56032 | 2026-10-09 04:29:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3da5208-064f-3076-b414-a02a5cf84466 | -18.63831 | -41.34914 | 2026-10-09 04:29:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a8d0c790-ad4d-3e2a-9dd8-ee2769c1d05e | -14.93681 | -48.09422 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6861312-2244-36cd-9876-23afcb6b516e | -16.91366 | -43.8848 | 2026-10-09 04:29:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 229c7859-195f-3ff6-adf8-b1a6e46d05a0 | -17.88017 | -45.98528 | 2026-10-09 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63048465-9a61-3af4-9dfa-7969613624a6 | -19.32556 | -44.01781 | 2026-10-09 04:29:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9e38da96-b1bf-3208-9bcd-31dd3578ac6c | -15.98885 | -44.85502 | 2026-10-09 04:29:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fe2b4e45-50a5-3957-b486-d8672164cab4 | -15.11859 | -48.52099 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d578ad6b-880f-3638-af30-401a503c4ca4 | -18.11168 | -54.52159 | 2026-10-09 04:29:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b22920c-cc2c-316b-b101-5bf07e60793b | -15.94944 | -41.08338 | 2026-10-09 04:29:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0fbbc8f5-5fa4-3228-874d-b26f4323650a | -16.30694 | -49.44569 | 2026-10-09 04:29:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 06f44b07-5a8a-3c6e-9cb0-7f35e19aefea | -14.74044 | -48.21869 | 2026-10-09 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fc183d4-25f4-38a7-ac41-3e82cd060748 | -14.97698 | -47.54369 | 2026-10-09 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b8503c21-1cd6-3497-a915-9c0a9b8a4166 | -15.56837 | -44.51815 | 2026-10-09 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b8764dc-bb95-3a57-963b-24c7bd95c5da | -18.33283 | -42.37566 | 2026-10-09 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 0d4f8255-3244-3861-a927-ae9ae7de2e4f | -15.79435 | -50.13113 | 2026-10-09 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48bf0db8-7875-3b17-923c-38f1e73fd859 | -15.73289 | -50.80338 | 2026-10-09 04:29:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f908515-d40b-3515-a35a-c2ec598b2329 | -14.35055 | -55.03388 | 2026-10-09 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52678726-8e5f-39c0-a87f-0af41a5a35de | -16.03783 | -49.18991 | 2026-10-09 04:29:00 | NOAA-21 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c22408ea-81cf-357e-8842-c34191fae76c | -15.62239 | -42.99336 | 2026-10-09 04:29:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7881b23-ea2c-30e0-bf8e-b98cee234d75 | -18.0856 | -42.26651 | 2026-10-09 04:29:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.4 |
| 396e0da5-48e3-31c0-b3ac-c76c9460ae3e | -17.44387 | -52.00478 | 2026-10-09 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab073a7e-d49c-3c9b-b431-3ee42552b720 | -19.99636 | -49.08459 | 2026-10-09 04:29:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a2abd6c-aada-3204-a001-898556f4b8c2 | -14.87732 | -50.29831 | 2026-10-09 04:29:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a11c32a6-eacb-35ac-ad06-35a914ff6007 | -18.63351 | -41.34833 | 2026-10-09 04:29:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 524bf206-3a42-32c6-b2d5-b376b136841c | -16.99554 | -41.17137 | 2026-10-09 04:29:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 20e7dc39-73eb-3123-b640-cc50c0bee37a | -18.43398 | -50.32243 | 2026-10-09 04:29:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6def538f-cc7d-36cc-9094-4133f9ac3a77 | -18.08113 | -42.26566 | 2026-10-09 04:29:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 01d1f8a0-3c23-353c-9a2d-b37f26960f4c | -14.92746 | -48.11092 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f7aed9f-1334-3ed3-ad16-84caba961f21 | -18.1157 | -54.52238 | 2026-10-09 04:29:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72929280-d016-3b7f-89e4-5e31eb8d6716 | -14.73714 | -48.21813 | 2026-10-09 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f8a1979-e678-36c7-8c47-447ca0b92074 | -17.20723 | -40.80947 | 2026-10-09 04:29:00 | NOAA-21 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d92d5bc6-d707-3022-803b-d52b47b6c5c8 | -15.95755 | -41.08221 | 2026-10-09 04:29:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d19c86e9-0d98-3bf7-aa49-289ab6317152 | -17.36487 | -48.17722 | 2026-10-09 04:29:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c18bf774-362f-326a-adcf-bbd24849f04c | -15.78808 | -44.68797 | 2026-10-09 04:29:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README119.md)
