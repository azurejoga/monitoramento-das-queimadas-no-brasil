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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00cdea65-b566-3250-bdb9-09a37fa2da5e | -16.67027 | -49.45245 | 2026-08-17 04:59:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61caee7e-870f-36ae-9d9c-8c30c619fad2 | -14.49813 | -59.32774 | 2026-08-17 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65452e67-4d59-3f5e-97bc-d6d1cebd3103 | -17.32905 | -54.93105 | 2026-08-17 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be0320d4-b2bb-3fa4-9dba-c970b448d935 | -14.49967 | -59.31937 | 2026-08-17 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9655049c-9cf6-364d-9fef-56187fcf27c1 | -16.41406 | -49.63452 | 2026-08-17 04:59:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d90c021c-9e6c-342e-80cd-367e36700fec | -16.22994 | -49.71008 | 2026-08-17 04:59:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1d1e382-c82b-3be5-9d1e-b17e392d49e1 | -15.90509 | -55.51957 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 54a9b3ff-1d59-344d-a9d0-80eea13f7ec3 | -16.81534 | -49.07106 | 2026-08-17 04:59:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13555721-18cd-32b4-b693-b905c0897238 | -17.53258 | -49.20876 | 2026-08-17 04:59:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37b3d654-f7e3-391a-9458-5849778c5ab4 | -19.28175 | -44.97153 | 2026-08-17 04:59:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| feb03599-21ba-388f-b02a-8695748a22b9 | -14.08557 | -58.45497 | 2026-08-17 04:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc728818-cc8a-3975-a1cb-597c4cabcc75 | -16.22132 | -57.64391 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c4669b18-c26f-341c-b654-c22caff0229b | -16.21751 | -57.64329 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f0e1d9e4-b2dc-36c7-878c-57d2defc8341 | -16.29737 | -53.17803 | 2026-08-17 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc6eba21-7904-3c76-9f10-1dab7d87d843 | -19.28138 | -44.97485 | 2026-08-17 04:59:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 23a463d8-a9d6-33b5-b9bf-a73a6b17340f | -15.82356 | -54.21825 | 2026-08-17 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7406db3-b6ea-3f69-bae5-64947100c3a7 | -15.91437 | -56.4884 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89fd575f-ae14-3174-9e22-f64ded632091 | -15.03088 | -52.68926 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87f38abb-8079-3e22-8525-152bb99d3d8d | -14.08697 | -58.44733 | 2026-08-17 04:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db270d0e-b86b-3ae1-b234-89fd50790753 | -14.49023 | -59.32193 | 2026-08-17 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be524da6-f07b-347e-8499-f25c705c596b | -19.28109 | -44.97087 | 2026-08-17 04:59:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 875a9e87-d652-339c-97eb-4822d4b301a6 | -15.82022 | -54.21764 | 2026-08-17 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8a81834-2756-33c1-9514-b067fa685746 | -16.22862 | -49.7036 | 2026-08-17 04:59:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b2bdda7-30ce-36cb-8982-4f8b531656ad | -16.41471 | -49.62993 | 2026-08-17 04:59:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3b8ba123-1fc9-39a4-a6d4-a251fe0b54ae | -15.89905 | -55.53421 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5e2b6009-d6e9-3c09-b433-1fad4fad6b7d | -15.91009 | -56.4701 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d770830a-0619-3cc6-a868-4d76a0c9caef | -15.90378 | -55.52732 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| dc3e6d39-e1fe-3046-9621-a4c9d51bceb0 | -15.8681 | -56.3492 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 260f8d38-6a6e-3235-a4a3-8073805a8d1f | -15.03199 | -52.68211 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c274ad6-f8d1-3252-a41c-a5e0457e29dd | -15.83476 | -54.2128 | 2026-08-17 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1e7b79d-5903-36d4-a30f-47a0a7d0e4d6 | -15.1618 | -50.08072 | 2026-08-17 04:59:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d6a27ad-42ba-306b-a791-c06d51f76c33 | -15.92412 | -56.47957 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c0d9099-c19c-3742-b1b3-81888f1157f1 | -17.32569 | -54.93044 | 2026-08-17 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 706440ce-6418-326f-aee2-20348d9a7252 | -16.67472 | -49.44831 | 2026-08-17 04:59:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5ae9821c-900a-3737-a573-f4a9ef209279 | -15.9313 | -56.48092 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 501490c9-a629-3153-9fab-c977f68966f5 | -15.07865 | -52.64571 | 2026-08-17 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c643f6b3-10fe-3f67-bf5e-815e644646fb | -16.29843 | -53.19299 | 2026-08-17 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd3b700f-3fe7-3b1f-83d8-76c09fc4c405 | -15.91215 | -55.54097 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 5d7694c8-778c-3da4-acdc-c8dbc842ff7a | -15.90592 | -55.53571 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16ed9945-073e-3015-a40e-6aad4c83dfbd | -15.78866 | -55.56796 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d6b698b-0083-388b-94ed-aacccfd38960 | -14.68917 | -57.19561 | 2026-08-17 04:59:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5de50fe3-64e9-366a-b0a6-a3ad571a3b92 | -14.50246 | -59.32853 | 2026-08-17 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1df699e0-b66d-378a-a628-e5b6078103b3 | -16.92826 | -54.15004 | 2026-08-17 04:59:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9baa044-d57f-322c-a1b4-52c37dda77d4 | -14.4989 | -59.32354 | 2026-08-17 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d496bcc8-cf07-3f34-8c82-e236fee5b641 | -17.35435 | -45.62204 | 2026-08-17 04:59:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d2ea8ee-aa90-344b-a514-4d278185804b | -15.82808 | -54.21156 | 2026-08-17 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e14b2d1d-e137-32ff-9dc7-de3192d60b91 | -16.22622 | -49.70958 | 2026-08-17 04:59:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7419c0e2-2bf6-331c-a034-8355f73d424e | -16.18192 | -55.95523 | 2026-08-17 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 69059567-7c8e-3abb-9791-5ffc9e0871d1 | -18.44776 | -49.73643 | 2026-08-17 04:59:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dab2eec-3343-38d5-8194-b0363bf31ce8 | -16.23059 | -49.70557 | 2026-08-17 04:59:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b345ee7c-5014-3112-be1b-dc763848c7b8 | -15.91546 | -56.48668 | 2026-08-17 04:59:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a06a4c24-8c40-32f3-a1f9-dc84e7ae81a0 | -16.22046 | -57.64879 | 2026-08-17 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 248989c4-7efd-360f-a84b-740dd4c752a3 | -15.79006 | -55.58078 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10f21967-b462-395a-9e16-ac2ac57bd675 | -15.81607 | -55.53228 | 2026-08-17 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5f5ba3f-016e-399e-a83d-aeb3cdd90c2f | -15.94228 | -47.84051 | 2026-08-17 04:59:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b03406c-99b7-31b0-aa31-9a28a2b9eb79 | -15.83201 | -54.20855 | 2026-08-17 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| afe8eb4a-5194-3be3-9d5d-e247fc91b064 | -6.6384 | -58.9636 | 2026-08-17 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e8bee0c8-9648-3c6a-91fa-15ed3a07e274 | -15.8994 | -55.5334 | 2026-08-17 05:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 28fbd1d2-20a3-3385-b5ef-f6abc602d716 | -15.9189 | -55.531 | 2026-08-17 05:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 8ec28bb9-c64b-359d-9c10-56a4347f9121 | -14.084 | -58.444 | 2026-08-17 05:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 7f99f3fc-aeec-390a-96e1-bc60ad14813b | -6.1106 | -57.7425 | 2026-08-17 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 73d378f8-210e-3242-943d-6d40948dcc6e | -6.6568 | -58.9628 | 2026-08-17 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ec4b96c5-e2f5-33a4-9c75-97338e288ded | -14.1031 | -58.4423 | 2026-08-17 05:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| e9eed49b-05d7-3e38-9bdc-19e6014c526f | -6.6568 | -58.9628 | 2026-08-17 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| eadb38c6-e1c1-3d41-8d6f-ac227bb81f5d | -15.9189 | -55.531 | 2026-08-17 05:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 461c800a-73ed-308e-9b10-f6243d56c69b | -15.8994 | -55.5334 | 2026-08-17 05:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 135.2 |
| f69dd30a-1e98-3429-a57c-04170ab9c71c | -15.9185 | -55.5518 | 2026-08-17 05:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| b4e68a72-fdda-3315-95db-c5f29c74d823 | -6.6199 | -58.9643 | 2026-08-17 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 2296c2dd-6c5b-3902-86bf-0511bfa97e5a | -14.1031 | -58.4423 | 2026-08-17 05:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| f71e78f1-859b-39cb-9c26-7b16fb3e1250 | -6.6384 | -58.9636 | 2026-08-17 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 900b1801-4ad7-3b82-999c-69159d7701f2 | -15.8997 | -55.5127 | 2026-08-17 05:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 575e92ee-642d-3448-b377-f96243bfb856 | -2.95639 | -49.26682 | 2026-08-17 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d8cef98-6032-3f52-b07b-686df9b86345 | -2.76437 | -48.57142 | 2026-08-17 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43ffa09a-1b6e-3cab-9abe-122a59fff041 | -2.76894 | -48.575 | 2026-08-17 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20124cbc-c477-3844-9568-72b25b600e00 | -2.80678 | -48.59509 | 2026-08-17 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8e90832-3145-31a9-832c-c3f2e0f1ff2d | -2.87583 | -48.85531 | 2026-08-17 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 38d7665c-2fb3-3582-85f8-943c6fc48e54 | 0.49065 | -60.59398 | 2026-08-17 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb22d07d-4583-3c0c-bfdc-84dbed6f2b0a | 0.49101 | -60.59637 | 2026-08-17 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a430f10b-f540-3b9b-812f-fe5ee7278388 | -2.87806 | -48.85923 | 2026-08-17 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d3bb479a-e46e-3b9d-8923-d0fb616e559e | 0.49413 | -60.59085 | 2026-08-17 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c72b181c-ab7a-3b52-a52e-cd039fbb360b | -1.83787 | -54.48684 | 2026-08-17 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4801030b-ddf4-38b8-8049-f73eb431b8c8 | -2.80721 | -48.59223 | 2026-08-17 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb8069e1-4122-3546-ada7-19ea79df6351 | -2.80221 | -48.59141 | 2026-08-17 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b69e0c9-ab03-3bb0-bef5-750c5dfe5ac9 | -2.76981 | -48.56932 | 2026-08-17 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed53ef23-04de-35ee-8d2d-b148ad5cfd9f | 0.49457 | -60.59335 | 2026-08-17 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44a832d2-2d73-3ea9-ba38-ec9119f30385 | -0.83412 | -47.36227 | 2026-08-17 05:14:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d5f3c5a-c3ee-3f11-8b88-25c568153c6b | -1.83443 | -54.48631 | 2026-08-17 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3122b188-8450-3fa9-a7ff-f0113bc11bce | -2.76937 | -48.57217 | 2026-08-17 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eafebdd5-e87d-356c-9c3f-989d2747eb4d | 0.87346 | -59.66884 | 2026-08-17 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 800dddd2-2eb6-33c8-887e-377833028aca | -0.83464 | -47.35903 | 2026-08-17 05:14:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fcc53b1-5e4f-3334-b31c-18dd6882100c | -6.96651 | -59.29966 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efd90931-0553-3d25-b724-d4c9e49337ba | -9.08575 | -61.38951 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b0f5b49-b4fc-3371-af74-665bbf5c2712 | -9.21419 | -59.67218 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8740d522-06af-3a30-9ca8-c6e3f3c2a35d | -8.95709 | -60.54617 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72223ddc-207c-320a-a4c0-2b7a18ff18fd | -8.90223 | -60.59696 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 171a473e-4517-3392-ba63-139f38d208f8 | -9.17254 | -59.67273 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8c4096f-4067-399b-9942-086cf2ab3e0d | -7.37539 | -55.50719 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5056a2c3-3b39-3d82-972b-82a66f2c9488 | -8.95741 | -60.52227 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0d23468-aa5c-3dac-bfe8-01d4daca295c | -8.96152 | -60.51897 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa54f0a3-2de9-3cef-ab7f-cecdafdeb19c | -6.11587 | -57.71073 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README43.md)
