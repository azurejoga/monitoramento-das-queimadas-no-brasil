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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3de5bd58-b89d-31e5-96a0-c454bd6717c8 | -10.99494 | -45.12767 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c897e5de-759b-3095-9317-7e097a05e6c5 | -14.30383 | -45.88004 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abbd2fd1-b22f-34c8-850b-548f6de449c4 | -13.96503 | -48.11991 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d42a9bc-d8f1-36b8-ab1e-76f013aa7097 | -11.34998 | -44.96766 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a36a4bae-3bef-3539-8384-5f52e10f66e1 | -12.60708 | -46.99924 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4674a68c-b573-3ef2-b7be-5158dad2aedb | -11.76611 | -46.82784 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d858600-f379-39f7-86cf-fa427ab912da | -11.9094 | -46.26972 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e79cb434-3494-3f18-b246-462e2df8f063 | -12.65202 | -46.87284 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ceaa6429-179b-3fd7-968e-178992091598 | -12.80556 | -46.85857 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb2c801d-e913-383a-8605-8aed14bb3271 | -11.12123 | -43.38807 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| df45633d-9faf-3246-b5f6-c78a977094d4 | -11.55593 | -46.99749 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 945a92d1-f76a-3c6f-ae6a-6628e03bb845 | -14.57806 | -48.34191 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cb0c5b9-c8c0-3a9d-84af-b9848fa87326 | -14.41964 | -46.09539 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 104aeb7a-ae91-3f4d-9175-3b8417bcec9d | -9.91945 | -43.72709 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d340108-37d7-308d-a049-f901b2d2d1a6 | -13.92066 | -48.07074 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7889babf-ecd7-3167-9ac3-7775771aaefc | -9.31609 | -45.96895 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ae9b5eb-e12e-330e-a3b9-d4ff29280773 | -9.87279 | -47.8111 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ae24dd9-76d5-3820-888a-7b97db6f5c8e | -11.67647 | -44.273 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c48a7cb-767d-34f9-a1bf-bd709e419dba | -13.2626 | -47.25546 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7320ea0e-63f6-3eca-877b-c0d98a0bf5d8 | -13.15234 | -47.8286 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56453004-000b-3bea-9c63-58bdbb0ebd2c | -13.00771 | -42.6712 | 2025-10-03 04:12:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0f0456f4-258f-3764-8d5c-561ea2ca01c9 | -9.44135 | -47.36876 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dda7a0fa-704c-3a40-90fd-a39afaaac0a2 | -12.71302 | -48.57412 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dde41e4f-c4d5-3371-a701-c5fbfb216369 | -10.85274 | -47.21959 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8951098-d270-3fb6-88a7-fb3927ef2a60 | -11.68576 | -47.50536 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb374c39-98b0-32b5-af84-3fda30f2fbb5 | -14.28589 | -45.92209 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce8310c5-e9a5-3b09-adb3-d1b967af1cbd | -13.78601 | -50.7884 | 2025-10-03 04:12:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adce79c7-b8fa-3fa7-bfd7-d29dfc0dc2e7 | -9.65175 | -48.20966 | 2025-10-03 04:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 72d02ff8-0ece-36b7-9740-5a9644e4afd9 | -14.24326 | -44.28007 | 2025-10-03 04:12:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e60e88c-b73b-3572-81ed-83fe5776f0c9 | -11.8714 | -45.00133 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ce5bc31-7d99-33bb-a3ca-08e0c703230d | -14.00757 | -44.97271 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e44a95b-a77b-3a02-9ddc-15cc09c3a5be | -11.90367 | -46.31031 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c54626c2-d403-3a38-8727-09aa0476da30 | -13.13142 | -47.88547 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ef3aa70f-63c1-395b-87b7-50865800d967 | -13.85969 | -47.94191 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d9afda3f-e8ba-3c2f-b109-7f452ea5fdbd | -10.81558 | -47.96615 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e53b716-0c76-3c6b-b303-c4119e56d557 | -14.38221 | -45.95143 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 335a2bc5-5c35-30a1-b6d9-9a623204b820 | -12.61815 | -46.95746 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad5a7bda-87bc-3f70-8790-244fbaa69ab9 | -13.96766 | -48.17534 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3339789e-5f4e-34ea-a043-b977fb3f5970 | -14.59774 | -48.24204 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8066762a-65c4-39d7-9daa-e07a5cbb0aac | -11.12457 | -43.38864 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b2427ae-04a7-3e30-b080-87669ccf2978 | -10.00736 | -50.23562 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e2ae4065-c6ee-3fdc-8443-41829ca0a815 | -13.48426 | -47.25099 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 471b5a24-3191-3b01-8761-ac81a99bede3 | -13.93375 | -48.08895 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f19e5255-4303-3ecb-9e62-9632f67cd20b | -12.90137 | -46.91005 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91eaec72-4096-3c6f-8337-99436c427f0f | -11.79887 | -47.93546 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bae6a64-aac9-3538-8b71-74f54065dc88 | -13.35001 | -47.32891 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f108ed5-60c8-3524-b151-3cda036f4924 | -13.76789 | -47.55199 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 07ee81a9-bbfd-35d7-b79c-830520aefd76 | -13.97586 | -48.16301 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f3268998-d3bb-3445-a8a8-65ef97033fb5 | -13.1425 | -47.89207 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33c33f7e-1888-3161-b073-d9e0f6bb3d97 | -13.51968 | -47.27185 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 056e4d61-f2b7-3e6e-9065-3e14ca324dbf | -11.81226 | -45.03499 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3980c170-3017-36c0-915e-835312d8ec68 | -13.20077 | -47.83037 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd13c610-4f1a-3f8a-86a0-bf219ecfa49f | -10.9261 | -46.74291 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b88a170c-7c63-3636-ba5c-55c422bc72d4 | -11.83611 | -44.99904 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0406d42d-21b1-3666-84b3-4af5fcef1d8e | -13.65743 | -47.30398 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a37e33af-08c3-33cd-baa6-8b932f505188 | -11.58753 | -47.66971 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e76d90e1-8e92-3419-9ffb-fb4cbc125c77 | -10.92912 | -46.7483 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62fbc8be-45fb-3d67-951b-9700ab1ac9ab | -11.78119 | -46.83098 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39fbf6c0-3b66-3ee0-a1f3-56bfd3e0c375 | -13.5321 | -47.29042 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efc1c9e1-8a7c-3ce5-b838-28556d515380 | -11.68207 | -44.28152 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 184639ac-082e-3503-83d0-8ba8e85f6328 | -10.92852 | -46.72868 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 4ff9fd2d-d329-3c94-964a-c687a58ec262 | -13.26163 | -47.26093 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 513e539d-e115-3aa4-bed1-733d2ca5349c | -13.15297 | -47.83164 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc14cb17-eb6c-3eb1-8625-c9cb8d78a2d1 | -11.59099 | -47.62683 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5faa474e-e982-3c28-9304-fb59e3a0f489 | -13.95662 | -48.09805 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ec0a497-9503-3597-a704-bf028e769a46 | -10.00471 | -48.27178 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9791fb2-f9d8-3ae7-98ba-f7bd69f08099 | -12.80611 | -47.01146 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb4b5e1a-7339-33f9-9eda-71fec764efff | -9.48232 | -47.86922 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6ff4c2d-95a3-3ac5-ad37-acb5b702f150 | -11.14622 | -43.40339 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7436d931-48e6-3210-85a8-403ac1acd80c | -11.68478 | -47.50251 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5010656-2107-3ca3-9ba3-219340dd3ab4 | -11.90552 | -46.31405 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4782c34-7b31-3377-a072-ce82ad6b16bd | -9.91887 | -43.73074 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab474cca-d896-34d6-9131-5c9462646b3a | -11.4662 | -45.03353 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2753763d-ffe0-3992-8091-e39c4acba19b | -13.57702 | -47.58492 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 74a6f3a3-47b2-362b-a2b3-dff6865afc57 | -14.79408 | -42.83016 | 2025-10-03 04:12:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5556117-e623-396f-9df8-7684a7fccdd8 | -14.32689 | -45.87165 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 987c0201-aa7d-33a4-8e2a-b8ddc96b1867 | -13.55219 | -47.59031 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47b7aa83-9026-3845-8935-b14807683b7f | -13.1577 | -47.82782 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3653749d-8a4a-3ba5-a38d-b60175dc0b3d | -14.46625 | -48.39924 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e73eb0f4-653d-31fb-87af-89c1a89f5cfe | -10.91539 | -47.04025 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 23cf99d0-47cd-38e7-b38c-b372917954eb | -12.83621 | -46.9495 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acb13891-f924-3e9a-82b3-2a97e02aee56 | -11.84731 | -44.95303 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8f80d83-14ae-38dc-979d-c0aa6d18c014 | -11.82313 | -44.90589 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bd53f57-0150-36b8-809d-9275026fa5c4 | -12.69619 | -48.54874 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d6bd9db-6c7b-3274-98e1-ae5fea1ca4b0 | -8.90178 | -46.60454 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 963f8fd0-7d8e-3d08-83dd-671b353fefae | -12.3723 | -46.51823 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38e338fa-77bf-3653-8254-10b3df74e9dc | -14.69838 | -43.88707 | 2025-10-03 04:12:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 09886401-e517-3aa2-91ec-ab47a67d6c4d | -11.90294 | -46.31467 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 047cee08-a9bd-3c3b-bfcf-de5a579ae5a9 | -10.92232 | -47.04884 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa4cf206-59d8-3c97-9048-5b432e4e2c76 | -14.68916 | -45.18435 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37adb2fa-8e54-3cab-8c6f-d3a236323e99 | -11.21751 | -49.95819 | 2025-10-03 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddfd4bbb-6e86-33ab-bdf7-686ab00bf8a5 | -11.87706 | -45.01029 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f34a764-f3dc-3e69-9e9b-13257ffaa315 | -13.15638 | -47.89681 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a442eb46-2ad0-32ff-85f9-c0cadb7c1d46 | -12.7803 | -44.91541 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b4e4d1a-a33d-33cd-a374-4b8092c3b89e | -12.61465 | -47.00056 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 09b2abde-c28c-3d31-950e-d13e8ba17873 | -13.47969 | -47.25473 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10f3bcbd-23f7-3b48-9376-4fe4347bf268 | -11.88209 | -45.02307 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6998e039-e4ca-3735-8af1-1f0b6118b79e | -11.14009 | -47.20362 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e6bad2e-5d9f-3d60-bc41-42f71dd82f28 | -13.22851 | -47.35874 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 143b6127-fe99-3d4c-bc73-95a45682eb63 | -10.94099 | -46.49564 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README71.md)
