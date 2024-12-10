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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ae96caf-057a-38e5-8027-f856581aa276 | -11.57171 | -54.56703 | 2024-12-10 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10c8888f-2d3f-367c-93e1-4d0842af46a6 | -2.78566 | -53.24518 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbd22680-b4cd-3da5-83c2-8161b17ad479 | -2.96363 | -54.31587 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cc350aa-eddd-3927-8ba2-0d66fb927533 | -3.79377 | -51.97718 | 2024-12-10 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b58b9884-dab7-327d-895e-8e80f3e6a1ad | -3.21846 | -53.63359 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 461503ca-30ac-35e0-bd36-a2527d5ce389 | -3.1098 | -54.08046 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a60da38-a080-38e9-bffe-2557f1b611cf | -2.77906 | -44.99346 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a4986cc-3421-39b7-9a1d-8f8b82e915e2 | -3.04526 | -54.24266 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbd74869-8641-33cd-bbcf-ea86d3e82cfb | -3.66352 | -50.97293 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50e76745-7439-39a7-9f28-d4779584c54f | -3.23407 | -52.83837 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 895a83d5-edd0-3d52-b3ba-55b7c1ec893e | -3.11459 | -54.02806 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cd8122c-d91d-3dc5-b6f2-c9978be11709 | -6.31445 | -45.76094 | 2024-12-10 04:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea076562-af44-3ece-8356-20db825202ae | -3.34185 | -53.25631 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 100e0cda-f1ad-373b-ad4e-3c9d3c92577b | -11.88772 | -54.67664 | 2024-12-10 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3ea73b1-f893-3b4b-a406-76a5f2b3ade6 | -2.22516 | -53.72239 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5064984-9fcb-3c7f-8b93-70271cf70721 | -4.08466 | -54.3984 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f54f679-5183-381e-af6f-71d53b9335ac | -3.7955 | -52.40396 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9efa76d2-6021-3ab2-87d2-f72da5afe406 | -4.41878 | -45.88057 | 2024-12-10 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41d266d0-9600-3157-8f3c-3868fe466767 | -6.30983 | -45.76019 | 2024-12-10 04:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3cbbbbd-8d20-39eb-b0d4-65239fd782ab | -4.12578 | -50.42488 | 2024-12-10 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35a7786f-542a-3996-8488-9c96997e8899 | -4.11647 | -50.20984 | 2024-12-10 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98df07c7-bd03-3ce9-bbcf-46ef1cacb9a8 | -2.29656 | -48.57155 | 2024-12-10 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9e17d08-d1f5-310c-b4a1-640f2efd8b9e | -3.09912 | -53.74468 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b8e31313-2d3a-3d8d-9e25-7b34b3046aff | -2.78774 | -52.86468 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cfa406d-60a4-32d5-ad7c-449b7b33c4d4 | -3.41234 | -52.17786 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a022594-b3ff-3185-81fd-8da705833583 | -2.62487 | -48.06084 | 2024-12-10 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e6139303-f34e-3085-9d56-bfa1749cdd31 | -2.41629 | -53.69142 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dba80032-1787-3400-bacd-9ebb3679d249 | -1.68527 | -52.97652 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e803f20-b084-3d7f-ace0-9553fc7019ab | -2.81678 | -53.06952 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 22f95832-3ac1-3e08-b828-a9b5b8f14f25 | -10.4502 | -44.88979 | 2024-12-10 04:53:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 915043d7-3def-36d0-9ce1-09875c95170b | -4.47225 | -48.11485 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8029fe4d-0a61-34e1-b58c-9ff4ee394a13 | -2.76698 | -54.02779 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d021d231-c1d7-3ff7-9692-740d4b6b63fb | -1.63806 | -53.30111 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cccadfbf-7d53-3dfb-97b1-1bae0c8e9698 | -2.80068 | -54.03678 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c9b772d-a049-3193-8ecf-5301a4cd1f26 | -3.21316 | -46.80813 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1a01d393-745a-39c9-b821-f1de7c0ba672 | -2.45615 | -53.97337 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ae30741-d7f6-397c-b61e-af43189f4b83 | -3.27706 | -51.07932 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cd77a2e-ec65-349e-8368-0458119b0189 | -3.11842 | -54.07034 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ac94db6-1385-3c91-b372-21bb4f708dea | -3.20603 | -46.80688 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d3847fe7-5fc8-3ebc-9d74-6cc0dde14b11 | -3.10645 | -53.7644 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 45bd0d4a-224e-38cb-b20e-f48704f87956 | -3.51649 | -50.98279 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5db64a4-8f86-3695-9730-778888fe609c | -4.39403 | -47.75079 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc504bf2-0e64-3ea2-8acd-508b68a81e51 | -2.47463 | -53.62966 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 930ca379-b207-353e-bf20-02736ea3e9f2 | -3.52817 | -54.69203 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8dc307a4-28c2-3f8f-aa19-01181f52210e | -2.81454 | -53.04043 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 124a252e-8ca3-362f-aedb-f611a22bb4a1 | -3.10701 | -53.76076 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d55f0af4-3a88-3b6e-b0b2-40f101977ac2 | -11.78173 | -55.12984 | 2024-12-10 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc882ade-2c57-36fa-be04-76486f4b69b1 | -6.32087 | -46.92995 | 2024-12-10 04:53:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 045e5f19-81e8-39a7-a42f-f180840bc3c4 | -1.67824 | -54.34624 | 2024-12-10 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe444e97-a9c0-341e-9578-ff4683884b4f | -2.31099 | -54.00473 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f67772b-f8f6-3357-8513-81841b66e469 | -3.52683 | -54.58915 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c545f9c-dd8a-3ba2-b675-078278b1a91e | -3.10295 | -54.07943 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d7fa9c9-a0f8-32c9-8073-770a78952a10 | -2.30535 | -53.74948 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cf75458-1b46-3dd8-865f-4ece01e43e21 | -2.45938 | -53.63839 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a394dded-d7fe-3cbf-a71d-862b9c752d50 | -3.10269 | -53.28373 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 366efa0a-d5d8-3c36-8bc7-c07595d6375e | -3.85895 | -50.12967 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39acd45e-8e5e-33bb-96d0-0678b75b2fb1 | -4.70427 | -43.79217 | 2024-12-10 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d86968ad-8817-35a9-a109-9405d6f8f0f4 | -6.91543 | -43.51836 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f496f40f-d70f-3fbc-9b15-fccc8c1872f5 | -12.85942 | -51.93158 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15ca4458-6295-3cc6-af19-07bcd9c20141 | -2.45654 | -53.6565 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e17957b-ae73-3b98-824c-1eed350588ff | -3.52939 | -53.93835 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34905b25-8df6-3cef-b693-b66632ee6a34 | -1.62103 | -53.9722 | 2024-12-10 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb42e345-2885-3875-b815-064aa3a11a45 | -2.99353 | -52.85384 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d5596453-b01b-3048-b144-ea559674ab54 | -2.99789 | -53.04376 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30185294-e65e-33e9-9d75-54e097641445 | -6.91494 | -43.52185 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbd81009-d74e-3407-aaa5-a3766a023a08 | -2.4721 | -53.71896 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c4c6e32-af67-3c90-9446-1c98c26e52f3 | -11.66078 | -58.26823 | 2024-12-10 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a6e159b-bc06-3370-9bf6-35fd4049f598 | -4.38077 | -47.75901 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 48111f8e-a72d-30ac-9760-59679799cb10 | -2.30068 | -54.00313 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff847f42-d3a1-3363-a605-13a6b87fe5d4 | -3.70956 | -53.75106 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f3a9a65-67b7-3ad4-926e-3e77a6b61f60 | -2.82055 | -52.98057 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b91f8b64-80c6-3b60-aadf-6e40ee83132c | -3.20495 | -46.80682 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bae6cd72-b18f-3bea-ba85-3156f6cb0714 | -2.48063 | -53.70908 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15802ec8-d3e1-39bf-86a3-575fc5507d9e | -2.9596 | -53.71953 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cf8aca44-f662-348b-8e75-083808b21fd7 | -5.71617 | -46.55006 | 2024-12-10 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b78df5dd-33fc-346c-8fdd-bfa056f8c5aa | -5.91744 | -48.05671 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| afc98847-7aa8-3ffb-a656-0d12286b56b2 | -3.09669 | -54.07465 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d0a2bad-f05b-3b8b-a883-a2320b149ed9 | -12.37296 | -54.16381 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d057e38-0f72-3584-baa6-252306a759ba | -3.06622 | -53.7994 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0114c187-0983-37df-b4dc-83f389de341c | -3.87658 | -54.22612 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7f07d5d-6cb6-3b72-a4b5-127e99ea4839 | -2.6759 | -53.03708 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a53f5a0-426d-3461-9e5a-9405a249eb59 | -4.03652 | -50.80312 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3724cb4-e9cd-3018-b714-e10f5740ebe8 | -2.2213 | -53.63577 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4c8a91a-94e2-3671-b756-f2c04d3a8550 | -3.68089 | -49.63998 | 2024-12-10 04:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a20fb059-eb87-39e5-83bd-09b1c46591fd | -3.21014 | -46.80753 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 522373ab-b764-3f53-a177-538a52ed1e53 | -3.0481 | -54.24702 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b11a8f1e-982e-3833-a0a6-a30a090348f5 | -10.87587 | -44.34248 | 2024-12-10 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5deee34-1134-3317-95c7-ad425ee6fd95 | -2.4735 | -53.6369 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b9d0c09-dfd1-37f2-9acd-0ac942280d27 | -1.65982 | -53.41502 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3c9dac4-4a23-39ad-98a8-08014188f58e | -4.07387 | -54.1122 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e18aab54-ac1b-35ba-9f32-20e764cfa4dc | -2.90539 | -54.15258 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6238d68f-a1b8-3133-8553-f7d4755b91b3 | -9.39773 | -62.57584 | 2024-12-10 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b47d22f2-647a-30bd-b807-05814884b29b | -2.56297 | -53.40748 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07c097ee-3f48-381d-9c61-86aa742e43d1 | -2.96705 | -54.22741 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97e11c27-f636-354b-bb96-9dee17bc88c6 | -3.02704 | -54.18259 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 287ed3dc-5ad7-33fb-9fd6-cdfe6acb036d | -3.41721 | -52.66898 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19a0eaf6-9f2d-3c18-9ac7-58f26f6f3a33 | -2.80241 | -53.24771 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 601f8a2b-7c9d-3be6-91c1-ebcf352194c7 | -2.81957 | -53.07353 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e88ed7ca-87f5-3596-bfd0-69164432c29c | -2.83336 | -53.00758 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b64571a3-6544-3dfe-9787-88004a82e31a | 1.96792 | -60.90956 | 2024-12-10 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
