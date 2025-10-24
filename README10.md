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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cf0eb94-b094-339b-9cb1-f21d078f6a39 | -12.25637 | -44.07587 | 2025-10-24 03:49:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cd846fe-ebc6-3922-b0c5-177cea6a566e | -11.35811 | -45.96526 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aa1b1d64-ddbb-31aa-ac38-81e6d11eaffc | -4.29079 | -40.70378 | 2025-10-24 03:49:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4cea4c2c-efd6-3b6c-a22a-4b8caf661475 | -5.24081 | -37.7316 | 2025-10-24 03:49:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 80dd90e9-f348-3895-bc83-cb9ee191bd29 | -12.82569 | -48.67119 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 325cf1d0-9e48-3211-af0a-5b65473c06d8 | -4.28236 | -40.7066 | 2025-10-24 03:49:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b6087987-f06c-3c47-8b69-c228c9c7e62c | -10.2745 | -47.87846 | 2025-10-24 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da923f8a-5e97-3713-a77e-10e7c3107329 | -11.35529 | -45.9533 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6e9b4085-2155-3735-8858-faa2a4bf3bdd | -13.67112 | -47.9586 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5c5cccb-5bef-3894-adb2-ffdb7d54bff6 | -3.92374 | -47.69787 | 2025-10-24 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b964a9e-8271-3eb1-a829-0910d8639a45 | -13.29994 | -47.44928 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76366356-3d71-3426-b6c4-3d92b82594a5 | -10.42362 | -49.37031 | 2025-10-24 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ef766c57-b3e7-3ce4-99c9-5cbf5ad5ab9d | -11.77745 | -47.55593 | 2025-10-24 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd724225-b670-36fa-b2a4-578dd6121ae9 | -9.25742 | -46.46259 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 845bb1d4-5819-3bff-b1cd-58af5862797a | -5.18465 | -35.66518 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c9b7afe-d53e-3f94-93c4-06c9958e30a2 | -13.34482 | -47.97802 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c3938f6-8f0d-3bd1-ae9b-1b032d35f079 | -9.6414 | -46.89358 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fa4d227-7672-38ce-9fa6-a2f59b65dd20 | -4.31634 | -48.22858 | 2025-10-24 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0686cd2-79c8-335f-b1f1-21c1e15d36e4 | -12.0218 | -46.92355 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9edbeb6e-73cf-3607-9c00-c86fff94593b | -14.0264 | -48.00654 | 2025-10-24 03:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20298e34-f5eb-36a5-bd66-a7b5ee9b27e3 | -13.76439 | -48.34453 | 2025-10-24 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 798cb642-433f-3c38-bde2-35724701a1af | -5.52134 | -43.8775 | 2025-10-24 03:49:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5206a805-d1ba-3656-aa27-2c80b779cc3b | -11.36836 | -45.93777 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b7253ab8-9617-3fbe-a417-484a05bab0e9 | -5.68544 | -38.59366 | 2025-10-24 03:49:00 | NOAA-21 | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6eb3f1d0-409c-39e1-af3e-2b51b32b3498 | -9.62353 | -46.88712 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 373ee5df-d3ef-3a7c-b896-20e9da76a3a2 | -2.42246 | -49.27642 | 2025-10-24 03:49:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 71b4c0ff-842b-38ed-8f94-6185fdcd4da3 | -2.47219 | -49.23671 | 2025-10-24 03:49:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 309d3271-e035-3835-bd76-a184366aa91a | -15.8348 | -49.10229 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| db25df47-baa3-3450-96c2-2f4dba9688dc | -14.54245 | -48.0333 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88f18395-bdfb-3c72-9760-812808d06388 | -10.95146 | -50.36966 | 2025-10-24 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4731f342-bebf-35c6-9762-ef8c5160ac09 | -11.3634 | -45.93719 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2be75dd6-4071-378c-8c0e-5b95430f6426 | -13.88595 | -48.36575 | 2025-10-24 03:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b22ee1a4-de95-323a-9471-805dfd4029db | -10.64172 | -42.30276 | 2025-10-24 03:49:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 284ef76e-f45d-3125-923e-10dbd000ee96 | -15.84002 | -49.10033 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 982b41c0-d136-366a-ba06-635e0c7f2848 | -4.6437 | -42.51616 | 2025-10-24 03:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0d5dc6a9-5f88-3b0d-8505-4b107b062fff | -5.61149 | -41.12546 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a34ca77a-39cd-3dc5-9606-4f7af5e400de | -9.24541 | -45.59129 | 2025-10-24 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 086c5da8-c7ee-394a-a790-bd85ab55dabd | -4.18154 | -42.98265 | 2025-10-24 03:49:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 252544c9-6ba0-3c07-a401-140ee99c4e30 | -12.92607 | -48.50596 | 2025-10-24 03:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d1388cc-3e84-3258-8e3e-2baf9a33dcfc | -9.60206 | -46.91293 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 48a8ff42-9174-3f17-baff-e4af2d870057 | -12.17589 | -46.56639 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0104a029-642c-3704-812e-b20efd176864 | -15.31211 | -46.89183 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20758476-f5f9-372f-a347-74c3a95f34a2 | -13.30534 | -47.44942 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4eae33d3-1c2a-3b31-a687-2df6cb61b0d3 | -12.31579 | -47.26135 | 2025-10-24 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9f00cf36-ca69-3509-97e1-6bdeaf6c51b1 | -11.35464 | -45.94571 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 12ed042c-dd51-3e9e-a8c6-e302abc397b2 | -3.70314 | -47.64903 | 2025-10-24 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 775ff6ea-b547-363c-bd76-ac2d163288cd | -12.18148 | -46.56436 | 2025-10-24 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cd8ebc6-ba33-3cbf-82fb-5dfd5c0b1920 | -5.18411 | -35.66865 | 2025-10-24 03:49:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5b9c289d-5fea-3a93-bb0e-ae904e38f785 | -9.63296 | -46.89639 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4efbf72a-0588-3465-b444-697367872427 | -12.29417 | -47.45752 | 2025-10-24 03:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d1079e3-7659-3ad7-b186-3826297d7bed | -11.99266 | -43.32874 | 2025-10-24 03:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a60c35c6-b5e7-38d9-88c8-65ed3211b911 | -13.40388 | -47.36252 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af58dbdc-4b21-306b-a6cb-08a58ca4a2d9 | -4.9052 | -43.22087 | 2025-10-24 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 755218b4-e2d5-3347-99df-8495e80179fb | -4.24656 | -48.55259 | 2025-10-24 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f906e4c2-f554-3617-8e8d-952a76d12469 | -14.46825 | -47.91552 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab2da11d-ca5b-3e23-8ee5-487c030017ce | -11.77812 | -47.55239 | 2025-10-24 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d8ea3b2-bb2e-34c0-a919-98737b99cd45 | -5.0655 | -40.4743 | 2025-10-24 03:49:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 188d669b-9d3f-3178-95e4-3cd5639afe46 | -8.87321 | -48.30276 | 2025-10-24 03:49:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 06bd86cb-b923-3117-ba1a-bbfcc92703a4 | -14.43695 | -50.9589 | 2025-10-24 03:49:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a51d2d3d-e250-3119-ba6d-3777b11b3b60 | -9.09751 | -46.53478 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 698a3aa3-34bd-30d0-ae7c-e2618284037c | -11.46478 | -43.70531 | 2025-10-24 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e18a85d0-06c4-3e5c-9495-f4592c977347 | -11.46407 | -43.70931 | 2025-10-24 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d9af5dc-cc48-33f1-be91-4b26e253af00 | -3.70454 | -47.65221 | 2025-10-24 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 664ef3dd-972a-31cd-99d9-f51727314e49 | -10.02001 | -47.08346 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3958106-61f7-3f1f-8b62-d8cc11120423 | -4.27737 | -48.33842 | 2025-10-24 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40cf2691-fa6e-34e9-a6c9-230510718f87 | -9.78284 | -43.85565 | 2025-10-24 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b35ee0fb-3554-35d9-a384-d7622b9b6dac | -9.26331 | -46.46009 | 2025-10-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eac91b4e-f935-366d-92e3-75d719b4cf04 | -9.6047 | -46.89868 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aba19530-9314-3b55-8da1-5f3e9bf74e0c | -2.74411 | -47.13917 | 2025-10-24 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8651bf25-4623-3ebd-b201-d76ea6e8060b | -4.27466 | -40.70491 | 2025-10-24 03:49:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 42aa79f3-1bf1-3d48-a38c-43efe3fba9fe | -10.04513 | -47.09912 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 368d096f-c445-3133-b9bc-a727e947e94a | -3.47487 | -43.24351 | 2025-10-24 03:49:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71891a94-1c61-3f2d-9b46-74b03ac98f91 | -9.25218 | -45.3491 | 2025-10-24 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00558de8-2741-38f3-8aa6-9aa6a78878ab | -4.87227 | -47.53413 | 2025-10-24 03:49:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b5113813-036e-31fc-882d-1f7058a0eca9 | -10.0423 | -47.08404 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 304b5cd7-166a-328a-9ae3-60bb13adba47 | -12.82725 | -48.63374 | 2025-10-24 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5d55243f-2315-3f09-9b9a-3680c61489b9 | -10.63047 | -48.08374 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ff6f2f69-1dab-3e21-a930-be8d0d9f74a4 | -14.53988 | -48.02597 | 2025-10-24 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22a31d66-fd23-37fa-9817-4caa1fa7c9dc | -14.42426 | -50.95614 | 2025-10-24 03:49:00 | NOAA-21 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54873ff1-776c-3303-8d5e-006e774f87ef | -9.62417 | -46.88369 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33997410-178f-36a2-ad6e-1cad2b51f953 | -13.34606 | -47.9716 | 2025-10-24 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cef22f71-911f-3b4a-9063-b56083583f03 | -4.54986 | -46.73785 | 2025-10-24 03:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72bf2d98-d01d-381e-946c-fa046068cfef | -4.27851 | -40.70578 | 2025-10-24 03:49:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5d53e0e8-77a0-3374-92f7-1470eb4e902a | -10.89639 | -48.04959 | 2025-10-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7966da5-ad24-3ebb-b3d6-136b77dd9b8b | -9.60604 | -46.89141 | 2025-10-24 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04cedb91-c742-3ecb-b194-9b67048fa2f2 | -12.15563 | -47.02194 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a68724ff-c045-3202-931f-695eeeaa14cf | -11.47967 | -43.2447 | 2025-10-24 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f8047379-452c-3f1b-b41e-dbf7a0206477 | -15.5725 | -47.71862 | 2025-10-24 03:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18957e49-a06e-301b-9b38-0261bfef2ce3 | -3.01673 | -49.45025 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0172370e-3f30-3825-9387-7faa9dacd8c5 | -12.02307 | -46.92326 | 2025-10-24 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 988c0652-bc6b-34e5-ade6-f50839a3fde6 | -3.23558 | -48.75922 | 2025-10-24 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4970bd10-e62d-381c-9abb-3dc15dc30577 | -4.84492 | -47.8012 | 2025-10-24 03:49:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a71a5b37-798c-348f-a476-02d0e0b4006c | -16.48256 | -46.47571 | 2025-10-24 03:49:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21b9b082-740d-306a-a8a6-4f9363f5d3e6 | -9.60785 | -44.62214 | 2025-10-24 03:49:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fe556e1-4f85-301b-93a8-7f3f9379d75c | -3.12532 | -49.10672 | 2025-10-24 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 14c20573-8dc8-3923-8293-bf3577d58264 | -9.86965 | -47.46471 | 2025-10-24 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7d31336-4690-33e5-847e-71f2aaf4acd1 | -15.83567 | -49.09797 | 2025-10-24 03:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 06bfe71c-bcba-31d7-8f82-ee8e6e1840c0 | -2.41642 | -48.43726 | 2025-10-24 03:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 39209682-4630-3649-9791-b54d77c6f63d | -14.76619 | -49.29271 | 2025-10-24 03:49:00 | NOAA-21 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c6397c2-7207-348f-9fc8-7586ef8a3e78 | -10.88794 | -46.04469 | 2025-10-24 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README11.md)
