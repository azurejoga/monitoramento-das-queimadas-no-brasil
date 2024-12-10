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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d59e0951-bb8e-3e31-bea2-5b2159be7881 | -12.5615 | -58.3546 | 2024-12-10 01:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 9ae0bd71-1635-3462-9d1e-caa55035e1a8 | -5.9183 | -48.0667 | 2024-12-10 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 6b1d3a8d-0826-3b04-ad31-a7af8f5fce1a | -5.9185 | -48.0449 | 2024-12-10 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 8459ce73-654c-3a58-9353-9486b30ea242 | -2.9859 | -52.8554 | 2024-12-10 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| ac8db93b-8f7c-3b2b-8791-35e52bf7faf3 | -11.5426 | -56.4438 | 2024-12-10 01:20:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 23f4d49b-6e68-36fa-933c-178e3e57900e | -3.0043 | -52.8549 | 2024-12-10 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| e88907a6-bd8f-33ca-8d82-04527cae3c48 | -4.3774 | -47.7627 | 2024-12-10 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 571c8ce2-5877-303e-9924-c2f7578f90f2 | -12.5425 | -58.3561 | 2024-12-10 01:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 2a3493e2-f8ed-309c-aa47-bdfc017c1957 | -2.9119 | -52.959 | 2024-12-10 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 5bcd833a-ac43-3a8b-9463-92ad2ce6fac6 | -5.9183 | -48.0667 | 2024-12-10 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 754f10a3-2226-3da9-a0c4-a1c48c06104f | -4.3961 | -47.74 | 2024-12-10 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ef7928d3-87ee-3301-a86e-4b684f9ca8cd | -2.8199 | -52.9816 | 2024-12-10 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 294a017c-1257-39cb-b941-09fe1f59fba3 | -12.5615 | -58.3546 | 2024-12-10 01:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| b41b0672-2aea-3710-88e1-89f3697c2eae | -2.986 | -52.835 | 2024-12-10 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 40d71959-e368-32ea-92af-1f2429bd04dc | -6.9158 | -43.5185 | 2024-12-10 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 2caa076b-e18a-35bb-a0e9-dcdab9a3be3f | -5.9185 | -48.0449 | 2024-12-10 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 14cf6ae4-067a-3016-9915-9a35f2a3234d | -3.0043 | -52.8549 | 2024-12-10 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 7389e93c-d919-38e8-bbe6-0a68b070cfbd | -3.0044 | -52.8345 | 2024-12-10 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a04a58f9-b729-343c-b25f-6683e06d1e91 | -2.9859 | -52.8554 | 2024-12-10 01:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| ef10c616-5df7-3edf-b95c-d668dc3b897c | -4.3774 | -47.7627 | 2024-12-10 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 9b4016a1-cb5a-3420-8f77-4c3428f20541 | -12.5425 | -58.3561 | 2024-12-10 01:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| f0c24f9b-3caa-3a21-a48d-e79498ccaa9c | -11.5426 | -56.4438 | 2024-12-10 01:30:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 4bbb5580-5f71-329d-9df8-abdb83ab0ed2 | -4.3959 | -47.7618 | 2024-12-10 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 88af9eb6-de99-362a-8db4-4c4d3424fb76 | -15.9898 | -57.1576 | 2024-12-10 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bb3a62f-99c5-3b59-b7cd-3c3482f543c3 | -14.2799 | -57.442501 | 2024-12-10 01:30:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 477bd80c-635c-3bba-9dbd-082ed5fa68f4 | -15.445 | -57.7994 | 2024-12-10 01:30:00 | METOP-B | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1398a12-c5a5-3cda-94d0-6812cc93f2e0 | -12.5545 | -58.330002 | 2024-12-10 01:30:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46607bf7-aeea-3e91-8b8b-4dfdfbc60b88 | -13.2069 | -56.875801 | 2024-12-10 01:30:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e64d1215-4357-3435-87bb-016f539db227 | -12.3619 | -54.155201 | 2024-12-10 01:30:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5f69b01-ae5d-3d9d-a025-0befc7c912a2 | -12.2296 | -64.247597 | 2024-12-10 01:30:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b3916a96-4ea7-3389-af18-f0e058125332 | -12.0785 | -64.216003 | 2024-12-10 01:30:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 891b379a-fd80-3c1a-9ffd-6c90acd03d55 | -11.5342 | -56.4305 | 2024-12-10 01:30:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f9b4891-79f8-3f03-a1f4-2e6c4284896e | -11.5245 | -56.432999 | 2024-12-10 01:30:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 094469ff-373e-3aa2-a7c0-47ce226b79c6 | -11.5382 | -56.446301 | 2024-12-10 01:30:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3fef1857-ecb2-3f7e-b3c7-ddea157c8a7f | -12.5475 | -58.343899 | 2024-12-10 01:30:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4e11488-153a-3e59-92b2-20c6da8f265d | -12.2311 | -64.254601 | 2024-12-10 01:30:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93b51faa-648a-3f58-be26-12593d5842a4 | -12.5447 | -58.3325 | 2024-12-10 01:30:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a9c7956-7d06-346b-8826-4e894d61608d | -13.2034 | -56.8619 | 2024-12-10 01:30:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5a56cd0-59a8-399f-a873-6b1353eec580 | -12.5378 | -58.346401 | 2024-12-10 01:30:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9856678e-6195-3bb5-9dd3-075d185648da | -14.2701 | -57.445 | 2024-12-10 01:30:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15e1e5f7-567c-3eea-9743-7b8495dcd238 | -12.7052 | -54.954498 | 2024-12-10 01:30:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0411f64-e2e2-34fc-a36a-21aeb09df999 | -12.5573 | -58.3414 | 2024-12-10 01:30:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9fab8635-00ba-3ffe-a349-eefc9baecc3f | -15.4353 | -57.801998 | 2024-12-10 01:30:00 | METOP-B | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0afa0446-e90a-32bc-a5fb-2641fd34b3a0 | -12.535 | -58.334999 | 2024-12-10 01:30:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 70aa5aa4-825c-38f9-9775-e78b251ec8a8 | -12.5406 | -58.3578 | 2024-12-10 01:30:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3faa823d-9278-388d-b5e0-3eadfc8a3de4 | -12.8545 | -58.204601 | 2024-12-10 01:30:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0758045a-79b0-3264-ac59-7e921d5013b7 | -15.25 | -53.551399 | 2024-12-10 01:30:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 02b03679-5e44-3e86-a838-fce9c675b2ff | -12.8574 | -58.216202 | 2024-12-10 01:30:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d3211d7-6aa8-376b-be50-0d7682cfce44 | -12.5503 | -58.355301 | 2024-12-10 01:30:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 858ca12b-2aef-37dc-8f2f-d72ac7147765 | -11.5285 | -56.448799 | 2024-12-10 01:30:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c59bf0fc-5d78-3ff9-91d6-bd13a9c65902 | -12.5601 | -58.352798 | 2024-12-10 01:30:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cc73dc1f-0c19-3f96-a775-7545fdcd386b | -28.73984 | -55.64428 | 2024-12-10 01:30:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 16.1 |
| 2d4d3ed3-68db-3a7d-b26b-0bca7ed7ec96 | 3.2352 | -61.182598 | 2024-12-10 01:31:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 75da669c-31e2-3d66-8a68-27eef6b29242 | -10.0837 | -64.370201 | 2024-12-10 01:31:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0d76b25c-4c64-3927-9bf5-e8024487b43d | -6.6493 | -54.925701 | 2024-12-10 01:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaea28ca-d92c-3d35-a46a-b60f089a67e3 | 3.2254 | -61.1805 | 2024-12-10 01:31:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2849f01e-8f88-351d-b61d-ec167aa2fbe5 | 2.4354 | -60.636101 | 2024-12-10 01:31:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 48cf7bfa-49f3-36f8-a1ce-76292ac1ba02 | 2.4324 | -60.649601 | 2024-12-10 01:31:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2a142f07-a3c1-3428-ab31-63e28fd64f2b | -19.43647 | -54.78286 | 2024-12-10 01:32:00 | TERRA_M-M | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9ef72382-48d5-3e32-a7ba-3e5bb0b31f55 | -12.24258 | -52.44674 | 2024-12-10 01:34:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d8ef1bf6-7b24-32a9-b6c2-bb639ab28fcf | -12.53825 | -57.73187 | 2024-12-10 01:34:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b58791f8-2d54-303a-b0a8-fab17507b800 | -11.54246 | -56.44098 | 2024-12-10 01:34:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1af6378-9c3c-3b0d-b8a2-c0d047cfb942 | -10.03204 | -53.76004 | 2024-12-10 01:34:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 330b83af-fa81-388d-9efa-71c39038a4b6 | -12.36172 | -54.178 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 890fd2df-f588-38cf-972f-f3abde9c7f9d | -15.16005 | -56.48177 | 2024-12-10 01:34:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2bc427ba-efc6-3e83-b970-5aecee90fda9 | -10.08513 | -64.38571 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 391a564c-bd53-34af-9273-72c39649cea7 | -15.2577 | -53.58345 | 2024-12-10 01:34:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7df3a9b0-d419-3d5a-80fe-4598b817604d | -12.91377 | -55.05801 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b8e44d7c-8dfc-3fed-86ad-4150e3e398a4 | -11.53466 | -56.45218 | 2024-12-10 01:34:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 76035553-e1f0-3308-a857-c3bac01bd90f | -11.53035 | -56.42271 | 2024-12-10 01:34:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 432bb373-2795-33b1-a2cb-1b91577d8691 | -11.53323 | -56.44237 | 2024-12-10 01:34:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 53588767-f4a2-3c57-a4e1-e5f1a04fb17e | -14.44859 | -57.43737 | 2024-12-10 01:34:00 | TERRA_M-M | SANTO AFONSO | MATO GROSSO | Brasil | 5107263 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 770aeb8f-4f05-38cd-b654-ffecc469d595 | -15.26805 | -53.58155 | 2024-12-10 01:34:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c00181c2-734a-30fe-9f46-be7bd99e9aa5 | -13.0264 | -57.21249 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 01877453-6ea4-36c6-aafb-57a560bbe71a | -15.44851 | -57.8143 | 2024-12-10 01:34:00 | TERRA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| abff781c-1078-38b9-b2b0-e3317570f51f | -12.70541 | -54.9658 | 2024-12-10 01:34:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a2448148-f76a-30f2-95d9-3e3a8fd50973 | -15.43961 | -57.81563 | 2024-12-10 01:34:00 | TERRA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 6432ab67-13eb-3db6-a9b3-dbfd0d100ba1 | -13.80124 | -52.97972 | 2024-12-10 01:34:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5eaf0085-932f-3ac2-a94d-dacfe02c7661 | -13.31791 | -52.41266 | 2024-12-10 01:34:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 77f95274-e312-3303-a0ba-eced980ba38f | -11.54389 | -56.45078 | 2024-12-10 01:34:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 27b7de48-a589-3e72-9466-7a248d3b2847 | -12.904 | -55.05951 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6691f1a9-57fa-31aa-b50a-44745fa55466 | -14.28517 | -57.45573 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ad9d3821-d41a-31ca-9783-9e03a59d5a66 | -13.79891 | -52.96505 | 2024-12-10 01:34:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2c8801fc-9454-301f-8f23-72f15420b8b7 | -15.25568 | -53.57065 | 2024-12-10 01:34:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e50605e2-faf0-32d3-b79b-4bb43917f3e7 | -15.26602 | -53.56864 | 2024-12-10 01:34:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e347d06-c336-33c9-8fd3-ac7d86de8145 | -13.20897 | -56.87984 | 2024-12-10 01:34:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 60cc3186-c391-36c8-8ec0-d6c4c440cb2e | -12.86427 | -58.21904 | 2024-12-10 01:34:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f419844e-cc28-3944-a037-f63a123ad7f3 | -12.71698 | -54.97557 | 2024-12-10 01:34:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 8ce266f8-eae4-3c19-a499-b22cf7529114 | -14.28644 | -57.46484 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f8770082-af2c-319b-abc7-34117cc74bf6 | -15.1587 | -56.47235 | 2024-12-10 01:34:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d67d626b-6c40-3d4e-bdc2-b27e7f420451 | -12.36653 | -54.17143 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 585acc7e-394d-35d2-b295-0e18fba93990 | -12.56117 | -58.3619 | 2024-12-10 01:34:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6631af32-70fc-37cc-a576-bd4351077f17 | -14.27757 | -57.46619 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 41d8477c-b57e-3187-8ec9-0ac887f2c250 | -12.86024 | -51.94531 | 2024-12-10 01:34:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 23f0e310-20e4-3767-a271-0dd4ee1aa2bc | -12.85719 | -51.9269 | 2024-12-10 01:34:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 905b2736-c613-34d0-9e0e-86742a48255f | -12.85479 | -58.22686 | 2024-12-10 01:34:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bf1ab802-461f-3c5d-bc83-ae0606c09f56 | -12.37494 | -54.15678 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| caa0a9b0-6345-308a-8a9a-13d484d20adf | -10.75229 | -54.78008 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2dd52b38-2a44-322e-aab8-8058c698371c | -13.02771 | -57.22166 | 2024-12-10 01:34:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 4edcdc1b-262d-38e4-9c86-ae02207896a0 | -12.21917 | -64.25967 | 2024-12-10 01:34:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |


[Clique aqui para ver as próximas entradas](README7.md)
