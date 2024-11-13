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
| 49214dc7-f685-3b29-ab31-34b2098b7956 | -1.28252 | -47.91354 | 2024-11-13 03:40:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b3248c68-6388-36ed-b067-13c4965086bd | -4.65925 | -47.43475 | 2024-11-13 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| eb24955b-58c5-3925-89fe-14d5873c1a9f | -4.21795 | -46.45 | 2024-11-13 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3426577-6da4-303c-a620-9983cfd2f794 | -4.64837 | -45.12714 | 2024-11-13 03:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 42c928b2-f609-3e72-be12-5917ee985205 | -4.37043 | -44.103 | 2024-11-13 03:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4422dd5f-a173-3c65-b229-5e703f3916ae | -3.95131 | -48.189 | 2024-11-13 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2901f387-dbe7-3543-acbd-713965c6a1d8 | -5.45492 | -43.25143 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99142faa-a24a-3817-baed-c500fa5bb48d | -1.27527 | -47.91228 | 2024-11-13 03:40:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ea9e6cf-560a-346a-adb4-40e413ca8d7c | -1.82608 | -47.80834 | 2024-11-13 03:40:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fe30269-c5eb-3f49-bebb-2c76093c285b | -3.25187 | -43.26137 | 2024-11-13 03:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d8c6ddfd-134d-3bbe-850d-fd13ac254bc9 | -2.71687 | -44.85592 | 2024-11-13 03:40:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da967812-6c4b-356d-bf8d-823e5c98204c | -3.03224 | -48.08271 | 2024-11-13 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddd6cf05-1d83-34be-be94-cd1fbd94bec2 | -4.20273 | -42.33058 | 2024-11-13 03:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 965af9b5-d16e-316e-a727-506a6a8b45a7 | -4.60246 | -46.94631 | 2024-11-13 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61c495a4-d761-35ef-b149-54de3963330e | -1.28284 | -47.90778 | 2024-11-13 03:40:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dfe37a0d-e069-34dc-bfab-34d5798ffabf | -5.36387 | -43.53178 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db869004-339a-3c85-87d4-fc9073382e0d | -6.75058 | -35.3295 | 2024-11-13 03:40:00 | NPP-375D | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a484f1d9-8d56-34e8-ac45-3ff3dd60f86c | -5.35347 | -43.5301 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0b1bd4c8-3d0b-34ee-b776-4c2a7b9beba6 | -3.25662 | -43.26553 | 2024-11-13 03:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f6e0910b-c9cb-3022-ac1e-8a06d4296cc2 | -7.12168 | -35.22839 | 2024-11-13 03:40:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 58c36f9a-3859-3545-b48a-080282eca361 | -3.26211 | -43.7192 | 2024-11-13 03:40:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3303104-06a8-3a22-87b1-ed0a6c039a83 | -4.6569 | -47.43342 | 2024-11-13 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b8fbdb7d-4801-30b0-a55a-e2c2f7ee762a | -1.27652 | -47.90499 | 2024-11-13 03:40:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eeaaa70e-979e-317e-b6a7-ee44447fe7f6 | -5.45543 | -43.24843 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e8e1756-dc2d-301b-96ea-40cd1603cdf4 | -4.14824 | -48.39553 | 2024-11-13 03:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12da6c66-a56d-3b74-97ad-5cd6430cf888 | -4.22349 | -46.87459 | 2024-11-13 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79bbe954-7b09-34a9-9c55-ba6aef747c3d | -3.95337 | -45.78109 | 2024-11-13 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6422fb7f-3b7c-3c44-8d5b-d6ef229c03bb | -5.35852 | -43.52702 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc2e9612-def2-39c5-a4d2-6b06b68e90e6 | -3.25083 | -43.26169 | 2024-11-13 03:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f827cac-4999-345c-945f-74d9dbf4db7b | -4.15535 | -48.39701 | 2024-11-13 03:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e83228f-b3b6-3139-b386-a1f9b7b66407 | -3.7707 | -47.48661 | 2024-11-13 03:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ecadbcd1-c3ac-326c-ae4a-fcb14617b451 | -3.95258 | -48.18183 | 2024-11-13 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26cc9ba0-d4da-3fdd-b915-4e8a7e3e6fab | -4.6468 | -45.12993 | 2024-11-13 03:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6ebcc436-ef6e-35dc-8045-efe066976272 | -4.58419 | -43.97539 | 2024-11-13 03:40:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07ba12a6-74d5-3d55-b59b-81038ea68175 | -4.07158 | -44.13921 | 2024-11-13 03:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7167d9ec-1a8d-3564-bf57-758463d1fd5c | -3.03342 | -48.07583 | 2024-11-13 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92c53719-3acb-3844-a6ac-1c4b52222e91 | -4.06898 | -45.87547 | 2024-11-13 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f81ec7a5-91f4-3767-b024-6d8455a90bb2 | -4.67746 | -44.57959 | 2024-11-13 03:40:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 99b27029-d1d1-330f-b04b-ab34df9a88ee | -4.14994 | -48.39756 | 2024-11-13 03:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ec596be0-ce85-3d56-8d03-d710d99fe8fc | -5.35922 | -43.52785 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 749c5c31-a88e-3b01-a317-d53d98f76180 | -3.25028 | -43.26492 | 2024-11-13 03:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6248b20e-8a0c-3ddf-a20b-d429175a935a | -4.65333 | -45.12703 | 2024-11-13 03:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85419d87-f202-3e1a-ad0f-d5447f0a974e | -6.30482 | -39.87786 | 2024-11-13 03:40:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fda36da3-eae9-38c7-b718-047f11281616 | -4.217 | -46.45533 | 2024-11-13 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d70e6e3-c3a0-388a-bff5-677b18fe203a | -4.77198 | -45.58158 | 2024-11-13 03:40:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a523f29-9ec0-3162-822e-36a0e7770a8c | -4.22303 | -46.4492 | 2024-11-13 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| aa42e35c-a119-3a50-b793-09c181f9cb7a | -5.35292 | -43.53321 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4394b73a-e049-365d-b659-4723629599ae | -4.14088 | -43.08356 | 2024-11-13 03:40:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b383897-8cf2-3a60-b2c7-4853e382e5c0 | -2.14415 | -46.40997 | 2024-11-13 03:40:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 09b638a2-4d16-3877-9694-f8e2d0794de5 | -3.73022 | -45.95089 | 2024-11-13 03:40:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7a83d87-6e0d-3984-83fa-2cbe1811e796 | -4.22447 | -46.8689 | 2024-11-13 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a657a7d9-603f-31a7-8117-9c71679b019f | -5.36319 | -43.53101 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21fc4ad0-26ba-38e8-860e-1d7344d19d4e | -4.21265 | -38.85399 | 2024-11-13 03:40:00 | NPP-375D | PACOTI | CEARÁ | Brasil | 2309805 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| da34a992-8c8c-3808-9094-b3dc19f13e59 | -5.35747 | -43.53326 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fc6ed83-e844-3c6f-8b96-dbd861274886 | -2.14507 | -46.40444 | 2024-11-13 03:40:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b19c7ab1-7603-3e5f-a486-c8996d4aeaf0 | -4.64764 | -45.1314 | 2024-11-13 03:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e548e123-58ae-377e-bf9c-6bbae6cb402b | -5.8006 | -35.58197 | 2024-11-13 03:40:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 119986dd-6617-39bc-b961-170bb9f7c285 | -4.65796 | -47.42741 | 2024-11-13 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3a8cb474-e046-37bc-9783-9d0973d248b6 | -4.71482 | -42.78564 | 2024-11-13 03:40:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b7107bb-ffee-342e-8c2a-af96b1fb9801 | -3.25715 | -43.26228 | 2024-11-13 03:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8b00e68a-f9da-3716-aa2b-490105758266 | -2.14599 | -46.39894 | 2024-11-13 03:40:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d36fa6c9-e475-3e2c-89ba-5c1f8448ba84 | -4.65415 | -45.12849 | 2024-11-13 03:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 21ea5383-fb25-3a5b-a37c-ddd88b727cb1 | -4.36434 | -44.10561 | 2024-11-13 03:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d5a728d-6bb4-3bc9-8c28-6c24d7ee5e3a | -4.06978 | -45.87079 | 2024-11-13 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 126bae8d-fe0d-36b4-99ea-8f974a76ea83 | -5.24527 | -37.6944 | 2024-11-13 03:40:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 00123f83-e25c-3cca-a643-5de97e2a3fcb | -3.95377 | -48.17515 | 2024-11-13 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 038e3057-a2b5-36e0-83a6-a8ac58d1adbc | -5.35799 | -43.53016 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea82d1c4-0d28-309c-ac63-18f9fd34b120 | -5.35867 | -43.53096 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc7015d9-530b-3972-9667-fa8d795c1f22 | -5.21494 | -44.67076 | 2024-11-13 03:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f3bceb1-9af3-33c7-937f-15b7b84308b0 | -4.77268 | -45.57751 | 2024-11-13 03:40:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3ab0b7d-1f69-35d5-a81b-0c0f16e38229 | -5.29616 | -36.81962 | 2024-11-13 03:40:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 39f47e80-0f76-3d58-ad0d-1def13e705d4 | -1.83323 | -47.8096 | 2024-11-13 03:40:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dccf25d-611c-3c8e-a0bf-4113dc7d1b9a | -4.22434 | -46.45107 | 2024-11-13 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6af009b2-d997-3a33-9d29-4722f0a9f711 | -4.57938 | -43.97091 | 2024-11-13 03:40:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 283d1382-582c-3f3d-a5c4-342f9edc7281 | -5.24884 | -37.69499 | 2024-11-13 03:40:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ebb83572-bb66-3cd0-81d0-3a54d9e02c8b | -4.07067 | -44.13792 | 2024-11-13 03:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9950203b-92c5-3685-8551-49617888706e | -3.70807 | -43.19431 | 2024-11-13 03:40:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce82e192-d17e-3977-adb2-aa40c9520c54 | -4.19785 | -42.32979 | 2024-11-13 03:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d46eddd0-b3bf-36b2-bf59-670b67549c6f | -3.95658 | -46.41591 | 2024-11-13 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a93e2da-b4a3-32ed-9cf3-74915dd65bde | -5.24743 | -37.6936 | 2024-11-13 03:40:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 0ff5f135-e46b-3d4c-ba6b-e3371a3e7a32 | -7.35599 | -34.91983 | 2024-11-13 03:40:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ac3dd749-9f81-318e-bd89-0da7fc4fd055 | -7.35654 | -34.91635 | 2024-11-13 03:40:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 81c3e9a0-1268-3175-8929-2545bfa51353 | -4.71063 | -42.78267 | 2024-11-13 03:40:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dca850b5-8f56-316d-9f3b-636b41214e9c | -4.71465 | -42.78932 | 2024-11-13 03:40:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9641291-22ed-3390-9698-ce757d6d59c6 | -4.66364 | -47.43454 | 2024-11-13 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e3dd393b-c1f8-34ed-af5d-fad1a0658bea | -3.95417 | -45.77644 | 2024-11-13 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ad96cab-5bda-3140-9b12-3be444bd606d | -2.72278 | -44.85689 | 2024-11-13 03:40:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 585092cf-db8a-386f-9de8-9baa368bffc9 | -4.2234 | -46.45637 | 2024-11-13 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 32b13c49-31ab-32c1-aabd-823c89c7455b | -3.95017 | -46.41492 | 2024-11-13 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96f167b9-5a0b-3216-82bf-b944a99a996e | -5.36268 | -43.53408 | 2024-11-13 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97ddf90d-13a9-3822-952b-105eec8871d7 | -4.36981 | -44.10663 | 2024-11-13 03:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 96a99f22-0939-3f3a-91cb-dd04127cfac8 | -4.68308 | -44.58063 | 2024-11-13 03:40:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6c47ed2e-baca-3129-8e35-1f615c4ec750 | -3.70753 | -43.19747 | 2024-11-13 03:40:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c60af87-f8ec-35b7-8cfa-d4a67e0dd822 | -4.61225 | -46.39467 | 2024-11-13 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec307bab-4b24-338f-858f-1307afe39916 | -4.22211 | -46.45463 | 2024-11-13 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ba5033c6-941f-3e8e-a6f6-6749183ade79 | -4.68374 | -44.5768 | 2024-11-13 03:40:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9fe57efd-2246-3990-957c-3235a525854f | -3.25555 | -43.26582 | 2024-11-13 03:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| dec14fa3-8268-38ae-967c-6950baff7feb | -4.64755 | -45.1257 | 2024-11-13 03:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da34666e-921f-3b6f-a7dc-d9c100f5fafa | -4.77447 | -45.58015 | 2024-11-13 03:40:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d7b5f56-3aea-38ab-8aa0-dd74e623ea0a | -4.21654 | -38.85443 | 2024-11-13 03:40:00 | NPP-375D | PACOTI | CEARÁ | Brasil | 2309805 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |


[Clique aqui para ver as próximas entradas](README14.md)
