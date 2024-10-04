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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90b303cf-8704-3215-bba5-141b67ac6b5d | -13.16556 | -48.63453 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 211ae6b2-4bee-311a-8b49-15fb32dde1e9 | -13.16503 | -48.66008 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1721172e-71ca-383c-8d43-e4a4129f419c | -13.16501 | -48.6381 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e22f2964-3126-39bd-90df-38c8880de1d8 | -13.16448 | -48.66366 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfde6dd3-1c4f-3cba-bb1b-4454c27a0c89 | -13.16443 | -48.61966 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0382df83-55c3-38f6-90d6-2c39364097d3 | -13.16393 | -48.66725 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dd31fb5-948d-3059-ab09-430953c70a91 | -13.16387 | -48.62324 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88830776-238b-3e36-881c-6a906515544c | -13.16337 | -48.67084 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 51dcda10-a801-3180-8cb2-3051d615bf31 | -13.16332 | -48.62682 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71b0dcee-1dc0-32b5-9dd3-62125ea2fd2e | -13.16282 | -48.67441 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ae3259fc-1d3d-328c-8457-2bf1d08526fa | -13.16277 | -48.63041 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd88f9f5-3b28-32ff-a921-060e6532d95b | -13.16227 | -48.67797 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 380a19e2-ed54-370b-88fb-ce74b9aaa5b6 | -13.1617 | -48.65954 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1f890c0-881e-37db-971b-76833e8dae34 | -13.16114 | -48.66312 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b85566a4-92e7-3c38-8cd7-4afd5e1135e1 | -13.15949 | -48.67385 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| be7e54db-4266-3e3f-8f87-c8a3c8c67f8b | -13.15893 | -48.67742 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a08079b4-675d-38ce-b9d4-fc44a62cf00f | -13.15836 | -48.659 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fad75ed-d9d1-3352-ad45-24bb6980cb9d | -13.15781 | -48.66257 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31dc8ca5-01ab-3065-8657-989a8f239826 | -13.15725 | -48.66615 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d028e1a8-7a26-3a40-b872-a23fe3272fba | -13.1567 | -48.66973 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 94e87841-9dc1-3d58-8906-43b33b85304d | -13.15615 | -48.6733 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9e14374c-2dbf-3ef3-a973-6ec7b2f4e872 | -13.1556 | -48.67688 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b086ef7f-04c4-3819-b3bf-b13c5c4e7013 | -13.15505 | -48.68045 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e45b8a69-9bf1-36fc-a3c9-8a533668a11d | -13.15337 | -48.66917 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13aea601-54e1-3aa4-bebb-f9b4da077111 | -13.15226 | -48.67633 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4e0598a4-c4e2-379e-a2e6-fb0728975a85 | -13.15171 | -48.6799 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e621cef4-04eb-3785-8f36-a7c53c9bc61c | -13.14892 | -48.67578 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1be86cf9-4987-3dc4-8514-c614ae86e28c | -13.14837 | -48.67936 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a579b375-4f73-34c6-97f8-165ff4e7cfc0 | -13.14782 | -48.68291 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e667315f-4d4b-3c83-b185-55d3210d8a98 | -13.14449 | -48.68237 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25c6203b-32b5-39db-a324-2b0537c67129 | -13.14115 | -48.68182 | 2024-10-04 04:34:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85eddd6f-6ad0-3c55-ad35-9d9e85de58ad | -13.31978 | -49.31878 | 2024-10-04 04:34:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f249e623-8926-3440-8ca1-27f900d2b6c1 | -13.31645 | -49.31824 | 2024-10-04 04:34:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e11c8b1-7407-3c13-a94a-22335df787e3 | -13.3098 | -49.31715 | 2024-10-04 04:34:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| acd1fe03-bc06-36c7-85a0-9ff76eab3a32 | -13.30814 | -49.30596 | 2024-10-04 04:34:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65abdfc0-55d5-3aa9-9c0a-cfbc10f7f3cb | -13.30759 | -49.30951 | 2024-10-04 04:34:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a146fae8-c807-306f-b7b5-72d22b38b3c1 | -12.27087 | -49.21416 | 2024-10-04 04:34:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39a18cde-4d6c-3331-a0a5-05961671e1e8 | -12.27031 | -49.2177 | 2024-10-04 04:34:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0aa11ab-81fb-3245-b557-70b9b318d921 | -12.26366 | -49.21661 | 2024-10-04 04:34:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4aacb53-0479-3112-8107-f14666a79916 | -14.68419 | -48.75814 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b02a5118-e6bd-35c9-9d4a-24bae0dadc1a | -14.68085 | -48.75756 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b8ebf471-b364-3019-9428-cfc90f08dec9 | -14.53728 | -49.29458 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3ffba05-47ad-34b5-837c-5b3f56502e32 | -14.53173 | -49.28634 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 980e8681-1559-3210-bd0e-4e887a62794c | -14.52174 | -49.28472 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0943dc8-3754-3469-9b7b-dede14fef3c5 | -14.52117 | -49.31027 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d2513d6-fa0d-33c4-8dd8-37c0746e352c | -14.51784 | -49.30972 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46586c7d-f283-3a69-ba81-e8d84eac7d81 | -14.51564 | -49.28008 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 847ff225-3518-3eb4-924e-6bde8ac3c140 | -14.51231 | -49.27954 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3c414fa-bc98-396c-8641-e0e66f3b2fb8 | -14.51062 | -49.31221 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2eddd800-7986-3481-969f-43213bb833f1 | -14.50898 | -49.27898 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 790e0205-a25c-3852-9766-269a2896bdbf | -14.50842 | -49.28256 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 27e1897a-ca06-3348-9bc4-6a19c9e4530a | -14.5051 | -49.282 | 2024-10-04 04:34:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e194620-abfe-3ec1-8519-eee8309607d0 | -14.69482 | -48.77835 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff0e57c0-e5a8-315d-b814-e18362558a0b | -14.68309 | -48.76529 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9a6c792-6dc1-3726-b767-0b36d2ff68c7 | -14.68196 | -48.75027 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe548254-48a1-38d6-85f4-9cfa7538ca0a | -14.63095 | -48.71251 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5be5d68d-ec31-3b4d-b62f-2d4d9319e871 | -14.69817 | -48.77893 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50312add-feb3-328b-92ba-123009b80243 | -14.68699 | -48.76228 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 402cdce2-12e3-3725-bc61-96ab4c5796ce | -14.68644 | -48.76587 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2221beda-d59e-39b1-bf47-1b4ac3cc36df | -14.68589 | -48.76946 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1e02189-b055-3ab1-9bf1-f5c28b2b6988 | -15.07789 | -48.94327 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e5eca5a-397d-3938-87b8-60e112406275 | -14.78798 | -48.96318 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 986e79e2-d16c-3e3c-9358-b189df66482f | -14.70432 | -48.78359 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e1bb063-2825-3db7-94e5-60e70be4c48e | -14.70097 | -48.78304 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c28a61cf-750c-3061-81ee-c36dd3b5b856 | -14.68364 | -48.76171 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6454d462-b0b3-3734-b5dc-526d054727e9 | -14.6814 | -48.75396 | 2024-10-04 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee118548-3f4c-3d8e-b092-079fc8278392 | -14.62816 | -48.70834 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d26b8902-da4f-3aba-bd69-11ed444d78fc | -14.6276 | -48.71197 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 993ed97e-f248-35df-8d90-042054fea808 | -13.72602 | -49.42167 | 2024-10-04 04:34:00 | NPP-375D | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cc4d9ad-be2e-3a0e-8b0d-a2c0ec776efd | -13.72546 | -49.42522 | 2024-10-04 04:34:00 | NPP-375D | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3b9dce5-721b-3bc2-9d23-6b84a17bc104 | -16.09304 | -50.25952 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39aab039-d370-37d1-a60b-3ebdbf18c015 | -16.08971 | -50.25897 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d757505d-0367-3485-b5a9-a783ffe6da86 | -16.08858 | -50.26617 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b0dafce-0482-3460-bcd1-fcd48a417afc | -16.08801 | -50.26976 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b25e221-9037-35ae-b5e5-17592f7d563f | -16.08468 | -50.26921 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 899827a2-9dfd-3c23-9921-f73908ca6078 | -16.08354 | -50.27641 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1d6fe81-1c8d-3ee4-8ba7-91c2c4adce64 | -16.08296 | -50.28001 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db58df16-915f-3591-abd2-d547a191f07d | -16.07564 | -50.30462 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca16d5c8-0319-36e7-8ca8-3fe7678ceb94 | -15.8978 | -50.16819 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb280df1-80b6-393e-9be1-3dc0075724bd | -15.71429 | -49.31229 | 2024-10-04 04:34:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60c56c54-7893-399f-b21d-f57840fbd337 | -15.71095 | -49.31174 | 2024-10-04 04:34:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 785204cb-5e39-3a5a-b3b7-e1e21ba17458 | -18.1145 | -49.28205 | 2024-10-04 04:34:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58537b9c-8918-3124-8a26-81261588d5a0 | -18.11393 | -49.2858 | 2024-10-04 04:34:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c262727-3272-34c4-b950-5cbbf0ae04e0 | -18.11336 | -49.28952 | 2024-10-04 04:34:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf008f72-f2b6-3a40-8e99-17da88a542ad | -18.10999 | -49.28898 | 2024-10-04 04:34:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39beb6d0-f96c-3bf7-946c-5ea64b5cf987 | -18.39472 | -49.319 | 2024-10-04 04:34:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e94c3191-bfdd-3a2b-b898-9a458f9de9cc | -16.09545 | -50.45973 | 2024-10-04 04:34:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97828500-f623-31e4-b366-51cc2c9b2b34 | -13.70517 | -49.85612 | 2024-10-04 04:34:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67ca9dce-4046-3c97-919f-b6af930ab15e | -13.70184 | -49.85557 | 2024-10-04 04:34:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16cf9f22-df88-30e2-952b-83f6dcdff602 | -11.96444 | -50.15409 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4728bd64-fba9-324d-8a6a-f0deb931497b | -11.93813 | -50.146 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1e264bc-d32c-31e3-9fca-4a2c0933dad7 | -11.91409 | -50.13875 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2321eb9-2bf6-3a03-b54c-408d6abe5cc9 | -11.91351 | -50.14236 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22c37b7a-8468-339c-9376-0c2cc3d59fa3 | -11.91073 | -50.13819 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25da8d6e-88d9-34cf-90bc-1a7b9634967c | -11.91015 | -50.1418 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a22e8dad-e802-3efd-9c73-41b99cb51d63 | -11.90679 | -50.14125 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2012510d-7c0e-3355-9387-957fc9ad6b76 | -11.90342 | -50.14069 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 287576a7-08fc-360c-ad70-52ad8618fe86 | -11.68341 | -50.03394 | 2024-10-04 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 748bba67-6da3-3e65-b07a-f59ed18767cf | -11.12309 | -49.60492 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c88b879-1239-3903-beb8-bdc601321cb1 | -11.12252 | -49.60848 | 2024-10-04 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README121.md)
