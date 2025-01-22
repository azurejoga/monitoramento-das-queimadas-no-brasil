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
| de009429-788b-303f-952d-78ca6ae63ee4 | -11.0495 | -45.037701 | 2025-01-22 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e5cdd740-ffd7-3c20-9856-3ac1fa8e5517 | -11.1523 | -40.614498 | 2025-01-22 00:06:00 | METOP-B | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f6160609-69b4-3e2a-98d3-fea62dd0a6ef | -11.0511 | -45.0452 | 2025-01-22 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0783c9a7-2785-347c-b10e-65fab91a7885 | -9.0555 | -35.620399 | 2025-01-22 00:06:00 | METOP-B | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c30c119c-37a8-3894-a52e-5af4ee3b3af4 | -21.2024 | -48.630001 | 2025-01-22 00:06:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb0c3d9c-c3f3-331f-9f06-4f8da894b1e9 | -21.199499 | -48.6134 | 2025-01-22 00:06:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d4d43e64-bcb6-3411-a4c1-fafd05359ac6 | -22.685499 | -42.846401 | 2025-01-22 00:06:00 | METOP-B | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a7b4a1b9-5e51-3641-938e-c07336d955e8 | -18.723499 | -40.563801 | 2025-01-22 00:06:00 | METOP-B | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4dd57368-fccd-3c0a-94f7-c2e0e050cb6d | -5.3697 | -45.165901 | 2025-01-22 00:06:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acc18038-bb32-37df-aa2b-5fa9d69f5506 | -13.8289 | -41.722401 | 2025-01-22 00:06:00 | METOP-B | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6279860b-fe2f-3814-9f8e-b0b508b034fb | -11.2404 | -40.371201 | 2025-01-22 00:06:00 | METOP-B | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 324ccbe4-1976-3684-a5c0-5823ffed60c9 | -3.2323 | -46.796501 | 2025-01-22 00:06:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 153a29f2-d578-3094-8c21-1f9bad53e72b | -11.9002 | -40.949699 | 2025-01-22 00:06:00 | METOP-B | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 89b0c871-aa90-367a-a883-f808c79c5fd1 | -11.0396 | -45.039799 | 2025-01-22 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d849d84-882a-3303-8cce-151ba99fe4b1 | -3.2306 | -46.789101 | 2025-01-22 00:06:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec47db79-e577-33ce-a914-79fc639be6da | -11.0478 | -45.030102 | 2025-01-22 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0280ec6d-870a-3f02-9042-f0a5427783a0 | -18.676399 | -40.306198 | 2025-01-22 00:06:00 | METOP-B | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 92e27333-c29d-385c-8902-b135e7a220fc | -18.622601 | -40.249901 | 2025-01-22 00:06:00 | METOP-B | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b54f59dc-0533-333a-b861-53a92f6fa33e | -18.7251 | -40.571098 | 2025-01-22 00:06:00 | METOP-B | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e5ba5b00-aef5-3306-bda9-851f8890cc20 | -15.8852 | -38.984901 | 2025-01-22 00:06:00 | METOP-B | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0df0f4a0-4923-34c2-b70c-9ec677e2ce2e | -10.623 | -37.000401 | 2025-01-22 00:06:00 | METOP-B | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84d034a1-184a-3a4e-81fb-d417b8a20ab9 | -11.1505 | -40.6068 | 2025-01-22 00:06:00 | METOP-B | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3b14613a-98e5-3933-9b61-4d7a1d590d7d | -11.0412 | -45.047298 | 2025-01-22 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fae7fed9-10b7-3028-9f5d-a37b0b2bf26b | -22.6936 | -42.8358 | 2025-01-22 00:06:00 | METOP-B | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c67c7e1-2094-3171-a788-7baf7d594f3a | -13.8304 | -41.7295 | 2025-01-22 00:06:00 | METOP-B | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e424bd81-cb39-33f9-9a30-3b31f21bbf90 | -11.9474 | -44.535198 | 2025-01-22 00:06:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f470964-c4c2-3508-82f1-ba6540e69606 | -22.696899 | -42.852501 | 2025-01-22 00:06:00 | METOP-B | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7545b2b3-b4fb-31c8-adbe-790208f81067 | -16.7687 | -41.042801 | 2025-01-22 00:06:00 | METOP-B | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa736804-e751-3bbe-a050-587dcfa47a1b | -5.3712 | -45.172901 | 2025-01-22 00:06:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e777786-2425-3edf-ba6c-c8a4327687b2 | -22.695299 | -42.8442 | 2025-01-22 00:06:00 | METOP-B | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e7bb541-c972-343b-98d9-0a61d11519a5 | -9.0458 | -35.622799 | 2025-01-22 00:06:00 | METOP-B | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6cea18f0-cb7c-3719-a36c-3aec31018e02 | -9.0379 | -35.6809 | 2025-01-22 00:20:00 | GOES-16 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| b3887901-ff35-3ece-a143-e3d6a31f631d | 0.8849 | -59.3243 | 2025-01-22 00:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c06b1039-d6bf-3d8a-995d-54965090ba68 | -9.0571 | -35.6778 | 2025-01-22 00:20:00 | GOES-16 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.2 |
| 4dc38940-c60b-3a5a-afd0-5b901dfb86a5 | 0.9939 | -59.8771 | 2025-01-22 00:30:00 | GOES-16 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5b78b87a-3d30-3932-a58a-f82e8563db5a | -9.3427 | -35.8205 | 2025-01-22 00:30:00 | GOES-16 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| 40cd7dcd-4642-3c33-9d3b-020d1621032f | 0.9939 | -59.8962 | 2025-01-22 00:30:00 | GOES-16 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 346bdd94-bb88-3235-9a98-6756fb2d3319 | -21.10879 | -47.7658 | 2025-01-22 00:34:00 | TERRA_M-M | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d73cb3cc-e167-3b96-868e-9e99f064a7fc | -21.11051 | -47.78163 | 2025-01-22 00:34:00 | TERRA_M-M | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 437ccb1c-da05-3232-be27-276229a3e662 | -22.67332 | -42.85641 | 2025-01-22 00:34:00 | TERRA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 0067d5e9-5d66-3462-9a7d-1d450a86e876 | -21.18374 | -48.6344 | 2025-01-22 00:34:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 49efcce4-6b0f-32b9-94b9-94f9fafd200f | -21.18999 | -48.64628 | 2025-01-22 00:34:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 2e02d3c2-4678-34be-82ba-75de8fba668d | -18.61287 | -40.2542 | 2025-01-22 00:37:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| d514d341-eea4-3202-ad07-a31058cf28c4 | -15.26863 | -51.48757 | 2025-01-22 00:37:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 7003b16b-2551-3806-a00f-4e2f6ab51dcc | -10.71152 | -36.99095 | 2025-01-22 00:37:00 | TERRA_M-M | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 1c228f16-91d8-34b6-aaa0-c7fd3ba78abe | -10.7089 | -36.998 | 2025-01-22 00:37:00 | TERRA_M-M | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 86c7fd4f-06d2-31a8-a2ef-ec845df8e749 | -15.27442 | -51.48021 | 2025-01-22 00:37:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 5153dc4f-e0b6-3d78-bea9-cd626a7b4b83 | -11.22992 | -40.37498 | 2025-01-22 00:37:00 | TERRA_M-M | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 1a23a1af-12f8-3e51-a3b0-6320c6ba9a6e | -13.82217 | -41.73278 | 2025-01-22 00:37:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e40aedf4-facd-3c1d-a395-614ee134bd08 | -11.93159 | -44.54805 | 2025-01-22 00:37:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a533de95-2a42-3aea-b934-969353a08c1a | -18.71252 | -40.5779 | 2025-01-22 00:37:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 18864c8a-faa8-3b95-ba15-bea266b3f17b | -11.88205 | -40.9577 | 2025-01-22 00:37:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e90fa663-4d4a-32bb-b720-acb82b89d41d | -3.67598 | -45.22217 | 2025-01-22 00:39:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bd666c69-7b64-321b-b91f-b9db6b7b90cb | -3.22354 | -46.80911 | 2025-01-22 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5af6ba53-6b31-35f7-8880-1199df949c72 | -3.22232 | -46.80031 | 2025-01-22 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 01e0ac90-34d4-3d65-9cfe-7848482964cb | -9.40116 | -35.68046 | 2025-01-22 00:39:00 | TERRA_M-M | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 36.8 |
| 9879cba9-0e7e-3d21-97ba-4e48e5931f30 | -11.03506 | -45.05087 | 2025-01-22 00:39:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| d75dafa7-4c46-395e-9de4-b0165cbb105f | -5.35641 | -45.17641 | 2025-01-22 00:39:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1d842be5-da31-3ac8-9b3d-7dbb117b7d3b | -3.26077 | -46.93289 | 2025-01-22 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94f32d28-f14e-33af-89eb-5c7c2206903e | -11.14226 | -40.61863 | 2025-01-22 00:39:00 | TERRA_M-M | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 53741ab0-7652-3a7e-be5e-3ea2b493c4a7 | -11.02622 | -45.05214 | 2025-01-22 00:39:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2a89604a-e420-3e4c-a4d3-6938090d38ed | -11.03382 | -45.04192 | 2025-01-22 00:39:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c72f1df4-1943-3523-9177-b7082261d963 | -3.25153 | -48.0742 | 2025-01-22 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 673586b8-61ec-3fdc-806b-107b3be30ed3 | 0.8849 | -59.3434 | 2025-01-22 00:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 3485fc59-d088-3ec5-8da0-d03ec97415ac | -15.2853 | -51.472198 | 2025-01-22 00:58:00 | METOP-C | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a481949d-d8d9-350f-865c-724dc9111ef5 | -20.722 | -55.4244 | 2025-01-22 00:58:00 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f6dd2d89-ab24-32ef-9def-aaab8d9b1554 | -20.7122 | -55.426498 | 2025-01-22 00:58:00 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e9ff6815-b614-3dc3-850f-1d7a6d43ac38 | -15.2869 | -51.479301 | 2025-01-22 00:58:00 | METOP-C | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 013c85fa-fd2c-301e-a359-f95f6e17b8f5 | -2.162 | -53.648602 | 2025-01-22 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86878e13-2421-315c-a9f1-669e6f897dc8 | -21.113199 | -56.264301 | 2025-01-22 01:01:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ca0684ee-c0dd-355b-8ab4-25d449d98115 | -21.203699 | -48.639301 | 2025-01-22 01:01:00 | METOP-C | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d2e79bac-0b88-3205-82b5-1156e9f578f6 | -21.2019 | -48.631599 | 2025-01-22 01:01:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1eaf54de-00a1-3429-96f9-6b4770c03e9a | -21.115499 | -56.2766 | 2025-01-22 01:01:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b591d93d-d368-3ccd-a64c-6b6df55bcac5 | -2.1604 | -53.641602 | 2025-01-22 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a56432a-59d4-3482-9613-156ae32eb0f0 | -21.0996 | -56.2715 | 2025-01-22 01:45:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5a558d04-958a-377c-b07b-2caf24d1c3ca | -7.49088 | -35.1508 | 2025-01-22 03:04:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dcddbace-5e11-3c94-8789-4ac23cfe59bb | -6.80405 | -35.18424 | 2025-01-22 03:04:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0e02ca96-5fa8-3e92-8ec1-30e7ca21ccaf | -6.76685 | -35.17365 | 2025-01-22 03:04:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 013cb470-55c1-3488-ac8f-8962ad75eb3c | -7.48896 | -35.15078 | 2025-01-22 03:04:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2ae26211-cfb1-3719-9714-ae2491b2b6b6 | -6.80344 | -35.18772 | 2025-01-22 03:04:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 72e324c4-981c-3511-9179-cf8047d131f3 | -7.48556 | -35.14974 | 2025-01-22 03:04:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 751b0744-760f-3da1-830f-b5ae8ee8f8d8 | -6.76748 | -35.17012 | 2025-01-22 03:04:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| acc1f882-19c7-3bed-82f9-253fe79f431c | -9.01697 | -35.4406 | 2025-01-22 03:04:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 6fdef7f8-7278-3ed0-9869-5162775c3df4 | -6.7681 | -35.16661 | 2025-01-22 03:04:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e82bb2d1-3204-3923-b624-266703038d0b | -9.01637 | -35.4439 | 2025-01-22 03:04:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 0623c315-08d1-344a-950f-605d4bbcafea | -10.7089 | -36.98146 | 2025-01-22 03:06:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1a867fde-a23e-361d-9ce9-af4561533d2d | -10.70811 | -36.9855 | 2025-01-22 03:06:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 947b822b-19d4-388b-ac56-b686e78d5f15 | -11.23417 | -40.37953 | 2025-01-22 03:06:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bb119cda-e0c7-3de0-a294-98e94a541eea | -10.7118 | -36.98692 | 2025-01-22 03:06:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fb7cdbcc-0e81-30a6-840c-a1c803af429e | -10.71257 | -36.98282 | 2025-01-22 03:06:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 56e5c563-91ec-3c1a-ac26-43726d5f405b | -18.61192 | -40.25641 | 2025-01-22 03:08:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 520f3e2e-ee3a-3a0b-b7c2-413901f18e7b | -18.60702 | -40.25745 | 2025-01-22 03:08:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3e9f3931-38f1-36a3-9c53-44164937ff9a | -18.61408 | -40.25413 | 2025-01-22 03:08:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| dd016939-32e5-3e4a-a7f8-ddab8940b793 | -18.61301 | -40.25885 | 2025-01-22 03:08:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 23056812-1312-3a68-a54f-9f5b64df9847 | -8.98406 | -35.61515 | 2025-01-22 03:29:00 | NPP-375D | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fa23771a-24b2-3525-b80d-d798b19c2a68 | -6.80319 | -35.18528 | 2025-01-22 03:29:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0d185081-65f6-3509-b27c-0e970412c9f9 | -8.72415 | -39.55125 | 2025-01-22 03:29:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f4870164-b24f-31e8-a8cf-397950a04caf | -7.47568 | -34.84385 | 2025-01-22 03:29:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e8fcf29d-9edf-3530-bb82-d0c737e8db62 | -8.98763 | -35.61573 | 2025-01-22 03:29:00 | NPP-375D | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 140a0b59-2bb8-3fab-a086-72da282d054a | -7.95925 | -35.24297 | 2025-01-22 03:29:00 | NPP-375D | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)
