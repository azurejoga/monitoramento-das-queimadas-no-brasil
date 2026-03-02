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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b84049ab-11fa-3a14-b438-54fa44d0d93b | 1.4864 | -59.9117 | 2026-03-02 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.6 |
| e070b11a-b98d-3da0-a28a-ac6922ae4151 | 1.5046 | -59.9306 | 2026-03-02 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.5 |
| e171953e-106f-3b82-b22b-7a7425073464 | 1.5047 | -59.9116 | 2026-03-02 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 4e60b875-75d7-32ed-bdb6-2de8b58c0c64 | 1.4864 | -59.9117 | 2026-03-02 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 81d04f6f-4846-33f8-8b0e-a28c567f5417 | 1.5229 | -59.9305 | 2026-03-02 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d6429cfa-98c6-35a4-aa67-b1d81c81589a | 1.5047 | -59.9116 | 2026-03-02 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 362099d6-f790-3686-9675-4cbab770893d | 1.5046 | -59.9306 | 2026-03-02 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.1 |
| e10f2364-b0fb-3e2d-80b7-13edbb04d489 | 1.5047 | -59.9116 | 2026-03-02 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 092a2280-a2e3-366f-ac06-574088a43c5b | 1.4864 | -59.9117 | 2026-03-02 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 7fee51a5-427a-3d77-a65c-8441713cec85 | 1.5046 | -59.9306 | 2026-03-02 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.5 |
| fbd56151-e025-3ffd-8094-a8ad26110627 | 1.4864 | -59.9117 | 2026-03-02 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 337001ef-7e02-37d2-ae7d-9c359ef33abe | 1.5046 | -59.9306 | 2026-03-02 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 6d970e80-2084-3404-b6e5-cefcf656705c | 1.5047 | -59.9116 | 2026-03-02 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 64850633-bc29-3255-b43f-d336ce192c29 | -24.33587 | -49.73029 | 2026-03-02 00:39:00 | TERRA_M-M | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5145c815-4355-3937-85fd-fc3e3f18f9ff | 1.5047 | -59.9116 | 2026-03-02 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 131.1 |
| dcac122c-7a76-3b2a-933d-ca936937b24e | 1.8689 | -60.4024 | 2026-03-02 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9a7aa51e-27ef-3f71-bd40-c7f7bc7b20f7 | 1.5046 | -59.9306 | 2026-03-02 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.5 |
| f995b8b7-f2fb-3ea0-9209-2b3d88a281aa | 1.4864 | -59.9117 | 2026-03-02 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.7 |
| cb6f5c2d-e577-3579-afe4-9c2ed368fb63 | -22.90134 | -51.20135 | 2026-03-02 00:41:00 | TERRA_M-M | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fb84cd58-5384-3083-ac99-cf34cf7d1ea0 | -21.09586 | -48.7434 | 2026-03-02 00:41:00 | TERRA_M-M | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 7c974dee-7ce5-3819-8df8-6d97ac1e77b0 | -22.57895 | -54.99648 | 2026-03-02 00:41:00 | TERRA_M-M | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 15ddb00f-b4fe-39ce-acd9-65980dc20f4c | -21.37827 | -48.64547 | 2026-03-02 00:41:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| be60acfa-983d-36f3-b758-11f1bc6cfbbb | -21.3762 | -48.63252 | 2026-03-02 00:41:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3bf5833e-a7c1-3f95-8362-e7c36b404daf | 1.11508 | -59.19744 | 2026-03-02 00:47:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 10f80dde-3625-393e-8655-02b0fca09436 | 0.45928 | -60.40007 | 2026-03-02 00:47:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3ed2e960-2d03-397d-b55b-27ae9f66a91c | 1.49205 | -59.90427 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.8 |
| f5d1c5ec-b7eb-3975-86af-bddfba9d1071 | 1.45592 | -60.06627 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e010932b-65a9-31b9-b197-7e159e71a76d | 0.64702 | -60.66039 | 2026-03-02 00:47:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e610ce48-6cd1-3264-8ca5-b08673a30962 | 1.49053 | -59.91492 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 352b5843-bc17-31f3-860d-6811f4f02f5f | 1.07911 | -59.25229 | 2026-03-02 00:47:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 481d01f0-5df2-34f3-a494-f486edf13d74 | 1.50974 | -59.91748 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 037205cf-059c-3ee6-8947-46ec134bb14a | 1.48597 | -59.91919 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.7 |
| dcb9a2d3-7909-365b-bfa7-a163b241e23b | 1.47492 | -59.92832 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5b6e0d4e-2267-3154-bf6a-c6475f14674d | 1.48904 | -59.92536 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 896b293c-0d35-34b5-9337-e4d12313cdfe | 1.48454 | -59.92961 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 40fc1d26-defe-358d-bf43-23a585f8e966 | 1.49864 | -59.9267 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 092e9675-bce7-319b-ac04-e55000b35fab | 1.50013 | -59.91621 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.1 |
| dd4d8ed7-9a61-389f-bbc2-4468f2c80262 | 1.11374 | -59.2072 | 2026-03-02 00:47:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 793964e8-96cb-3af8-b132-20f265c06604 | 1.09484 | -60.17496 | 2026-03-02 00:47:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 9cc2620c-8249-3313-899e-8db7ee1f6f9d | 1.48742 | -59.90863 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| eb7af750-579a-3800-b821-2b69c2ab557b | 1.50825 | -59.92802 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 2527c190-e676-3f8d-8059-59f447e7b464 | 1.07774 | -59.2621 | 2026-03-02 00:47:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 44b58534-a602-3b14-bb35-a4701f1db3f6 | 0.92174 | -60.53058 | 2026-03-02 00:47:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d37f93be-8691-35e6-8cdc-27841b0efefd | 1.51784 | -59.92948 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a3970c76-6d20-3722-ac10-168b70792f7c | 1.10465 | -60.17634 | 2026-03-02 00:47:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9a3941b8-06b4-3b54-b0c8-838837e9e641 | 1.45445 | -60.07694 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 99a35d8b-638a-3890-b4fa-64deb59f83ad | 1.50163 | -59.90565 | 2026-03-02 00:47:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| bf80c9af-a06d-39a8-9f3e-95002e6cf145 | 1.09328 | -60.18594 | 2026-03-02 00:47:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a473464d-119d-30f4-899b-a18e081ba26b | 3.1903 | -60.691 | 2026-03-02 00:49:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7e10baa8-f6be-3847-b42a-136c34273d98 | 1.72262 | -60.29481 | 2026-03-02 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 480c26e0-2085-366a-8080-4d34bdbf389c | 1.87154 | -60.38932 | 2026-03-02 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b2ccdea6-14f9-34bc-92c5-20ce73e20439 | 4.08537 | -59.88376 | 2026-03-02 00:49:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3655ca4a-8d38-3224-81df-69f5d1bd495c | 3.6162 | -61.66066 | 2026-03-02 00:49:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3f3e2b2e-98c5-3be2-85d0-6b7e7a6b74e1 | 1.78077 | -61.174 | 2026-03-02 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5d20ceef-7820-31bf-98f2-24172c87300e | 3.17221 | -60.6768 | 2026-03-02 00:49:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0a22c8b0-9b78-36cb-abab-93a00fffd989 | 3.61799 | -61.64799 | 2026-03-02 00:49:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6ca043c3-71e8-386e-835f-f8531b4f2357 | 1.72105 | -60.30583 | 2026-03-02 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| dc7bb6d5-571b-3711-8285-4848b20908f2 | 4.25062 | -59.90332 | 2026-03-02 00:49:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1bd7bcc4-5af5-3f06-ae96-91372f10e330 | 1.86015 | -60.39904 | 2026-03-02 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 75f07849-78d9-3ded-8808-cb33cad740da | 3.5801 | -60.33074 | 2026-03-02 00:49:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d69d97a2-e9b9-3882-a617-0719d311071a | 2.21928 | -60.7579 | 2026-03-02 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8d76cce6-0ad3-3f53-9242-f6b4345d7462 | 3.19188 | -60.67981 | 2026-03-02 00:49:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a60cef67-32d6-3359-b6ef-b8a2c548da05 | 2.8567 | -60.80885 | 2026-03-02 00:49:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 52998fd0-843e-377e-8346-79e63c6317f5 | 1.8617 | -60.3879 | 2026-03-02 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8c4d5150-5e07-353b-85df-08fe88401943 | 4.24925 | -59.9132 | 2026-03-02 00:49:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b108715c-3994-385e-8250-832e7c88ef7b | 3.16844 | -59.91655 | 2026-03-02 00:49:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f754b111-0476-33da-90fc-f15980d15c35 | 4.25653 | -59.91007 | 2026-03-02 00:49:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 488ec115-eb84-3af9-9c42-080b3deb14e5 | 2.83342 | -60.82889 | 2026-03-02 00:49:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fed1e9cb-9168-326b-b9b5-a521992f6dac | 2.23096 | -60.74776 | 2026-03-02 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0cae4f97-2c56-3d98-84a3-3e3b2a739991 | 4.25792 | -59.90033 | 2026-03-02 00:49:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 28ee0fad-e36f-31df-a525-df6ec9820a96 | 3.1805 | -60.68926 | 2026-03-02 00:49:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| af9f33ba-e39d-39cc-a8d3-92f8a443d642 | 1.51223 | -60.32552 | 2026-03-02 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c3d49a7a-0298-36b3-8089-68f594937567 | 2.834 | -60.82325 | 2026-03-02 00:49:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a1b8dff1-11af-39f2-9dae-27808d670ea5 | 2.85506 | -60.82028 | 2026-03-02 00:49:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a1123dc5-2efe-3417-9fed-37c784f320de | 3.46214 | -60.79354 | 2026-03-02 00:49:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b565c82b-62e1-3b6a-b420-5238cd7ae611 | 4.06746 | -59.89576 | 2026-03-02 00:49:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e2b00ae0-d980-367f-8839-5b54d81daa44 | 2.22093 | -60.74638 | 2026-03-02 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 80a2548a-7102-3825-b1b9-d849f890a6fc | 1.87 | -60.40043 | 2026-03-02 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 0f29e935-fe12-390d-b021-b38e6f109ecb | 4.07893 | -60.33576 | 2026-03-02 00:49:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cc5ad6fe-5df7-38b3-9c24-6529abd71c3f | 1.78257 | -61.16153 | 2026-03-02 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.2 |
| fd2acdbc-9729-3e50-ae45-154afac73386 | 2.8536 | -60.8259 | 2026-03-02 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 5641dcea-5b29-32e5-83b9-f7a0e0f897e3 | 1.4864 | -59.9117 | 2026-03-02 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.8 |
| f881d5d2-cf4e-3a9d-a46c-a3d05481ed0b | 1.5046 | -59.9306 | 2026-03-02 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d89d9379-1f23-38ae-aa02-54e7ad71ada3 | 2.8536 | -60.807 | 2026-03-02 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 101.9 |
| c1b7b9d3-983f-333b-8c30-626d46c9d024 | 1.5047 | -59.9116 | 2026-03-02 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 97d267bf-4cae-31cc-af41-2d36c2c7d71b | 1.5047 | -59.9116 | 2026-03-02 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 210fbad3-0cee-3d37-844c-94c6263126fd | 0.4648 | -60.3925 | 2026-03-02 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.2 |
| bce8dc72-4ca1-34fc-9822-9e5dd238113d | 1.4864 | -59.9117 | 2026-03-02 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 78c482c0-ea8f-3c58-9fe7-39fefb8ab42b | 2.8536 | -60.8259 | 2026-03-02 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.8 |
| cb069e5e-8174-353b-95ea-90d8bb42db1c | 0.4466 | -60.3925 | 2026-03-02 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.0 |
| cb534846-568c-37eb-932d-40260f4fc483 | 1.5046 | -59.9306 | 2026-03-02 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 0ebe45a0-e040-3ea9-be15-87a7e9c320f6 | 1.5047 | -59.9116 | 2026-03-02 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 77ecb2fa-d4fb-389c-b934-b50f37811ced | 0.4648 | -60.3925 | 2026-03-02 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 17036863-2f4e-382b-8e90-2d019edcfd28 | 1.5046 | -59.9306 | 2026-03-02 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 75759aa1-6f0b-31b4-9c0b-e8c68aa67523 | 1.8689 | -60.4024 | 2026-03-02 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 81e7476b-1317-3497-99e9-778df274e96e | 2.8536 | -60.8259 | 2026-03-02 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.3 |
| ed8db1ed-1db7-3e32-a450-bd11d78b127a | 1.4864 | -59.9117 | 2026-03-02 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0701f6cd-39a1-3038-91fe-a3bbd63d95ba | 1.5047 | -59.9116 | 2026-03-02 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 55236145-ea73-35e9-99c2-59b824ab160e | 2.8536 | -60.8259 | 2026-03-02 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2a3f8c92-9422-3a38-8d72-a782fe046e20 | 1.4864 | -59.9117 | 2026-03-02 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |


[Clique aqui para ver as próximas entradas](README2.md)
