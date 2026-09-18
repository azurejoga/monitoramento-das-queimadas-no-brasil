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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7804c457-977f-3b16-85d3-d0a523649913 | -2.6985 | -57.615799 | 2026-09-18 01:02:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc838bee-40f6-3d57-afe5-150e9c9404de | -11.2788 | -43.5037 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 66f87047-500a-3f13-9799-125141e9f46f | -9.7189 | -54.821701 | 2026-09-18 01:02:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93eed8eb-9cbf-3fdf-9e50-9ec1a35168e0 | -6.6648 | -50.900501 | 2026-09-18 01:02:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80660cbf-52e0-39a0-b77c-bcd92ce8c9bb | -11.3201 | -43.348598 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e52e6da2-2143-3aed-a5ac-b1c232275e12 | -1.8354 | -54.930099 | 2026-09-18 01:02:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7ec2015-aa98-3a56-bda6-2fd2c7536dab | -21.624901 | -50.007198 | 2026-09-18 01:02:00 | METOP-C | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d63b10e3-e36d-3da1-9217-c01a085a6b60 | -10.824 | -50.190399 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9eab25f4-1bb5-37bb-a7f4-9084727b1e11 | -4.4472 | -55.478199 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82d20b03-5f7e-3519-af82-ed84d0458d97 | -12.3871 | -50.7215 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9dbf76b-4b01-3f62-a919-8f476a832002 | -2.8188 | -50.466702 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c293ea06-c344-33c5-9b68-cebf0b52c613 | -3.9241 | -55.761101 | 2026-09-18 01:02:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be1f4537-3cdd-3fb6-a7af-3bbc8dbde70d | -3.3802 | -50.444801 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c43e3c59-8d80-3a11-bef7-af47a3d52298 | -12.4699 | -50.897598 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a651728f-ba91-314f-8fa2-87d42f1b6b6e | -9.7107 | -54.831001 | 2026-09-18 01:02:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f056e10c-3dbc-376a-be22-55bf34385745 | -10.8143 | -50.192799 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f29b900-9817-32e6-b231-5729955e7aa0 | -6.5268 | -49.888302 | 2026-09-18 01:02:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fda37fe7-2692-3de4-b114-6f283694ead0 | -6.0233 | -51.769001 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e948afd-effd-379c-907e-f30679a7e5a0 | -1.7116 | -54.8857 | 2026-09-18 01:02:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ad0a6b8-f3a2-3888-94ae-236d200cb3ee | -6.0327 | -51.8088 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fe5c995-1c19-380e-ae71-ebd6f4927429 | -15.6678 | -52.732899 | 2026-09-18 01:02:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| acb89df9-1252-3bdb-afa3-15fe270e5490 | -12.3633 | -50.751999 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7279b19c-ee56-3896-ab3a-1f0f6869c250 | -12.3339 | -50.759102 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0436252-c7b3-3ad7-91d8-02925c9627ab | -21.0401 | -48.464901 | 2026-09-18 01:02:00 | METOP-C | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c93ed50d-699d-3a0f-a7d8-23f7336f10aa | -6.3687 | -58.291401 | 2026-09-18 01:02:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58794fdb-af0b-3b70-a7ab-1df05bd02b3c | -4.509 | -54.9832 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87cd2cf8-a620-3919-a68c-09c545e39aa8 | -3.921 | -55.747398 | 2026-09-18 01:02:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef2d5cad-2864-36e5-b619-095a2bfba5a6 | -12.3242 | -50.761501 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3052b0e-c974-3e90-8d43-a0ca102adae5 | -3.3728 | -50.4571 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f051221d-6e1f-3710-8715-02fe8c091af1 | -19.1786 | -48.7812 | 2026-09-18 01:02:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 07d7c130-9f68-382f-9ee1-dd5a232aa3d3 | -5.743 | -52.2463 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a926acf0-5fbb-3b54-986d-11f67c260880 | -11.8247 | -46.808998 | 2026-09-18 01:02:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4afa1dbd-56fb-3572-8a46-66dfbbc2c769 | -12.5797 | -47.095299 | 2026-09-18 01:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6a9c1b3-a123-3da7-a2ba-7ab8c5d72f5f | -3.4674 | -54.714901 | 2026-09-18 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 389b2b52-342a-3930-b4ac-886a267744eb | -4.478 | -54.983002 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 914bc0f9-fceb-3301-a949-9f64ee91ce72 | -4.5075 | -54.976299 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a67d8514-9673-3103-9c78-278ce538a0c6 | -4.4354 | -55.516899 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20ee2de4-f72e-3436-adc5-06c30327ed89 | -2.8846 | -54.0672 | 2026-09-18 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 123214ec-83a8-36ff-9f0f-d3e759c07578 | -12.4645 | -50.874599 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed9aedc6-ca4c-3e45-965c-b3beb5e23ba6 | -14.7082 | -52.452499 | 2026-09-18 01:02:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77f24db3-66a5-35d5-a19a-f1d727570d62 | -12.3186 | -50.738098 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a478a61-b114-3789-9d1a-a1bb9cfc6a29 | -4.3726 | -55.423 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9ad6561-0332-36a1-b863-d6b177d85e96 | -12.293 | -50.7607 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9054bee3-d629-375a-a5c4-712dafa93f80 | -10.9946 | -57.066399 | 2026-09-18 01:02:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac752c68-2597-312b-9d3f-efe7ca2713f5 | -8.9353 | -51.462502 | 2026-09-18 01:02:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c47aebd2-a782-3e2e-afbc-21f2af6535d3 | -8.9304 | -50.917099 | 2026-09-18 01:02:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc418cf-b634-3f56-92ff-e1a45b2b9dc1 | -11.022 | -54.158298 | 2026-09-18 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c571fe0-6430-302d-9488-b00ac23eed92 | -7.8092 | -44.894199 | 2026-09-18 01:02:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40700747-490f-3fe9-b5c1-3a668052949e | -10.5229 | -46.7304 | 2026-09-18 01:02:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30bc0586-2b42-3c89-bb50-bb4ef7f07786 | -3.7043 | -54.176201 | 2026-09-18 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d029612e-b3f0-3ed4-8691-acb9c18f05f2 | -11.2702 | -54.1166 | 2026-09-18 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8ab61ef-6fde-37fe-89b7-d6081ee46e63 | -2.8334 | -50.485001 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e256e296-53d7-321e-80d8-9c3074ba3c9e | -6.6668 | -50.909199 | 2026-09-18 01:02:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2dfd4a5-faa5-357f-ac7c-c3c9517258b0 | -3.3379 | -53.2621 | 2026-09-18 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e693aa0-d754-3448-aa59-a1b1292fdf16 | -9.9169 | -46.539001 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a179137-846a-3cc1-baaf-fb15a3da5895 | -12.2832 | -50.7631 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 238847f4-3853-3e24-9170-921f02b0d299 | -4.5502 | -54.938099 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2975820-1ea4-3ab7-9e76-8de0206924a3 | -6.5171 | -49.890598 | 2026-09-18 01:02:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 900a8e56-81c1-36e0-bd64-f54535a44dba | -4.5471 | -54.9244 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f20b8f55-2286-342b-8795-870dbb71fe2e | -3.4982 | -51.253201 | 2026-09-18 01:02:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a45e21a-8334-3646-a9c9-33b5f5f34305 | -6.1209 | -59.955502 | 2026-09-18 01:02:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b112862f-6a87-3e03-8672-89f613c9f918 | -3.3295 | -57.854099 | 2026-09-18 01:02:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6145d595-ba8d-3ecb-b2e4-c98ce8e860be | -8.3918 | -47.209202 | 2026-09-18 01:02:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62e180ba-184e-3a20-b3f0-3131df85911d | -3.4803 | -54.726398 | 2026-09-18 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d868d62b-9054-3221-a8d7-68b64adcdbc2 | -11.5333 | -46.884201 | 2026-09-18 01:02:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 753dc1b1-33c8-34e3-a9a5-5cc22dd17411 | -12.326 | -50.769299 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e2b487c-9bda-3291-a901-0ab7e94cec82 | -10.8045 | -50.195099 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6bfd8d78-8b25-323f-9912-2794ab079505 | -7.8144 | -44.914501 | 2026-09-18 01:02:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 97d449b0-2932-343e-b51d-0c6c2b93c047 | -11.1389 | -49.0518 | 2026-09-18 01:02:00 | METOP-C | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ebd40e2-8bdd-3eef-9366-e1a9d539b06a | -2.0626 | -52.168301 | 2026-09-18 01:02:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfb8907a-2e1b-3703-a7b5-0ed7c75f307f | -3.2695 | -54.259602 | 2026-09-18 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45163d49-b16a-3371-b6d7-1e11ef983778 | -14.9036 | -48.153 | 2026-09-18 01:02:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b83db4a-90f1-339f-baf8-ab5e65abf076 | -4.5636 | -54.906399 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0125f7a-17cd-3cea-9d04-c2516e69347b | -12.4761 | -50.879902 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 086831c4-e82e-38e1-8ea7-56f54eeed18d | -11.6642 | -54.4505 | 2026-09-18 01:02:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e4b3877-62e4-3ad4-aa43-aaa54c4634d4 | -1.7018 | -54.887901 | 2026-09-18 01:02:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd7df8f-b91e-338d-ae02-d269a031a104 | -12.63 | -50.875198 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b6db5b65-f4cf-3179-b01b-1529be4c7120 | -12.4519 | -50.689499 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bbd60ae-81c2-3896-a2f5-deff36983f86 | -12.2098 | -53.2117 | 2026-09-18 01:02:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68dccc14-659f-3227-8768-3ba8ed577812 | -4.3709 | -47.780602 | 2026-09-18 01:02:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0e8cc5e-25a9-3541-a105-2e990d9c9b7b | -12.26 | -50.752201 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbf5c563-2161-30bf-a629-6fcf79ae8460 | -3.368 | -50.436798 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fada3d0a-a75a-3abd-87ff-310982687083 | -12.3284 | -50.735699 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0086da8c-82d7-3db1-9f60-96854c15d3be | -4.6056 | -42.966 | 2026-09-18 01:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3d3d8de-4e0c-3b52-88ea-d2898154dbf8 | -10.6522 | -50.249901 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62d3c8e6-619f-3f90-8c13-7c8935c2cdc6 | -14.9395 | -49.929199 | 2026-09-18 01:02:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2368a743-59eb-3fd2-88f1-c3d4b74baff0 | -12.3456 | -50.7645 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07a1c010-5e66-3b9f-a3ff-4bc2b65b095e | -3.0448 | -51.385799 | 2026-09-18 01:02:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec86b3fb-9581-3aa4-ba35-e49ad558764c | -4.5943 | -43.001999 | 2026-09-18 01:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bfdda33e-2b96-33a7-b50c-f78ed8d5c994 | -11.5301 | -46.871201 | 2026-09-18 01:02:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f476b15-f818-306e-9ffb-8fe87043bac1 | -4.5785 | -42.939602 | 2026-09-18 01:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e8d0e4d-694e-37d6-9386-f477c099c5fc | -5.7412 | -52.238602 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 765fb0c9-40dd-3b3b-b9df-3c7e5cee6c57 | -3.3396 | -53.269402 | 2026-09-18 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e693eb37-c31a-39d1-b75d-11cab6e4a480 | -12.6203 | -50.877602 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3538a144-199c-3050-b138-1ee26646e78b | -12.2753 | -50.7733 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7bbdb82e-9c92-376e-b94d-ce182454e607 | -19.180599 | -48.789398 | 2026-09-18 01:02:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e81b87dc-dd81-3358-975e-4b38e17076d2 | -3.4284 | -58.1991 | 2026-09-18 01:02:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f191723-5702-30e3-914e-25c92ef7b2ef | -12.3144 | -50.763802 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 940f43b7-b5b2-37bf-b53b-603663cc64c1 | -21.0693 | -48.4571 | 2026-09-18 01:02:00 | METOP-C | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 41965aae-6568-3b5c-beec-702b2c664b93 | -16.414 | -49.9543 | 2026-09-18 01:02:00 | METOP-C | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README14.md)
