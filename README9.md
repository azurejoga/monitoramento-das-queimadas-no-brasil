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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1b33f45-5168-3be0-a488-b00b720178f9 | -11.0991 | -49.450199 | 2026-09-19 00:19:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ff92758-0746-3e70-a231-c0a1b935795a | -10.8696 | -56.166199 | 2026-09-19 00:19:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e609fe5-5806-3ba3-bba9-8e8a6aa82fa8 | -8.7678 | -46.898701 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24893e5d-ceb1-33bc-bb49-dbc71e66f793 | -10.8624 | -54.094398 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c16ffe0-313d-3cc0-96a3-6c24c7fef453 | -3.3729 | -52.7869 | 2026-09-19 00:19:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1a1eff-0146-3b41-83d8-23af8852fb1a | -4.4927 | -54.977699 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac528986-e10f-3138-b141-49835cb9458f | -8.842 | -50.450199 | 2026-09-19 00:19:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f7a6578-bdf3-335e-a17c-4099b7628572 | -5.7436 | -57.587101 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4318138-4177-355e-8b18-2e7e424c336c | -13.6162 | -46.960201 | 2026-09-19 00:19:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 471b14db-bbd1-337a-b702-1b3b90a812f0 | -7.4989 | -55.004002 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61cc1339-408e-31ae-8e21-9de5e5104f2a | -12.1323 | -46.977901 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6b8602c-e599-3c1c-9676-946e480ac042 | -11.9391 | -55.909 | 2026-09-19 00:19:00 | METOP-B | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eed6ca0c-eaaa-399d-8462-d4fc4394067e | -7.6644 | -46.1231 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f882e570-0665-3ae3-afdb-90d8266dc303 | -2.8253 | -50.468899 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7de6be-ba6e-3966-ad65-cf1104c1e18c | -4.7101 | -55.6791 | 2026-09-19 00:19:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bda28a2-cf05-344d-a4e0-3c7be972628f | -12.3481 | -48.201 | 2026-09-19 00:19:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26c8f3f4-d94a-3979-9630-674baa072858 | -3.3641 | -50.4361 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47ef2576-6a33-3488-bc2e-058c405bb32c | -3.7368 | -54.633499 | 2026-09-19 00:19:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 351accc8-a72b-3523-a000-660a7bf0e0c8 | -13.62 | -48.297699 | 2026-09-19 00:19:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dead1b57-002e-3955-8a5c-5471f8f853ef | -6.6318 | -51.248299 | 2026-09-19 00:19:00 | METOP-B | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca6dc44-928d-36ab-87e8-f8ba6ccaf198 | -8.1529 | -54.801899 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6675efb-c473-3185-b284-0831ed5701f1 | -11.2883 | -47.251202 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24fd99b2-a3c1-3a8a-aebc-f76353b417d5 | -12.7391 | -47.009102 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c98ab15f-aa9f-31fd-a7e1-9718d3ae45a7 | -11.1296 | -49.044399 | 2026-09-19 00:19:00 | METOP-B | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8f4da81-3b92-3e3b-a08f-6c8127acfc98 | -14.8174 | -48.566399 | 2026-09-19 00:19:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 836b13ae-ddad-3c40-ab06-d19d318b7c46 | -5.8296 | -47.773899 | 2026-09-19 00:19:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17df231b-8b7a-3f04-82ae-b0434af62a67 | -10.8762 | -56.198002 | 2026-09-19 00:19:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3afc9bd-2550-3a6d-a17c-bc02a094442e | -5.8638 | -52.0443 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddda0d7f-1811-3df2-adaf-46a99662075d | -9.8362 | -50.651199 | 2026-09-19 00:19:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4962f844-5c09-3314-9900-fb698be43a5b | -21.021799 | -47.256401 | 2026-09-19 00:19:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 26c483d6-3d24-329e-9765-64bd688b211c | -4.3553 | -47.7691 | 2026-09-19 00:19:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc74f91-3f5e-3784-8308-d27710c265e3 | -3.0212 | -51.191898 | 2026-09-19 00:19:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00dfe61f-b31d-3791-9fca-b71dd6992617 | -11.3001 | -47.257801 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b19862b6-87f7-38f1-9f8b-65ff629ff70e | -13.0026 | -46.944 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7708f1cf-d9db-38cc-9f48-23c485c92fc2 | -6.5675 | -44.1437 | 2026-09-19 00:19:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2463042d-4c6f-3ba0-b702-3c54e9ef93b3 | -1.1909 | -54.212601 | 2026-09-19 00:19:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fdb55a0-0657-3f66-99ae-c24716f3e4e0 | -14.8157 | -48.558899 | 2026-09-19 00:19:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aabadb16-49a1-37c0-b374-00e22f4afb4f | -12.9873 | -46.966599 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f25dbc87-5563-37c7-a172-d8d7ce81a5e0 | -11.9396 | -50.107101 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce0650b6-8031-3ec2-b8f7-50d28f29479e | -12.1291 | -47.007401 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fc61ab5-085e-37bb-98be-17911ba58296 | -6.0052 | -51.803501 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36dc3dee-af95-3360-848e-414ddaa3930e | -12.2801 | -49.156799 | 2026-09-19 00:19:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf9c6d19-f768-3d60-8d35-8dbd1c9e41b7 | -10.8848 | -54.055401 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4525b185-2bdb-329a-a4b1-9f9f0387b88e | -10.6115 | -50.251202 | 2026-09-19 00:19:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d6012e6-e0d8-3be4-8cb4-15c9b192cb72 | -13.6849 | -48.5788 | 2026-09-19 00:19:00 | METOP-B | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| af72721e-e164-352d-9830-511762bc51a1 | -10.8807 | -53.9883 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 751cc6e1-ac82-35ad-9ab2-b6b139793d8f | -14.2625 | -52.8228 | 2026-09-19 00:19:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ccacfbac-6639-33e3-84b7-c653d877f2dd | 1.2258 | -50.995998 | 2026-09-19 00:19:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4329a84d-af6b-38a8-b474-94b1f701d2e0 | -11.2999 | -46.779701 | 2026-09-19 00:19:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4b64cb9-d0f5-3f74-a093-2956b4ada0ef | -5.5528 | -48.441799 | 2026-09-19 00:19:00 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52a4f035-950a-3738-b2b0-53d6abba3fc2 | -6.6527 | -51.476799 | 2026-09-19 00:19:00 | METOP-B | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ab18453-896d-3006-a3a2-7e15afbcfb7d | -12.9796 | -46.977901 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45b0cc25-8c78-37a5-8df1-743e1095fb8e | -3.2368 | -46.944401 | 2026-09-19 00:19:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fcecf6f-d5c5-3dd3-89b2-d2222409593b | -4.426 | -55.510399 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bfd8462-143f-37eb-8b2f-2735ce97fa9d | -5.5078 | -43.798698 | 2026-09-19 00:19:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e6201d1-1ad5-32ad-9e71-ef186e99bef2 | -10.5518 | -51.313202 | 2026-09-19 00:19:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e346de28-6e59-3f8f-8613-ae12664bf1fe | -10.6098 | -50.244202 | 2026-09-19 00:19:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae501df8-4c98-33c8-b8c0-c9abe338dc77 | -4.5008 | -54.967999 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc9830fa-df78-3b74-b82b-eee06b373bf4 | -4.5708 | -54.912601 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5955896f-1f4e-30ba-ad6c-36b394403aca | -10.8866 | -54.063599 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8175ee0-8723-33cb-91e9-362fb9597620 | -14.6868 | -46.636902 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b7018437-91dd-3953-87b8-9d4f6e550dbd | -14.8577 | -47.140202 | 2026-09-19 00:19:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 82ab41ff-2ce0-343d-9206-984f8530c6c5 | -8.0149 | -49.051201 | 2026-09-19 00:19:00 | METOP-B | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 010a56f4-f7f3-382c-98a6-395f40c49716 | -12.6062 | -50.873901 | 2026-09-19 00:19:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 586a891d-0458-3f70-92ba-48802db2318a | -11.3546 | -44.126499 | 2026-09-19 00:19:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21e3ab07-e368-36f6-af28-5f3b608686c2 | -14.1672 | -48.7463 | 2026-09-19 00:19:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c36d767c-3bce-3b3e-98af-98891743fde3 | -12.9894 | -46.975498 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 638590f7-9826-3b63-bacf-f24636f3ae30 | -8.6118 | -54.599701 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b08b0f0d-7932-3166-b656-a115044dbe96 | -3.5167 | -50.788502 | 2026-09-19 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70676c94-aee3-32e7-8816-4639cf12f895 | -12.1366 | -46.995998 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6298ebae-67dc-3c4f-a0bd-ac3604404a90 | -13.3023 | -51.2761 | 2026-09-19 00:19:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e68533a6-7513-33f9-94a1-e17c64e29b6a | -10.2758 | -49.999901 | 2026-09-19 00:19:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4216d494-f7bc-36bb-b6ce-c239729825fd | 1.2563 | -50.9524 | 2026-09-19 00:19:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6bbf7df5-bbd5-3903-90cf-d8ad7e11b28d | -13.6832 | -48.571301 | 2026-09-19 00:19:00 | METOP-B | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 81f1e844-3f9b-3f99-bf88-251e3cbac5b2 | -12.1497 | -46.964001 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53972b5c-f39b-3596-9027-4035245f9abd | -3.7351 | -54.626202 | 2026-09-19 00:19:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1698a655-4ece-3923-bae6-7481dde9f03b | -7.6324 | -46.118599 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88fcec3b-0994-302d-a149-298619b1a5fb | -8.4867 | -57.608299 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e1e15e1-f71f-32c2-8938-59cfb208907d | -10.5843 | -46.595001 | 2026-09-19 00:19:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8bf76434-572d-3530-8d36-73289261b3bd | -6.0103 | -51.780701 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0de68c8-b138-3973-94d0-a3d5f690a6fc | -13.3007 | -51.269001 | 2026-09-19 00:19:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99fbb3e0-b558-3508-87aa-0adead7e1d73 | -2.9034 | -54.177799 | 2026-09-19 00:19:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e7b4b3e-00df-3ee4-82b0-3d5ffb33eb0e | -13.6176 | -46.922699 | 2026-09-19 00:19:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 89d61a8a-6292-3763-965b-a3356e0d9dc9 | -4.2769 | -48.582802 | 2026-09-19 00:19:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f9a2987-1fe7-3645-aa99-005055fcd90d | -9.9581 | -46.610199 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62f322aa-fb63-3bec-86ea-e55c45efc5de | -4.451 | -55.5303 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fc0be56-4ea4-3471-9cb2-a75a66676a8c | -11.0798 | -50.681599 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 93980733-47be-310b-8b1f-bdd8dff07ee5 | 1.2545 | -50.9604 | 2026-09-19 00:19:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff9c098-964a-3ae0-893c-e1452cab2f97 | -11.6736 | -54.439098 | 2026-09-19 00:19:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6515c3a6-ff4f-3e36-bfb1-7c2a229c8526 | -6.6368 | -52.962601 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b1e2c85-3bed-368b-aa55-eb7aab03ad58 | -11.0738 | -48.270599 | 2026-09-19 00:19:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa28a612-7ef4-3f26-b594-37057e5dc019 | -9.9557 | -46.600101 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48495322-bd84-369e-b0cd-fae95193d12e | -11.117 | -45.297298 | 2026-09-19 00:19:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a93b2269-8398-3d51-b624-dad34082138a | -5.2481 | -49.3946 | 2026-09-19 00:19:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 192484d7-a53a-3bf3-996c-654d991e65f5 | -10.8173 | -50.159 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10958d8e-d66d-3199-acb4-c805ce7daa5a | -7.8533 | -44.859001 | 2026-09-19 00:19:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6dce6f04-1d3a-3c6e-8b60-c52c1940a357 | -7.0027 | -49.758999 | 2026-09-19 00:19:00 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dece2e9-c1e5-3239-8628-fd5375d9bad2 | -7.3591 | -50.323299 | 2026-09-19 00:19:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c426312-9f8f-3658-a776-eb10cdcdea26 | -4.1427 | -48.226799 | 2026-09-19 00:19:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28e7a585-4743-3b3c-9a94-93a7e394ddf4 | -6.1981 | -45.3358 | 2026-09-19 00:19:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
