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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9612ec3-1034-34e1-83c1-7df671f4dbd2 | -10.88048 | -48.18528 | 2025-09-14 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60a133c4-2c66-3c8a-a6cf-6549ccfa056c | -13.91141 | -48.30674 | 2025-09-14 03:49:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acec9fa3-a329-3702-9263-01b382e60ce6 | -14.18742 | -46.16119 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3abf3560-961c-30b1-9b9d-e93d954e9135 | -12.77973 | -48.0064 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 10ecd5ae-d233-3169-85aa-e94f9f03109b | -12.77769 | -48.01885 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c66553e-79df-3a2e-a15e-f50e893013bd | -15.04551 | -50.15199 | 2025-09-14 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e5dd04e-c67e-323c-92d6-b99e0a96f50d | -15.75649 | -52.25122 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b16b9c72-9140-32d8-952e-76725f1993f4 | -14.63059 | -52.11658 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd522418-9c3a-32ea-9da8-022408091be1 | -18.01521 | -46.9543 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2870f27-5de8-3258-b3d4-f147bdc0836a | -18.00274 | -46.96858 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae090a9d-b511-3e96-a4a8-56fa580ea0f9 | -14.88078 | -44.45573 | 2025-09-14 03:49:00 | NOAA-20 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc916898-43aa-34ce-acf5-25f0d2f4d42d | -12.80757 | -47.14875 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aaad5015-fbdf-3796-a698-21d34fd8b2d9 | -12.79078 | -47.98148 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b09cafe-1f37-32ea-9c5d-cd9a243a6e4b | -6.3317 | -43.86969 | 2025-09-14 03:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 3d730a27-f81c-306b-89db-c28d877c19cf | -12.96568 | -48.04898 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2667ded6-0c2b-3385-a07a-3ef17cc962b7 | -17.59122 | -42.74216 | 2025-09-14 03:49:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f917097-2e1f-3f06-a6c6-3bbfad683fd1 | -15.19005 | -52.47579 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01039d55-562e-36b3-9c04-3266c6dbf306 | -16.83929 | -40.85424 | 2025-09-14 03:49:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dd635ddf-ad01-3740-a150-7bf3a141d57b | -16.44148 | -45.68733 | 2025-09-14 03:49:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98c63cfd-202b-3903-bcae-7e5dfacb2cd4 | -11.46583 | -50.75866 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5877afb-4250-3594-a775-fdcae91ade9e | -6.67851 | -45.51764 | 2025-09-14 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e056531c-4852-33b8-870d-c2fab5f6c447 | -15.53815 | -49.98992 | 2025-09-14 03:49:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5894c735-9fee-342f-939e-bfde21f818af | -12.13846 | -47.58651 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3137c88d-f31b-3da3-840a-6307e33e201a | -11.30119 | -50.83811 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a4e672f-eb65-3e6a-ae1c-5a744c1609a0 | -13.27505 | -43.78278 | 2025-09-14 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecefa06a-6672-3abf-92b1-7c86554149d6 | -17.97044 | -45.27304 | 2025-09-14 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f6c5e69-2780-34d1-a4c3-c185af1f7a62 | -11.40127 | -43.53147 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6be98ca-60e2-3c6c-a346-0ec27bbe7cd6 | -15.80099 | -52.20734 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ddc19e79-f082-35fd-94a0-8292d3ca24ce | -15.19322 | -50.11268 | 2025-09-14 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 221ebf3e-ddca-36e0-825d-6361634c76d3 | -11.38689 | -47.33996 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e5438b4-7114-301c-ab1f-d89a07f0ac16 | -5.9569 | -42.78313 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c2dfbd65-385d-36d3-b236-0fc5a800858f | -12.9662 | -48.01434 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 85b448cc-e662-37de-b1d2-a1e815db157f | -14.4361 | -43.19828 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 382035d1-0ab6-3d36-b077-ae1d22aaa5f7 | -11.91356 | -46.52576 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fcb1679-2629-3510-a80d-f84e01151e6d | -10.92284 | -45.57592 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 15c6d7ad-37a6-36d9-baae-aba2951e6a19 | -15.03486 | -50.1629 | 2025-09-14 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac92849f-fe55-3b7a-b4b8-d125ce3d57ab | -16.23034 | -43.1091 | 2025-09-14 03:49:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4e124c0-1eee-3917-b292-22ad8bf7fcaa | -17.95972 | -45.25464 | 2025-09-14 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c08448a2-467a-305b-b825-228b7e70d028 | -6.17968 | -41.17505 | 2025-09-14 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 418696e8-d156-39fc-b760-c671c0aaada0 | -11.3897 | -47.3385 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c34f1a9-83a3-3955-bc58-e5873c949e93 | -10.96671 | -49.56886 | 2025-09-14 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5329bbaa-4a1d-390e-a05d-39b942d65144 | -15.76327 | -52.25217 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9da80494-68be-3cfd-93e7-b0e9b7aacea3 | -12.2444 | -46.78897 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69024de1-b2f9-3837-9094-91eb7ba2cbc8 | -12.55471 | -45.66199 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 327ad4d1-b89b-36bb-87cd-3a14f8524f82 | -16.65241 | -49.76709 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bba12be3-fcd9-377c-ba1c-4abd991fe0f4 | -10.75835 | -46.47275 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ae402e3-fff9-3dcd-9964-162ddc88a8f7 | -10.92001 | -45.59144 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0cfbfb0d-ca5a-3dc3-b5da-ad42f2b4005d | -11.43383 | -43.54838 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd060bf1-69d4-3cc0-a63b-af93be2ac7ba | -11.05232 | -43.23552 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70f9c349-f80e-3a87-a72a-09883803a910 | -11.46333 | -48.70382 | 2025-09-14 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c22e41dd-1010-3a8c-86fe-b7381dbc63f5 | -15.76616 | -52.23901 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 176943fa-b7a2-3c32-8ac4-c8802f31198c | -5.72853 | -43.20388 | 2025-09-14 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| abd37991-137a-3b3e-af42-a24000950b79 | -11.85395 | -50.49839 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c992be73-e61c-320d-ac3b-ea1b64d00488 | -15.93125 | -49.98 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 61e38005-a07f-35dd-924a-3eefa575b279 | -13.93079 | -44.83454 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0990c1ae-4dfd-33e8-a1b8-0baf6f333306 | -12.9288 | -47.94607 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af6c4ad4-b40d-38f2-a7e6-ad87d1c81102 | -12.75786 | -48.00235 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fbd126c9-6180-321b-a5d0-9ab1d601dd29 | -10.91986 | -45.56503 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07269828-09d4-36c3-ac77-aa4ce58aadd5 | -10.92195 | -45.58081 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 74b70831-ea78-34d9-9e20-93ceb3906f3b | -10.74258 | -46.44361 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 141c34ff-779e-34bb-aed2-21614b54bf46 | -12.77141 | -48.02028 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5cf2f89-d0a5-3584-b903-2b232dbda562 | -12.7823 | -47.99295 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da28b99f-204b-3f7d-bd29-dbf02efdbc52 | -12.78069 | -48.0038 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d5c2f91d-4b12-3661-8227-4855783943ec | -4.48577 | -48.11394 | 2025-09-14 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 075df7e0-03d6-3c69-8171-ade57f0b383a | -10.89988 | -47.2168 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21fb74c3-4dcf-314c-a8ee-06167b369e24 | -12.74884 | -48.01965 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a55fa5da-ad98-36f3-bb90-c7a15b8cc3b2 | -18.29216 | -45.10969 | 2025-09-14 03:49:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96acaaf1-4942-34da-9d94-32d205f7fed2 | -14.16873 | -46.15659 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a3a5e10-a484-370a-952c-78e53ab0d33b | -11.50411 | -43.63778 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0a9a9da-d35c-3979-b452-1db695776ff6 | -15.76574 | -53.48391 | 2025-09-14 03:49:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9d6c0c75-2161-32a3-8cb1-619d0f7d3e9a | -16.65654 | -49.77547 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d353380e-e07f-3c87-90bf-3e6d861c0de4 | -18.34794 | -43.60622 | 2025-09-14 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5fb9cd0-f1fb-365c-97e8-16e8a8fe0fc6 | -14.31029 | -46.08458 | 2025-09-14 03:49:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08b74dd6-2d37-3492-93c2-e7a4180bb84a | -13.43703 | -49.13081 | 2025-09-14 03:49:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99b92bff-3304-30b4-9f7c-f2f2ce4ed506 | -17.12907 | -48.51129 | 2025-09-14 03:49:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a5c1986-9e7b-36c0-aea3-abe8fc9f7783 | -12.96861 | -48.03109 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 228d2db1-a59c-3abe-a800-810be653e8eb | -11.6683 | -46.51054 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c7d3434-8d25-3127-850e-06918033c05b | -18.53351 | -44.93848 | 2025-09-14 03:49:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2837fab6-7beb-3a3b-936e-e2ccb74c03be | -6.65412 | -46.09171 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6facb18-2783-3fee-8d0e-9b0fd3cac059 | -14.63211 | -46.36913 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d9945abe-936c-363d-a00b-1934323a60b1 | -6.69991 | -45.54721 | 2025-09-14 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d0ab8d4-ea54-3924-b3c8-1ea0b29eb599 | -11.30657 | -50.77781 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c08225f2-814c-3f54-8d94-e490d3d4d4b9 | -15.44379 | -47.35142 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3279a17d-3d2d-306d-b19e-9b34d9e1fefe | -14.43338 | -43.21339 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1b579d1-5e48-32db-b448-7f0860dda578 | -11.23062 | -47.62929 | 2025-09-14 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3dc0632-f379-36ef-85ca-e54d21342ede | -15.91398 | -49.98014 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f5ab68a-0a6c-310c-af5d-4a8fb3f89671 | -12.92225 | -47.95067 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 89bbedd8-28bb-3445-83e9-47b647337e18 | -15.76875 | -52.22725 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7ea719f5-2cec-3056-af3c-517eba007dfc | -13.9327 | -44.84842 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1009e248-4603-3d36-b69a-b89fcaf3c956 | -13.01244 | -46.74583 | 2025-09-14 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4a82441-4e10-3a86-8a23-8b701e50c827 | -15.80262 | -52.21489 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ce3e746-f81a-3bfc-9139-7f29489fc346 | -15.63638 | -44.37685 | 2025-09-14 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0667101a-1070-3de4-8509-d4885d9e75a1 | -10.90116 | -47.21009 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31a4c6e7-cc33-3ac0-9d5b-b60f5e91cfce | -6.43839 | -43.32566 | 2025-09-14 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a53fbf4-73dc-3b2b-b87d-e2677b3108b5 | -11.33782 | -50.82794 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e6ba699-07c8-3d06-831b-51452a6a9784 | -5.0893 | -41.15637 | 2025-09-14 03:49:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 842e40f0-f964-3e80-8d2f-af7610595a13 | -12.81838 | -47.1556 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61cd11a5-c029-3578-b556-ff7d86bed436 | -11.39493 | -47.34021 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a950b633-772e-394d-8e40-99a7ab37eb26 | -17.96387 | -45.2555 | 2025-09-14 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a686ee61-4d9d-3267-a68d-f237bfdffcab | -17.99665 | -46.95074 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README17.md)
