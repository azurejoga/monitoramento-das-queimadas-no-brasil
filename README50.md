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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc40408b-8ea2-3ba9-a5e7-6f5a9955ac00 | -14.498 | -47.88098 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 613346d4-4f88-32ee-80b9-3cf8a1119e7d | -13.91803 | -48.45304 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c30dc1b3-7fe8-3ba7-bfc6-4ad5b9488624 | -11.36612 | -47.02026 | 2025-10-29 04:25:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae9fea9e-c19a-38c5-9c0d-121dbde031ed | -15.15555 | -47.23254 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5840115d-ad5c-33cd-afef-a6091e986e04 | -13.64149 | -46.51954 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72671ce2-08e1-3b11-ac56-72a653af2d16 | -13.3286 | -47.48227 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f97bf683-bde0-337d-8085-1466c4b2a5db | -13.64759 | -48.43527 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c8913ff-1bee-338e-8b84-0ea5b2ab635c | -14.4194 | -47.84881 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97256943-bc4a-3bcf-8cda-7ce9f4ea94e0 | -12.15872 | -47.90666 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a09a9a55-3619-3610-956a-4dce71001b2a | -14.14163 | -44.14189 | 2025-10-29 04:25:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f358d21-3463-3323-9779-d6c07c36b2ab | -13.26781 | -47.85622 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa842438-8c12-3f98-b25f-c78b8b450357 | -13.56728 | -47.15462 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cc8bd27a-3ecc-331b-b2fe-51498eb1f9ec | -13.2261 | -47.72832 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33444d96-1002-352b-a54b-32683f9be1d0 | -13.66898 | -47.17579 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b2e6d995-cb8f-318d-ae50-7f4453ddd05a | -12.58265 | -43.36807 | 2025-10-29 04:25:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d86401f-91e8-30a0-8699-d69304913007 | -15.27002 | -43.1782 | 2025-10-29 04:25:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1faca905-03ff-3fce-8967-80ef5b288c1a | -13.68394 | -47.18942 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03b38f3c-4fcf-343c-aa6b-ddcb89770a0a | -17.25885 | -45.29014 | 2025-10-29 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| babfde0f-652e-3691-b536-6704f56a2f5c | -13.65664 | -48.44477 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74a096f5-a4d6-3e85-a581-9499ac992825 | -13.30742 | -47.4638 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66fc0cd2-a2c9-3e53-a68d-d63beafad710 | -12.36802 | -50.15902 | 2025-10-29 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3153618-853f-3f57-8451-bfe2b36bc261 | -14.42337 | -47.84573 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b964b989-f193-36b4-a48a-1baa70c4ceb8 | -19.37791 | -43.64348 | 2025-10-29 04:25:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f483f836-69f0-353c-985a-f267d2080f16 | -11.70446 | -46.70008 | 2025-10-29 04:25:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8afe0ea-7cf0-3c12-a510-59ca9378eca0 | -13.67333 | -47.19139 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 636c6d61-ca9c-393e-815a-0782d66f1006 | -18.92157 | -45.03981 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d1b77be5-b19a-3f90-b710-b0298a844e2e | -14.65951 | -50.19156 | 2025-10-29 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e995465c-0dc5-3079-97d7-327a0c8d9f96 | -12.41234 | -44.70464 | 2025-10-29 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a760ca2c-6147-3fa9-901a-cbef8273ced8 | -12.69157 | -46.32389 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21a260b5-cea6-38ba-be22-370e09fd22a2 | -13.94051 | -48.44542 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d776285-a04d-35ff-8885-660662713e01 | -13.61794 | -47.59739 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2733ce82-f018-3d9c-a3a2-d9a14a65763f | -12.8073 | -47.27308 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b912353-48ff-34c1-84a1-91cf03bd1036 | -13.53191 | -47.35234 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13472f58-2353-31de-9089-a5e7f568b01f | -14.47629 | -45.25482 | 2025-10-29 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a44caa46-4846-3d68-a037-3c55184ea3f5 | -13.56675 | -47.32838 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a41bcd45-24e1-34cb-b32e-2085d714aa4a | -15.31926 | -47.85798 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d253fb05-d5eb-3260-9fa3-49903cab82ce | -13.6811 | -47.66087 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afec7bbb-0e58-3181-9ad4-c43ce013aa41 | -13.32217 | -47.43676 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f88c8cf-3d77-3199-b279-218998f7e0cd | -13.20986 | -47.05898 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4932a494-33db-35ca-9e2e-2dbabd67390f | -13.89002 | -48.51521 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 468f1901-11c9-3727-987f-ae4d3991f65a | -13.60102 | -48.42426 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e80278cc-ec21-337d-a264-c62ee09041b6 | -12.70987 | -46.31601 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8b8251ca-3560-370b-9ac9-0fdc87081bae | -13.6421 | -46.49414 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad5116b2-3e1c-372b-8fd6-b597bfe00511 | -14.48315 | -43.94547 | 2025-10-29 04:25:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bf3d66d-1a8e-3eb6-a2ea-623f013ef474 | -13.35469 | -47.67008 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9907dbba-98f7-3d42-bca5-232f014048e3 | -13.52478 | -47.3326 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04ab9ab1-978a-33af-8eaa-1e195f77c685 | -13.78786 | -52.79023 | 2025-10-29 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eace193d-25a8-373b-a9f7-2273bb21ff7b | -14.60773 | -48.40077 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f3dc248-366d-3fb3-bb68-e13582f3177b | -13.0453 | -48.4661 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cce11cd4-7c03-3a4e-8a85-6be203df6ac6 | -15.31867 | -47.86164 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e812e07-6a7e-3607-9df4-0a678071a14b | -14.98875 | -47.8694 | 2025-10-29 04:25:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 008ea85c-ca46-3e61-a7cd-b3d924243ccf | -13.6324 | -47.04797 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abca382c-ee27-312c-a62f-58d6973c2e86 | -13.54929 | -47.35126 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a60765b-14cd-37e3-85da-b2af4a24fc9e | -13.03215 | -45.83877 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0315d9a-bb92-3823-80e3-edb1aa580b5c | -14.54395 | -48.00293 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4acd599-857d-389c-93f5-71d8d6d100fb | -12.53044 | -47.53735 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3071cae6-a486-3587-b18c-31e6b2fb46aa | -12.6949 | -46.32443 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce67cbc7-805e-3f3d-8fad-999302a90218 | -13.20811 | -47.06977 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 291f538a-a778-3e29-b2f0-b67d2922a76a | -13.56341 | -47.32777 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89c8799d-7f05-3c3e-a8ff-c8b0e9c7317b | -14.35 | -46.85238 | 2025-10-29 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 564261e9-0951-335c-8993-fbbff3ef4e3a | -13.68336 | -47.19303 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f14d242-00b2-3780-8de4-e314f643dd32 | -15.15498 | -47.23613 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdea9c24-c8c4-3655-93eb-b5bc2cd4dc9c | -12.97828 | -48.38741 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 436d50ec-f00b-3e65-8165-dc56cca0538d | -14.61114 | -48.40138 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67edccf9-345d-3f80-a53d-af5d6ed801c8 | -12.75618 | -45.17157 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c957db5-cf7c-358d-a71f-ab10f8531654 | -13.32063 | -47.68726 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 894aba6a-ee94-32ed-bd2b-bbb5cd8d4de3 | -13.95715 | -48.46409 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 202aac3d-f913-3030-90d9-114720c136f9 | -15.17507 | -47.21743 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 994ca22a-a2ea-35d4-8328-89f4833c4359 | -13.2672 | -47.85999 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34b3d752-aa90-3129-8d9c-df7e4f7e0662 | -12.70159 | -46.30375 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b370c3f1-254f-3faf-8b3d-cc19de7505e6 | -13.85086 | -48.51611 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b590dec-5096-387f-9357-0f7d30e7e504 | -15.35571 | -47.91663 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63b90c5b-b0bc-3cc7-801c-b86f5dbe4a63 | -16.29712 | -46.56108 | 2025-10-29 04:25:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7c4a1b2-86c8-3f41-9e86-d2a71c398f58 | -17.26344 | -45.28297 | 2025-10-29 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd4d8740-d8e0-3589-96d7-fbff8f6f93b5 | -13.2087 | -47.06617 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0559ab3c-dedf-31d7-b488-47d59bccb03e | -13.54351 | -47.13194 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dfb76ff2-3e5b-364c-b794-29ba39bf1da0 | -13.04834 | -43.82137 | 2025-10-29 04:25:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 91d7ad83-9496-3093-9119-8078b973b3d6 | -15.74869 | -45.11418 | 2025-10-29 04:25:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbd3342c-35cd-32b6-b400-c7515d17126c | -11.02585 | -47.7977 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28f4ab8e-c58f-3125-af5a-f5b17e93c78c | -13.46623 | -47.45958 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59aafe97-83f2-3496-a7d4-8313611c36e0 | -14.32234 | -46.51531 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf15bbbb-2601-3b7a-ab60-aa5e410ac1fe | -13.93489 | -48.43659 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7e4a09e-3d61-35c8-9cf4-a55610775118 | -13.57621 | -49.60041 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e782f74-f050-36e9-a8d3-fb485026f03c | -13.74247 | -48.39662 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51a5cc41-0f93-35b1-b381-2d9424fcf72a | -11.99883 | -46.7854 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 40e31211-f1e7-34c1-bd14-8a82046531e9 | -12.40896 | -44.7041 | 2025-10-29 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcb6830b-3490-33b7-887e-7bee627d372a | -15.20443 | -47.22625 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e109b6e0-3180-3299-bda1-77f2cc0b16f8 | -11.03491 | -47.84976 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e414703-6c5c-3a19-a1a6-f502fb9c6400 | -12.69495 | -46.30264 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 81154535-9204-388b-b057-a4c301b3d9fd | -13.26513 | -47.72353 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28caabea-fac6-3f9a-bffa-86c3bd05ad3e | -12.86961 | -48.6325 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3fc701a-6d36-373c-8089-bf39875a7033 | -12.14294 | -45.2075 | 2025-10-29 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b303544a-a46a-3c8d-9ad9-b96006f5393b | -13.91892 | -48.46906 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c52809a9-bc97-39a5-b8fc-612b829de82e | -13.47 | -47.81768 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99ee0e74-39a8-3c23-aa7b-e172243a98d3 | -13.3756 | -47.41526 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b5d083e-503c-314e-bdeb-745a1044108f | -19.2407 | -43.99982 | 2025-10-29 04:25:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6f7fc7c-e387-3a76-ae9a-d95ce1326367 | -18.92215 | -45.0357 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a1cdc60b-e8a2-3559-8b13-95df53915d05 | -15.16611 | -47.23065 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d45a930-db56-33ef-a47b-27695fa0ab5d | -11.28849 | -47.56313 | 2025-10-29 04:25:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff78578c-bcdb-31d7-966a-1e87e4ee95e9 | -11.76678 | -43.21995 | 2025-10-29 04:25:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README51.md)
