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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c806357-fd08-38f4-b611-f0ed141b8c98 | -14.32595 | -47.66649 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e8044bd-2806-31d3-9351-d794731714d4 | -12.30649 | -55.14564 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d865953-8bb8-3d27-a398-99b76d65ba59 | -13.52021 | -47.29249 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae6f1641-db56-3c8c-95ea-b59f97b0e173 | -10.07941 | -62.50146 | 2025-10-05 05:16:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f526f99-a925-3aea-afc3-5a714e73e6a9 | -12.46644 | -45.52529 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f40aad3e-e59a-34be-b721-b70e780e2b56 | -13.33267 | -47.79264 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffabbe29-3672-3058-b849-8768974ef912 | -14.68331 | -48.34442 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fda9d31b-7be6-3a0d-b442-4fcb13fc6d6e | -15.29456 | -47.3317 | 2025-10-05 05:16:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80df6b46-d019-37a5-99d6-5eae3c6047e1 | -15.57103 | -52.46973 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b5d999a-23fd-3803-81cd-9c526fa14c06 | -12.69499 | -45.8531 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fb2e085-4f2d-3a97-8172-61cdf2f6d610 | -16.01096 | -50.95509 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca520a5d-3e64-3c9b-be56-a3ab50616500 | -12.97981 | -51.04707 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3440e74d-e613-3d1e-9c5d-37a5ee3c418e | -14.26861 | -45.86863 | 2025-10-05 05:16:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd6aece9-d45f-3ed1-8130-1bd21b3f6de6 | -15.50653 | -46.85581 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f8641c8-2005-3470-8060-9e58e17be59c | -15.23589 | -49.30145 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a11ef7d-8b20-3691-a35f-57419b5fcb03 | -18.23853 | -53.33069 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 688a6133-93a8-3aa8-bbfb-cb01f71c9a36 | -15.20573 | -46.38746 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af5c1b46-eb29-3282-9577-bf1237fa9fc2 | -16.34694 | -51.46061 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b537c4e3-44c8-3c17-a64e-06a2feac593d | -15.23118 | -49.2927 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4112fd0d-d5c8-3d06-95e7-475df8df9625 | -14.68968 | -48.36124 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1fecb4d9-bf26-3aa1-a9b3-a9b106773fed | -18.25399 | -53.33084 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fa52e316-c890-3926-ad00-f56ab81b4eef | -10.65291 | -58.75872 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be4cc53b-fa96-3bcd-863b-47ddc9789d60 | -12.29907 | -55.14447 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cca12f54-8c23-3df0-a310-1d08db270c33 | -10.65014 | -58.75465 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d74ffad-deca-329c-90bb-7a61eb14b645 | -18.23738 | -53.33993 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd9fe367-0b67-3a0f-b108-1a47319c8011 | -11.72092 | -51.46682 | 2025-10-05 05:16:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1cb72c8-eed3-3de2-9015-7422c6c7f557 | -17.87694 | -57.59502 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 792ac762-64b8-3201-beec-04b6c5456a51 | -15.59289 | -52.51756 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f496a40d-9101-31eb-a1f5-9ed455e7445a | -15.76679 | -46.25861 | 2025-10-05 05:16:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eab8e8c4-9b7b-3336-9d75-7e8bfefcdb2a | -12.87089 | -47.27938 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c38b607e-8b1f-3fa3-836e-ed3703b01ac2 | -12.30669 | -55.11823 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 807ab52e-1634-389c-8cfd-bbfb69b7f754 | -13.09314 | -47.82756 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c2e8f4d7-a86f-39b2-9847-a8e60791b3c4 | -10.8372 | -57.17631 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81c7ea7a-72a1-3fb1-8af5-adc4a3beae4d | -17.88562 | -57.63374 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c032224d-9182-398f-b5d4-f5df24e8b51f | -13.51972 | -47.2968 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2a6c0c19-55a7-30a4-b92a-ecfc7cafa5ce | -18.45231 | -49.43954 | 2025-10-05 05:16:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a57edfaf-e340-3524-a6f8-b3d44293fcf7 | -14.32885 | -47.69665 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50ef0109-fb4b-3b42-8400-ea2e88bdd682 | -13.68171 | -48.05479 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96a3afd6-5c7a-3322-bb1e-c92cb657f980 | -13.347 | -48.06232 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6788a52b-8553-3231-ba3b-c8ae196f878c | -15.75879 | -46.26871 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9eb2a47-1704-3b7c-a013-c51c997ad3d5 | -13.262 | -47.60051 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 981388e4-d3f9-3336-89cb-47c26ca6ba1c | -15.22124 | -56.85438 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 433800b2-f3de-3f1c-a8b1-b883751b65c1 | -14.81001 | -59.71445 | 2025-10-05 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f24558b-b10e-3c0a-8f91-0657e7800cb1 | -15.59404 | -52.50866 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08da9a01-9005-35ec-b0a1-813bddd566cf | -10.83945 | -57.18408 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b09ecdc-14f9-38b7-a616-e58749ecb51f | -15.75923 | -46.26482 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7a4b5cb-4ebb-33d4-884b-b351385e9c46 | -13.26758 | -47.82393 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac393c78-e3c1-3b3d-b9f3-d896c0ef4e1a | -9.64925 | -67.40016 | 2025-10-05 05:16:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 991c16ac-0d79-385e-ba30-2ed114576f7c | -15.20717 | -56.82879 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb79e993-c410-3d72-bd97-dac706039de5 | -16.12802 | -53.97556 | 2025-10-05 05:16:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54714a64-7d9f-3f4a-89c9-2d604ea71770 | -18.24748 | -53.33232 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 906452da-d0f9-3f01-acd9-13676bf8d287 | -15.23329 | -49.74456 | 2025-10-05 05:16:00 | NPP-375D | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f26de5f4-6137-3ac0-83f9-35c2595cdc67 | -12.94657 | -54.72625 | 2025-10-05 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b2498a0-1b89-387d-a296-8cd98f4d9a7b | -15.30346 | -46.30848 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93601ffb-09e7-3289-9762-4e08e88ac972 | -17.84355 | -57.62716 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 471f746d-ca35-3ac2-805b-9cfa1e5b495f | -12.16809 | -51.42464 | 2025-10-05 05:16:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b32fd997-3a12-30a9-8ef2-9996e0866c7d | -16.3499 | -51.47881 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a710f45c-06d7-3d58-bedf-6df21437c932 | -14.32485 | -47.67635 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 432e48e2-6a77-3524-bb8a-34553491c371 | -12.89249 | -47.31157 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d77a4cd0-78da-3dfd-9a4c-ead73ac14e38 | -13.29114 | -47.61817 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bf3b8702-15eb-3cf2-b4e3-802fdb158088 | -16.15314 | -57.57959 | 2025-10-05 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bf56aca2-8eb1-350b-aca1-269ddbd82a89 | -12.45258 | -45.5241 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e61bfae8-9cc7-3749-9c0a-2f48ebbc9b35 | -15.23511 | -49.30809 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfeb57a2-ab88-3dd9-b458-163adac54837 | -14.87282 | -48.15142 | 2025-10-05 05:16:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20646205-09ad-38bc-b602-fb8f738d536b | -15.91031 | -48.82912 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 01f192bb-6925-3d0e-a0b8-cfb1f3f1189a | -13.7276 | -48.07999 | 2025-10-05 05:16:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eb76f0fc-2d7a-38bb-813d-ba26fac8e8ed | -13.077 | -47.90398 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 998ff7ff-897f-3da8-95dd-56cc97e8a9c7 | -12.46504 | -45.53016 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1a5a877-1d09-388d-bbfc-61fcf1f1e9b8 | -13.15755 | -50.89315 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8551067c-e16a-373d-84c4-f0e539c51313 | -17.95879 | -57.60195 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| d76e6565-058d-3aa3-9a0a-1636c057aaa5 | -19.01421 | -50.60401 | 2025-10-05 05:16:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 2018549a-641d-3f5a-b77f-6e180e794d95 | -16.15427 | -57.57198 | 2025-10-05 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9f7da717-02f3-3fb0-9cac-e61351f29c61 | -18.189 | -53.36161 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5846de1-367d-308d-936b-3e1fde766951 | -13.35069 | -48.05909 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e2864fe-17a9-3884-8875-94e6eb010a41 | -17.95054 | -57.58442 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1717cee9-2c15-30c3-b61f-aa2b88aece80 | -17.33287 | -54.19775 | 2025-10-05 05:16:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7660148d-0647-3db9-a7be-85a6fe90b971 | -13.24694 | -48.48462 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1555b343-cb42-3b69-9f16-be900fe9e47d | -16.34943 | -51.47805 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e10e59d-5bc5-3e89-ac37-fcaf6beda90e | -13.28958 | -47.62325 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 75508523-2bd9-3f94-bbea-cb9a5ae96ba5 | -14.66926 | -48.36167 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f5940606-3b47-3ecb-be4b-1f501f130840 | -12.81396 | -46.85089 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff67460c-b539-3b24-821f-da401376c213 | -14.97345 | -49.97034 | 2025-10-05 05:16:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dd11dbe-de3e-33dc-a50f-71b98e5f3a55 | -12.59876 | -48.1424 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9615ba80-3105-39b1-a420-8af11f6283a9 | -13.28847 | -47.58741 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 956ebfe0-5711-3856-9da6-0cadfb675d98 | -14.6748 | -48.36617 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5e406c31-40e3-3691-9084-92e9b57b2d68 | -14.64897 | -48.32674 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6d02a31-b634-3373-84df-3d2a7e9f95de | -13.08017 | -47.88803 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c999b0a-00fd-34bf-9680-20958e975ed4 | -13.15897 | -50.88182 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a1f3eb5-428c-30db-af89-064fb21135f8 | -15.23212 | -49.30267 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a846859d-f862-3c5a-be59-c754a3b3e6de | -16.34133 | -51.46545 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 52226251-e715-3747-9bca-64c92715cf33 | -12.9044 | -47.31788 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d9a0aabf-11a4-38e7-8b3a-26a9c2d37ca1 | -15.59005 | -52.501 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e30991e2-9696-3f57-9053-8002100b81dc | -15.39558 | -47.94447 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 921c7350-04f4-32cd-bdbb-f7aa00ea71d2 | -18.25064 | -53.35927 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7f13c10b-0d17-3f05-bf46-db6899e566c2 | -13.74069 | -47.96476 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd58d09b-ff2b-3fab-b27c-c32ea7bdad52 | -17.93357 | -57.60241 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9fa60d68-8b7f-33ef-b091-60ab36e58240 | -13.46665 | -47.2829 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa689503-3b48-3c79-bf66-4648181a48a2 | -13.28771 | -47.58327 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35b7d3c8-f7ce-38a3-8e9c-7d60f55350c8 | -13.13021 | -47.98275 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3adef733-e4c5-3125-9092-f84f2a1d6012 | -13.32667 | -47.56982 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README131.md)
