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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17d337f7-d6f6-36d6-9bcf-f8d95bcc2516 | -15.0362 | -48.56641 | 2026-09-16 05:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ca7507c8-ec3a-3d69-85a2-421357407b8c | -13.75871 | -48.79128 | 2026-09-16 05:38:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4584d11-4f66-3d67-9815-f278932ed1af | -15.46166 | -53.78001 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c0fbcf7-32f1-3a69-89d4-50cf1ad5f67c | -15.46607 | -53.78733 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f13e2ddf-2c41-31b2-9cc4-eee85375b05a | -18.03396 | -50.94905 | 2026-09-16 05:38:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a905d8bb-71f6-3889-b769-fd25a10237e6 | -13.4031 | -57.024 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 137888e7-49f2-3570-b9b0-6a5da2012947 | -13.39655 | -57.04176 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85d0d081-2a4c-35c1-9431-2f12eff22815 | -15.45647 | -53.77926 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55f7b532-7de3-32a6-bfb0-3a46f91e4a39 | -18.03342 | -50.95447 | 2026-09-16 05:38:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 33d8c212-20cb-36c0-b8ce-d43abda6cb1f | -13.76333 | -48.8147 | 2026-09-16 05:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| baf5e328-93a5-3e5c-b346-86e08f674325 | -15.50089 | -53.80788 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb1f85d2-b8f6-3b64-9989-9bb0ae864fb8 | -12.05593 | -63.37731 | 2026-09-16 05:38:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc00068b-fda6-3607-ba1a-3e927478fa4a | -13.44111 | -54.58086 | 2026-09-16 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16fb2e8b-3c52-389a-abdb-f0782d81158a | -13.37523 | -57.02069 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 646129fa-dfda-3504-8619-dbcbfbe10d74 | -18.0403 | -50.9505 | 2026-09-16 05:38:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3b8d4d48-bb03-3eaa-876d-d55f39f84ba5 | -13.39249 | -57.04118 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dde429d-1ea6-3604-b111-4b11e3acdd41 | -13.39904 | -57.0234 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d35786f6-0c9e-354c-8662-f016cd004c3b | -13.39298 | -57.03753 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38640abd-41ca-355c-8a69-7bfb0746aef8 | -15.49569 | -53.80722 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 15485a49-b100-3c96-ab63-7d175571a93b | -13.7602 | -48.79336 | 2026-09-16 05:38:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 277a904e-3a56-303e-9298-f54a574658a1 | -13.3904 | -57.02595 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da8d7414-3091-3eea-972e-2fd5a3831a6e | -13.75695 | -48.80838 | 2026-09-16 05:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c6f0ffa-bba1-3710-942d-76a14cd6c186 | -13.37877 | -57.02498 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa3c40ae-1bc2-35ff-aa1a-112c320a0f99 | -15.46127 | -53.78331 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5578bd69-db64-37c6-8f57-747d7cc6bafa | -15.48571 | -53.79948 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc287846-d72f-343f-afbd-ef2ffe683dd2 | -13.76418 | -48.82122 | 2026-09-16 05:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d06c2ce9-afe9-37b9-a38d-20a47dc18cf2 | -13.75805 | -48.79772 | 2026-09-16 05:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 108d9126-1a63-3c67-b057-1975ea591e78 | -15.04071 | -48.59272 | 2026-09-16 05:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1dabe12-00d2-3f60-85c7-a13ca41fd802 | -13.7697 | -48.82107 | 2026-09-16 05:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 048bc37c-3e75-3884-84ac-d279195ff4ef | -15.47608 | -53.79185 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51857ebb-a008-301d-a9a8-5b62debd653f | -12.80744 | -60.48732 | 2026-09-16 05:38:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6767bcff-ade2-3b05-93e4-bf2f694ff77c | -13.37821 | -57.02415 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b55e49d-2aec-3b71-b649-ddf16dae091a | -13.37929 | -57.02129 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d74b61d0-1481-3c47-9cc5-2a8bfbad2c7b | -13.37824 | -57.02866 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29065858-310a-3593-9594-7d6e4b2587e9 | -15.03896 | -48.56476 | 2026-09-16 05:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3dfbc84b-dac8-39f7-a8ea-c325df11a73b | -15.47126 | -53.788 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b208854-fe2b-35cf-a986-83fff1ee05f3 | -15.52683 | -53.85658 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fffa3d0-d8e7-3925-a615-c1257bc5e7a6 | -13.39497 | -57.02282 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 239816ad-e22e-3308-b119-acb0727d8648 | -13.76474 | -48.81616 | 2026-09-16 05:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28d55d6b-8294-31d8-9a62-8b346226d458 | -13.75953 | -48.7995 | 2026-09-16 05:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 943e67ea-06c5-386a-b7f4-d324b259de1d | -14.22569 | -48.51121 | 2026-09-16 05:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2d5536aa-da17-3022-9729-ea2efc9aeb34 | -13.37772 | -57.02785 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 15dbd280-c635-3e85-8c78-75766ed0e769 | -15.46646 | -53.78402 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b895f2e-ca72-3ba5-af8e-888233fb8b5c | -12.80688 | -60.49102 | 2026-09-16 05:38:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b763f73c-e396-3bad-bfb3-fba5e14f8d2c | -15.26789 | -56.28861 | 2026-09-16 05:38:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45ba0e42-525b-3cb0-8cbe-ed66f5b31318 | -15.04007 | -48.59893 | 2026-09-16 05:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d117b9ec-cc92-3e6e-8c59-18f69d0a812b | -13.21826 | -61.84797 | 2026-09-16 05:38:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0db01c3f-d19a-35cd-8392-a06d56da728b | -12.05933 | -63.37788 | 2026-09-16 05:38:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9f531e4-ec44-3dbc-94fe-713a2c93362f | -13.75182 | -48.78991 | 2026-09-16 05:38:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bed0441b-7ebd-3336-947c-ccc56b9ed587 | -6.3257 | -62.6721 | 2026-09-16 05:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 1977f250-32f3-3ffd-90bf-95c428800ba3 | -6.3256 | -62.6909 | 2026-09-16 05:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 5c446d00-b3b0-3713-98dc-dcad201fa78e | -6.344 | -62.6904 | 2026-09-16 05:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 2cca759b-5263-30b0-aa0f-587fad9c76e6 | -6.344 | -62.6904 | 2026-09-16 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ca8fa599-4266-3b6b-bd27-3ab2fdf0f7bb | -6.3256 | -62.6909 | 2026-09-16 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 4588f342-60b5-3fe8-9e2d-c8ab0c1558a8 | -6.3257 | -62.6721 | 2026-09-16 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| bec4bd0f-cb07-3dc6-a7a8-a8dd85f50cb9 | -5.49542 | -60.16808 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cad581ab-74c5-30a7-8690-53e939f0bd0f | -3.38495 | -61.30824 | 2026-09-16 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca918d2d-bf3e-327a-86e4-bdd127864adf | -6.32798 | -60.00972 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6944e0c3-43f2-3a83-bfd6-e57602bcaf13 | -4.51895 | -54.9509 | 2026-09-16 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4514f8a-23c1-3052-9570-679d3c6e4cd7 | -3.34971 | -61.29162 | 2026-09-16 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a5f2a3f-d67c-35d2-8778-87d1a3e439fd | -3.1734 | -61.11418 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9e598bb-d817-3489-b4d6-8fe590c0dc7f | -6.71648 | -58.8065 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b890c49-c4f6-3bc6-8590-3bfb920b279b | -6.1219 | -59.88153 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9e311b6-bb8e-3475-949c-6c5456fc643b | -3.37631 | -61.31057 | 2026-09-16 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f12c679-e2ed-3ed5-83d7-8017fc7edbef | -5.2403 | -59.98735 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 352a12b1-220d-3cea-985d-378eb5331b53 | -3.76328 | -59.39395 | 2026-09-16 05:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66fd770c-b04f-3210-b516-78f7b4e6cac8 | -3.51415 | -60.41579 | 2026-09-16 05:53:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27f16ac4-119c-37e6-a044-03df1c922fba | -6.34663 | -62.69159 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1946bb2-0a91-395f-b074-74b9c12ea7fc | -6.10059 | -57.63488 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5f2e22d-3750-3cf8-9687-ed53003d5468 | -6.71226 | -58.79989 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a983b26e-f3ca-393c-8a96-20634cb7b670 | -6.81213 | -59.17124 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1ec82d3-ecb0-39ba-bbdd-fad4f7564a83 | -3.17806 | -61.11114 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9a98739-4409-3f6b-980c-0345db641dc3 | -6.7169 | -58.80359 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d306ce43-bf58-3122-bf5a-d3a460557c7e | -6.79521 | -58.78958 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 605dbbea-9f89-33ea-a09b-87aa3d76d85c | -3.12309 | -61.25006 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e1a641c-6b49-318f-8676-cf4755254005 | -3.58539 | -58.54012 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0b68e73-f97d-3549-9a6e-c5029dbcaf08 | -6.35061 | -55.56132 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bec588c-8aae-30c8-a473-62a8ecdfb3ef | -3.17863 | -61.1075 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 502e5e05-8bfd-3f18-9468-93635857ec45 | -6.34434 | -55.56068 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ac552b1-5fa1-3936-8d5f-d8eec65e8193 | -6.35481 | -55.56479 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dd5877b-bb70-3209-9529-c8d60e98cff9 | -4.51972 | -54.94566 | 2026-09-16 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c3cf445-1d2a-3d28-9439-a50be41defd5 | -6.71184 | -58.80285 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6629ac46-e45d-3df6-9032-6d2b60c20c01 | -5.75539 | -57.59804 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 16bc2edc-996e-3d38-861d-c68c57be0a23 | -6.32474 | -59.99941 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 165a9b5b-e232-38c3-8b2a-7868ea878a00 | -3.42617 | -58.23139 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b81a6bc4-c575-3fdd-a4ed-e751c851cadf | -6.32544 | -59.99465 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87fb1ac4-71cc-3d20-8948-70cc7f1319b3 | -6.02897 | -57.77253 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1f9f7c4-032f-3570-91e6-adeb8fe8147d | -5.59069 | -60.18903 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a2091a7-a5d5-3b4e-8aec-9cae3497be7c | -3.37204 | -61.33903 | 2026-09-16 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 948304f8-cdd2-3bc2-94b4-76141a893dcf | -3.58458 | -58.54562 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d11b33a8-3e8a-34a5-8323-f6a34704ce75 | -3.54999 | -58.67929 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd7f0f19-d0c3-34f7-b026-0574385e4a6e | -6.07404 | -57.8626 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 520fe824-abdb-3631-a855-19411d35d0c4 | -6.34275 | -62.69101 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4ac95a9-e70b-3e68-97b7-4526f364070c | -3.81213 | -58.89553 | 2026-09-16 05:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 129f7e3a-833a-39e7-9c91-70c7442c8b31 | -6.77877 | -58.79617 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e8f5dd9-a072-3481-a600-aefd89dceff6 | -6.71142 | -58.80578 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9aa630e-6701-3d1f-8dbb-1b011d5c631e | -3.36959 | -61.32775 | 2026-09-16 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ca83774-c024-3faf-b7a5-3a5364c5eb04 | -6.76659 | -58.80943 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a8d63d9-0874-3c5f-a671-404491fe9447 | -6.36297 | -55.82983 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f163039-92a9-300d-8bfd-7d2358ba7554 | -6.33573 | -62.68501 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |


[Clique aqui para ver as próximas entradas](README62.md)
