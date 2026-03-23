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
| 19486e92-75d4-3fc8-9f54-abc47b0cafae | 4.37396 | -60.77053 | 2026-03-23 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8124d08f-3fef-3362-8669-fd2f4057ccc7 | -1.60796 | -53.88047 | 2026-03-23 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e847c42-a81d-3f40-b0ae-74bba61ba5e2 | 2.64898 | -61.30121 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f72873c5-c30b-3b65-b337-8f3ca19a0a6e | 2.43333 | -60.40484 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec349373-20a8-3226-bfcf-71e61dec267f | 0.99059 | -59.38796 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8ce11a5-4790-3707-8023-3be45c68208d | 0.98314 | -59.38529 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e612d50d-1219-31a4-80f7-d86dadbeb404 | 3.51373 | -61.38754 | 2026-03-23 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af01a54b-3b5e-3ad4-8d57-ef2a27c9e981 | 2.64511 | -61.30178 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 624396d0-4c4e-3576-837f-5ffabaf7f6c1 | 0.7736 | -59.86888 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d47dfc95-cfb1-3e76-83b5-b5ac9d66f229 | 1.50569 | -59.94072 | 2026-03-23 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66ca0e7f-cc51-3e93-bec9-db6e9bb90c56 | 1.97727 | -60.50812 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22f073ba-538b-3e03-bc2d-593eb3379f06 | 0.54158 | -60.26641 | 2026-03-23 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bc74dab-7881-366e-8929-321bb96d6a7e | 0.77709 | -59.86834 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 95e677cd-49b6-315e-b0de-ceaab7ab67f6 | 0.98883 | -59.37678 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a39a6e02-797c-369a-83d9-82193765d332 | 1.64471 | -60.29749 | 2026-03-23 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5e2190b-7229-3e87-b6b2-9a78453fc091 | 2.59427 | -60.59519 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dfb6fdd-5f38-396a-88e6-2cba185d4375 | 0.61486 | -59.76566 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1dd7c0a-7658-3e63-964f-7ca0d17956ab | 2.64679 | -61.28684 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 380e101c-b432-336f-95cb-e69bc2ba3a7d | 0.58024 | -59.90908 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dedb5286-4770-327d-af5f-a3f46129a041 | 3.53947 | -61.81588 | 2026-03-23 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ad2c620-0083-37c6-8be6-d7fbc551ca82 | 2.01788 | -60.67448 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d234c241-25c3-33f7-8079-572bcbfb32e5 | 0.98255 | -59.38156 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 022503d5-df7a-3fcf-94a0-c79800517a0f | 0.64104 | -59.99962 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01bc3da4-72ca-3ec3-a6df-abbe3fc5ac31 | 4.37554 | -60.77357 | 2026-03-23 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea52b020-073a-397d-880e-27cc932466bb | 2.65285 | -61.30067 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc4ee632-ba3a-3480-a613-a7377488ecbe | -1.56002 | -54.01013 | 2026-03-23 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26fae098-c880-3d40-8afc-2ce084c92808 | 4.37481 | -60.76884 | 2026-03-23 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8613ece0-b3c8-3ffc-ab46-c078eebf7b32 | 4.39693 | -60.76717 | 2026-03-23 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e602d6b6-fbc8-3ef2-8610-a31aef4301dd | 2.65212 | -61.29589 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d32fa3c1-4e5f-3392-8742-b90fe9e794b7 | 2.0591 | -60.21298 | 2026-03-23 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a758c60e-264e-390c-a1f4-9e0b454e07ac | 4.37467 | -60.7753 | 2026-03-23 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5bbe362d-dec1-31ae-8caf-23090856cb84 | 4.37861 | -60.76814 | 2026-03-23 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 16157904-71d1-3bf6-b8d2-a4033ece5c48 | 0.59419 | -60.20922 | 2026-03-23 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92c774b6-cb19-329c-8cd9-e2d7e111cab7 | 0.9854 | -59.37731 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23a87a2d-332d-3d2e-b64c-9ef7ce06eda0 | 0.75098 | -60.55673 | 2026-03-23 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e7b1e66-6950-31a4-ab45-b3eae33ddc2b | 0.98598 | -59.38103 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a140a3c-9ad9-39a4-bb5e-3515bcd6baac | 0.7795 | -59.88389 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6506c43-dbb3-3bd8-8d78-fc724080b222 | 1.35399 | -60.03666 | 2026-03-23 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8fb18f49-e40b-33f1-a201-3af37427ec5c | 0.59432 | -60.2091 | 2026-03-23 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76e31b7f-ab72-3eb4-bb8a-4ce71b8a1c92 | 2.63667 | -61.29819 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f0f751e-84c5-3ffb-86fc-b78241db1534 | -1.61173 | -53.88113 | 2026-03-23 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1307180b-ea95-3b5c-a966-ac5b80462471 | 0.7801 | -59.88778 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee8a1dda-c420-3feb-b989-cf174d561780 | 0.98657 | -59.38477 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b8d908e-6537-3094-948d-4281380a12a9 | 4.92681 | -60.55252 | 2026-03-23 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94994531-e0eb-3807-9950-ba17126887bf | 2.31628 | -60.54454 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91e4c4d6-7b31-327a-bd5e-bc59380375d6 | 3.50044 | -61.37927 | 2026-03-23 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ab01b047-96bc-3e42-af6b-3e6a31f727bc | 2.23875 | -60.28888 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c41797a6-2c62-34d4-8848-a32c6478846f | 4.66825 | -60.17546 | 2026-03-23 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26215054-026e-3927-8476-3d13106c0bf5 | 1.35461 | -60.04066 | 2026-03-23 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 210d3151-72f9-3387-8cb8-6f68ea20b3cb | 4.37777 | -60.7698 | 2026-03-23 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e89b41ee-0e44-36d3-8df0-488289b9b3e7 | 2.33122 | -61.98281 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d80d5836-75e9-3810-a1ff-a6c23e35261d | 2.65139 | -61.2911 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 429962b7-7f04-35eb-87f3-ea33bf61b505 | 1.81235 | -60.41412 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b26b9bd-d27f-3777-b43d-34c62f894e88 | 0.61321 | -59.86835 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99314df5-3f52-3d67-9281-78d45e4006e3 | 0.73272 | -59.6044 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80c95a87-dbf9-3876-a7ec-395bd4422d05 | 3.57121 | -61.71757 | 2026-03-23 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 475fa3b7-9141-3d8a-bd79-2b6e79943a87 | 2.05945 | -61.8094 | 2026-03-23 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b91dd5f5-53da-3d9b-be9b-bbc60daae06b | 0.59078 | -60.20967 | 2026-03-23 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 484851aa-8e6b-3292-8cce-8280d7b3457d | 0.76147 | -59.58452 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72a5e15e-f2c0-3332-b52d-08b8d095c014 | 0.99 | -59.38424 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce33b6eb-5394-3bc5-8059-46ae65a1d2c6 | 2.24003 | -60.28949 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d102543-4e9d-3d6c-b15c-4cdafe1283e4 | 1.64407 | -60.29337 | 2026-03-23 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a456871-2a9f-30c7-ab14-87cbb30038fb | 0.8271 | -59.39754 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0bdce36-0603-3983-a6af-3137a1d4ced1 | 3.4999 | -61.37635 | 2026-03-23 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| daa0e826-c219-38c7-9ff3-9c081feaa70a | 2.65065 | -61.28628 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f357660-05ba-39ee-a410-003903a182db | 3.5098 | -61.38813 | 2026-03-23 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93ac11ab-1165-3074-9a6a-f22632c8d4fd | 3.74629 | -59.94938 | 2026-03-23 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3607d31-dfd8-3940-8dc7-7eb4670d62a9 | 2.33333 | -60.38814 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fbec878-57c4-3cca-a477-928e62761acd | 0.51902 | -60.26162 | 2026-03-23 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e295272a-56b2-391a-91f5-2c3431cb75ee | 0.6167 | -59.86781 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 586575f1-0741-3a7a-9f81-a8030d72bb5e | 0.69406 | -60.08092 | 2026-03-23 05:16:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e57d9b46-1778-3d54-87cf-5f8e1ba18d51 | 3.94227 | -60.95813 | 2026-03-23 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f7e94597-32dc-3c0e-a6e6-b25352bfa05a | 4.65992 | -60.65793 | 2026-03-23 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5eda83ff-2108-3b91-950b-31dfbc8b1155 | 0.72251 | -60.2893 | 2026-03-23 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d37dabdd-7516-39a7-b712-595638839054 | 0.98196 | -59.37783 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf1b0a5e-300b-31e3-bbba-7e3e347273cf | 4.92228 | -60.54821 | 2026-03-23 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 653f7588-a33b-329f-8dee-8f82713e5759 | 0.6126 | -59.86448 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7888db2e-21c3-3148-b6c6-de4a396153a3 | 3.23538 | -61.19985 | 2026-03-23 05:16:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 889039c1-0e6e-37d7-af4d-4032c050f1b3 | 1.47224 | -60.05187 | 2026-03-23 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5da28ac4-e6fa-39c0-a542-141f036ce506 | 0.64879 | -60.37426 | 2026-03-23 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7c31c88-5322-3168-ad07-2b0c89a8ced9 | 2.12185 | -61.22343 | 2026-03-23 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8d7db98a-0ecf-38b9-bfa7-ea66ad60667e | 0.72188 | -60.28525 | 2026-03-23 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0cbe7b41-691b-3a2f-9b1f-344b6f59ddc2 | 0.57963 | -59.9052 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90de39d1-faf1-3350-9ec7-e4502d04fecc | 3.24407 | -60.29268 | 2026-03-23 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ff1ca33-3872-3f4a-b963-c86bb675804b | 0.05483 | -60.67876 | 2026-03-23 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3503d90f-959c-3cd3-905a-1218af791e53 | -1.55628 | -54.00954 | 2026-03-23 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb32d26f-9575-31f2-8fb7-43158824e41b | 2.63739 | -61.30298 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26a22687-3b8a-3c97-a9dc-e0fff291f2c5 | 2.64825 | -61.29645 | 2026-03-23 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ed4a857-64bc-3ea5-bb2e-5940056df95e | 1.9755 | -60.56997 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f2eb92b-a265-3151-9e7c-d1700877818f | 1.55725 | -60.17592 | 2026-03-23 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66c21880-32c6-3a13-b3d6-bab9eeecea85 | 2.94701 | -60.74246 | 2026-03-23 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68f0e130-4871-3b6a-9d1e-7aba668734d9 | 0.64042 | -59.9957 | 2026-03-23 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a42ed978-cdf2-333f-ba08-d656669215f0 | 2.23945 | -60.29327 | 2026-03-23 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 915ab1ea-4b99-3592-83f9-6c9ef35dd385 | 0.73618 | -59.60388 | 2026-03-23 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c873a56-4e81-314f-a3ae-b7f5c86fc16c | -16.42789 | -54.932 | 2026-03-23 05:21:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b19ed4dd-01ce-3566-97aa-86913fbc6f34 | -16.3134 | -58.49074 | 2026-03-23 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5a5b1053-6c6c-3467-a47e-3282f1552385 | -16.31303 | -58.49165 | 2026-03-23 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 889c498c-d306-306e-a420-881c605885a4 | -12.63959 | -52.14008 | 2026-03-23 05:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40d92e31-8a4a-3c6d-900d-51dafbfba08d | -12.6404 | -52.14005 | 2026-03-23 05:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1a0a4ee-e75f-31f0-9896-85fc2cc66ff7 | -16.43223 | -54.93266 | 2026-03-23 05:21:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
