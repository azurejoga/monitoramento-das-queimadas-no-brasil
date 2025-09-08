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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de88f6d5-f2c1-3075-9300-6315e4d743fc | -11.99966 | -47.76995 | 2025-09-08 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe8bdfb4-2672-34e4-ab05-ff36859b036d | -13.63609 | -43.81015 | 2025-09-08 03:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf1d3ece-5f51-32f6-8e99-f65494447986 | -13.81242 | -46.28625 | 2025-09-08 03:40:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ca21126-3255-36cc-8ad4-52a18f027ddb | -9.82619 | -47.77401 | 2025-09-08 03:40:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74b3b7b3-1bcc-3b57-b247-b73825992948 | -10.79389 | -47.7327 | 2025-09-08 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ff08b36-d04e-3ae3-99f1-52a3f9143d3f | -14.68643 | -48.19647 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa178b46-e7e3-301a-8757-8956542e2b53 | -10.29294 | -48.81683 | 2025-09-08 03:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 34bd6abd-007f-3c0d-9ba7-069509bb85a2 | -11.41023 | -43.5872 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3c2da12-fdd0-35cb-b582-73ee1011c31c | -15.93173 | -43.52724 | 2025-09-08 03:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f72e66bb-f25d-3c4a-9c6f-97c99ae2acbc | -16.28957 | -45.68701 | 2025-09-08 03:40:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11924966-4802-39e5-bcae-94940c6b8379 | -15.1795 | -47.96357 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b58402e0-42e9-34ac-9b3e-c217ba789c7e | -14.29985 | -44.8722 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67d7d486-7e97-315e-950d-cec7d715542b | -14.47277 | -48.80026 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ffcbec5-23cd-37f1-aa36-6c520bd01484 | -13.8186 | -46.25631 | 2025-09-08 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb9fc65f-b6b4-33e5-91fe-bd4f6dcb52aa | -11.42506 | -43.6524 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05c178d1-324d-31cd-81e6-3aecbaf23031 | -9.20405 | -46.04564 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e0a3867-f14f-3a30-83e2-aba262619209 | -8.9256 | -45.80922 | 2025-09-08 03:40:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a90ba3c-ed73-3d00-8864-b1b986ad2299 | -14.29376 | -44.8747 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04e26d49-adb3-3841-a7b5-0444f728561e | -9.86561 | -46.58758 | 2025-09-08 03:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97b1825d-d4b6-339f-bbdf-5ee55741659e | -14.68427 | -48.19847 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd004b21-c7a3-3800-98f4-e6912fdfc57b | -11.39476 | -43.55473 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f076b4f-c16f-33ce-980d-b52ab6c6d8de | -13.5475 | -48.11919 | 2025-09-08 03:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b04ef635-7496-3fb4-bcc0-b0af4f0d5349 | -14.73726 | -47.77292 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6e16946a-1845-3f0b-94fe-70e5d01ba4d0 | -8.70307 | -45.31638 | 2025-09-08 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a30b0ed4-f53f-392e-ab39-f691d1dba9f4 | -13.80882 | -46.27386 | 2025-09-08 03:40:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e76b3b9-ada9-3764-bb6d-8560b13be05f | -11.61408 | -47.14506 | 2025-09-08 03:40:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0f34f1b8-ec1d-3de3-9656-033eb4d0738a | -11.28223 | -46.45426 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0371ec9c-e60f-3624-a456-e2c8a5c8a1fa | -10.80166 | -47.73637 | 2025-09-08 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4fc293e-36d5-3ed9-9daf-21a898caf4da | -14.46604 | -48.79869 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 69eb64cb-29b8-35d6-a5b9-e18e3ac187e0 | -16.35782 | -43.64079 | 2025-09-08 03:40:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9cf81ec-d388-348d-b498-c4e83937d923 | -10.13793 | -46.21622 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a322adf-1837-3cd6-85b5-052670060d31 | -14.50697 | -48.80994 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d257fbb-10bd-368c-ae4f-78a0805c2597 | -9.72316 | -43.98484 | 2025-09-08 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b0df2f4c-9cc5-3a37-9cbd-524816347fd6 | -9.72421 | -43.98277 | 2025-09-08 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e2736dc-38d3-32d8-ac5f-39648f3c707e | -14.52033 | -48.77661 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f045c5c0-45bb-3982-8ea5-1a6973e31ce8 | -13.72424 | -46.89447 | 2025-09-08 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f31637b-1cb8-34ab-9053-33b760eaedf9 | -8.69696 | -45.31541 | 2025-09-08 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7f99e5be-d940-3f13-920d-4296ba83b622 | -11.28604 | -46.45465 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7f85345f-3769-3140-85c0-eb064cf3092a | -10.14621 | -46.20698 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5566a81-ab3a-355d-8ef5-9a5dacdeb05b | -11.27836 | -46.47393 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| b58c6a34-02af-3853-95c1-58710365e277 | -9.17797 | -46.06509 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b2a39f4-56c4-35eb-b2f7-0cbdb47902b2 | -9.1954 | -46.04235 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57d1afa2-7bb2-3a02-9c10-0e6479fb9e8c | -13.6412 | -43.8109 | 2025-09-08 03:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 250d0546-044d-372e-9745-8646f89259f4 | -9.19648 | -46.03668 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad26d0e4-e3b1-384f-bd46-ac01961f6f5b | -11.27936 | -46.46887 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| f92e02fb-0468-3b4b-b046-95ef624214a3 | -14.52312 | -48.76375 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 554d6eb7-8a58-395c-b6da-43279e6f5cae | -15.13004 | -48.06707 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d70a0dfa-e67e-3889-9c0b-25c777eba204 | -14.50646 | -48.80793 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8aa82fa4-a018-391f-a32b-1b982e2be6fe | -10.81956 | -47.74529 | 2025-09-08 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 883612aa-60ce-38e6-8997-ea5637d153c5 | -14.25745 | -44.94324 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41de200d-5e2b-32d1-b8fa-2147abd5273d | -13.81091 | -46.26379 | 2025-09-08 03:40:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9de99022-3b24-39ed-ab07-6084fa5d6f63 | -15.53364 | -49.24326 | 2025-09-08 03:40:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb0cd2ae-cf04-31c9-b00a-fbf8b27b8992 | -11.56635 | -44.65504 | 2025-09-08 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 029848fc-befe-391d-b8a1-acc4f74e408f | -14.81053 | -48.17637 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ed91e1f7-0cff-37b8-a5a6-704d0f990835 | -8.92851 | -45.81084 | 2025-09-08 03:40:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2aaf03df-5097-30ed-aeeb-5846f370c63f | -16.28492 | -45.68214 | 2025-09-08 03:40:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81739964-b3e0-3452-bf99-124e8bbb04fe | -15.42297 | -47.68504 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2462699-8e5e-39df-9b5b-b2df55176f8b | -10.1409 | -46.20082 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b6a1804-193b-3dac-ab71-9b39e88c9e92 | -10.28602 | -48.8137 | 2025-09-08 03:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e0725c43-c989-3acb-aaba-8b4696bca948 | -11.42231 | -43.63852 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de0feab4-1b31-3766-9493-63c26f493ea6 | -9.86454 | -46.59312 | 2025-09-08 03:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 134184d5-e4ed-3da3-acae-9be53ec915e4 | -8.6964 | -45.32005 | 2025-09-08 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 52ce78a6-8ce0-3115-b334-81e9b0d359e8 | -10.73778 | -46.33518 | 2025-09-08 03:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e17be54-0b72-379d-bca9-d7142632972a | -11.02921 | -45.94157 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c61bcac5-b463-3914-b584-5a967e071cf6 | -15.29512 | -43.38366 | 2025-09-08 03:40:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4281acf0-f72b-3262-9018-f6117b18c42a | -14.51962 | -48.78503 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 10a721fd-2abd-3fe4-8c15-282032a803fd | -9.82528 | -47.77269 | 2025-09-08 03:40:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05bb3840-1bef-37e2-8895-08dd9487d6ae | -11.82916 | -46.77455 | 2025-09-08 03:40:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9b47e66-e5eb-3744-899a-600f5ba8ff4a | -14.29047 | -44.86344 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f444830-c21b-3e2e-a62b-f22fdc18f4ec | -8.69914 | -45.30593 | 2025-09-08 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a75c0478-0bca-3d6d-abe8-1979fd849832 | -11.41135 | -43.58324 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9eec964-8da4-3258-b646-bd052533cab9 | -15.29989 | -43.38465 | 2025-09-08 03:40:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9840a4f0-5180-3168-9c3f-c46976807fdf | -14.4983 | -48.81289 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb237454-981d-372c-8c9f-3cb34c504461 | -11.14502 | -45.25332 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2765f982-512d-38e6-92db-eba4b5127fc3 | -15.3835 | -46.42738 | 2025-09-08 03:40:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97ba630f-a28c-3c3c-ba26-7b4d6f447c14 | -11.83128 | -46.77699 | 2025-09-08 03:40:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b866bee-248b-32c5-8829-18a635a23213 | -16.28389 | -45.68684 | 2025-09-08 03:40:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 243e7453-7f29-3e4a-aeb8-01ded68c0099 | -12.83059 | -47.99342 | 2025-09-08 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc1b3fcc-252a-3fb1-9074-43bb77ab12d5 | -11.62056 | -47.14626 | 2025-09-08 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 342c6c65-4739-33cd-a6a2-a3d79aeee166 | -12.1726 | -43.94782 | 2025-09-08 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88076f89-a9ea-3952-ac06-3d2f44a16dfe | -9.15003 | -46.07415 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cff9dd07-5cad-3b01-b363-5857df00c0fd | -12.00629 | -47.7714 | 2025-09-08 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2abef1fb-98d9-39c2-9038-0396b00c4cf0 | -14.51814 | -48.79169 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f31e5d8c-e640-3e25-91ae-60f29db8ba06 | -13.82604 | -43.86347 | 2025-09-08 03:40:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49cb2e4e-4a90-3678-8f8b-cac89f5d95bd | -11.41985 | -43.65136 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c146fbf1-c2c6-3e25-9d5d-70974e3f7d7c | -13.72576 | -46.88715 | 2025-09-08 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f752969-83d1-319e-8205-b6648ed47bb5 | -11.01799 | -46.03121 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de7dd172-fb37-3655-a4e6-5eede2050599 | -12.8713 | -47.98154 | 2025-09-08 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5175635-cabc-3047-b307-644c642a70c1 | -9.20939 | -46.05173 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e28b1e3-11b8-34d9-9edc-506df9e9c442 | -14.79274 | -48.10449 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d7f6bdf-ea0a-3bfb-a7c6-aa6dcc8cf003 | -13.52029 | -42.01422 | 2025-09-08 03:40:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 219ac030-36d4-3582-8548-2ec969b4275a | -14.73773 | -47.765 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6097dbb-30ff-387c-b372-adc5790a889f | -14.7905 | -48.14399 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d9035c9-37f7-38f1-8a9d-4ff32dda30d7 | -11.28308 | -46.46925 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 465e0141-0bfe-3f8a-885f-270fb9cc0f16 | -11.42691 | -43.64273 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46eb0098-904b-36a1-9b34-dc0934684065 | -13.8177 | -46.26064 | 2025-09-08 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82610c66-3e0e-3fb5-a471-b4936a977f13 | -15.16652 | -47.98975 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f764809b-12ae-3a93-a080-26aa70666c09 | -16.939 | -45.84995 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df41fe73-9ed5-3e64-8140-97992efaf176 | -18.96113 | -46.79944 | 2025-09-08 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4024fda-9628-38f4-8eae-6caad0f3411a | -15.96386 | -48.1048 | 2025-09-08 03:42:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
