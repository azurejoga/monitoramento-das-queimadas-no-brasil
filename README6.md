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
| 5e6a9b7e-45f5-3f9c-8568-8ec051105a82 | -8.04014 | -43.11411 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 28857a59-e11d-3a2b-b91c-8e7227615178 | -8.00106 | -43.14041 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 6073f59f-ce27-3759-ad00-149ab31af878 | -8.01262 | -43.19385 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3a3b6a5f-b003-39b5-bfb1-1a95c934e403 | -8.00128 | -43.17678 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e819b107-8d9f-3ab3-b4ab-d0e7372dc4a1 | -8.00679 | -43.14851 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| ad916a36-d865-3e4b-80e9-8587f5cd4561 | -8.00424 | -43.19926 | 2025-08-04 03:15:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cef312c6-5de2-3346-bfa8-709f180fec28 | -8.05554 | -43.1101 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 51273830-e86c-3b69-98c8-b19c7bcb2d57 | -8.0415 | -43.1073 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| e86763d2-01c8-39d7-8a74-25b321122d35 | -8.01651 | -43.13615 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd1824df-2969-37af-97da-e811470a6f45 | -7.99692 | -43.1616 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.3 |
| a7bbcd49-d273-3abd-ab30-11aabc3b2c26 | -8.00263 | -43.16985 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| eba6d2ed-7d68-339b-bee6-96a6ba5d9fbe | -7.98837 | -43.16788 | 2025-08-04 03:15:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 229b6940-a2bb-3be6-a628-bd62896e8649 | -8.05689 | -43.1033 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 44f5fa53-a416-389b-9de5-59b51b9db6ce | -6.85406 | -41.70789 | 2025-08-04 03:15:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ba757e8b-46fa-33a6-81e7-5130d9dbec8d | -8.02753 | -43.11697 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5df2bf90-1edf-3091-b1aa-f9c1a3759fd4 | -8.00284 | -43.20642 | 2025-08-04 03:15:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ecce33d8-6449-3db0-9ad3-7905f0f48573 | -8.00144 | -43.21364 | 2025-08-04 03:15:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a7b9c432-31f9-3115-8f30-317b0c298466 | -7.99435 | -43.21235 | 2025-08-04 03:15:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 4d9f717d-edb1-3025-a283-ea5104b6e888 | -8.05826 | -43.10891 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| f1970614-7b6e-3fe8-8645-d0cbd1c4e60c | -8.0 | -43.22104 | 2025-08-04 03:15:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f27f0278-4e12-3e14-b038-af9080392bcb | -7.99575 | -43.20518 | 2025-08-04 03:15:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 32a9bf01-d571-3701-a921-35b1a13d9090 | -7.99275 | -43.18295 | 2025-08-04 03:15:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 573747cc-d434-3000-acf6-ae2b31c07552 | -7.99974 | -43.14718 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 40273d12-6389-32e5-9fd3-e4ccbfe623e1 | -8.01809 | -43.16565 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e94f169b-005b-36c3-b29c-5b2372c4a488 | -4.78573 | -37.75636 | 2025-08-04 03:15:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0ae2dc71-485d-3fb5-b69f-4171b7d4835c | -7.99837 | -43.15415 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.3 |
| 9b46f42b-8c4c-37d6-a98d-9193d409f004 | -8.00562 | -43.19213 | 2025-08-04 03:15:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6e218ad3-91a2-377c-8281-1bfaa83983db | -8.05125 | -43.10747 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ca113bbf-646a-34f6-969f-d4a9adc3f33a | -8.007 | -43.18506 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4d3f9e45-a8c1-3bae-a681-2d473b17b169 | -7.99292 | -43.2197 | 2025-08-04 03:15:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 29d0caea-c719-308f-b63a-3c08f23ca51b | -8.01534 | -43.17985 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ec00f093-c810-3919-a57b-0840ec9d3868 | -7.9955 | -43.1689 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ce6bca8e-4aa1-30f3-8e24-77c1f4a19ce5 | -8.00812 | -43.14169 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| b4a7e825-db61-3f25-aca1-04cf69dae2df | -8.04292 | -43.11285 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fea02d15-8480-363d-a69d-94a848c23c63 | -8.03457 | -43.11832 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| e7650eb1-a2e4-3740-abe9-9b6e9813c5ff | -7.99413 | -43.17591 | 2025-08-04 03:15:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4c587990-363b-3d09-b5f2-d6dcb82b6ecb | -8.0167 | -43.17285 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0aaa16d9-cebd-3247-84db-6a9bd2d4f61e | -13.68456 | -41.36823 | 2025-08-04 03:17:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2cb2aadf-215c-3eb0-b87e-688ea5f05271 | -13.69118 | -41.36526 | 2025-08-04 03:17:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5dbb2e7b-f206-3777-9549-0f831ac67e2f | -12.14321 | -43.38541 | 2025-08-04 03:17:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0320aa5-40a7-364c-8153-91240a1332f8 | -13.69091 | -41.36697 | 2025-08-04 03:17:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 35ad4967-7fdd-32c9-8ebc-3391d020529a | -13.68541 | -41.36411 | 2025-08-04 03:17:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b7ca3efa-8f6e-382a-93d2-eeeb136f8a79 | -12.13806 | -43.37669 | 2025-08-04 03:17:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d633dd4-26ce-34e0-b22b-875609129821 | -13.68431 | -41.36996 | 2025-08-04 03:17:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1b942bec-8e56-3e3a-bcfc-f8247d9ae2f8 | -13.68513 | -41.36583 | 2025-08-04 03:17:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb684520-c38a-3e4d-9e03-1b53cdddea92 | -13.69034 | -41.36931 | 2025-08-04 03:17:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e86cd1c6-364d-3fb3-872b-4387c77129fe | -13.69009 | -41.37105 | 2025-08-04 03:17:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6cc85ce4-ea6d-3a73-9db9-e12f0bd1d830 | -12.13659 | -43.38374 | 2025-08-04 03:17:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a777d27-c3cd-3110-9605-b9a986c69bea | -17.35868 | -46.08609 | 2025-08-04 03:19:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 405bf17c-2d84-3a6e-9969-861f73a3a291 | -22.56126 | -42.16324 | 2025-08-04 03:19:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9cca7778-ffc5-32f0-9b2d-18cf9e822ab0 | -16.42601 | -43.72523 | 2025-08-04 03:19:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5934a58-4dc1-3d6a-9bca-d45170c88808 | -16.42721 | -43.71987 | 2025-08-04 03:19:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ac366e1-f034-3509-a24d-7a00247951f8 | -20.25028 | -42.02023 | 2025-08-04 03:19:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| febc2437-26df-3a4e-9783-a056c2206d1d | -20.31741 | -42.89076 | 2025-08-04 03:19:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd201514-3bf5-3269-b83e-a55b9793b78f | -17.36595 | -46.08686 | 2025-08-04 03:19:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1363f6d-fdf8-3fa3-83d7-f4f1c8c334b8 | -22.56198 | -42.15997 | 2025-08-04 03:19:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9935dee7-528d-38f6-99b0-97974c68a28d | -21.87347 | -46.13982 | 2025-08-04 03:19:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 628f3fcb-7907-3f08-8d46-7654c97c9727 | -17.99372 | -44.33653 | 2025-08-04 03:19:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c068d103-643b-3305-a69b-65317e10506d | -17.37078 | -46.09805 | 2025-08-04 03:19:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eaff28ef-18d5-3ae7-80bb-7c9859dae989 | -21.25456 | -43.98645 | 2025-08-04 03:19:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 495c6b89-38d8-348b-990a-6b46db7628f5 | -16.42425 | -43.7236 | 2025-08-04 03:19:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 43563be6-b97a-3c57-90fb-851d8305c5f6 | -19.32928 | -44.16133 | 2025-08-04 03:19:00 | NOAA-20 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 587c457d-a52d-3748-8d61-b3dcb05fed23 | -19.09734 | -43.60518 | 2025-08-04 03:19:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4deeecb7-2289-3ddb-9ec8-92364f38e251 | -20.32298 | -42.89211 | 2025-08-04 03:19:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e5fbe0ed-1043-38e3-be84-6c2829ad6290 | -20.02896 | -42.43418 | 2025-08-04 03:19:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8269480d-f9b3-38ab-bef8-e891ac912c03 | -22.56054 | -42.16651 | 2025-08-04 03:19:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 22571292-8c8d-3e5b-807e-a9c9ed3aefaa | -15.27163 | -43.08115 | 2025-08-04 03:19:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 201c7ca0-6000-3b4d-a495-a5606eca439f | -22.46413 | -43.84516 | 2025-08-04 03:19:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6cb61da6-d8b8-333e-8da1-ab5e5322fce0 | -20.32064 | -42.88836 | 2025-08-04 03:19:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8518fd0c-d421-32c8-aec4-76f28f7089c2 | -22.4651 | -43.84094 | 2025-08-04 03:19:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 692a0e3c-00d3-324f-bb47-cf8dc5efc15c | -20.4617 | -42.02495 | 2025-08-04 03:19:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4e9ebcb4-12a8-3f99-a966-73488cab477f | -21.25136 | -43.9815 | 2025-08-04 03:19:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 227a6baf-e948-3bbb-b2f9-c2bec3d0186b | -18.606 | -43.88308 | 2025-08-04 03:19:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2afcdae-edb3-33db-a8d2-f14ecd82bf16 | -22.55762 | -42.15538 | 2025-08-04 03:19:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 200bdf41-b5a9-3a20-80c2-1f23b5fa4f59 | -22.56563 | -42.16781 | 2025-08-04 03:19:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| cad140c7-4804-35fd-bbea-b28031224a77 | -20.3184 | -42.88635 | 2025-08-04 03:19:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3e229f99-6bdd-38de-bf15-da4e2ad02ecc | -20.31965 | -42.89291 | 2025-08-04 03:19:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| daddaf95-cbaa-3bc4-8a10-3cad3f4c7a57 | -15.27273 | -43.07595 | 2025-08-04 03:19:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 541ff07f-ec88-3115-9b6b-06546eadf7b9 | -19.32821 | -44.16603 | 2025-08-04 03:19:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa8b2d3b-06aa-35b0-b78c-249b951a641d | -21.24988 | -43.98008 | 2025-08-04 03:19:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2e7ff719-1a56-38f3-b569-9ef4bb40c0e6 | -20.24945 | -42.02409 | 2025-08-04 03:19:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 43d680ee-052f-3906-a486-d08d41ac6b8b | -15.27005 | -43.07681 | 2025-08-04 03:19:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 6.3 |
| cb8c0bd0-9406-3b82-a707-989018f57969 | -20.32524 | -42.89421 | 2025-08-04 03:19:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4a3bda68-f47d-3ab0-a4f4-4d0f1fa63614 | -21.25028 | -43.98622 | 2025-08-04 03:19:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 44100758-443a-34dd-b2a0-3b1e84de9399 | -22.56635 | -42.16455 | 2025-08-04 03:19:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7d152afc-62f8-3924-97d7-c29d898f374a | -21.25569 | -43.98162 | 2025-08-04 03:19:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f1b7facf-3b85-3fee-a168-c27b06c17796 | -20.46267 | -42.0204 | 2025-08-04 03:19:00 | NOAA-20 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 03ee2108-4cab-36a5-89d2-876db9d528e4 | -7.994 | -43.1534 | 2025-08-04 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 474cc1f0-6345-3336-83d6-14ddd1386276 | -4.7346 | -44.4457 | 2025-08-04 03:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e3c39ed8-748d-3e53-a378-4655c1516960 | -8.0129 | -43.1513 | 2025-08-04 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |
| 3e0d6586-7f71-36bb-b219-b178625169c2 | -8.0132 | -43.1278 | 2025-08-04 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 7f72e52f-fddd-3ec2-b7ad-021489e29657 | -6.6329 | -59.9649 | 2025-08-04 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 6f119e58-2f51-32ac-a8bc-589da043d58e | -22.91487 | -43.70733 | 2025-08-04 03:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 16f961cb-e960-3f07-9aa0-2b58a2caed76 | -22.90935 | -43.7058 | 2025-08-04 03:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 24d1613d-af06-3acf-acdf-3d7884c2e1d9 | -22.75432 | -43.73774 | 2025-08-04 03:21:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39219b96-6b29-3644-b8db-5662f361240c | -4.7346 | -44.4457 | 2025-08-04 03:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8d7f274b-52f6-350b-8e13-6e1d501d70c9 | -7.9943 | -43.1298 | 2025-08-04 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 0dffe4b7-115e-363c-9b94-5d4e9cfdb79d | -8.0132 | -43.1278 | 2025-08-04 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| c669d689-ff02-3c92-820c-ea7fb23cfb17 | -7.994 | -43.1534 | 2025-08-04 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| e3eebba4-d8d7-363c-b90e-a7ef8776f610 | -8.0129 | -43.1513 | 2025-08-04 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.4 |


[Clique aqui para ver as próximas entradas](README7.md)
