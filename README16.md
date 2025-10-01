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
| 9bbed31b-72e3-3278-bde5-ecdfcdc13590 | -14.70088 | -42.31831 | 2025-10-01 03:30:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9bc5f785-a2b2-3831-b88c-cf89eb9f3a2e | -11.52428 | -43.55562 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da27e032-8513-34f1-9160-159129863f58 | -11.38096 | -45.05885 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e4f00616-5b4f-3ab6-8652-bade597a6e2b | -12.8732 | -45.26739 | 2025-10-01 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e485c9a-1d83-36d2-b898-ad4aecece998 | -11.46748 | -45.09811 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| fba00062-9694-3f8e-9c43-b39db9b2f487 | -9.92669 | -43.6659 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a677ca3f-6218-3066-a81e-609ceadc28d7 | -13.13677 | -47.42067 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f536e0d6-d935-35f4-bb20-7cdbcef5beda | -13.29005 | -47.24413 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 950c78b7-4613-3dbf-a186-8d1b3f495e28 | -14.70588 | -42.31923 | 2025-10-01 03:30:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c346b0a-487c-3da2-b965-245441b73b5d | -13.76801 | -47.96962 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 709708cb-330c-3442-88f8-225679b6d187 | -13.37346 | -47.32112 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15f15ad1-f0e8-3245-86e1-1a3431986c14 | -11.67906 | -44.29698 | 2025-10-01 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 336026f6-0c77-35ce-9687-bb41a0ce7b39 | -13.14517 | -47.41559 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2379c117-0994-321f-b861-7d54a7cd4185 | -11.13761 | -43.38277 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 513eebd5-20ca-316b-8a1e-808cf7df0773 | -10.8298 | -45.39005 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d641f16-4752-3fc7-8265-e48ed6b6617a | -9.85693 | -44.60736 | 2025-10-01 03:30:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8bf20ff0-e203-30c6-af20-60270c0686a2 | -13.66598 | -48.07981 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 866113f7-44ee-396e-b443-8e18c5437897 | -11.42721 | -43.50574 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58a026bf-f3cb-3cae-8a22-963309d80e5b | -11.47364 | -45.1 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74bf0a8a-d127-3a2f-92da-a0580740d2ea | -11.80711 | -44.99701 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11e76a22-864c-3426-81e6-fbed369facf2 | -9.26142 | -45.69744 | 2025-10-01 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2e35b136-4b25-3f29-8add-fff0b43c0995 | -11.45598 | -44.97717 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9c0d278-16be-3866-90d9-36bc0c62a98c | -11.5247 | -43.55841 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ee4fd90-18ae-3ffc-9761-48089e2f5fdb | -13.75763 | -47.93417 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb03bd6d-6ec5-3948-aa11-b76bf2f43077 | -9.93852 | -43.66825 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 318dcc11-f636-3d72-bdbf-c7c0273349a9 | -11.83028 | -44.96798 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5508923-6078-3470-9b50-8d9a33e0ce42 | -10.79579 | -45.35868 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89b86eca-5cc0-3cd3-8768-28a506384e83 | -13.32582 | -47.8783 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0da86e90-8faa-3e37-8fc8-326fa1fe15b3 | -12.58258 | -41.28435 | 2025-10-01 03:30:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 245ce20c-dec6-3cbc-a113-a4b1d27782af | -13.30472 | -47.20966 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5eb365db-5961-3120-80a4-b31fecfd04a7 | -14.0192 | -46.32935 | 2025-10-01 03:30:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4ae1ad7-e42a-3256-8a38-8fea73f4d823 | -8.54675 | -44.64809 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 19e4d563-f2d9-3dcb-bef2-697a1e4f0ad2 | -11.44791 | -43.51437 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e05e9e45-28b5-333a-84b7-578618fd59fe | -11.49706 | -43.51238 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1454d373-fb2a-3631-ae52-581f5b24797a | -13.13527 | -47.42752 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fd2025e-01e7-3098-b852-2ad1a9ca9e9c | -10.90501 | -46.54571 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da272156-57a9-335a-b8f4-98d9150fcc0e | -8.5504 | -44.73299 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3f88ff1-e5e0-353a-8efa-16a51715d6ca | -10.90567 | -46.57298 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 369add00-f86a-3195-b3a5-2b2b1bd3f6f4 | -11.46129 | -45.09634 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 58e735f0-a550-3241-a7fa-5ffd538614a3 | -10.82449 | -45.38322 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 056edcfb-ba83-3313-bf8d-487f9a579d93 | -11.45933 | -45.09208 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e1827bfb-cfe8-3a5e-8a8b-ef2a05f1cf08 | -13.98042 | -44.90974 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36d6347e-b6f8-32e6-a2ba-634c0f77ff23 | -8.53431 | -44.71225 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84021ede-74bf-325a-ab99-62b842e97615 | -14.0538 | -45.01983 | 2025-10-01 03:30:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13f5eaa2-4283-3256-8b89-9d8c432a09b8 | -12.18306 | -40.4072 | 2025-10-01 03:30:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d6a031d6-b398-3343-b01d-4d92cc5e8d2d | -11.20779 | -47.20427 | 2025-10-01 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3a8b29c-c6c9-320c-9c4d-3fd624854cc9 | -14.05838 | -44.37414 | 2025-10-01 03:30:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97f3e33b-20d1-3db4-a0cb-1dbbca818fd1 | -13.13802 | -47.42527 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ceb2904-e96f-374d-aec7-afbfc8de904e | -11.47265 | -45.10489 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6eb56cdb-beef-30b8-9639-8aeec64384c3 | -11.9663 | -46.59873 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6054d08-a719-3336-a518-a6de81c58872 | -11.75975 | -46.86688 | 2025-10-01 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ad5629ab-c589-302c-ba0e-79873cde18f8 | -11.42069 | -43.50865 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef63b4bb-2080-343d-89fb-64deeeea9df9 | -11.83542 | -44.97445 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4fbfbbb3-7f84-3b95-b36f-155bbef68336 | -11.46506 | -44.98214 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8f68961-303c-3420-9e54-ecb43b110540 | -9.98044 | -40.50669 | 2025-10-01 03:30:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dc400f68-0193-3db1-813d-3b64c7cf6d56 | -11.9595 | -46.5973 | 2025-10-01 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75e3d782-4141-3934-b857-eff7aa44d8b5 | -9.32623 | -45.69904 | 2025-10-01 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dd5b801-5a91-30ad-94a2-c8558aae0d5b | -13.76363 | -47.9751 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| de33b5ee-61fc-3eb6-a164-e3ec75308275 | -12.86992 | -44.60076 | 2025-10-01 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6333de12-d359-39a1-a59d-106c880c35f5 | -12.39838 | -44.7637 | 2025-10-01 03:30:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5601b87-dd94-3541-bf99-40ef2281aeb4 | -9.93511 | -43.65409 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aded3bbd-e2d2-33c7-8198-201ee1f97741 | -13.36897 | -47.30854 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9a03f972-95e6-397b-9240-097ab8186544 | -14.18145 | -46.10781 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 09c6fb9b-7cd6-39b9-9f90-faddf1df4f44 | -10.90841 | -46.55999 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f2bdcc78-8632-3059-97ff-a9025bdbe051 | -11.81713 | -44.94611 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9683c11a-17b5-3d94-a1ad-bbf4254377ed | -11.45692 | -45.02187 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5cf08c8-6548-3dca-93cb-5b28d73744dd | -11.82513 | -44.96153 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cff08db-8078-3b4b-ad4a-c29b21bf909d | -11.73734 | -46.8767 | 2025-10-01 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c2757ac0-fd19-3f18-a69a-9007e91fefa8 | -10.90789 | -46.56682 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 37e59123-8fae-3a4e-a416-ad80eb2f036b | -13.32322 | -47.83641 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c32a00a8-6f38-36a9-9fcc-a78231782ce5 | -14.05738 | -45.04157 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d32e357d-7198-3c84-9f5b-90d83f3ebf15 | -8.58351 | -44.73495 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 730ae8cc-cd29-3d8c-86a1-c9518ff43de8 | -11.67994 | -44.29248 | 2025-10-01 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ad06fa4-a0e8-3833-8536-7a1b316732f9 | -11.38968 | -44.89875 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff8844b6-d63b-36ae-8e8e-8f45a33ef88d | -10.83091 | -45.38466 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1b04096-4d05-3e84-bb43-bc7eeb28f943 | -14.21345 | -46.11379 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77d14d3b-c2be-3e74-8ffc-3b2ec344ecda | -10.97852 | -46.53403 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b15ff69d-9d13-3451-a905-cd8c4bdd9635 | -11.67488 | -44.28672 | 2025-10-01 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a33f39a-2bd4-377b-b154-0b8446763fa1 | -13.64777 | -47.31253 | 2025-10-01 03:30:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0fefb2b-fb99-32c0-bdea-4802b4fd6268 | -12.785 | -46.86194 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfa43f5d-0ad5-3c34-9c39-863f8b7badce | -11.3887 | -44.90375 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2179651c-4c6c-33bc-a9ba-5d0e505cef5b | -8.58141 | -44.746 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 305f030b-d550-3542-800f-12b316ee7276 | -11.4657 | -44.99368 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7a011ac-a512-380c-bdbf-2f1717663f3e | -13.76348 | -47.95652 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2f784535-96f4-393b-abbf-0500e1227746 | -14.7003 | -42.32135 | 2025-10-01 03:30:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55f915f5-221b-3adc-9ba3-8aefd9f55c37 | -11.45411 | -43.5197 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9877324-12bd-3796-94eb-8c7a34bce595 | -11.60549 | -45.04584 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f363be29-0d2b-3d9f-95f9-1127ee53eabd | -9.9393 | -43.60073 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73a53bb0-ae08-36dd-9e96-b0eb0681c19b | -14.70008 | -42.32154 | 2025-10-01 03:30:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 26c21806-21c5-3c91-a5db-7ed2d09ee52a | -13.29417 | -47.58265 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e2671bd8-5c94-3972-aeed-d4c0cb7fc837 | -12.81483 | -47.02185 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12f06c03-e8bc-3536-b1ca-508174218e1d | -13.55396 | -47.28199 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7aa8048f-9218-37b0-85be-260c8b607894 | -13.55442 | -47.28209 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1ba6ab0-233a-379b-a76a-b6be7394de47 | -12.41357 | -44.09734 | 2025-10-01 03:30:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28cca05c-59cc-3e74-aa5c-34ac56490435 | -11.8122 | -44.97112 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09b8d033-b39f-3c8d-a01c-f28e9e3cd12b | -9.92415 | -43.67899 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2783075f-7eb1-3b2a-8607-e6da3d4b6bae | -11.46366 | -45.00405 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e569514-262c-339a-8862-b2320efba27d | -10.97583 | -46.54702 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea367c24-668a-390b-b29c-ac1d52a152cc | -11.46599 | -44.97758 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cfaf913-9938-3c76-bb8e-40e83aace454 | -11.81075 | -44.96872 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README17.md)
