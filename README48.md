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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bbf2b7b-6d12-3c44-bfec-abd04a213407 | -16.29083 | -45.68549 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f49db29-4cd4-3fb6-b8d7-cd86d7be56ff | -17.55332 | -44.54854 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6a5f47c-0e21-3414-9bec-2d6d4c4e03bb | -11.50405 | -50.37294 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b43a6bb-a561-3924-bc6d-6ca9c527b43a | -11.95983 | -51.17838 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| beb745bb-c6a7-31fe-803d-e4fecb7108a4 | -12.8254 | -47.9675 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bfd5b51f-7f9a-3c13-9c0d-1f09c08c881d | -17.91393 | -45.71359 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d711b9cc-0cd0-3141-bb3d-ff03afdb75f8 | -12.58657 | -45.6847 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| baa90c26-2ace-3fa9-bd34-a7acd4fb7a0a | -17.33596 | -46.67338 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 366bfde2-b500-35ac-aa88-44985db11819 | -15.11281 | -48.10003 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a4ff08f4-e6b9-39e7-869e-36987aabaee4 | -13.26706 | -43.74455 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3597d605-e22f-3ad1-a55a-7dbcfd21ba7a | -17.904 | -44.59796 | 2025-09-12 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ab1d2ec-b342-3089-8054-cf7194beb5ca | -13.24789 | -43.77336 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c65d833-d774-3eb1-ad78-89968e65a601 | -15.07836 | -52.43695 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce47f3d7-90c9-36c8-9250-01382f190742 | -17.94001 | -44.44718 | 2025-09-12 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7adede2d-5cd5-3271-ac7d-4e0eb3eaf5b7 | -11.79837 | -50.56977 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42a883dd-f57f-3e7a-9abf-2d62b8ef86cd | -14.17957 | -46.17077 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d453118a-7a4e-37ed-9c5e-19a31e2e3b07 | -17.35702 | -46.6877 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32d0f65d-dbca-3502-8ade-0a3ac0726099 | -15.52902 | -48.5488 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 907a9670-99cc-3d1a-8997-a7a07cfda518 | -14.38202 | -45.18508 | 2025-09-12 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2730cb7f-dc23-3714-8714-18906eefe803 | -15.20573 | -44.05126 | 2025-09-12 04:06:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cb6f73a-e005-31b0-aa99-cff336140b96 | -12.00125 | -47.76471 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f86e2fd-8267-32d7-ab3b-68434c079ae7 | -15.09136 | -48.01293 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03790a70-56d0-35f4-aaa1-6c374fbca8b4 | -14.44788 | -47.30666 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24da758f-c46c-388f-a9b8-a4441938f4c8 | -18.48744 | -44.28339 | 2025-09-12 04:06:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e28809db-9aab-3524-8e22-299334a2ddb9 | -11.52515 | -50.60922 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| acec265e-34b5-3787-94a0-b2d3da5964c4 | -15.10639 | -48.01575 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b79917b8-454a-31ef-a6e4-0872f2bac091 | -11.22614 | -54.89582 | 2025-09-12 04:06:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b612b1f8-39f0-36b7-b775-d064f86a7630 | -18.08723 | -45.42652 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a276ddd-ab81-3bb9-a694-108b005eb401 | -11.19446 | -55.08418 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 490ab85f-2a40-36d0-aa23-ad41468b3f47 | -11.80548 | -50.57302 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56b21796-e533-331d-81aa-bb0a4f28598e | -15.796 | -52.23475 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7c8a495-cb54-335a-a9f8-2aebd15ac890 | -16.49074 | -51.97669 | 2025-09-12 04:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 030fd2b4-d0ea-3c11-8aa1-fb02b8032bb6 | -12.9329 | -48.00777 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 707001e3-52fb-3e90-afab-dca819da03f7 | -12.53761 | -44.6894 | 2025-09-12 04:06:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e60ed2a8-cf7b-3bd6-bd1f-201ff54e5604 | -11.52849 | -50.59177 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5964a901-51ac-33f0-8eab-6412a5a8e897 | -15.11886 | -48.61796 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8789850e-c4b2-3470-81c7-05dec2c27dfc | -12.53903 | -44.68715 | 2025-09-12 04:06:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6022e47-1050-368f-b700-c65667fc16bf | -12.80698 | -44.75561 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51032186-71d6-3bfb-bae8-943638894a28 | -13.78005 | -46.29189 | 2025-09-12 04:06:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0352d090-b8bb-38ef-9a45-d0ca3f6af052 | -13.35954 | -41.92138 | 2025-09-12 04:06:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b84bbc3-7aa4-3e21-b363-5b1d10ffc893 | -15.07769 | -48.01502 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 25621f72-d31e-30e2-a815-e868ec73f7ed | -14.42186 | -47.33224 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6e09f51-d4ce-32cb-a9af-9e7eda6b81f4 | -16.27984 | -45.68345 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 067d0461-60c3-3b6c-9890-0d6a85f8081e | -11.6371 | -50.58826 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35ddbe37-e6d6-3a16-87e6-8f53ba0b4c6e | -11.94798 | -51.17983 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c79d88e4-1396-3f13-82e1-b262fb83acd9 | -16.24643 | -52.65443 | 2025-09-12 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0ac6398-736c-31a3-97f3-ec9a233ad49b | -11.52609 | -50.40191 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5ab58ee8-ec56-3cb1-8687-6bbbde94bcaa | -12.87937 | -47.94877 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6098497-88e6-3084-a881-77a606425a78 | -17.55721 | -44.55615 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d282dcb1-f2e7-350f-b66f-6047a6218932 | -12.8384 | -47.9591 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46d8b2cd-cf2e-33c0-a8a7-867f2aabd950 | -16.25783 | -46.78977 | 2025-09-12 04:06:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c4bc827-eb61-392f-bf0c-866afa55469f | -11.52404 | -50.38394 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b5d22ba6-2944-3911-9351-af95929f3b08 | -12.92034 | -54.7642 | 2025-09-12 04:06:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 5736169a-baf1-37f7-862a-2de02ab0d3ac | -11.52783 | -50.59526 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 566ecc31-3c39-3ce0-9648-529a8c36ed64 | -14.60769 | -46.33745 | 2025-09-12 04:06:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1434aab-cf10-3797-a6d5-4d5a1c1470fa | -14.7787 | -43.92686 | 2025-09-12 04:06:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 86758460-3582-3f8c-8157-a43404286964 | -13.91742 | -47.97047 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58d2e0e2-997c-33a4-a660-a525f2811200 | -11.97747 | -51.147 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1dc66496-eb31-3659-b282-d451049eb1aa | -17.90678 | -44.60247 | 2025-09-12 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d6493f9-bd8f-3108-aac1-6f36b4890f17 | -12.87864 | -47.95268 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c9c695d-80d1-3cf5-bede-6590d688cb37 | -16.42147 | -49.04591 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 947bd2a3-29fc-3c1a-8f65-e22a22e539db | -12.85954 | -47.95676 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 992430b8-6055-363b-b7c0-ad216cd36621 | -11.51871 | -50.38288 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cef95f10-8bc9-30d4-9e90-ac9d68da4d29 | -14.33015 | -54.13025 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d09d7cf-0ec8-395c-abd5-8361ea1fb5e8 | -16.49685 | -51.97425 | 2025-09-12 04:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 277bf045-8286-3182-a61a-9a1f26d8a64a | -17.13813 | -48.49944 | 2025-09-12 04:06:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dcdcd9a6-22cb-3f70-8826-1a6ad2f35f07 | -12.54126 | -44.69006 | 2025-09-12 04:06:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7eefec8d-51c4-3076-9d96-d4f356043e25 | -14.32555 | -54.12473 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a500a2f2-a4d7-3781-8494-41dbad40e3c0 | -16.43409 | -49.04172 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 756a9d24-6767-31bb-bc9c-7231e76423ec | -17.47334 | -43.72197 | 2025-09-12 04:06:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16da6d50-0422-3de1-a8b4-40ddae0f7aab | -14.32273 | -54.1338 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9a71f3fd-8d05-3a3e-b2ea-8bc8782bcf51 | -15.66261 | -47.03933 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| befc2ab6-7d52-3c15-93d3-d5368533e365 | -13.98182 | -48.2128 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 729461a0-925f-335a-9b76-7f2e1f02a270 | -16.42966 | -49.04068 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62a52370-1e71-3eaf-b312-ea8d47b5a025 | -15.78426 | -52.23551 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e567e4a1-0ac4-3549-9c4d-40c1906d73d2 | -11.98929 | -51.14552 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8ce63b62-fc1b-32f4-8395-fa2e810b41df | -15.09679 | -52.46822 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4554a80-f4f6-3146-95c4-ce2f72251c0e | -11.52141 | -50.39746 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 99c99bbb-54cc-37fc-9044-dd1289f5dcb8 | -15.8006 | -52.23563 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 291349af-e3da-3b5d-99da-21dd894891fd | -15.24696 | -44.03856 | 2025-09-12 04:06:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d520601-e222-379a-adbd-267975d427f2 | -17.35614 | -46.69262 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5f0d803-7fcf-33f2-abb8-da7dd8e859d6 | -12.93143 | -48.00534 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 80fac914-d32f-3596-bcaa-a14ce5b769ed | -15.66898 | -47.07275 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f233e3d-e9b2-3ba3-b75b-ec8051464eb0 | -15.88292 | -48.18073 | 2025-09-12 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 901de001-84a9-34dd-8d95-1823e00503d9 | -14.12729 | -45.38434 | 2025-09-12 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67ba2943-00ac-374f-bb6a-702fac816dea | -16.42952 | -49.02758 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 153b8401-49d7-3edf-8218-e5e9d4e7a092 | -12.83146 | -47.95965 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74a8495f-7505-3d7d-89a2-c6b8bb3b2032 | -15.7183 | -42.19219 | 2025-09-12 04:06:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b095ea39-5c4b-30cc-922e-d53a2ad75d16 | -15.07343 | -48.01406 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2015c487-c1ef-34ed-825d-17b3923d0ed6 | -11.63438 | -50.57332 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa36db25-0f2e-37c7-ad56-f84d195ef6f2 | -17.4861 | -42.49246 | 2025-09-12 04:06:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71cb2357-88ac-3edc-bab9-2e052cac329b | -17.56545 | -44.54947 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aebda00-e4ac-3e7e-a529-a524c1581233 | -15.52993 | -48.54408 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7066dd26-b88d-3ea4-9b28-4f046f168f3e | -11.87755 | -47.53283 | 2025-09-12 04:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acd759c5-178a-3f6e-9e06-ee96ba78ad37 | -14.3233 | -54.13515 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d4714c67-e482-38de-9ca7-45356b90ca3c | -17.71902 | -46.13598 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7d5610f-78b1-3b6f-afd5-6a2d784c0d47 | -12.89136 | -47.95833 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 488808fc-7ec1-3f3b-a48e-28208326aaa4 | -12.91355 | -54.76276 | 2025-09-12 04:06:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 92489e15-1110-3d36-af3a-1150c188f4d6 | -15.60418 | -52.73603 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de545973-c0b6-3677-ba59-3fcc748658da | -11.52581 | -50.60575 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |


[Clique aqui para ver as próximas entradas](README49.md)
