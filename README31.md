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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 281fd633-96c9-3140-a7d9-e6ab9920b5f0 | -8.5321 | -63.8792 | 2026-09-08 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 01440ca0-d4b3-3cd0-8601-527772431de2 | -9.0982 | -65.4904 | 2026-09-08 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c2f586c1-6f9c-3376-bbf2-347d9ef10113 | -3.3871 | -59.4075 | 2026-09-08 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 6fb0f75c-d565-3aab-81ca-916984065f85 | -9.0058 | -65.4373 | 2026-09-08 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 8075938c-2100-3970-8838-16abe9fce6b6 | -8.7438 | -62.4169 | 2026-09-08 16:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 82e602b5-54d2-3a49-b409-8983d6836d6a | -8.7624 | -62.4162 | 2026-09-08 16:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| ae0a4889-a5a8-3754-bb46-f80161d8c9cd | -10.71 | -45.97 | 2026-09-08 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f8e742c-6888-31ab-ad31-78db56fe32d1 | -12.6 | -45.46 | 2026-09-08 16:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b108f03-fb39-3dce-a2a6-5a33b4307bff | -10.74 | -45.93 | 2026-09-08 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81e94c83-9028-376a-8e5e-de9a59314558 | -10.71 | -45.92 | 2026-09-08 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4ccb0678-5764-3368-a653-4c398ed16e99 | -12.63 | -45.47 | 2026-09-08 16:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f921e77-b55f-381b-b2a1-8e12f23ca902 | -9.75 | -43.52 | 2026-09-08 16:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39a8b64b-2e63-3740-84a5-42f5ad59b066 | -12.6 | -45.51 | 2026-09-08 16:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e6b9c7e-9f38-3f8e-a481-6d02f55631bf | -11.27 | -45.68 | 2026-09-08 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7125e01a-0085-3023-89bc-8995c5d0c68f | -9.72 | -43.51 | 2026-09-08 16:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 400ef9ea-9033-38e4-9b19-e8232723cea8 | -11.27 | -45.73 | 2026-09-08 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e4c39d2-8e13-3856-9ac6-99348d462a39 | -10.74 | -45.98 | 2026-09-08 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be2c22ba-79e7-37c7-81a8-bfa246dcc23f | -9.0982 | -65.4904 | 2026-09-08 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 5bb02adf-0815-3c81-abf4-a86a49e04ce8 | -7.6968 | -44.3247 | 2026-09-08 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 616d2df0-b063-3c6d-b05b-e8ddfc687a70 | -9.0415 | -65.7349 | 2026-09-08 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 944ac537-513b-3b4f-a422-b260c0ab6668 | -7.6779 | -44.3266 | 2026-09-08 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d0630539-d631-3727-98e3-b3a9c3ede7fd | -8.7624 | -62.4162 | 2026-09-08 16:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| dc2b1032-e1e7-3d12-8c8b-47347d0f6bcb | -2.0934 | -49.5359 | 2026-09-08 16:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 0c634c8a-92e4-326b-8e3d-1b0909b41ea0 | -3.3871 | -59.4075 | 2026-09-08 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6e11230f-1c73-3998-b445-114adf6420f1 | -8.7253 | -62.4177 | 2026-09-08 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 7cacf536-6283-359f-9848-d256cc522ae1 | -8.5506 | -63.8786 | 2026-09-08 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 266d6a87-dd75-37a2-8037-75f7fdaef0af | -3.3871 | -59.4075 | 2026-09-08 16:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b2a8f396-386e-30b3-b2b7-0186942e0d8f | -7.6968 | -44.3247 | 2026-09-08 16:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 60ce888d-8efa-3985-8c2f-ab0438e9de62 | -7.6779 | -44.3266 | 2026-09-08 16:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 44a5d24e-6462-32db-a306-416210ed0f8f | -2.0934 | -49.5359 | 2026-09-08 16:40:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7b8b03e2-4be5-3dca-a1de-00fb5257b15e | -7.6968 | -44.3247 | 2026-09-08 16:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 302.1 |
| ed25a7de-6bcc-383a-bf19-481c3540b558 | -7.6779 | -44.3266 | 2026-09-08 16:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 168.2 |
| a83b654b-a8da-3b68-a8c1-2b0fb0886f02 | -7.7156 | -44.3228 | 2026-09-08 16:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c3a3c2f0-3d28-3c79-a3fa-9d1dfdb52871 | -2.0934 | -49.5359 | 2026-09-08 16:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 90c6ced6-28af-3886-9596-9e30d51f9579 | -7.6968 | -44.3247 | 2026-09-08 16:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 0e10a325-aba1-35b7-a78f-f1e374e64a44 | -2.0934 | -49.5359 | 2026-09-08 17:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 224ef596-9356-399a-a500-3dd8a0f9a21a | -7.6968 | -44.3247 | 2026-09-08 17:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 239.6 |
| b9d6d8a9-0747-3640-8fe0-53de323e6723 | -7.7156 | -44.3228 | 2026-09-08 17:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 86c5b775-8fe3-3ac8-8458-017017165600 | -2.0934 | -49.5359 | 2026-09-08 17:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d435d0fd-3e08-3682-ac95-db2765b63ee5 | -7.6968 | -44.3247 | 2026-09-08 17:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.9 |
| d52cd831-fd97-3ac0-b481-e0a861c4f52d | -2.0934 | -49.5359 | 2026-09-08 17:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3aff5d87-f415-3f9e-981d-8c2bc130ceaa | -1.4944 | -54.2563 | 2026-09-08 17:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4eb39a00-3173-3b0a-bca8-2c400d6b5bbf | -7.6968 | -44.3247 | 2026-09-08 17:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5e1e81af-020a-3190-86ec-fd1f703b1053 | -3.3871 | -59.4075 | 2026-09-08 17:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 5d7f3982-0f68-318c-9016-3b9cb9c4fd66 | -3.0071 | -57.8547 | 2026-09-08 17:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 067e0a33-ebe0-346f-a34b-595779f67cd3 | -7.6968 | -44.3247 | 2026-09-08 17:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 8fceaa5c-166f-3b60-90fd-0cf3dbcafc96 | -9.7138 | -43.4192 | 2026-09-08 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 430.9 |
| 3624a590-b9e4-3e02-8922-92114c3f3e04 | -5.3645 | -56.0447 | 2026-09-08 17:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d84e7c28-abff-3e19-99fe-40d37f4672c4 | -3.382 | -61.309 | 2026-09-08 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 7af0443f-8a07-39d8-b06f-e902ae60cea7 | -5.3462 | -56.0256 | 2026-09-08 17:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| d0b3f072-2e67-3e94-9832-472b6a98ef85 | -3.3688 | -59.4079 | 2026-09-08 17:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9ae62a6f-5701-3bac-83af-e5336f39facf | -7.6968 | -44.3247 | 2026-09-08 17:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |


