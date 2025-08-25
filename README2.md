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
| 60eae35b-a13b-35b6-8363-0d1305380eac | -20.0508 | -44.479 | 2025-08-25 00:14:00 | METOP-C | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 830cffd3-586b-387b-b9b3-56ab70ff9aa8 | -7.5342 | -46.0145 | 2025-08-25 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80bbdfdb-7b4f-37e4-94af-0d53b45ebdb2 | -17.835501 | -40.123001 | 2025-08-25 00:14:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 97aecb99-656a-31b5-bb78-b36c903b7344 | -6.3098 | -43.7743 | 2025-08-25 00:14:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3999315-bb09-31ac-b7a7-8b7d0885449c | -17.5033 | -44.792702 | 2025-08-25 00:14:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 40e4c03c-c80d-3026-8954-9ecfcfab90ba | -11.6049 | -46.374298 | 2025-08-25 00:14:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d624be2e-6545-3888-a79e-3e4328d78d40 | -13.6263 | -48.164398 | 2025-08-25 00:14:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 221c9c6b-9507-3cc8-9de4-6ecb41777540 | -5.8858 | -43.399799 | 2025-08-25 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a13dbfee-74fa-3802-afc7-87dd9cc6e4a6 | -11.6095 | -46.347599 | 2025-08-25 00:14:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e415c3c-7b66-3c74-98fe-0335a8f3af55 | -14.6519 | -44.0807 | 2025-08-25 00:14:00 | METOP-C | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 3d585498-5876-351e-8bfb-f50d29b1431c | -10.6031 | -44.335098 | 2025-08-25 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 04aa8571-c286-3c7b-b615-0cb58b0aa89c | -7.8135 | -46.879398 | 2025-08-25 00:14:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccbcb4cd-bd19-3e21-80c5-f75764c45735 | -15.1045 | -48.6782 | 2025-08-25 00:14:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0496ac42-c18c-31cc-a85e-784c4cef9c6c | -5.8639 | -43.8964 | 2025-08-25 00:14:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0b7ac85-3b32-3de9-b595-8a11b5a319b6 | -14.9259 | -45.536301 | 2025-08-25 00:14:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f26cc46-8603-3653-aa67-ad4806fd91bf | -5.1097 | -43.201099 | 2025-08-25 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c07ca41e-1a82-3585-9078-37365cb4a3c9 | -6.4332 | -44.556702 | 2025-08-25 00:14:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66c6eaf4-77cc-3ab9-b938-38f343eea2a0 | -6.3081 | -43.766701 | 2025-08-25 00:14:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c30c0ae5-a515-3c53-a4f5-18fe23be86cd | -14.389 | -51.9711 | 2025-08-25 00:14:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a67cb090-0a5e-3e6d-828f-f1b529728f5c | -6.0302 | -43.995998 | 2025-08-25 00:14:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c06d999-8f67-3ebd-9874-2ccd9a3ec15f | -20.048401 | -44.4664 | 2025-08-25 00:14:00 | METOP-C | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e406a9af-34ba-3fa4-9ade-69d4b6e2abba | -11.6121 | -46.360001 | 2025-08-25 00:14:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab76ead2-6401-3a5f-ab0d-8b79ff41b46d | -10.7205 | -47.121899 | 2025-08-25 00:14:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4b68a34-15fe-38be-b106-4641f393f22f | -12.7391 | -48.1241 | 2025-08-25 00:14:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04af7899-6a09-31ee-9b44-c870a67f283d | -11.1085 | -44.783199 | 2025-08-25 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77683af7-5c50-3eb5-89d9-415fd098ed7b | -20.373301 | -46.725399 | 2025-08-25 00:14:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cc404a42-d73f-3b4e-9bb3-9bcdee36141d | -12.7586 | -44.411301 | 2025-08-25 00:14:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c626566a-11f5-3767-8e0e-1918532cfa3c | -10.0298 | -45.291199 | 2025-08-25 00:14:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 47dafe76-badd-33be-b969-c2c4dc756e4a | -19.1754 | -44.5144 | 2025-08-25 00:14:00 | METOP-C | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 19c43f16-0297-350d-a8a9-b2c6fe34d059 | -11.274 | -44.984699 | 2025-08-25 00:14:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ef12918-5e43-30ea-b86b-d81d3105141d | -13.4396 | -46.9002 | 2025-08-25 00:14:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b52db37f-e4fa-3503-95ea-a5508f520a62 | -7.8973 | -45.8941 | 2025-08-25 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae27263a-2174-3200-ba48-7a66e4dc7c80 | -17.827299 | -40.132599 | 2025-08-25 00:14:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a94e0544-16dc-3115-9912-c628c9477e33 | -5.4887 | -48.081299 | 2025-08-25 00:14:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9dca637b-20e4-3d55-b360-1cc69eb0db14 | -10.0236 | -51.082901 | 2025-08-25 00:14:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6f76212-50eb-3326-aa28-64a65bce5d88 | -20.3255 | -41.6922 | 2025-08-25 00:14:00 | METOP-C | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4cca2c90-0029-36fa-b2a3-8aeaa110f8f6 | -11.5998 | -46.349602 | 2025-08-25 00:14:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c5ec917-a6dc-3638-bf96-00b481932854 | -7.6678 | -42.6707 | 2025-08-25 00:14:00 | METOP-C | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f897789f-b370-30e7-a944-feb5c61a0d04 | -7.8513 | -49.986198 | 2025-08-25 00:14:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46de581d-535f-368f-894d-4de5204c67db | -18.0741 | -51.371799 | 2025-08-25 00:14:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09de32ab-582d-3328-a0d0-2d2afbc6c826 | -12.7508 | -44.423199 | 2025-08-25 00:14:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 905d91ae-d5c1-3f00-8961-6bcca0265364 | -11.1976 | -48.466599 | 2025-08-25 00:14:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8869a16b-c1cb-3007-8588-fe1a40d1b5d0 | -5.298 | -45.272499 | 2025-08-25 00:14:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 490379f3-dabc-373b-b423-cbe1b2874525 | -4.7769 | -45.332199 | 2025-08-25 00:14:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec0af134-64b4-3c56-855e-04eb706fcad3 | -12.7357 | -48.107201 | 2025-08-25 00:14:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1cee4edc-d5cd-32cc-a246-ce7982dff8e4 | -14.8398 | -49.203499 | 2025-08-25 00:14:00 | METOP-C | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f45befe5-e7c5-3e7d-8318-4a02a591e882 | -20.3636 | -46.7272 | 2025-08-25 00:14:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 89e16481-490f-31e6-bbb3-34da499fc820 | -6.2425 | -43.749401 | 2025-08-25 00:14:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 364b21ee-fef9-3a1c-a441-b2f545ba8fd2 | -5.8825 | -43.385201 | 2025-08-25 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da3911fa-74ff-3b31-9ecf-05d76e0cbe1f | -14.3775 | -51.905499 | 2025-08-25 00:14:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bffee03-c017-35b7-97db-441add7038a4 | -19.8151 | -42.202999 | 2025-08-25 00:14:00 | METOP-C | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e82a7ed-bbad-330e-ab46-5d39fab3cb23 | -15.7087 | -41.938 | 2025-08-25 00:14:00 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a39fa9da-8294-3374-97c9-602f19f86b96 | -3.4293 | -49.0313 | 2025-08-25 00:14:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a5bf4f3-dc77-3eb9-8808-8ec9557330b3 | -5.3078 | -45.270401 | 2025-08-25 00:14:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc2fcd80-4fe2-3a5e-b03a-107091679a6d | -10.0187 | -51.0583 | 2025-08-25 00:14:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8689df3-186e-3449-8e3c-49e0e48a9e5b | -6.131 | -43.162601 | 2025-08-25 00:14:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 5cf1fc5d-ae4a-3d51-bf9b-49056e1e4540 | -5.4866 | -41.4179 | 2025-08-25 00:14:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3a82a706-02a7-3048-a192-bb872e9656d0 | -17.500999 | -44.780602 | 2025-08-25 00:14:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e1fc8f44-d8d5-363d-9f0a-c9eadab83557 | -8.2809 | -47.249599 | 2025-08-25 00:14:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97b88d2d-4f4e-3c38-b985-1a18dd746bdf | -6.2408 | -43.741901 | 2025-08-25 00:14:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81861591-b0e5-3003-8154-69d76aeb4559 | -21.638201 | -44.0257 | 2025-08-25 00:14:00 | METOP-C | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 28987674-958e-3748-bf74-ca1854fda7cb | -3.4391 | -49.029202 | 2025-08-25 00:14:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a362a9f2-6144-3680-9159-f070d29d5218 | -9.3164 | -40.215302 | 2025-08-25 00:14:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 642f48f8-4818-3674-b528-35bda942c193 | -15.1142 | -48.676399 | 2025-08-25 00:14:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 929ea527-b99c-3cec-86be-e7a78b75acaa | -20.549601 | -41.689301 | 2025-08-25 00:14:00 | METOP-C | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2529b80-6399-3903-958a-2cf9efb2a1a0 | -11.0966 | -44.7756 | 2025-08-25 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 109ff22b-d4c2-3819-883d-5401e271b699 | -7.5909 | -45.241798 | 2025-08-25 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a028d37-e0b1-34ca-a4b5-730a75b2e0fc | -7.658 | -42.672901 | 2025-08-25 00:14:00 | METOP-C | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a192820c-37a0-3f2e-acd2-4b4ed6326521 | -5.1129 | -43.215302 | 2025-08-25 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be208e64-0b5b-3b9e-aec4-13b40bb8ae89 | -20.3764 | -46.743301 | 2025-08-25 00:14:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6908e3a5-71ea-3d4e-8188-00fe926b4ebb | -4.775 | -45.3237 | 2025-08-25 00:14:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce1628cf-1ccb-3848-b915-4a146846cc41 | -19.5714 | -41.6026 | 2025-08-25 00:14:00 | METOP-C | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8268aafd-35dc-3e8a-9d93-0e7b6e07d56e | -5.1113 | -43.208199 | 2025-08-25 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ecb938e-4256-3fd8-a7ad-e535904d03da | -9.3195 | -40.229099 | 2025-08-25 00:14:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7bd087e1-d003-33fc-aafd-3152563e947c | -7.5791 | -45.234699 | 2025-08-25 00:14:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1f87d990-25cd-309e-8368-7c2d361b9671 | -6.9173 | -43.776699 | 2025-08-25 00:14:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4e781d49-6739-378c-99c0-4d6d699c03f2 | -10.605 | -44.344101 | 2025-08-25 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f774a21a-004a-3f76-961e-5993d29e20f4 | -19.177799 | -44.526699 | 2025-08-25 00:14:00 | METOP-C | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0dfe7458-1ef8-3d19-bc5b-a47c531faf52 | -3.451 | -43.339401 | 2025-08-25 00:14:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c70a9b6c-bd16-3725-8599-b4308f7c8f5e | -20.379499 | -46.761299 | 2025-08-25 00:14:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5a16a04c-2c1e-31a1-a26c-1a6202d436da | -6.4369 | -44.5732 | 2025-08-25 00:14:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f2e10a9-303c-32d1-b292-b94748578636 | -6.5056 | -42.951302 | 2025-08-25 00:14:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df0d13dd-2f6a-3ec7-bf4c-ae5ed9f246ce | -5.3058 | -45.261799 | 2025-08-25 00:14:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0423c94c-4c5b-31cf-b926-a3dfaf32a32b | -12.7454 | -48.105301 | 2025-08-25 00:14:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5e3f680-fea3-36a1-8f5f-e34ed67068f7 | -12.7488 | -44.413399 | 2025-08-25 00:14:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 45526616-1650-32d3-8292-2609aac16b30 | -6.04 | -43.9939 | 2025-08-25 00:14:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e5833b2-fbc7-3b32-8271-bef0afe0b0ac | -5.8875 | -43.407101 | 2025-08-25 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0447beaf-f99f-3419-b40d-d17c7debf6d5 | -14.3928 | -51.936501 | 2025-08-25 00:14:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf3a1672-171e-345c-ae9c-c1dad5682c92 | -8.8087 | -45.4687 | 2025-08-25 00:14:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40c44495-39cf-33ba-ae89-135c61e7c57f | -5.1015 | -43.2104 | 2025-08-25 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fee7ed61-ba88-334c-93de-85975fb141df | -3.4355 | -49.059299 | 2025-08-25 00:14:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 669dc291-e0ff-32ae-8b5f-ab397b8501ad | -11.6284 | -46.2416 | 2025-08-25 00:14:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78a3820e-357f-3a95-9016-dc74e019260b | -19.1852 | -44.512402 | 2025-08-25 00:14:00 | METOP-C | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0d51d7f4-fc3f-3855-b1c9-600606626ea5 | -11.6429 | -46.2132 | 2025-08-25 00:14:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d075ad17-b1e1-351f-9574-195bba33f3ab | -13.6609 | -47.977402 | 2025-08-25 00:14:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de4a6267-831f-34a5-888a-d4e6c9a30023 | -14.9185 | -45.550598 | 2025-08-25 00:14:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb291a26-e530-38b3-856e-963bc8194769 | -8.2783 | -47.237099 | 2025-08-25 00:14:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79aea3c6-bb18-3ac4-9d74-d50daf636d2d | -7.6662 | -42.663502 | 2025-08-25 00:14:00 | METOP-C | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4ee7d91a-bbce-3021-88fa-b6ac758e6730 | -6.2057 | -44.136299 | 2025-08-25 00:14:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5505385d-550c-3f1d-9702-c3058afe83ff | -5.1227 | -43.2131 | 2025-08-25 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
