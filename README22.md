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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94e6cb53-f9bd-3d4a-b713-418f9e45e2da | -12.7764 | -44.4223 | 2026-06-24 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 216.4 |
| b7e12da5-bfbe-3f85-84a1-e3da9779fa0f | -12.8354 | -44.3657 | 2026-06-24 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| d515d48b-5edf-3c22-8278-77359053b0d2 | -12.8548 | -44.3625 | 2026-06-24 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| ccd1129d-3ae7-3a5b-86d9-32b841dcc6b2 | -12.8359 | -44.3422 | 2026-06-24 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| ccaf375b-4a95-3456-af61-016f6317f73a | -12.8354 | -44.3657 | 2026-06-24 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| f3d5596d-61a2-3a21-8de4-16332eb3ee61 | -11.2407 | -43.3464 | 2026-06-24 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 139.1 |
| beee1081-2a67-3e92-a995-3f290fee2b58 | -12.7764 | -44.4223 | 2026-06-24 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 226.6 |
| 586f2153-bd33-338b-94c8-b82a8fb28a85 | -12.8552 | -44.3389 | 2026-06-24 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| beedaf22-1f12-3618-9acd-7535ece0609e | -15.7635 | -43.2146 | 2026-06-24 13:10:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 98.2 |
| fe863a61-31db-3501-b94e-416ee4bddaa2 | -9.7442 | -47.8688 | 2026-06-24 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 1a8197ea-5d55-30c4-a7ed-0cdcda43d8c9 | -12.8552 | -44.3389 | 2026-06-24 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 2efac78e-4750-3756-9c96-79e3e17e9ece | -11.318 | -43.3109 | 2026-06-24 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| fc48d07c-e362-3e19-a564-11858e0f58e9 | -9.7439 | -47.8908 | 2026-06-24 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 16490198-77f3-31cb-ab1b-0d189da13a6f | -12.8359 | -44.3422 | 2026-06-24 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| c23a6443-2ca0-30d7-bd02-19f4a0ce1daf | -11.3175 | -43.3347 | 2026-06-24 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 1d12976a-4005-3540-8ebc-dd84988ef0a6 | -12.8354 | -44.3657 | 2026-06-24 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| e71f32b0-f6e7-3248-9a16-bc32ad94611e | -15.7635 | -43.2146 | 2026-06-24 13:20:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 91.7 |
| a2cfc6b7-7545-33bd-9794-4626393561d8 | -12.8548 | -44.3625 | 2026-06-24 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 1c42f665-0c4a-3b7c-802d-9385c22bffb8 | -12.7764 | -44.4223 | 2026-06-24 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 210.3 |
| b856acee-d8dd-33cc-8ec9-d0fd114a76c8 | -11.2407 | -43.3464 | 2026-06-24 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 139.9 |
| d24aad6b-f1f2-348d-9fc4-d5c70760ba1d | -9.7442 | -47.8688 | 2026-06-24 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| fdc2c541-5380-3537-ba78-f5e588ee692d | -12.7764 | -44.4223 | 2026-06-24 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 288a9043-5e2a-38d9-b6eb-5f9c30769e3e | -12.8548 | -44.3625 | 2026-06-24 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 39a90bd8-ed6f-34b5-9733-fe5857a6b066 | -9.7439 | -47.8908 | 2026-06-24 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f0e72de5-71de-31df-b2eb-e2b69fadde88 | -11.2407 | -43.3464 | 2026-06-24 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 103.5 |
| e838243e-ebec-386a-b730-054d4b64d47c | -12.8359 | -44.3422 | 2026-06-24 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| ab254da7-748f-372b-89a7-e53e08dd062b | -11.591 | -47.4496 | 2026-06-24 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 50d2406f-48d2-3020-bee3-0effc1c90891 | -9.7442 | -47.8688 | 2026-06-24 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 83eb8576-0338-32e2-a080-15e03c4f9f96 | -12.8354 | -44.3657 | 2026-06-24 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 1b6875b8-0cc4-3744-ba83-58826c006907 | -9.7442 | -47.8688 | 2026-06-24 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| cc4e7fad-9f04-30b1-a31f-76fa4842857c | -9.7439 | -47.8908 | 2026-06-24 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1a57f094-06bc-33f2-955c-a15d8e9d086b | -15.7635 | -43.2146 | 2026-06-24 13:40:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 82.0 |
| e4f2e5a3-5fd2-3c4b-9c48-4982896340da | -12.8354 | -44.3657 | 2026-06-24 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 02496372-cbf9-3861-b2fb-e5c609870cae | -12.8359 | -44.3422 | 2026-06-24 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| ff9d4470-8b16-3036-8c84-6713a5de1cf0 | -11.3175 | -43.3347 | 2026-06-24 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 1f117141-72e5-3054-bc18-eeabf91e326e | -12.7764 | -44.4223 | 2026-06-24 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| c39163b3-3d19-3c94-9a7d-b07a92ae246b | -11.318 | -43.3109 | 2026-06-24 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 362734d4-9127-3dce-b537-ccfddaeaac22 | -11.2407 | -43.3464 | 2026-06-24 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 250.8 |
| acee57e4-2219-3f03-9ece-1327c7c8f1a5 | -12.8354 | -44.3657 | 2026-06-24 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 90c5fcd0-48f8-3ddb-83cc-adf9e3a4fe97 | -11.591 | -47.4496 | 2026-06-24 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 0f2c94d1-785f-3c6f-9608-80072b6f3296 | -11.2211 | -43.373 | 2026-06-24 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 9106b62b-c3c9-373e-b84a-fa5825818ec7 | -11.2216 | -43.3493 | 2026-06-24 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 224.6 |
| 6a3aebef-be29-3bde-8f6e-e9a56e850a2e | -12.7764 | -44.4223 | 2026-06-24 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 7bd55226-2066-307b-bb14-22b3365057b7 | -15.7635 | -43.2146 | 2026-06-24 13:50:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 142.2 |
| 10b48583-fe33-3101-a8c5-b01a75eee17a | -11.2403 | -43.3701 | 2026-06-24 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 89.3 |
| da91da79-06ec-3793-88be-bbbd3104664a | -9.7439 | -47.8908 | 2026-06-24 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 454bc7bd-260b-3c66-ba96-25b1afed6c10 | -9.7442 | -47.8688 | 2026-06-24 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 1e317c6a-3635-3f7d-8a19-d8cc727b1ba4 | -12.8359 | -44.3422 | 2026-06-24 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| cb41db6d-25a2-3103-ad0b-98a879a0d592 | -15.7629 | -43.239 | 2026-06-24 13:50:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 823877d9-761a-359f-99a0-74718b2d66db | -12.8552 | -44.3389 | 2026-06-24 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 7499d046-667a-30fa-9705-feae0fb9e176 | -9.7442 | -47.8688 | 2026-06-24 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 39a6415c-aac9-3716-a6b4-f491e9a66c18 | -12.8354 | -44.3657 | 2026-06-24 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| b73a5024-f7bf-3b9c-90dd-2b7869009e0a | -11.591 | -47.4496 | 2026-06-24 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 9a82278d-6f61-37d5-be5e-3725c056f870 | -6.5924 | -43.8957 | 2026-06-24 14:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 63dd3d28-deb0-3af4-82c2-8c3ad6bc0af7 | -12.7764 | -44.4223 | 2026-06-24 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 3bd2b705-5ead-3404-bf23-a95a3598cde5 | -11.2216 | -43.3493 | 2026-06-24 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 177.7 |
| 45a8d03e-098e-3558-970a-69bbb4a14e5d | -14.6973 | -46.1364 | 2026-06-24 14:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c6e615ed-dd89-3580-b095-e38c11155efd | -11.2403 | -43.3701 | 2026-06-24 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 9b3ea6a6-34df-394d-a95e-83662e943151 | -12.8359 | -44.3422 | 2026-06-24 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 28a8f15d-5b0d-3976-b831-ce7d3accfceb | -9.7439 | -47.8908 | 2026-06-24 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 70fa5f5f-77de-360f-b199-7acfeff800e6 | -11.2407 | -43.3464 | 2026-06-24 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 206.8 |
| a2b77922-3291-3fb0-9e0b-eac8fe9fccd0 | -11.2211 | -43.373 | 2026-06-24 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 168ffb29-fd92-3999-82e1-e567bc3d3ed9 | -15.7629 | -43.239 | 2026-06-24 14:00:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 77660de4-1b36-3d8c-b397-c904ec56cf13 | -15.7635 | -43.2146 | 2026-06-24 14:00:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 216.3 |
| b86a6729-9e49-35bf-b798-b8327cdec50c | -6.5924 | -43.8957 | 2026-06-24 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 17f0fd26-cb4a-3202-9356-030443cf5f0b | -9.7439 | -47.8908 | 2026-06-24 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| cca835dd-701a-31c8-88d7-7c7ed94421ac | -12.8359 | -44.3422 | 2026-06-24 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| a6711f53-bf85-33f7-9c5f-cec50ce82a2d | -15.7635 | -43.2146 | 2026-06-24 14:10:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 128.9 |
| da489fba-07f8-3975-b979-3ade0d507e03 | -11.591 | -47.4496 | 2026-06-24 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| ab968c22-5516-33e1-b004-0c259fb01843 | -11.2407 | -43.3464 | 2026-06-24 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 174.0 |
| 84be6422-f1d9-3642-a890-8b35fc2565de | -9.7442 | -47.8688 | 2026-06-24 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 982cbe41-5d93-329c-8af9-9c06f27c331b | -12.8354 | -44.3657 | 2026-06-24 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 0d36061b-91bd-3905-9933-1c39f7382eac | -11.2216 | -43.3493 | 2026-06-24 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 145.1 |
| 34e90636-11d6-394d-877d-00d3f33228be | -8.9427 | -45.68 | 2026-06-24 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 9ab655e4-466f-3e62-84c6-925d92d765a9 | -11.2407 | -43.3464 | 2026-06-24 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 174.7 |
| 02158521-eb59-3e5a-8275-9b34aa7abdae | -12.8359 | -44.3422 | 2026-06-24 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 18693d4b-3697-33f2-adbf-59e07e55b8ce | -12.8354 | -44.3657 | 2026-06-24 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 9ef7f07b-9619-3bd7-a9d6-763891656ab9 | -11.591 | -47.4496 | 2026-06-24 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 940bfb7e-952d-3ab2-a6c6-dbd597dfb1be | -11.318 | -43.3109 | 2026-06-24 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a2d93ca9-4c0c-3273-a80a-3f6f943202bc | -9.7442 | -47.8688 | 2026-06-24 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| f395b37a-796c-3d7d-be5e-1bc4857ed6d6 | -11.3175 | -43.3347 | 2026-06-24 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| dc64df4a-2600-30cd-9702-263fe2c41b43 | -11.5914 | -47.4273 | 2026-06-24 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| a587eb31-d927-365c-95dc-9001067a28e2 | -6.5924 | -43.8957 | 2026-06-24 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ea37004f-495f-38f5-a17a-06b556604e1e | -11.2216 | -43.3493 | 2026-06-24 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 122.4 |
| a154efd5-bc5f-3241-ab38-b829ed4e0c4f | -9.7439 | -47.8908 | 2026-06-24 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5fe60262-49c9-3d6f-a3b8-a9d5b2f82d5e | -12.8552 | -44.3389 | 2026-06-24 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 422339f8-7a32-32dc-9ac4-b602947b9679 | -11.2403 | -43.3701 | 2026-06-24 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 9735a8d2-84d7-3f52-b1de-7f95e33c6707 | -8.9427 | -45.68 | 2026-06-24 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 74219a91-3c62-330b-b663-7d04fdb97881 | -11.591 | -47.4496 | 2026-06-24 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 4280b99a-5bae-3b7e-b022-223a2ab5541d | -11.2407 | -43.3464 | 2026-06-24 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 131.2 |
| 9408a73a-dc6d-322e-95e2-f8fc9feeaf2d | -11.2216 | -43.3493 | 2026-06-24 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 111.5 |
| 3f2a80bf-828c-3583-af79-a05384c1f51b | -9.7439 | -47.8908 | 2026-06-24 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c111c00d-9fa6-3570-9ee5-b6afbeecda62 | -12.8354 | -44.3657 | 2026-06-24 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| f22a6c77-1c3c-3f96-a7a2-1ee6c6946322 | -6.5924 | -43.8957 | 2026-06-24 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 95011f80-9654-325f-a54a-5e683bc6cef6 | -12.8359 | -44.3422 | 2026-06-24 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 429269bc-9683-34a9-ab1c-e98169a84400 | -9.7442 | -47.8688 | 2026-06-24 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 4cf58a24-d2d5-373b-9de8-73ed1bee9d2c | -12.8552 | -44.3389 | 2026-06-24 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 6fb4d4cc-6348-3146-be97-f1225218764c | -11.591 | -47.4496 | 2026-06-24 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 3733d2e0-00a5-36c9-86dd-2350f872276a | -6.5924 | -43.8957 | 2026-06-24 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 27b5abfd-2023-3227-aa1b-4c8729c45925 | -9.7442 | -47.8688 | 2026-06-24 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |


[Clique aqui para ver as próximas entradas](README23.md)
