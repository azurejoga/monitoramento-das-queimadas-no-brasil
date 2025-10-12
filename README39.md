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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0d66eee-b3a6-3ac3-8b8d-2c6c92095e6e | -6.28289 | -44.41576 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71d6d3d7-f913-374c-83fd-174c34b1b6ec | -5.91299 | -45.42582 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00c148f8-64c2-3bb3-b029-0d5edb46700a | -4.42118 | -43.4721 | 2025-10-12 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d418825-83e6-3f7b-b454-390f913b436c | -7.48719 | -42.76959 | 2025-10-12 05:01:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2516d16b-bb2c-3790-9ac8-91e1223fa1ce | -2.4367 | -49.36257 | 2025-10-12 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18a0e804-6adc-37ce-83ca-e6a3fa7bd2cd | -5.75691 | -46.49851 | 2025-10-12 05:01:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a470c858-3e20-360d-9a42-63e0b746456b | -3.51588 | -45.84328 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 983c7103-90d3-3415-a339-00851e4e0610 | -3.1738 | -48.61392 | 2025-10-12 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eff73d05-7250-3943-9cc4-41430c5b4ca5 | -2.7177 | -48.35897 | 2025-10-12 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d0629f3-6334-3205-9aed-8fc123794ddb | -3.60935 | -42.75243 | 2025-10-12 05:01:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7f3f718-ec78-3f44-a6f2-838dfb15839f | -2.54353 | -47.80245 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 081e133d-2468-3aa5-bd85-aae78b1ac120 | -1.90292 | -51.01248 | 2025-10-12 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd3f3b06-0beb-3eea-ae1c-883e488e7253 | -4.26786 | -46.9256 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ab6241e-4f55-368f-b3e8-a533705dd1ac | -7.85522 | -44.53356 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9d3b90c-7fa2-3c1b-9064-2b9a66c75778 | -2.88721 | -50.73109 | 2025-10-12 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5fc84d1-fe5d-3b42-8012-cd5c6db55d55 | -5.91812 | -45.43047 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 594e1f6b-6a31-3877-911c-bdb39d1a714a | -3.86724 | -42.51656 | 2025-10-12 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 29bc2df3-1169-3377-a089-2695f83a8b49 | -7.40136 | -46.95158 | 2025-10-12 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7a039ff1-c958-35b3-a6e8-d607c8eea112 | -7.42367 | -45.16401 | 2025-10-12 05:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eba80b42-5827-36e9-802e-afc4d3365d27 | -3.50699 | -45.84099 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4de5a48e-809d-367d-913a-c303ddbf042a | -3.40776 | -52.66283 | 2025-10-12 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc4023d4-494c-35d0-a25a-4a48dbf3ed32 | -2.26407 | -47.85153 | 2025-10-12 05:01:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a0b7b96-cf08-3e27-91e1-88f26895fd1d | -5.91867 | -45.42662 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5916c476-cd47-3d53-8c45-c1f3fe92a718 | -5.91244 | -45.42962 | 2025-10-12 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af370c13-7adc-32b3-907b-80fb7a8c9953 | -3.50424 | -45.84838 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7bd1c6c-a2c8-3cef-b0a9-9c286f6cb7ed | -2.29356 | -47.99169 | 2025-10-12 05:01:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8cd89ded-e252-3339-9556-c2d72fa4fe2b | -7.65194 | -42.57906 | 2025-10-12 05:01:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8a7fb086-2b7a-3797-b553-c07bbfa1f0ba | -7.52471 | -44.29346 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55f455ec-1a24-39e7-ac45-4ee93559a8e9 | -4.54312 | -49.68972 | 2025-10-12 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff44dbbe-f4cd-3485-8484-dd3529835353 | -6.50365 | -44.13491 | 2025-10-12 05:01:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a56a9b4c-4ecb-31f0-8036-1059549b7777 | -6.28392 | -44.4148 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d4af2f1-0fac-35ef-a4f1-a7a78e540e67 | -2.99706 | -48.74207 | 2025-10-12 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e78c4adb-7be4-37c4-a8ac-64b60543b388 | -7.85081 | -44.51971 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fe0a034-c614-355c-8c92-f8bbbd525c65 | -7.41799 | -42.96793 | 2025-10-12 05:01:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0ee5ddc6-9e31-360d-91e9-40c3d51397c6 | -3.87653 | -42.51714 | 2025-10-12 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4e1cc2d3-2e72-3540-802b-a9cc5b03cd19 | -6.75871 | -44.65144 | 2025-10-12 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 783aa465-81ea-3f1f-b9ec-20dddc4a4807 | -2.44962 | -49.36077 | 2025-10-12 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac53ba0b-f871-396e-8e84-c6fa8bb9a4ae | -3.1965 | -49.483 | 2025-10-12 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53105e94-9ffa-38fc-95b2-902cd70d1e4f | -4.61835 | -45.77694 | 2025-10-12 05:01:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7b46822-73cd-3ee0-8cc9-729cb043b803 | -2.63506 | -47.30657 | 2025-10-12 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e96af31-783a-3a32-8357-a4119983a63b | -6.50248 | -44.13303 | 2025-10-12 05:01:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57ca3f89-b0c4-3666-96ed-82be056deee5 | -7.54566 | -43.84219 | 2025-10-12 05:01:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd0788a9-55fb-31ee-a4cd-75b06ee60131 | -6.3177 | -44.2574 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0bf11d1-7114-3586-aebb-84842af899ef | -6.50877 | -44.13335 | 2025-10-12 05:01:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06bb6775-ba4b-3882-8e74-3101746c075e | -3.41154 | -52.88253 | 2025-10-12 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 607ad67e-3592-35a0-9e7e-3d32a0a9d5e8 | -3.50268 | -49.0577 | 2025-10-12 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 253fa27d-4c89-364a-9392-89bf312f5866 | -7.05799 | -44.70665 | 2025-10-12 05:01:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 18db99f3-3bca-33a8-ada6-b6c7e0bb7b64 | -7.85011 | -44.51672 | 2025-10-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 384b9e70-a521-3534-9efa-78ab3fba7017 | -3.50473 | -45.84505 | 2025-10-12 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fadfe474-7a1a-37fb-bb39-0def83c8356a | -6.27846 | -44.40921 | 2025-10-12 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54e160d2-1316-3c25-a87b-7a9e72f0bae9 | -2.53359 | -47.80596 | 2025-10-12 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 27ec2eba-0feb-31ae-9d47-da7c0801a9ee | -14.02851 | -48.15281 | 2025-10-12 05:04:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf57e770-1f73-330e-b0c1-1b8e757cca2d | -13.57033 | -46.35257 | 2025-10-12 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 32c9a6cb-6dab-3c16-9b9d-7ef5da028639 | -14.92601 | -46.76048 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff4dd7c6-2c78-3596-a8fa-348d8ce2f6e2 | -10.67816 | -62.25704 | 2025-10-12 05:04:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 092b5fff-ae49-3426-9d57-9624f0ce25b7 | -12.39435 | -63.7065 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f80b8d7e-6073-368a-a974-15151985cba6 | -14.96522 | -46.72918 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f6b66183-ac23-3f5b-af87-606eac7b5e23 | -9.08232 | -48.03358 | 2025-10-12 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c28387c-76b0-375d-8b9c-7882ed820169 | -11.46642 | -61.94913 | 2025-10-12 05:04:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10025111-259f-3fe3-821e-4424c7844b70 | -13.57293 | -46.35062 | 2025-10-12 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f118b97d-5699-3cbb-92bc-9fe12ecc500e | -14.97034 | -46.73676 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a9ad5f1-3f60-31d2-a78b-20a66384ca9f | -10.56676 | -57.52042 | 2025-10-12 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 385070c6-d99c-3478-90a6-0109d3fe4155 | -12.21033 | -64.36969 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 56f88b83-df1c-38b6-b0d0-d73f5de83218 | -8.83564 | -46.03806 | 2025-10-12 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32fc507e-2aae-3812-bf0e-07d6427de00c | -8.47921 | -46.23253 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb431ec4-c13d-3dc3-aa13-73f8fa426d1a | -12.24113 | -45.33917 | 2025-10-12 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2f32196-1a7f-336b-ab29-22c69b58f112 | -10.15943 | -44.55322 | 2025-10-12 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6aebbfe8-b2b6-309a-a858-c274087a5c3c | -14.94621 | -46.73935 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0b778a5-6cc6-3d87-a237-7833d8cf65f4 | -8.50957 | -45.95339 | 2025-10-12 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 330e4952-c593-3baa-a84c-4c3819f60952 | -12.21126 | -64.3646 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eb8abb03-5c65-3a74-9b6c-0fa9d9192a3c | -14.91878 | -46.77226 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d435b641-9451-3bcd-85f8-fc628a44023d | -12.39528 | -63.87762 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 506581a4-dfc7-326b-8381-8eee81c268d9 | -12.20939 | -64.37477 | 2025-10-12 05:04:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b7ac7c0-40ab-3c73-8039-692c3e52b2ba | -11.75754 | -61.06594 | 2025-10-12 05:04:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c00dcae3-6aa6-3937-b9a4-1a7f4da98f43 | -8.47528 | -46.23088 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f8a0b00-7256-3a3b-9eca-72c894500a0d | -13.5772 | -46.34495 | 2025-10-12 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ecce4e5-7f2a-3a6a-9087-7215b7e31549 | -8.51007 | -45.94952 | 2025-10-12 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78b6e03e-1c4d-3d4c-bbeb-9aadad6345f0 | -14.96471 | -46.73373 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 341f2b5c-358f-374a-8385-fcd9cae31df4 | -10.56343 | -57.51986 | 2025-10-12 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4db883b9-24c5-3788-907f-8cd7fda6849e | -10.77909 | -43.95394 | 2025-10-12 05:04:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 475c8f1a-2ecf-32c4-af6d-bc67f5e021d0 | -13.57129 | -46.34401 | 2025-10-12 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 495b27a9-c3d0-3341-9daf-6b44b2877e7f | -12.59022 | -62.95019 | 2025-10-12 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a312d012-76a7-3ed1-a435-262664db9662 | -10.37983 | -65.33371 | 2025-10-12 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f27adcf-bf5a-3833-b07b-aa6eda59d34d | -10.14875 | -44.5535 | 2025-10-12 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d259fb1e-b18f-37f9-8ba0-67fa1a957e98 | -8.47219 | -46.21189 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01e6d041-cc1f-3c02-af12-af0245abaca2 | -8.47579 | -46.2272 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ffed477d-5c9f-3fde-b50b-eba07e896ef6 | -14.95413 | -46.7217 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c4759714-7321-3841-8c5c-f569b706e088 | -14.02735 | -43.49391 | 2025-10-12 05:04:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6d9bcbe-424a-3206-835e-61494831fe82 | -11.07692 | -57.87928 | 2025-10-12 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f76b170f-d646-35b4-942c-8b6745caa395 | -14.96576 | -46.72443 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5b43ce25-3485-3e86-87ef-2fdbb2611ea5 | -10.64121 | -69.35537 | 2025-10-12 05:04:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9185026-13b5-3dea-b0ea-f44be2bff90a | -11.75827 | -61.0683 | 2025-10-12 05:04:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55c6418a-76e7-3c0d-9f35-92c6814d0e5b | -8.69684 | -47.06043 | 2025-10-12 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 649b00f3-fcad-39e5-ad47-62b87581ef0d | -14.93956 | -46.74561 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f862972e-64b7-3717-8707-a06e2dbbce0f | -8.4727 | -46.20815 | 2025-10-12 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2affb2a8-9e5a-3ff4-bd92-c1ece8cd5ddf | -10.16727 | -44.54218 | 2025-10-12 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0cc82d3-8fb2-3fb7-a854-ea226ab1c402 | -11.14213 | -55.19466 | 2025-10-12 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b3dc15b-7953-3f94-9d0c-bd108240adb6 | -13.57394 | -46.34214 | 2025-10-12 05:04:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce87ec78-a8a3-3f3a-b1e9-e58c7a5011c3 | -11.62444 | -55.01514 | 2025-10-12 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69a6193a-6466-3958-9c5d-bc8aa239a636 | -14.92062 | -46.75536 | 2025-10-12 05:04:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README40.md)
