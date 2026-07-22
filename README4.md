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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79e599fb-9825-3800-9505-f55a5b09d41e | -17.57898 | -47.50767 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 53625e1c-7547-34e7-80ba-97867d1f3700 | -12.14134 | -48.25771 | 2026-07-22 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 97ed5e25-3404-3414-9e7b-db952f7ec725 | -17.25757 | -48.28496 | 2026-07-22 04:10:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb819052-bf72-33b9-9a7e-6caa985f0232 | -11.33227 | -48.00117 | 2026-07-22 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5384428-64d5-39de-9510-4072c20a4172 | -15.70413 | -43.00142 | 2026-07-22 04:10:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e75abf4-7155-383e-879a-885b73168848 | -12.00085 | -49.26846 | 2026-07-22 04:10:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38ec5d66-82ef-33ff-821e-2ef98e3f561c | -12.51857 | -48.25743 | 2026-07-22 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 24bcc1e4-7b9d-33f4-a389-be858d277c4d | -10.63089 | -47.48513 | 2026-07-22 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3ba4f5a5-90b1-37ab-aa15-efcb11d81b55 | -17.58334 | -47.50399 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9f530ae7-00f5-3120-a677-a323f2cfbd02 | -17.58278 | -47.51141 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e3671009-93f1-31f0-b028-3055d7adc1c5 | -12.23372 | -46.58524 | 2026-07-22 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 933564d8-e5aa-3ba6-9854-4e5ed0fe7042 | -12.52263 | -48.25819 | 2026-07-22 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8728a32-e674-31d8-b4ac-702ee3638dfc | -17.57917 | -47.51069 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| cd3d00f7-049d-3ecd-8a96-7711318bcbf3 | -17.57175 | -47.50632 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 834b1196-1a06-3bf7-adda-5d0d331a4bca | -17.58108 | -47.51728 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4fcf21b4-2f63-3c09-93d1-916535f833c4 | -11.84249 | -44.77587 | 2026-07-22 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0b53ac5-e83c-3864-b556-7119fb7cb7a4 | -10.51116 | -50.2772 | 2026-07-22 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00b3584c-8d30-31bf-af92-1a75edcb623c | -11.81354 | -47.34152 | 2026-07-22 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 350bcd8b-7102-3ac9-bece-eeb8d32697ae | -12.51728 | -48.26482 | 2026-07-22 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b75ee90-c5da-39b8-aac1-972eb84d77f5 | -11.37444 | -47.483 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82234e83-afc2-3c22-b85a-125b4d2014d6 | -11.55796 | -47.61199 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bc05ae9-7316-3c4b-a1b9-05bbdb8dc2e5 | -11.40382 | -47.49607 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30b27973-55e5-3334-8e4e-aa2f717759ea | -11.33099 | -48.00854 | 2026-07-22 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 267d2813-1541-3aa4-b125-5b97a1804d7d | -12.51985 | -48.25007 | 2026-07-22 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a54afe97-2298-38f9-a308-67ee63dd2990 | -11.81439 | -47.33649 | 2026-07-22 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 454ffbf4-8e68-3209-81dc-a67cf28fb73e | -13.71262 | -49.85417 | 2026-07-22 04:10:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ef52613-2ae6-389b-b6de-e5fb56a88ab3 | -12.46044 | -46.51112 | 2026-07-22 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c2a21749-c7cc-31ac-81d8-999782cf76bb | -11.88743 | -43.82926 | 2026-07-22 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 70d66f84-81a9-3c27-a835-babbf0f32c86 | -11.83811 | -44.75969 | 2026-07-22 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dc4b60f-4983-33b5-b564-ffc79db95c67 | -10.95454 | -49.80968 | 2026-07-22 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f410f925-6bff-30e9-bb71-65470c0f0f5a | -14.00325 | -42.54789 | 2026-07-22 04:10:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8526a725-cb4a-32fc-a0f2-8b622cc7bc4b | -12.66827 | -48.21592 | 2026-07-22 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15e6af7a-d71c-37f3-aeb7-b3c57197ff1a | -16.72715 | -49.40104 | 2026-07-22 04:10:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 456330be-afb1-3307-80f8-62c521db35f2 | -17.59701 | -44.6026 | 2026-07-22 04:10:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bea3988-b3cf-385f-b1fe-36e3c1bd6799 | -11.55399 | -47.61127 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c66f6881-7fca-36b7-8be3-9184019f595f | -17.57555 | -47.51003 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 759b9f23-8421-37f4-8784-60c8ec75c783 | -11.91183 | -43.84798 | 2026-07-22 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ffab54a9-17cf-3c6f-8a89-20cb82703936 | -17.67772 | -47.22194 | 2026-07-22 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7548e1f-4740-3b6b-8867-f5abc6328bc0 | -17.91676 | -44.40844 | 2026-07-22 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c8df42b-43e5-314a-89ec-0d9e8d0eaf3a | -12.5267 | -48.25896 | 2026-07-22 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d2b91a6-c6aa-3e1e-a447-dbcbaa5ebadd | -11.41778 | -47.50946 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2789d793-8c2e-33bd-8c16-2ccaffb3a5bc | -10.54199 | -50.27178 | 2026-07-22 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1f4e823-b20c-3676-b613-8cedff456701 | -11.9124 | -43.84439 | 2026-07-22 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28218d92-cf89-3f3e-8f42-0be2382c1e2a | -15.66188 | -43.32127 | 2026-07-22 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b4c8fb09-1aa2-314b-8836-2c5a25c52ae0 | -17.57838 | -47.51514 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9ee992e4-806a-39e3-8c64-ebf01b9a976a | -11.84188 | -44.77956 | 2026-07-22 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20b15606-7c0e-36b4-b78c-51b03aae99d5 | -11.40205 | -47.50624 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b07b031e-d3c1-315b-94c0-99c69c13b70d | -17.60306 | -44.60737 | 2026-07-22 04:10:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 479326af-f2d0-3359-8d64-5449830b58ee | -17.5725 | -47.50192 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cfb147e5-b753-3df9-9fef-687882c7f266 | -10.66759 | -49.56329 | 2026-07-22 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 428e10c6-485e-3b2f-96f1-8401203be577 | -13.9921 | -49.59251 | 2026-07-22 04:10:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d897590d-cef8-338a-ac31-befa166f29f0 | -11.63788 | -48.5417 | 2026-07-22 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a7dba90-d141-38e0-a186-45c60942f463 | -12.23003 | -46.58458 | 2026-07-22 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7df79ca-bb47-3232-b598-ae17018414c1 | -11.38115 | -47.48604 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b41f5dc7-cd86-3c03-8eb4-20de1de24ad1 | -17.56813 | -47.50566 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 30952672-9103-35a3-a02c-b4599a1cbcac | -11.37721 | -47.48533 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 664fea98-39d7-33bb-bb79-20af24a68a96 | -17.57995 | -47.50631 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 54d0d72f-7b70-3a1a-9f8a-f58f2120715b | -17.58433 | -47.50264 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa1f8bfc-0bec-310b-a407-a52d59e1fe5a | -18.27188 | -43.69706 | 2026-07-22 04:10:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9bfc6f56-7119-32e9-9129-cec3f4bf31f6 | -12.49312 | -43.76772 | 2026-07-22 04:10:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c337013c-c517-367c-bf1a-72040f99e8eb | -17.57537 | -47.50699 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| effaca40-8a1f-35fb-a722-330f91f5c5de | -17.57823 | -47.51207 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 63cbeaff-d7f5-3f72-b7d9-8a8ec266b3c7 | -12.49644 | -43.76827 | 2026-07-22 04:10:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e1f7399-4ccb-350f-9782-542e2df16a99 | -15.85624 | -43.60236 | 2026-07-22 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88599272-2aa8-39c2-91c2-2e402f9ed087 | -11.97008 | -43.97158 | 2026-07-22 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8915072-9de2-386e-961a-4ff5fd4faad7 | -11.33163 | -48.00484 | 2026-07-22 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d660a5f-3df5-3646-8926-0f934cb96a7a | -12.37587 | -45.67484 | 2026-07-22 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea299729-adc6-3643-86ba-88ba072d2113 | -13.43998 | -43.67561 | 2026-07-22 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38e76afc-486b-3ce6-b794-688e2a9198d4 | -17.5826 | -47.50838 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 241c36ea-61b1-3f73-ac5c-932dbc26edcb | -11.38902 | -47.48759 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| baa29dd4-ad0f-33b5-a2b2-a73645e9eb17 | -12.45969 | -46.51555 | 2026-07-22 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4a438438-cfc5-320b-99b8-89a9825f61a9 | -17.57611 | -47.5026 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ddc7f4bd-5acf-34df-b6da-56406ef6c725 | -11.42387 | -47.52139 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4adfa9f-e902-3e60-bf97-a52bc648a012 | -10.5468 | -50.27268 | 2026-07-22 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d87ee0ca-5de1-3737-bd34-2ca3a178e477 | -12.6985 | -45.32384 | 2026-07-22 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e639dad-5f83-3dce-a106-d18bab10e4fa | -12.32656 | -53.27805 | 2026-07-22 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e3460fa-d699-3ecf-bb64-3f16e6b2dd2b | -17.57759 | -47.51965 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f37e7276-eb14-3683-877f-7ee00143e7bf | -11.42082 | -47.51547 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28d4cb3a-6557-3911-b2e6-a04dcca0bff0 | -12.69504 | -45.32325 | 2026-07-22 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7d736ba-5906-3581-95a4-d57422b5621a | -12.45893 | -46.51999 | 2026-07-22 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c2580eb-0b99-389c-8a95-23dc633bd866 | -17.57973 | -47.50328 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f0d4e046-1ae9-3b6e-a4cb-0b36e3541e8b | -12.66762 | -48.21954 | 2026-07-22 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 130f4fb2-7362-3037-ad24-03df81dad361 | -12.32985 | -50.01291 | 2026-07-22 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a7838d6-6317-3b7b-ab8c-ab035082b791 | -11.63224 | -48.5489 | 2026-07-22 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9c19ae4-0c2f-34fa-8f11-3d30e795cd28 | -11.33508 | -48.00922 | 2026-07-22 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33e5f52e-8843-37ba-8bbf-7735db97511d | -13.40905 | -44.16929 | 2026-07-22 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62e48be7-19f3-3493-868b-54714c7ae339 | -10.98184 | -44.55794 | 2026-07-22 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b05d0b7-1595-3a6b-ae89-d4ba13f24324 | -11.38599 | -47.48165 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e55f8e9f-de03-320a-b48e-f61d26827111 | -17.58047 | -47.49894 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9645b37c-fe52-3d63-885a-1a7a301ddca4 | -11.64209 | -48.54245 | 2026-07-22 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58b8199a-fcd9-381a-b59a-e20316419e83 | -12.52846 | -48.53039 | 2026-07-22 04:10:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9cc51ae-e5bf-3c0a-ad67-49c5d7fc7afe | -11.09824 | -46.94892 | 2026-07-22 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0db9bb3a-0de2-33d5-bc42-5f18f54444c7 | -12.52775 | -48.53435 | 2026-07-22 04:10:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c7235dd-a955-3946-a63a-a7fa00d2410a | -17.58199 | -47.51588 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 92cb1a60-9b27-3b1a-aa53-494f0ac1797d | -11.63366 | -48.54098 | 2026-07-22 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c56435b-6fef-3508-905b-22d59cf1ebd0 | -11.40687 | -47.50193 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afa4915e-8584-3464-a4cd-415a339da18e | -10.42655 | -50.19925 | 2026-07-22 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40e22ca8-e640-3c91-b03a-51ede9e305b4 | -11.33636 | -48.00185 | 2026-07-22 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7887c394-c106-3964-8834-d70e7a802456 | -10.51019 | -50.28257 | 2026-07-22 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a15182cc-73ec-35aa-89f0-6cbd0bb59d23 | -23.19303 | -46.29775 | 2026-07-22 04:12:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README5.md)
