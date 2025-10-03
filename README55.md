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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1e4054c-8c57-3bed-9eba-577cf9b7c255 | -11.45263 | -45.13559 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05c3adb3-575e-32d6-a312-65a8de04a878 | -11.01322 | -46.54897 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 995c22e0-ef5f-3bdd-b348-3a8eb042e857 | -11.80356 | -47.93254 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6d7758e-785d-331a-991d-aacaae8d396f | -13.96056 | -48.09886 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 962da88c-6f85-3510-9f29-ef01bfc7add4 | -13.08572 | -47.07352 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b6931a1-ebc6-3aa4-a155-5952b9722631 | -11.66968 | -44.27186 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ece678f-3417-3408-9e53-2de119d98586 | -10.9355 | -51.06738 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 040dedbf-df6b-33f8-a959-5d5d9d27e8ad | -14.64024 | -44.73693 | 2025-10-03 04:12:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b8dbf69-bebf-30cd-ac36-f803ad4c8391 | -12.61842 | -47.00126 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 622c2c0e-6813-3fe6-87bf-15937fea662a | -9.34374 | -45.75838 | 2025-10-03 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e45c69bc-5435-3451-aa9d-feb2d5073cdb | -13.28666 | -46.98468 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d883331e-ad86-3d4d-9931-490410862a40 | -13.96996 | -48.17297 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 46d3f035-0d7e-3b0f-803b-51962813d8bc | -9.34447 | -45.75397 | 2025-10-03 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af1a2809-b672-3b6a-be57-13b8af7901a9 | -13.67791 | -48.63332 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00d9120d-7681-3bde-8b6c-2411de50e63c | -13.19711 | -47.80525 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04b34db3-74fe-37d4-a518-f168657283e4 | -13.97882 | -48.16932 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dcf19518-0d8f-3318-b0ac-e2816614843d | -13.3438 | -48.08381 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf5725b8-ee88-3263-b7df-f92eaff5fbe4 | -12.60627 | -47.00395 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b6c350f-4578-3e6a-97ff-8f2270c35677 | -9.9071 | -43.71759 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 25bcbcf1-29fd-30a8-895a-d6d98bf0f98f | -11.6213 | -45.03121 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f68782ff-1df6-37d9-8282-18db50a13115 | -11.1468 | -43.39983 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cbd569eb-0495-389d-92e4-6fb42baa1b2c | -12.89077 | -43.13208 | 2025-10-03 04:12:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9f1a80d4-56cc-324c-a7a8-c37953814992 | -11.30644 | -42.79814 | 2025-10-03 04:12:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 909d7759-9846-3f86-b81a-197bd5e9e16d | -15.08423 | -42.12072 | 2025-10-03 04:12:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4408252a-e03a-3213-a16e-bda4813e2c79 | -11.91811 | -46.263 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d63defee-97ae-34b0-bb26-a8a5116957b1 | -14.44409 | -46.37482 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdcf9dbb-f599-3dab-b1bb-945290360bfe | -12.49998 | -48.00003 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56991d53-53f0-3c0c-a1c4-19590805ddad | -10.06311 | -48.18727 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c297636-eac2-36cf-9c46-78a75edffc92 | -10.84488 | -47.21819 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6c94bf5-0477-335f-8ca4-705c0ff3f81a | -12.95714 | -47.16444 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 819bf858-d7ac-3d79-bbdd-d40c24436f2c | -13.19878 | -47.79584 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 053e2a78-8d9b-30b4-ac4b-15e2f8a9bf34 | -11.90186 | -46.31329 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 33de5351-e0d3-3426-8b18-dd852f2b2962 | -13.12654 | -47.89011 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f93c371-caa0-3c1b-863f-9d7e2394fe9d | -10.41156 | -54.4094 | 2025-10-03 04:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 595e3ac6-a160-3bc3-9a33-d17bd7438201 | -12.75827 | -50.55444 | 2025-10-03 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16487c1b-37fa-3839-8794-0d55360e970e | -10.98391 | -46.67306 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bec6714-3aa3-3f66-9fc4-74b7d78841d0 | -12.53619 | -43.19016 | 2025-10-03 04:12:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9b838b7-af28-30c6-b093-701d74ca5f2d | -12.80479 | -46.86295 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9e444ac-eef4-3ad9-a611-f2946ecf8987 | -10.00832 | -50.24611 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 4a1cc651-ad38-35c4-8c3b-e7f479b01e9e | -11.34588 | -44.97083 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1659b09-d95d-3476-9cf3-baa163f63d9c | -11.59246 | -47.66512 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0aafe269-ba5e-35d7-8e86-f945bb8a49c5 | -13.39824 | -47.55003 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e3bf9138-6e84-3306-8028-916d7540288c | -13.21595 | -50.89244 | 2025-10-03 04:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 61f75f6b-b15c-3e7b-a8fe-7c89e7f25634 | -13.20268 | -47.79673 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e108363-341e-321a-af39-ebaf071996eb | -11.8379 | -45.03124 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a0c3649-fd41-3511-beea-3f8d87d8d55b | -13.30601 | -47.59639 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 683e7599-105a-3157-a808-f5aeddb7ea1a | -14.59625 | -46.70967 | 2025-10-03 04:12:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5036ad99-32c9-365f-bf70-a3e7436c43c2 | -11.30815 | -47.83939 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 43e3149c-2f5e-3a46-bc39-103a0efb464b | -13.96656 | -48.15807 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8493b17-9c99-302c-9c67-940db74e6159 | -13.34919 | -47.33355 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e86343b4-5090-3ebd-b047-c15963389351 | -12.60329 | -46.99859 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3a4db265-2c55-36d5-965e-4e6b7ec00b6c | -11.55512 | -47.00222 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39d75f2d-b355-31ae-aa23-1190c60e198d | -13.53191 | -47.2465 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eef18c13-af74-3e2e-8c57-02e6b106744c | -14.19712 | -46.0656 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 7097e01a-7cbe-3787-a055-74b498dac179 | -12.3686 | -46.51762 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8091dbab-b565-38ca-8b95-7e9496e52867 | -10.9731 | -51.09011 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a690e758-a915-3447-9703-e927535fb2a3 | -12.62922 | -46.9837 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 037f3618-5bd1-385d-b1cb-00ca5231f340 | -8.11733 | -49.75528 | 2025-10-03 04:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90242632-591e-35f6-9b3a-84d2c3427d27 | -10.76114 | -45.33553 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4716f38-71bb-3073-ab85-3fea7dfb4378 | -11.45679 | -45.13227 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a55e16f0-7825-3f83-9ac2-b86bc00484ca | -14.23093 | -46.11706 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abe8cabf-34fc-3f66-aae9-a7e8e6cd6f9c | -11.49298 | -45.00193 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 110fe83e-484c-32d5-88a1-01ea1a5a5dcf | -10.27732 | -48.07265 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae4c4562-d02d-3573-a175-2ded4823eff2 | -13.3424 | -43.6507 | 2025-10-03 04:12:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b187909-14c5-31b9-9446-b6e20f257be5 | -9.90313 | -43.72068 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8f12626d-2c42-3909-9262-476aea780516 | -13.35215 | -48.12923 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a490c1cf-2612-3d08-80a2-058bccd3c54d | -10.10802 | -50.3575 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 299ea6c4-eda7-3696-aa3a-a73d22124cc8 | -12.82399 | -46.90809 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1aed280d-0dc7-3013-a299-4f722564cc9e | -11.85642 | -44.96254 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5a73f1d-e7fb-3693-b49a-4d82671df3c2 | -11.80578 | -45.00971 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4e59786-0b47-3c7c-8761-8c615eaad51a | -8.08138 | -49.90101 | 2025-10-03 04:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01f019a7-1564-33fe-8ffc-851c7a8570e6 | -12.94054 | -48.44429 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afaf1ff9-0aad-346f-a076-4a0a1a4c2634 | -11.79179 | -41.19698 | 2025-10-03 04:12:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 806ca416-7ee5-3e98-ab8c-b762d86f0d7b | -12.61122 | -46.97514 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dd1bb83c-83b9-3ac4-b6e1-31a5886c0355 | -13.68104 | -48.03874 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7dd7ac0d-2ce6-3864-8a68-c7841cc4ba12 | -8.75834 | -47.32967 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9993dc3-0bf5-3c42-ab52-b58a2682b8d0 | -11.90133 | -46.27272 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfe2b4a5-9b73-3fbc-a7c8-03ddaca36e7f | -12.90285 | -46.90156 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c93b442-ba2b-39e5-9741-b048080a8f4c | -11.31617 | -53.95839 | 2025-10-03 04:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 328446e9-6f7f-30d4-bb19-68f1622c4fb2 | -12.91103 | -46.92111 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cf02617-daa3-3f75-9d1e-788721e68716 | -11.47163 | -45.02252 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bfc798e-9f43-3ddd-9998-3c6b257327af | -10.01422 | -50.22574 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fe4b5bfc-d911-3522-855c-0703dd3b0df1 | -14.15867 | -49.20327 | 2025-10-03 04:12:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 899ea13c-4108-30c4-a6c1-e997bb30ee87 | -14.22879 | -46.10823 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c42e645b-02d1-3237-a2a4-b36543e9f23d | -13.30505 | -47.60347 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b892a11-06dd-348a-9673-fb06643c366c | -12.62498 | -46.96295 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53aecca1-1795-3f8c-9b2a-d503e1786bbf | -11.64349 | -46.8669 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9a76860-c6ac-3f4e-93f0-dc50fff34831 | -11.48516 | -45.11316 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1c0aac5-3095-3523-8b35-3acacf4feaba | -14.20145 | -46.08319 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6f5e372-423b-3a0c-87fb-1c2c6864f23e | -12.62119 | -46.96237 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa1c1afb-242f-3d2c-88f5-7180aa4b6b47 | -10.8452 | -45.37954 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e1352a1-d454-393c-a7a0-d82c8e41ddfc | -11.14126 | -43.39156 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9cb5906-d495-3430-b991-0163c437fb50 | -14.40366 | -46.14726 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b8686b2-df6f-3bec-869b-f8393308a59f | -13.97788 | -48.17453 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4298280e-1f56-36d4-8122-45efc1f9876f | -14.31637 | -45.86987 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 795fb991-9632-3a08-99d1-2fd066f7ba4c | -12.39722 | -45.01247 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0ebb222-99b1-3851-9c23-edfb9bdebc72 | -11.32399 | -49.01562 | 2025-10-03 04:12:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f7f8dab-a6d0-36e9-ab70-99000f45654c | -8.75668 | -49.92149 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cab4637-dd4b-3fbf-b06f-16e25179c381 | -9.9578 | -48.77268 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7e22c166-4adc-3259-af33-6ddf9afec850 | -14.21746 | -46.0892 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README56.md)
