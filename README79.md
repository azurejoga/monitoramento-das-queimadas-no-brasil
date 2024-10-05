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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcb041fc-236e-3191-9ec0-be348f272203 | -18.09516 | -43.96088 | 2024-10-05 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15076d45-7f85-3d2d-b49c-dda69180717f | -18.0919 | -43.96114 | 2024-10-05 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c3948fb-02ff-3d69-8d40-5136219fc51c | -17.74251 | -43.82883 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f4c530f-fb0b-3ae3-8f9f-063bcc128c97 | -17.7391 | -43.82824 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26a9f9f6-ad2a-3f22-a41d-4107e4dbc4e8 | -17.70141 | -43.79882 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a782f95-c507-3eb9-aadb-fdbf63e54c82 | -17.70085 | -43.80265 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2d03670c-f425-3405-abde-c5385531a150 | -17.70029 | -43.80648 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13cdbf31-e7fb-34ea-a91e-3ab353532e37 | -17.69855 | -43.79446 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d112a2ca-2a8e-3212-90e9-b3315d89a4b2 | -15.20365 | -47.50447 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d867f08e-03e8-302d-a63d-964587ed856a | -17.69799 | -43.7983 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89a6e6e0-30d2-39e5-8c1d-e00ad58db007 | -17.69742 | -43.80214 | 2024-10-05 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a05fbef9-90b6-3dde-8beb-97d90912a615 | -17.3149 | -42.36446 | 2024-10-05 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ddcce114-a662-3a53-b3a5-cb9f5e8f5339 | -17.14987 | -44.77713 | 2024-10-05 04:17:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04642841-b6a1-318b-93bd-bbf309e0d985 | -15.62655 | -47.1766 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1170f805-21dd-3c3b-ab7d-ed9077133153 | -15.62335 | -47.19594 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a24dc396-251c-3bd3-ae2c-dc283d264bc8 | -15.4342 | -47.4248 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2b87f5d-e96e-3202-ac32-beddc376ec7d | -15.43137 | -47.42036 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ec83051-224f-38a6-ba50-3e86b5d65fd3 | -15.43102 | -47.67992 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9471a3f5-3323-3720-9218-be55c528eb0b | -15.43035 | -47.68393 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6dfb8546-6017-308d-8a48-c73ee119c82f | -15.42789 | -47.41972 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acf9537f-ef07-32ba-9d2c-f49bf84d0961 | -15.42751 | -47.67925 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e933d1dd-5192-3dad-a40b-56d170d0187f | -15.42684 | -47.68325 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d66a6a0-2f32-35bc-875e-9e55d91a3792 | -15.42441 | -47.41916 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c5d1d56-af15-37e3-a0e3-adcc5ae7b20d | -15.4221 | -47.7115 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6fcae216-cac5-3ccf-a52c-5dbd97843506 | -15.41926 | -47.70686 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9269d45-0d1c-352e-98af-83417abc0929 | -15.41858 | -47.71088 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 415e7870-8fca-341f-b096-57a74a9cf4a6 | -15.41523 | -47.40986 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e37c133-d5eb-39b5-9c5b-aa68d7287ce6 | -15.41239 | -47.40541 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6c9b35c-5564-386d-8eda-6a0b5622e349 | -15.41175 | -47.40925 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c45b4f5-79b9-3a0e-9112-a77a614c8487 | -15.40608 | -47.40036 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 918d634c-69e9-3d3d-b194-c310c7d34f09 | -15.40588 | -47.70016 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fdd2e17-8494-3bcc-b689-6a9ec8d1b4e2 | -15.40544 | -47.40416 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2292004-d920-3a03-9bc8-9fe8b5454540 | -15.40512 | -47.68318 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32140efa-a76f-301f-a45f-4a669447e660 | -15.40131 | -47.40741 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3d829651-83ef-3a8d-859f-7d8a809bb12d | -15.3978 | -47.40693 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f0e485d7-5d93-38a1-8587-86642f889c1a | -15.39716 | -47.41072 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 343285a2-c56e-36a4-9bdb-f151b816b2bc | -15.39651 | -47.41457 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 313ee965-deb4-3b55-b4a2-f32f8e6f19ee | -15.39234 | -47.41803 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b45d151-3783-3eaa-8a97-030226c2802a | -15.27734 | -47.49688 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2e3f44c-1f25-3c78-87e0-36a03ec93387 | -15.27384 | -47.49627 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3756bd3-56b8-3f63-b1ad-4070d9319c54 | -15.27319 | -47.50008 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ee492ea-390c-34e0-8b19-08839973613c | -15.26971 | -47.4994 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 591a64ee-343e-3cdf-bcfb-60b676b58b87 | -15.25989 | -47.49363 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdfcc763-abf8-385e-bc6b-994556112c6a | -15.24955 | -47.48849 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39f26d8a-c6dd-3ad8-a3dd-d3413ab88257 | -15.23013 | -47.49693 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f64c780-bae4-3b9e-9104-dd2d25b855b0 | -15.22724 | -47.49272 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3140e041-3f0f-3345-933b-f2edc23e90f4 | -15.22586 | -47.16012 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e126bb65-c87a-333a-ac37-ef69be09d45f | -15.22308 | -47.49603 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 728fa42d-2e70-3c43-8aad-d46fed6ac3fb | -15.22303 | -47.15584 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 53ff34ed-7434-3702-a028-320d827c16d7 | -15.22237 | -47.15975 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74270f90-e034-3d6c-a18f-b5ba38cfc0ff | -15.21957 | -47.49554 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bccb666-07a1-3069-a70c-d612f92e9e03 | -15.21543 | -47.49872 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d66fae2c-080a-335a-80b7-6c3b56309820 | -15.20077 | -47.50022 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ed38938-bec4-3a45-8aa7-ff60f233f60a | -15.20013 | -47.50399 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c32e100-b009-3a2b-a94f-e00f2da4fe6b | -15.19952 | -47.50763 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0a963bdc-d29a-3d39-b937-36170800b629 | -15.19599 | -47.50719 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82737abd-6620-3d9b-a804-d6f1a716f951 | -15.19245 | -47.50677 | 2024-10-05 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2c5ef9c-2ef6-3c65-93cf-d80f019675df | -15.18266 | -48.07078 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff616981-1f3f-32bb-83ff-0126c2fa5028 | -15.18192 | -48.07505 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad71d03e-1723-38c3-a7b8-717b3b94d9cf | -15.16906 | -48.06389 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6de6d143-beaa-386e-b2ba-32431bd09205 | -15.16837 | -48.06059 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81c63e00-2606-3984-b2be-c91148bbe441 | -14.94876 | -47.06259 | 2024-10-05 04:17:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 759709a5-595d-3ad6-9216-b77a207036c3 | -14.79688 | -48.09249 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0b175af-aa9e-3510-befb-5bbf2179d920 | -14.77456 | -48.04938 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f403db55-debd-339c-b9ae-91dd7db5b26e | -14.77095 | -48.0488 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| db2e214e-18f1-3035-b663-443b129ee332 | -14.76234 | -48.03415 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f8776a2-210f-3345-a939-ef11403b9946 | -14.76161 | -48.0384 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4c30d5a-4235-32cd-82ae-e32db3f3a575 | -22.32493 | -43.18304 | 2024-10-05 04:17:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a18bf9c2-7057-35b9-a12e-77ff99a1dc44 | -22.32432 | -43.18761 | 2024-10-05 04:17:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b177a372-3771-3864-8aff-bbb96bc5e248 | -21.9473 | -45.41024 | 2024-10-05 04:17:00 | NPP-375D | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 17221e95-5d05-35bc-b367-61d8192ab82d | -21.53547 | -45.43579 | 2024-10-05 04:17:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5c2268d2-b765-30d2-badf-3b6d18594aad | -21.19629 | -44.93686 | 2024-10-05 04:17:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 606c1178-6212-3162-9778-8ee38255ffeb | -21.04204 | -44.80181 | 2024-10-05 04:17:00 | NPP-375D | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fa7d6b0c-3459-3a6c-8cc4-a3b25a4e249e | -21.04147 | -44.8057 | 2024-10-05 04:17:00 | NPP-375D | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1737ccc4-771e-3104-b3f8-deb4caff9f4a | -20.51607 | -44.89491 | 2024-10-05 04:17:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 871d0f23-c50e-3e16-9553-4a7df4548a4f | -20.48104 | -42.36003 | 2024-10-05 04:17:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bd1c3b4a-95b1-315f-bd80-ea1943d8b963 | -20.48043 | -42.36454 | 2024-10-05 04:17:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0ffac3eb-fc24-3ff7-affe-5b2d1e4a58c5 | -19.95373 | -44.31964 | 2024-10-05 04:17:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1578be6b-c4ff-3dc3-877f-678b86d839f4 | -19.31194 | -42.57478 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 383baef8-2fe3-3093-b7c4-d0ac03eb408a | -19.3097 | -42.56392 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e01ed2f9-5163-3d77-8c10-9d88f00f28f4 | -19.30833 | -42.57393 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b8390e77-e8bc-3555-9249-6f10a4b8ac79 | -19.30765 | -42.57891 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| de32545f-55a3-3b8b-89c2-22f97a83fb9c | -19.307 | -42.58362 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f006c428-e876-388a-b60d-c78f09ad89b1 | -19.30607 | -42.56321 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e8326c74-c006-3d96-bba0-4544ab0c5ce4 | -19.3054 | -42.56807 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 03799c3c-2d41-38b7-95f1-5ff1961ff4ab | -19.30403 | -42.57807 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 66e1e900-dbf4-39b5-9fb3-cd8273db1c62 | -19.30337 | -42.58284 | 2024-10-05 04:17:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e2b576fa-d225-3441-9065-4d352cc91618 | -19.26091 | -42.86308 | 2024-10-05 04:17:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd9be766-806d-39ba-855f-443f9290fb77 | -19.02015 | -43.173 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fa65d140-581e-3c2e-92cc-286f31c1a648 | -19.01662 | -43.17242 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d5fa9248-d0fb-3743-8cf2-0389ed4cec86 | -19.01428 | -43.16335 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 66e18a74-3de8-39a2-a469-505beb09e820 | -19.01308 | -43.17181 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e002c357-3928-355b-8f08-c93cf608a242 | -18.88104 | -43.59143 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f9906e3f-a253-3de1-a73a-4ec956daa115 | -18.88046 | -43.59542 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ea141b16-36bd-35aa-af6a-3785e8e76ce9 | -18.87988 | -43.59941 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 15387f7e-f805-343e-b3ec-282f07356329 | -18.8793 | -43.60339 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 77575775-e0bd-3e7e-89fc-d2e9817042d3 | -18.87754 | -43.59101 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| a5502280-d5ef-30d9-9e36-be0ad9a1b6ea | -18.87696 | -43.59501 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 28648ab2-d36f-392a-8573-c48decf0a24f | -18.87638 | -43.59898 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| d15377ac-6ba1-30b6-bed9-8319299d235f | -18.87403 | -43.59064 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |


[Clique aqui para ver as próximas entradas](README80.md)
