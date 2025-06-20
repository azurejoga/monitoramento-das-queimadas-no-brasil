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
| d8f4aa90-e2b4-36e4-8482-ab0fa8dcaf06 | -18.22081 | -45.05225 | 2025-06-20 04:02:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed382951-f77c-3d77-983c-74e80fb5d70b | -15.42603 | -47.83546 | 2025-06-20 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db145d56-7f99-3711-a415-ce1d3bab323a | -14.03066 | -55.1236 | 2025-06-20 04:02:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d392bbd-70c3-357a-bed3-2f5edc60b7c8 | -10.59356 | -49.4643 | 2025-06-20 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e88e1ef2-a23a-3b57-be76-952490c98cc6 | -11.47172 | -47.28778 | 2025-06-20 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5e540c6-08c7-3598-8505-219935743d65 | -14.62484 | -48.11579 | 2025-06-20 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aec53e1e-ec2e-3c50-b12f-95c0c6f76d87 | -12.2001 | -49.6231 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e726bc38-10d2-3b37-80b2-c17f3470d0f0 | -15.40484 | -47.80924 | 2025-06-20 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f078936-942c-33a5-afa8-f330d2a64ca5 | -11.1483 | -46.65572 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 425a1576-1d07-387f-b8b3-3993a36cf7a9 | -12.19623 | -49.61631 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1894f3f-9ae8-356b-88fb-1ac751b13ce6 | -12.34326 | -49.30556 | 2025-06-20 04:02:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7df30371-b965-31b1-9841-0e58cb2b4c06 | -10.49167 | -47.0265 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed55c573-ae4c-31e0-8f8c-8047d5b185b3 | -14.02391 | -55.12215 | 2025-06-20 04:02:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01422138-1faf-3eb5-a84b-000df7bebd0d | -10.65946 | -49.3624 | 2025-06-20 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08479698-bdf6-3542-9ed3-322cd0aacf5e | -10.48439 | -47.0423 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac3b370c-6e92-384d-a62d-25b2c9421133 | -12.20892 | -45.52946 | 2025-06-20 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2da64435-02a2-341a-8ea8-1161a6045639 | -10.73231 | -49.55568 | 2025-06-20 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f8c60f2-0801-3fce-9055-1f0d18868876 | -11.96309 | -53.50026 | 2025-06-20 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1f8490c-1f4f-3fc0-a660-607c95409633 | -10.47073 | -47.04396 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f4a53f6b-3985-3842-96bc-b9fb8c617b91 | -10.4801 | -47.04142 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bcb7c7f7-d5d6-3031-8561-38de8ba8bc4c | -11.45654 | -47.29795 | 2025-06-20 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb478f35-f713-37b6-a2c1-2190b7b37394 | -10.42942 | -47.11771 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5732786-d3a3-3af0-a776-f7c93682a8fe | -11.32034 | -45.20378 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 786fbc08-87e6-3047-a269-3908d4fd9419 | -11.15515 | -46.64108 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2964d3d0-8be6-3afd-951a-25294b26b104 | -11.90855 | -44.06943 | 2025-06-20 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 940b155d-0fbb-3273-a56f-e2d02a4979b9 | -10.47428 | -47.049 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| db6547e6-4384-3039-a5f8-3ea8e7a6fd43 | -12.75858 | -44.41039 | 2025-06-20 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2cd1fa8-996f-3433-bb39-c52f765c7e6c | -12.26888 | -44.60428 | 2025-06-20 04:02:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ca5933f-95ce-3536-a734-a0bf9eaf0342 | -15.39985 | -47.81295 | 2025-06-20 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2a2e1d3-2b31-3ad7-aed4-81d03ef74928 | -14.43776 | -48.90281 | 2025-06-20 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e21c1bc7-f919-39a2-8097-f639e59ec781 | -17.78216 | -42.80795 | 2025-06-20 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 40c4e21b-95ad-37db-99cf-6941b9a34f25 | -12.76378 | -44.41415 | 2025-06-20 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cee430eb-0663-3874-a84f-22173bd8a6d6 | -14.42963 | -48.92108 | 2025-06-20 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e7ceeaf4-270a-3974-aede-3288743c8cd3 | -10.69097 | -46.88751 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b0c2a6a-1a4d-3b3a-8498-c2fc0ac31222 | -12.75501 | -44.40976 | 2025-06-20 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| be1a3e6f-3b36-3831-b0f6-ecd7bbf5bb05 | -11.46086 | -47.29876 | 2025-06-20 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f856802-4513-362b-8fc6-40fe05944244 | -10.46412 | -47.05587 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 5ddef16a-f8e6-3f15-8542-b621508cae37 | -10.52849 | -46.64695 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24a590b5-147f-34b3-b6a7-f8efcc697a21 | -11.77528 | -54.37152 | 2025-06-20 04:02:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6f51a17-17a3-3129-8495-4367dec974b6 | -10.53858 | -46.93706 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dbb0f1e0-10fe-3557-8b70-d8b304ca6093 | -13.77634 | -54.20244 | 2025-06-20 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e6133ca9-2921-365a-9d31-d4be2766e6fa | -10.49671 | -47.02324 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2c77655-82ca-30f2-8903-5591221b859c | -11.80072 | -43.78151 | 2025-06-20 04:02:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd7cfc40-07f9-39de-979d-9215a147e7ba | -12.21954 | -45.53632 | 2025-06-20 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19020b54-6030-3c67-9945-a32b3c9e5d3d | -17.66489 | -46.6799 | 2025-06-20 04:02:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe1b16a9-1db7-3d2e-be47-353b3fbe767a | -11.98345 | -51.61112 | 2025-06-20 04:02:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24ed3ecf-e3ed-3f35-a614-1721622585c3 | -13.24833 | -46.8136 | 2025-06-20 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d67abe1d-77aa-3193-923d-a47d66ccae53 | -11.56858 | -47.43068 | 2025-06-20 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f63c0df-f46a-3bdf-a3db-1bb662021c3e | -12.26598 | -44.59932 | 2025-06-20 04:02:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3a08e8a3-8936-3d3a-bb47-3d8476811730 | -10.95043 | -48.14638 | 2025-06-20 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9003ff41-533b-39f4-a38c-2ed8d0a7d580 | -10.46335 | -47.06017 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 2c184ea5-24b0-3773-9a5b-b4255d316f54 | -14.56538 | -42.94426 | 2025-06-20 04:02:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 712fd59b-1e78-3290-a121-9a1cf28d2fe1 | -11.31744 | -45.20197 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ac946046-f651-3766-a5ce-1b7f47db0a3a | -12.22036 | -45.53152 | 2025-06-20 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18338de6-2604-3cbd-b532-833532f9a232 | -10.59557 | -46.92897 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bdee062-8955-3924-9693-9e388956309e | -10.5343 | -46.93627 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 24e98920-0667-341e-9e87-1ad76c5cce8a | -17.48998 | -46.87343 | 2025-06-20 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fa302f2-8a53-3e11-948a-88c2e25e43ea | -11.13445 | -46.66122 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1da07004-7c33-3a5d-b732-7d7bae5ca4a6 | -11.90002 | -51.76491 | 2025-06-20 04:02:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e823b672-f6b7-3cdb-9f1c-24067d4be42a | -17.2168 | -44.80317 | 2025-06-20 04:02:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b283537-b9b5-3a72-8d5f-89a5a8e8932f | -11.81249 | -54.50483 | 2025-06-20 04:02:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1c703f2-b44c-3403-b184-f02f542a032c | -11.14345 | -46.6589 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d89dd4e0-f56f-3a03-af3e-891bf939864c | -12.21273 | -45.53014 | 2025-06-20 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1305a944-27ba-37b5-83f5-9facdcc3a085 | -10.73064 | -49.56474 | 2025-06-20 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8901716f-b7d1-3171-9411-305fa8e059b5 | -12.76215 | -44.41102 | 2025-06-20 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbe3ddaf-68dd-3ac8-b67f-4bae77d1d23d | -12.75736 | -44.40874 | 2025-06-20 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5eaffde9-aa2b-3088-8328-80e863a3d35c | -12.39513 | -46.36217 | 2025-06-20 04:02:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75817c12-e9d7-3d9a-b508-fea9cd4d1280 | -16.42642 | -44.51432 | 2025-06-20 04:02:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 176fd738-ac27-3765-bab4-df94806248f4 | -10.66394 | -49.36634 | 2025-06-20 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 762f4af5-b36f-360a-9506-07a7c9b2a246 | -14.47511 | -50.29094 | 2025-06-20 04:02:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb1399f2-155c-3c6e-a909-769408e8a3ac | -11.14898 | -46.65184 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1dc1bf5-9218-388c-8060-8e6e018d9129 | -13.23934 | -48.41521 | 2025-06-20 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 477640b8-7b98-320e-9d79-877f5446a672 | -11.76862 | -54.36985 | 2025-06-20 04:02:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e55e9a7-ca38-34e2-acda-4bfba2ccee18 | -11.90086 | -51.76065 | 2025-06-20 04:02:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 591f4209-b294-3dd4-97cc-ccef7774c03b | -11.9861 | -51.60746 | 2025-06-20 04:02:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8de3a5c-b432-32ee-b2b6-a97e8838cf21 | -12.21573 | -45.53562 | 2025-06-20 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a713fbbb-3dde-3b6e-9cfa-d7ff19325ab9 | -11.9331 | -48.42146 | 2025-06-20 04:02:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 273bfb57-2714-37f3-a203-287f09c6d3eb | -10.48085 | -47.03722 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 472e80c9-5d33-39c2-9af6-03feefc0dec7 | -11.31666 | -45.20661 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce8d2475-6f7a-35e4-a0fc-dd2486dc2018 | -10.4989 | -47.01091 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bbd09d6-7af0-30c4-bd55-54b960e3b293 | -11.31355 | -45.19788 | 2025-06-20 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 540e44d0-d8cc-3a0a-8ccd-75dcaa55a2bd | -11.13916 | -46.63437 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 657721af-19bb-34e3-aa87-cff85cdb1ca5 | -10.72667 | -49.55772 | 2025-06-20 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e5f4b96-380a-3cb2-9349-4fe47da8adb8 | -12.647 | -54.12484 | 2025-06-20 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fabb83b1-2b3a-36b5-92a6-0140e3273c78 | -13.39238 | -48.4524 | 2025-06-20 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06f98104-f272-3b0e-a482-8aff4a1f00b0 | -10.49597 | -47.02737 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c517d12b-3e9b-3c9e-ba57-9b9cd24824b4 | -11.27424 | -46.65535 | 2025-06-20 04:02:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd9133cd-5ff6-3e16-918a-9731b1d797fa | -11.1664 | -47.40338 | 2025-06-20 04:02:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09d82f7d-943e-3627-8e66-8b5a1dc30735 | -11.92846 | -47.8496 | 2025-06-20 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c8b16b9-3e6b-31ff-ad47-0b803f2caf0c | -13.09697 | -52.29703 | 2025-06-20 04:02:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ad243344-1fd9-3399-b910-e2633c116854 | -11.14401 | -46.63118 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5e575d4-d974-3b9a-ae50-60a0f003b2a6 | -11.80115 | -48.09078 | 2025-06-20 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 893ca456-6824-3982-9d53-cd882579601a | -10.86202 | -53.75769 | 2025-06-20 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f21c524-a7b4-3fd0-8729-515287c26493 | -10.51941 | -46.64934 | 2025-06-20 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5909c2be-9118-34cd-9d39-87f3cac7286b | -11.47024 | -47.29619 | 2025-06-20 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaf5b527-a13f-31a0-85c6-57f5a3e32c13 | -11.93475 | -48.41897 | 2025-06-20 04:02:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 065ded88-36f7-3b4b-a368-7859f6bc52d3 | -10.59469 | -49.4583 | 2025-06-20 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eec644a0-daaf-3316-a77d-f3e933443dd8 | -11.47529 | -47.29281 | 2025-06-20 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98a49cc2-d121-3e28-a417-8f087861ab64 | -17.57355 | -47.49907 | 2025-06-20 04:02:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 704d4230-4f03-38f7-98b2-c05a12278700 | -12.2638 | -44.61225 | 2025-06-20 04:02:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
