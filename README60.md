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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e109f8d-d923-3608-bd8e-5ab776236dff | -1.17871 | -53.89204 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 609583b0-d5f4-30c1-8879-f6bf0340c8e7 | -1.17799 | -53.89662 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c39506b2-c522-35d5-abaf-4374884337da | -1.17728 | -53.90117 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05a945b0-ca5f-3218-81f0-7fd8a10d3dfd | -1.175 | -53.8913 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cec9a4df-c5b8-37b7-907d-da40e0a819a2 | -1.17428 | -53.89589 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cac5b91a-59d4-3b6a-86b3-388fab8f49cc | -1.14106 | -54.10754 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3ee7f7b-6fdb-3a98-b6e8-2456175257fc | -1.13805 | -54.10258 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96ba50b2-94a1-3f60-b503-8867f23a0592 | -1.12152 | -54.1358 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| deb15dbe-10ca-3396-8f80-6749084814ff | -1.11918 | -54.12664 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd68ae73-7901-303f-b43d-6b0975305e64 | -1.1185 | -54.13099 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b2da96f-a7de-3a2c-9866-16d5763fd1c4 | -1.11783 | -54.13531 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8520c79-b2f6-3a14-90f9-e21cca874604 | -1.11479 | -54.13058 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c53e193d-63ad-3a1d-a931-75b29ccbcd63 | -1.11412 | -54.13484 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b4c6ff9-9c2a-356c-8a35-ee7e20b92e87 | -0.99537 | -53.7005 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4c949341-c664-353d-b84d-b58c3d982728 | -0.99465 | -53.70509 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9e7a3c8a-bea4-3536-a1c3-7593ab55f30c | -0.99393 | -53.70966 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6e082fe1-c134-3951-8c97-1b8b091a285f | -0.99304 | -53.69076 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b3dbeb8-6b6e-30dd-9b65-9870a3beff02 | -0.99232 | -53.69534 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e152c3b1-7226-3f8a-8ed1-5bb90d54d636 | -0.9916 | -53.69991 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 94509166-b3e6-338d-ab1a-7dd1e81a1379 | -0.99088 | -53.70448 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 98a0aa96-6af0-3ddd-aca0-43867249327b | -0.99015 | -53.70913 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 64f8f88d-ad47-353f-8421-eed39c358780 | -0.98999 | -53.6856 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de03c262-4ba1-3f8f-b6d3-96b43cb3c79a | -0.98942 | -53.71378 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 759c50f6-667e-3c93-815c-be68f3718d14 | -0.98927 | -53.69016 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0891767d-9918-34d8-9b12-5818bb7ba15c | -0.98854 | -53.69479 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6a56ee8d-6771-3233-9a74-74302e38f644 | -0.98783 | -53.69935 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f9273a37-0573-33a0-a622-4368ecc5f137 | -0.98712 | -53.70387 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 7f57650a-add9-313d-b64d-11707276edc3 | -0.98638 | -53.70856 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 97446dd9-ff58-34f2-8c65-99b201ef27f6 | -0.98564 | -53.71326 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ce3af5c-497e-3962-a29b-c2420655b4ff | -0.98549 | -53.68959 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95522d7c-b537-3794-90d7-0b058b15422d | -0.98476 | -53.69427 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 77f56bdd-554e-32b6-99e5-985169a113c9 | -0.98405 | -53.69882 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ac2e5918-cdd7-3bbf-8b40-863a8374578b | -0.98334 | -53.70329 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| d7ad6e4a-c5ab-3d76-9a48-d42e4be462e6 | -0.98261 | -53.70795 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 8f88cefc-d032-30ec-b2b1-d28a146027fd | -0.98187 | -53.71266 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92f5eab1-6261-3939-9437-3f359609cc77 | -0.98171 | -53.68908 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 379763ca-46aa-32bc-9751-2594ff67955f | -0.98098 | -53.69376 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f27156b-c755-3c75-a6cf-e9788cbfc6f1 | -0.98026 | -53.69831 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc4b426f-aa79-3fb3-8d62-6e7697a95237 | -0.97957 | -53.70273 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| acaa2fce-306c-34f6-87c3-92da97bf91ff | -0.97884 | -53.70737 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 552680da-91f4-335b-8dfd-f051558b6be5 | -0.9772 | -53.6932 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53f25951-8069-3c04-a57d-26bd2e71745b | -0.97649 | -53.69775 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0fc42023-cf9c-3ee3-a869-793809581381 | -0.97578 | -53.70228 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de5e7f48-0851-3f7b-9973-15846d323ab4 | -0.97504 | -53.70701 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d09e0516-5e53-3946-9a54-6a351dcadbb4 | -0.87693 | -53.68851 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4507dec5-f5e7-3c67-ab62-4f938fab4483 | -2.20744 | -53.6914 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 253b54ab-41c8-3a64-bcb2-ecde06573981 | -2.20649 | -53.68821 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7a91be2-ef99-342c-8ac7-2892b75d059a | -2.20578 | -53.69292 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 690b6281-0aba-336e-a4f9-17498d1be457 | -2.2036 | -53.69083 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a46cdd4-a757-34ee-a852-bd0ccfc20cc9 | -2.20194 | -53.69237 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6370df37-1cef-3b79-9ebb-4aafeb18ef26 | -2.19381 | -53.72825 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36463c66-a43a-3c5e-8011-d9855c82337e | -1.88102 | -53.59513 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eee6667f-4535-33e3-aa88-3a6906287cbd | -1.57792 | -53.5145 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 07819ee8-6571-39b4-9e01-b1d70cceb5a9 | -1.57591 | -53.5125 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c2b2653-a48f-3326-8657-f484a740841d | -1.57515 | -53.51731 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6df3bf0a-c8f3-3228-87a7-5b373a66fa71 | -1.43771 | -53.42472 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a3bec2a-2f55-3695-885f-83e3a5c49a66 | -1.43698 | -53.42949 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f250016-d963-3b35-8510-a598e117837e | -1.43386 | -53.42411 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 333f982e-e46a-38dd-8381-2234ee02bf12 | -1.43312 | -53.42888 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c87a54c2-3f36-3f2e-a4f9-544c97d8f747 | -1.18355 | -53.66362 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be8f4c9e-b926-3ad7-a0f4-689f41961938 | -1.1278 | -53.4493 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f12cb125-3d79-3d2c-898e-c9a1b3b4487c | -1.08021 | -53.6543 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f5eb181-8d5e-3bd8-bcf2-ba083c9a7d0d | -1.07342 | -53.64803 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aebc5fef-b909-3c18-8f46-aed7a302b18f | -1.07194 | -53.65759 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc9d78f9-349c-3742-b386-21b2949ab33b | -1.07121 | -53.66235 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b6cf851-5f79-3154-abad-2e0b5d5579ce | -1.0705 | -53.66688 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d359f2dc-930c-38b3-b550-5cf6a5fdafa3 | -1.06816 | -53.65696 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74dde69b-0e99-3e61-81b6-8f900df7b976 | -1.06743 | -53.66171 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aad53796-85f5-305b-8bd7-f33f600a53eb | -1.06602 | -53.67081 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 992a0f04-7a9b-3753-9ae8-be1d4155b60a | -2.89133 | -54.89905 | 2024-10-27 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ae62d3d-43d6-32d3-9d19-bcc54329797d | -2.88938 | -54.89695 | 2024-10-27 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd6bed4e-a252-302a-898d-fa5176a2e403 | -2.88875 | -54.90114 | 2024-10-27 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2425c2cb-645d-3d01-865b-2b20b2936039 | -2.88837 | -54.89431 | 2024-10-27 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24bdd084-23bf-3115-929a-f5b7f4bb9ce4 | -2.88772 | -54.89851 | 2024-10-27 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec95106d-cc3d-3515-b13c-d8d3e7c6e188 | -2.8397 | -53.98771 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5c811a5-ed47-3fe1-9743-b9e9f758c284 | -2.82105 | -53.90953 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 091849fe-8673-3b37-90be-ee19638fc7a6 | -2.79208 | -54.02058 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f27c88d1-238f-31a0-9990-3d7365a3894b | -2.77825 | -54.73692 | 2024-10-27 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| de94ee73-193b-3c06-b232-0ce3c1153dd3 | -2.77489 | -53.95555 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed025337-d504-305a-a6c9-bc3cff8e6316 | -2.7627 | -54.03497 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02819557-18ad-3e9b-a377-ee76fbc37b8f | -2.75134 | -54.03318 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88aedffa-83fa-3ee4-af5f-ef09793d5b41 | -2.64058 | -54.29702 | 2024-10-27 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1f38f75f-b7f2-3945-8c7c-6a207e699190 | -2.56734 | -54.01949 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59b5b53c-4f88-30bd-9014-04a5dd602a0c | -2.56663 | -54.02408 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a5ad35e-a106-364a-8c37-9e76e9f84526 | -2.56356 | -54.01891 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d822e40f-bf75-3268-b2b1-6e370f1a41bb | -2.56049 | -54.01373 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efb50088-c608-3078-921e-874ed9f4bd06 | -2.55978 | -54.01832 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a0f0ce3-2a9e-3bcc-934b-8e416a385e04 | -2.54371 | -53.99689 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af55dff6-a549-3f94-a8c5-2e53b11d2856 | -2.543 | -54.00151 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac193b01-a325-3ae1-9f44-037abd8fddf7 | -2.53994 | -53.99619 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed6ce9c8-7deb-3554-b53e-77c0d26e33e0 | -2.5393 | -54.65954 | 2024-10-27 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac5e4404-5b88-322d-8dc9-3ef6fac2d5bc | -2.22448 | -54.4888 | 2024-10-27 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4898adba-7cb3-3385-83c6-128c2bfdc2c0 | -2.21375 | -54.82385 | 2024-10-27 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e96115bf-a783-398b-8349-2c161f64475c | -2.94619 | -53.70221 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a67eb63-9936-3dbf-acc8-00d897eeb014 | -2.27052 | -53.62956 | 2024-10-27 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0af7da8b-87b8-384b-81d5-3113a0b49054 | -3.21129 | -54.94658 | 2024-10-27 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6e115de-9b07-3111-9b41-ab2e30d800d0 | -3.21055 | -54.9439 | 2024-10-27 05:16:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b1c54b3-27a8-3944-9b19-5a7aa078a59c | -3.07931 | -54.17057 | 2024-10-27 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e6a257f3-bb2f-31d5-83d2-ea03fde629e5 | -3.07553 | -54.16999 | 2024-10-27 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3a3e6ac0-a66d-36cb-ae35-a21b39a2fd2a | -4.50448 | -54.96234 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README61.md)
