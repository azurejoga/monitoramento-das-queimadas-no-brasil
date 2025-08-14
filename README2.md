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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37673001-294b-34a9-a86a-10656d48588e | -6.0807 | -59.9465 | 2025-08-14 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.7 |
| f2c4e070-4697-30bc-b0a1-ed2219910edb | -17.0432 | -51.8016 | 2025-08-14 00:30:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 42.7 |
| a8fc2ba0-e09e-3a5c-9979-fd4836e9b435 | -9.152 | -59.6772 | 2025-08-14 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a7bf8042-320f-34bf-a552-504b5b328b3c | -8.1028 | -61.2069 | 2025-08-14 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| c4881aec-51a5-38f2-9807-9698fdbda1f1 | -6.0991 | -59.9459 | 2025-08-14 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 2ca17f76-828b-3a28-90be-2d236a48dc5d | -22.6774 | -47.4407 | 2025-08-14 00:40:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 47.5 |
| dd74e47a-2897-3e74-80bb-9d77e7e05429 | -22.6767 | -47.4647 | 2025-08-14 00:40:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 192a5212-3e63-38eb-aef9-291eb30c4101 | -6.9422 | -44.5562 | 2025-08-14 00:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| b3abcd89-0987-3274-b893-dbfcce8339ac | -22.302 | -49.5486 | 2025-08-14 00:40:00 | GOES-19 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.5 |
| 8e15b119-c866-3e0f-b977-ce327b43656a | -8.5208 | -43.3298 | 2025-08-14 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 16e0e27f-1c4d-3c0c-9e75-8c1829f5e2c1 | -7.6287 | -63.5154 | 2025-08-14 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 46afeb11-a2f3-3b13-9abb-476bd47704a3 | -6.2655 | -53.6817 | 2025-08-14 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| af3d74b4-9b13-3512-b991-d86969a4b89e | -8.5211 | -43.3063 | 2025-08-14 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 7f9eb434-dcf6-3aab-aad5-49fed9143563 | -7.8774 | -61.8253 | 2025-08-14 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 9a561a6c-8496-32b0-99c7-a56ca74019dc | -7.8775 | -61.8063 | 2025-08-14 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 70d9a361-3d25-3009-86b7-46df6ef9e979 | -6.0807 | -59.9465 | 2025-08-14 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 69a8327f-02a9-34d7-a67f-da12fd9f5cb0 | -9.4994 | -60.5278 | 2025-08-14 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 3894204e-35b2-3858-906a-ba20c1d2dbe4 | -5.9899 | -44.1528 | 2025-08-14 00:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 06400463-0086-39ec-9968-5107677b38dd | -9.152 | -59.6772 | 2025-08-14 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| c3ac5072-4c12-3af1-b23e-8f6cdbbfcc69 | -7.6103 | -63.516 | 2025-08-14 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 5419ef79-b9fe-3130-881c-91b67322bddd | -6.0992 | -59.9267 | 2025-08-14 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| a85b95dc-513e-33e0-8490-7ee752823351 | -9.1522 | -59.6578 | 2025-08-14 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 09e8e837-9932-3baf-91a2-d8ce004ce617 | -9.1336 | -59.6588 | 2025-08-14 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e1c0160d-daa5-3f1c-9505-b1f1b9794629 | -7.5918 | -63.5166 | 2025-08-14 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| f747bebd-60a9-3c97-a40f-77e3e7917f44 | -8.7484 | -44.019299 | 2025-08-14 00:41:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 09dc3e3f-5252-3256-9dd8-d0e1f7821239 | -6.1937 | -43.310699 | 2025-08-14 00:41:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aee4d624-1bb7-3962-a83f-4ebe001e34fb | -12.3529 | -49.913399 | 2025-08-14 00:41:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3abbcdc-57e3-36cb-a4f4-d295a29785d7 | -20.3514 | -45.9869 | 2025-08-14 00:41:00 | METOP-C | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8292db58-9369-3336-9b0a-014473ee51a2 | -8.5289 | -43.320301 | 2025-08-14 00:41:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a9076240-1e2d-345d-856a-9f4fdfef9469 | -19.2556 | -44.169102 | 2025-08-14 00:41:00 | METOP-C | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6f3074d9-988e-3705-9924-fc05f96e2450 | -6.9074 | -59.124199 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66588c9d-f803-3f01-9d25-519c4bc580c6 | -6.8839 | -59.156399 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0cdfe27-b315-36e6-b8cf-dfb7006f494d | -14.3263 | -48.6408 | 2025-08-14 00:41:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e1433082-aaaa-37aa-8081-f80b265ce6dc | -6.8827 | -59.1021 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75f7ed87-fa16-33fb-b3e1-723c005d3cd2 | -12.3512 | -49.9053 | 2025-08-14 00:41:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c63f694-a5d7-3801-8448-8c3c1192ce79 | -10.9719 | -49.561699 | 2025-08-14 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a948a738-ce8b-36f8-8087-ec6d45b8e719 | -16.683399 | -49.457001 | 2025-08-14 00:41:00 | METOP-C | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45962b6e-d825-3dba-9fa3-0b9a377b7e34 | -6.6168 | -43.870998 | 2025-08-14 00:41:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eba29725-4faf-3fe1-ac17-6b662deb5b2d | -9.1452 | -59.653099 | 2025-08-14 00:41:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 374b77f8-4bc1-3c93-9635-86216b091650 | -3.4371 | -49.0396 | 2025-08-14 00:41:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6deb67-fce9-3758-881a-8fb1773ee660 | -19.0847 | -48.150002 | 2025-08-14 00:41:00 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fd9011c5-4357-3f5b-acab-05af3ae065d3 | -9.0524 | -45.081501 | 2025-08-14 00:41:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9aeb0787-7977-3af0-8ff6-d6b6128a3650 | -12.5825 | -46.9501 | 2025-08-14 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64cd61a5-0b5c-396e-a346-f3b6cb15b0d2 | -12.3265 | -46.055599 | 2025-08-14 00:41:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 62ccd01c-a6ea-3f8c-94b9-12d069a15a2c | -12.5742 | -46.959301 | 2025-08-14 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06e91757-ee32-3419-8787-ff43ee7d9b79 | -8.7463 | -44.0103 | 2025-08-14 00:41:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c12d76a2-5809-3c3c-8ef2-bd262fad13be | -18.5338 | -46.053101 | 2025-08-14 00:41:00 | METOP-C | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5c4a00d6-c8ab-3a51-a720-73996b41b500 | -6.184 | -43.313 | 2025-08-14 00:41:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b54f3ec-f6ca-3b2f-9dd4-74923a9f117c | -6.6094 | -43.883202 | 2025-08-14 00:41:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d458a105-d80f-3e88-85ff-af0da8d7cff5 | -19.8909 | -44.601898 | 2025-08-14 00:41:00 | METOP-C | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f3fe2b83-3a27-3e4b-9dac-ec8e3c400656 | -6.8881 | -59.128201 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81c5a6cd-9fba-3c93-a71c-a34e54ec6cb8 | -20.005899 | -42.204102 | 2025-08-14 00:41:00 | METOP-C | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dfa8130e-d6bc-3ab9-b6a2-b4b2f0986b79 | -8.7408 | -44.030701 | 2025-08-14 00:41:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 32648568-4716-30a0-9c01-1437b0af1039 | -6.1814 | -43.3022 | 2025-08-14 00:41:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60dac8b1-5a02-3bae-a41e-49749e89f1c9 | -5.8849 | -57.733101 | 2025-08-14 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 387972b3-baa6-399c-8799-5b5b7330ec53 | -9.1294 | -59.624298 | 2025-08-14 00:41:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| deee8c92-ed32-3209-a45d-1c0dd360dde0 | -22.6693 | -47.4594 | 2025-08-14 00:41:00 | METOP-C | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 244a12e8-9c66-34fd-9bd4-a3ae5f701298 | -8.5167 | -43.312698 | 2025-08-14 00:41:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9819bf5d-ec04-3b99-a33d-5662932466cf | -12.584 | -46.9571 | 2025-08-14 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 861eca36-7371-38da-b88f-7ef701c48f43 | -8.524 | -43.3004 | 2025-08-14 00:41:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 67d31d0a-0733-3388-af93-54f1d38c4d47 | -5.7928 | -43.617802 | 2025-08-14 00:41:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db547652-a6b5-3f8c-b767-a707feb0f31b | -22.5588 | -47.317501 | 2025-08-14 00:41:00 | METOP-C | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d69fc9a6-421f-3338-b439-c67aa907861b | -15.5517 | -43.150398 | 2025-08-14 00:41:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| a8fda0f4-7308-3f5a-a2ad-df31bcd0545d | -22.311399 | -49.5457 | 2025-08-14 00:41:00 | METOP-C | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35b527cd-3f2f-37ca-8b91-e30e2cfe5ab4 | -19.253901 | -44.161701 | 2025-08-14 00:41:00 | METOP-C | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8a619e3c-0d60-3ddf-a3a7-8c2bae63063e | -18.545099 | -46.057999 | 2025-08-14 00:41:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 091ea0a3-2abb-3956-8dcc-efc1f0238ef1 | -9.7729 | -48.749802 | 2025-08-14 00:41:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e74d4c19-f53c-385b-a65d-849e3118ab1d | -15.5497 | -43.141899 | 2025-08-14 00:41:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| d233fa49-f575-30da-a79e-cb5f02a21a13 | -6.873 | -59.104 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9c03c1d-bc82-3eed-a0ba-6d65f7e6cd13 | -5.1529 | -39.504799 | 2025-08-14 00:41:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 193c15d0-d73f-363a-a6b2-066c5e221655 | -16.6852 | -49.465698 | 2025-08-14 00:41:00 | METOP-C | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6fec11ad-ebc6-387c-8e4d-149efc66453b | -22.600599 | -46.718899 | 2025-08-14 00:41:00 | METOP-C | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5236b05d-e791-3a1d-9053-96ffc98863fe | -6.6191 | -43.880798 | 2025-08-14 00:41:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05019aa7-43df-3922-975a-2e765e21987d | -18.2491 | -47.252102 | 2025-08-14 00:41:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 69730203-7e56-3fc9-a86a-ea68ff1a6827 | -22.560499 | -47.325901 | 2025-08-14 00:41:00 | METOP-C | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 75d04efd-f122-3e7e-9d01-f54b6bc54b9c | -8.5313 | -43.330299 | 2025-08-14 00:41:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3357dd2-4e3f-3219-979e-a2fa0098b4c0 | -7.9439 | -46.834499 | 2025-08-14 00:41:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5477793a-0752-34c9-ae09-551056d7aaa3 | -6.5392 | -56.187801 | 2025-08-14 00:41:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef5216e3-c8a3-369d-af19-23e7137fd9ee | -6.9032 | -59.152401 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c51d782-ca57-3c3e-8427-4dda8f8fed9e | -6.9559 | -44.557999 | 2025-08-14 00:41:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5bca6d4-c30f-3fb0-b506-be4206780702 | -6.8936 | -59.1544 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 488f2cd7-1cac-3051-85a1-2480da4fd97c | -14.4833 | -46.054901 | 2025-08-14 00:41:00 | METOP-C | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4f01d93c-2855-36c9-b34a-9558461c1885 | -6.2726 | -53.687199 | 2025-08-14 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b542ab6e-bac3-3467-8b53-9d773c39b665 | -9.0543 | -45.0895 | 2025-08-14 00:41:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 16c3f746-945c-3a3b-8ac9-bad138b39c11 | -4.2241 | -47.216702 | 2025-08-14 00:41:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37fa19b5-a59a-3355-8733-8cb8f6e120c5 | -8.7365 | -44.012699 | 2025-08-14 00:41:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9f76ff69-387b-3786-813e-a8c1dec976a8 | -3.4386 | -49.046398 | 2025-08-14 00:41:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06c349e9-5a40-3702-8c0f-2abcf4442556 | -12.3249 | -46.0485 | 2025-08-14 00:41:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 000145e0-53ec-3576-b5a8-8f0622feea56 | -6.9171 | -59.122299 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dfc4f7aa-46ec-32df-8e2c-0fc96ab00d9f | -6.0815 | -59.892899 | 2025-08-14 00:41:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdd0be91-19b8-3302-b956-efb3ce78b54f | -17.6145 | -46.695702 | 2025-08-14 00:41:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8434bb0c-e57f-33ed-b771-2ea0f4597bce | -15.5802 | -47.319599 | 2025-08-14 00:41:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e099fdc5-94c2-35aa-88f4-5699dfc44f06 | -9.1391 | -59.622398 | 2025-08-14 00:41:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70dc400c-cc73-3240-bcb1-fdf6a658daac | -7.1158 | -59.593498 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef273879-2525-36fb-adc7-612688a20c88 | -6.9129 | -59.150398 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0894a376-2cbb-3c71-a708-53567e147066 | -6.8687 | -59.132099 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 231be2e0-bf1e-3da5-9703-88a30ebbe185 | -5.9825 | -44.153801 | 2025-08-14 00:41:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fbb02ad-39df-3497-9e95-df61e37952c7 | -9.7745 | -48.756901 | 2025-08-14 00:41:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d134f0c-7132-390c-b9d5-dba936ec7c02 | -18.542 | -46.043499 | 2025-08-14 00:41:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 30570af9-382c-36f8-aedc-fa2354c857d6 | -13.8862 | -45.5658 | 2025-08-14 00:41:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
