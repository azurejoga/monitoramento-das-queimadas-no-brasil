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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f08fa85-a91e-361d-8e72-58654c626884 | -11.54049 | -49.43201 | 2025-10-27 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef603eab-d9cb-3be4-8264-bbada7431356 | -14.21558 | -44.39309 | 2025-10-27 04:34:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74889937-e9f2-3a72-b09f-61f07c482550 | -10.41216 | -45.30194 | 2025-10-27 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d222ae4-d50c-392d-b8b2-14e13bcee367 | -10.60536 | -46.62185 | 2025-10-27 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87d6fc01-6418-3fb9-9993-d114a3e48d4f | -10.35524 | -47.18634 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 61164995-3eff-30c4-bd6f-9b49c152246f | -12.21842 | -46.52163 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d57fce02-8de0-3221-8646-5bee45ec5238 | -11.84253 | -49.86583 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce702c66-f308-3439-8abd-8391c7ff6662 | -15.47559 | -47.36122 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 476b040f-800f-3874-9099-560e0f0b1d13 | -15.86716 | -45.25785 | 2025-10-27 04:34:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4047348-3922-3d90-a55d-81d1efd58530 | -13.55575 | -49.55725 | 2025-10-27 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72e7a384-32a1-3a6c-880b-3f229f877332 | -14.02377 | -43.26588 | 2025-10-27 04:34:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a77a2fbe-f8f4-3076-aa54-43d0a1ed9d99 | -10.91112 | -47.95113 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2855254a-8728-3c9e-8548-90bb43eda44f | -10.63152 | -52.18592 | 2025-10-27 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7924ba02-f0e2-3635-abcd-4435b6a0032c | -10.96826 | -47.86613 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df10cc49-1d58-3529-acf7-bc592c62a972 | -11.32867 | -47.21912 | 2025-10-27 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e19b3620-463c-3cd8-928a-8d6e839988ed | -11.00859 | -47.82521 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c00a8ad3-5975-34e5-97f0-6d55a5f97f36 | -13.55245 | -44.26331 | 2025-10-27 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5270816b-f9b0-38d7-a4e1-8ea322a875ba | -16.62892 | -44.58643 | 2025-10-27 04:34:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ace2eda3-f531-3029-bf53-ec28b7d156ee | -11.42234 | -46.10717 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2924579f-d6ad-3665-9a9d-9458b6161495 | -11.9743 | -44.30731 | 2025-10-27 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03d360ea-0d00-3d72-bd89-1c32ca3274c6 | -10.2082 | -52.66653 | 2025-10-27 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb7c4155-c75f-3951-85e0-ebb87b429579 | -14.02548 | -48.00646 | 2025-10-27 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9e1fdad-cfd6-34f7-ab5a-6701036fa937 | -12.52847 | -47.56786 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 07caa27e-ef65-3a64-a9fe-d6abcce6e378 | -13.54748 | -49.56676 | 2025-10-27 04:34:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f67f3cca-b280-37f3-84ea-173a79c85bdf | -10.55942 | -51.35267 | 2025-10-27 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35aeb651-1651-3260-a1f2-8c92c04519e1 | -13.64384 | -47.62965 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 427a8032-42ba-3776-ae01-b569225f643c | -14.63562 | -48.3987 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19c825ec-f0f8-3378-904c-9465ce44f23f | -12.8587 | -48.63814 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bff2152e-b43e-3b11-bf7a-98a4a74be389 | -12.05103 | -46.60548 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 22581425-28a9-3c81-943d-bd19a8b807d8 | -15.51223 | -50.01251 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 18087c64-eda8-3cfc-986d-61071107b5ea | -13.24914 | -47.9729 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f23eaa06-47d9-3816-b46f-ae1183bffdc8 | -14.25481 | -48.13293 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daf95235-4c5f-3f4a-a479-ac3b7f622f7c | -14.22963 | -44.38031 | 2025-10-27 04:34:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6472ebfe-2d0f-3f38-8a92-51ebb6523fc9 | -13.6038 | -43.11547 | 2025-10-27 04:34:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b4db543b-5ebf-35ec-b854-1cb9b941befd | -11.80127 | -52.49169 | 2025-10-27 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 097ced91-f99f-362a-9286-2c67db6f8118 | -11.60592 | -50.99435 | 2025-10-27 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f802a4fb-d111-3729-98cf-de95bcd34c17 | -12.50811 | -44.32795 | 2025-10-27 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b51fbc6c-adee-38d7-9858-d4070c3940b9 | -11.33076 | -53.92891 | 2025-10-27 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99b0fcc6-c058-3871-95aa-c0323bba1f15 | -10.20976 | -52.65734 | 2025-10-27 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ceeca2c-8122-3164-b45e-6cf50baf4787 | -12.87085 | -48.64727 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 269ee3ba-af58-3083-b70d-7d93c2b5177a | -12.30373 | -47.44696 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ed1919c-204e-3541-b279-74fee1603e3f | -10.95422 | -47.58199 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23eba6d8-3902-3869-b6f2-0b8533b604fd | -14.8329 | -47.40345 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ca95b12-fe11-3f12-b140-80776760595a | -11.01858 | -47.82678 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa2bda80-b487-32cd-b363-e60832b6aef7 | -12.7852 | -48.56392 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df6d25e8-75f4-3a5d-b424-10c785f4e1f0 | -11.02573 | -47.80239 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54ee969c-0d91-32f6-b4f9-2a8f874a768b | -11.631 | -54.58302 | 2025-10-27 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 418718b3-5c62-353b-95d2-eec5b1d0473a | -10.9985 | -47.77977 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59266b12-4fb3-3cf5-b6f4-e7349482effd | -10.17479 | -49.3101 | 2025-10-27 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10c1e661-2ee0-3187-b8ed-2122a2caf330 | -13.54087 | -49.5657 | 2025-10-27 04:34:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e220324-499c-3007-ace7-81e9b92f182a | -11.33405 | -47.89784 | 2025-10-27 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 67c236f7-0763-3c54-8a1c-b3922fbe6a0b | -11.42589 | -46.10761 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe97c25d-6c94-38c9-b62e-7aa4b71811da | -12.32704 | -47.48479 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ff770575-61da-3525-9d15-9fc3d194a23d | -13.54418 | -49.56623 | 2025-10-27 04:34:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc8b4f56-d502-3e20-a404-f6a4729767d8 | -12.5262 | -47.55996 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c89e315-a63e-3d20-9629-9ca821d960a3 | -11.33072 | -47.89732 | 2025-10-27 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f8ee281d-08cf-3cef-ab6b-974d226d1db1 | -10.23413 | -52.15903 | 2025-10-27 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 915bc4b7-5e43-3aed-9fad-5f1ca96f3ebf | -13.64365 | -48.44184 | 2025-10-27 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 472d9460-e430-3d04-a758-4e95a12abbc4 | -14.55361 | -48.0392 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aff188b4-8f59-3dfd-bb93-82bceecf776b | -15.29463 | -42.93443 | 2025-10-27 04:34:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b2ff8af9-f1e7-3e3c-b357-0a46e02caa27 | -13.54474 | -49.56268 | 2025-10-27 04:34:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0265c0e-973b-3ddb-92cf-e2db16e6afd9 | -10.32542 | -47.15574 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43ab6ad3-2a1d-3006-86bf-1de945318f45 | -17.40899 | -46.8867 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33baa812-819b-3c65-99ed-a82d9bc760e3 | -12.32413 | -47.45794 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97b120e3-603f-3444-a966-2ba582bb7e9a | -12.5265 | -49.5902 | 2025-10-27 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 710e1626-7fa6-33df-a056-c6551023e6d8 | -12.00551 | -48.94321 | 2025-10-27 04:34:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42dcd409-4c23-3c66-af98-f8f5be0a433e | -12.28754 | -43.75932 | 2025-10-27 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02de392b-a4e7-3666-8f9a-2a6d2be37267 | -15.19433 | -47.22719 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 147bbd39-26c9-3cd4-a663-84cce6fdf16e | -15.29403 | -42.93908 | 2025-10-27 04:34:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 18f58c3b-4519-3232-8c8a-80ab335802b4 | -11.44987 | -43.72089 | 2025-10-27 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9b0e3c6-cd82-38f5-bcc5-8cf3cbae89e4 | -10.61497 | -44.64981 | 2025-10-27 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89f9e485-81d1-3a38-9a71-74bf0c302a27 | -10.35464 | -47.16763 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6958ab4d-4467-3eb3-a33b-9f5ed510f408 | -10.17423 | -49.31362 | 2025-10-27 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 659d6474-fd84-3a4a-a200-7da3e6de4d7b | -12.53827 | -48.70931 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df7f96ab-39bd-3d26-afdf-bb6a89d81735 | -11.42467 | -46.1158 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 719d27cc-fd6e-364e-bae0-9e5f25d666d8 | -10.77914 | -43.86642 | 2025-10-27 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a564860-5087-3ae6-80f2-4fee30d019a0 | -13.24969 | -47.96925 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73868e3e-0afa-3b16-8e2a-e45e4d54cb2f | -13.08297 | -44.54205 | 2025-10-27 04:34:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f318c9f1-f047-3830-8a88-0d066358703e | -9.92439 | -48.97846 | 2025-10-27 04:34:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7c60f2b-b517-327c-ba9a-8fe971862e61 | -13.64036 | -47.60639 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35504ecf-54f0-3264-bcd1-25996a2fd28b | -10.3431 | -54.19768 | 2025-10-27 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ddc0f7e-e504-30f2-b38a-0c0cc21210b7 | -12.28343 | -43.75892 | 2025-10-27 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d16111a-e5c5-3ce4-b59e-525d2ab04c07 | -13.41712 | -48.56713 | 2025-10-27 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d3f50d5-7e88-344b-bdbb-5af93592b1da | -14.25817 | -48.13343 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15832ece-f861-3bcb-b9d0-74c5a2f0ac3d | -10.5372 | -51.59766 | 2025-10-27 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a179617f-aa0a-3c90-ac9a-28ec2f356f02 | -10.32001 | -47.21421 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1261ece-d02b-3cba-b88a-397dc22a99ff | -11.05128 | -47.87878 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06c76078-61fb-34d4-a3f2-846740b1adb4 | -12.32312 | -47.4879 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e751fc6d-4830-324c-8a80-8f89e9c0e9d6 | -14.82763 | -52.42847 | 2025-10-27 04:34:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 75bc3e1f-d118-3171-ac82-4e437b799ba0 | -10.87837 | -54.05096 | 2025-10-27 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f88bea0d-6054-3e50-96d3-f79eb36c97aa | -10.87962 | -54.04373 | 2025-10-27 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7e5640e-b5d0-3136-8521-e816ac36375e | -15.18841 | -47.21881 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2271eed1-d07f-35d8-9d9a-14aed4c79719 | -10.35016 | -47.1744 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95999ff9-bafe-3563-80bf-ffd518d5ea21 | -13.74281 | -49.795 | 2025-10-27 04:34:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c5ba483-de71-36fd-abdd-422d58b4453c | -12.23654 | -46.49607 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abfeb524-294b-39f4-a683-365619a51c64 | -12.31973 | -47.48738 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b7e1c8e-2ed8-32c4-b73f-8dd606aac57f | -12.52565 | -47.56364 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5dbd059-c3f8-3c41-a79e-0f5e1f1c9e8a | -10.88884 | -50.14677 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18df0a5f-300d-3102-a1fc-c1f3fd760505 | -13.23579 | -47.99308 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 78554ac6-d5a0-3102-a095-a31ce3e53fbf | -10.34271 | -47.10989 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README49.md)
