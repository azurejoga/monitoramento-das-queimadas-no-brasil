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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f922edf4-6e5d-3be5-b9d1-6894cfdcd0f6 | -13.56025 | -42.56189 | 2025-09-23 03:32:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d1e8edf5-5d15-37e4-b70a-d3dbfc91a3a4 | -11.45591 | -43.53333 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 211de74e-300f-3dfb-8613-1c2e496b46d2 | -11.41498 | -44.93622 | 2025-09-23 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c6b2137d-4a80-30fd-b511-533446369579 | -9.99845 | -46.28601 | 2025-09-23 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 668d4d21-06a5-39b8-a9d8-2103344d89e1 | -16.6163 | -40.57959 | 2025-09-23 03:32:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b8b662c1-d376-3d43-98e9-5a5d3e3ef5cd | -14.55955 | -42.48777 | 2025-09-23 03:32:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 598fa549-1d8b-3e27-ad95-45904c3a4ced | -15.59422 | -42.39162 | 2025-09-23 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 71897d74-b33f-3af5-a817-7ebe98956a9e | -11.20945 | -46.16586 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc24b27e-4b67-30b9-af64-bb7323232f39 | -10.96473 | -45.70731 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50382c49-da87-34c6-a940-f3ac040e15bc | -11.53083 | -43.615 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c25815d6-b272-369e-948e-0efd299596f6 | -16.84175 | -40.74775 | 2025-09-23 03:32:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 02451698-527b-34cd-9bfd-a2bb0a5ab3b4 | -11.21329 | -46.16711 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f6231b37-8184-3043-a2c7-275f28a3682e | -11.93075 | -38.33405 | 2025-09-23 03:32:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 49ceda31-f998-3644-a24f-588025889f0e | -10.95842 | -45.70391 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7437541b-2ed8-3c82-85d4-0c20bcd347a2 | -11.40683 | -44.94506 | 2025-09-23 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ba110a76-d35b-317d-8323-874f1b77b941 | -11.41186 | -44.95191 | 2025-09-23 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0210f777-b4e5-3939-93c3-4af66105a30a | -11.50075 | -43.55946 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 875cab21-6ce9-3af1-9d7c-1d9d624be35d | -11.4406 | -43.52192 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 349ae3d6-d43a-3969-9373-39ed6df2b4ec | -11.44621 | -43.52313 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7697191-2b56-3fe2-a2e8-fa813c18e5ce | -13.42422 | -47.55264 | 2025-09-23 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f60b90b0-9275-3fc3-b055-31537b037247 | -11.52701 | -43.63449 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fadd952-1bf4-39c1-b89e-ae99c6803f0d | -11.44697 | -43.51925 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6a08332-5bac-3c9d-9a2a-8cd12fa34fd3 | -15.58014 | -42.412 | 2025-09-23 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 19c45530-93b1-3119-934c-7895235db3f1 | -14.69077 | -42.50512 | 2025-09-23 03:32:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9fb4fd3b-1098-3ee0-9087-2085003686a1 | -11.40576 | -44.9504 | 2025-09-23 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a17ee1e3-febd-3a75-b748-f25591b0d286 | -10.30454 | -45.23415 | 2025-09-23 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ba55e5fd-4abd-3d48-b15b-039d3b51f7c2 | -11.21442 | -46.16164 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64c2247c-8e7a-3a70-b7e7-bb2548e2efd1 | -10.96408 | -45.70917 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee2c3af6-593a-3bdb-ab2f-bca50c2fc11e | -11.02803 | -45.88941 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a3195a2-b0be-304b-965f-15f07996a86e | -11.93137 | -38.33055 | 2025-09-23 03:32:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 12a86047-1a7b-34a6-b7bb-34ad6f5656c9 | -11.40784 | -44.93999 | 2025-09-23 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 49dd60fd-c766-3b77-ba09-53aea6e20352 | -13.80923 | -41.82427 | 2025-09-23 03:32:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 36f4f045-0184-39e8-a0a8-1e27b40917e6 | -11.89069 | -41.27215 | 2025-09-23 03:32:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| fe2a239a-6d03-3582-8efe-6f62c575d5ee | -11.82473 | -43.16128 | 2025-09-23 03:32:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cc47538b-eb77-36a3-8d4c-404ec1e8e85b | -11.49804 | -43.55748 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6456d250-afae-355e-9e0a-a04dcff15383 | -11.43498 | -43.5208 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d8fe034-a19e-3ca2-bc04-7465297ec91e | -11.21056 | -46.16033 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3e23cbb-0ef8-3475-b312-0b4726281908 | -13.41654 | -47.55792 | 2025-09-23 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e4b161c-9301-30e7-b524-92a5897ecdab | -11.52295 | -43.24643 | 2025-09-23 03:32:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cc0a34dc-add2-31d7-a49a-e827a3d6436e | -11.66791 | -44.35841 | 2025-09-23 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8eacedc4-69cc-3408-904a-870098c15fd9 | -11.21606 | -46.16729 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d040dca-6c50-3d1f-9b47-e11a357ff359 | -9.99718 | -46.29221 | 2025-09-23 03:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02583437-0580-332e-bfae-786cf475ee96 | -13.42575 | -47.54564 | 2025-09-23 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9281cfa3-eaef-3117-b86f-288979aeabfd | -14.62914 | -42.52908 | 2025-09-23 03:32:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 99621f2e-f5da-36a1-9ee3-274a450640b4 | -14.95881 | -40.89906 | 2025-09-23 03:32:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c5d38ead-f2e1-33bf-99f1-db385ef50726 | -16.84255 | -40.74357 | 2025-09-23 03:32:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cf0e9da8-e044-36f9-844d-ae13118ae388 | -24.20716 | -50.4211 | 2025-09-23 03:36:00 | NOAA-21 | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a144c495-603a-3d3c-8db2-0fc7a0306d0d | -24.20504 | -50.41827 | 2025-09-23 03:36:00 | NOAA-21 | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 9db99fbe-eb65-320e-a5f2-d1fa3102caa5 | -6.3412 | -56.2009 | 2025-09-23 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 934474d6-9f10-3912-b5ab-520bb122b959 | -12.7378 | -57.8632 | 2025-09-23 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a9f62296-2b53-3949-b382-84d38c400dae | -6.3412 | -56.2009 | 2025-09-23 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 72330188-eba6-3b73-b73e-846650dc2e8a | -12.7375 | -57.8831 | 2025-09-23 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 6e321a4c-4524-3f4d-bd46-6289e50500d2 | -3.81039 | -41.56183 | 2025-09-23 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| f1065f63-3f3c-3479-a4f3-67d7358f328c | -4.01065 | -43.27161 | 2025-09-23 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 08f7d78e-a760-3f40-9b2c-51a6e51947f0 | -2.25315 | -47.88152 | 2025-09-23 03:55:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 53c88708-62d7-36dd-802b-f71dad16f386 | -2.37945 | -47.72478 | 2025-09-23 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39eb5f21-49c9-34bf-8ebe-f6c002999879 | -4.01126 | -43.26784 | 2025-09-23 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f9b1463d-46e0-33e7-9d7f-417c1d74a746 | -4.7863 | -37.72816 | 2025-09-23 03:55:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c80549c-efa4-3650-8063-66f92509d325 | -4.62315 | -38.69495 | 2025-09-23 03:55:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0b177c62-5efa-35ba-9645-9d8f7c4f1630 | -3.85644 | -40.33892 | 2025-09-23 03:55:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4e7d1aee-e40e-3f52-9ab1-eaea49bf76a3 | -3.65585 | -40.35274 | 2025-09-23 03:55:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e1a2ad34-f246-322c-83bd-9ee7e14603f0 | -4.30804 | -41.85121 | 2025-09-23 03:55:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 99d058f5-a234-36bb-b618-6401773ba065 | -5.16223 | -36.89654 | 2025-09-23 03:55:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1b68dcce-5005-37f5-b3a0-20931c9e21fa | -4.55598 | -38.02546 | 2025-09-23 03:55:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 78b9387d-8562-31ae-94dc-5343001beddd | -2.78846 | -49.58263 | 2025-09-23 03:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7adcf2a0-a3b7-3aa9-ace7-9c4000f68e01 | -4.01191 | -43.27121 | 2025-09-23 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ece45f8-d0e7-3578-81f7-eb7a8795f0ba | -3.85997 | -40.33949 | 2025-09-23 03:55:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d7510b5-4d13-3d41-a433-b7658533b95e | -3.46357 | -43.18879 | 2025-09-23 03:55:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21cbdc75-5dbe-37df-951e-f7d8e4766869 | -3.8116 | -40.95603 | 2025-09-23 03:55:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3cfd1215-6b36-317a-8b10-6677ee17c66e | -4.01255 | -43.26745 | 2025-09-23 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e142eeb5-85a4-37e3-9690-d5df732d05ab | -2.91062 | -40.38831 | 2025-09-23 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0067eccf-6095-3492-82a5-6696a5cadcb7 | -4.40795 | -42.15171 | 2025-09-23 03:55:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3649dd5e-3719-35cd-ba5d-b41b963cec8e | -2.38011 | -47.72077 | 2025-09-23 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ae58d35-da0b-3c6c-81f8-dd2cb499a366 | -3.06319 | -46.30854 | 2025-09-23 03:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1a5e221-2d78-3162-a54a-99a4fc043a31 | -2.25247 | -47.88562 | 2025-09-23 03:55:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dcd8e43d-9546-3ea6-a142-71b317cf4830 | -3.05746 | -46.31083 | 2025-09-23 03:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c32046f3-e755-3504-b852-53de8469cede | -3.06266 | -46.31174 | 2025-09-23 03:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c86042bb-ab47-338b-8cc8-afcbd03d366c | -3.85292 | -40.33834 | 2025-09-23 03:55:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 16b5c5a0-4a06-3ccf-bd97-d4c89c52b4e2 | -2.78199 | -49.58157 | 2025-09-23 03:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1b63399-023b-365b-9ea0-79dc1cc45806 | -4.76266 | -43.63514 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16ef11f4-9675-3de0-84d9-e5c23dc27053 | -11.60494 | -45.02788 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e481c54d-bdf3-3720-8d83-f386e74b700f | -11.81856 | -43.16228 | 2025-09-23 03:57:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9d16680-2d0d-3af4-891e-2ad37a101bb9 | -7.88796 | -44.01891 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 05fc8224-d0b3-382a-a688-d113a2eca150 | -7.88604 | -44.0299 | 2025-09-23 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 78795724-55a8-351b-b0d9-cf367668b431 | -5.23607 | -43.6983 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cec21d9-f1e3-3fbd-9742-14657103efaf | -9.18794 | -44.62519 | 2025-09-23 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c41f94ff-2dc9-3bac-aabd-2c5305db85d7 | -4.07088 | -48.0438 | 2025-09-23 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db2693d4-b31e-3d9b-a29c-eee6239e1991 | -4.4928 | -48.11839 | 2025-09-23 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee5dba12-b2cb-314a-805f-a9d1cc4b0665 | -11.48074 | -43.53654 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d677b159-d1a7-39c0-85b2-98201f0932ba | -5.1026 | -43.16564 | 2025-09-23 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b895306-6fc3-3253-8e44-bf8461a909d4 | -6.61356 | -44.61102 | 2025-09-23 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32aa4afb-5728-3e51-b099-9bb40fac9efb | -8.00264 | -45.71572 | 2025-09-23 03:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a58e074-52ed-3901-b74e-930dd9281fe0 | -6.89323 | -44.76621 | 2025-09-23 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b963295f-b402-3204-8885-a4f580210bdd | -11.89644 | -41.27163 | 2025-09-23 03:57:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d6c385f2-5d1f-3a47-8066-b00c560ec8b5 | -5.87169 | -47.20896 | 2025-09-23 03:57:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcb0f8fe-6978-3bfd-a3ee-db609c229f43 | -11.40803 | -44.94073 | 2025-09-23 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5356c368-fd0b-3f80-b9e6-de6fb659d1ee | -11.5254 | -43.63392 | 2025-09-23 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13b761ac-97b2-37e8-abea-7ba6491e18de | -11.02146 | -45.88544 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 143034cb-76cc-35ae-86e0-f8c87b1ec1ac | -11.21477 | -46.16222 | 2025-09-23 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fe985cc-03c3-3d07-b148-f6cc7a66ea2d | -8.13767 | -44.47194 | 2025-09-23 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README7.md)
