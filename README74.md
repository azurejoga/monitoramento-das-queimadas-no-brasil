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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 619bec75-c416-3d99-8a61-d464b442fb58 | -14.7948 | -42.83035 | 2025-10-01 04:21:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 742e3829-6cbb-3960-8ab8-b6c722242635 | -16.02017 | -50.9045 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cac4a034-5e91-37b0-a714-aee20969ed36 | -13.58778 | -48.03999 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2c773569-c1e1-332c-bf70-e996d4ea0428 | -12.22374 | -43.75182 | 2025-10-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e291af6-033c-3952-a0af-44b735c3c083 | -13.94479 | -48.11093 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c30ca22-d7f3-31f4-bc2c-705228683327 | -11.82641 | -44.9719 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 050a008f-1b31-323e-942b-2d7cb5a29bf7 | -16.37839 | -47.07287 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 37315bf1-9e81-314a-8ecd-71f12c184f12 | -11.83808 | -44.9847 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7227fca0-5a6e-3da3-a61c-c9d18846462c | -14.91818 | -47.81964 | 2025-10-01 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1042c464-6ea9-31dc-ae57-c20f762e5201 | -12.40114 | -51.07461 | 2025-10-01 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4193009-8b1e-3300-a719-6e1d4299bbf6 | -13.35961 | -48.1436 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f766915-9e42-3283-b7e9-9f5b6e87cc7a | -11.6907 | -45.3461 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3fb46c4-67ec-36c6-9818-e99ea43bf3aa | -11.84697 | -44.99344 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bf732fb2-124c-35f9-b1ee-4f2205cfee50 | -13.04044 | -47.08862 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cdc7cfb-9a8a-36ae-800f-4733f0030259 | -15.62681 | -49.17162 | 2025-10-01 04:21:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e924b798-da78-32b1-86db-be3c6cda5dd1 | -11.9507 | -47.06896 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 708201e4-ae6d-3efe-852c-34e214d0eb68 | -11.84424 | -45.01121 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82909493-5538-322f-9d16-02c0173f8cb0 | -15.39174 | -49.18804 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c4ecad8-39b3-303e-8529-a58177166419 | -14.90446 | -51.67615 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2aa122c0-d94b-36ac-bbdc-52c48451f92a | -10.91125 | -44.32799 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a6276e0-9138-3b27-b6c5-4fdd7722f99b | -13.97811 | -45.05603 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fee205c2-0ea3-3a62-848e-135e79c0c252 | -11.92271 | -47.89739 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ce8a9e38-29e6-3fbb-9076-de73cd41f564 | -14.7226 | -48.14735 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdd99fbd-ba59-30fb-ae19-7601e5cea2be | -12.90933 | -43.46852 | 2025-10-01 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3dcb428c-fe81-3a30-9e3a-84916948b9ec | -15.3387 | -47.9359 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aeb4e201-0129-3e74-8e6d-fe0edc571b64 | -13.21239 | -47.33359 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11f156ca-7313-3852-9df6-e7edefaa3096 | -12.13473 | -42.87595 | 2025-10-01 04:21:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0d3691c7-dd01-3f0e-b980-e9a9fd14f98b | -13.36763 | -48.09492 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55fd7a6b-2da1-3fe1-ad94-d6ae6f5907a4 | -14.9068 | -51.67951 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 39e89823-2bf8-36db-bda4-d2d80085acf2 | -10.17824 | -44.90048 | 2025-10-01 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f656ec3-bcc4-314f-9652-749747af9ae0 | -14.0591 | -44.36938 | 2025-10-01 04:21:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d8a4980-afa5-38b0-9d8e-cf87cd2a7964 | -13.37377 | -47.32383 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7817e6a-a1e9-3dfb-a8bf-bcc39ed25624 | -10.9059 | -46.55468 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 51b29247-c9c9-3ef2-afae-633794a9e281 | -16.49747 | -43.72933 | 2025-10-01 04:21:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0279598e-59b5-3d21-a597-b8146d98ecf5 | -14.90057 | -48.37178 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d104a66-9e7e-3c17-a599-22cde53b3282 | -14.5527 | -48.24465 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 273da771-c039-30d1-bbd8-fe994d83ca3d | -14.97908 | -50.77961 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 464c9866-763d-3f52-9ac1-81a29c666a6b | -12.79451 | -46.90179 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c9398df-c008-3f14-9323-136b180b229c | -13.21974 | -50.90051 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 680c3d53-9275-3bb3-bc0f-d20c9413dd39 | -12.95514 | -46.42172 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cbabb603-c2be-3983-8447-cb4d160bf24b | -15.48744 | -45.90517 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ac7ec239-f007-3459-a511-08c8e54450e5 | -11.84256 | -44.99999 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa8eb767-4787-39d8-aa38-020680832508 | -12.66114 | -46.88313 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b47a64d4-2ad8-367e-a6cb-7eeea57e5fdc | -13.37181 | -47.29375 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d462219-fc60-3d05-939f-1073bdaa5ba1 | -10.80216 | -45.35153 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4ef2450-f2c2-3362-bf2c-90f417fd931c | -11.19656 | -47.75765 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24efa5c2-c524-3934-98a9-7ae37aa8d4b4 | -10.17162 | -44.89942 | 2025-10-01 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea44fc67-055e-3fd5-8c48-c37ead5306a4 | -15.13153 | -46.45309 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2889d851-47a1-3048-80fb-057b5b1df9ea | -10.89364 | -53.75846 | 2025-10-01 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ce8b66c8-0b46-333e-b123-8445fd7cd70b | -13.32951 | -47.85188 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0839bcf9-0c00-3c40-ab86-3eee40f19e0c | -11.81648 | -44.99227 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36276104-1b54-3c81-931a-df7ba36d552c | -13.06754 | -47.08944 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28516192-d10d-3c22-a24d-2814f6327869 | -14.37118 | -47.13485 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40638700-73a4-3eaa-a2f9-55dd32185fef | -12.87211 | -46.7766 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 398d52cb-1605-380e-8891-70b39c18cfb7 | -14.87811 | -48.3182 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cb88d1c-4149-3505-aa9b-61eedbc2fb19 | -16.28395 | -47.8405 | 2025-10-01 04:21:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee471c49-e792-378e-98af-3d34af930a88 | -10.47955 | -47.58352 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d043ec0-553f-32e2-8eeb-0b9707469c40 | -14.66326 | -48.12996 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cde78c3-0727-352f-b462-397a52daee4a | -11.94565 | -47.07914 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11ef9ebb-59cc-30c7-95b2-c5445a260656 | -14.49912 | -48.44302 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| da0a1add-5c80-3b98-879f-bb5123a75f5d | -17.4152 | -45.46048 | 2025-10-01 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 111f571a-324e-3502-80e8-d97392845388 | -13.81604 | -47.49656 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c331ad81-f832-30c0-b03f-d3258e01cd91 | -14.35697 | -47.13639 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| abd8a75e-b6fa-334b-ae5e-fca598361a37 | -13.98564 | -44.91368 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 25d31e51-7221-3458-98f8-917351f573b6 | -14.76691 | -45.74939 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae294d5a-c341-3b32-a800-e70f482efe5e | -14.44133 | -46.36208 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08ec1a97-c354-35b2-a0f6-1ea1752e85bf | -17.38939 | -47.13224 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 393ffc3a-348b-3afb-a478-51b24fdcd016 | -14.60137 | -48.22251 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e736be6-03c0-318a-9874-da95e9e88ee7 | -16.83076 | -48.85035 | 2025-10-01 04:21:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 690c2934-ce1d-3c03-8c6d-8bf10ed4b7cc | -11.59157 | -45.04033 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 97c4a8f0-5a7e-3a8e-928d-51e0e4e152e0 | -14.02113 | -44.97617 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a3d0749-dff9-30b0-b110-6e60c86b4e35 | -10.80162 | -45.35502 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f85716a-425e-3d30-98e1-186dee551ed0 | -16.0886 | -51.02739 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dd282b9-7178-3ee8-b56f-be2163605954 | -12.86617 | -46.9426 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad6379d6-5459-331e-a85d-c2c609e659e8 | -13.16984 | -47.3856 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cedaa1f7-78c7-3a7e-9b1f-9d490f41067f | -15.76156 | -43.68507 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19799d2d-219b-3967-a674-22fd93d5788d | -13.3864 | -48.0866 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72d6d47b-4915-3802-bee0-8c6f6d57fdbb | -11.48562 | -43.50739 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d13e2225-abc5-33d8-a53c-ec83bd34f083 | -15.39273 | -44.9715 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c8c25a48-084b-3232-ae5f-eb168ea7eba2 | -11.8192 | -44.97443 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7cabf0c-2fc8-3323-811f-715b1c96bae4 | -14.87019 | -49.71464 | 2025-10-01 04:21:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 162962f1-e92b-30a7-8b77-87e2f37a0b8d | -16.08486 | -51.02667 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8cdc91dc-91a7-3dd1-9bf2-29317700d48d | -14.19169 | -46.10701 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf4da16b-2ce1-3926-b2f8-642ea4590797 | -14.6755 | -45.29608 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b0bea83-13c8-3078-89b1-65553286ccaf | -14.89973 | -47.21236 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c5d75f5-c2c0-37a0-80cd-533612ac2962 | -11.14899 | -54.30827 | 2025-10-01 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 218d84fb-c0f5-336f-b138-1d8e71ccc99b | -12.85369 | -46.87141 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e12cbf3-4df1-3064-9602-107ece260a66 | -13.36855 | -48.11047 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e40f16d-f9e1-3698-abb7-5e888f8ba952 | -12.94791 | -48.4016 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93438249-54bd-30ab-aeee-19f9b9d093c3 | -10.92127 | -44.3072 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47ced7b5-41e7-348b-9b79-40beb60d823b | -14.0526 | -47.97015 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 58b1e0cb-27ac-3e87-8af7-1bce5df6ea4e | -15.7547 | -43.69475 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fad12e0-d3a3-3686-a14f-5d1119985c1b | -14.92209 | -47.81661 | 2025-10-01 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc7ab4f5-3175-337e-955c-ef76314ffec5 | -12.00027 | -46.65089 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 419c048a-c59e-3335-9491-fd0e3572cf7d | -11.13442 | -43.3779 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e3b7adec-3eeb-3a65-b109-200e6643f21e | -11.82647 | -44.99379 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 139f494e-6a45-3b49-a8a2-2981d8df0c38 | -14.69984 | -48.22354 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36cdada2-9bda-37dc-b61e-c2db4e677731 | -14.90287 | -48.12455 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3b75f0ce-a649-3720-85bb-f3a45049bd4c | -12.69595 | -48.5656 | 2025-10-01 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8963572a-c261-38c9-b1c9-c5d676fb72ae | -14.60713 | -48.31515 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README75.md)
