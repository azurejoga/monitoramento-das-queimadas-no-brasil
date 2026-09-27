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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92e50ec5-726d-3024-a0ac-50e2022ce4aa | -3.066 | -58.405602 | 2026-09-27 00:53:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf532ac3-238c-3542-a99a-3e1def9a2c6a | -11.279 | -54.4375 | 2026-09-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e246843c-7e66-3e85-ad96-289c565293d5 | -3.295 | -54.696301 | 2026-09-27 00:53:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 851aa43b-3e6e-376f-be9a-487bc0f0e4ba | -11.0186 | -54.048302 | 2026-09-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61ea8caf-9bec-3709-b636-be58849e80a1 | -23.579 | -51.618 | 2026-09-27 00:53:00 | METOP-B | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ee317e1-d5e5-3416-abe7-cce17a203c5d | -10.6734 | -57.627399 | 2026-09-27 00:53:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2a47f77-fc8b-34fd-af77-a0a1555c287d | 1.6599 | -55.9254 | 2026-09-27 00:53:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4df2b8da-31a7-3d70-b9e6-c690c52a0b2d | -1.613 | -54.918201 | 2026-09-27 00:53:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e7d3efb-a897-3504-abb5-1c5abbca884e | -6.7184 | -52.990299 | 2026-09-27 00:53:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4719a8d2-f476-3a6f-8014-feac2980b14b | -11.964 | -50.590801 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be53c57e-2754-3d84-a673-d36bc20290ed | -10.2428 | -59.122398 | 2026-09-27 00:53:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 714aa7d4-6c87-3e28-b70b-576774124e4d | 2.8952 | -60.267899 | 2026-09-27 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d70d131f-fbfa-3fe1-9cbc-19908fd4d3c6 | -11.0383 | -51.322399 | 2026-09-27 00:53:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af9c3488-4add-3788-b28d-d1e18bdda901 | -1.0435 | -53.565701 | 2026-09-27 00:53:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39348f83-0a7a-3d6a-8094-b64b617459b6 | -6.0812 | -57.625599 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e57f34ab-9387-36b5-8398-dca352c04fb3 | -7.692 | -54.754799 | 2026-09-27 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c41ab9d8-c694-3ca2-b161-16b13b904409 | -6.1299 | -53.064301 | 2026-09-27 00:53:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bcc34b5-a75c-3191-926a-d64140795e82 | -20.842199 | -57.716801 | 2026-09-27 00:53:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6584fd9b-e416-3bfc-9e26-553661df0a23 | -23.5762 | -51.606899 | 2026-09-27 00:53:00 | METOP-B | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e85de34-d14e-333b-8b2e-1766df5ec5f0 | -17.049999 | -56.578701 | 2026-09-27 00:53:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dfec7974-08d9-30d9-93a0-e1d3fde05cee | -10.2542 | -59.127201 | 2026-09-27 00:53:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6980002-00ba-36d6-b7ae-10c0ba5d5545 | -4.4917 | -54.934399 | 2026-09-27 00:53:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e15e01a5-5382-37aa-a1ae-efe4575a2962 | -6.0833 | -57.812302 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e4a8145-1af9-391a-8fc0-c473d86dffef | -8.0328 | -54.885899 | 2026-09-27 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5272f8ae-a9b7-3ece-ae9c-02f5b01eede9 | -6.0637 | -57.816799 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecc0fb45-874e-321a-b26f-10c94cd6bd33 | -4.5429 | -54.977501 | 2026-09-27 00:53:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aafd3769-a7bc-3bb9-83fe-e849879945e1 | -11.9197 | -50.539398 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 179160b5-fc5f-3d9f-86e9-1aebcbf5f090 | -30.8211 | -54.350201 | 2026-09-27 00:53:00 | METOP-B | LAVRAS DO SUL | RIO GRANDE DO SUL | Brasil | 4311502 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 9efe9453-fe23-3657-a2bb-e684536c88bd | 2.6509 | -60.163898 | 2026-09-27 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fa17dccb-b84d-31df-b127-ea3d6191acca | -17.0518 | -56.586399 | 2026-09-27 00:53:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e8ba031-09b8-3a1d-a0f6-330ae6370ded | -11.0254 | -54.033798 | 2026-09-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 238be614-8826-3a92-be1b-ca902c7fcc1a | -9.532 | -62.2644 | 2026-09-27 00:53:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2a984264-0729-37a6-bffe-66e5bd367f7a | -3.9617 | -59.3452 | 2026-09-27 00:53:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50f001b3-d4c5-3735-bb04-f81bf1045386 | -12.2932 | -50.3092 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa918691-6010-36f7-8449-4be4de805512 | -6.093 | -57.631901 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46d3df80-7059-3aab-9095-3bc20b4f0235 | -2.6687 | -56.460499 | 2026-09-27 00:53:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faeeced1-211e-3fc2-a749-f26c0159a742 | -6.091 | -57.623299 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b491afdb-ef19-3508-ac19-3608f84ca071 | -23.5734 | -51.595699 | 2026-09-27 00:53:00 | METOP-B | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 986d4208-dfab-33b3-b894-af7cd7d8d9f1 | -7.6794 | -54.745201 | 2026-09-27 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb458ec2-130b-3ce1-a0fc-421b2838ad9c | -2.79 | -57.6978 | 2026-09-27 00:53:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf90de9c-c9f3-352f-9c63-718a3f76d67d | -3.96 | -59.3377 | 2026-09-27 00:53:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3d874ba-0f7f-35f7-b48c-fb9ea7fb365a | -11.9293 | -50.5368 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62f27672-5a2c-3f55-ad39-6ebf4f29fc39 | -11.9589 | -50.571098 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a7f8de8-8aa2-3ff2-abd8-61bf12436997 | -11.8856 | -50.527401 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 638ebec6-4cca-3341-b184-c529ab1cbed9 | -1.6751 | -55.896599 | 2026-09-27 00:53:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84d64f7b-0d91-3c0b-a514-aa8ab37c7919 | -12.2739 | -50.314499 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0dea0523-e463-3fc3-8850-c53ade1064fa | -10.8158 | -60.712399 | 2026-09-27 00:53:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1077803b-24b6-3f87-b4bc-caaae33c69ca | -11.9049 | -50.522099 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a936a317-7263-3f73-8ad0-9ca6a376ba7c | -2.0524 | -56.864101 | 2026-09-27 00:53:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd47c85-3cec-3fa5-a854-766e9b206c0e | -11.0337 | -51.304199 | 2026-09-27 00:53:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8cf9833-f130-38a3-ba55-3fb94a1f8d82 | -7.7107 | -61.240398 | 2026-09-27 00:53:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4a1050c-e82a-30b7-beaf-7fb9f379894a | -11.7634 | -51.012001 | 2026-09-27 00:53:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea0a4d37-cadf-3197-94f1-5a0fc35e402e | 2.8934 | -60.275902 | 2026-09-27 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9dd6ebb9-13bb-38fb-8ae8-a33eb880d4a1 | -12.893 | -61.706001 | 2026-09-27 00:53:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb080b3-3c1b-312d-a7d1-41f3d137f708 | 2.6375 | -60.1777 | 2026-09-27 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b12f6834-cecd-3811-a4f0-c4f81208f8db | -3.2917 | -54.682098 | 2026-09-27 00:53:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f87ab5d9-e6b1-366e-a940-e130b452c2a3 | -3.9698 | -59.3354 | 2026-09-27 00:53:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6de5de1-fd42-356f-b7b6-c6a037a34025 | -9.0411 | -66.051102 | 2026-09-27 00:53:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8221c25c-92c2-368d-9678-be549ef96a31 | -6.0715 | -57.806198 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8327fdbc-ebbc-3b7c-8e69-0da34d86e70a | -2.0622 | -56.861801 | 2026-09-27 00:53:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c984921-715c-3fc2-81b0-fa0e58a1a44a | -10.8205 | -60.733398 | 2026-09-27 00:53:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8064328c-6bb3-3226-9a02-90b781b7c17b | -10.806 | -60.7146 | 2026-09-27 00:53:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9543b122-1c70-38d2-851b-47977555cd5d | 2.6491 | -60.171902 | 2026-09-27 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c3bf6c90-ca26-3b7a-991f-b7a08343aa12 | 0.4944 | -50.956402 | 2026-09-27 00:53:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4d42b4d4-04d6-3b24-8282-546dc7211f90 | -2.0646 | -56.872398 | 2026-09-27 00:53:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7166531-9294-39aa-9248-af2da5bcfb82 | 2.6429 | -60.153801 | 2026-09-27 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 55b33040-979a-3fc0-8c2d-12fd5737c3e8 | -11.9882 | -57.598801 | 2026-09-27 00:53:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6ff0741-c5cd-3f39-8dee-0fcc557cd68d | -2.6662 | -56.449402 | 2026-09-27 00:53:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dec68ae0-1c7e-300c-9ed7-376aca323789 | -4.3774 | -56.329899 | 2026-09-27 00:53:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eec04ed-5ea2-3ec2-9bb5-0e84bd909c8d | -6.0559 | -57.8274 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1284d04-2856-3742-aa0d-64e8184ef4d5 | -4.5302 | -54.966801 | 2026-09-27 00:53:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4dc2384-ebc7-3fee-b198-6ac9a6396539 | -11.0089 | -54.050701 | 2026-09-27 00:53:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43b43602-5780-3787-81b2-c707c8b826e2 | -9.9308 | -60.713699 | 2026-09-27 00:53:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03cbea48-f276-37ae-8299-0a864634512c | 2.6473 | -60.179798 | 2026-09-27 00:53:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 815328db-2fae-3d72-a2aa-b8e6550aff5f | -4.5332 | -54.979801 | 2026-09-27 00:53:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad621ddd-7a6e-36fa-82f7-625c2c46352e | -6.0539 | -57.819 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ccac478-ecb8-3bb8-b13f-96f4ca41f403 | -5.1549 | -56.000702 | 2026-09-27 00:53:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baa34061-1e03-3140-b6e7-631beb3e254e | -4.5399 | -54.9645 | 2026-09-27 00:53:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e435a62-cdea-3810-94fc-934e066cdf28 | -11.9345 | -50.556599 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8117fa1-ea2f-397a-8732-08653b282d84 | -8.0231 | -54.888302 | 2026-09-27 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4471b0c2-be37-3668-a06e-66bb065eae75 | -3.1791 | -51.027802 | 2026-09-27 00:53:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90af0aef-fa50-3a54-9efe-c8aa2693f9d5 | -21.562401 | -56.724998 | 2026-09-27 00:53:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 79ec77ac-2929-3d68-9d99-70108242fa33 | -9.6102 | -55.0951 | 2026-09-27 00:53:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a87794fc-e38f-35cc-b98e-3cdd71a7ad32 | -4.4948 | -54.947498 | 2026-09-27 00:53:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5bcd151-3ced-3642-9a33-cd91f6a4e7a2 | -1.5988 | -54.813099 | 2026-09-27 00:53:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 232c40e7-2df2-3457-b10e-46b033191264 | -4.3749 | -56.319199 | 2026-09-27 00:53:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81685c9a-0966-3d19-af3c-c46ba56ec8b7 | -9.9323 | -60.720699 | 2026-09-27 00:53:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 867cfc98-8caa-3b64-8f6a-11ff3b44b6f3 | -11.9737 | -50.5882 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a67f6283-46f9-34bd-b149-349f3fa5d166 | -4.5014 | -54.932098 | 2026-09-27 00:53:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c3d8fab-9040-36c9-b43f-470d280a2aae | -4.2422 | -51.0364 | 2026-09-27 00:53:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f793580-d325-3e4a-88cd-f0b62a95509a | -12.0426 | -51.414799 | 2026-09-27 00:53:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 31cee060-1cf5-39d4-adee-b5a0301e39cf | -11.8952 | -50.5247 | 2026-09-27 00:53:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| edfd72ab-bb15-3752-aac8-3dbe932fa7d0 | -4.2482 | -51.061001 | 2026-09-27 00:53:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7fc665e-939b-34eb-b84e-308a6103744a | -6.0832 | -57.634201 | 2026-09-27 00:53:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f7ef1a4-00b8-3173-892f-0bd86d39e277 | -10.2526 | -59.120098 | 2026-09-27 00:53:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66e9e7aa-949d-3743-bf8d-734d0c92c123 | -15.4325 | -57.404099 | 2026-09-27 00:53:00 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79fdf7ce-6570-3724-9934-374e0df3359e | -6.7143 | -52.973801 | 2026-09-27 00:53:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5c7a701-1e6e-329d-94e2-eb3d9542eb05 | -17.04906 | -56.57011 | 2026-09-27 00:54:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 7b310d5b-f379-3a6f-a690-2f40d0380a48 | -17.04099 | -56.5781 | 2026-09-27 00:54:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 88b8f761-ee1c-3a4b-ab6b-2740de34a297 | -17.05181 | -56.58646 | 2026-09-27 00:54:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.2 |


[Clique aqui para ver as próximas entradas](README4.md)
