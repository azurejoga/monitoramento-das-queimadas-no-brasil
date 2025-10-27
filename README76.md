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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b38590e9-0a20-3cc3-ad74-f648935f5517 | -4.4415 | -43.658 | 2025-10-27 13:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 28306a92-06b0-3439-8f8a-7af0107bf247 | -4.8744 | -43.2595 | 2025-10-27 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| c024afde-4c83-34ad-ad29-30a0a1447cb3 | -3.7096 | -44.3409 | 2025-10-27 13:50:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 7e3c67e6-1dd0-3a38-af91-5331d94e7b43 | -4.9138 | -42.9998 | 2025-10-27 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| c30f683e-fb81-3e6f-a8fe-962beeee61bd | -3.3261 | -42.8778 | 2025-10-27 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| ede81a3a-b8b9-3e99-8d45-a36ce3ab7325 | -4.4066 | -43.3118 | 2025-10-27 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 980f7133-247e-3a62-a529-b3a99154cb51 | -5.7758 | -42.9842 | 2025-10-27 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 3c3db722-8ac4-3fc0-a6e9-178280d1e36a | -6.1735 | -42.6221 | 2025-10-27 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 5ecf615b-4ea8-380a-be06-9853f885978b | -5.6619 | -41.1099 | 2025-10-27 13:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 189.7 |
| bb4c84b6-2031-3965-bdda-15483f6d9ec0 | -4.9146 | -42.906 | 2025-10-27 13:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| fe66d8e1-b45b-389b-aae7-3bdb057ec696 | -3.7661 | -47.5727 | 2025-10-27 13:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 7ae77039-08e2-3540-9f54-5943e6dc4508 | -2.9961 | -41.6859 | 2025-10-27 13:50:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 124.6 |
| 290d27fa-e351-3e50-8db6-38bce1992c93 | -6.1923 | -42.6205 | 2025-10-27 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 4d47e2d8-1121-3c9f-a0a7-504574e1bb43 | -3.0146 | -41.709 | 2025-10-27 13:50:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| a073995d-6c44-35ce-89bd-f3fd1d29197b | -3.5834 | -43.5877 | 2025-10-27 13:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 3add4330-4b39-3095-bb7c-28a70eab0370 | -5.9656 | -42.7574 | 2025-10-27 13:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 1a8e35dd-b896-38dc-bc40-89fb62349f99 | -3.0148 | -41.6851 | 2025-10-27 13:50:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| dce0c644-00d3-3e31-acb1-adc8e0310fab | -6.4615 | -45.7536 | 2025-10-27 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8ac58105-39fd-369a-97fd-b29c898183fa | -12.3424 | -47.1013 | 2025-10-27 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e1ba9fea-36da-386d-b093-ffaf9cbd3546 | -4.3877 | -43.3362 | 2025-10-27 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 11683a81-a18a-3db3-bb98-d8d7d9d1beec | -3.3448 | -42.877 | 2025-10-27 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 188.3 |
| a9438d22-813c-37bf-bf19-24fbefa1fd4b | -14.7816 | -44.9599 | 2025-10-27 13:50:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 128.3 |
| b74f3228-1cac-3ad7-8457-8585b6341d3d | -4.8557 | -43.2607 | 2025-10-27 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 578163e6-0b2a-39bc-a7d6-c246729dfb49 | -4.388 | -43.2896 | 2025-10-27 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5154e7b1-1659-3589-939b-4424422fe11d | -5.9653 | -42.781 | 2025-10-27 13:50:00 | GOES-19 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 7eb3bb83-ee00-38e4-90ee-026e44c9a2be | -3.691 | -44.3418 | 2025-10-27 13:50:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| b16d2ac4-ac2a-3001-87af-d6cef8259538 | -6.1925 | -42.5969 | 2025-10-27 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| b7f4f517-af87-3b25-9f0d-1c29aa8a0d9f | -3.3448 | -42.877 | 2025-10-27 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| a520e3cb-2dff-38a9-8d27-d0b938f93c69 | -3.3261 | -42.8778 | 2025-10-27 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f843752f-3037-313b-a9a0-25f7c2d75093 | -2.9961 | -41.6859 | 2025-10-27 14:00:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 123.5 |
| 322dc947-eb34-35cc-8632-c29920647445 | -6.1737 | -42.5985 | 2025-10-27 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| e6bf65fe-cfbc-3093-b00e-0120823963f7 | -7.0835 | -45.3865 | 2025-10-27 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 8afe8041-cab9-34f6-b839-4d1db987f0db | -4.8557 | -43.2607 | 2025-10-27 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| b5a714e1-974e-3fb6-80c7-a60f47b8f1d8 | -4.9138 | -42.9998 | 2025-10-27 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 67cdbf57-6dc9-3e53-879f-dea3591c5c7f | -6.1925 | -42.5969 | 2025-10-27 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| f60780c1-906c-36ae-8a47-e87bc4b96d12 | -14.3599 | -51.5281 | 2025-10-27 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.3 |
| b4709709-5c2a-365c-96af-b3ea63cb4461 | -3.0148 | -41.6851 | 2025-10-27 14:00:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| b5ceadb7-48b9-37a0-9584-cd9000fb7984 | -7.0695 | -44.9335 | 2025-10-27 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 80cb6ebc-08e3-39a1-b22c-3e1a8529b14d | -5.6431 | -41.1114 | 2025-10-27 14:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 207.9 |
| f4b2b90c-ec7f-3981-848d-568e3e7b87e4 | -14.7816 | -44.9599 | 2025-10-27 14:00:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 18b3f796-d1d4-3753-96ac-789f7f39c810 | -7.257 | -44.9623 | 2025-10-27 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| dc182120-1ceb-3eac-8fe9-0f6dfdfc1790 | -3.3447 | -42.9004 | 2025-10-27 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 144.6 |
| a24f2890-e9e4-3948-8a78-9cd44d77d3f4 | -7.2567 | -44.9851 | 2025-10-27 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 62144a4a-9f1c-3b3d-acdb-c91578c4194e | -12.3424 | -47.1013 | 2025-10-27 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| a0fc3dce-b67c-39ce-80e2-3844038d9e85 | -12.5356 | -44.9274 | 2025-10-27 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 211.3 |
| b6970c6c-12c4-3d90-b8a4-2818f3d058bd | -12.2836 | -47.1769 | 2025-10-27 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 7389e7ba-f0b5-3be9-9b36-3c354f746ce8 | -5.6619 | -41.1099 | 2025-10-27 14:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 153.1 |
| 823203a9-a90e-39e7-b147-e1f8bdceda78 | -4.4618 | -43.4248 | 2025-10-27 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 3f027b0a-7140-3566-9069-c5f09d8a2621 | -6.1735 | -42.6221 | 2025-10-27 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 362e1227-e8d6-3649-a216-62d7942dcf7f | -14.3982 | -51.5443 | 2025-10-27 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 60508e45-8b1a-369d-896a-a29d05882266 | -4.8744 | -43.2595 | 2025-10-27 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 295813e0-e8cd-30b3-8601-13d01531a33d | -4.4415 | -43.658 | 2025-10-27 14:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 66daf76c-8762-33fa-bd16-474ffb1dd4ad | -5.9653 | -42.781 | 2025-10-27 14:00:00 | GOES-19 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| b222368c-542c-388d-9f05-8fd01402a77a | -4.8558 | -43.2373 | 2025-10-27 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 4bbb02df-6837-3461-b6a1-0ad42b0fa454 | -5.7758 | -42.9842 | 2025-10-27 14:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 118.8 |
| 94e499ac-0c1b-33a1-8096-ead0e956347a | -2.2591 | -56.8365 | 2025-10-27 14:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| aca55f5e-2417-31d1-a256-58f89621ebf7 | -4.8179 | -43.3097 | 2025-10-27 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 48d980b7-4a9b-37da-b6ec-a1068721aa7d | -3.5834 | -43.5877 | 2025-10-27 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| dac51d3d-3a03-33ad-9ef2-a40783c16b6d | -4.9146 | -42.906 | 2025-10-27 14:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| ad0c20a6-c5ce-348b-84ca-841292f41932 | -4.8951 | -43.001 | 2025-10-27 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 4eedd963-c89e-38cc-bea0-7fc51d1ad243 | -14.781 | -44.9835 | 2025-10-27 14:00:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 88ad5705-5aa8-36f0-be23-051f246392c1 | -3.0146 | -41.709 | 2025-10-27 14:00:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 87550771-3015-3823-9575-82f35e9bae75 | -4.3877 | -43.3362 | 2025-10-27 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0f397207-24ff-3e96-8494-3e8926d93fa2 | -14.2491 | -48.1148 | 2025-10-27 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 146.7 |
| afabcba7-c4be-3503-be1b-c6e4db229fed | 1.1502 | -51.0603 | 2025-10-27 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 5472c905-31ec-3365-bfdc-8147ca1da5d9 | -16.1505 | -45.0921 | 2025-10-27 14:00:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 104.5 |
| bc7cadcd-0b90-37e1-b375-0a42d965b319 | -14.2487 | -48.1372 | 2025-10-27 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 60cc8b25-be16-32e4-aa58-54b2893af560 | -4.4066 | -43.3118 | 2025-10-27 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f27dc022-c9b4-365d-afc0-970373769368 | -4.914 | -42.9764 | 2025-10-27 14:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9695a0fe-2488-386c-986d-98a3fbb7a5a7 | -5.9656 | -42.7574 | 2025-10-27 14:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 05a3235d-25c3-3add-b757-cf6a83295846 | -4.2579 | -46.0519 | 2025-10-27 14:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 44d58d9e-5997-308f-b574-2a95c73ae954 | -6.5864 | -42.6804 | 2025-10-27 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 2bb5f4e7-7bbb-3860-8ad5-4b69699798d8 | -6.1923 | -42.6205 | 2025-10-27 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 44c83cd0-1c64-32d5-bb97-36a8491e01de | -12.5361 | -44.9041 | 2025-10-27 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 72f63a20-79d2-3410-8869-4d81d3e7c243 | -6.4312 | -43.1411 | 2025-10-27 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| cccfec90-0768-3bff-bb9a-121918141b32 | -7.0693 | -44.9563 | 2025-10-27 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a5183a8c-6df0-32cb-8c7f-99f2ae6783be | -4.4602 | -43.6569 | 2025-10-27 14:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 3525870e-1104-37d6-a705-5bea65b97403 | -6.5605 | -41.5859 | 2025-10-27 14:00:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| e7ae4fd0-52c8-3b51-83e3-8abde21f3120 | 1.602 | -55.7262 | 2025-10-27 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d164524e-e326-3ead-8893-efd0d3c1698c | -7.011 | -46.9581 | 2025-10-27 14:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 860caf58-e1a2-39bd-bcae-ab5c92775206 | -4.8951 | -43.001 | 2025-10-27 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 19bc5153-6122-31a5-9866-b371012b4234 | -6.1925 | -42.5969 | 2025-10-27 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| eb1df7ed-137b-3e85-aa59-76beef101bb5 | -3.3261 | -42.8778 | 2025-10-27 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 1582495f-6ad2-3c0a-98c8-950d40bd1b6f | -6.5605 | -41.5859 | 2025-10-27 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 207.9 |
| 7edb674c-7856-3681-99f5-87dde09f3bdc | -3.6253 | -42.7933 | 2025-10-27 14:10:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c440c83b-4398-33bf-94c1-6614605e0e1a | -4.4066 | -43.3118 | 2025-10-27 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 32156f92-cd5f-369e-8065-c8be2e790715 | -7.257 | -44.9623 | 2025-10-27 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 8863fcd2-60d0-3081-8ec8-4e1a36042349 | -7.6922 | -46.3443 | 2025-10-27 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 2bbe28e6-ac13-3ca4-b131-914ca85e155d | -3.5834 | -43.5877 | 2025-10-27 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 378469f5-def7-3e2b-966d-8770bba9fcf7 | -4.8744 | -43.2595 | 2025-10-27 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 0f376257-3dd8-31b1-8abb-9362a6d06c19 | -6.2304 | -42.57 | 2025-10-27 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 47734d40-e502-36d5-bf1f-3762125f078b | -4.8179 | -43.3097 | 2025-10-27 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 61c2735f-b91d-367f-b80d-0e448dad694b | -2.8971 | -42.8492 | 2025-10-27 14:10:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 34b4fa71-2e79-3ba0-90e0-6c9990aded55 | -7.5429 | -46.2683 | 2025-10-27 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| afe1f112-0a4a-30ac-8b2d-2c4f3ebad314 | -3.0148 | -41.6851 | 2025-10-27 14:10:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |
| 1201655a-e8ad-39a5-8806-356034521c1f | 1.6203 | -55.7062 | 2025-10-27 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| bdbc35a0-a8d6-3085-8949-c1d702cfc365 | -7.0883 | -44.9319 | 2025-10-27 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| c1338b43-99bf-3768-b1e6-20b8074e9aed | -8.0444 | -45.1606 | 2025-10-27 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 92cf7eca-25b9-3cb8-b2b9-b01b9a5b2a15 | -3.0146 | -41.709 | 2025-10-27 14:10:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 108.7 |
| 234a8540-37f0-386a-a68f-50624aee7056 | -4.3879 | -43.3129 | 2025-10-27 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 263.3 |


[Clique aqui para ver as próximas entradas](README77.md)
