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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfee43df-7376-34ec-ab40-da3ba3936d7f | -2.8809 | -51.2972 | 2024-11-02 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 1411deb9-dac6-3eb8-82b5-9d239d53488a | -3.0088 | -51.5834 | 2024-11-02 00:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5957756f-8a33-3085-bedd-8f2b73c5c168 | -3.0734 | -54.167 | 2024-11-02 00:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| a36219dd-c2c2-3e45-a906-acd4b385e250 | -3.2249 | -44.431 | 2024-11-02 00:35:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 1784306e-11ef-3c79-ae51-3e70a435b331 | -3.225 | -44.4081 | 2024-11-02 00:35:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 164.4 |
| 9a1bd8ab-d977-3206-b229-38a0febc62e8 | -3.2435 | -44.4302 | 2024-11-02 00:35:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 322668c6-6cd6-30e4-bea5-59aee97af91b | -3.2436 | -44.4073 | 2024-11-02 00:35:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b1578749-50bd-399f-8b60-4bcb0fcbcf7e | -3.1097 | -54.2865 | 2024-11-02 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 8c485f15-8e1f-33c4-88e5-814d637eb94b | -3.1098 | -54.2665 | 2024-11-02 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a43e0406-a29c-3aca-a9be-15f777a6016f | -3.1212 | -51.1244 | 2024-11-02 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 9026096f-7a44-3e9a-a6eb-f6e19644cf2e | -3.1281 | -54.266 | 2024-11-02 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| b11cb9f8-70ed-3e24-a27b-f807b9493c63 | -3.1282 | -54.2459 | 2024-11-02 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 21fa87fe-0366-3f83-9a2c-68bee16df240 | -3.1767 | -51.0812 | 2024-11-02 00:35:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 039c55da-e2c4-3468-9ffe-1b62b525f72d | -3.2063 | -44.4317 | 2024-11-02 00:35:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5145e987-ac0e-30d3-80e1-aaa6a00bb3f4 | -3.2064 | -44.4089 | 2024-11-02 00:35:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a7ece5d5-57c0-348e-84f3-327614a9a169 | -3.3131 | -45.4013 | 2024-11-02 00:35:25 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f96a2f8e-d7c3-3c03-8415-5aa48d00dbe7 | -3.6387 | -43.7007 | 2024-11-02 00:35:26 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 52727f38-a5b9-338c-be75-72eac6284148 | -3.4574 | -50.1731 | 2024-11-02 00:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 8fec8d17-6c91-35b0-a01b-572a62018e2e | -3.6572 | -43.7229 | 2024-11-02 00:35:27 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| bab1168f-7192-3a94-ae5d-9ddfc82a8b37 | -3.6574 | -43.6998 | 2024-11-02 00:35:27 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 0a712f73-ac15-3ba8-a030-fa9a34823c6f | -3.6575 | -43.6767 | 2024-11-02 00:35:27 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f56eb0ad-2839-3d8f-9ce2-d5d0194effe2 | -3.7701 | -43.5554 | 2024-11-02 00:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 6607a239-b255-3427-bd32-bc108ef09b2f | -3.7703 | -43.5323 | 2024-11-02 00:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 50443776-431e-33ee-9eae-2b1affa7499c | -3.7888 | -43.5545 | 2024-11-02 00:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 3357c2a3-b06a-317f-8bab-3819e1792531 | -3.7558 | -46.0536 | 2024-11-02 00:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 60aa6fe3-7236-3992-a7d9-884fdc1c48d5 | -3.7372 | -46.0545 | 2024-11-02 00:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 221.9 |
| 1e1a4e48-993f-3c16-969d-8f71eb033db6 | -3.7373 | -46.0322 | 2024-11-02 00:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 109.6 |
| a2ca6c42-98e3-3f98-9113-60494c96e786 | -3.7559 | -46.0313 | 2024-11-02 00:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b48013f5-0231-3a6f-83f2-92c8a25e81fd | -3.9473 | -48.3666 | 2024-11-02 00:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c619023f-ca18-3d06-a258-4844385b9bf2 | -3.9474 | -48.3451 | 2024-11-02 00:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 795a7655-e144-3d2a-acdb-e451555390af | -4.2796 | -45.5587 | 2024-11-02 00:35:30 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| f6391fe7-2073-3dd0-8f3e-25f726ae7155 | -4.3164 | -48.6515 | 2024-11-02 00:35:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| ceff7faf-87ed-38f2-bd43-9cb52101a1b9 | -4.3867 | -43.4757 | 2024-11-02 00:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 1b13038b-a47f-3404-8a21-e854e6baa0b5 | -4.4054 | -43.4746 | 2024-11-02 00:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 04ad7c78-8701-3268-935c-e7ab8238a75e | -4.3537 | -48.6068 | 2024-11-02 00:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| d1c71271-3aa2-31e4-ae19-169f5d0eeaa6 | -4.5575 | -43.1162 | 2024-11-02 00:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| d30ffca6-a66c-30e3-890e-0e013845b79b | -4.5577 | -43.0928 | 2024-11-02 00:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 19ba93af-ee03-3467-8ced-3e0760b3648a | -4.6072 | -43.9945 | 2024-11-02 00:35:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| eb65b770-ed94-350c-a85a-16daf5cb2662 | -4.665 | -46.3862 | 2024-11-02 00:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 8658d3e3-76f4-3c6f-9278-b5fa6b432eef | -4.6837 | -46.3852 | 2024-11-02 00:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| fa9a958f-ae93-3402-9e59-4807d680eb9b | -5.1146 | -46.0264 | 2024-11-02 00:35:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a6e7242b-8ff6-3e78-a2ef-55cd021bfb3a | -6.1302 | -47.2444 | 2024-11-02 00:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 02ebfa29-45be-3770-8ac4-9c8779f521dc | -6.1304 | -47.2224 | 2024-11-02 00:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| af07af9c-0575-39c9-b5e8-d9b54f70eaea | -6.1489 | -47.2431 | 2024-11-02 00:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| ecc61bf8-f96a-3127-a99a-3d8d864737dc | -6.1491 | -47.2211 | 2024-11-02 00:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 9e759fbe-8ee7-33c2-adfd-1dea9036b86c | -1.5531 | -52.1896 | 2024-11-02 00:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c68fa3af-2553-31f5-8f7b-3d1cc6170a5d | -1.5899 | -52.1481 | 2024-11-02 00:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 21ed5aa8-ef82-37d7-8136-63f53cbdb60d | -2.195 | -46.4634 | 2024-11-02 00:45:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 103b83c8-d4bc-3fe6-8b57-50a50d297479 | -2.2135 | -46.4629 | 2024-11-02 00:45:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2d738adb-f07c-3381-990f-1007c1674c85 | -2.2568 | -50.4376 | 2024-11-02 00:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f98bc061-facc-38c1-90c9-ee500c6c0d1e | -2.2663 | -53.7422 | 2024-11-02 00:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 3a061a52-b730-3af3-ad00-86d5119c3694 | -2.2847 | -53.7419 | 2024-11-02 00:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d468545e-4aae-366c-87be-a74955e0bd81 | -2.3985 | -46.5683 | 2024-11-02 00:45:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d06653ec-e8e4-3e37-aa7b-4a700f49805d | -2.6759 | -46.7585 | 2024-11-02 00:45:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 34de14a7-d390-3a0b-a28f-642d655434ef | -2.6944 | -46.758 | 2024-11-02 00:45:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a009774e-e984-3a50-b5c1-98b3ec5ce5b3 | -2.78 | -48.5806 | 2024-11-02 00:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8199afb3-1e6d-3e7a-9357-656127fb87c1 | -2.8056 | -51.7539 | 2024-11-02 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 33a7eb91-d11b-3d50-b018-01344a13debd | -2.8555 | -53.3459 | 2024-11-02 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c4b38f2e-4066-3c79-b945-18b677d1b564 | -2.8808 | -51.3179 | 2024-11-02 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a976f2ce-02e3-3ec9-9170-ee13c2a1be44 | -2.8386 | -52.8794 | 2024-11-02 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 34fff4b0-e56e-33b6-af55-f71afb22fcec | -3.0088 | -51.5834 | 2024-11-02 00:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| a09065fb-d0b2-3cb5-a48d-6a65fb45f016 | -3.0734 | -54.167 | 2024-11-02 00:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| e77fbe1d-6873-38b6-8dc3-0cfbb06e3196 | -3.1097 | -54.2865 | 2024-11-02 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| c1e66f1d-d52b-3c81-9c71-d97c3030ab63 | -3.1098 | -54.2665 | 2024-11-02 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 6aa2e1c0-5120-3aae-9a83-b91db689e0b4 | -3.1098 | -54.2464 | 2024-11-02 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 885731c7-c7b1-3709-aee6-1f7faf54c03f | -3.1212 | -51.1244 | 2024-11-02 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| da547f7d-738e-34d5-b1d8-1aa49aafd678 | -3.1281 | -54.266 | 2024-11-02 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 06026c97-df67-382a-b02d-9a3c284ff949 | -3.1282 | -54.2459 | 2024-11-02 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 52d2240c-9aa6-3a97-be13-7339f39414b1 | -3.1767 | -51.0812 | 2024-11-02 00:45:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 316f149b-c202-383d-b0df-f510612148d8 | -3.2249 | -44.431 | 2024-11-02 00:45:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 8ba9b881-c449-375b-bdb4-21e1ae1fa20b | -3.2378 | -45.5839 | 2024-11-02 00:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 063c4e4e-7624-310e-b98a-3582f1df1135 | -3.2436 | -44.4073 | 2024-11-02 00:45:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 9f37ae75-2912-3b59-b3d3-e3d2c7feb31c | -3.225 | -44.4081 | 2024-11-02 00:45:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 162.4 |
| c90fb09a-c69b-33b8-836b-1b9a3c85ed87 | -3.3461 | -50.2609 | 2024-11-02 00:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 65e6c7ac-3742-3aa2-afb8-a5886c5cc3d3 | -3.4574 | -50.1731 | 2024-11-02 00:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9ce26e52-102f-305d-847e-7c3c937eed70 | -3.6574 | -43.6998 | 2024-11-02 00:45:27 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| f79d77fb-5918-3619-82c2-b51c67ada946 | -3.7701 | -43.5554 | 2024-11-02 00:45:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 06ff6869-3ca4-354e-b24a-3c1ffcf721fe | -3.7703 | -43.5323 | 2024-11-02 00:45:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 325f3aca-e624-3114-bc6b-ac09544d24c8 | -3.7888 | -43.5545 | 2024-11-02 00:45:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 7a7bcbcf-8684-3b63-9e8f-3eea5cc5163a | -3.7372 | -46.0545 | 2024-11-02 00:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 193.1 |
| 84c642e1-016d-30d4-b1ad-5eb2782e4029 | -3.7373 | -46.0322 | 2024-11-02 00:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 110.1 |
| a98aafda-ee30-3af4-87b7-994eddb36123 | -3.7558 | -46.0536 | 2024-11-02 00:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 131.2 |
| ff7d9d76-bca2-39c7-994d-7301a2c69332 | -3.7559 | -46.0313 | 2024-11-02 00:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0df30d3f-3109-3537-9fee-c74748f4cf90 | -3.9473 | -48.3666 | 2024-11-02 00:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 4f0ec5b3-92ee-3729-a7af-751360daaca4 | -3.9474 | -48.3451 | 2024-11-02 00:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| beed8775-6cef-36da-9641-8cb0b3c96e29 | -4.3165 | -48.63 | 2024-11-02 00:45:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 82220b3e-b111-3ff7-b6e6-bf5686dc1170 | -4.3867 | -43.4757 | 2024-11-02 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 329b57ba-2353-3ac8-bf9c-d8c683d7189b | -4.4054 | -43.4746 | 2024-11-02 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 2165eecc-1743-305c-83ab-3fd43f2c3259 | -4.3537 | -48.6068 | 2024-11-02 00:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 8d1a27b5-e936-3192-bd48-cfac91d838f0 | -4.5575 | -43.1162 | 2024-11-02 00:45:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| fa203661-23d6-3236-a8c2-89d9b4a8a23b | -4.5577 | -43.0928 | 2024-11-02 00:45:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 52f17ddf-4c58-37f8-a49b-cabd943f40b9 | -4.6072 | -43.9945 | 2024-11-02 00:45:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 76cd7c3b-9483-371d-8e7a-ff2f9d5aab32 | -4.665 | -46.3862 | 2024-11-02 00:45:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8cc19607-b7b1-3535-9641-e2877b089f9f | -4.6837 | -46.3852 | 2024-11-02 00:45:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| fa41ca8b-6ba9-3b75-9cf6-aa6622b86f9b | -5.1146 | -46.0264 | 2024-11-02 00:45:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3ab2d155-dc68-3715-94f8-37caf03dc88f | -5.2027 | -44.3014 | 2024-11-02 00:45:35 | GOES-16 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ee420070-9ea8-35e2-83c6-03298aced558 | -5.3252 | -43.065 | 2024-11-02 00:45:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 94386461-bd4f-3eed-aff1-dae188a3c4ce | -5.3063 | -43.0897 | 2024-11-02 00:45:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| e8c325c9-3e53-39da-8326-5a306ab37e91 | -5.3065 | -43.0663 | 2024-11-02 00:45:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| d32b6bee-eb65-3b6d-bd30-64b357b02462 | -8.0276 | -71.3254 | 2024-11-02 00:45:52 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 37.1 |


[Clique aqui para ver as próximas entradas](README4.md)
