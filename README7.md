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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c7fb165-6c78-3786-a0f5-b96b152cbc2e | -6.8795 | -43.693001 | 2026-10-08 00:26:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e1de5fe-fe6b-3a76-b14e-d5591111e3b8 | -1.5389 | -54.820301 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3619e45c-cad6-3457-a4e9-2ad1e304a967 | -3.2415 | -56.796101 | 2026-10-08 00:26:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 100fbe4c-4364-3986-9534-961ab3f6bffe | -7.2323 | -55.163898 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ed89420-ac62-3c9c-a898-7d80a29ef287 | -3.0597 | -54.251598 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47a7579c-f494-37de-8817-700b8ee2bc1b | -3.5038 | -54.619499 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55b13d8e-21b2-3034-987a-99aacf22c7e3 | -8.2564 | -54.722801 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb4eaeb8-47c4-3937-b7b1-8256a9651353 | -7.2755 | -46.788399 | 2026-10-08 00:26:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d186733e-9570-3e09-9da2-0e990077a6b7 | -16.352699 | -55.331501 | 2026-10-08 00:26:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6b1dbcb-876c-320c-bea6-f10cb74d6f42 | -3.2836 | -54.0569 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0696a25-4672-394d-8028-c58c5d604b70 | -5.8671 | -50.088299 | 2026-10-08 00:26:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfd0e211-ef59-30ea-9a9a-ebe8fa18852a | -3.0234 | -53.955101 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce18c259-6142-3a13-9c26-38ca0eebfd38 | -3.0041 | -54.097599 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7999a442-9fa3-37a8-9fc2-6de1b1708e02 | -4.3441 | -43.819099 | 2026-10-08 00:26:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e6ca973-51b7-315a-9516-4293fc63ffb0 | -3.1664 | -54.723202 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 443c8fc8-2639-3326-9d6f-e4d2b76ed087 | -4.1557 | -55.133099 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 758638d3-5762-36b2-8147-da4a391f22a2 | -6.4674 | -55.4739 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33650350-7c7b-3360-9039-ce045530909e | -3.4348 | -56.923801 | 2026-10-08 00:26:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7ea13b6-1e2a-33c9-a36a-9780dcedbe49 | -13.3067 | -48.670101 | 2026-10-08 00:26:00 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f3cfec7e-825e-39ea-b3f1-4be1abbd1cb8 | -6.33 | -55.319401 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5308a8ef-1256-31b3-a674-ef9e9eaa0e9c | -3.0177 | -54.7491 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da87756b-39b9-3142-9c40-68f291ae865e | -3.5616 | -59.480598 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72e3e244-8703-386d-bc2c-6a72726bddfa | -3.0146 | -54.7355 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5631d654-93d4-3e67-9444-c68275b585ab | -3.5451 | -59.452801 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f478b28b-8358-33c2-a25b-a834c485160f | -5.8906 | -57.750301 | 2026-10-08 00:26:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bda1a14a-e49d-3d16-8025-03b07c2f7a45 | -3.1912 | -50.5457 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e53da69d-60c1-36a9-beb5-08ef6f577b3f | -2.9557 | -54.202599 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebb77e7d-800b-3423-b4d0-5a5f05b7cea9 | -4.1345 | -53.989799 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92855dc9-bfdd-3a44-88f6-7887ce442928 | -6.5074 | -55.376099 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cece687e-0d20-35b0-81be-b8ea1c5329cf | -6.3071 | -43.3302 | 2026-10-08 00:26:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 690e8c7f-8f9b-3a66-b6ba-9d007c6af748 | 4.6883 | -60.571301 | 2026-10-08 00:26:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 075b5639-3be4-3df1-8658-f8a2b297e462 | -6.6701 | -55.089802 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8025aa5d-4868-3e60-89c1-5f50a9de9616 | -16.8445 | -40.563099 | 2026-10-08 00:26:00 | METOP-B | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34adbad4-e693-3dab-bb77-4578635f2482 | -2.9959 | -54.106701 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43ac41f6-07ad-3d4b-9975-3becdbdf19fe | -3.7853 | -50.754299 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 787b7d8d-04c1-3d19-8969-9c177010c1f3 | -2.584 | -56.162201 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58c1e7b0-8abc-3431-a92e-4368176ef36c | -3.2981 | -54.075401 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86a61f02-0c58-3155-b6ef-7198bcfb9107 | -5.9989 | -55.681702 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 064c0425-2845-3eca-8170-c09c60626ab5 | -2.3803 | -56.126801 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9825b40c-352f-3047-a0fe-427a84275b94 | -2.4835 | -56.082001 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 734ef892-93b9-3210-9bc3-08bc57a13d9b | -2.979 | -54.168499 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b82cf2e9-4c5c-354a-a8e3-2bc5bbf8f2bc | -4.5826 | -54.9235 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b977e72-7f3a-3016-aec3-8d299e774de3 | -3.1016 | -53.754601 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f74e22f-fbe9-36a6-8b5b-a3d394bacce1 | -3.2094 | -53.957199 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7783886d-da60-35a5-b6da-bdcb8a2ac0e9 | -3.5211 | -59.3442 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 778b4761-9949-3b3e-9b20-2f16ebc70cc9 | -2.8797 | -54.1399 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70ac39d2-34fe-3c00-8dd9-8e2ce3b3d732 | -3.8267 | -55.777699 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee287d19-f8b2-334b-9622-2cb4bb52bab2 | -10.4291 | -47.286201 | 2026-10-08 00:26:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb591888-7f50-3484-9086-47f2069c9522 | -4.7254 | -56.157398 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7b13a53-7967-352b-ba68-b01f65b42fd5 | -4.1097 | -54.016998 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17b9744c-a0bd-3d67-ac9d-c921247a6204 | -6.1427 | -53.070599 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83170406-703f-3436-ae39-8c0af3adb940 | -5.7741 | -52.360298 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea919237-c7e1-310c-927b-f68e17365aef | -5.8923 | -55.526798 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63b93d7c-7b89-3f6b-97d5-009575d7ad17 | -3.5442 | -59.4949 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80639358-e866-3496-8159-28828d91b3d8 | -3.4479 | -56.936501 | 2026-10-08 00:26:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b29b2f22-1409-34f9-a436-14c9ef549fb9 | -1.7956 | -57.0994 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 617f1ab0-dfa2-33ad-b16e-d65c0f82e23f | -3.176 | -58.622299 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd65b103-29c8-33ac-887a-e8b853776e88 | -3.7325 | -59.4645 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42f0103e-6a50-3a68-95b6-70436ffd4bed | -3.5594 | -59.4706 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26ec960f-b71c-3761-be45-76e0564f92d5 | -2.8766 | -54.126099 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5de9a086-a96f-3940-b98a-6e0d269a4798 | -6.1413 | -51.937901 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4253cd58-f80e-3ac5-ae97-e32c348a5106 | -2.8261 | -57.607601 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35d8c587-bd47-362e-adaa-651dbba2a093 | -2.6128 | -56.473301 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7886cf9-6609-3085-b46a-ccd82a41356f | -3.864 | -55.989601 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0edce270-99bf-3435-9cb1-3de1b7f787a2 | -4.1113 | -55.1646 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc2b3990-14a3-39d5-a59a-9cd358554408 | -2.6262 | -54.750401 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45f8d359-d855-3f8d-9e98-7b0953bf7b5d | -3.5644 | -54.477001 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e32dfc8-e22d-3cce-84ff-7acefcc0cbee | -3.5152 | -54.6241 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b00a7140-0fae-30c9-bc91-239f4ab6f4bb | -1.8327 | -54.933998 | 2026-10-08 00:26:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3bd96d4-9f06-3bb6-8440-16091a29c09a | -3.2652 | -54.658298 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0bdb2b6-6d30-30ac-a0a9-f7d9d3641b1a | 1.7032 | -55.618698 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6daeb85-b136-306e-acc5-56513cdcb816 | -3.3584 | -50.467098 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9abf8285-a060-3fbe-8cd0-7f867696c8b5 | -1.463 | -54.758301 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97320a14-9d26-37c6-9639-be8d3fe30268 | -16.8832 | -40.886101 | 2026-10-08 00:26:00 | METOP-B | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8396a113-d6dd-3f0f-ba7b-50880c726dca | -7.2198 | -55.107601 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f8c1d42-14a7-37a3-881e-21702564f697 | -3.5549 | -59.450699 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a808268d-1e1e-3ef0-8a3c-222c75111cf6 | -3.0952 | -53.726501 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98eee278-e828-381f-9f3f-f41d6346a965 | -2.7581 | -57.6717 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 084b3566-aa7b-3f5a-98f6-bc4f5012d975 | -2.9845 | -54.102001 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58dce7cc-d977-34c3-b52d-7f341be633ac | -6.1065 | -55.702801 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba3d74c4-a4be-3c19-9d00-a135bdad3e1e | -3.588 | -54.672298 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3386ab2-006e-336c-8a79-c32052d4f28f | -3.2758 | -54.0224 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53eb85b3-d6bb-3ec6-833e-c54f1ad2c3f9 | -2.9225 | -54.101299 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1804639-e56e-3533-971c-7cb50ab9fd3b | -2.9865 | -54.065201 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 083fd6f4-0411-3d0c-9c87-993f12500fbf | 3.3033 | -60.050701 | 2026-10-08 00:26:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc71a59-4601-3fc7-8348-2ba4abd9eee9 | -3.1478 | -54.094501 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 647d1922-28e5-3da4-8f3a-84f2abed1499 | -10.4389 | -47.283798 | 2026-10-08 00:26:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c60c55d-7ba7-36d6-995f-9f534ba9f33b | -3.0617 | -54.215099 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e83d5537-dd32-3dfe-8682-874bffad8393 | -11.7503 | -61.035301 | 2026-10-08 00:26:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bf82607f-4603-350c-a47e-9d02f06727f1 | -3.838 | -55.9659 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcfd5ab9-9e0b-3302-b5f3-54d6e9a21b9f | -6.2071 | -52.855301 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40221e85-3671-3528-be2c-d8ce9a80088f | -2.7777 | -54.053699 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da164e45-b359-3e10-ab0c-35758a6402cb | -5.6926 | -53.494999 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 206668b6-b6af-3642-adb9-00786bb7edb3 | -2.4753 | -56.091099 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca180b64-324f-3e9d-bdd8-05da1ca3693c | -2.7826 | -56.495602 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c98953b-feea-3c68-b7a4-2695af8e40ac | -3.1161 | -53.7733 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29807b5f-5dc6-33af-8db0-abc33fec4863 | -4.7238 | -56.150299 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903b3d28-f10f-3ce7-8eff-088d50909b68 | -2.4894 | -56.153801 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10884f91-afdd-3cd7-b648-33c877b9c3eb | -3.3099 | -54.036598 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cbe6f24-8819-3256-a6ab-6e86352432d3 | -3.2676 | -54.031502 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
