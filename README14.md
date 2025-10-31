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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d543401-b8ca-32f6-a9d7-a21d76cb2507 | -12.84058 | -43.47895 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e5488a7-b113-3c63-8c94-3ab71c66dcb9 | -12.6052 | -47.52741 | 2025-10-31 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f61a4343-ded3-3015-b735-fedd0b096707 | -12.29008 | -43.19377 | 2025-10-31 03:49:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f07c5ffe-f343-3dec-a521-8747fd433e56 | -12.20027 | -42.91887 | 2025-10-31 03:49:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 61923aef-2fab-31d2-80b0-3704e4eea821 | -12.60037 | -47.53391 | 2025-10-31 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09a4d2bb-2777-345c-9616-cbcd09e98c14 | -11.64057 | -44.04687 | 2025-10-31 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a39a3f9-ac8e-32ac-8011-cadce0225d38 | -12.29455 | -43.1945 | 2025-10-31 03:49:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d94b365d-66fc-33db-ac04-3ec830c5f5f6 | -12.84041 | -43.47165 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c3be688-22f6-3602-893a-9541b8b8adaf | -12.13637 | -47.1558 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f226159d-42dc-3d37-9f8d-5d4476b57048 | -12.13721 | -47.15168 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3326510-77c4-3af2-a3b0-23793881e8c9 | -11.64152 | -44.04166 | 2025-10-31 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c079b15-7dcb-37cd-b01b-a9857f3c494b | -12.84507 | -43.4798 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd9a02ee-10d0-3e2e-9ae2-1394c2576af8 | -12.84402 | -43.46069 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11f22ccd-3619-3451-8207-e1f0e81a68cc | -13.38138 | -41.32558 | 2025-10-31 03:49:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65451a84-b39a-38f5-9254-eb8fdc0623dd | -12.91951 | -45.05302 | 2025-10-31 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d6cc2ba1-ee2f-3301-b79b-2be5071b2574 | -12.53062 | -47.54622 | 2025-10-31 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96f29571-c0af-32c6-8dfd-87b50bf4d1f2 | -12.39816 | -46.8285 | 2025-10-31 03:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d339de3e-b023-3b6c-8d39-f674521db25a | -10.54376 | -48.7076 | 2025-10-31 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 49b1c2b2-c081-3f16-83ed-2bad27338c35 | -12.15262 | -45.21938 | 2025-10-31 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4eb07ef-4b4b-3965-bc98-c372899e47f9 | -11.50722 | -43.99825 | 2025-10-31 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 997c6369-426e-30d6-b2bf-6cd258fc709e | -12.82278 | -43.49193 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3c0ff0fd-cc29-3a79-8240-77814012f4a3 | -12.8449 | -43.47253 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| accd97d1-2327-3738-ba16-bef9a3404732 | -12.20062 | -42.92014 | 2025-10-31 03:49:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 88b8fed9-d03f-3033-9fe4-555f77734353 | -11.12847 | -45.15743 | 2025-10-31 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 235bd433-b927-3a95-83ab-b23a7e18fa65 | -10.54141 | -48.71909 | 2025-10-31 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 40d3ca79-2c6e-3274-ba2e-5437463cc643 | -12.8423 | -43.46982 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1cd034f0-f5e6-341b-bc2b-f71bb3293dc5 | -12.52487 | -43.75652 | 2025-10-31 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b440368-c2d8-3018-91ab-1a91e58c8f42 | -12.84573 | -43.46796 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 72fb9b62-9ef2-30a4-b4a4-e68ff1998003 | -10.54367 | -48.71494 | 2025-10-31 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64626514-ff14-31ac-952d-0fec4968b514 | -12.60122 | -47.52959 | 2025-10-31 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a7689edf-9227-3b5e-b4fa-41899e721cd9 | -10.54479 | -48.70927 | 2025-10-31 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b51d35fd-bff0-3210-99d5-03c9702b221d | -11.63676 | -44.04071 | 2025-10-31 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d13749e-276f-3171-96ba-693209fd4f20 | -10.53823 | -48.7081 | 2025-10-31 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f290fca8-db21-3ddb-9827-8db5379ba5ed | -12.82362 | -43.48734 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2ee2bd5-7765-34e6-8e13-0479bfe6d77f | -12.84407 | -43.4771 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 00a40451-2d69-3d91-9582-7e6688e6e281 | -12.12991 | -47.15996 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c776008-d4a0-3698-a0fd-efb89456e7c1 | -12.8326 | -43.48909 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1255a982-1d15-3016-b371-bf3f1fbe8ce7 | -12.82727 | -43.49281 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8afd67c1-9dc3-362e-a3ee-f9682deacb9c | -12.06515 | -47.3351 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0904c851-a216-3b2b-9c49-0c34f4c4c6fe | -12.72619 | -43.00596 | 2025-10-31 03:49:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 531d34f3-3b0d-3b46-85e7-c6437408b1b3 | -10.53714 | -48.71361 | 2025-10-31 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2fe8df09-3e87-3583-91ab-6c98dc447c2b | -12.52977 | -47.55042 | 2025-10-31 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5425faf7-f5b7-325f-ae7b-0c0ad6c53c4b | -11.03324 | -45.49341 | 2025-10-31 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3534177a-4ff4-31af-9024-8683fd63dc10 | -12.84488 | -43.45613 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a953257-799c-3cba-90c1-df63cc759ee3 | -12.8429 | -43.45794 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68c15512-55fb-346d-8971-cf6fea12e8d1 | -12.52946 | -43.75743 | 2025-10-31 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4a12dd1-a7c5-36e2-91a7-c0d41a48d73d | -11.7136 | -43.91838 | 2025-10-31 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ed7b23e-0702-33d7-b777-a920e235cd8a | -11.71455 | -43.91328 | 2025-10-31 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3715568-58df-3a54-aca8-28e347f870b2 | -5.0399 | -43.6205 | 2025-10-31 03:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 60335936-aae1-3743-9e04-c6f469f3b77f | -3.017 | -49.4482 | 2025-10-31 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 128a0fbb-e2d2-3577-9bca-71587e3b4c03 | -7.668 | -43.5857 | 2025-10-31 03:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| e29bea93-b360-3f2c-aaf5-0a773faced38 | -7.6491 | -43.5876 | 2025-10-31 03:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 64143954-e131-3381-b371-3745dd773c71 | -10.5293 | -44.7798 | 2025-10-31 03:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 7cf09bd1-a58f-32a5-b885-ac0109f211c8 | -11.559 | -47.0742 | 2025-10-31 03:50:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 3e4fd8fd-addb-3963-bb8c-f85b23ab2296 | -3.3024 | -51.9254 | 2025-10-31 03:50:00 | GOES-19 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 0c7b8ae0-5b6e-3b32-be6a-29fd46059c31 | -10.5483 | -44.7773 | 2025-10-31 03:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 2b72338c-a912-3476-be91-f0d130aa0de5 | -7.6488 | -43.6109 | 2025-10-31 03:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 494a905e-37dd-376f-b6de-4d49f74bd3d9 | -7.6677 | -43.609 | 2025-10-31 03:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 53cb38ab-cb1f-3bf0-878f-7903c462f3db | -3.017 | -49.4482 | 2025-10-31 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| add607ce-6883-319a-a6f4-e30c9513e466 | -7.6488 | -43.6109 | 2025-10-31 04:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 5f5934b4-ec11-3c27-9955-b914fc4eaae5 | -5.0399 | -43.6205 | 2025-10-31 04:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a8b4216a-4154-3f28-a615-2a65eefab71b | -4.8013 | -43.0306 | 2025-10-31 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 0a6ed7df-1e22-3cf5-860c-5fa82d420899 | -10.5483 | -44.7773 | 2025-10-31 04:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| e5d2058b-9b5a-352b-864c-e8b26ececdcb | -7.6677 | -43.609 | 2025-10-31 04:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 59430b44-b8eb-3bc6-a262-19ae8b698ed1 | -11.559 | -47.0742 | 2025-10-31 04:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| c0e5e09e-f761-39da-b085-2120acf0efb3 | -7.668 | -43.5857 | 2025-10-31 04:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 185.7 |
| a2917714-a0af-3a49-b8e2-72c8f16867f7 | -12.2874 | -48.0676 | 2025-10-31 04:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ddcc97a8-9961-3988-9b74-1d90a1a5d0a5 | -7.6491 | -43.5876 | 2025-10-31 04:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 252.8 |
| ce7e4302-1b5d-3354-9267-93064d32a031 | -3.01368 | -49.45184 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0d5c3984-95d2-3858-995d-eeb88f7ceb4a | -6.38958 | -44.24456 | 2025-10-31 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1ef895f-441a-3927-86b7-2152a4fa4bd1 | -3.01475 | -49.44551 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 6938e08f-2559-3b26-b340-e59ec2c477e0 | -4.48062 | -46.5674 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c55772ca-707d-3c5d-9625-b592eb9fcb69 | -7.48251 | -41.74182 | 2025-10-31 04:06:00 | NOAA-20 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab2c3287-de86-3797-871c-ea2f5513c11b | -5.69594 | -43.15962 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3e753919-4ce4-3caa-84b0-3eedccc48203 | -4.80571 | -43.02478 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 019865fd-ce62-35e2-9857-80456a392eaa | -4.35444 | -46.7791 | 2025-10-31 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4722f0c4-6302-3fa5-98fb-1773811ea8b3 | -7.48582 | -41.74234 | 2025-10-31 04:06:00 | NOAA-20 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 07bf1cae-8a65-34bd-bcef-fbbaba0bfc3b | -5.97632 | -43.73007 | 2025-10-31 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab4aae16-70cc-3b5a-a2af-3fcf8808fbb4 | -7.31498 | -44.97664 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 94613eec-04ea-382e-9d4f-a9c8d768f8a1 | -5.69193 | -43.16275 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 66a312f7-339e-3c6e-8806-20ceef24cb7d | -4.70049 | -46.49872 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc241dbe-d82f-37d7-9665-19943e0a9e05 | -4.85554 | -45.56837 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c1c2c47-39b2-32b9-982e-cca97cfb43dd | -6.02962 | -40.26258 | 2025-10-31 04:06:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3e903f5f-a130-3e40-8a8f-15e883c7c167 | -5.13844 | -46.14844 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71499387-2ab4-3c6e-a598-0d04c7aaf2c7 | -6.12844 | -41.79591 | 2025-10-31 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8e3c63a5-cf59-315e-baa3-cf89149ef84b | -4.68044 | -50.44735 | 2025-10-31 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1321f2e-8b37-37bd-816b-34b4f4abc111 | -4.04989 | -47.50392 | 2025-10-31 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc6a39cb-ee6a-321c-b21e-774eb6e95ed6 | -5.48046 | -48.48771 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4702b42d-7d7c-34f4-98da-77511ea77e43 | -5.71927 | -44.53555 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97d5ea5e-c5cf-359d-a675-35c7a3e27fb4 | -4.15468 | -43.8816 | 2025-10-31 04:06:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70fe2757-392a-3863-b109-f399494121a6 | -5.10229 | -45.18131 | 2025-10-31 04:06:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5eb11a7a-5510-3bd0-9434-e8d030c8200c | -3.22521 | -50.65302 | 2025-10-31 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e84f67e1-2743-3e92-ac33-6d6372ecbd75 | -5.06665 | -45.11396 | 2025-10-31 04:06:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be68aaf9-f9a5-3d8c-a2cf-dee45866cb4b | -2.4188 | -49.30306 | 2025-10-31 04:06:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d243a8c0-fb6c-3be2-8bee-d241e8977bde | -4.85944 | -45.56898 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67a8a1ee-cd2d-3039-b442-52081caf6866 | -6.58629 | -40.10797 | 2025-10-31 04:06:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8ff1912-b62c-3b30-a46b-a4510859b778 | -4.80845 | -43.02851 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| eb8936f6-722b-395f-8847-f7e736702a05 | -1.95393 | -47.85913 | 2025-10-31 04:06:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff18e177-96a7-31c6-9b1c-e93046274401 | -7.33184 | -42.73368 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c867a1f4-d010-3d35-af6d-79345c1c9bd1 | -4.68113 | -42.72945 | 2025-10-31 04:06:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README15.md)
