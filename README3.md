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
| 2346b6e1-f636-3a93-9f5a-af33707f4f1b | -10.7805 | -54.103401 | 2026-06-28 00:33:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c53098c-eaa2-3085-8607-2c616b004533 | -9.0914 | -59.373001 | 2026-06-28 00:33:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abdb13b9-1038-35a7-a4d5-ecc17a2ba845 | -12.2055 | -52.878201 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0309b9ef-7167-33df-ad74-333f6d254c9d | -11.3104 | -53.938702 | 2026-06-28 00:33:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d52ba34-05b0-39fb-904b-de5807a3d79b | -17.2934 | -42.645699 | 2026-06-28 00:33:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f347e937-d42c-333d-8719-cf96a1ed3da8 | -12.1827 | -52.868599 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0c197a2-71fa-3959-9043-4f7a15daa49f | -12.2071 | -52.8853 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98514579-8922-3feb-8e4d-731cdfdb6e3f | -12.9882 | -57.765701 | 2026-06-28 00:33:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c3f5dbd8-3bf6-3f0f-af80-da39ba46ab87 | -12.549 | -57.180801 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 251aaa09-696f-37d6-93be-f6ac3824f9b4 | -17.302999 | -42.642799 | 2026-06-28 00:33:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0f28357d-d7ef-38eb-8138-766a836ff11b | -10.3103 | -57.114498 | 2026-06-28 00:33:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5f5e7a1-b248-33f5-9074-6efd116e7ce9 | -12.2315 | -56.552601 | 2026-06-28 00:33:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a92f5d37-a5a7-378c-b169-490eac4d182c | -13.261 | -54.376301 | 2026-06-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00d18039-380c-37bd-808b-6be9304f1b67 | -12.1893 | -52.8521 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94535970-f86d-31e9-8f7e-d0d41a86f87f | -12.1771 | -57.1175 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49fc5cad-d4b6-323a-bd35-33870d07a11b | -12.0922 | -52.020802 | 2026-06-28 00:33:00 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 432ac255-af3f-3079-9fd4-d445abb4375d | -9.0882 | -59.406101 | 2026-06-28 00:33:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2199b4f9-5e17-31c6-89cc-855b914a710e | -12.0871 | -51.9986 | 2026-06-28 00:33:00 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 859fc100-bc16-3dd9-a675-a60d0fae8e31 | -12.1809 | -52.9063 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c67d3acb-3e14-39e4-b543-6bcc6fdfe448 | -12.1807 | -57.134499 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f54713a-5e50-3be2-ba60-aa2205991d9c | -11.222 | -53.820301 | 2026-06-28 00:33:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5ddee38-f06c-3ab9-9265-1bb881f1336c | -17.287399 | -42.623798 | 2026-06-28 00:33:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 28f8edb8-3802-3d4a-9546-3113ca4989e6 | -12.2023 | -52.863998 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 206f7efd-1f28-3c7c-8600-ab4070e0e7f0 | -12.1941 | -52.873402 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f71fa0c7-da79-3881-9e77-aef4b3f39966 | -12.1991 | -52.8498 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e68a2f04-68a8-371a-b257-711867b5ff4b | -9.1686 | -58.054199 | 2026-06-28 00:33:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46b5fdfc-41c6-3f1e-b35b-76e1ba4ee2a0 | -10.3085 | -57.1064 | 2026-06-28 00:33:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac3d3e01-85fa-3eda-a8c3-65354301d196 | -12.1673 | -57.119598 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5d1e4cf-6e47-3cd1-8f9d-021e26966383 | -12.1909 | -52.8592 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbaf7858-8ea5-3667-b345-6f8193f6870f | -12.1753 | -57.109001 | 2026-06-28 00:33:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 823f5132-b9fc-3857-857e-6c33c3fade55 | -11.908 | -57.104801 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83943769-d0ef-31b7-a11e-8a5319bea62e | -12.2039 | -52.871101 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cac4b362-1ca9-32c5-9889-c488b8a209b2 | -11.529 | -54.782902 | 2026-06-28 00:33:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b76ba6bc-a8a6-3a0b-b20c-8bc435170328 | -9.5993 | -56.912201 | 2026-06-28 00:33:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50ac6739-63af-324b-a407-cde95c82908d | -11.6614 | -57.2467 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd825e85-d267-3c90-80b2-e3dbc7f5c5d8 | -12.2005 | -52.901699 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b380b0d-bc37-380d-ba68-dfadff8f0840 | -12.7949 | -54.878399 | 2026-06-28 00:33:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52bd1043-d281-353d-a055-394ba9fa0c46 | -12.1777 | -52.8922 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 184ee8bb-5e0e-3e3a-9f39-8b8b25220f5c | -13.2528 | -54.385502 | 2026-06-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 113ae62e-0583-33f8-85d1-dc2f375eb662 | -12.1907 | -52.903999 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aee9887f-65d3-3dd2-9c20-9d384d51e819 | -11.6632 | -57.255199 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93edfb7f-f2a6-32cb-9153-bd61e146b995 | -9.086 | -59.395802 | 2026-06-28 00:33:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c4893a1-47a7-3043-9e76-e26c6822bd5e | -12.1891 | -52.8969 | 2026-06-28 00:33:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28928cbf-4229-3091-9949-0aa5fdb75e0b | -12.4711 | -58.478001 | 2026-06-28 00:33:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 67365942-66f7-327e-a745-8ebab880b724 | -10.2987 | -57.108601 | 2026-06-28 00:33:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ced447a7-3f41-3f75-a6ad-5d9167289272 | -12.622 | -57.873199 | 2026-06-28 00:33:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29e95214-9b5d-35a8-a595-5d9a0946e8f4 | -16.038401 | -50.550098 | 2026-06-28 00:33:00 | METOP-B | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e7d769f-ab6b-3107-9e47-f72b5032f239 | -11.6694 | -57.236099 | 2026-06-28 00:33:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a360b875-0fab-3f04-b863-639cf9ea9fbc | -18.47095 | -54.09405 | 2026-06-28 00:39:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e1c2d26d-ad9b-393d-8f96-9233a4b5c9b3 | -18.47235 | -54.10379 | 2026-06-28 00:39:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 25.7 |
| e5775fa7-281b-3164-a6a1-a9dd750d0b26 | -18.48276 | -54.11201 | 2026-06-28 00:39:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 3e75c116-dfdd-3cbd-a8d1-ea8e9a576eff | -18.48137 | -54.10235 | 2026-06-28 00:39:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 68.3 |
| caa0b6d5-17dd-304c-9e9b-3e2e1cdaee01 | -16.04053 | -50.56822 | 2026-06-28 00:39:00 | TERRA_M-M | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e56f7ced-8359-32d3-ada4-c0ddaa711383 | -12.5856 | -57.8958 | 2026-06-28 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 3d5265ab-c539-3781-9808-95bcfc2b58c0 | -12.4462 | -58.5023 | 2026-06-28 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| ef073374-082f-394b-b1a6-07cb3805caa1 | -11.6657 | -57.2536 | 2026-06-28 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| dd619d38-9823-3cd9-b4be-de0a267f2682 | -9.0796 | -59.4098 | 2026-06-28 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 5f237106-baa0-3017-805d-f7621ec5dd8b | -12.4654 | -58.481 | 2026-06-28 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| ed82d0ad-6162-3c6b-92cc-b80a181f7154 | -18.4795 | -54.1105 | 2026-06-28 00:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 61.6 |
| c3297145-48c5-37c6-83a3-39feb6d575be | -12.073 | -52.0197 | 2026-06-28 00:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| f6f24f77-dc9b-36a4-bb8e-9034582fd244 | -10.2942 | -57.1182 | 2026-06-28 00:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 5e83552c-70ee-3f3c-861d-d326ac1188e0 | -12.1773 | -57.1519 | 2026-06-28 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 42e216f8-e319-33fd-afcd-a875aa328ce6 | -12.4651 | -58.5009 | 2026-06-28 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| dadc90fa-9261-32d3-bb1a-4e57f4a386aa | -11.5241 | -54.8076 | 2026-06-28 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e6da0499-090d-3e47-a522-17a66d0e495a | -11.5243 | -54.7872 | 2026-06-28 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 6c56864c-ddef-3af3-9ec1-c949ff8a5dc4 | -12.6048 | -57.8743 | 2026-06-28 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 94067b69-bfe2-3aef-9fc2-cd3faec51902 | -10.2941 | -57.138 | 2026-06-28 00:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| a4aba59a-8c14-3a1a-a463-1113cd6c96d0 | -9.0982 | -59.4088 | 2026-06-28 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| afad7598-3058-3f23-a302-124bb77d2adb | -12.6046 | -57.8942 | 2026-06-28 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2e03dd22-cd88-3721-a916-d9af7ed4395d | -10.313 | -57.1169 | 2026-06-28 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 971ddfed-2673-3d3b-b0f1-89cdf58beae3 | -12.092 | -52.0176 | 2026-06-28 00:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 291.7 |
| 8fa268cf-8104-3db8-af9b-65c24a63307e | -17.3041 | -42.643 | 2026-06-28 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 65cbc0b7-cbb8-3fc4-b31a-44f4ed50bb99 | -12.0917 | -52.0387 | 2026-06-28 00:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 34387f8a-7719-3329-b278-73ee70b0aeb9 | -12.2222 | -56.5467 | 2026-06-28 00:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f41c33e4-14c6-361d-a398-0a1d09321a14 | -12.0923 | -51.9966 | 2026-06-28 00:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 129.3 |
| bea36ac6-a7d8-38ef-af75-f436ab33b70a | -12.1775 | -57.1319 | 2026-06-28 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 266bed31-6b54-359f-aca2-b25b250f805a | -12.5858 | -57.8759 | 2026-06-28 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 5de9665f-025d-3709-b378-e021acb60d50 | -10.3128 | -57.1367 | 2026-06-28 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| bc53623e-6854-32ef-ac6a-fdd05a4ebd32 | -12.54895 | -57.19312 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c5d1ffff-e52b-33a2-8e92-df82d9560076 | -11.93193 | -58.63332 | 2026-06-28 00:41:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 59a31a0b-3a97-3946-964c-a4f6097c4d43 | -12.20689 | -52.86908 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 115af78c-f06a-3dea-a83e-0bea5b5065fe | -13.26002 | -54.38604 | 2026-06-28 00:41:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f2fe621c-fd20-32a3-989f-d139d7132ff2 | -11.52165 | -54.80258 | 2026-06-28 00:41:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 714d50be-7204-3b2d-b77e-2e4fe44f6fcd | -12.18603 | -52.87245 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 1afe0a13-af38-3e34-95ce-fb3becaa8b1b | -12.46635 | -58.50272 | 2026-06-28 00:41:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 3f5e3e40-b35f-39ad-95c0-2243ca3cf32f | -12.54771 | -57.18406 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ade1c364-1bdc-3673-aecc-aa9c1052a0f3 | -12.44653 | -58.48143 | 2026-06-28 00:41:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a49ecb8-2124-34c1-8e03-4b6726c92213 | -12.45702 | -58.48992 | 2026-06-28 00:41:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| a9e1df01-8092-3382-bbbd-1b13d0f774b0 | -12.78823 | -54.88375 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| af7fa1ce-0be5-3ad5-a11b-47debe6b7982 | -12.0774 | -52.01509 | 2026-06-28 00:41:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 5645321c-7c93-3a52-bdc4-a61b7bb8941b | -12.10174 | -52.02036 | 2026-06-28 00:41:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5496f8cd-2d93-3985-a8b6-a2ec26206c2f | -15.44311 | -59.2308 | 2026-06-28 00:41:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8bc6d225-2c7d-33b2-b24e-ddb21fdfc2f1 | -12.27776 | -50.10938 | 2026-06-28 00:41:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 17d21da9-4caa-3d08-b198-065bd9aa26c2 | -12.44783 | -58.4912 | 2026-06-28 00:41:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6cae74a3-1735-39c3-8de8-a6cebc5535f6 | -10.78322 | -54.10458 | 2026-06-28 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5b4705fc-fd77-310f-a0a9-07d4bd6c300e | -12.18267 | -57.14147 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 8b9308d9-fca1-3134-8ecd-9bc9961650b0 | -12.07949 | -52.02411 | 2026-06-28 00:41:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| b07949f4-9196-3ba2-a664-cb1a5302275f | -11.667 | -57.26443 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 8e526dbb-31ac-374a-96c1-9f1e5ace5641 | -12.18515 | -57.15951 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 36ee668b-0de4-38e8-a9ef-2bf9f8991cbc | -11.87847 | -57.81207 | 2026-06-28 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README4.md)
